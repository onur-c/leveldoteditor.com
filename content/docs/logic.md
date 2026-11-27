# Entities and logic

<div class="note"><p><strong>Completely optional.</strong> Leveldot builds and exports levels without any of this: use your own entities and logic only if your game needs them.</p></div>

<div class="note"><p><span class="tag-exp">Experimental</span> <strong>Logic is still being built.</strong> It works, but it grows and changes with each version: windows, names and steps on this page may change. Share what you need on the Leveldot <a href="https://discord.gg/e3CdgVQxp" target="_blank" rel="noopener">Discord</a>.</p></div>

## What an entity is

An entity is an object that does something in the game: a light, a door, a lift, a trigger, an effect.

Its script says what it can do, in plain Godot:

| In the script | In Leveldot |
|---|---|
| `@export` variable | a **setting**, edited in Entity Details |
| public function | something it **does** when told |
| signal | something it **announces**, to start a connection |

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

- Your Godot code can talk to an entity too: **Entity Details → Events → Copy game code** copies the lines to use.

## Write the script

An entity type is a scene in `res://leveldot/entities/`: a `Node3D` root with a script that extends `LeveldotEntity`.

| You write | Leveldot reads it as |
|---|---|
| `signal powered_up` | an announcement with no value |
| `signal fuel_changed(litres: float)` | an announcement that carries one value |
| `func add_fuel(litres: float) -> void` | a command that takes one value |
| `func shut_down() -> bool` | a command that may refuse: return `false` |
| `@export var capacity := 20.0` | a setting; `@export_range` gives it a min and max |
| `## Pours fuel in.` above a member | the help text Leveldot shows for it |
| `const LEVELDOT_CATEGORY := "Machines"` | the group it is filed under in the drawer |

- A signal or a function takes **at most one value**, typed: `bool`, `int`, `float`, `String` or `Vector3`. A setting can also be a `Color`.
- Names that start with `_` stay private: Leveldot does not offer them.

## Example: a generator

A generator that needs fuel before the lights come back on.

```gdscript
## A generator. Fill it up and it powers the room.
extends LeveldotEntity

const LEVELDOT_CATEGORY := "Machines"

## Sent once, when the tank is full.
signal powered_up
## Sent on every refill, with the litres in the tank.
signal fuel_changed(litres: float)

## Litres it needs before it runs.
@export_range(1.0, 100.0) var capacity := 20.0

var _fuel := 0.0

## Pours fuel in.
func add_fuel(litres: float) -> void:
	if _fuel >= capacity:
		return
	_fuel = minf(_fuel + litres, capacity)
	fuel_changed.emit(_fuel)
	if _fuel >= capacity:
		powered_up.emit()

## Stops it and empties the tank. Refused while it is empty.
func shut_down() -> bool:
	if _fuel <= 0.0:
		return false
	_fuel = 0.0
	fuel_changed.emit(_fuel)
	return true
```

After **Update from Godot**, the Generator is in the drawer under **Machines**, with **capacity** in its settings. Wire it up in the level with [[K]]:

<div class="flow">
  <div class="node"><p class="node-kicker">Trigger Area</p><p class="node-title">entered</p><p class="node-text">the player walks in with a can</p></div>
  <div class="edge"><span>add_fuel, value 5</span></div>
  <div class="node"><p class="node-kicker">Generator</p><p class="node-title">powered_up</p><p class="node-text">after four cans</p></div>
  <div class="edge"><span>turn_on</span></div>
  <div class="node accent"><p class="node-kicker">Omni Light</p><p class="node-title">The room lights up</p></div>
</div>

- **entered → add_fuel**: `entered` carries no value, so the connection gives `add_fuel` a fixed one: 5 litres.
- **powered_up → turn_on**: every light in the room can listen to the same announcement.
- `fuel_changed` carries its value along: connect it to a command that takes a `float`, such as a gauge of your own.
- If something tells an empty generator to `shut_down`, it refuses and nothing else happens.
