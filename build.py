"""Wrap index.html (the Claude artifact source) into a standalone page for GitHub Pages at docs/index.html."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "index.html").read_text()
if body.startswith('<meta charset="utf-8">'):
    body = body.split("\n", 1)[1]
page = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
    "<style>[hidden]{display:none!important}</style>\n"
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(page)
print("wrote docs/index.html")
