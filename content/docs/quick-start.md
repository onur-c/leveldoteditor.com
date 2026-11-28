# Quick Start

From download to your own game scene in a few steps.
{: .lead }

1. **Download Leveldot** from [itch.io](https://onur-c.itch.io/leveldot-editor), extract the ZIP and run `LeveldotEditor.exe` ([Install](install.html) has the details).
1. **Open Leveldot** and save your project ([[Ctrl+S]]) in a folder of your choice.
2. **Link the Godot project** your levels should go to: choose **File → Link Godot Project…** and pick the folder that holds `project.godot`.
3. **Export to Godot:** save again with [[Ctrl+S]] (or [[Ctrl+E]]). Your levels go into the game.
4. **In Godot:** make sure the Leveldot plugin is on (**Project → Project Settings → Plugins**), then **Project → Reload Current Project**.
5. **Create Game Scene:** open the **Leveldot** screen at the top of Godot, select your level in **Levels**, press **Create Game Scene…** and choose where to save it.

<figure class="ui-strip"><img src="../img/qs-leveldot-tab.jpg" alt="Godot's top bar with the Leveldot screen next to 2D, 3D, Script, Game and Asset Store" width="530" height="44" loading="lazy"><figcaption>The Leveldot screen in Godot</figcaption></figure>

<figure class="ui-strip"><img src="../img/qs-create-game-scene.jpg" alt="The Levels tab of the Leveldot screen with the Backrooms level selected and the Create Game Scene button" width="900" height="252" loading="lazy"><figcaption>Levels → Create Game Scene…</figcaption></figure>

Leveldot makes the scene for you and opens it, nothing to build by hand: your level is inside it as **World**. Add your player, enemies and scripts to this scene, next to World.

<figure class="ui-strip"><img src="../img/qs-world.jpg" alt="The new scene in Godot: Backrooms with the World level under it" width="262" height="68" loading="lazy"><figcaption>The scene Create Game Scene made, with the level as World</figcaption></figure>

<div class="note"><p><strong>Keep World as it is.</strong> If you make World editable in Godot, your changes in Leveldot no longer appear.</p></div>

<div class="note"><p><strong>Only once.</strong> These steps are the first setup. After that, export from Leveldot ([[Ctrl+S]] or [[Ctrl+E]]) and World updates itself.</p></div>

More on linking: [Link Godot](link-godot.html).
