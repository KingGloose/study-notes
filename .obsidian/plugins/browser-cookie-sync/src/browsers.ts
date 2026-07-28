import * as os from "os";
import * as path from "path";

export type BrowserId = "chrome" | "edge" | "brave" | "arc";

export interface BrowserDef {
	id: BrowserId;
	label: string;
	/** ~/Library/Application Support 下的相对目录 */
	userDataSubdir: string;
	/** macOS Keychain 中 Safe Storage 的 service 名 */
	keychainService: string;
	/** Keychain account 名（macOS 上通常等于浏览器展示名） */
	keychainAccount: string;
}

const HOME = os.homedir();
const APP_SUPPORT = path.join(HOME, "Library", "Application Support");

export const BROWSERS: Record<BrowserId, BrowserDef> = {
	chrome: {
		id: "chrome",
		label: "Google Chrome",
		userDataSubdir: "Google/Chrome",
		keychainService: "Chrome Safe Storage",
		keychainAccount: "Chrome",
	},
	edge: {
		id: "edge",
		label: "Microsoft Edge",
		userDataSubdir: "Microsoft Edge",
		keychainService: "Microsoft Edge Safe Storage",
		keychainAccount: "Microsoft Edge",
	},
	brave: {
		id: "brave",
		label: "Brave",
		userDataSubdir: "BraveSoftware/Brave-Browser",
		keychainService: "Brave Safe Storage",
		keychainAccount: "Brave",
	},
	arc: {
		id: "arc",
		label: "Arc",
		userDataSubdir: "Arc/User Data",
		keychainService: "Arc Safe Storage",
		keychainAccount: "Arc",
	},
};

/** 浏览器用户数据根目录 */
export function userDataDir(id: BrowserId): string {
	return path.join(APP_SUPPORT, BROWSERS[id].userDataSubdir);
}

/**
 * cookie 库路径。新版 Chromium 把 Cookies 放在 <profile>/Network/Cookies，
 * 老版本直接在 <profile>/Cookies。两个都返回，读取时挑存在的那个。
 */
export function cookieDbCandidates(id: BrowserId, profile: string): string[] {
	const base = path.join(userDataDir(id), profile);
	return [
		path.join(base, "Network", "Cookies"),
		path.join(base, "Cookies"),
	];
}
