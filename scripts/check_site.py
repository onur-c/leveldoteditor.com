"""Checks the built site: every local link and image exists (anchors included), every page
carries the current shared header and footer, the community links are on the home page,
every image has alt text, and nothing personal or unfinished slipped in.
Prints `CHECK: OK` or the problems and exits 1."""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

SITE = build.SITE
MAX_SITE_BYTES = 8 * 1024 * 1024


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []
        self.ids: set[str] = set()
        self.images_without_alt: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for key in ("href", "src", "srcset"):
            if a.get(key):
                self.refs.append(a[key].split()[0])
        if tag == "img" and a.get("alt") is None:
            self.images_without_alt.append(a.get("src", "?"))


def main() -> int:
    problems: list[str] = []
    pages = sorted(SITE.rglob("*.html"))
    parsed = {}
    for p in pages:
        page = Page()
        page.feed(p.read_text(encoding="utf-8"))
        parsed[p.resolve()] = page
    for p, page in parsed.items():
        rel = p.relative_to(SITE.resolve()).as_posix()
        text = p.read_text(encoding="utf-8")
        prefix = "../" * rel.count("/")
        expected_header = build.header(prefix, "home" if rel == "index.html" else "docs")
        if expected_header not in text:
            problems.append(f"{rel}: the header is not the one scripts/build.py writes (run it)")
        if build.footer(prefix) not in text:
            problems.append(f"{rel}: the footer is not the one scripts/build.py writes (run it)")
        for src in page.images_without_alt:
            problems.append(f"{rel}: image without alt text: {src}")
        if re.search(r'(href|src)="[./]*(style\.css|docs\.js|home\.js)"', text):
            problems.append(f"{rel}: style.css / docs.js without a version (browsers keep an old copy; run scripts/build.py)")
        if "<!--" in text:
            problems.append(f"{rel}: an HTML comment is published (comments belong in content/, run scripts/build.py)")
        if "{{" in text or "TODO" in text:
            problems.append(f"{rel}: unfinished placeholder text")
        if re.search(r"[A-Za-z]:\\\\?Users|@gmail\.com", text):
            problems.append(f"{rel}: a local path or an e-mail address")
        for ref in page.refs:
            if re.match(r"(https?:|mailto:|data:)", ref):
                continue
            if "?" in ref.split("#")[0]:
                ref, _, query = ref.partition("?")
                name = ref.split("/")[-1]
                if query != build.asset_url("", name).split("?")[1]:
                    problems.append(f"{rel}: {name}?{query} is not the current file (run scripts/build.py)")
            path, _, anchor = ref.partition("#")
            target = (p.parent / unquote(path)).resolve() if path else p
            if not target.exists():
                problems.append(f"{rel}: broken link {ref}")
            elif anchor and target in parsed and anchor not in parsed[target].ids:
                problems.append(f"{rel}: no #{anchor} in {path or rel}")
    home = (SITE / "index.html").read_text(encoding="utf-8")
    for name, url in build.LINKS.items():
        if url not in home:
            problems.append(f"index.html: the {name} link {url} is missing")
    size = sum(f.stat().st_size for f in SITE.rglob("*") if f.is_file())
    if size > MAX_SITE_BYTES:
        problems.append(f"the site is {size // 1024} KB, over {MAX_SITE_BYTES // 1024} KB")
    if len(pages) < 1 + len(build.PAGES):
        problems.append(f"only {len(pages)} pages: run scripts/build.py")
    for line in problems:
        print("CHECK: " + line)
    print("CHECK: OK" if not problems else f"CHECK: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
