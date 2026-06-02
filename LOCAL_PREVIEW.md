# 本地预览

本项目使用标准 MkDocs 结构：`mkdocs.yml` 位于项目根目录，正文、图片、样式等站点资源位于 `docs/` 目录。

## 环境

需要本机能够运行：

- Node.js / npm
- Python
- MkDocs 及项目所需 Python 插件

项目脚本通过 `package.json` 统一入口运行。

## 构建站点

```powershell
npm run docs:build
```

构建产物会生成到 `site/` 目录。`site/` 是生成目录，已在 `.gitignore` 中忽略，不需要提交到 GitHub。

## 实时预览

```powershell
npm run docs:serve
```

然后访问：

```text
http://127.0.0.1:4173/
```

`docs:serve` 会监听 `docs/` 和 `mkdocs.yml`。修改源文件后，预览脚本会自动重新构建，并刷新浏览器页面。

## 维护说明

- 只编辑 `docs/` 中的 Markdown、图片、样式等源文件。
- 不要直接编辑 `site/`，它会在每次构建时重新生成。
- 提交前建议运行一次 `npm run docs:build`，确认站点可以完整构建。
- 如果本地出现 `site/`、缓存目录或其他生成产物，可以直接删除后重新构建。
