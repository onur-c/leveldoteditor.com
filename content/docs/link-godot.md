# Link a Godot project

Link connects your Leveldot project to your Godot game. After that, every save puts your levels into the game.
{: .lead }

## How it fits together

<div class="flow">
  <div class="node"><p class="node-kicker">Leveldot Editor</p><p class="node-title">You build the level</p><p class="node-text">Rooms, textures, entities, logic.</p></div>
  <div class="edge"><span>Save [[Ctrl+S]]</span></div>
  <div class="node"><p class="node-kicker">Your Godot game</p><p class="node-title">The level arrives</p><p class="node-text">Godot refreshes it by itself.</p></div>
  <div class="edge"><span>Play [[F5]]</span></div>
  <div class="node accent"><p class="node-kicker">Your game scene</p><p class="node-title">You walk through it</p><p class="node-text">With your player and scripts.</p></div>
</div>

You need a Godot game on **Godot 4.4 or later** and a saved Leveldot project.

## First time

1. **Save** the project with [[Ctrl+S]]. Link needs a saved project.
2. **Link:** choose **File → Link Godot Project…** and pick the folder that holds `project.godot`.
3. **Open the game in Godot:** **File → Open in Godot**. If it was already open, choose **Project → Reload Current Project** once.
4. **Make a game scene:** in Godot open the **Leveldot** screen → **Levels**, select your level, press **Create Game Scene…**.
5. **Add your game:** put your player, enemies and scripts into that scene, never into the generated level.

<div class="note"><p><strong>What Link changes in your game:</strong> it adds the Leveldot Bridge addon and switches it on, then exports once. Your own scenes and scripts are never changed.</p></div>

## Every day

| Key | What happens |
|---|---|
| [[Ctrl+S]] | Saves and exports every level. Godot refreshes them, even in the background. |
| [[Ctrl+E]] | Exports again, without an edit. |
| [[F5]] | Saves, exports and starts the game at the level you are editing. |

Both programs tell you when the level has arrived: a status button on Godot's top toolbar, and the status bar in Leveldot.

## Where files go

<div class="tree"><pre>
res://
├─ addons/leveldot_bridge/      <span>the addon (Leveldot keeps it up to date)</span>
└─ leveldot/
   ├─ generated/                <span>written by Leveldot, never edit</span>
   │  └─ levels/&lt;level&gt;/        <span>world.glb, generated_world.tscn</span>
   ├─ entities/                 <span>your entity types</span>
   └─ levels/                   <span>your game scenes</span>
</pre></div>

Keep your own scenes and scripts outside `generated/`.

## Common problems

<details><summary>“Save the project first”</summary><p>Press [[Ctrl+S]], then link again.</p></details>
<details><summary>Godot does not react to an export</summary><p>The game must be open in Godot with <strong>Leveldot Bridge</strong> switched on (<strong>Project → Project Settings → Plugins</strong>). Reload the project once after linking, or press <strong>Refresh</strong> on the Leveldot screen.</p></details>
<details><summary>The level is not in the game</summary><p>Only a scene that contains the level shows it. Make one with <strong>Create Game Scene…</strong> (step 4).</p></details>
<details><summary>My Godot is older than 4.4</summary><p>The addon needs Godot 4.4 or later. Open the game in a newer Godot.</p></details>
<details><summary>An error code (A201, X40x, E30x)</summary>
<table>
<thead><tr><th>Code</th><th>Meaning</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>A201</td><td>A file the export needs is missing or not imported yet.</td><td>Let Godot finish importing, then export again.</td></tr>
<tr><td>X401</td><td>A refresh stopped with an error.</td><td>Read Godot's Output panel, export again.</td></tr>
<tr><td>X402</td><td>The export and the addon do not match.</td><td>Export again from Leveldot; it updates the addon.</td></tr>
<tr><td>X403</td><td>A <code>generated_world.tscn</code> Leveldot did not write is in the way.</td><td>Move or rename it.</td></tr>
<tr><td>E301</td><td>An entity type's scene is missing in the game.</td><td>Leveldot screen → Levels → <strong>Create …</strong> next to it.</td></tr>
<tr><td>E302</td><td>A reaction is broken, or an entity script lacks the event functions.</td><td>Make the entity extend <code>LeveldotEntity</code>, export again.</td></tr>
<tr><td>E303</td><td>A stored value no longer fits the entity's setting.</td><td>Set it again in the level or the script.</td></tr>
</tbody>
</table>
</details>

A failed export keeps the level's previous export, so the game never breaks halfway.
