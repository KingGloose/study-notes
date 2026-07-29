#!/usr/bin/env python3
"""学习计划管理：创建/查看/推进学习计划，追踪进度。

计划存 `<库根>/learning/<slug>.json`,是**过程性产物**(不是沉淀知识,故不进 wiki)。
真正的学习靠 AI 和主人对话完成,本脚本只负责记账。

用法:
  python plan.py list                                  # 所有计划
  python plan.py show <slug>                           # 某计划详情
  python plan.py new <标题> --steps "步骤1|步骤2|..."   # 创建计划
  python plan.py done <slug> <步骤号> [--note "收获"]   # 标记步骤完成
  python plan.py note <slug> --note "..."              # 追加笔记(误解/卡点/啊哈时刻)
  python plan.py session <slug> --minutes 20           # 记一次学习会话
  python plan.py archive <slug>                        # 归档(学完或放弃)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

# ---------- 库根解析（内联，保持本脚本零依赖） ----------
def _looks_like_vault(p: Path) -> bool:
    try:
        return p.is_dir() and (p / "AGENTS.md").is_file() and (p / "wiki").is_dir()
    except OSError:
        return False


def _walk_up(start: Path, limit: int = 8) -> Path | None:
    cur = start.resolve()
    for _ in range(limit):
        if _looks_like_vault(cur):
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return None


def find_vault() -> Path:
    """定位知识库根。优先级：KG_VAULT 环境变量 → 配置文件 → cwd 向上 → 本文件向上。"""
    import os
    v = os.environ.get("KG_VAULT")
    if v:
        p = Path(v).expanduser().resolve()
        if _looks_like_vault(p):
            return p
        sys.exit(f"[错误] KG_VAULT 指向 {p}，但那里不像知识库（需 AGENTS.md + wiki/）")

    cfg = Path.home() / ".config" / "kg-wiki" / "config.json"
    if cfg.is_file():
        try:
            v = json.loads(cfg.read_text(encoding="utf-8")).get("vault")
            if v:
                p = Path(v).expanduser().resolve()
                if _looks_like_vault(p):
                    return p
        except (json.JSONDecodeError, OSError):
            pass

    for start in (Path.cwd(), Path(__file__).parent):
        p = _walk_up(start)
        if p:
            return p

    sys.exit(
        "[错误] 找不到知识库。请用以下任一方式指定：\n"
        "  1. export KG_VAULT=/path/to/your-vault\n"
        f"  2. 写入 {cfg}：{{\"vault\": \"/path/to/your-vault\"}}\n"
        "  3. 在知识库目录内执行\n"
        "知识库需包含 AGENTS.md 和 wiki/ 目录。"
    )



VAULT = find_vault()
LEARN_DIR = VAULT / "learning"


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def slugify(title: str) -> str:
    s = re.sub(r"[\\/:*?\"<>|\s]+", "-", title.strip())
    return re.sub(r"-+", "-", s).strip("-")[:50] or "plan"


def plan_path(slug: str) -> Path:
    return LEARN_DIR / f"{slug}.json"


def load(slug: str) -> dict:
    p = plan_path(slug)
    if not p.is_file():
        sys.exit(f"[错误] 找不到计划: {slug}（用 list 看现有计划）")
    return json.loads(p.read_text(encoding="utf-8"))


def save(plan: dict) -> None:
    LEARN_DIR.mkdir(parents=True, exist_ok=True)
    plan_path(plan["slug"]).write_text(
        json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")


def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def cmd_new(args) -> int:
    slug = slugify(args.title)
    if plan_path(slug).is_file():
        sys.exit(f"[错误] 计划已存在: {slug}（用 show 查看，或换个标题）")
    steps = [s.strip() for s in (args.steps or "").split("|") if s.strip()]
    if not steps:
        sys.exit("[错误] 需要 --steps「步骤1|步骤2|...」")
    plan = {
        "slug": slug,
        "title": args.title,
        "domain": args.domain or "",
        "created": now_iso(),
        "status": "active",
        "why": args.why or "",           # 学这个是为了解决什么问题
        "steps": [{"n": i + 1, "text": t, "done": False, "done_at": None, "note": ""}
                  for i, t in enumerate(steps)],
        "notes": [],                      # 误解/卡点/啊哈时刻
        "sessions": [],                   # 学习会话记录
    }
    save(plan)
    print(f"✅ 已创建计划 `{slug}`（{len(steps)} 步）")
    print(f"   文件: learning/{slug}.json")
    for s in plan["steps"]:
        print(f"   {s['n']}. {s['text']}")
    return 0


def cmd_list(args) -> int:
    if not LEARN_DIR.is_dir() or not list(LEARN_DIR.glob("*.json")):
        print("还没有学习计划。用 `plan.py new` 创建。")
        return 0
    plans = []
    for f in sorted(LEARN_DIR.glob("*.json")):
        try:
            plans.append(json.loads(f.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    active = [p for p in plans if p.get("status") == "active"]
    archived = [p for p in plans if p.get("status") != "active"]

    def line(p):
        done = sum(1 for s in p["steps"] if s["done"])
        total = len(p["steps"])
        bar = "█" * done + "░" * (total - done)
        mins = sum(s.get("minutes", 0) for s in p.get("sessions", []))
        return (f"  {p['slug']:<32} {bar} {done}/{total}"
                f"  累计 {mins} 分钟  {p.get('domain','')}")

    if active:
        print("# 进行中\n")
        for p in active:
            print(line(p))
    if archived:
        print("\n# 已归档\n")
        for p in archived:
            print(line(p))
    return 0


def cmd_show(args) -> int:
    p = load(args.slug)
    done = sum(1 for s in p["steps"] if s["done"])
    print(f"# {p['title']}")
    print(f"\n状态: {p['status']} | 进度 {done}/{len(p['steps'])} | 创建 {p['created']}")
    if p.get("domain"):
        print(f"领域: {p['domain']}")
    if p.get("why"):
        print(f"为什么学: {p['why']}")

    print("\n## 步骤\n")
    for s in p["steps"]:
        mark = "✅" if s["done"] else "⬜"
        print(f"  {mark} {s['n']}. {s['text']}")
        if s.get("note"):
            print(f"      收获: {s['note']}")

    if p.get("notes"):
        print("\n## 过程记录（误解 / 卡点 / 啊哈时刻）\n")
        for n in p["notes"]:
            print(f"  · [{n['at']}] {n['text']}")

    if p.get("sessions"):
        total = sum(s.get("minutes", 0) for s in p["sessions"])
        print(f"\n## 学习会话（共 {len(p['sessions'])} 次 / {total} 分钟）\n")
        for s in p["sessions"][-6:]:
            print(f"  · {s['at']}  {s.get('minutes','?')} 分钟"
                  + (f"  — {s['summary']}" if s.get("summary") else ""))
    return 0


def cmd_done(args) -> int:
    p = load(args.slug)
    hit = next((s for s in p["steps"] if s["n"] == args.step), None)
    if not hit:
        sys.exit(f"[错误] 没有第 {args.step} 步（共 {len(p['steps'])} 步）")
    hit["done"] = True
    hit["done_at"] = now_iso()
    if args.note:
        hit["note"] = args.note
    save(p)
    done = sum(1 for s in p["steps"] if s["done"])
    print(f"✅ 第 {args.step} 步完成：{hit['text']}")
    print(f"   进度 {done}/{len(p['steps'])}")
    if done == len(p["steps"]):
        print("\n🎉 全部步骤完成！建议：")
        print("   1. 回顾整个 notes（误解/卡点）——那是最值得沉淀的部分")
        print("   2. 把认知收获写进 wiki（记「我原以为 X 实际是 Y」，不是记知识点本身）")
        print("   3. `plan.py archive` 归档")
    return 0


def cmd_note(args) -> int:
    p = load(args.slug)
    if not args.note:
        sys.exit("[错误] 需要 --note 内容")
    p["notes"].append({"at": now_iso(), "text": args.note})
    save(p)
    print(f"✅ 已记录（该计划共 {len(p['notes'])} 条过程记录）")
    return 0


def cmd_session(args) -> int:
    p = load(args.slug)
    p["sessions"].append({
        "at": now_iso(),
        "minutes": args.minutes,
        "summary": args.summary or "",
    })
    save(p)
    total = sum(s.get("minutes", 0) for s in p["sessions"])
    print(f"✅ 已记录本次会话（{args.minutes} 分钟，累计 {total} 分钟）")
    return 0


def cmd_archive(args) -> int:
    p = load(args.slug)
    p["status"] = "archived"
    p["archived_at"] = now_iso()
    save(p)
    print(f"✅ 已归档 `{args.slug}`")
    print("   提醒：归档前确认认知收获已沉淀进 wiki（计划本身不是知识）")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new", help="创建计划")
    p_new.add_argument("title")
    p_new.add_argument("--steps", required=True, help="步骤，用 | 分隔")
    p_new.add_argument("--domain", default=None, help="领域，如 Rust / 前端")
    p_new.add_argument("--why", default=None, help="学这个为了解决什么问题")

    sub.add_parser("list", help="列出所有计划")

    p_show = sub.add_parser("show", help="查看计划详情")
    p_show.add_argument("slug")

    p_done = sub.add_parser("done", help="标记步骤完成")
    p_done.add_argument("slug")
    p_done.add_argument("step", type=int)
    p_done.add_argument("--note", default=None, help="这步的收获")

    p_note = sub.add_parser("note", help="记录误解/卡点/啊哈时刻")
    p_note.add_argument("slug")
    p_note.add_argument("--note", required=True)

    p_sess = sub.add_parser("session", help="记一次学习会话")
    p_sess.add_argument("slug")
    p_sess.add_argument("--minutes", type=int, required=True)
    p_sess.add_argument("--summary", default=None)

    p_arch = sub.add_parser("archive", help="归档计划")
    p_arch.add_argument("slug")

    args = ap.parse_args()
    return {
        "new": cmd_new, "list": cmd_list, "show": cmd_show,
        "done": cmd_done, "note": cmd_note, "session": cmd_session,
        "archive": cmd_archive,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
