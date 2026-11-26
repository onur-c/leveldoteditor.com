# Tools

A short tour, grouped by job. Every command and its key is on the [Shortcuts](shortcuts.html) page; in the app [[Ctrl+K / F3]] finds any of them.
{: .lead }

## Blockout

Pick a shape on the Blockout bar, drag on the grid or on any surface, then pull up the height. [[Enter]] confirms, [[Esc]] cancels.

<figure class="ui-strip"><img src="../img/ui-blockout.jpg" alt="The Blockout bar: Box, Plane, Polygon, Height, Spline, Cylinder, Cone, Sphere, Ramp, Stairs, Arch, Decal" width="750" height="55" loading="lazy"><figcaption>The Blockout bar</figcaption></figure>

Quick keys: Box [[Shift+B]], Plane [[Shift+P]]. **Height** sets where a shape starts above the grid.

**Draw on** chooses where a shape starts: the surface under the mouse, or the grid.

## Modeling

Select something first, then use a tool. Its settings show at the bottom left of the 3D view.

| Tool | Key | What it does |
|---|---|---|
| Extrude | [[Shift+E]] | Grows faces out, or walls from open edges |
| Inset | [[I]] | Shrinks faces and adds a frame around them |
| Bevel | [[B]] | Rounds or chamfers edges and corners |
| Loop Cut | [[Ctrl+R]] | Adds a ring of edges around the mesh |
| Knife | [[Shift+K]] | Cuts new edges point by point |
| Opening | [[Ctrl+Shift+O]] | Cuts a door or window through a wall |
| Hollow | [[Ctrl+Shift+W]] | Turns a solid block into a room |
| Bridge | [[Shift+C]] | Joins two rows of edges with faces |
| Fill Hole | [[Ctrl+F]] | Closes an opening |
| Boolean difference | [[Ctrl+Minus / Ctrl+Shift+Numpad Subtract]] | Cuts one object out of another |
| Merge Objects | [[M]] | Joins objects into one |
| Jumble | [[J]] | Moves vertices by a pattern: hills, ridges, cells |

## Texture and UV

| Do | How |
|---|---|
| Open the Material Browser | [[Ctrl+M]] |
| Apply the active material | [[Shift+T]] |
| Make a material from an image | [[Ctrl+Shift+I]], or drop the image on the window |
| Pick a face's material | [[Shift+Right-click]] |
| Continue a texture across an edge | [[Alt+Right-click]] |
| Fit the texture to a face | [[Ctrl+Alt+Numpad 5]] |
| Show a UV checker | [[Alt+Shift+U]] |

Hotspot atlases, a UV editor, decals and vertex colours are in the **Texture** menu.

## Props

- **File → Import Models…** brings in GLB, glTF or FBX files (with Blender installed, `.blend` and `.obj` too). Dropping files on the window does the same.
- Each model becomes a tile in the **Props** drawer [[Shift+M]]. Drag a tile into the level; the wheel turns it before you drop it.

## Entities

Entities are objects that do something in the game: lights, doors, coins, triggers, effects.

<div class="flow">
  <div class="node"><p class="node-kicker">In Godot</p><p class="node-title">A script that extends <code>LeveldotEntity</code></p></div>
  <div class="edge"><span>Leveldot reads it</span></div>
  <div class="node"><p class="node-kicker">In Leveldot</p><p class="node-title">A tile in the Entities drawer</p></div>
  <div class="edge"><span>drag</span></div>
  <div class="node accent"><p class="node-kicker">In the level</p><p class="node-title">An entity with its settings</p></div>
</div>

- Open the **Entities** drawer with [[Shift+A]]. It also holds the built-in set: lights, effects (smoke, fire, rain…), doors and lifts, Player Start, Level Exit.
- [[Alt+Enter]] shows the selected entity's settings and events.

## Logic

One building block: **when this happens, do this.**

<div class="flow">
  <div class="node"><p class="node-kicker">When</p><p class="node-title">Coin 1 is collected</p></div>
  <div class="edge"><span>then</span></div>
  <div class="node accent"><p class="node-kicker">Do</p><p class="node-title">Door 1 opens</p></div>
</div>

| Do | Key |
|---|---|
| Connect the selected entity to another | [[K]] |
| See the connections in the level | [[F4]] |
| The level's own logic: start, timers, signals | [[Ctrl+L]] |
| A list of all connections in the level | [[Ctrl+Shift+L]] |
| The connections as a graph | [[Alt+G]] |

## Levels

<div class="flow">
  <div class="node"><p class="node-kicker">Level</p><p class="node-title">Hall</p><p class="node-text">Player Start · Level Exit</p></div>
  <div class="edge"><span>the player walks into the exit</span></div>
  <div class="node accent"><p class="node-kicker">Level</p><p class="node-title">Cellar</p><p class="node-text">Player Start</p></div>
</div>

- A project holds many levels. Switch with the level picker on top of the Outliner, or [[Ctrl+PageUp]] and [[Ctrl+PageDown]].
- A **Player Start** says where the player appears; a **Level Exit** sends them to another level.

## Check your level

| Do | Key |
|---|---|
| List problems: missing destinations, broken links | [[F8]] |
| Show what the player collides with | [[Alt+Shift+K]] |

If something looks wrong, the status bar says so in yellow; [[Ctrl+Z]] undoes it.
