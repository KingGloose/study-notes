#!/usr/bin/env bash
# 学习笔记 skills 一键安装 / 迁移脚本
#
# 支持：macOS (Apple Silicon / Intel) 与 Linux / Windows WSL2
# 用法：
#   bash install.sh              # 完整安装（推荐首次/迁移新机器）
#   bash install.sh --minimal    # 只装基础+底层库（不装文档/ASR 重依赖）
#   bash install.sh --no-link    # 跳过注册到全局（不建软链）
#   bash install.sh --help
#
# 幂等：可重复运行，已装的会跳过或升级。

set -uo pipefail

SKILLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SKILLS_DIR/.." && pwd)"
PY_VERSION="3.12"
LINK_NAME="kg"

MINIMAL=0
DO_LINK=1
for arg in "$@"; do
  case "$arg" in
    --minimal) MINIMAL=1 ;;
    --no-link) DO_LINK=0 ;;
    -h|--help)
      sed -n '2,12p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "未知参数: $arg（用 --help 查看用法）"; exit 1 ;;
  esac
done

# ---------- 输出辅助 ----------
info()  { printf '\033[36m[..]\033[0m %s\n' "$*"; }
ok()    { printf '\033[32m[ok]\033[0m %s\n' "$*"; }
warn()  { printf '\033[33m[!]\033[0m %s\n' "$*"; }
fail()  { printf '\033[31m[x]\033[0m %s\n' "$*" >&2; }
step()  { printf '\n\033[1m=== %s ===\033[0m\n' "$*"; }

# ---------- 平台探测 ----------
step "1/6 平台探测"
OS="$(uname -s)"
ARCH="$(uname -m)"
IS_WSL=0
if [ "$OS" = "Linux" ] && grep -qi microsoft /proc/version 2>/dev/null; then
  IS_WSL=1
fi

case "$OS" in
  Darwin)
    PLATFORM="macOS"
    if [ "$ARCH" = "arm64" ]; then
      ASR_REQ="asr-mac.txt"; ASR_DESC="mlx-whisper (Apple Silicon / Metal GPU)"
    else
      ASR_REQ="asr-linux.txt"; ASR_DESC="faster-whisper (Intel Mac，仅 CPU)"
      warn "Intel Mac 无 Metal 加速，ASR 会比较慢"
    fi
    FFMPEG_HINT="brew install ffmpeg"
    ;;
  Linux)
    [ "$IS_WSL" = 1 ] && PLATFORM="Windows WSL2" || PLATFORM="Linux"
    ASR_REQ="asr-linux.txt"; ASR_DESC="faster-whisper (有 NVIDIA GPU 走 CUDA，否则 CPU)"
    FFMPEG_HINT="sudo apt install -y ffmpeg"
    ;;
  *)
    fail "不支持的平台: $OS（本脚本支持 macOS / Linux / WSL2）"
    fail "纯 Windows 请参考 README.md 手动安装"
    exit 1 ;;
esac
ok "平台: $PLATFORM ($ARCH)"
ok "ASR 后端: $ASR_DESC"

# ---------- 依赖检查 ----------
step "2/6 检查前置工具"
if ! command -v uv >/dev/null 2>&1; then
  fail "未找到 uv（Python 环境管理器）"
  echo "    安装方式: curl -LsSf https://astral.sh/uv/install.sh | sh"
  echo "    安装后重开终端或 source ~/.bashrc，再运行本脚本"
  exit 1
fi
ok "uv $(uv --version 2>/dev/null | awk '{print $2}')"

if command -v ffmpeg >/dev/null 2>&1; then
  ok "ffmpeg 已安装"
else
  warn "ffmpeg 未安装（视频抽音轨 / 音频转码需要它）"
  echo "    请手动执行: $FFMPEG_HINT"
  echo "    不影响本次安装，但用到音视频转写时会报错"
fi

# ---------- Python 环境 ----------
step "3/6 创建统一虚拟环境"
cd "$SKILLS_DIR"
info "确保 Python $PY_VERSION 可用"
uv python install "$PY_VERSION" 2>&1 | grep -viE "already installed" || true

if [ -d .venv ]; then
  ok ".venv 已存在，复用"
else
  uv venv --python "$PY_VERSION" || { fail "创建 venv 失败"; exit 1; }
  ok "已创建 .venv (Python $PY_VERSION)"
fi

VENV_PY="$SKILLS_DIR/.venv/bin/python"
[ -x "$VENV_PY" ] || { fail "venv 里找不到 python: $VENV_PY"; exit 1; }
export VIRTUAL_ENV="$SKILLS_DIR/.venv"

