# الإعداد الشامل — أي وكيل (عربي)

يعمل على **أي وكيل** يقرأ `SKILL.md`. المعرض وكتابة البرومبت يعملان بدون حساب. التوليد يحتاج Higgsfield MCP.

## 1. التثبيت

```sh
curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash
# مع تحديد الوكيل:
curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash -s -- --agent pi
```

أو يدوياً:

| الوكيل | المسار |
|---|---|
| Claude Code | `~/.claude/skills/motion-design` |
| Pi | `~/.pi/agent/skills/motion-design` |
| Cursor | `.cursor/skills/motion-design` |
| عام | `./skills/motion-design` |

## 2. ربط Higgsfield (للتوليد فقط)

الرابط الموحد: `https://mcp.higgsfield.ai/mcp`

- Claude: `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`
- Pi: `pi mcp add higgsfield --transport http --url https://mcp.higgsfield.ai/mcp`
- Cursor: Settings → MCP → Add HTTP

بدون ربط؟ صدّر البرومبت واستخدمه في موقع Higgsfield مباشرة.

## 3. جرّب بدون توليد

```
استخدم kinetic typography لإعلان 15 ثانية: "ابنِ أول سير عمل AI"
موسيقى + مؤثرات بدون سرد — أرني البرومبت قبل التوليد
```

## 4. المعرض

https://mot1209.github.io/King-design
أو محلياً: `python -m http.server 8765 --directory skills/motion-design` ثم افتح `/assets/gallery.html`
