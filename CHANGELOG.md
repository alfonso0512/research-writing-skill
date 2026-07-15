# Changelog

All notable changes to the research-writing skill.

## [3.0.0] - 2026-07-15

### Added
- 新增 `references/prompts/` 目录：30 个 Prompt 模板拆分为独立文件，按需加载，大幅减少上下文占用
- 新增 `scripts/escape_latex.py`：确定性 LaTeX 特殊字符转义工具
- 新增 `scripts/title_case.py`：Title Case / Sentence case 转换工具
- SKILL.md 新增决策树：5 大常见场景的 Prompt 使用流程指引
- Frontmatter 新增 `compatibility` 字段和反触发模式

### Changed
- **重构**：SKILL.md 从 50KB/970 行瘦身至 ~3KB/100 行，仅保留索引、决策树和路由逻辑
- **统一**：所有 Prompt 的角色头格式统一（中文 Prompt 用 `## 角色`，英文用 `## Role`）
- **统一**：变量命名规范化为 `{{VARIABLE_NAME}}` 大写格式
- **强化**：#10 缩写检查 Prompt 从 13 行扩展至 50+ 行，增加约束规则、执行步骤和格式化输出
- **重写**：#17 从"模型选择推荐"改为"AI 写作辅助工具选择"，聚焦科研写作场景
- README: "30+" 修正为 "30"
- Frontmatter: `author` 修正为 "alfonso0512"，`version` 升至 3.0.0

### Removed
- 移除 .gitignore 中的个人偏好条目（`notes/`、`private/`）

## [2.0.0] - 2026-03-18

### Added
- 30 个科研论文写作 Prompt 模板
- 覆盖文献调研→写作→润色→投稿→基金申请全流程
- README、QUICKSTART、DEPLOY 文档
- MIT License

[3.0.0]: https://github.com/alfonso0512/research-writing-skill/compare/v2.0.0...v3.0.0
[2.0.0]: https://github.com/alfonso0512/research-writing-skill/releases/tag/v2.0.0
