# Changelog

The latest version first. Download it on [itch.io](https://onur-c.itch.io/leveldot-editor); projects from earlier versions open as they are.
{: .lead }

## 0.220 · November 2026

<div class="cards three">
  <div class="card"><p class="card-title">Collections</p><p>Folders in the Outliner that nest. In Godot each one is a node with its objects under it. <a href="basics.html#outliner-and-details">How</a></p></div>
  <div class="card"><p class="card-title">Merge vertices</p><p>[[Alt+M]] in Vertex Mode: at the centre, into the first or last picked vertex, or by distance. <a href="tools.html#join-and-copy">How</a></p></div>
  <div class="card"><p class="card-title">Prop pivots</p><p>Move a prop's pivot to a corner, its centre or its bottom; every copy of the model follows. <a href="tools.html#props">How</a></p></div>
</div>

### New

- **Create** menu in the Material Browser: Blank Material, From Image Files, From Texture Sets, Blockout Set.
- **Blank Material:** a material without an image, for a tint or your own shader.
- **Draw Grid:** the wheel while dragging adds or removes cells.
- [[Ctrl]] lines up with a prop's corners, edges and surfaces.

### Better

- Text stays sharp at every UI Scale.
- **Texture Sets** take the category you type.

### Fixed

- Changing a texture and saving no longer opens Windows' "Item Not Found" window.
- A failed Save keeps the last good copy of the project.
- Undoing **Import Level from Project** brings back the original Level Exit destinations.

## 0.215 · November 2026

<div class="cards three">
  <div class="card"><p class="card-title">Proportional editing</p><p>[[O]] bends a mesh softly: nearby corners follow, the wheel sets the reach. <a href="basics.html#proportional-editing">How</a></p></div>
  <div class="card"><p class="card-title">Draw Grid</p><p>A flat plane cut into cells, ready for hills and uneven ground. <a href="tools.html#blockout">How</a></p></div>
  <div class="card"><p class="card-title">Your own shaders</p><p>A material can use a <code>.gdshader</code> from your Godot game, with a field for each setting. <a href="tools.html#your-own-shader">How</a></p></div>
</div>

### New

- **Drag number fields** in Details to change them, as in Blender. Right-click one to reset, copy or paste it.
- **Export on Save** check box at the top right: turn it off and Save only saves; [[Ctrl+E]] then updates the game.
- **Window → UI Scale** goes down to 75 %.

### Better

- **Outliner:** drag rows onto a group to put them in, [[F2]] renames.
- **Details** fits small screens.
- Saving exports to Godot in the background, and Godot shows when it has refreshed the level.
- **Open in Godot** and [[F5]] start the Godot version your game is made with.
- Holding [[Shift]] while moving takes fine 1 cm steps.

### Fixed

- Projects saved by the first public version open again.
- Saving with a level open in Godot no longer crashes Godot.
- Export never overwrites or deletes a file of yours.
- Moving platforms carry their trigger and solid areas with them in the game.
- Level changes in the game never stay on a black screen.

## 0.195 · November 2026

The first public alpha.
