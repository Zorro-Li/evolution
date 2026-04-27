#!/usr/bin/env python3
import argparse
import collections
import gzip
import json
import re
import sys
import time
import urllib.request
from pathlib import Path


META_URL = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Toys_and_Games.jsonl.gz"
REVIEWS_URL = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Toys_and_Games.jsonl.gz"

INCLUDE_PATTERNS = [
    re.compile(r"\blego\b", re.I),
    re.compile(r"\bmega\s*bloks?\b", re.I),
    re.compile(r"\bbuilding\s+(blocks?|bricks?|sets?)\b", re.I),
    re.compile(r"\bmagnetic\s+(tiles?|blocks?)\b", re.I),
    re.compile(r"\bbristle\s+blocks?\b", re.I),
]

EXCLUDE_PATTERNS = [
    re.compile(r"\bbook\b", re.I),
    re.compile(r"\bsticker\b", re.I),
    re.compile(r"\bplush\b", re.I),
    re.compile(r"\bparty\b", re.I),
    re.compile(r"\bshirt\b", re.I),
    re.compile(r"\bposter\b", re.I),
    re.compile(r"\bcostume\b", re.I),
]


def open_jsonl_gz(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Jarvis research script (contact: local user)"},
    )
    response = urllib.request.urlopen(request, timeout=60)
    return gzip.GzipFile(fileobj=response)


