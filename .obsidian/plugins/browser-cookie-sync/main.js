var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => BrowserCookieSyncPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian2 = require("obsidian");

// src/browsers.ts
var os = __toESM(require("os"));
var path = __toESM(require("path"));
var HOME = os.homedir();
var APP_SUPPORT = path.join(HOME, "Library", "Application Support");
var BROWSERS = {
  chrome: {
    id: "chrome",
    label: "Google Chrome",
    userDataSubdir: "Google/Chrome",
    keychainService: "Chrome Safe Storage",
    keychainAccount: "Chrome"
  },
  edge: {
    id: "edge",
    label: "Microsoft Edge",
    userDataSubdir: "Microsoft Edge",
    keychainService: "Microsoft Edge Safe Storage",
    keychainAccount: "Microsoft Edge"
  },
  brave: {
    id: "brave",
    label: "Brave",
    userDataSubdir: "BraveSoftware/Brave-Browser",
    keychainService: "Brave Safe Storage",
    keychainAccount: "Brave"
  },
  arc: {
    id: "arc",
    label: "Arc",
    userDataSubdir: "Arc/User Data",
    keychainService: "Arc Safe Storage",
    keychainAccount: "Arc"
  }
};
function userDataDir(id) {
  return path.join(APP_SUPPORT, BROWSERS[id].userDataSubdir);
}
function cookieDbCandidates(id, profile) {
  const base = path.join(userDataDir(id), profile);
  return [
    path.join(base, "Network", "Cookies"),
    path.join(base, "Cookies")
  ];
}

// src/cookieReader.ts
var import_child_process = require("child_process");
var fs = __toESM(require("fs"));
var os2 = __toESM(require("os"));
var path2 = __toESM(require("path"));
var import_util = require("util");
var execFileP = (0, import_util.promisify)(import_child_process.execFile);
function resolveCookieDb(id, profile) {
  for (const p of cookieDbCandidates(id, profile)) {
    if (fs.existsSync(p))
      return p;
  }
  return null;
}
async function readCookies(dbPath) {
  const tmpDir = fs.mkdtempSync(path2.join(os2.tmpdir(), "bcs-"));
  const tmpDb = path2.join(tmpDir, "Cookies");
  try {
    fs.copyFileSync(dbPath, tmpDb);
    for (const ext of ["-wal", "-shm"]) {
      const side = dbPath + ext;
      if (fs.existsSync(side)) {
        try {
          fs.copyFileSync(side, tmpDb + ext);
        } catch (e) {
        }
      }
    }
    const sql = "SELECT host_key, name, path, is_secure, is_httponly, samesite, expires_utc, has_expires, is_persistent, source_scheme, source_port, hex(encrypted_value) AS ev_hex FROM cookies;";
    const { stdout } = await execFileP(
      "/usr/bin/sqlite3",
      ["-json", "-readonly", tmpDb, sql],
      { maxBuffer: 64 * 1024 * 1024 }
    );
    const trimmed = stdout.trim();
    if (!trimmed)
      return [];
    const rows = JSON.parse(trimmed);
    return rows;
  } finally {
    try {
      fs.rmSync(tmpDir, { recursive: true, force: true });
    } catch (e) {
    }
  }
}

// src/decrypt.ts
var import_child_process2 = require("child_process");
var crypto = __toESM(require("crypto"));
var import_util2 = require("util");
var execFileP2 = (0, import_util2.promisify)(import_child_process2.execFile);
async function getKeychainKey(browser) {
  try {
    const { stdout } = await execFileP2("security", [
      "find-generic-password",
      "-w",
      "-s",
      browser.keychainService,
      "-a",
      browser.keychainAccount
    ]);
    const key = stdout.trim();
    if (!key) {
      throw new Error(`Keychain \u8FD4\u56DE\u7A7A key\uFF08service=${browser.keychainService}\uFF09`);
    }
    return key;
  } catch (e) {
    try {
      const { stdout } = await execFileP2("security", [
        "find-generic-password",
        "-w",
        "-s",
        browser.keychainService
      ]);
      const key = stdout.trim();
      if (key)
        return key;
    } catch (e2) {
    }
    throw new Error(
      `\u65E0\u6CD5\u4ECE Keychain \u53D6\u5F97 ${browser.label} \u7684 Safe Storage key\uFF1A${e.message || e}`
    );
  }
}
function deriveKey(keychainKey) {
  return crypto.pbkdf2Sync(keychainKey, "saltysalt", 1003, 16, "sha1");
}
function decryptValue(encryptedValue, derivedKey) {
  if (encryptedValue.length === 0) {
    return null;
  }
  const prefix = encryptedValue.subarray(0, 3).toString("latin1");
  if (prefix !== "v10") {
    return null;
  }
  try {
    const iv = Buffer.alloc(16, 32);
    const ciphertext = encryptedValue.subarray(3);
    const decipher = crypto.createDecipheriv("aes-128-cbc", derivedKey, iv);
    decipher.setAutoPadding(true);
    const plaintext = Buffer.concat([
      decipher.update(ciphertext),
      decipher.final()
    ]);
    if (plaintext.length < 32) {
      return plaintext.toString("utf8");
    }
    return plaintext.subarray(32).toString("utf8");
  } catch (e) {
    return null;
  }
}

