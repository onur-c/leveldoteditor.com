# Basics

The screen, selecting, moving things and the camera. Ten minutes here saves hours later.
{: .lead }

## The screen

<div class="screen-map" role="img" aria-label="The editor window: menu and toolbar on top, Blockout bar below it, Tools panel on the left, 3D view in the middle, Outliner and Details on the right, status bar at the bottom">
  <div class="area a-top">Menu and toolbar</div>
  <div class="area a-bar">Blockout bar: shapes</div>
  <div class="area a-left">Tools<small>[[F6]]</small></div>
  <div class="area a-view">3D view</div>
  <div class="area a-right">Outliner and Details<small>[[F7 / Alt+O]]</small></div>
  <div class="area a-status">Status bar: hints, Entities and Props drawers</div>
</div>

- **Tools** on the left: the four selection modes and the tools for what is selected.
- **Outliner** on the right lists the objects of the level; **Details** shows the selected one.
- **Status bar** at the bottom always says what you can do now. Read it when a step does not work.

## Selection modes

<div class="keycards">
  <div class="keycard">[[1]]<span>Vertex</span></div>
  <div class="keycard">[[2]]<span>Edge</span></div>
  <div class="keycard">[[3]]<span>Face</span></div>
  <div class="keycard">[[4]]<span>Object</span></div>
</div>

The mode decides what a click selects. These four keys never change.

| Do | How |
|---|---|
| Select | Click |
| Add or remove | [[Shift+Click]] |
| Select many | Drag a rectangle |
| Connected faces, or an edge loop | Double-click |
| Everything, nothing | [[Ctrl+A]], [[Alt+A]] |

## Move, rotate, scale

<div class="keycards">
  <div class="keycard">[[W]]<span>Move</span></div>
  <div class="keycard">[[E]]<span>Rotate</span></div>
  <div class="keycard">[[R]]<span>Scale</span></div>
  <div class="keycard">[[G]]<span>Grab</span></div>
</div>

- Drag an arrow or ring of the gizmo for one axis, a square for a plane.
- **Exact values:** while dragging, type a number and press [[Enter]]. [[Esc]] cancels.
- **Grab** moves with the mouse. Press [[X]], [[Y]] or [[Z]] to lock an axis.
- Hold [[Ctrl]] while dragging to snap to a vertex.

## Camera

| Do | How |
|---|---|
| Look around | Hold [[Right mouse]] and move |
| Fly | Hold [[Right mouse]] and press [[W]] [[A]] [[S]] [[D]]; [[Q]] and [[E]] go down and up |
| Pan | Drag with [[Middle mouse]] |
| Zoom | [[Wheel]] |
| Orbit | [[Alt+Left drag]] |
| Frame the selection | [[F]] |
| Four views | [[Alt+Q / Ctrl+Alt+Q]] |

## Undo and repeat

| Do | Key |
|---|---|
| Undo | [[Ctrl+Z]] |
| Redo | [[Ctrl+Y]] |
| Repeat the last Extrude, Inset or Bevel | [[Shift+R]] |
| Duplicate | [[Ctrl+D]] |
| Delete | [[Delete]] |
