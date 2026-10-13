---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
slug: ""                # 留空则用文件名做 URL，也可写英文短名
image: cover.jpg        # 封面图：把图片放进文章文件夹即可
categories: ["生活"]     # 分类（只能选一个，如：技术 / 生活 / 阅读）
tags: ["标签1", "标签2"] # 标签（可以多个）
description: "一句话摘要，会显示在首页卡片上"
draft: false
---

正文从这里开始，支持 **Markdown**，也可以直接写 HTML。
