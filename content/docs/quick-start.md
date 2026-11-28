# Quick Start

From an empty level to your own game scene in five steps.
{: .lead }

1. **Open Leveldot** and save your project ([[Ctrl+S]]) in a folder of your choice.
2. **Link the Godot project** your levels should go to: choose **File → Link Godot Project…** and pick the folder that holds `project.godot`.
3. **Export to Godot:** save again with [[Ctrl+S]] (or [[Ctrl+E]]). Your levels go into the game.
4. **In Godot:** make sure the Leveldot plugin is on (**Project → Project Settings → Plugins**), then **Project → Reload Current Project**.
5. **Make your game scene:** open the **Leveldot** screen at the top of Godot, select your level in **Levels**, press **Create Game Scene…**.

<figure class="ui-strip"><img src="../img/qs-leveldot-tab.jpg" alt="Godot's top bar with the Leveldot screen next to 2D, 3D, Script, Game and Asset Store" width="530" height="44" loading="lazy"><figcaption>The Leveldot screen in Godot</figcaption></figure>

<figure class="ui-strip"><img src="../img/qs-create-game-scene.jpg" alt="The Levels tab of the Leveldot screen with the Backrooms level selected and the Create Game Scene button" width="900" height="252" loading="lazy"><figcaption>Levels → Create Game Scene…</figcaption></figure>

This makes a scene with your level inside it as **World**. Add anything you want to this scene: your player, enemies, scripts.

<figure class="ui-strip"><img src="../img/qs-world.jpg" alt="The new scene in Godot: Backrooms with the World level under it" width="262" height="68" loading="lazy"><figcaption>Your scene, with the level as World</figcaption></figure>

<div class="note"><p><strong>Keep World as it is.</strong> If you make World editable in Godot, your changes in Leveldot no longer appear.</p></div>

More on linking: [Link Godot](link-godot.html).
