<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/wordmark-dark.svg" />
    <img src="docs/images/wordmark-light.svg" alt="King-design" width="960" />
  </picture>
</p>

<p align="center">
  <strong>King-design</strong> — حوّل منتجك أو موقعك أو فكرتك إلى فيلم موشن متكامل.<br />
  اختر الأسلوب. كيّف البرومبت. ولّد عبر Higgsfield.
</p>

<p align="center">
  <strong>يعمل على أي وكيل</strong> &nbsp; / &nbsp; 10 أساليب موشن &nbsp; / &nbsp; مهارة واحدة &nbsp; / &nbsp; Higgsfield MCP
</p>

<p align="center">
  <a href="README.md">🇺🇸 English</a> &nbsp;·&nbsp;
  <a href="https://mot1209.github.io/King-design/"><strong>🌐 المعرض المباشر</strong></a> &nbsp;·&nbsp;
  <a href="install.sh">⚡ تثبيت بسطر واحد</a> &nbsp;·&nbsp;
  <a href="LICENSE">MIT</a>
</p>

<p align="center">
  <sub>إصدار <strong>King-design v5.0.0</strong> — تطوير من <a href="https://github.com/cth9191/motion-design">cth9191/motion-design</a> ليعمل على أي وكيل</sub>
</p>

---

## 👑 ما هو King-design؟

**King-design** هو تطوير عربي لـ `motion-design` — مهارة موحدة تجعل أي وكيل ذكاء اصطناعي (Codex / Claude Code / Cursor / Pi / Windsurf / أي وكيل يدعم MCP) قادر على تحويل فكرتك إلى فيلم موشن 15 ثانية بأسلوب احترافي.

> **الأصل:** cth9191/motion-design (Codex + Claude فقط) → **الآن:** MOT1209/King-design (أي وكيل + عربي + Pages + MIT)

## 🎬 مكتبة الموشن

من الواجهات الزجاجية إلى كشف المنتجات — ابدأ باتجاه بصري يمكنك مشاهدته فعلاً. **اضغط أي صورة لتشغيل الفيلم الأصلي.**

> المعرض المباشر: **https://mot1209.github.io/King-design** — يعمل بدون تحميل، انسخ الطلب والصقه في وكيلك

| الأسلوب | الوصف | الأفضل لـ |
|---|---|---|
| **Glass UI launch** | ألواح زجاجية تحمل المنتج من المشكلة إلى الحل | SaaS وأدوات AI |
| **Tropical product** | تصوير استوائي بطيء + مكونات معلقة | مشروبات وعطور |
| **Kinetic typography** | حروف تتحرك — عناوين وبطاقات وأيقونات | إعلانات ودورات |
| **Blueprint to building** | خطوط المخطط ترتفع وتصبح مبنى | عقارات وعمارة |
| **Exploded product** | تفكيك المنتج على محور واحد مع ماكرو | ساعات وسماعات |
| **Flat vector explainer** | شخصية مسطحة تتحول عبر 3 حالات | تطبيقات وخدمات |
| **+ 4 أساليب أخرى** | hyper-motion, hybrid 2D+3D, collage, footage | — |

## ⚡ التثبيت السريع — أي وكيل

### بسطر واحد (موصى به)

```sh
curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash
# مع تحديد الوكيل:
curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash -s -- --agent pi
curl -fsSL https://raw.githubusercontent.com/MOT1209/King-design/main/install.sh | bash -s -- --agent claude
```

### يدوي

```sh
git clone https://github.com/MOT1209/King-design.git /tmp/King-design
cp -r /tmp/King-design/skills/motion-design ~/.claude/skills/motion-design  # Claude Code
cp -r /tmp/King-design/skills/motion-design ~/.pi/agent/skills/motion-design  # Pi
cp -r /tmp/King-design/skills/motion-design .cursor/skills/motion-design       # Cursor
# أو ./skills/motion-design لأي وكيل عام
```

راجع [دليل الإعداد الشامل](docs/setup-universal.md) و [النسخة العربية](docs/setup-universal.ar.md)

### ربط Higgsfield (للتوليد فقط)

```
الرابط الموحد: https://mcp.higgsfield.ai/mcp
Claude: claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
Pi:     pi mcp add higgsfield --transport http --url https://mcp.higgsfield.ai/mcp
Cursor: Settings → MCP → Add HTTP Server
```

بدون ربط؟ يمكنك التصفح وتصدير البرومبت واستخدامه في موقع Higgsfield مباشرة — المعرض والبرومبت يعملان **بدون اتصال**.

### 🎬 اصنع أول فيلم

في وكيلك اكتب `motion-design` (أو `$motion-design` / `/motion-design` حسب الوكيل):

```
استخدم kinetic typography لإعلان 15 ثانية:
"ابنِ أول سير عمل AI خاص بك."
موسيقى + مؤثرات بدون سرد.
أرني البرومبت الكامل قبل التوليد.
```

## ⚙️ كيف يعمل

**اختر → كيّف → ولّد → راجع**

ينطلق من البرومبت الأصلي الكامل لأقرب مثال، ويحافظ على تقنيات الحركة الفعالة مع تكييف المشاهد والتوقيت لموضوعك. يُرسل الفيلم كـ **طلب واحد متكامل** عبر Higgsfield MCP (يفضل Seedance).

| | أي وكيل (كشف تلقائي) |
|---|---|
| **صور مرجعية** | أداة الوكيل الأصلية إن وجدت → وإلا Higgsfield `GPT Image 2` |
| **الفيلم الكامل** | Higgsfield MCP — Seedance (أي وكيل مع MCP) · تصدير برومبت بدون MCP |
| **بدون توليد** | يعمل في كل مكان بدون اتصال |

راجع [SKILL.md](skills/motion-design/SKILL.md) و [tool-routing.md](skills/motion-design/references/tool-routing.md) للتفاصيل.

## 📦 ما الجديد في King-design v5.0.0

- ✅ يعمل على **أي وكيل** (7 محولات: Codex/Claude/Cursor/Pi/Windsurf/Gemini/Generic)
- ✅ تثبيت **سطر واحد** + Pages مباشر
- ✅ **عربي كامل** + MIT License + npm `@mot1209/king-design`
- ✅ فحص `validate` + نشر `gh-pages` تلقائي

## 📄 الترخيص

MIT — راجع [LICENSE](LICENSE). البرومبتات الأصلية ومقاطع المعاينة ملك Higgsfield — راجع [ATTRIBUTION.md](ATTRIBUTION.md).

---

<p align="center">صنع بـ ❤️ بواسطة <a href="https://github.com/MOT1209">MOT1209</a> — <strong>King-design</strong> 👑 يعمل على أي وكيل</p>
<p align="center"><a href="https://github.com/MOT1209/King-design">⭐ نجّم المشروع</a> · <a href="https://mot1209.github.io/King-design">🌐 المعرض</a> · <a href="CHANGELOG.md">📝 السجل</a></p>
