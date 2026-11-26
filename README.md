# Leveldot Editor website

Leveldot Editor'ün tanıtım ve dokümantasyon sitesi: <https://onur-c.github.io/leveldoteditor.com/>
(alan adı `leveldoteditor.com` alınıp bağlanınca orada).

## Kullanım

- **Site:** ana sayfa kısa tanıtım, ekran görüntüleri ve itch.io / Discord / YouTube bağlantıları;
  **Docs** Install, Link Godot, Basics, Tools ve Shortcuts sayfaları.
- **Metni değiştirmek:** sayfaların kaynağı `content/docs/*.md`; sonra `python scripts/build.py`.
  Kısayol sayfası editörün kısayol listesinden kendiliğinden üretilir; editörde bir tuş değişince yalnız
  `build.py` çalıştırılır. `master`'a gelen her değişiklik birkaç dakika içinde yayında olur.
- **Yerelde bakmak:** `site/index.html`'i tarayıcıda aç; sunucu gerekmez.

## Sık sorunlar

- `build: the Leveldot editor repository was not found` → editör reposunun yolunu `.source-path`
  dosyasının ilk satırına yaz ya da `--source` ver.
- `build: … names keys the editor does not have` → sayfadaki tuş editörde yok ya da değişmiş; tuşu
  düzelt (fare hareketiyse `build.py` `EXTRA_KEYS`'e ekle).
- `No module named 'markdown'` → `pip install markdown`.
- Site güncellenmedi → GitHub'da repo → **Actions** → **Pages** koşusunun sonucuna bak.
