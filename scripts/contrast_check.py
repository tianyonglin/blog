#!/usr/bin/env python3
"""WCAG 2.1 contrast checker for the blog color system."""

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def blend(fg_hex, bg_hex, alpha):
    fg, bg = hex_to_rgb(fg_hex), hex_to_rgb(bg_hex)
    return tuple(round(f * alpha + b * (1 - alpha)) for f, b in zip(fg, bg))

def lum(rgb):
    def chan(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(c1, c2):
    r1, r2 = (hex_to_rgb(c) if isinstance(c, str) else c for c in (c1, c2))
    l1, l2 = lum(r1), lum(r2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

def grade(r, big=False):
    need = 3.0 if big else 4.5
    return "PASS" if r >= need else "FAIL"

checks = [
    # ---------- 浅色模式 ----------
    ("浅色|正文 #1E293B / 卡片 #FFFFFF", "#1E293B", "#FFFFFF"),
    ("浅色|正文 #1E293B / 页面 #F8FAFC", "#1E293B", "#F8FAFC"),
    ("浅色|次要 #475569 / 卡片 #FFFFFF", "#475569", "#FFFFFF"),
    ("浅色|次要 #475569 / 页面 #F8FAFC", "#475569", "#F8FAFC"),
    ("浅色|品牌蓝 #2563EB / 卡片 #FFFFFF (链接)", "#2563EB", "#FFFFFF"),
    ("浅色|品牌蓝 #2563EB / 页面 #F8FAFC (链接)", "#2563EB", "#F8FAFC"),
    ("浅色|品牌蓝悬停 #1D4ED8 / 卡片 #FFFFFF", "#1D4ED8", "#FFFFFF"),
    ("浅色|按钮白字 #FFFFFF / 品牌蓝 #2563EB", "#FFFFFF", "#2563EB"),
    ("浅色|行内代码 #475569 / 代码底 #F1F5F9 (候选)", "#475569", "#F1F5F9"),
    ("浅色|行内代码 #808080 / 代码底 #F1F5F9 (主题默认)", "#808080", "#F1F5F9"),
    ("浅色|代码块文字 #334155 / 代码底 #F1F5F9 (候选)", "#334155", "#F1F5F9"),
    # 分类徽章
    ("浅色|徽章白字 / 技术蓝 #2563EB", "#FFFFFF", "#2563EB"),
    ("浅色|徽章白字 / 生活青 #0F766E", "#FFFFFF", "#0F766E"),
    ("浅色|徽章白字 / 阅读紫 #7C3AED", "#FFFFFF", "#7C3AED"),
    ("浅色|徽章白字 / 旧青 #2A9D8F (对照)", "#FFFFFF", "#2A9D8F"),
    ("浅色|徽章白字 / 旧珊瑚 #FF6B5E (对照)", "#FFFFFF", "#FF6B5E"),
    ("浅色|徽章白字 / 旧紫 #8D6CE8 (对照)", "#FFFFFF", "#8D6CE8"),
    # 提示框（浅色）
    ("浅色|提示框 note 标题 #2563EB / #EFF6FF", "#2563EB", "#EFF6FF"),
    ("浅色|提示框 tip 标题 #15803D / #F0FDF4", "#15803D", "#F0FDF4"),
    ("浅色|提示框 important 标题 #6D28D9 / #F5F3FF", "#6D28D9", "#F5F3FF"),
    ("浅色|提示框 warning 标题 #B45309 / #FFFBEB", "#B45309", "#FFFBEB"),
    ("浅色|提示框 caution 标题 #B91C1C / #FEF2F2", "#B91C1C", "#FEF2F2"),
    # ---------- 深色模式 ----------
    ("深色|正文 #E5E7EB / 卡片 #111827", "#E5E7EB", "#111827"),
    ("深色|正文 #E5E7EB / 页面 #0B1220", "#E5E7EB", "#0B1220"),
    ("深色|次要 #AAB6C5 / 卡片 #111827", "#AAB6C5", "#111827"),
    ("深色|次要 #AAB6C5 / 页面 #0B1220", "#AAB6C5", "#0B1220"),
    ("深色|品牌蓝 #60A5FA / 卡片 #111827 (链接)", "#60A5FA", "#111827"),
    ("深色|品牌蓝 #60A5FA / 页面 #0B1220 (链接)", "#60A5FA", "#0B1220"),
    ("深色|品牌蓝悬停 #93C5FD / 卡片 #111827", "#93C5FD", "#111827"),
    ("深色|按钮深字 #0B1220 / 品牌蓝 #60A5FA", "#0B1220", "#60A5FA"),
]

print(f"{'组合':<58}{'对比度':>8}  结论")
print("-" * 78)
for name, fg, bg in checks:
    r = ratio(fg, bg)
    print(f"{name:<58}{r:>7.2f}:1  {grade(r)}")

# alpha 混合的特殊项
print()
print("Alpha 混合项：")
dark_code_text = blend("#FFFFFF", "#0F172A", 0.9)   # rgba(255,255,255,.9) on #0F172A
r = ratio(dark_code_text, "#0F172A")
print(f"{'深色|代码文字 rgba(255,255,255,.9) / #0F172A':<58}{r:>7.2f}:1  {grade(r)}")

# 深色提示框：背景用 alpha 叠加在卡片 #111827 上
dark_alerts = [
    ("note",      "#3B82F6", 0.14, "#93C5FD"),
    ("tip",       "#22C55E", 0.14, "#4ADE80"),
    ("important", "#8B5CF6", 0.14, "#C4B5FD"),
    ("warning",   "#F59E0B", 0.14, "#FBBF24"),
    ("caution",   "#EF4444", 0.14, "#FCA5A5"),
]
for t, tint, a, title in dark_alerts:
    bg = blend(tint, "#111827", a)
    bg_hex = "#{:02X}{:02X}{:02X}".format(*bg)
    r = ratio(title, bg_hex)
    print(f"{'深色|提示框 %s 标题 %s / 混合底 %s' % (t, title, bg_hex):<58}{r:>7.2f}:1  {grade(r)}")
