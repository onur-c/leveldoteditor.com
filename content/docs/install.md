# Install

Leveldot Editor is a standalone program for Windows. You build levels in it; your game runs in Godot.
{: .lead }

## What you need

<div class="cards three">
  <div class="card"><p class="card-title">Windows 10 or 11</p><p>64-bit.</p></div>
  <div class="card"><p class="card-title">A Vulkan graphics card</p><p>Most cards from the last ten years.</p></div>
  <div class="card"><p class="card-title">Godot 4.4 or later</p><p>Only for your game. The editor does not need it.</p></div>
</div>

## Install

1. Download the ZIP from [itch.io](https://onur-c.itch.io/leveldot-editor).
2. Extract it into a folder you can write to.
3. Run `LeveldotEditor.exe`. Like Godot itself, the editor is a single file: nothing else to install.

## First launch

- An empty level opens with one cube and a **New level** card.
- Click an empty spot in the 3D view to close the card.
- Press [[Shift+B]] and drag on the grid to draw your first box.

## Projects

A project is one folder. It holds every level of your game, with its materials and models.

<div class="tree"><pre>
My Game.leveldot/
└─ project.json      <span>← open this file</span>
</pre></div>

| Do | Key |
|---|---|
| Save | [[Ctrl+S]] |
| Save to a new folder | [[Ctrl+Shift+S]] |
| Open (pick `project.json`, or drop the folder on the window) | [[Ctrl+O]] |
| New project | [[Ctrl+N]] |

## Safety nets

- **Undo and redo:** [[Ctrl+Z]] and [[Ctrl+Y]]. Every edit is one step, selection included.
- **Recovery:** unsaved work is copied every 30 seconds. After a crash the copies are offered at the next start.
- **Your settings** (theme, scale, layout, keys) belong to you, not to the project.

## Find anything

- [[F1]] opens the manual inside the app.
- [[Ctrl+K / F3]] finds any command by name and shows its key.
- **Help → Tutorial** builds a small game with you, step by step.
