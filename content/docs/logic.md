# Entities and logic

<div class="note"><p><span class="tag-exp">Experimental</span> <strong>Logic is still being built.</strong> It works, but it grows and changes with each version: windows, names and steps on this page may change. Tell us what you need on <a href="https://discord.gg/e3CdgVQxp" target="_blank" rel="noopener">Discord</a>.</p></div>

## What an entity is

An entity is an object that does something in the game: a light, a door, a lift, a trigger, an effect.

- It has **settings**: a light's energy, a door's speed.
- It can **do things** when told: `enable`, `start`, `toggle`.
- It **announces** what happens to it: `entered`, `turned_on`.

## Make your own entity type

<div class="flow">
  <div class="node"><p class="node-kicker">In Godot</p><p class="node-title">New Entity…</p><p class="node-text">a script that extends <code>LeveldotEntity</code></p></div>
  <div class="edge"><span>Update from Godot</span></div>
  <div class="node"><p class="node-kicker">In Leveldot</p><p class="node-title">A tile in the Entities drawer</p></div>
  <div class="edge"><span>drag</span></div>
  <div class="node accent"><p class="node-kicker">In the level</p><p class="node-title">An entity with its settings</p></div>
</div>

1. In Godot, open the Leveldot screen → **Entities** → **New Entity…**, which writes the type to `res://leveldot/entities/`. Any script that extends `LeveldotEntity` works too.
2. In Leveldot, open the Entity Catalog ([[Ctrl+Shift+A]]) and press **Update from Godot** (the first time: **Import from Godot…**). Linking a game imports its types for you.
3. The type is now in the **Entities** drawer ([[Shift+A]]), next to the built-in ones.

The built-in entities are ordinary `LeveldotEntity` scripts in the addon. Open one and copy it to start your own.

## Use entities in a level

| Do | Key |
|---|---|
| Open the Entities drawer, drag a type into the view | [[Shift+A]] |
| Search every type | [[Ctrl+Shift+A]] |
| Edit the selected entity's settings and events | [[Alt+Enter]] |
| Write every entity's name above it | [[Alt+Shift+N]] |

## Connect entities <span class="tag-exp">Experimental</span>

Logic is "when this happens, do this": a trigger turns on a light, a button opens a door.

| Do | Key |
|---|---|
| Make the selected entity tell another one to do something | [[K]] |
| The level's own logic: level start, timers, signals | [[Ctrl+L]] |
| See the connections in the level | [[F4]] |
| List every connection in the level | [[Ctrl+Shift+L]] |
| See the connections as a graph | [[Alt+G]] |

- The lists offer only what the entity can do with its current settings. A connection made before a setting changed is kept and marked with **!**.
- Your Godot code can talk to an entity too: **Entity Details → Events → Copy game code** copies the lines to use.