# ---------- 安装依赖 ----------
step "4/6 安装依赖"
pipi() {  # pipi <requirements 文件名> <说明>
  info "安装 $2"
  if uv pip install -q -r "requirements/$1"; then
    ok "$2"
  else
    fail "$2 安装失败"
    return 1
  fi
}

pipi base.txt "基础依赖（HTTP / HTML 解析）" || exit 1

info "安装底层库 kg-media-to-text（editable）"
if uv pip install -q -e ./kg-media-to-text; then
  ok "底层库（可编辑模式，改代码立即生效）"
else
  fail "底层库安装失败"; exit 1
fi

pipi bilibili.txt "B 站支持" || true
pipi wechat.txt   "微信公众号支持" || true

if [ "$MINIMAL" = 1 ]; then
  warn "--minimal：跳过文档处理（Docling，约 1GB）和 ASR（Whisper 模型约 1.5GB）"
  warn "以后需要时再执行："
  echo "    uv pip install -r requirements/doc.txt"
  echo "    uv pip install -r requirements/$ASR_REQ"
else
  pipi doc.txt "文档处理（Docling + MarkItDown，较大，首次运行还会下模型）" || true
  pipi "$ASR_REQ" "音视频转写 - ${ASR_DESC}" || true
fi

# ---------- 注册到全局 ----------
step "5/6 注册到全局（让任何目录都能用 kg-* skill）"
if [ "$DO_LINK" = 0 ]; then
  warn "--no-link：跳过软链"
else
  AGENTS_SKILLS="$HOME/.agents/skills"
  mkdir -p "$AGENTS_SKILLS"
  TARGET="$AGENTS_SKILLS/$LINK_NAME"
  if [ -L "$TARGET" ]; then
    CURRENT="$(readlink "$TARGET")"
    if [ "$CURRENT" = "$SKILLS_DIR" ]; then
      ok "软链已存在且正确: $TARGET -> $SKILLS_DIR"
    else
      warn "软链已存在但指向别处: $CURRENT"
      ln -sfn "$SKILLS_DIR" "$TARGET" && ok "已更新指向 $SKILLS_DIR"
    fi
  elif [ -e "$TARGET" ]; then
    warn "$TARGET 已存在且不是软链，跳过（请手动处理）"
  else
    ln -s "$SKILLS_DIR" "$TARGET" && ok "已创建软链: $TARGET -> $SKILLS_DIR"
  fi
fi

# ---------- 自检 ----------
step "6/6 自检"
CHECK_FAIL=0
check_py() {  # check_py <描述> <python 代码>
  if OUT=$("$VENV_PY" -c "$2" 2>&1); then
    ok "$1${OUT:+: $OUT}"
  else
    fail "$1 —— $(echo "$OUT" | tail -1)"
    CHECK_FAIL=1
  fi
}

check_py "底层库可导入" \
  "from media_to_text import to_text; from media_to_text.handlers.audio import pick_backend; print('ASR 后端 =', pick_backend())"
check_py "类型探测" \
  "from media_to_text import detect_kind; assert detect_kind('a.pdf').value=='pdf'; print('OK')"
check_py "库根定位（脚本能找到 raw/ 与 AGENTS.md）" \
  "from pathlib import Path; r=Path('kg-doc/scripts/ingest_doc.py').resolve().parents[3]; assert (r/'AGENTS.md').is_file() and (r/'raw').is_dir(); print(r)"

if [ "$MINIMAL" = 0 ]; then
  check_py "文档处理依赖" "import docling, markitdown; print('docling + markitdown')" || true
fi
check_py "B 站依赖" "import bilibili_api; print('bilibili-api')" || true

# ---------- 收尾 ----------
step "完成"
if [ "$CHECK_FAIL" = 0 ]; then
  ok "安装成功，全部自检通过"
else
  warn "安装完成，但有自检项失败（见上方 [x]）"
fi

cat <<EOF

后续步骤：
  1) 激活环境：  cd "$SKILLS_DIR" && source .venv/bin/activate
  2) B 站登录：  python kg-bilibili/scripts/login.py     （扫码，凭证写入 .env）
  3) 验证全局：  cd /tmp && pi --print "列出名字以 kg- 开头的 skill"
$( [ "$(command -v ffmpeg >/dev/null 2>&1; echo $?)" != "0" ] && echo "  4) 装 ffmpeg： $FFMPEG_HINT" )

说明：
  · .venv 和 .env 不进 git，各机器本地重建（本脚本即为重建工具）
  · 首次用文档/转写功能会下载模型（Docling 数百 MB、Whisper 约 1.5GB），存 ~/.cache
  · 详细文档见 README.md
EOF
