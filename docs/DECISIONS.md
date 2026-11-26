# Decisions

Only decisions someone could later ask "why?" about. Numbers are never reused; a superseded decision gets
one line "Superseded by ADR-NNN" instead of being rewritten. A side branch writes `ADR-TBD`; the session
that merges into master assigns the number.

## ADR-001 — Separate public repo, hand-written HTML, docs generated from the editor (2026-11-26)

The editor repository is private, and GitHub Pages on a private repository needs a paid plan, so the site
lives in its own public repository and is published from `site/` by a GitHub Actions workflow. The pages
are plain HTML / CSS with a few lines of JS: no framework, no build step on GitHub, no web fonts or
trackers. The documentation is not written twice: `scripts/build.py` reads the editor's own user docs
(the F1 manual, Link Godot, shortcuts, tutorial) from the editor's committed `master` and commits the
generated pages, because the workflow cannot reach the private repository. This rules out docs that
drift from the app and any build dependency on the hosting side; it means the docs are only as fresh as
the last `build.py` run.
