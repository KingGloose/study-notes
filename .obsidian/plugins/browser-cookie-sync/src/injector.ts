import { RawCookieRow } from "./cookieReader";
import { decryptValue } from "./decrypt";

/** Electron cookies.set 的入参子集 */
interface ElectronCookieDetails {
	url: string;
	name: string;
	value: string;
	domain?: string;
	path?: string;
	secure?: boolean;
	httpOnly?: boolean;
	expirationDate?: number;
	sameSite?: "unspecified" | "no_restriction" | "lax" | "strict";
}

export interface InjectResult {
	total: number; // 白名单命中的 cookie 数
	success: number; // 成功注入
	failed: number; // 注入失败
	skippedDecrypt: number; // 解密失败跳过
	errors: string[];
}

/** Chromium epoch(1601)微秒 → Unix epoch 秒 */
function chromeTimeToUnixSeconds(expiresUtc: number): number {
	if (!expiresUtc || expiresUtc <= 0) return 0;
	return expiresUtc / 1_000_000 - 11_644_473_600;
}

/** samesite 数字 → Electron 字符串 */
function mapSameSite(v: number): ElectronCookieDetails["sameSite"] {
	switch (v) {
		case 0:
			return "no_restriction";
		case 1:
			return "lax";
		case 2:
			return "strict";
		default:
			return "unspecified";
	}
}

/**
 * host_key 是否命中白名单。
 * 白名单项形如 ".zhuanspirit.com" 或 "zhihu.com"，
 * 命中规则：host_key 等于该域，或是它的子域。
 */
export function matchesWhitelist(hostKey: string, whitelist: string[]): boolean {
	const h = hostKey.replace(/^\./, "").toLowerCase();
	for (const rawItem of whitelist) {
		const item = rawItem.trim().replace(/^\./, "").toLowerCase();
		if (!item) continue;
		if (h === item || h.endsWith("." + item)) return true;
	}
	return false;
}

/**
 * 由 host_key + source_scheme 构造一个合法的 https/http URL 给 Electron。
 * Electron 用 url 做 origin 校验；给一个和 domain 匹配的即可。
 */
function buildUrl(row: RawCookieRow): string {
	const scheme = row.is_secure || row.source_scheme === 2 ? "https" : "http";
	// host_key 可能以点开头（.example.com），取一个可访问主机名
	const host = row.host_key.replace(/^\./, "");
	return `${scheme}://${host}${row.path || "/"}`;
}

/**
 * 把一批原始 cookie 解密并注入指定 Electron session。
 * session 由调用方（main.ts）通过 @electron/remote 取得后传入。
 */
export async function injectCookies(
	session: any,
	rows: RawCookieRow[],
	derivedKey: Buffer,
	whitelist: string[]
): Promise<InjectResult> {
	const result: InjectResult = {
		total: 0,
		success: 0,
		failed: 0,
		skippedDecrypt: 0,
		errors: [],
	};

	for (const row of rows) {
		if (!matchesWhitelist(row.host_key, whitelist)) continue;
		result.total++;

		const ev = Buffer.from(row.ev_hex, "hex");
		const value = decryptValue(ev, derivedKey);
		if (value === null) {
			result.skippedDecrypt++;
			continue;
		}

		const details: ElectronCookieDetails = {
			url: buildUrl(row),
			name: row.name,
			value,
			// host-only cookie（host_key 不以点开头且非通配）不设 domain，
			// 让它挂在精确主机上；以点开头的设成域 cookie。
			domain: row.host_key.startsWith(".") ? row.host_key : undefined,
			path: row.path || "/",
			secure: !!row.is_secure,
			httpOnly: !!row.is_httponly,
			sameSite: mapSameSite(row.samesite),
		};

		// 持久 cookie 才带过期时间；会话 cookie 不带（也无法持久化）
		if (row.has_expires && row.is_persistent) {
			const exp = chromeTimeToUnixSeconds(row.expires_utc);
			if (exp > Date.now() / 1000) {
				details.expirationDate = exp;
			}
		}

		try {
			await session.cookies.set(details);
			result.success++;
		} catch (e: any) {
			result.failed++;
			if (result.errors.length < 10) {
				result.errors.push(
					`${row.host_key} ${row.name}: ${e?.message || String(e)}`
				);
			}
		}
	}

	return result;
}
