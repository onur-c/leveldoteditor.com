# Handoff

> Updated: 2026-11-26 · Verified against: `ba4473b` + docs-v2 · Status: idle

Current state only; replace, never append. History is `git log`, reasons are in DECISIONS.md.

## Where it stands

- Docs rewritten short and hand-written (ADR-002): Install, Link Godot (flow diagram, file tree, problem
  accordions), Basics (window map, key cards, camera table), Tools (chips, tables, entity / logic / level
  diagrams), Shortcuts (cheat sheet from the editor's SHORTCUTS.md at `034c99cc`: key caps, filter, keyless
  commands hidden by default). Tutorial page removed. Alpha pill on the logo.
- Repo renamed to `onur-c/leveldoteditor.com`; live at `https://onur-c.github.io/leveldoteditor.com/`.

## Not verified

- Rendering checked with headless Edge (1440 px dark and light, 390 px in iframes). Not seen on a real
  phone, Safari or Firefox.

## Open requests

- Custom domain `leveldoteditor.com`: not registered (no DNS on 2026-11-26). Once the user owns it and
  its DNS points at GitHub Pages (A 185.199.108.153 / .109.153 / .110.153 / .111.153, `www` CNAME
  `onur-c.github.io`), set it: `gh api -X PUT repos/onur-c/leveldoteditor.com/pages -f cname=leveldoteditor.com`,
  then `https_enforced=true` once the certificate is issued.

## Uncommitted work

- none
