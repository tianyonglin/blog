---
title: "写作指南：这个博客支持的全部格式"
date: 2026-10-06
slug: markdown-tips
image: cover.jpg
categories: ["技术"]
tags: ["Markdown", "写作", "教程"]
description: "标题、列表、引用、代码块、表格、图片、HTML 富文本……一篇文章看懂在这个博客里怎么写。"
---

这个博客用 Markdown 写作，同时支持直接写 HTML。这篇文章本身就是一个「格式示范」，把会用到的写法都过一遍。

<!--more-->

## 新建一篇文章

每篇文章是一个**文件夹**，里面放 `index.md` 和图片：

```text
content/post/my-new-post/
├── index.md      ← 文章正文（Markdown）
├── cover.jpg     ← 封面图（文件名固定为 cover）
└── 其他图片.jpg   ← 正文插图，直接 ![](文件名) 引用
```

`index.md` 开头是 front matter（文章信息）：

```yaml
---
title: "文章标题"
date: 2026-10-06
image: cover.jpg
categories: ["技术"]        # 分类：只能一个
tags: ["Markdown", "教程"]  # 标签：可以多个
description: "显示在首页卡片上的摘要"
---
```

## 常用 Markdown 语法

### 文字样式

**加粗**、*斜体*、~~删除线~~、`行内代码`，以及[链接](/)。

### 列表

1. 有序列表第一项
2. 有序列表第二项

- 无序列表
- 可以嵌套
  - 像这样

- [ ] 任务清单也可以
- [x] 已经完成的项

### 引用

> 引用别人的话，或者标注重点，都会变成这样的小卡片。
> 可以写好几行。

### 代码块

````markdown
```python
def hello():
    print("Hello, World!")
```
````

渲染成：

```python
def hello():
    print("Hello, World!")
```

### 表格

| 语法 | 作用 |
| --- | --- |
| `#` 号 | 标题层级 |
| `>` | 引用块 |
| `![](...)` | 插入图片 |

### 数学公式（LaTeX）

行内公式：$E = mc^2$；块级公式：

$$
\int_{-\infty}^{+\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## 图片的两种放法

**方式一：图注图片**（推荐，自带居中边框和说明文字）

```markdown
![图片说明文字](street-1.jpg)
```

**方式二：普通图片**，把图片文件放在文章文件夹里，直接按文件名引用即可，本站主题会自动做响应式缩放。

## 直接写 HTML 也可以

本博客开启了 `unsafe = true`，Markdown 里可以直接混写 HTML 富文本：

<details>
<summary>点我展开：这是一个 HTML 折叠块</summary>

可以把补充说明、剧透、彩蛋放在这里。

</details>

按 <kbd>Ctrl</kbd> + <kbd>D</kbd> 可以把本页加入书签 —— 这个键盘按键样式就是 HTML 的 `<kbd>` 标签。

## Mermaid 流程图

用 ` ```mermaid ` 代码块直接画图：

````markdown
```mermaid
flowchart LR
    A[写 Markdown] --> B[git push]
    B --> C[GitHub Actions 构建]
    C --> D[自动发布上线]
```
````

渲染成：

```mermaid
flowchart LR
    A[写 Markdown] --> B[git push]
    B --> C[GitHub Actions 构建]
    C --> D[自动发布上线]
```

## 提示框（GitHub 风格 Alerts）

```markdown
> [!TIP]
> 重要的经验或建议放在这里。

> [!WARNING]
> 容易踩的坑放在这里。
```

> [!TIP]
> 重要的经验或建议放在这里，读者一眼就能看到重点。

> [!WARNING]
> 容易踩的坑放在这里，提前预警。

## 终端命令与输出

写教程时，命令和输出分开展示更清晰：

```bash
# 在博客根目录执行
hugo new post/my-post/index.md   # 新建文章
git add -A && git commit -m "post: my new post"
git push                          # 推送后自动构建上线
```

---

格式就这么多。剩下的，交给内容本身。
