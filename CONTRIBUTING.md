# المساهمة

## إضافة Preset جديد

1. شاهد الفيديو الأصلي واحفظ البرومبت الكامل في `references/source-prompts/<id>.txt`
2. احسب `SHA256` وأضف المدخل في `assets/presets.json`
3. اكتب `references/presets/<id>.md` و `references/templates/<id>.md` (يجب أن يحتوي كلاهما على `` `id` ``)
4. شغّل `python skills/motion-design/scripts/build_gallery.py` — سيتحقق من الـ timeline ويبني الـ gallery
5. تأكد أن `validate` ينجح

## الترجمة

- `README.ar.md` للعربية — حافظ على الروابط نفسها
- المعرض يدعم العربية عبر `gallery.html` — أضف ترجمات في `presets.json` إذا لزم

## الـ Agents

- كل وكيل له ملف في `agents/<name>.yaml` — انسخ `generic.yaml` وعدّل `install.hint`

## الإصدارات

- حدّث `VERSION` و `CHANGELOG.md` ثم `git tag vX.Y.Z && git push --tags`
