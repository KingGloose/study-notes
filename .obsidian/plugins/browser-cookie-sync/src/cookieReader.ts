import { execFile } from "child_process";
import * as fs from "fs";
import * as os from "os";
import * as path from "path";
import { promisify } from "util";
import { BrowserId, cookieDbCandidates } from "./browsers";

const execFileP = promisify(execFile);

/** sqlite3 -json 查出来的一行原始记录 */
export interface RawCookieRow {
	host_key: string;
	name: string;
	path: string;
	is_secure: number;
	is_httponly: number;
	samesite: number; // -1 unspecified, 0 none, 1 lax, 2 strict
	expires_utc: number; // Chromium epoch: microseconds since 1601-01-01
	has_expires: number;
	is_persistent: number;
	source_scheme: number; // 1 http, 2 https
	source_port: number;
	ev_hex: string; // hex(encrypted_value)
}

/** 找到第一个存在的 cookie 库文件 */
export function resolveCookieDb(id: BrowserId, profile: string): string | null {
	for (const p of cookieDbCandidates(id, profile)) {
		if (fs.existsSync(p)) return p;
	}
	return null;
}

/**
 * 读取 cookie 库。
 * Chrome 运行时会锁库，所以先 cp 到临时文件再读。
 * 用系统 /usr/bin/sqlite3 的 -json 输出，零第三方依赖。
 */
export async function readCookies(
	dbPath: string
): Promise<RawCookieRow[]> {
	const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "bcs-"));
	const tmpDb = path.join(tmpDir, "Cookies");
	try {
		// 复制主库 + 可能存在的 WAL/SHM，保证读到最新写入
		fs.copyFileSync(dbPath, tmpDb);
		for (const ext of ["-wal", "-shm"]) {
			const side = dbPath + ext;
			if (fs.existsSync(side)) {
				try {
					fs.copyFileSync(side, tmpDb + ext);
				} catch {
					/* ignore */
				}
			}
		}

		const sql =
			"SELECT host_key, name, path, is_secure, is_httponly, samesite, " +
			"expires_utc, has_expires, is_persistent, source_scheme, source_port, " +
			"hex(encrypted_value) AS ev_hex FROM cookies;";

		const { stdout } = await execFileP(
			"/usr/bin/sqlite3",
			["-json", "-readonly", tmpDb, sql],
			{ maxBuffer: 64 * 1024 * 1024 }
		);

		const trimmed = stdout.trim();
		if (!trimmed) return [];
		const rows = JSON.parse(trimmed) as RawCookieRow[];
		return rows;
	} finally {
		// 清理临时文件
		try {
			fs.rmSync(tmpDir, { recursive: true, force: true });
		} catch {
			/* ignore */
		}
	}
}
