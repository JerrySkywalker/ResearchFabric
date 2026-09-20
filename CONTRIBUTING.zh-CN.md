# 贡献指南

ResearchFabric 欢迎对公共架构、理念、术语、示例和文档检查工具进行聚焦改进。

提交变更前：

1. 确保英文与简体中文对应文档在含义上保持一致。
2. 保持 Vault／Design Lab 的权威分工以及门户的非运行时角色。
3. 不得导入组件源码、私有协调记录、研究数据、凭据、聊天记录或机器专属路径。
4. 区分事实、提案、证据和已采纳决策；不得把智能体输出描述为科学证据。
5. 除非公共门户存在明确需求，否则不要加入框架、中间件、子模块或复杂自动化。
6. 运行 `python scripts/check_bilingual_docs.py`、`python -m py_compile scripts/check_bilingual_docs.py` 与 `git diff --check`。

建议提交小而明确的拉取请求，并同步更新双语文档。组件行为变更应提交到对应组件仓库。