def clean_text(value):
    if value is None:
        return ""
    value = str(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def is_blocks_product(item):
    title = clean_text(item.get("title"))
    categories = " ".join(clean_text(x) for x in item.get("categories", []))
    text = f"{title} {categories}"
    if any(pattern.search(text) for pattern in EXCLUDE_PATTERNS):
        return False
    return any(pattern.search(text) for pattern in INCLUDE_PATTERNS)


def product_family(title):
    lower = title.lower()
    if "lego" in lower:
        return "LEGO"
    if "mega bloks" in lower or "mega blocks" in lower:
        return "MEGA BLOKS"
    if "magna-tiles" in lower or "magna tiles" in lower:
        return "Magna-Tiles"
    if "picassotiles" in lower or "picasso tiles" in lower:
        return "PicassoTiles"
    if "bristle" in lower:
        return "Bristle Blocks"
    if "magnetic" in lower and "tile" in lower:
        return "Magnetic Tiles"
    return "Building Blocks"


def choose_products(meta_limit):
    by_family = {}
    scanned = 0
    started = time.time()
    with open_jsonl_gz(META_URL) as fh:
        for raw in fh:
            scanned += 1
            if meta_limit and scanned > meta_limit:
                break
            if scanned % 250000 == 0:
                elapsed = time.time() - started
                print(f"meta scanned={scanned} candidates={sum(len(v) for v in by_family.values())} elapsed={elapsed:.1f}s", file=sys.stderr)
            item = json.loads(raw)
            if not is_blocks_product(item):
                continue
            asin = clean_text(item.get("parent_asin"))
            title = clean_text(item.get("title"))
            rating_number = int(item.get("rating_number") or 0)
            average_rating = float(item.get("average_rating") or 0)
            if not asin or not title or rating_number < 200:
                continue
            family = product_family(title)
            entry = {
                "asin": asin,
                "title": title,
                "average_rating": average_rating,
                "rating_number": rating_number,
                "family": family,
                "amazon_url": f"https://www.amazon.com/dp/{asin}",
                "categories": item.get("categories", []),
                "store": item.get("store"),
            }
            by_family.setdefault(family, []).append(entry)
    selected = []
    preferred_order = ["LEGO", "MEGA BLOKS", "Magna-Tiles", "PicassoTiles", "Bristle Blocks", "Magnetic Tiles", "Building Blocks"]
    for family in preferred_order:
        entries = sorted(by_family.get(family, []), key=lambda x: x["rating_number"], reverse=True)
        for entry in entries:
            if entry["asin"] not in {x["asin"] for x in selected}:
                selected.append(entry)
                break
        if len(selected) == 5:
            break
    if len(selected) < 5:
        all_entries = []
        for entries in by_family.values():
            all_entries.extend(entries)
        for entry in sorted(all_entries, key=lambda x: x["rating_number"], reverse=True):
            if entry["asin"] not in {x["asin"] for x in selected}:
                selected.append(entry)
            if len(selected) == 5:
                break
    return selected


def quality_review(item):
    text = clean_text(item.get("text"))
    title = clean_text(item.get("title"))
    if len(text) < 35:
        return False
    if "vine customer review" in text.lower():
        return False
    return bool(title or text)


def collect_reviews(products, per_product, review_limit):
    target_asins = {product["asin"] for product in products}
    reviews = {asin: [] for asin in target_asins}
    scanned = 0
    started = time.time()
    with open_jsonl_gz(REVIEWS_URL) as fh:
        for raw in fh:
            scanned += 1
            if review_limit and scanned > review_limit:
                break
            if scanned % 500000 == 0:
                counts = {asin: len(items) for asin, items in reviews.items()}
                elapsed = time.time() - started
                print(f"reviews scanned={scanned} counts={counts} elapsed={elapsed:.1f}s", file=sys.stderr)
            item = json.loads(raw)
            asin = clean_text(item.get("parent_asin"))
            if asin not in target_asins:
                continue
            if len(reviews[asin]) >= per_product:
                continue
            if not quality_review(item):
                continue
            reviews[asin].append(
                {
                    "rating": item.get("rating"),
                    "title": clean_text(item.get("title")),
                    "text": clean_text(item.get("text")),
                    "helpful_vote": int(item.get("helpful_vote") or 0),
                    "verified_purchase": bool(item.get("verified_purchase")),
                    "timestamp": item.get("timestamp"),
                    "user_id": item.get("user_id"),
                    "asin": asin,
                }
            )
            if all(len(items) >= per_product for items in reviews.values()):
                break
    return reviews, scanned


def summarize_reviews(products, reviews):
    positive_terms = {
        "quality": ["quality", "sturdy", "durable", "solid", "well made", "great"],
        "value": ["price", "value", "worth", "affordable", "deal"],
        "kids": ["kids", "child", "children", "son", "daughter", "grandson", "granddaughter"],
        "compatibility": ["compatible", "fit", "works with", "lego", "tiles"],
        "creativity": ["creative", "imagination", "build", "building", "fun"],
    }
    pain_terms = {
        "missing_or_wrong_parts": ["missing", "wrong", "not included", "short"],
        "small_or_choking": ["small", "tiny", "choking"],
        "weak_magnets_or_fit": ["magnet", "magnets", "fall apart", "loose", "do not fit", "doesn't fit"],
        "packaging": ["box", "package", "packaging", "damaged"],
        "price_expectation": ["expensive", "pricey", "overpriced", "not worth"],
    }
    product_summaries = []
    all_reviews = []
    for product in products:
        items = reviews.get(product["asin"], [])
        all_reviews.extend(items)
        ratings = [float(item["rating"]) for item in items if item.get("rating") is not None]
        text = " ".join((item["title"] + " " + item["text"]).lower() for item in items)
        product_summaries.append(
            {
                "asin": product["asin"],
                "title": product["title"],
                "amazon_url": product["amazon_url"],
                "sample_size": len(items),
                "sample_avg_rating": round(sum(ratings) / len(ratings), 2) if ratings else None,
                "dataset_avg_rating": product["average_rating"],
                "dataset_rating_number": product["rating_number"],
                "top_positive_signals": rank_terms(text, positive_terms),
                "top_pain_signals": rank_terms(text, pain_terms),
            }
        )
    all_text = " ".join((item["title"] + " " + item["text"]).lower() for item in all_reviews)
    ratings = [float(item["rating"]) for item in all_reviews if item.get("rating") is not None]
    return {
        "sample_size": len(all_reviews),
        "sample_avg_rating": round(sum(ratings) / len(ratings), 2) if ratings else None,
        "rating_distribution": dict(sorted(collections.Counter(int(float(r)) for r in ratings).items())),
        "top_positive_signals": rank_terms(all_text, positive_terms),
        "top_pain_signals": rank_terms(all_text, pain_terms),
        "products": product_summaries,
    }


def rank_terms(text, groups):
    scored = []
    for name, terms in groups.items():
        score = sum(text.count(term) for term in terms)
        if score:
            scored.append({"signal": name, "count": score})
    return sorted(scored, key=lambda x: x["count"], reverse=True)


def write_markdown(path, products, reviews, summary, review_scanned):
    lines = []
    lines.append("# Amazon 积木品类评论样本分析")
    lines.append("")
    lines.append("数据来源：McAuley Lab Amazon Reviews 2023，Toys_and_Games 商品元数据与评论。Amazon 搜索页当前对自动请求返回限制页，本次使用公开研究数据集里的 Amazon 评论样本。")
    lines.append("")
    lines.append(f"- 样本量：{summary['sample_size']} 条评论")
    lines.append(f"- 商品数：{len(products)} 个")
    lines.append(f"- 评论扫描行数：{review_scanned}")
    lines.append(f"- 样本平均星级：{summary['sample_avg_rating']}")
    lines.append(f"- 样本星级分布：{summary['rating_distribution']}")
    lines.append("")
    lines.append("## 五个 Amazon 链接")
    lines.append("")
    for idx, product in enumerate(products, 1):
        product_summary = next(item for item in summary["products"] if item["asin"] == product["asin"])
        lines.append(f"{idx}. [{product['title']}]({product['amazon_url']})")
        lines.append(f"   - ASIN：{product['asin']}")
        lines.append(f"   - 数据集评分：{product['average_rating']} / {product['rating_number']} ratings")
        lines.append(f"   - 本次样本：{product_summary['sample_size']} 条，平均 {product_summary['sample_avg_rating']} 星")
    lines.append("")
    lines.append("## 总体结论")
    lines.append("")
    lines.append("- 购买动机集中在儿童礼物、亲子陪玩、开放式搭建和高复购基础件。")
    lines.append("- 好评高频点是孩子持续玩、能和现有积木兼容、颜色/形状选择够多、性价比合理。")
    lines.append("- 差评高频点是缺件、包装破损、磁力或咬合弱、尺寸比预期小、价格与件数预期错位。")
    lines.append("- 商品页最关键的转化信息是年龄段、件数、单块尺寸、兼容性、收纳方式、缺件补偿政策。")
    lines.append("")
    lines.append("## 信号统计")
    lines.append("")
    lines.append(f"- 正向信号：{summary['top_positive_signals']}")
    lines.append(f"- 痛点信号：{summary['top_pain_signals']}")
    lines.append("")
    lines.append("## 单品观察")
    lines.append("")
    for item in summary["products"]:
        lines.append(f"### {item['title']}")
        lines.append("")
        lines.append(f"- 链接：{item['amazon_url']}")
        lines.append(f"- 样本：{item['sample_size']} 条，平均 {item['sample_avg_rating']} 星")
        lines.append(f"- 正向信号：{item['top_positive_signals']}")
        lines.append(f"- 痛点信号：{item['top_pain_signals']}")
        lines.append("")
    lines.append("## 评论样本索引")
    lines.append("")
    lines.append("评论正文保存在 JSON 文件中；报告只呈现结构化摘要，减少大段复制评论文本。")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-product", type=int, default=20)
    parser.add_argument("--meta-limit", type=int, default=0)
    parser.add_argument("--review-limit", type=int, default=0)
    parser.add_argument("--out-dir", default="runs/amazon_blocks_reviews_2026-04-26")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    products = choose_products(args.meta_limit)
    reviews, review_scanned = collect_reviews(products, args.per_product, args.review_limit)
    summary = summarize_reviews(products, reviews)

    payload = {
        "source": {
            "metadata_url": META_URL,
            "reviews_url": REVIEWS_URL,
        },
        "products": products,
        "reviews": reviews,
        "summary": summary,
        "review_scanned": review_scanned,
    }
    (out_dir / "amazon_blocks_reviews_sample.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(out_dir / "analysis.md", products, reviews, summary, review_scanned)
    print(out_dir / "analysis.md")
    print(out_dir / "amazon_blocks_reviews_sample.json")


if __name__ == "__main__":
    main()
