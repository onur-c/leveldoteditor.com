# What's new

The latest version first. Download it on [itch.io](https://onur-c.itch.io/leveldot-editor); projects from earlier versions open as they are.
{: .lead }

## 0.215 · November 2026

<div class="cards three">
  <div class="card"><p class="card-title">Proportional editing</p><p>[[O]] bends a mesh softly: nearby corners follow, the wheel sets the reach. <a href="basics.html#proportional-editing">How</a></p></div>
  <div class="card"><p class="card-title">Draw Grid</p><p>A flat plane cut into cells, ready for hills and uneven ground. <a href="tools.html#blockout">How</a></p></div>
  <div class="card"><p class="card-title">Your own shaders</p><p>A material can use a <code>.gdshader</code> from your Godot game, with a field for each setting. <a href="tools.html#your-own-shader">How</a></p></div>
</div>

### New

- **Drag number fields** in Details to change them, as in Blender: the level follows live, [[Shift]] drags finer, [[Ctrl]] snaps, [[Esc]] puts it back. Right-click a field to reset, copy or paste it.
- **Export on Save** check box at the top right: turn it off and Save only saves; [[Ctrl+E]] then updates the game.
- **Window → UI Scale** goes down to 75 %.
- The Blockout bar folds to a thin strip: click its name.

### Better

- **Outliner:** the row icon shows the type, a selection in the 3D view scrolls to its row, drag rows onto a group to put them in, [[F2]] renames.
- **Details:** the object's own settings first, the group after; it fits small screens and remembers how much room you give it.
- **Entity Details:** values change in place, [[Enter]] moves to the next one.
- A copied group keeps its name with a number (Group 1_001).
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
