"""Builds the documentation pages of the Leveldot site from the editor's own user docs.

The docs have one source: docs/*.md in the Leveldot editor repository (the same text the
editor shows on F1). This script reads them from that repository's committed `master`
(never its working copy), turns them into site/docs/*.html and puts the shared header into
every page, site/index.html included. Run it after the editor's docs changed:

    python scripts/build.py [--source <editor repo>] [--ref master]

The editor repository is found by --source, else $LEVELDOT_EDITOR_REPO, else the first line
of `.source-path` in this repository (git-ignored, one per machine).
"""
from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

LINKS = {
    "itch": "https://onur-c.itch.io/leveldot-editor",
    "discord": "https://discord.gg/e3CdgVQxp",
    "youtube": "https://www.youtube.com/@LeveldotEditor",
}

# (output file, nav label, page title, source in the editor repo, part of it)
PAGES = [
    ("index.html", "Install", "Install and first steps", "docs/MANUAL.md", "getting-started"),
    ("link-godot.html", "Link Godot", "Link a Godot project", "docs/LINK-GODOT.md", "all"),
    ("tools.html", "Tools", "Tools", "docs/MANUAL.md", "tools"),
    ("shortcuts.html", "Shortcuts", "Commands and keyboard shortcuts", "docs/SHORTCUTS.md", "all"),
    ("tutorial.html", "Tutorial", "Tutorial", "docs/TUTORIAL.md", "all"),
]
# Links between the editor's docs become links between the pages.
DOC_TARGETS = {"MANUAL.md": "tools.html", "LINK-GODOT.md": "link-godot.html",
               "SHORTCUTS.md": "shortcuts.html", "TUTORIAL.md": "tutorial.html"}

ICONS = {
    "download": '<path d="M12 3v12m0 0-5-5m5 5 5-5M4 19h16"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5Z"/><path d="M4 21a2 2 0 0 1 2-2h13"/>',
    "discord": '<path d="M5 6.5C7 5.2 9 4.6 12 4.6s5 .6 7 1.9c1.4 2.6 2 5.4 1.8 8.6-1.6 1.5-3.4 2.5-5.3 3l-1.1-1.9M5 6.5C3.6 9.1 3 11.9 3.2 15.1c1.6 1.5 3.4 2.5 5.3 3l1.1-1.9M7.5 16c2.9 1.3 6.1 1.3 9 0"/><circle cx="9.2" cy="12" r="1.1"/><circle cx="14.8" cy="12" r="1.1"/>',
    "youtube": '<rect x="2.5" y="5.5" width="19" height="13" rx="3.5"/><path d="m10.2 9.3 4.6 2.7-4.6 2.7V9.3Z"/>',
    "itch": '<path d="M3 9.5 5 4h14l2 5.5M3 9.5c0 1.4 1 2.5 2.25 2.5S7.5 10.9 7.5 9.5c0 1.4 1 2.5 2.25 2.5S12 10.9 12 9.5c0 1.4 1 2.5 2.25 2.5s2.25-1.1 2.25-2.5c0 1.4 1 2.5 2.25 2.5S21 10.9 21 9.5M5 12v8h14v-8M10 20v-4h4v4"/>',
}


