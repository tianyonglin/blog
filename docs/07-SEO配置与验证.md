# 第七部分：SEO 配置与验证

> 原则：**技术上做到位，不承诺收录与排名**。收录与排名取决于内容质量、外链与搜索算法。

## 1. 十七项要素逐项落实

| # | 要素 | 状态 | 实现位置 / 配置 |
|---|------|------|----------------|
| 1 | 每篇独立 Title + Description | ✅ | 文章 front matter `title` / `description`；`description` 会进 meta 与分享卡片，**每篇必写**（约 60~120 字） |
| 2 | H1/H2/H3 层级 | ✅ | 主题渲染：文章标题=唯一 H1，正文 `##`=H2；写作时**不要用一级标题**、不跳级 |
| 3 | 简洁稳定 URL | ✅ | `hugo.toml` 固定链接 `/p/:slug/`；写作时 front matter `slug` 用**小写英文短横线**（如 `hugo-deploy`），一经发布不再改 |
| 4 | XML Sitemap | ✅ | Hugo 内置生成 `/sitemap.xml`（构建后可访问验证） |
| 5 | robots.txt | ✅ | `static/robots.txt`（含 sitemap 地址，⚠️上线前改域名） |
| 6 | Canonical | ✅ | 主题 head 输出 `<link rel="canonical">`；如需指向他处可在 front matter 加 `canonicalUrl` |
| 7 | Open Graph | ✅ | 主题输出 og:title/description/image/type/url（文章封面自动作 og:image） |
| 8 | Twitter Card | ✅ | 主题输出 summary_large_image（`params.toml [opengraph.twitter]` 可填你的账号） |
| 9 | JSON-LD 结构化数据 | ✅ | `layouts/_partials/head/custom.html`：首页 WebSite+SearchAction；文章 BlogPosting（标题/发布与更新时间/作者/字数/封面/关键词） |
| 10 | 作者 + 发布/更新时间 | ✅ | 文章页显示；`lastmod` 更新后显示「更新于…」并写入 JSON-LD 的 `dateModified` |
| 11 | 图片 ALT | ⚠️写作纪律 | `![必填描述](图片)`；无意义装饰图写 `![]()`（空 alt） |
| 12 | 内链 + 相关推荐 | ✅ | 主题内置相关文章模块；写作中多用站内相对链接 |
| 13 | RSS/Atom | ✅ | `/index.xml`（全文 RSS）；侧边栏与页脚入口 |
| 14 | Google Search Console | ⏳待你操作 | 见第 2 节 |
| 15 | Bing Webmaster | ⏳待你操作 | 见第 2 节 |
| 16 | 索引/抓取异常/死链监控 | ⏳待你操作 | GSC「网页索引」报告 + 死链检查见文档 11 |
| 17 | Core Web Vitals | ✅基线良好 | 静态站+系统字体+懒加载；检测流程见文档 09 |

## 2. 注册搜索引擎站长平台（上线后执行）

### Google Search Console（GSC）

1. 打开 <https://search.google.com/search-console>，用 Google 账号登录；
2. 添加资源：选 **网域**（需 DNS TXT 验证，按页面提示在注册商加 TXT 记录）或 **网址前缀**（推荐：填 `https://sunmusic.top/`，用 HTML 标记验证——把给到的 `<meta name="google-site-verification" ...>` 粘贴进 `layouts/_partials/head/custom.html` 顶部，推送发布后点验证）；
3. 左侧 **站点地图** → 提交 `sitemap.xml`；
4. 新文章发布后，用顶部 **网址检查** → 请求编入索引（不必每篇都做，重要文章即可）。

### Bing Webmaster Tools

1. 打开 <https://www.bing.com/webmasters>，微软账号登录；
2. 可直接**从 GSC 导入**（推荐，一键）；或同 GSC 方式验证；
3. 提交 `sitemap.xml`。

### 验证配置是否生效（工具箱）

| 工具 | 用途 | 地址 |
|---|---|---|
| 富媒体结果测试 | 校验 JSON-LD 是否合法 | <https://search.google.com/test/rich-results> |
| OG 预览 | 分享卡片效果 | 微信无法本地测，可用 Telegram 粘贴链接预览 |
| robots 校验 | GSC 内 Settings → robots.txt | GSC 面板 |
| `site:` 查询 | 查看收录情况（发布 1~2 周后） | 搜索引擎输入 `site:sunmusic.top` |

## 3. SEO 写作规范（比任何配置都重要）

1. 标题包含主题关键词，不标题党，≤ 30 个汉字；
2. 每篇写满 `description`；
3. 开头两段讲清楚“这篇文章解决什么”；
4. 用 H2/H3 组织，小节自带关键词；
5. 图片填 ALT；代码块标注语言；
6. 站内互链：新文章引用 2~3 篇旧文，旧文酌情回链；
7. 改版/换域名时用 301 重定向，绝不让旧链接裸奔（Cloudflare 可用 Redirect Rules）。
