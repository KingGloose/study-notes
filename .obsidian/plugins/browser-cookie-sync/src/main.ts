import { Notice, Plugin } from "obsidian";
import { BROWSERS } from "./browsers";
import { readCookies, resolveCookieDb } from "./cookieReader";
import { deriveKey, getKeychainKey } from "./decrypt";
import { injectCookies } from "./injector";
import {
	BrowserCookieSyncSettings,
	BrowserCookieSyncSettingTab,
	DEFAULT_SETTINGS,
} from "./settings";

export default class BrowserCookieSyncPlugin extends Plugin {
	settings: BrowserCookieSyncSettings;

	async onload() {
		await this.loadSettings();

		this.addCommand({
			id: "sync-login-state-from-browser",
			name: "Sync login state from browser",
			callback: () => this.syncNow(),
		});

		this.addSettingTab(new BrowserCookieSyncSettingTab(this.app, this));
	}

	onunload() {}

	async loadSettings() {
		this.settings = Object.assign(
			{},
			DEFAULT_SETTINGS,
			await this.loadData()
		);
	}

	async saveSettings() {
		await this.saveData(this.settings);
	}

	/** 取 web viewer 用的持久 partition */
	private getWebviewPartition(): string {
		const appId = (this.app as any).appId;
		return "persist:vault-" + appId;
	}

	/** 通过 @electron/remote 拿到 web viewer 的 session */
	private getWebviewSession(): any {
		// eslint-disable-next-line @typescript-eslint/no-var-requires
		const electron = require("electron");
		const remote = electron.remote || require("@electron/remote");
		return remote.session.fromPartition(this.getWebviewPartition());
	}

	async syncNow(): Promise<void> {
		const s = this.settings;
		const browser = BROWSERS[s.browser];

		if (!s.domainWhitelist || s.domainWhitelist.length === 0) {
			new Notice("Browser Cookie Sync：域名白名单为空，未同步任何 cookie。");
			return;
		}

		// 1. 定位 cookie 库
		const dbPath = resolveCookieDb(s.browser, s.profile);
		if (!dbPath) {
			new Notice(
				`未找到 ${browser.label} 的 cookie 库（profile=${s.profile}）。请确认浏览器已安装、profile 名正确。`
			);
			return;
		}

		try {
			// 2. Keychain key → 派生 AES key
			const keychainKey = await getKeychainKey(browser);
			const derivedKey = deriveKey(keychainKey);

			// 3. 读 cookie 库
			const rows = await readCookies(dbPath);
			if (rows.length === 0) {
				new Notice(`${browser.label} cookie 库为空或读取失败。`);
				return;
			}

			// 4. 注入 web viewer session
			const session = this.getWebviewSession();
			const result = await injectCookies(
				session,
				rows,
				derivedKey,
				s.domainWhitelist
			);

			// 5. 可选 UA 对齐
			if (s.alignUserAgent) {
				try {
					const ua = session.getUserAgent();
					// 去掉 Obsidian/Electron 标识，让 UA 更像纯浏览器
					const cleaned = ua
						.split(" ")
						.filter((p: string) => !/^(obsidian|electron)/i.test(p))
						.join(" ");
					session.setUserAgent(cleaned);
				} catch {
					/* 忽略 UA 设置失败 */
				}
			}

			// 6. 记录 & 反馈
			s.lastSync = { time: Date.now(), count: result.success };
			await this.saveSettings();

			let msg =
				`Browser Cookie Sync：命中 ${result.total} 条，` +
				`成功注入 ${result.success} 条`;
			if (result.skippedDecrypt > 0) {
				msg += `，解密跳过 ${result.skippedDecrypt} 条`;
			}
			if (result.failed > 0) {
				msg += `，失败 ${result.failed} 条`;
			}
			msg += "。重新打开 web viewer 标签生效。";
			new Notice(msg, 8000);

			if (result.errors.length > 0) {
				console.warn("[browser-cookie-sync] 注入错误：", result.errors);
			}
		} catch (e: any) {
			console.error("[browser-cookie-sync] 同步失败：", e);
			new Notice(`Browser Cookie Sync 失败：${e?.message || String(e)}`, 10000);
		}
	}
}
