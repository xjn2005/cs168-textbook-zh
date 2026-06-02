# CS 168 Textbook 中文翻译状态


## 当前状态

- 翻译状态：已完成。
- 站点结构：`mkdocs.yml` 在项目根目录，内容源文件在 `docs/`。
- 构建产物：`site/` 由 MkDocs 生成，不提交到 GitHub。
- 本地验证：提交前建议运行 `npm run docs:build`。

## 已完成章节

- Introduction
- Routing
- Transport
- Applications
- End-to-End
- Datacenters
- Beyond Client-Server
- Wireless
- Glossary

## 翻译与维护规范

- `mkdocs.yml` 的导航项和 front matter 中的 `title` 保持英文，除非后续明确决定整体本地化导航。
- 正文使用自然、清楚、专业的中文，保持课程讲义风格。
- 常见网络术语按项目既有风格保留英文，例如 `packet`、`header`、`router`、`switch`、`flow`、`protocol`、`routing`、`sender`、`recipient`。
- 固定表达 `benchmark` 和 `trade-off` 保留英文。
- 专业术语、协议名、算法名、字段名、标准名和专有名词可以保留英文；普通表达应译成中文。
- 首次出现且有助于理解的术语，可以使用中文解释搭配英文术语；后续保持一致，不重复解释。
- 保留原文 Markdown 结构、图片路径、页面层级、公式、表格、代码和链接。
- 中文正文使用中文标点，并在中文与英文、中文与数字之间保留合适空格。
- 行内公式使用 `$...$`；独立成行的展示公式使用 `$$...$$`。

## 提交前检查

- 运行 `npm run docs:build`，确认站点可以完整构建。
- 确认没有提交 `site/`、缓存目录或临时文件。
- 抽查修改过的页面，确认没有乱码、残留英文正文、损坏图片路径或公式渲染问题。
