import { execFile } from "child_process";
import * as crypto from "crypto";
import { promisify } from "util";
import { BrowserDef } from "./browsers";

const execFileP = promisify(execFile);

/**
 * 从 macOS Keychain 取浏览器的 Safe Storage key。
 * 首次调用会弹系统授权对话框。
 */
export async function getKeychainKey(browser: BrowserDef): Promise<string> {
	try {
		const { stdout } = await execFileP("security", [
			"find-generic-password",
			"-w",
			"-s",
			browser.keychainService,
			"-a",
			browser.keychainAccount,
		]);
		const key = stdout.trim();
		if (!key) {
			throw new Error(`Keychain 返回空 key（service=${browser.keychainService}）`);
		}
		return key;
	} catch (e: any) {
		// 有些浏览器 account 名不同，退一步只按 service 查
		try {
			const { stdout } = await execFileP("security", [
				"find-generic-password",
				"-w",
				"-s",
				browser.keychainService,
			]);
			const key = stdout.trim();
			if (key) return key;
		} catch {
			/* fall through */
		}
		throw new Error(
			`无法从 Keychain 取得 ${browser.label} 的 Safe Storage key：${e.message || e}`
		);
	}
}

/**
 * 由 Keychain key 派生 AES key。
 * macOS Chromium v10 方案：PBKDF2-SHA1(key, "saltysalt", 1003) → 16 bytes。
 */
export function deriveKey(keychainKey: string): Buffer {
	return crypto.pbkdf2Sync(keychainKey, "saltysalt", 1003, 16, "sha1");
}

/**
 * 解密单个 encrypted_value。
 * - 前 3 字节是版本标记（"v10"），跳过
 * - AES-128-CBC，IV = 16 个空格（0x20）
 * - 明文前 32 字节是 host_key 的 SHA-256（integrity check），需 strip
 *
 * 返回真正的 cookie 值；解密失败返回 null。
 */
export function decryptValue(
	encryptedValue: Buffer,
	derivedKey: Buffer
): string | null {
	if (encryptedValue.length === 0) {
		return null;
	}
	// v10 前缀
	const prefix = encryptedValue.subarray(0, 3).toString("latin1");
	if (prefix !== "v10") {
		// 未加密（极少数）或不支持的 v20（Windows）
		return null;
	}
	try {
		const iv = Buffer.alloc(16, 0x20); // 16 个空格
		const ciphertext = encryptedValue.subarray(3);
		const decipher = crypto.createDecipheriv("aes-128-cbc", derivedKey, iv);
		decipher.setAutoPadding(true);
		const plaintext = Buffer.concat([
			decipher.update(ciphertext),
			decipher.final(),
		]);
		// 去掉 32 字节 host hash 前缀
		if (plaintext.length < 32) {
			return plaintext.toString("utf8");
		}
		return plaintext.subarray(32).toString("utf8");
	} catch {
		return null;
	}
}
