"""Builds the documentation pages of the Leveldot site and the shared header / footer.

- content/docs/*.md (written for the site, short) become site/docs/*.html. Keys are written
  [[Ctrl+S]] (alternatives with " / ") and become key caps; a key the editor does not have stops
  the build, so the pages cannot drift from the app.
- The Shortcuts page is generated whole from docs/SHORTCUTS.md of the Leveldot editor repository,
  read from its committed `master` (never its working copy).
- The header and footer are written into every page, site/index.html included.

    python scripts/build.py [--source <editor repo>] [--ref master] [--shared-only]

The editor repository is found by --source, else $LEVELDOT_EDITOR_REPO, else the first line
of `.source-path` in this repository (git-ignored, one per machine).
"""
from __future__ import annotations

import argparse
import hashlib
import html
import os
import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CONTENT = ROOT / "content" / "docs"

LINKS = {
    "itch": "https://onur-c.itch.io/leveldot-editor",
    "discord": "https://discord.gg/e3CdgVQxp",
    "youtube": "https://www.youtube.com/@LeveldotEditor",
}

# (output file, nav label, source: a file in content/docs or "shortcuts")
PAGES = [
    ("index.html", "Install", "install.md"),
    ("link-godot.html", "Link Godot", "link-godot.md"),
    ("basics.html", "Basics", "basics.md"),
    ("tools.html", "Tools", "tools.md"),
    ("shortcuts.html", "Shortcuts", "shortcuts"),
    ("whats-new.html", "What's new", "whats-new.md"),
    ("logic.html", "Entities and logic", "logic.md"),
]

# Pages about a part of the app that is still changing: tagged in the sidebar and the title.
EXPERIMENTAL = {"logic.html"}
EXP_TAG = ' <span class="tag-exp">Experimental</span>'

# Keys the pages may name that are not commands of SHORTCUTS.md: mouse gestures and the keys
# that work inside a tool (manual: Transform, Camera and mouse, Modeling tools).
EXTRA_KEYS = {
    "Enter", "Esc", "Ctrl", "Shift", "X", "Y", "Z", "A", "S", "D", "Q",
    "Right mouse", "Middle mouse", "Wheel", "Alt+Left drag", "Shift+Click",
    "Shift+Right-click", "Alt+Right-click", "Ctrl+Alt+Right-click", "Caps Lock",
}

KEY_NAMES = {
    "Comma": ",", "Period": ".", "Minus": "−", "Equal": "=", "Slash": "/", "BracketLeft": "[",
    "BracketRight": "]", "Delete": "Del", "PageUp": "PgUp", "PageDown": "PgDn",
    "Up": "↑", "Down": "↓", "Left": "←", "Right": "→", "Space": "Space", "Escape": "Esc",
}

ICONS = {
    "download": '<path d="M12 3v12m0 0-5-5m5 5 5-5M4 19h16"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5Z"/><path d="M4 21a2 2 0 0 1 2-2h13"/>',
    "discord": '<path d="M5 6.5C7 5.2 9 4.6 12 4.6s5 .6 7 1.9c1.4 2.6 2 5.4 1.8 8.6-1.6 1.5-3.4 2.5-5.3 3l-1.1-1.9M5 6.5C3.6 9.1 3 11.9 3.2 15.1c1.6 1.5 3.4 2.5 5.3 3l1.1-1.9M7.5 16c2.9 1.3 6.1 1.3 9 0"/><circle cx="9.2" cy="12" r="1.1"/><circle cx="14.8" cy="12" r="1.1"/>',
    "youtube": '<rect x="2.5" y="5.5" width="19" height="13" rx="3.5"/><path d="m10.2 9.3 4.6 2.7-4.6 2.7V9.3Z"/>',
    "itch": '<path d="M3 9.5 5 4h14l2 5.5M3 9.5c0 1.4 1 2.5 2.25 2.5S7.5 10.9 7.5 9.5c0 1.4 1 2.5 2.25 2.5S12 10.9 12 9.5c0 1.4 1 2.5 2.25 2.5s2.25-1.1 2.25-2.5c0 1.4 1 2.5 2.25 2.5S21 10.9 21 9.5M5 12v8h14v-8M10 20v-4h4v4"/>',
    "arrow-left": '<path d="M19 12H5m0 0 6-6m-6 6 6 6"/>',
    "arrow-right": '<path d="M5 12h14m0 0-6-6m6 6-6 6"/>',
}


