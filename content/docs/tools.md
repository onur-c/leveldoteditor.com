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

### Shape

| Tool | Key | What it does |
|---|---|---|
| Extrude | [[Shift+E]] | Grows faces out, or walls from open edges |
| Inset | [[I]] | Shrinks faces and adds a frame around them |
| Bevel | [[B]] | Rounds or chamfers edges and corners |
| Push Through | | Pushes faces into a wall until it is pierced |
| Opening | [[Ctrl+Shift+O]] | Cuts a door or window through a wall |
| Solidify | | Gives faces a thickness |
| Hollow | [[Ctrl+Shift+W]] | Turns a solid block into a room |
| Jumble | [[J]] | Moves vertices by a pattern: hills, ridges, cells |

### Cut and split

| Tool | Key | What it does |
|---|---|---|
| Loop Cut | [[Ctrl+R]] | Adds a ring of edges around the mesh |
| Cut | [[C]] | Drag a line across faces to cut them |
| Knife | [[Shift+K]] | Cuts new edges point by point |
| Subdivide | [[Alt+V]] | Splits faces into a grid |
| Slice | [[Shift+X]] | Splits whole objects along a line |
| Detach Faces | [[N]] | Moves faces into a new object |

### Join and copy

| Tool | Key | What it does |
|---|---|---|
| Bridge | [[Shift+C]] | Joins two rows of edges with faces |
| Fill Hole | [[Ctrl+F]] | Closes an opening |
| Merge Objects | [[M]] | Joins objects into one |
| Boolean difference | [[Ctrl+Minus / Ctrl+Shift+Numpad Subtract]] | Cuts one object out of another |
| Mirror | [[Shift+Z]] | Mirrors objects (X; Y and Z in the menu) |
| Array | | Copies in a line or around a circle |
| Group | [[Ctrl+G]] | Parts that select and move together |

## Texture and UV

| Do | How |
|---|---|
| Open the Material Browser | [[Ctrl+M]] |
| Apply the active material | [[Shift+T]] |
| Make a material from an image | [[Ctrl+Shift+I]], or drop the image on the window |
| Pick a face's material | [[Shift+Right-click]] |
| Continue a texture across an edge | [[Alt+Right-click]] |
| Carry a texture along a strip (an arch, a pipe) | [[Ctrl+Alt+Right-click]] the next face; keep the button down to go on |
| Fit the texture to a face | [[Ctrl+Alt+Numpad 5]] |
| Fit a rectangle of an atlas to each face | [[Shift+H]] |
| Copy and paste a face's UV | [[Ctrl+Alt+C]], [[Ctrl+Alt+V]] |
| Show a UV checker | [[Alt+Shift+U]] |

A UV editor, decals and vertex colours are in the **Texture** menu.

## Props

- **File → Import Models…** brings in GLB, glTF or FBX files (with Blender installed, `.blend` and `.obj` too). Dropping files on the window does the same.
- Each model becomes a tile in the **Props** drawer [[Shift+M]]. Drag a tile into the level; the wheel turns it before you drop it.
- **Mark as Prop** turns your own geometry into a reusable model. Edit it once, every copy follows.

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
- Make your own entity types and connect entities: [Entities and logic](logic.html) <span class="tag-exp">Experimental</span>.
- **Movers** make a group move on its own, without code: a door, a lift, a platform, a spinner (**Add Mover to Group**).
- A **Physics Body** falls and can be pushed in the game; **Settle** drops it where it comes to rest.

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
