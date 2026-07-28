import { App, PluginSettingTab, Setting } from "obsidian";
import { BROWSERS, BrowserId } from "./browsers";
import type BrowserCookieSyncPlugin from "./main";

export interface BrowserCookieSyncSettings {
	browser: BrowserId;
	profile: string;
	domainWhitelist: string[];
	alignUserAgent: boolean;
	lastSync?: { time: number; count: number };
}

export const DEFAULT_SETTINGS: BrowserCookieSyncSettings = {
	browser: "chrome",
	profile: "Default",
	domainWhitelist: [],
	alignUserAgent: true,
	lastSync: undefined,
};

export class BrowserCookieSyncSettingTab extends PluginSettingTab {
	plugin: BrowserCookieSyncPlugin;

	constructor(app: App, plugin: BrowserCookieSyncPlugin) {
		super(app, plugin);
		this.plugin = plugin;
	}

	display(): void {
		const { containerEl } = this;
		containerEl.empty();

		containerEl.createEl("h2", { text: "Browser Cookie Sync" });
		containerEl.createEl("p", {
			text:
				"把本机浏览器已登录站点的 cookie 注入 Obsidian web viewer。仅按下方白名单同步，手动触发。macOS 桌面端专用。",
			cls: "setting-item-description",
		});

		// 源浏览器
		new Setting(containerEl)
			.setName("源浏览器")
			.setDesc("从哪个浏览器读取登录态")
			.addDropdown((dd) => {
				(Object.keys(BROWSERS) as BrowserId[]).forEach((id) => {
					dd.addOption(id, BROWSERS[id].label);
				});
				dd.setValue(this.plugin.settings.browser).onChange(async (v) => {
					this.plugin.settings.browser = v as BrowserId;
					await this.plugin.saveSettings();
				});
			});

		// Profile
		new Setting(containerEl)
			.setName("Profile 目录")
			.setDesc('浏览器 profile 名，默认 "Default"。多账号时可能是 "Profile 1" 等')
			.addText((t) => {
				t.setPlaceholder("Default")
					.setValue(this.plugin.settings.profile)
					.onChange(async (v) => {
						this.plugin.settings.profile = v.trim() || "Default";
						await this.plugin.saveSettings();
					});
			});

		// 域名白名单
		new Setting(containerEl)
			.setName("域名白名单")
			.setDesc(
				"每行一个域名，如 .zhuanspirit.com 或 zhihu.com。命中该域及其所有子域的 cookie。留空则不同步任何 cookie。"
			)
			.addTextArea((ta) => {
				ta.setPlaceholder(".zhuanspirit.com\n.zhihu.com")
					.setValue(this.plugin.settings.domainWhitelist.join("\n"))
					.onChange(async (v) => {
						this.plugin.settings.domainWhitelist = v
							.split("\n")
							.map((s) => s.trim())
							.filter((s) => s.length > 0);
						await this.plugin.saveSettings();
					});
				ta.inputEl.rows = 6;
				ta.inputEl.style.width = "100%";
			});

		// UA 对齐
		new Setting(containerEl)
			.setName("对齐 User-Agent")
			.setDesc(
				"把 web viewer 的 UA 设成所选浏览器的 UA，提升 Cloudflare 等站点的成功率。"
			)
			.addToggle((tg) => {
				tg.setValue(this.plugin.settings.alignUserAgent).onChange(
					async (v) => {
						this.plugin.settings.alignUserAgent = v;
						await this.plugin.saveSettings();
					}
				);
			});

		// 立即同步
		new Setting(containerEl)
			.setName("立即同步")
			.setDesc("读取浏览器 cookie 并注入 web viewer。首次运行会弹 Keychain 授权。")
			.addButton((btn) => {
				btn.setButtonText("Sync now")
					.setCta()
					.onClick(async () => {
						btn.setDisabled(true);
						btn.setButtonText("同步中…");
						try {
							await this.plugin.syncNow();
						} finally {
							btn.setDisabled(false);
							btn.setButtonText("Sync now");
							this.display(); // 刷新 lastSync 显示
						}
					});
			});

		// 上次同步信息
		const last = this.plugin.settings.lastSync;
		if (last) {
			containerEl.createEl("p", {
				text: `上次同步：${new Date(last.time).toLocaleString()}，成功注入 ${
					last.count
				} 条 cookie。`,
				cls: "setting-item-description",
			});
		}

		// 安全提示
		const warn = containerEl.createEl("div", { cls: "setting-item-description" });
		warn.style.marginTop = "1em";
		warn.style.color = "var(--text-muted)";
		warn.createEl("strong", { text: "安全提示：" });
		warn.appendText(
			"web viewer 的 cookie 库以明文存储。任何能读你 home 目录的程序都能读到这些登录态。请只把信任的、必要的域名加入白名单。Google 账号等有设备绑定校验的站点通常无法通过搬运 cookie 登录。"
		);
	}
}
