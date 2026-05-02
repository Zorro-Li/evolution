# Jarvis Reflection - 2026-05-02

Window: last 1 day(s)

## Signals

- feedback: 3
- observations: 14
- done_tasks: 7
- open_tasks: 5

## Top Tags

- context: 13
- correction: 3
- automation: 1

## Recent Feedback

- fb_71c5c7fd2b: 用户纠正：币圈以史为鉴 Skill 和老祖宗祖训扩展到 AI/Agent 的 Skill 是两个完全不同的工作，必须分开文件夹和概念边界。
- fb_2e9b80b703: 用户明确要求：Codex 自己加入进化流程；每次对话后整理出的研究方案、复盘、技能蒸馏都要用 gbrain put 存入本地知识库；每次开始任务前先用 gbrain search 查上下文。
- fb_a87073b306: 用户要求安装 https://github.com/pogjester/company-research-agent，加入 gbrain，并在以后查公司时优先使用这个本地公司研究 agent。

## Recent Observations

- obs_8a3af584c9: Created crypto-history-as-mirror Skill from 华语币圈经典2010-2024 PDF. Added detailed PDF knowledge map, 2010-2024 crypto rise-fall history, ancestral prompt rules, and due-diligence playbook. Linked crypto-rug-analysis to the new historical skill.
- obs_d3612c4c98: Created local branch codex/ancestral-agent-workflow-skill with reusable ancestral-agent-workflow Skill and local install. GitHub publish blocked: SSH publickey denied, gh unavailable, GitHub tokens absent, connector lacks repo access.
- obs_aca5d52457: Corrected skill organization per user: crypto-history-as-mirror and ancestral-agent-workflow are separate folders and concepts. Removed ancestral prompt references from crypto history Skill, added repo crypto skill, synced local installs, pushed branch codex/separate-history-ancestral-skills. PR creation blocked by GitHub connector 404.
- obs_df45a76932: 已新增每周 GBrain digest 自动化：scripts/weekly_gbrain_digest.py 每次扫描最近 7 天更新的 GBrain 页面，写入 runs/gbrain_weekly/YYYY-MM-DD-weekly-gbrain-digest.md，并用 gbrain put 回写 weekly-gbrain-digest-YYYY-MM-DD；launchd 已安装为 com.lizongru.jarvis.weekly-gbrain-digest，每周一 09:10 运行。
- obs_d6983cf600: 用户要求每天自动把新获取资料上传到 GitHub，重点覆盖 GBrain；实现方向应把 GBrain markdown export 纳入每日 evolution publish 后再 push。
- obs_6d9df20b7c: 已创建 Daily X Creator Distillation Codex cron：每天 09:30 Asia/Shanghai 在 /Users/lizongru/codex/进化 本地运行，使用 Safari 登录态 soro、Computer Use、x-creator-distiller skill、GBrain 和 Jarvis 记录来增量覆盖关注列表里的 AI/美国相关 X 创作者。
- obs_e819399d8a: company-research-agent 已安装到 /Users/lizongru/codex/进化/tools/company-research-agent；后端依赖在 .venv，前端依赖在 ui/node_modules；gbrain 工具卡 slug 为 company-research-agent-tool。
- obs_4335912e65: company-research-agent 验证通过：后端 compileall/import/uvicorn health check 通过；前端 npm run build 通过；npm audit fix 后 npm audit --audit-level=high 为 0 vulnerabilities。
- obs_24f9479341: X creator task source corrected to https://x.com/xiaoyuZorro/following; user wants 1700+ following accounts collected through Computer Use and categorized for US stocks and AI.
- obs_61bf185549: X following Computer Use crawl batch 001 captured 260 unique accounts from @xiaoyuZorro/following, categorized into AI_CORE=62, US_STOCKS_MACRO=37, PRODUCT_GROWTH=23, CRYPTO_WEB3=90, OTHER=48. Artifacts: runs/x-creator-watch/2026-05-02/00_following_registry.md and 01_ai_us_stock_shortlist.md.

## Recommended Promotions

- Review correction-tagged feedback and promote durable behavior into `memory/rules.md`.

## Next Actions

- P1 task_aff468be5f: 抓取 Amazon 积木品类 5 个商品链接与 100 条公开评论样本，并输出分析
- P1 task_d69157a087: 每 6 小时自动巡检 Twitter/GitHub 上新的商业诊断、客户发现、销售和竞品 skill，评估是否安装，并基于 token-compression startup 更新客户获取建议
- P1 task_cafa7ce59a: Agent API V1 上线计划：完成隐私法律安全调研、竞品宣发调研、用户画像访谈、V1 效果报告和首批用户试点
- P1 task_a85571fd3d: Complete GitHub publish for ancestral-agent-workflow after GitHub auth is available: push codex/ancestral-agent-workflow-skill and open PR
- P1 task_d70fd6ec46: 用 Computer Use 抓取 @xiaoyuZorro X following 1700+ 账号并整理 AI/美股分类列表
