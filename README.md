# 拾贝集 · The Beachcomber —— Hugo 个人博客

基于 **Hugo + Stack 主题**（卡片式设计）的专业化个人博客。
Markdown 写作（支持内联 HTML）、图片/标签/分类/搜索/评论/统计/深浅色/SEO 结构化数据一应俱全。

📚 **完整建设方案见 [`docs/`](docs/)（13 部分：选型、部署、SEO、安全、性能、运维……）**

## 目录结构

```
blog/
├── .github/workflows/hugo.yml   自动构建部署（GitHub Actions，已锁定 Hugo 版本）
├── config/_default/
│   ├── hugo.toml                ★ baseURL（上线前必改）、统计入口
│   ├── languages.toml           ★ 中英文站名、侧边栏标语
│   ├── menu.toml                导航菜单（首页/文章/分类/项目/关于）+ 社交图标
│   ├── markup.toml              Markdown/HTML/公式渲染（HTML 已开启）
│   └── params.toml              ★ 头像、评论、小部件、作者名
├── content/
│   ├── post/                    ★ 文章（每篇一个文件夹：index.md + cover.jpg + 插图）
│   ├── page/                    功能页：关于/归档/搜索/项目/友链/隐私/更新日志
│   └── categories/              分类元数据（名称/描述/徽章颜色）
├── assets/scss/custom.scss      ★ 自定义配色（珊瑚橙主题，改变量即换肤）
├── layouts/_partials/
│   ├── head/custom.html         JSON-LD 结构化数据 + 统计代码位
│   └── footer/custom.html       页脚导航 + 阅读进度条 + 返回顶部 + 分享按钮
├── static/
│   ├── img/avatar.png           ★ 头像/favicon（换成你的）
│   └── robots.txt               ★ 上线前改里面的域名
├── themes/hugo-theme-stack/     主题（只读）
└── docs/                        完整建设方案（13 篇）
```

## ✍️ 写文章

```
content/post/my-new-post/
├── index.md      ← front matter（title/date/slug/categories/tags/description）+ Markdown 正文
├── cover.jpg     ← 封面，自动出现在首页卡片/分享预览/JSON-LD
└── 插图.jpg       ← ![](插图.jpg) 直接引用，自动懒加载 + 点击放大
```

格式示范见已发布文章《写作指南：这个博客支持的全部格式》（含表格、公式、Mermaid、提示框、HTML 折叠块）。

## 💬 评论 / 📊 统计（待你启用）

- **评论**：`params.toml` → `[comments]`，giscus 教程见 `docs/13`（约 5 分钟）
- **统计**：三选一，配置位见 `layouts/_partials/head/custom.html` 顶部注释与 `docs/07`

## 🚀 部署（详见 docs/05）

**GitHub Pages（推荐）**：仓库 Settings → Pages → Source 选 **GitHub Actions** → 推送即发布。
**Cloudflare Pages（备选）**：Framework 选 Hugo，命令 `hugo -b $CF_PAGES_URL`，输出目录 `public`，环境变量 `HUGO_VERSION=0.167.0`。

绑域名：改 `hugo.toml` 的 `baseURL` → Pages 填 Custom domain → 注册商加 DNS 记录（表格见 `docs/06`）→ 开启强制 HTTPS。

## 🎨 上线前个性化清单（全局搜 ⚠️ 定位）

- [ ] `hugo.toml` baseURL、`robots.txt` 域名
- [ ] `languages.toml` 站名与标语、`menu.toml` GitHub 链接
- [ ] `params.toml` 作者昵称（authorName）
- [ ] 关于 / 项目 / 友链页占位内容、`static/img/avatar.png` 头像
- [ ] 示例文章改写或删除
- [ ] 评论/统计启用并同步更新隐私政策页

## 🖥️ 本地预览（可选）

安装 Hugo **extended** 版（<https://github.com/gohugoio/hugo/releases>），在 `blog/` 下运行 `hugo server`。
不装也完全不影响发布 —— GitHub Actions 替你构建。
