# HiTw93 / Tw93 公开知识源台账

采集时间：2026-04-30  
对象：X 账号 [@HiTw93](https://x.com/HiTw93)，公开名 Tw93

## 数据边界

本次覆盖公开可访问资料：X 账号资料、X 推文样本、公开 GitHub 仓库、公开博客文章、公开 README。私域对话、未发布草稿、付费社群内容、代码仓库之外的个人经验属于未知区。

Computer Use 核验结果：本机 Chrome 已打开 `https://x.com/HiTw93`，页面停留在 X loading screen；身份和内容核验采用 6551 X API、GitHub API、Tw93 博客和公开 README 交叉证据。

## 原始文件

- `raw/user_info.json`: X 账号资料。
- `raw/user_tweets_top.json`: 账号 Top 推文样本，100 条。
- `raw/user_tweets_latest.json`: 账号 Latest 推文样本，100 条。
- `raw/user_tweets_latest_with_replies.json`: 含回复样本，100 条。
- `raw/search_from_top.json`: X 搜索 fromUser Top 返回，20 条。
- `raw/search_from_latest.json`: X 搜索 fromUser Latest 返回，20 条。
- `normalized_tweets.jsonl`: 去重后的推文样本，197 条。
- `top_tweets.tsv`: 按互动分排序的推文摘要。
- `extracted_urls.jsonl`: 从推文样本抽取的外链，46 条。
- `raw/github_repos_updated.json`: GitHub `tw93` 最近更新仓库列表。
- `raw/github_Kaku.json`, `raw/github_Mole.json`, `raw/github_Pake.json`, `raw/github_MiaoYan.json`, `raw/github_Waza.json`, `raw/github_kami.json`: 核心仓库元数据。
- `raw/README_Kaku.md`, `raw/README_Waza.md`: 已成功抓取的核心 README。
- `raw/blog_ai_coding.html`: Tw93 长文《You Don't Know AI Coding》。
- `raw/blog_learn.html`: Tw93 长文《How I Turn Learning Into a Workflow in the AI Era》。
- `raw/blog_llm.html`: Tw93 长文《You Don't Know LLM Training》。

## 账号资料

X API 返回：

- `screenName`: `HiTw93`
- `name`: `Tw93`
- `description`: Creator of Kaku, Mole, Pake, MiaoYan
- `userId`: `1521688129559613440`
- `verified`: true
- `followersCount`: 138713 in `user_info.json`; tweet payload中出现约 142K follower 字段
- `statusesCount`: 6864

## 核心公开项目

GitHub API 当前元数据：

| 项目 | 公开定位 | Stars | 主要语言 | 更新时间 | 链接 |
| --- | --- | ---: | --- | --- | --- |
| Mole | Deep clean and optimize your Mac | 49632 | Shell | 2026-04-30 | https://github.com/tw93/Mole |
| Pake | Turn any webpage into a desktop app with one command | 48247 | Rust | 2026-04-30 | https://github.com/tw93/Pake |
| MiaoYan | Lightweight Markdown app | 8204 | Swift | 2026-04-30 | https://github.com/tw93/MiaoYan |
| Kaku | Fast terminal built for AI coding | 4792 | Rust | 2026-04-30 | https://github.com/tw93/Kaku |
| Waza | Engineering habits turned into Claude skills | 4233 | Shell | 2026-04-30 | https://github.com/tw93/Waza |
| Kami | Good content deserves good paper | 3898 | HTML | 2026-04-30 | https://github.com/tw93/Kami |
| Weekly | Trendy Weekly records life and links | 854 | CSS | 2026-04-30 | https://github.com/tw93/Weekly |
| Maple | Bookmark-bar hiding and bookmark browsing | 493 | JavaScript | 2026-04-29 | https://github.com/tw93/Maple |

## 高信号外链

- X profile: https://x.com/HiTw93
- GitHub profile: https://github.com/tw93
- Kaku: https://github.com/tw93/Kaku
- Waza: https://github.com/tw93/Waza
- Kami: https://github.com/tw93/Kami
- Mole: https://github.com/tw93/Mole
- Pake: https://github.com/tw93/Pake
- MiaoYan: https://github.com/tw93/MiaoYan
- AI Coding 长文: https://tw93.fun/en/2026-04-26/ai-coding.html
- 学习工作流长文: https://tw93.fun/en/2026-04-06/learn.html
- LLM 训练长文: https://tw93.fun/en/2026-04-03/llm.html

## 内容样本统计

- 去重推文：197 条。
- 抽取外链：46 条。
- 高频主题：
  - AI coding / agents: 80 条。
  - Product / open source: 60 条。
  - macOS / dev tools: 41 条。
  - Design / writing: 19 条。
  - Learning / education: 13 条。
  - Taste / life: 9 条。

