# Basics

The screen, selecting, moving things and the camera.
{: .lead }

## The screen

<figure class="annotated"><div class="annotated-img"><img src="../img/ui-window.jpg" alt="The Leveldot Editor window with its areas numbered" width="1920" height="1030" loading="lazy"><span class="pin" style="left:56%;top:4.9%">1</span><span class="pin" style="left:49.5%;top:9.7%">2</span><span class="pin" style="left:6.5%;top:73%">3</span><span class="pin" style="left:62.5%;top:68%">4</span><span class="pin" style="left:90.4%;top:40.8%">5</span><span class="pin" style="left:95.5%;top:55.7%">6</span><span class="pin" style="left:67.7%;top:98.4%">7</span></div></figure>

<ol class="legend">
<li><strong>Menu and toolbar:</strong> modes, Move / Rotate / Scale, Play, Export.</li>
<li><strong>Blockout bar:</strong> the shapes you draw.</li>
<li><strong>Tools</strong> [[F6]]: selection modes and the tools for what is selected.</li>
<li><strong>3D view:</strong> where you build.</li>
<li><strong>Outliner:</strong> every object of the level.</li>
<li><strong>Details:</strong> the selected object's settings.</li>
<li><strong>Status bar:</strong> what you can do now. Read it when a step does not work.</li>
</ol>

Hide or show the side panels: Tools [[F6]], Outliner and Details [[F7 / Alt+O]]. Too small or too large: **Window → UI Scale** (75 % to 150 %).

### Outliner and Details

- **Outliner:** drag rows onto a group to put them in, or onto a loose row to take them out. [[F2]] renames.
- **Details:** drag a number sideways to change it. [[Shift]] drags finer, [[Ctrl]] snaps, [[Esc]] puts it back.
- Right-click a number: **Reset**, **Copy**, **Paste**.

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

## Selection modes

<figure class="ui-strip"><img src="../img/ui-modes.jpg" alt="The four selection mode buttons, 1 to 4, at the top of the Tools panel" width="227" height="49" loading="lazy"><figcaption>Top of the Tools panel</figcaption></figure>

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

<figure class="ui-strip"><img src="../img/ui-transform.jpg" alt="The Move, Rotate and Scale buttons W, E, R on the toolbar" width="156" height="42" loading="lazy"><figcaption>On the toolbar</figcaption></figure>

<div class="keycards">
  <div class="keycard">[[W]]<span>Move</span></div>
  <div class="keycard">[[E]]<span>Rotate</span></div>
  <div class="keycard">[[R]]<span>Scale</span></div>
  <div class="keycard">[[G]]<span>Grab</span></div>
</div>

- Drag an arrow or ring of the gizmo for one axis, a square for a plane.
- **Exact values:** while dragging, type a number and press [[Enter]]. [[Esc]] cancels.
- **Fine steps:** hold [[Shift]] while you drag the Move gizmo: 1 cm at a time.
- **Grab** moves with the mouse. Press [[X]], [[Y]] or [[Z]] to lock an axis.

### Snap to corners, edges and faces

Hold [[Caps Lock]] while you drag a gizmo or Grab, and point the mouse at something in the level. The selection lines up with it.

<div class="flow">
  <div class="node"><p class="node-kicker">1 · Drag</p><p class="node-title">Move a selection</p><p class="node-text">With the gizmo, or [[G]].</p></div>
  <div class="edge"><span>hold [[Caps Lock]]</span></div>
  <div class="node"><p class="node-kicker">2 · Point</p><p class="node-title">At a corner, edge or face</p><p class="node-text">A yellow dot marks the spot.</p></div>
  <div class="edge"><span>release the mouse</span></div>
  <div class="node accent"><p class="node-kicker">3 · Done</p><p class="node-title">Lined up exactly</p></div>
</div>

- It catches corners, edge middles, face centres, and any point on an edge or a face.
- [[Ctrl]] does the same while held.

### Proportional editing

Press [[O]] (or the **Proportional** button beside World) to bend a mesh softly instead of moving single corners.

<div class="flow">
  <div class="node"><p class="node-kicker">1 · Select</p><p class="node-title">A few corners, edges or faces</p></div>
  <div class="edge"><span>[[O]] on, then [[G]] / [[W]] / [[E]] / [[R]]</span></div>
  <div class="node"><p class="node-kicker">2 · Drag</p><p class="node-title">Nearby corners follow</p><p class="node-text">Less the farther they are.</p></div>
  <div class="edge"><span>[[Wheel]] while dragging</span></div>
  <div class="node accent"><p class="node-kicker">3 · Reach</p><p class="node-title">The circle grows or shrinks</p></div>
</div>

- Works in Vertex, Edge and Face Mode, on the same mesh.
- Good with **Draw Grid** on the [Tools](tools.html#blockout) page: hills, dents, uneven ground.

## Undo and repeat

| Do | Key |
|---|---|
| Undo | [[Ctrl+Z]] |
| Redo | [[Ctrl+Y]] |
| Repeat the last Extrude, Inset or Bevel | [[Shift+R]] |
| Duplicate | [[Ctrl+D]] |
| Delete | [[Delete]] |