def asset_url(prefix: str, name: str) -> str:
    """A site asset with its content hash, so a browser never keeps an old copy after a change
    (GitHub Pages lets browsers cache for 10 minutes)."""
    # line endings left out: a Windows checkout (CRLF) and GitHub (LF) must agree
    digest = hashlib.sha1((SITE / name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:10]
    return f"{prefix}{name}?v={digest}"


def icon(name: str) -> str:
    return ('<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


# ---- shared blocks

def header(prefix: str, current: str) -> str:
    """The bar on top of every page; `prefix` leads from the page to the site root."""
    def nav(href: str, label: str, key: str, name: str, external: bool = False) -> str:
        attrs = ' target="_blank" rel="noopener"' if external else ""
        here = ' aria-current="page"' if key == current else ""
        return f'<a class="nav-link" href="{href}"{attrs}{here}>{icon(name)}<span>{label}</span></a>'
    return f"""<header class="top">
  <div class="top-inner">
    <a class="brand" href="{prefix}index.html" aria-label="Leveldot home, alpha">
      <picture>
        <source srcset="{prefix}img/logo-light.png" media="(prefers-color-scheme: light)">
        <img src="{prefix}img/logo-dark.png" alt="Leveldot" width="144" height="31">
      </picture>
      <span class="pill" aria-hidden="true">Alpha</span>
    </a>
    <nav class="top-nav" aria-label="Site">
      {nav(prefix + "docs/index.html", "Docs", "docs", "book")}
      {nav(LINKS["discord"], "Discord", "", "discord", True)}
      {nav(LINKS["youtube"], "YouTube", "", "youtube", True)}
      <a class="button primary small" href="{LINKS["itch"]}" target="_blank" rel="noopener">{icon("download")}<span>Download</span></a>
    </nav>
  </div>
</header>"""


def footer(prefix: str) -> str:
    return f"""<footer class="foot">
  <div class="foot-inner">
    <img src="{prefix}img/icon.png" alt="" width="24" height="24">
    <span>Leveldot Editor, a level editor for Godot 4. Alpha: things still change.</span>
    <nav aria-label="Elsewhere">
      <a href="{LINKS["itch"]}" target="_blank" rel="noopener">itch.io</a>
      <a href="{LINKS["discord"]}" target="_blank" rel="noopener">Discord</a>
      <a href="{LINKS["youtube"]}" target="_blank" rel="noopener">YouTube</a>
      <a href="{prefix}docs/index.html">Docs</a>
    </nav>
  </div>
</footer>"""


def write_home() -> None:
    """content/index.html (hand-written) -> site/index.html: the shared header and footer go in
    at the <!-- header --> / <!-- footer --> marks, assets get their versions, comments stay out."""
    text = (ROOT / "content" / "index.html").read_text(encoding="utf-8")
    text = text.replace("<!-- header -->", header("", "home")).replace("<!-- footer -->", footer(""))
    text = re.sub(r"<!--.*?-->\n?", "", text, flags=re.S)
    text = re.sub(r'href="style\.css(\?v=\w+)?"', 'href="' + asset_url("", "style.css") + '"', text)
    text = re.sub(r'src="home\.js(\?v=\w+)?"', 'src="' + asset_url("", "home.js") + '"', text)
    (SITE / "index.html").write_text(text, encoding="utf-8", newline="\n")


# ---- keys

def key_cap(part: str) -> str:
    name = part
    if part.startswith("Numpad "):
        rest = part[len("Numpad "):]
        rest = {"Add": "+", "Subtract": "−", "Multiply": "*", "Divide": "/", "Period": "."}.get(rest, rest)
        name = "Num " + rest
    else:
        name = KEY_NAMES.get(part, part)
    return f"<kbd>{html.escape(name)}</kbd>"


def keys_html(combo_text: str) -> str:
    """'Ctrl+Shift+E / Alt+E' -> key caps; alternatives joined by 'or'."""
    alts = []
    for combo in combo_text.split(" / "):
        parts = [p for p in combo.strip().split("+") if p]
        alts.append('<span class="combo">' + '<span class="plus">+</span>'.join(key_cap(p) for p in parts) + "</span>")
    return '<span class="keys">' + '<span class="or">or</span>'.join(alts) + "</span>"


# ---- editor shortcuts

def read_shortcuts(text: str) -> list[tuple[str, list[dict]]]:
    """SHORTCUTS.md -> [(category, [{keys, command, mode, where, what}])]."""
    out: list[tuple[str, list[dict]]] = []
    for block in re.split(r"(?m)^## ", text)[1:]:
        title, _, body = block.partition("\n")
        rows = []
        for line in body.splitlines():
            if not line.startswith("| ") or line.startswith("| Keys") or line.startswith("|---"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            rows.append({"keys": "" if cells[0] == "—" else cells[0], "command": cells[1],
                         "mode": cells[2], "where": cells[3], "what": cells[4]})
        out.append((title.strip(), rows))
    return out


# The Shortcuts page puts what people press most first; a group not listed goes last.
CARD_ORDER = ["Modes and Transform", "Create", "Mesh", "Select", "Edit", "3D View", "Texture and UV", "File",
              "Overlays", "Material Browser", "Window and Help", "Logic and Entities", "Logic Graph Window"]


# Within a group these single keys lead, in this order (modes, then Move / Rotate / Scale / Grab).
FIRST_KEYS = {k: i for i, k in enumerate(["1", "2", "3", "4", "W", "E", "R", "G"])}


def by_priority(shortcuts):
    rank = {t: i for i, t in enumerate(CARD_ORDER)}
    return sorted(shortcuts, key=lambda group: rank.get(group[0], len(CARD_ORDER)))


def known_keys(shortcuts) -> set[str]:
    known = set(EXTRA_KEYS)
    for _, rows in shortcuts:
        for r in rows:
            if r["keys"]:
                known.add(r["keys"])
                known.update(k.strip() for k in r["keys"].split(" / "))
    return known


def shortcuts_body(shortcuts) -> str:
    cards = []
    for title, rows in shortcuts:
        items = []
        # single keys first (1-4, W/E/R...), then combos by how many modifiers they need, keyless last
        for r in sorted(rows, key=lambda r: (r["keys"] == "", r["keys"].split(" / ")[0].count("+"),
                                         FIRST_KEYS.get(r["keys"], len(FIRST_KEYS)), r["keys"], r["command"].lower())):
            mode = "" if r["mode"] == "Any" else f'<span class="mode">{html.escape(r["mode"])}</span>'
            keys = keys_html(r["keys"]) if r["keys"] else '<span class="nokey">no key</span>'
            what = re.sub(r"[*`]", "", r["what"])
            items.append(
                f'<li class="sc{"" if r["keys"] else " unbound"}" title="{html.escape(what)}">'
                f'<span class="sc-name">{html.escape(r["command"])}{mode}</span>{keys}</li>')
        tag = ' <span class="tag-exp">Experimental</span>' if 'Logic' in title else ''
        cards.append(f'<section class="sc-card"><h2 id="{slug(title)}">{html.escape(title)}{tag}</h2>'
                     f'<ul class="sc-list">{"".join(items)}</ul></section>')
    return (
        '<p class="lead">The default keys. Change them in the app: <strong>Help → Keyboard Shortcuts…</strong> '
        f'(the selection modes {keys_html("1")} to {keys_html("4")} are fixed). Hover a command to see what it does.</p>'
        '<div class="sc-tools">'
        '<label class="filter"><span class="visually-hidden">Filter commands</span>'
        '<input id="filter" type="search" placeholder="Filter: extrude, ctrl+s…" autocomplete="off"></label>'
        '<label class="toggle"><input id="show-unbound" type="checkbox"> Show commands without a key</label>'
        '</div>'
        '<p id="filter-empty" class="muted" hidden>No command matches.</p>'
        f'<div class="sc-grid">{"".join(cards)}</div>')


# ---- pages

def slug(value: str, separator: str = "-") -> str:
    value = re.sub(r"[^\w\s-]", "", value.lower()).strip()
    return re.sub(r"[\s_-]+", separator, value)


def render_content(text: str, known: set[str] | None, name: str) -> tuple[str, str, list[tuple[str, str]]]:
    title_match = re.match(r"# (.+)\n", text)
    if not title_match:
        sys.exit(f"build: {name} must start with '# Title'")
    title = title_match.group(1).strip()
    text = text[title_match.end():]
    unknown = []

    def key(m: re.Match) -> str:
        combo = m.group(1).strip()
        if known is not None:
            for alt in combo.split(" / "):
                if alt.strip() not in known and combo not in known:
                    unknown.append(alt.strip())
        return keys_html(combo)
    text = re.sub(r"\[\[([^\]]+)\]\]", key, text)
    if unknown:
        sys.exit(f"build: {name} names keys the editor does not have: {', '.join(sorted(set(unknown)))} "
                 "(check SHORTCUTS.md, or add a gesture to EXTRA_KEYS)")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc", "attr_list"],
                           extension_configs={"toc": {"slugify": slug, "toc_depth": "2-2"}})
    body = md.convert(text)
    toc = [(t["id"], re.sub(r"\s*Experimental$", "", re.sub(r"<[^>]+>", "", html.unescape(t["name"]))).strip())
           for t in md.toc_tokens if t["level"] == 2]
    return title, body, toc


def doc_page(index: int, title: str, body: str, toc: list[tuple[str, str]]) -> str:
    out = PAGES[index][0]
    current = ' aria-current="page"'
    side = "\n    ".join(f'<a href="{o}"{current if o == out else ""}>{html.escape(l)}{EXP_TAG if o in EXPERIMENTAL else ""}</a>'
                           for o, l, _ in PAGES)
    on_page = "".join(f'<li><a href="#{i}">{html.escape(n)}</a></li>' for i, n in toc)
    toc_block = (f'<aside class="toc"><p class="toc-title">On this page</p><ul>{on_page}</ul></aside>'
                 if toc and out != "shortcuts.html" else "")
    pager = []
    if index > 0:
        o, l, _ = PAGES[index - 1]
        pager.append(f'<a class="pager-prev" href="{o}">{icon("arrow-left")}<span><small>Previous</small>{html.escape(l)}</span></a>')
    if index + 1 < len(PAGES):
        o, l, _ = PAGES[index + 1]
        pager.append(f'<a class="pager-next" href="{o}"><span><small>Next</small>{html.escape(l)}</span>{icon("arrow-right")}</a>')
    wide = " wide" if out == "shortcuts.html" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Leveldot Docs</title>
<meta name="description" content="Leveldot Editor documentation: {html.escape(title.lower())}.">
<link rel="icon" href="../img/icon.png">
<link rel="stylesheet" href="{asset_url("../", "style.css")}">
</head>
<body class="docs">
{header("../", "docs")}
<div class="docs-layout{wide}">
  <nav class="sidebar" aria-label="Documentation">
    <p class="side-title">Documentation</p>
    {side}
  </nav>
  <main class="doc page-{out.removesuffix('.html')}" id="main">
    <h1>{html.escape(title)}{EXP_TAG if out in EXPERIMENTAL else ""}</h1>
    {body}
    <nav class="pager" aria-label="Pages">{"".join(pager)}</nav>
  </main>
  {toc_block}
</div>
{footer("../")}
<script src="{asset_url("../", "docs.js")}"></script>
</body>
</html>
"""


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


def read_editor_doc(source: Path, ref: str, path: str) -> str:
    out = subprocess.run(["git", "-C", str(source), "show", f"{ref}:{path}"], capture_output=True, check=True)
    return out.stdout.decode("utf-8").replace("\r\n", "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", help="the Leveldot editor repository")
    parser.add_argument("--ref", default="master", help="the editor commit to read (default: master)")
    parser.add_argument("--shared-only", action="store_true",
                        help="only write site/index.html from content/index.html (no editor repository needed)")
    args = parser.parse_args()

    write_home()
    if args.shared_only:
        print("BUILD: OK (shared blocks only)")
        return 0
    source = find_source(args.source)
    commit = subprocess.run(["git", "-C", str(source), "rev-parse", "--short", args.ref],
                            capture_output=True, text=True, check=True).stdout.strip()
    shortcuts = by_priority(read_shortcuts(read_editor_doc(source, args.ref, "docs/SHORTCUTS.md")))
    known = known_keys(shortcuts)
    docs = SITE / "docs"
    docs.mkdir(exist_ok=True)
    written = set()
    for i, (out, label, src) in enumerate(PAGES):
        if src == "shortcuts":
            title, body, toc = "Keyboard shortcuts", shortcuts_body(shortcuts), []
        else:
            title, body, toc = render_content((CONTENT / src).read_text(encoding="utf-8"), known, src)
        (docs / out).write_text(doc_page(i, title, body, toc), encoding="utf-8", newline="\n")
        written.add(out)
    for stale in docs.glob("*.html"):
        if stale.name not in written:
            stale.unlink()
    print(f"BUILD: OK ({len(PAGES)} doc pages; shortcuts from the editor's {args.ref} at {commit})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
