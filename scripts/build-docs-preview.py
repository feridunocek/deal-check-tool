#!/usr/bin/env python3
"""Copy the result page template into docs/app/ for the landing page preview.

docs/app/deal-check.html     = app/deal-check.html as it is (English example run)
docs/app/deal-check.tr.html  = same template, data from examples/example-2026-11-21.tr.json
Run after changing app/deal-check.html: python3 scripts/build-docs-preview.py
"""
import json, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "app/deal-check.html").read_text(encoding="utf-8")
out = root / "docs/app"
out.mkdir(parents=True, exist_ok=True)
(out / "deal-check.html").write_text(tpl, encoding="utf-8")

tr = json.loads((root / "examples/example-2026-11-21.tr.json").read_text(encoding="utf-8"))
block = '<script type="application/json" id="deal-data">\n' + json.dumps(tr, ensure_ascii=False, indent=2) + "\n</script>"
new, n = re.subn(r'<script type="application/json" id="deal-data">.*?</script>', lambda m: block, tpl, flags=re.S)
assert n == 1, "data block not found"
(out / "deal-check.tr.html").write_text(new.replace('<html lang="en">', '<html lang="tr">'), encoding="utf-8")
print("ok")
