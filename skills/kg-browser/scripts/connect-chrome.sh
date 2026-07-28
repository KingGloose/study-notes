#!/usr/bin/env bash
#
# 把 chrome-devtools CLI daemon 连接到「用户可见的真实 Chrome」。
#
# 为什么要连真实 Chrome 而不是起一个干净实例：
#   · 天然带用户已有的登录态（知乎/内网文档等无需再配 cookie）
#   · 天然通过站点的 JS 挑战（如知乎 zse-ck）——因为就是真浏览器在跑
#   · 不做任何 cookie 注入/伪造，只读用户自己已经能看到的页面
#
# 前置：
#   1. npm i -g chrome-devtools-mcp@latest
#   2. Chrome 开启 remote debugging（见下方 guide，一次性）
#
# 用法：bash scripts/connect-chrome.sh
# 成功后即可使用 chrome-devtools 各命令（navigate_page / evaluate_script 等）。

set -euo pipefail

DEVTOOLS_FILE="${CHROME_DEVTOOLS_ACTIVE_PORT_FILE:-$HOME/Library/Application Support/Google/Chrome/DevToolsActivePort}"
CONNECT_ATTEMPTS="${CHROME_DEVTOOLS_CONNECT_ATTEMPTS:-6}"
CONNECT_DELAY_SECONDS="${CHROME_DEVTOOLS_CONNECT_DELAY_SECONDS:-2}"
MAX_RESTARTS="${CHROME_DEVTOOLS_MAX_RESTARTS:-3}"

REMOTE_DEBUGGING_GUIDE='Chrome remote debugging 手动开启步骤：
1. 打开 Chrome。
2. 访问 chrome://inspect/#remote-debugging。
3. 勾选 "Allow remote debugging for this browser instance"。
4. 彻底关闭 Chrome。
5. 重新打开 Chrome。
6. 重新执行本脚本 bash scripts/connect-chrome.sh。'

fail_with_guide() {
  local message="$1"
  echo "Error: $message" >&2
  echo "$REMOTE_DEBUGGING_GUIDE" >&2
  exit 1
}

if ! command -v chrome-devtools >/dev/null 2>&1; then
  cat >&2 <<'EOF'
Error: 未找到 chrome-devtools 命令。
请先安装 CLI：

  npm i chrome-devtools-mcp@latest -g
EOF
  exit 1
fi

read_ws_endpoint() {
  local port
  local ws_path

  if [[ ! -f "$DEVTOOLS_FILE" ]]; then
    fail_with_guide "Chrome DevToolsActivePort file not found: $DEVTOOLS_FILE"
  fi

  port="$(sed -n '1p' "$DEVTOOLS_FILE")"
  ws_path="$(sed -n '2p' "$DEVTOOLS_FILE")"

  if [[ -z "$port" || -z "$ws_path" ]]; then
    fail_with_guide "Failed to read Chrome debugging info from $DEVTOOLS_FILE"
  fi

  if ! [[ "$port" =~ ^[0-9]+$ ]]; then
    fail_with_guide "Invalid Chrome debugging port in $DEVTOOLS_FILE: $port"
  fi

  printf 'ws://127.0.0.1:%s%s\n' "$port" "$ws_path"
}

start_daemon() {
  local endpoint="$1"

  chrome-devtools stop >/dev/null 2>&1 || true
  # --no-headless：必须连有界面的真实 Chrome（headless 拿不到用户登录态）。
  if ! chrome-devtools start \
    --wsEndpoint "$endpoint" \
    --no-headless >/dev/null 2>&1; then
    return 1
  fi
}

WS_ENDPOINT="$(read_ws_endpoint)"
restart_count=1

while ((restart_count <= MAX_RESTARTS)); do
  echo "Connecting chrome-devtools CLI daemon to user Chrome:"
  echo "  $WS_ENDPOINT"

  if ! start_daemon "$WS_ENDPOINT"; then
    fail_with_guide "Failed to start chrome-devtools daemon for user Chrome"
  fi

  attempt=1
  while ((attempt <= CONNECT_ATTEMPTS)); do
    sleep "$CONNECT_DELAY_SECONDS"

    latest_endpoint="$(read_ws_endpoint)"
    if [[ "$latest_endpoint" != "$WS_ENDPOINT" ]]; then
      echo "Chrome debugging endpoint changed; reconnecting."
      WS_ENDPOINT="$latest_endpoint"
      break
    fi

    status_output="$(chrome-devtools status 2>&1 || true)"
    if [[ "$status_output" != *"$WS_ENDPOINT"* ]]; then
      ((attempt += 1))
      continue
    fi

    pages_output="$(chrome-devtools list_pages 2>&1 || true)"
    status_after_pages="$(chrome-devtools status 2>&1 || true)"
    if [[ "$pages_output" == *"## Pages"* && "$status_after_pages" == *"$WS_ENDPOINT"* ]]; then
      echo "Connected to user Chrome."
      printf '%s\n' "$pages_output"
      exit 0
    fi

    ((attempt += 1))
  done

  ((restart_count += 1))
done

chrome-devtools stop >/dev/null 2>&1 || true
fail_with_guide "User Chrome connection did not become ready after ${MAX_RESTARTS} restart attempts"
