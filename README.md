# Leveldot site

Leveldot Editor'ün tanıtım ve dokümantasyon sitesi: <https://onur-c.github.io/leveldot-site/>

## Kullanım

- **Site:** ana sayfa kısa tanıtım, ekran görüntüleri ve itch.io / Discord / YouTube bağlantıları;
  **Docs** kurulum, Godot bağlama, araçlar, kısayollar ve öğretici.
- **Belgeler güncellenince:** dokümantasyon editörün kendi belgelerinden (F1'deki kılavuz) üretilir.
  Editörde bir sürüm çıkınca `python scripts/build.py` sayfaları yeniler; `master`'a gelen her değişiklik
  birkaç dakika içinde yayında olur.
- **Yerelde bakmak:** `site/index.html`'i tarayıcıda aç; sunucu gerekmez.

## Sık sorunlar

- `build: the Leveldot editor repository was not found` → editör reposunun yolunu `.source-path`
  dosyasının ilk satırına yaz ya da `--source` ver.
- `No module named 'markdown'` → `pip install markdown`.
- Site güncellenmedi → GitHub'da repo → **Actions** → **Pages** koşusunun sonucuna bak.
