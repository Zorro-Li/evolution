#!/usr/bin/env python3
"""Build a local self-memory profile from HumanOS and workspace evidence."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Any
from zoneinfo import ZoneInfo


TZ = ZoneInfo("Asia/Shanghai")
WORKSPACE = Path(__file__).resolve().parents[1]
DEFAULT_HUMANOS = Path("/Users/lizongru/codex/humanOS")
DEFAULT_DOCUMENTS = Path("/Users/lizongru/Documents")

SELF_ALIASES = {
    "李阿宇",
    "李阿鱼",
    "李宗儒",
    "lzr",
    "LZR",
    "lzr（不知道啊 你要吃火龙果吗）",
    "lzr（stu dying",
    "lzr（stu dying）",
    "lzr（ᯤ¹⁰ᴳ）",
}

TEXT_TYPES = {0, 25}
SESSION_GAP_SECONDS = 6 * 60 * 60

MARKERS = {
    "support": [
        "谢谢", "辛苦", "抱抱", "加油", "可以的", "放心", "我理解", "我懂",
        "没事", "慢慢来", "陪你", "支持", "别担心",
    ],
    "repair": [
        "对不起", "抱歉", "我的问题", "说清楚", "解释", "商量", "解决", "和好",
        "以后我会", "下次我",
    ],
    "clarity": [
        "我觉得", "我希望", "我需要", "我想", "我们可以", "能不能", "可不可以",
        "认真说", "说清楚", "直接", "结论", "目标",
    ],
    "intimacy": [
        "晚安", "早安", "想你", "喜欢你", "爱你", "宝宝", "宝贝", "亲亲", "贴贴",
        "抱抱",
    ],
    "execution": [
        "做", "跑", "实现", "代码", "系统", "自动化", "agent", "Codex", "本地",
        "验证", "落地",
    ],
}

QUESTION_RE = re.compile(r"[?？]|(吗|嘛|为什么|怎么|咋|是不是|能不能|可不可以|要不要|什么|哪里|几|谁)")
SECRET_NAME_RE = re.compile(r"(pass|password|token|secret|key|pem|ppk|credential)", re.I)


@dataclass
class ConversationStats:
    name: str
    path: str
    total_messages: int = 0
    text_messages: int = 0
    self_messages: int = 0
    other_messages: int = 0
    self_chars: int = 0
    other_chars: int = 0
    self_questions: int = 0
    other_questions: int = 0
    self_initiations: int = 0
    other_initiations: int = 0
    self_reply_seconds: list[int] = field(default_factory=list)
    other_reply_seconds: list[int] = field(default_factory=list)
    marker_counts_self: Counter[str] = field(default_factory=Counter)
    marker_counts_other: Counter[str] = field(default_factory=Counter)
    active_days: set[str] = field(default_factory=set)
    start_ts: int | None = None
    end_ts: int | None = None
    senders: Counter[str] = field(default_factory=Counter)


def now_stamp() -> str:
    return datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S %Z")


def run_id() -> str:
    return datetime.now(TZ).strftime("%Y%m%d-%H%M%S")


def local_dt(ts: int) -> datetime:
    return datetime.fromtimestamp(ts, TZ)


def pct(part: float, whole: float) -> float:
    if whole <= 0:
        return 0.0
    return round(part / whole, 4)


def median(values: list[int]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2


def fmt_hours(seconds: float | None) -> str:
    if seconds is None or math.isnan(seconds):
        return "NA"
    if seconds < 60:
        return f"{seconds:.0f}s"
    if seconds < 3600:
        return f"{seconds / 60:.1f}m"
    return f"{seconds / 3600:.1f}h"


def is_self(sender: str) -> bool:
    normalized = sender.strip()
    if normalized in SELF_ALIASES:
        return True
    lowered = normalized.lower()
    return lowered in {alias.lower() for alias in SELF_ALIASES}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                rows.append(json.loads(stripped))
            except json.JSONDecodeError:
                continue
    return rows


def safe_read_text(path: Path, limit: int = 120_000) -> str:
    if not path.exists() or SECRET_NAME_RE.search(path.name):
        return ""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    return text[:limit]


def marker_hits(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for category, words in MARKERS.items():
        hits = sum(1 for word in words if word in text)
        if hits:
            counts[category] += hits
    return counts


def scan_conversation(path: Path) -> ConversationStats:
    name = path.parent.name.replace("私聊_", "")
    stats = ConversationStats(name=name, path=str(path))
    previous_sender_type: str | None = None
    previous_ts: int | None = None

    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                row = json.loads(stripped)
            except json.JSONDecodeError:
                continue
            if row.get("_type") != "message":
                continue
            sender = str(row.get("accountName") or row.get("sender") or "unknown")
            timestamp = row.get("timestamp")
            if not isinstance(timestamp, int):
                continue
            sender_type = "self" if is_self(sender) else "other"
            stats.total_messages += 1
            stats.senders[sender] += 1
            stats.active_days.add(local_dt(timestamp).date().isoformat())
            stats.start_ts = timestamp if stats.start_ts is None else min(stats.start_ts, timestamp)
            stats.end_ts = timestamp if stats.end_ts is None else max(stats.end_ts, timestamp)

            gap_starts_session = previous_ts is None or timestamp - previous_ts > SESSION_GAP_SECONDS
            if gap_starts_session:
                if sender_type == "self":
                    stats.self_initiations += 1
                else:
                    stats.other_initiations += 1
            elif previous_sender_type and previous_sender_type != sender_type and previous_ts is not None:
                delta = max(0, timestamp - previous_ts)
                if sender_type == "self":
                    stats.self_reply_seconds.append(delta)
                else:
                    stats.other_reply_seconds.append(delta)

            previous_sender_type = sender_type
            previous_ts = timestamp

            msg_type = row.get("type")
            content = str(row.get("content") or "")
            if msg_type not in TEXT_TYPES or not content or content.startswith("["):
                continue
            stats.text_messages += 1
            if sender_type == "self":
                stats.self_messages += 1
                stats.self_chars += len(content)
                stats.self_questions += int(bool(QUESTION_RE.search(content)))
                stats.marker_counts_self.update(marker_hits(content))
            else:
                stats.other_messages += 1
                stats.other_chars += len(content)
                stats.other_questions += int(bool(QUESTION_RE.search(content)))
                stats.marker_counts_other.update(marker_hits(content))

    return stats


def scan_chats(humanos: Path) -> list[ConversationStats]:
    chat_root = humanos / "微信聊天记录"
    files = sorted(chat_root.glob("私聊_*/*.jsonl"))
    return [scan_conversation(path) for path in files]


def parse_attachment_results(humanos: Path) -> dict[str, Any]:
    path = humanos / "依恋关系分析" / "reports" / "attachment_batch_results.json"
    if not path.exists():
        return {"path": str(path), "exists": False}
    data = json.loads(path.read_text(encoding="utf-8"))
    self_rows: list[dict[str, Any]] = []
    relationships = Counter()
    high_data = 0
    for item in data:
        relationship = item.get("relationship_pattern", {}).get("type", "unknown")
        relationships[relationship] += 1
        if item.get("data_sufficiency", {}).get("level") == "high":
            high_data += 1
        for participant in item.get("participants", []):
            if is_self(str(participant.get("name", ""))):
                self_rows.append(
                    {
                        "conversation": item.get("conversation"),
                        "attachment_type": participant.get("attachment_type"),
                        "confidence": participant.get("confidence"),
                        "scores": participant.get("scores", {}),
                        "metrics": participant.get("metrics", {}),
                        "marker_counts": participant.get("marker_counts", {}),
                    }
                )
    score_keys = ["anxiety", "avoidance", "security", "fear"]
    avg_scores: dict[str, float] = {}
    for key in score_keys:
        values = [row["scores"].get(key) for row in self_rows if isinstance(row.get("scores"), dict) and row["scores"].get(key) is not None]
        avg_scores[key] = round(mean(values), 2) if values else 0.0
    confidences = [row.get("confidence") for row in self_rows if isinstance(row.get("confidence"), (int, float))]
    return {
        "path": str(path),
        "exists": True,
        "conversation_count": len(data),
        "high_data_count": high_data,
        "self_rows": self_rows,
        "self_attachment_distribution": dict(Counter(row.get("attachment_type") for row in self_rows)),
        "self_average_scores": avg_scores,
        "self_average_confidence": round(mean(confidences), 3) if confidences else 0.0,
        "relationship_distribution": dict(relationships),
    }


def collect_existing_report_signals(humanos: Path) -> list[str]:
    report_dirs = [
        humanos / "chatrel_analysis_reports_inbox",
        humanos / "依恋关系分析" / "reports" / "per_conversation",
    ]
    signals: list[str] = []
    patterns = [
        "李阿鱼更多",
        "李阿鱼",
        "稳定回应",
        "持续承接",
        "支持",
        "修复",
        "安全型",
        "快速回应",
        "短反馈",
        "自动化",
    ]
    for directory in report_dirs:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md"))[:120]:
            text = safe_read_text(path, 80_000)
            for line in text.splitlines():
                compact = line.strip()
                if 12 <= len(compact) <= 180 and any(pattern in compact for pattern in patterns):
                    signals.append(f"{path.name}: {compact}")
                    break
    return signals[:30]


def collect_project_signals(documents: Path, humanos: Path) -> dict[str, Any]:
    sources = [
        documents / "Codex Operating Prompt.md",
        documents / "daily" / "RoyalHolloway_PersonalStatement.txt",
        documents / "李宗儒.md",
        WORKSPACE / "AGENTS.md",
        WORKSPACE / "memory" / "rules.md",
        humanos / "Knowledge of 心理学" / "chat_record_knowledge_base" / "chat_record_analysis_blueprint.md",
        humanos / "Knowledge of 健康赛道" / "README.md",
        humanos / "Knowledge of 药食同源" / "README.md",
    ]
    keywords = Counter()
    evidence: list[dict[str, str]] = []
    keyword_map = {
        "AI": ["人工智能", "Artificial Intelligence", "AI", "LLM", "GPT"],
        "RAG": ["RAG", "retrieval", "检索", "知识库", "citation", "可追溯"],
        "automation": ["自动化", "agent", "Codex", "执行", "本地", "workflow"],
        "engineering": ["代码", "系统", "工程", "实现", "验证", "reliable", "robust"],
        "research": ["论文", "research", "IEEE", "实验", "评估", "evidence"],
        "health": ["HealthOS", "健康", "营养", "药食同源", "HealthKit"],
        "psychology": ["心理", "聊天记录", "关系", "依恋", "共情", "支持"],
        "directness": ["direct", "concise", "直接", "No filler", "answer first"],
    }
    for path in sources:
        text = safe_read_text(path)
        if not text:
            continue
        local_hits = []
        for label, terms in keyword_map.items():
            count = sum(text.lower().count(term.lower()) for term in terms)
            if count:
                keywords[label] += count
                local_hits.append(f"{label}:{count}")
        if local_hits:
            evidence.append({"path": str(path), "signals": ", ".join(local_hits[:8])})
    return {"keywords": dict(keywords), "evidence": evidence}


def aggregate_chat_stats(conversations: list[ConversationStats]) -> dict[str, Any]:
    total_text = sum(c.text_messages for c in conversations)
    self_text = sum(c.self_messages for c in conversations)
    other_text = sum(c.other_messages for c in conversations)
    self_chars = sum(c.self_chars for c in conversations)
    other_chars = sum(c.other_chars for c in conversations)
    self_inits = sum(c.self_initiations for c in conversations)
    other_inits = sum(c.other_initiations for c in conversations)
    self_replies = [value for c in conversations for value in c.self_reply_seconds]
    other_replies = [value for c in conversations for value in c.other_reply_seconds]
    self_markers: Counter[str] = Counter()
    other_markers: Counter[str] = Counter()
    for convo in conversations:
        self_markers.update(convo.marker_counts_self)
        other_markers.update(convo.marker_counts_other)
    active_days = set()
    for convo in conversations:
        active_days.update(convo.active_days)
    top_conversations = sorted(conversations, key=lambda c: c.total_messages, reverse=True)[:10]
    return {
        "conversation_count": len(conversations),
        "total_messages": sum(c.total_messages for c in conversations),
        "total_text_messages": total_text,
        "self_text_messages": self_text,
        "other_text_messages": other_text,
        "self_text_share": pct(self_text, total_text),
        "self_char_share": pct(self_chars, self_chars + other_chars),
        "self_avg_chars": round(self_chars / self_text, 2) if self_text else 0,
        "other_avg_chars": round(other_chars / other_text, 2) if other_text else 0,
        "self_question_rate": pct(sum(c.self_questions for c in conversations), self_text),
        "other_question_rate": pct(sum(c.other_questions for c in conversations), other_text),
        "self_initiation_share": pct(self_inits, self_inits + other_inits),
        "self_median_reply": median(self_replies),
        "other_median_reply": median(other_replies),
        "self_marker_counts": dict(self_markers),
        "other_marker_counts": dict(other_markers),
        "active_days": len(active_days),
        "top_conversations": [
            {
                "name": c.name,
                "messages": c.total_messages,
                "text": c.text_messages,
                "self_text_share": pct(c.self_messages, c.text_messages),
                "self_initiation_share": pct(c.self_initiations, c.self_initiations + c.other_initiations),
                "active_days": len(c.active_days),
            }
            for c in top_conversations
        ],
    }


def build_profile_markdown(payload: dict[str, Any]) -> str:
    chat = payload["chat"]
    attachment = payload["attachment"]
    project = payload["project"]
    generated = payload["generated_at"]
    source_count = len(project.get("evidence", []))

    avg_scores = attachment.get("self_average_scores", {})
    attachment_dist = attachment.get("self_attachment_distribution", {})
    top_projects = sorted(project.get("keywords", {}).items(), key=lambda item: item[1], reverse=True)[:8]

    lines = [
        "# Self Memory Profile",
        "",
        f"Generated: {generated}",
        "",
        "## Identity",
        "",
        "- Legal/name signal: 李宗儒.",
        "- WeChat self aliases: 李阿宇 from user instruction, 李阿鱼 from HumanOS chat exports.",
        "- Core direction: applied AI engineer / AI systems builder focused on RAG, agents, planning, automation, and reliable execution.",
        "- Strong project gravity: HumanOS / HealthOS, relationship analysis from chat records, psychology knowledge base, health content knowledge base, remote Codex execution, AI research applications.",
        "",
        "## Operating Preferences",
        "",
        "- Answer first, direct language, high information density.",
        "- Prefer local execution, verified commands, working artifacts, and durable automation.",
        "- Treat Codex as an execution backend that can read the workspace, change files, run checks, and remember corrections.",
        "- Use Chinese by default for collaboration; keep code, commands, and logs in their original language.",
        "- Preserve user corrections as memory and change behavior immediately when assumptions are corrected.",
        "",
        "## Chat-Derived Interaction Tendencies",
        "",
        f"- HumanOS private-chat sample: {chat['conversation_count']} conversations, {chat['total_messages']} total messages, {chat['total_text_messages']} text messages, {chat['active_days']} active days.",
        f"- Self text share: {chat['self_text_share'] * 100:.1f}%; self character share: {chat['self_char_share'] * 100:.1f}%.",
        f"- Average text length: self {chat['self_avg_chars']} chars, others {chat['other_avg_chars']} chars.",
        f"- Conversation initiation share: self {chat['self_initiation_share'] * 100:.1f}%.",
        f"- Median cross-speaker reply latency: self {fmt_hours(chat['self_median_reply'])}, others {fmt_hours(chat['other_median_reply'])}.",
        f"- Marker profile: self support {chat['self_marker_counts'].get('support', 0)}, repair {chat['self_marker_counts'].get('repair', 0)}, clarity {chat['self_marker_counts'].get('clarity', 0)}, intimacy {chat['self_marker_counts'].get('intimacy', 0)}.",
        "",
        "## Relationship Pattern From Existing HumanOS Analyses",
        "",
        f"- Existing attachment batch: {attachment.get('conversation_count', 0)} conversations, high-data records {attachment.get('high_data_count', 0)}.",
        f"- Self attachment distribution in generated reports: {json.dumps(attachment_dist, ensure_ascii=False)}.",
        f"- Self average scores: anxiety {avg_scores.get('anxiety', 0)}, avoidance {avg_scores.get('avoidance', 0)}, security {avg_scores.get('security', 0)}, fear {avg_scores.get('fear', 0)}.",
        "- Behavioral reading: across available reports, the stable pattern is high availability, fast response, support/repair behavior, and low avoidance.",
        "- Boundary: this is an interaction-pattern memory with clinical diagnosis excluded.",
        "",
        "## Work And Learning Pattern",
        "",
    ]
    for label, count in top_projects:
        lines.append(f"- {label}: {count} source hits across local materials.")
    lines.extend(
        [
            f"- Evidence source count: {source_count}.",
            "- Repeated themes: practical AI systems, retrieval quality, evaluation, automation, relationship/health data products, and agentic workflows.",
            "",
            "## Jarvis Adaptation Rules",
            "",
            "- Start with local context and current project files.",
            "- Build a working artifact before expanding theory.",
            "- Verify with commands and write the result into memory.",
            "- Skip secrets, credential files, and unrelated account stores during personality analysis.",
            "- Treat 李阿宇 and 李阿鱼 as the same WeChat identity unless the user gives a correction.",
            "- Re-run this profile generator on a 6-hour cadence and compare the new profile with the previous latest profile.",
            "",
            "## Evidence Index",
            "",
            "- `/Users/lizongru/codex/humanOS/微信聊天记录`: raw WeChat JSONL records.",
            "- `/Users/lizongru/codex/humanOS/依恋关系分析/reports/attachment_batch_summary.md`: existing attachment batch summary.",
            "- `/Users/lizongru/codex/humanOS/依恋关系分析/reports/attachment_batch_results.json`: structured relationship-analysis results.",
            "- `/Users/lizongru/Documents/Codex Operating Prompt.md`: durable collaboration and coding preferences.",
            "- `/Users/lizongru/Documents/daily/RoyalHolloway_PersonalStatement.txt`: AI/research/project trajectory.",
            "- `/Users/lizongru/Documents/李宗儒.md`: education and project-history signals.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_preferences_markdown(payload: dict[str, Any]) -> str:
    generated = payload["generated_at"]
    return "\n".join(
        [
            "# Preferences",
            "",
            f"Generated: {generated}",
            "",
            "## Communication",
            "",
            "- Direct Chinese response by default.",
            "- Answer first, then provide context.",
            "- Dense technical detail when the task is technical.",
            "- Minimal filler; recommendations replace decorative balance essays.",
            "",
            "## Execution",
            "",
            "- Prefer local commands and code changes over conceptual discussion.",
            "- Verify claims with the smallest reliable command.",
            "- Keep durable artifacts in the workspace.",
            "- Build automation when a task will recur.",
            "",
            "## Memory",
            "",
            "- Capture explicit corrections immediately.",
            "- Promote repeated corrections into durable rules.",
            "- Keep privacy-sensitive evidence local.",
            "- Store profile conclusions with source paths and aggregate statistics.",
            "",
            "## Analysis",
            "",
            "- Use evidence from HumanOS chat records and existing reports.",
            "- Distinguish behavioral patterns, product preferences, and clinical claims.",
            "- Treat relationship-analysis outputs as probabilistic interaction summaries.",
            "",
        ]
    )


def write_outputs(payload: dict[str, Any], markdown: str, preferences: str) -> dict[str, str]:
    run = payload["run_id"]
    archive_dir = WORKSPACE / "evolution" / "self_memory" / run
    archive_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "latest_profile": WORKSPACE / "memory" / "self_profile.md",
        "latest_preferences": WORKSPACE / "memory" / "preferences.md",
        "latest_json": WORKSPACE / "memory" / "self_profile.json",
        "archive_profile": archive_dir / "self_profile.md",
        "archive_preferences": archive_dir / "preferences.md",
        "archive_json": archive_dir / "self_profile.json",
    }
    outputs["latest_profile"].write_text(markdown, encoding="utf-8")
    outputs["latest_preferences"].write_text(preferences, encoding="utf-8")
    outputs["latest_json"].write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    outputs["archive_profile"].write_text(markdown, encoding="utf-8")
    outputs["archive_preferences"].write_text(preferences, encoding="utf-8")
    outputs["archive_json"].write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return {name: str(path) for name, path in outputs.items()}


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    humanos = Path(args.humanos).expanduser()
    documents = Path(args.documents).expanduser()
    conversations = scan_chats(humanos)
    chat = aggregate_chat_stats(conversations)
    attachment = parse_attachment_results(humanos)
    project = collect_project_signals(documents, humanos)
    report_signals = collect_existing_report_signals(humanos)
    return {
        "run_id": run_id(),
        "generated_at": now_stamp(),
        "humanos": str(humanos),
        "documents": str(documents),
        "self_aliases": sorted(SELF_ALIASES),
        "chat": chat,
        "attachment": attachment,
        "project": project,
        "report_signals": report_signals,
        "privacy_policy": {
            "raw_message_policy": "aggregate statistics and source paths; raw private message dumps excluded",
            "secret_file_policy": "skip filenames matching pass/password/token/secret/key/pem/ppk/credential",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate evolving self-memory from local evidence.")
    parser.add_argument("--humanos", default=str(DEFAULT_HUMANOS))
    parser.add_argument("--documents", default=str(DEFAULT_DOCUMENTS))
    parser.add_argument("--print-summary", action="store_true")
    args = parser.parse_args()

    payload = build_payload(args)
    markdown = build_profile_markdown(payload)
    preferences = build_preferences_markdown(payload)
    outputs = write_outputs(payload, markdown, preferences)

    if args.print_summary:
        chat = payload["chat"]
        print("Self-memory generated")
        print(f"- conversations: {chat['conversation_count']}")
        print(f"- text_messages: {chat['total_text_messages']}")
        print(f"- self_text_share: {chat['self_text_share'] * 100:.1f}%")
        print(f"- latest_profile: {outputs['latest_profile']}")
        print(f"- latest_preferences: {outputs['latest_preferences']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