// src/injector.ts
function chromeTimeToUnixSeconds(expiresUtc) {
  if (!expiresUtc || expiresUtc <= 0)
    return 0;
  return expiresUtc / 1e6 - 11644473600;
}
function mapSameSite(v) {
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
function matchesWhitelist(hostKey, whitelist) {
  const h = hostKey.replace(/^\./, "").toLowerCase();
  for (const rawItem of whitelist) {
    const item = rawItem.trim().replace(/^\./, "").toLowerCase();
    if (!item)
      continue;
    if (h === item || h.endsWith("." + item))
      return true;
  }
  return false;
}
function buildUrl(row) {
  const scheme = row.is_secure || row.source_scheme === 2 ? "https" : "http";
  const host = row.host_key.replace(/^\./, "");
  return `${scheme}://${host}${row.path || "/"}`;
}
async function injectCookies(session, rows, derivedKey, whitelist) {
  const result = {
    total: 0,
    success: 0,
    failed: 0,
    skippedDecrypt: 0,
    errors: []
  };
  for (const row of rows) {
    if (!matchesWhitelist(row.host_key, whitelist))
      continue;
    result.total++;
    const ev = Buffer.from(row.ev_hex, "hex");
    const value = decryptValue(ev, derivedKey);
    if (value === null) {
      result.skippedDecrypt++;
      continue;
    }
    const details = {
      url: buildUrl(row),
      name: row.name,
      value,
      // host-only cookie（host_key 不以点开头且非通配）不设 domain，
      // 让它挂在精确主机上；以点开头的设成域 cookie。
      domain: row.host_key.startsWith(".") ? row.host_key : void 0,
      path: row.path || "/",
      secure: !!row.is_secure,
      httpOnly: !!row.is_httponly,
      sameSite: mapSameSite(row.samesite)
    };
    if (row.has_expires && row.is_persistent) {
      const exp = chromeTimeToUnixSeconds(row.expires_utc);
      if (exp > Date.now() / 1e3) {
        details.expirationDate = exp;
      }
    }
    try {
      await session.cookies.set(details);
      result.success++;
    } catch (e) {
      result.failed++;
      if (result.errors.length < 10) {
        result.errors.push(
          `${row.host_key} ${row.name}: ${(e == null ? void 0 : e.message) || String(e)}`
        );
      }
    }
  }
  return result;
}

// src/settings.ts
var import_obsidian = require("obsidian");
var DEFAULT_SETTINGS = {
  browser: "chrome",
  profile: "Default",
  domainWhitelist: [],
  alignUserAgent: true,
  lastSync: void 0
};
var BrowserCookieSyncSettingTab = class extends import_obsidian.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    containerEl.createEl("h2", { text: "Browser Cookie Sync" });
    containerEl.createEl("p", {
      text: "\u628A\u672C\u673A\u6D4F\u89C8\u5668\u5DF2\u767B\u5F55\u7AD9\u70B9\u7684 cookie \u6CE8\u5165 Obsidian web viewer\u3002\u4EC5\u6309\u4E0B\u65B9\u767D\u540D\u5355\u540C\u6B65\uFF0C\u624B\u52A8\u89E6\u53D1\u3002macOS \u684C\u9762\u7AEF\u4E13\u7528\u3002",
      cls: "setting-item-description"
    });
    new import_obsidian.Setting(containerEl).setName("\u6E90\u6D4F\u89C8\u5668").setDesc("\u4ECE\u54EA\u4E2A\u6D4F\u89C8\u5668\u8BFB\u53D6\u767B\u5F55\u6001").addDropdown((dd) => {
      Object.keys(BROWSERS).forEach((id) => {
        dd.addOption(id, BROWSERS[id].label);
      });
      dd.setValue(this.plugin.settings.browser).onChange(async (v) => {
        this.plugin.settings.browser = v;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian.Setting(containerEl).setName("Profile \u76EE\u5F55").setDesc('\u6D4F\u89C8\u5668 profile \u540D\uFF0C\u9ED8\u8BA4 "Default"\u3002\u591A\u8D26\u53F7\u65F6\u53EF\u80FD\u662F "Profile 1" \u7B49').addText((t) => {
      t.setPlaceholder("Default").setValue(this.plugin.settings.profile).onChange(async (v) => {
        this.plugin.settings.profile = v.trim() || "Default";
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian.Setting(containerEl).setName("\u57DF\u540D\u767D\u540D\u5355").setDesc(
      "\u6BCF\u884C\u4E00\u4E2A\u57DF\u540D\uFF0C\u5982 .zhuanspirit.com \u6216 zhihu.com\u3002\u547D\u4E2D\u8BE5\u57DF\u53CA\u5176\u6240\u6709\u5B50\u57DF\u7684 cookie\u3002\u7559\u7A7A\u5219\u4E0D\u540C\u6B65\u4EFB\u4F55 cookie\u3002"
    ).addTextArea((ta) => {
      ta.setPlaceholder(".zhuanspirit.com\n.zhihu.com").setValue(this.plugin.settings.domainWhitelist.join("\n")).onChange(async (v) => {
        this.plugin.settings.domainWhitelist = v.split("\n").map((s) => s.trim()).filter((s) => s.length > 0);
        await this.plugin.saveSettings();
      });
      ta.inputEl.rows = 6;
      ta.inputEl.style.width = "100%";
    });
    new import_obsidian.Setting(containerEl).setName("\u5BF9\u9F50 User-Agent").setDesc(
      "\u628A web viewer \u7684 UA \u8BBE\u6210\u6240\u9009\u6D4F\u89C8\u5668\u7684 UA\uFF0C\u63D0\u5347 Cloudflare \u7B49\u7AD9\u70B9\u7684\u6210\u529F\u7387\u3002"
    ).addToggle((tg) => {
      tg.setValue(this.plugin.settings.alignUserAgent).onChange(
        async (v) => {
          this.plugin.settings.alignUserAgent = v;
          await this.plugin.saveSettings();
        }
      );
    });
    new import_obsidian.Setting(containerEl).setName("\u7ACB\u5373\u540C\u6B65").setDesc("\u8BFB\u53D6\u6D4F\u89C8\u5668 cookie \u5E76\u6CE8\u5165 web viewer\u3002\u9996\u6B21\u8FD0\u884C\u4F1A\u5F39 Keychain \u6388\u6743\u3002").addButton((btn) => {
      btn.setButtonText("Sync now").setCta().onClick(async () => {
        btn.setDisabled(true);
        btn.setButtonText("\u540C\u6B65\u4E2D\u2026");
        try {
          await this.plugin.syncNow();
        } finally {
          btn.setDisabled(false);
          btn.setButtonText("Sync now");
          this.display();
        }
      });
    });
    const last = this.plugin.settings.lastSync;
    if (last) {
      containerEl.createEl("p", {
        text: `\u4E0A\u6B21\u540C\u6B65\uFF1A${new Date(last.time).toLocaleString()}\uFF0C\u6210\u529F\u6CE8\u5165 ${last.count} \u6761 cookie\u3002`,
        cls: "setting-item-description"
      });
    }
    const warn = containerEl.createEl("div", { cls: "setting-item-description" });
    warn.style.marginTop = "1em";
    warn.style.color = "var(--text-muted)";
    warn.createEl("strong", { text: "\u5B89\u5168\u63D0\u793A\uFF1A" });
    warn.appendText(
      "web viewer \u7684 cookie \u5E93\u4EE5\u660E\u6587\u5B58\u50A8\u3002\u4EFB\u4F55\u80FD\u8BFB\u4F60 home \u76EE\u5F55\u7684\u7A0B\u5E8F\u90FD\u80FD\u8BFB\u5230\u8FD9\u4E9B\u767B\u5F55\u6001\u3002\u8BF7\u53EA\u628A\u4FE1\u4EFB\u7684\u3001\u5FC5\u8981\u7684\u57DF\u540D\u52A0\u5165\u767D\u540D\u5355\u3002Google \u8D26\u53F7\u7B49\u6709\u8BBE\u5907\u7ED1\u5B9A\u6821\u9A8C\u7684\u7AD9\u70B9\u901A\u5E38\u65E0\u6CD5\u901A\u8FC7\u642C\u8FD0 cookie \u767B\u5F55\u3002"
    );
  }
};

// src/main.ts
var BrowserCookieSyncPlugin = class extends import_obsidian2.Plugin {
  async onload() {
    await this.loadSettings();
    this.addCommand({
      id: "sync-login-state-from-browser",
      name: "Sync login state from browser",
      callback: () => this.syncNow()
    });
    this.addSettingTab(new BrowserCookieSyncSettingTab(this.app, this));
  }
  onunload() {
  }
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
  getWebviewPartition() {
    const appId = this.app.appId;
    return "persist:vault-" + appId;
  }
  /** 通过 @electron/remote 拿到 web viewer 的 session */
  getWebviewSession() {
    const electron = require("electron");
    const remote = electron.remote || require("@electron/remote");
    return remote.session.fromPartition(this.getWebviewPartition());
  }
  async syncNow() {
    const s = this.settings;
    const browser = BROWSERS[s.browser];
    if (!s.domainWhitelist || s.domainWhitelist.length === 0) {
      new import_obsidian2.Notice("Browser Cookie Sync\uFF1A\u57DF\u540D\u767D\u540D\u5355\u4E3A\u7A7A\uFF0C\u672A\u540C\u6B65\u4EFB\u4F55 cookie\u3002");
      return;
    }
    const dbPath = resolveCookieDb(s.browser, s.profile);
    if (!dbPath) {
      new import_obsidian2.Notice(
        `\u672A\u627E\u5230 ${browser.label} \u7684 cookie \u5E93\uFF08profile=${s.profile}\uFF09\u3002\u8BF7\u786E\u8BA4\u6D4F\u89C8\u5668\u5DF2\u5B89\u88C5\u3001profile \u540D\u6B63\u786E\u3002`
      );
      return;
    }
    try {
      const keychainKey = await getKeychainKey(browser);
      const derivedKey = deriveKey(keychainKey);
      const rows = await readCookies(dbPath);
      if (rows.length === 0) {
        new import_obsidian2.Notice(`${browser.label} cookie \u5E93\u4E3A\u7A7A\u6216\u8BFB\u53D6\u5931\u8D25\u3002`);
        return;
      }
      const session = this.getWebviewSession();
      const result = await injectCookies(
        session,
        rows,
        derivedKey,
        s.domainWhitelist
      );
      if (s.alignUserAgent) {
        try {
          const ua = session.getUserAgent();
          const cleaned = ua.split(" ").filter((p) => !/^(obsidian|electron)/i.test(p)).join(" ");
          session.setUserAgent(cleaned);
        } catch (e) {
        }
      }
      s.lastSync = { time: Date.now(), count: result.success };
      await this.saveSettings();
      let msg = `Browser Cookie Sync\uFF1A\u547D\u4E2D ${result.total} \u6761\uFF0C\u6210\u529F\u6CE8\u5165 ${result.success} \u6761`;
      if (result.skippedDecrypt > 0) {
        msg += `\uFF0C\u89E3\u5BC6\u8DF3\u8FC7 ${result.skippedDecrypt} \u6761`;
      }
      if (result.failed > 0) {
        msg += `\uFF0C\u5931\u8D25 ${result.failed} \u6761`;
      }
      msg += "\u3002\u91CD\u65B0\u6253\u5F00 web viewer \u6807\u7B7E\u751F\u6548\u3002";
      new import_obsidian2.Notice(msg, 8e3);
      if (result.errors.length > 0) {
        console.warn("[browser-cookie-sync] \u6CE8\u5165\u9519\u8BEF\uFF1A", result.errors);
      }
    } catch (e) {
      console.error("[browser-cookie-sync] \u540C\u6B65\u5931\u8D25\uFF1A", e);
      new import_obsidian2.Notice(`Browser Cookie Sync \u5931\u8D25\uFF1A${(e == null ? void 0 : e.message) || String(e)}`, 1e4);
    }
  }
};
