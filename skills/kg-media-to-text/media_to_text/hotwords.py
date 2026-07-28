"""从素材元信息里抽取 ASR 热词（专有名词）。

**为什么需要这一步**：Whisper 靠通用声学模型，没有「这期在讲什么」的先验，
所以专名会稳定听错（实测：携隐→显影、商学院→上学院、金缮→金扇）。
把已知专名通过 initial_prompt 喂进去能显著提高命中率。

**为什么不能直接把 shownotes 塞进 prompt**（实测结论，别再试）：
- initial_prompt 上限是 223 tokens（n_ctx//2-1），且从尾部截断
- 一整段 shownotes 约 1811 tokens，超 8 倍
- 实测后果：输出退化成「路路路路…」，专名命中 0/7，比不加更糟

所以必须先抽取、排序、限量，再由 audio.py 包成自然句注入。

抽取策略全部是确定性规则，不猜、不调 LLM：
1. 结构化字段（播客名/主播名/UP主/嘉宾）直接取——这是最可靠的来源
2. 正文按模式抽：《书名》、连续 ASCII 词、括号内短语
3. 上层可再手动补几个（--hotword 参数）
"""
from __future__ import annotations

import re

# 抽出来但没价值的噪声词：平台通用词、口播套话、常见英文虚词
STOPWORDS = {
    # 平台/推广
    "小宇宙", "喜马拉雅", "苹果播客", "Apple Podcast", "Spotify", "bilibili", "B站",
    "微信", "微博", "小红书", "即刻", "公众号", "知乎", "抖音", "视频号",
    "关注", "订阅", "点赞", "投币", "收藏", "转发", "一键三连", "评论",
    # 通用英文虚词/短词（连续 ASCII 抽取会误命中）
    "the", "The", "and", "And", "for", "For", "with", "With", "you", "You",
    "PS", "ps", "OK", "ok", "AI", "APP", "App", "app", "UP", "up", "CC",
    "http", "https", "www", "com", "cn", "ID", "id", "QQ",
    # 文档结构词（shownotes 自身的小标题，不是节目内容里的专名）
    "Shownotes", "shownotes", "Show Notes", "Notes", "Timeline",
}

# 明显不是专名的形态
_BAD_PATTERNS = [
    re.compile(r"^\d+$"),              # 纯数字
    re.compile(r"^[\d:：.\-]+$"),      # 时间戳/编号
    re.compile(r"^[a-zA-Z]$"),         # 单字母
]


def _is_noise(word: str) -> bool:
    if word in STOPWORDS:
        return True
    if len(word) < 2:
        return True
    # 域名/URL 碎片（www.zhangxinxu.com、example.cn）——带点标识符规则会误命中
    if re.search(r"\.(com|cn|net|org|io|dev|me|top|xyz)$", word, re.I):
        return True
    if word.lower().startswith(("www.", "http")):
        return True
    return any(p.match(word) for p in _BAD_PATTERNS)


def extract_hotwords(
    *,
    fields: list[str] | None = None,
    text: str | None = None,
    extra: list[str] | None = None,
    limit: int = 12,
) -> list[str]:
    """抽取热词，按重要度降序返回（尾部可能被 token 预算舍弃）。

    Args:
        fields: 结构化字段值（播客名/主播/UP主/嘉宾等）。**最可靠，排最前。**
        text:   自由文本（shownotes / 视频简介），按模式抽取。
        extra:  人工补充的词。**优先级最高**，排在最前面。
        limit:  最多返回多少个。默认 12，配合底层 120 token 预算足够。

    Returns:
        去重、去噪、按重要度排序的词表。
    """
    ordered: list[str] = []

    def push(w: str) -> None:
        w = (w or "").strip().strip("《》()（）[]【】,，。.、:：\"'“”")
        if not w or _is_noise(w):
            return
        if w not in ordered:
            ordered.append(w)

    # 1. 人工补充最优先——主人明确指定的一定要保住
    for w in extra or []:
        push(w)

    # 2. 结构化字段：播客名、主播名、UP主、嘉宾，命中率最高
    for w in fields or []:
        push(w)

    # 3. 自由文本按模式抽
    if text:
        # 《书名》/「专名」/“专名” —— 中文里被标记起来的词几乎都是专名，
        # 这是命中率最高的模式（实测：《深度关系》、「七幕人生」都能抽到）
        for pat in (r"《([^》]{1,20})》", r"「([^」]{1,20})」", r"“([^”]{2,12})”"):
            for m in re.findall(pat, text):
                push(m)
        # 带点/下划线的标识符（JSON.rawJSON、torch.nn、process.env）——技术内容常见，
        # 必须排在普通 ASCII 词前面，否则会先被抽成 "JSON" 而丢掉后半截
        for m in re.findall(r"\b[A-Za-z][A-Za-z0-9]*(?:[._][A-Za-z][A-Za-z0-9]*)+\b", text):
            push(m)
        # 连续 ASCII 词组（Touchy Feely / Connect / LangGraph），允许中间一个空格
        for m in re.findall(r"\b[A-Z][A-Za-z0-9]{1,18}(?:\s[A-Z][A-Za-z0-9]{1,18})?\b", text):
            push(m)
        # 中文人名+英文名的组合（携隐Melody 这种播客常见署名形态）
        for m in re.findall(r"[\u4e00-\u9fff]{2,4}[A-Z][a-zA-Z]{2,12}", text):
            push(m)

    return ordered[:limit]
