# Changelog

## 5.0.0 — 2026-09-15 — Universal Edition

### 🚀 Universal Agent Support
- `SKILL.md` أصبح يكتشف القدرات تلقائياً — يعمل على أي وكيل يقرأ `SKILL.md`
- `tool-routing.md` مصفوفة عامة بدل Codex/Claude فقط — Higgsfield MCP هو نفسه في كل الوكلاء
- `gallery.html` يدعم 6 وكلاء: Codex / Claude Code / Cursor / Pi / Windsurf / Generic
- `agents/` — 7 محولات: openai, claude, cursor, pi, windsurf, gemini, generic

### 📦 Professionalize
- `LICENSE` MIT + ملاحظة Higgsfield في ATTRIBUTION
- `install.sh` مثبت سطر واحد: `curl -fsSL ... | bash` مع `--agent` flag
- `README.ar.md` عربي كامل + badge للمعرض المباشر في README.md
- `.github/workflows/pages.yml` نشر المعرض على `https://mot1209.github.io/King-design`
- `.github/ISSUE_TEMPLATE/` قوالب بلاغات عربية

### 🔧 Fixes
- `pages.yml` enablement=true لإنشاء Pages تلقائياً
- `validate.yml` يفحص LICENSE والوكلاء

---

## 4.x — Upstream (cth9191)

- 10 presets v4 مع SHA256 + gallery + adaptation guides
- انظر `ROADMAP.md` في الأصل