def icon(name: str) -> str:
    return ('<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


def header(prefix: str, current: str) -> str:
    """The bar on top of every page; `prefix` leads from the page to the site root."""
    def nav(href: str, label: str, key: str, name: str, external: bool = False) -> str:
        attrs = ' target="_blank" rel="noopener"' if external else ""
        here = ' aria-current="page"' if key == current else ""
        return f'<a class="nav-link" href="{href}"{attrs}{here}>{icon(name)}<span>{label}</span></a>'
    return f"""<!-- header (scripts/build.py writes this block) -->
<header class="top">
  <div class="top-inner">
    <a class="brand" href="{prefix}index.html" aria-label="Leveldot home">
      <picture>
        <source srcset="{prefix}img/logo-light.png" media="(prefers-color-scheme: light)">
        <img src="{prefix}img/logo-dark.png" alt="Leveldot" width="144" height="31">
      </picture>
    </a>
    <nav class="top-nav" aria-label="Site">
      {nav(prefix + "docs/index.html", "Docs", "docs", "book")}
      {nav(LINKS["discord"], "Discord", "", "discord", True)}
      {nav(LINKS["youtube"], "YouTube", "", "youtube", True)}
      <a class="button primary small" href="{LINKS["itch"]}" target="_blank" rel="noopener">{icon("download")}<span>Download</span></a>
    </nav>
  </div>
</header>
<!-- /header -->"""


def find_source(arg: str | None) -> Path:
    candidates = [arg, os.environ.get("LEVELDOT_EDITOR_REPO")]
    path_file = ROOT / ".source-path"
    if path_file.exists():
        candidates.append(path_file.read_text(encoding="utf-8-sig").splitlines()[0].strip().strip('"'))
    for c in candidates:
        if c and (Path(c) / ".git").exists():
            return Path(c)
    sys.exit("build: the Leveldot editor repository was not found. Pass --source, set "
             "LEVELDOT_EDITOR_REPO, or put its path on the first line of .source-path.")


def read_doc(source: Path, ref: str, path: str) -> str:
    out = subprocess.run(["git", "-C", str(source), "show", f"{ref}:{path}"],
                         capture_output=True, check=True)
    return out.stdout.decode("utf-8").replace("\r\n", "\n")


def sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Splits a document into its intro (title and text before the first ##) and its ## sections."""
    parts = re.split(r"(?m)^## ", text)
    intro, rest = parts[0], parts[1:]
    out = []
    for p in rest:
        title, _, body = p.partition("\n")
        out.append((title.strip(), "## " + p))
    return intro, out


def select(text: str, part: str) -> str:
    intro, secs = sections(text)
    intro_body = re.sub(r"(?m)^# .*\n", "", intro).strip()
    if part == "getting-started":
        gs = next(body for title, body in secs if title == "Getting started")
        return re.sub(r"(?m)^## Getting started\n", "", gs).strip()
    if part == "tools":
        return intro_body + "\n\n" + "\n".join(body for title, body in secs if title != "Getting started")
    return re.sub(r"(?m)\A# .*\n", "", text.strip()).strip()


def clean(text: str) -> str:
    # Notes for the editor's developers are not for the site.
    text = re.sub(r"Generated from the editor's action catalog .*?out of date\)\. ", "", text)
    # The in-app pointers "F1 opens this manual" stay true for the app; links between docs are rewritten.
    def link(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if re.match(r"https?://", target):
            return m.group(0)
        file, _, anchor = target.partition("#")
        page = DOC_TARGETS.get(Path(file).name)
        if page is None:
            return label  # a developer document: keep the words, drop the link
        return f"[{label}]({page}{'#' + anchor if anchor else ''})"
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def slug(value: str, separator: str = "-") -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower()).strip()
    return re.sub(r"[\s_-]+", separator, value)


def render(text: str) -> tuple[str, list[tuple[str, str]]]:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"],
                           extension_configs={"toc": {"slugify": slug, "toc_depth": "2-2"}})
    body = md.convert(text)
    toc = [(t["id"], html.unescape(t["name"])) for t in md.toc_tokens if t["level"] == 2]
    return body, toc


def doc_page(out: str, label: str, title: str, body: str, toc: list[tuple[str, str]]) -> str:
    current = ' aria-current="page"'
    side = "\n    ".join(
        f'<a href="{o}"{current if o == out else ""}>{html.escape(l)}</a>' for o, l, *_ in PAGES)
    on_page = "".join(f'<li><a href="#{i}">{html.escape(n)}</a></li>' for i, n in toc)
    filter_box = ""
    if out == "index.html":
        filter_box = (f'<p class="callout">{icon("download")}<span>Download Leveldot Editor from '
                      f'<a href="{LINKS["itch"]}" target="_blank" rel="noopener">itch.io</a>. '
                      'Then link your game: <a href="link-godot.html">Link a Godot project</a>.</span></p>')
    if out == "shortcuts.html":
        filter_box = ('<label class="filter"><span class="visually-hidden">Filter commands</span>'
                      '<input id="filter" type="search" placeholder="Filter commands or keys…" autocomplete="off"></label>'
                      '<p id="filter-empty" class="muted" hidden>No command matches.</p>')
    toc_block = f'<aside class="toc"><p class="toc-title">On this page</p><ul>{on_page}</ul></aside>' if toc else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Leveldot Docs</title>
<meta name="description" content="Leveldot Editor documentation: {html.escape(title.lower())}.">
<link rel="icon" href="../img/icon.png">
<link rel="stylesheet" href="../style.css">
</head>
<body class="docs">
{header("../", "docs")}
<div class="docs-layout">
  <nav class="sidebar" aria-label="Documentation">
    <p class="side-title">Documentation</p>
    {side}
  </nav>
  <main class="doc page-{out.removesuffix('.html')}" id="main">
    <h1>{html.escape(title)}</h1>
    {filter_box}
    {body}
  </main>
  {toc_block}
</div>
{footer("../")}
<script src="../docs.js"></script>
</body>
</html>
"""


def footer(prefix: str) -> str:
    return f"""<!-- footer (scripts/build.py writes this block) -->
<footer class="foot">
  <div class="foot-inner">
    <img src="{prefix}img/icon.png" alt="" width="24" height="24">
    <span>Leveldot Editor, a level editor for Godot 4.</span>
    <nav aria-label="Elsewhere">
      <a href="{LINKS["itch"]}" target="_blank" rel="noopener">itch.io</a>
      <a href="{LINKS["discord"]}" target="_blank" rel="noopener">Discord</a>
      <a href="{LINKS["youtube"]}" target="_blank" rel="noopener">YouTube</a>
      <a href="{prefix}docs/index.html">Docs</a>
    </nav>
  </div>
</footer>
<!-- /footer -->"""


def put_shared_blocks(page: Path, prefix: str, current: str) -> None:
    text = page.read_text(encoding="utf-8")
    for start, end, block in [("<!-- header ", "<!-- /header -->", header(prefix, current)),
                              ("<!-- footer ", "<!-- /footer -->", footer(prefix))]:
        a, b = text.index(start), text.index(end) + len(end)
        text = text[:a] + block + text[b:]
    page.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", help="the Leveldot editor repository")
    parser.add_argument("--ref", default="master", help="the editor commit to read (default: master)")
    parser.add_argument("--shared-only", action="store_true",
                        help="only rewrite the header and footer of site/index.html (no editor repository needed)")
    args = parser.parse_args()

    put_shared_blocks(SITE / "index.html", "", "home")
    if args.shared_only:
        print("BUILD: OK (shared blocks only)")
        return 0
    source = find_source(args.source)
    commit = subprocess.run(["git", "-C", str(source), "rev-parse", "--short", args.ref],
                            capture_output=True, text=True, check=True).stdout.strip()
    (SITE / "docs").mkdir(exist_ok=True)
    cache: dict[str, str] = {}
    for out, label, title, path, part in PAGES:
        text = cache.setdefault(path, read_doc(source, args.ref, path))
        body, toc = render(clean(select(text, part)))
        (SITE / "docs" / out).write_text(doc_page(out, label, title, body, toc), encoding="utf-8", newline="\n")
    print(f"BUILD: OK ({len(PAGES)} doc pages from the editor's {args.ref} at {commit})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
