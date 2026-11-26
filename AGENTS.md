# Leveldot Editor website

Leveldot Editor'ün herkese açık statik sitesi (<https://leveldoteditor.com>): tanıtım ana sayfası
(özet, ekran görüntüleri, itch.io / Discord / YouTube bağlantıları) ve kısa dokümantasyon. GitHub Pages'te
`site/` klasöründen yayımlanır.

Bu dosya bu projede çalışan her ajanın (Claude Code, Codex, diğerleri) ortak sözleşmesidir. Proje kuralları
yalnız burada durur; CLAUDE.md yalnız `@AGENTS.md` satırıdır.

## Belgeler (tam liste)

Projede yalnız bu belgeler vardır; yeni bir `.md` önce buraya bir satırla eklenir (kanca, listede olmayan
yeni belgeyi engeller). Geçmiş `git log`'dadır.

| Belge | Ne için |
|---|---|
| `AGENTS.md` | bu sözleşme: komutlar, akış, kurallar, tuzaklar |
| `CLAUDE.md` | yalnız `@AGENTS.md` |
| `README.md` | kullanıcı için: nasıl çalıştırılır, nasıl kullanılır |
| `docs/HANDOFF.md` | şu anki durum, doğrulanmayanlar, bekleyen istekler (değiştirilir, eklenmez) |
| `docs/DECISIONS.md` | kararlar ve nedenleri (ADR) |
| `content/docs/install.md` | site sayfası kaynağı: Install (`site/docs/index.html`) |
| `content/docs/link-godot.md` | site sayfası kaynağı: Link Godot |
| `content/docs/basics.md` | site sayfası kaynağı: Basics (ekran, seçim, dönüşüm, kamera) |
| `content/docs/tools.md` | site sayfası kaynağı: Tools |

## Komutlar

| İş | Komut |
|---|---|
| Sayfaları üret | `python scripts/build.py` (editör reposunun `master`'ındaki `docs/SHORTCUTS.md`'yi okur; yol: `--source`, `$env:LEVELDOT_EDITOR_REPO` ya da git-ignored `.source-path` ilk satırı) |
| Yalnız ortak üst / alt bloğu yaz | `python scripts/build.py --shared-only` |
| Tam kapı (commit öncesi) | `powershell -ExecutionPolicy Bypass -File scripts/ci.ps1` → `CI: ALL GATES PASSED` |
| Yayın | `master`'a push → `.github/workflows/pages.yml` denetler ve `site/`'ı yayımlar |

## Çalışma akışı (her ajan)

1. Önce bu dosya, sonra handoff; handoff'taki iddiaları koda ve `git log`'a karşı doğrula.
2. Dosya değiştiren her oturum kendi git worktree'sinde ve branch'inde çalışır; ana kopyadaki
   commit'lenmemiş dosyalar başka bir oturumundur, dokunma.
3. Kod → test → tam kapı yeşil → yalnız açık yollar stage edilir (`git add .` yok) → commit → master'a
   merge → worktree silinir. Sürüm ve ADR numarasını yalnız master'a merge eden verir (yan dal `ADR-TBD`).
4. Belgeler: karar → DECISIONS.md, kural/komut/tuzak → bu dosya, kullanıcıya görünen değişiklik →
   README, iş bitince durum → handoff (değiştirilir, eklenmez). Plan, rapor, not, özet dosyası yok;
   yanlışlaşan metni aynı işte düzelt ya da sil.
5. Metinler UTF-8, Türkçe karakterlerle (ç ğ ı ö ş ü). Sırlar (.env, anahtar, token) asla commit'lenmez.
6. Kullanıcıya soru yalnız felakette (veri kaybı, geri alınamaz adım, kırık master); test listesi yok.

## Kurallar

- **Repo herkese açık.** Yerel yol, kullanıcı adı, e-posta, editörün özel kaynak kodu buraya girmez
  (`check_site.py` sayfalarda yerel yol ve e-posta arar). Editör reposunun yeri yalnız git-ignored `.source-path`'te.
- **Doküman sayfaları** `content/docs/*.md`'den üretilir (`site/docs/*.html` elle düzenlenmez). Yazım:
  İngilizce, sade; her bölüm başlıklı, kısa maddeler / tablolar, üst üste uzun paragraf yok. Anlatılan şey
  editörün kılavuzunda (editör reposu `docs/MANUAL.md`, `LINK-GODOT.md`) olandır; site onu kısaltır,
  yeni iddia eklemez. Kafa karıştıran şey yazılmaz: hata kodları, iç terimler (reaction, export
  schema…), ne anlattığını söylemeyen başlıklar (“Every day”); başlık bölümün işini söyler. Sayfa listesi ve sırası: `build.py` `PAGES`. Öğretici (Tutorial) sitede yok;
  uygulamada **Help → Tutorial**.
- **Tuşlar** `[[Ctrl+S]]` diye yazılır (`/` ile alternatif: `[[F7 / Alt+O]]`); `build.py` onları tuş
  kapakçığına çevirir ve editörün `SHORTCUTS.md`'sinde olmayan bir tuşta durur (fare hareketleri ve araç
  içi tuşlar `EXTRA_KEYS`'te). Shortcuts sayfası tümüyle `SHORTCUTS.md`'den üretilir.
- **Diyagramlar** HTML + CSS'tir, resim değil: `.flow` (kutular ve oklar; telefonda alt alta), `.tree`
  (dosya ağacı), `.annotated` (pencere görüntüsü + numaralı `.pin`'ler, altında `ol.legend`),
  `.ui-strip` (uygulamadan kesilmiş küçük arayüz şeridi), `.keycards`, `.cards`. Tema renklerini
  kullanırlar, ikisinde de okunur. Arayüz görüntüleri `site/img/ui-*.jpg`: kullanıcının verdiği gerçek
  ekran kesitleri; `.pin` konumları görüntüdeki yüzde koordinatlarıdır, görüntü değişince güncellenir.
- **Ortak üst bar ve alt bilgi** `build.py`'deki `header()` / `footer()`'dadır; `site/index.html`'de
  `<!-- header -->` / `<!-- footer -->` işaretleri arasına o yazar. Logonun sağ üstündeki **Alpha** hapı
  orada. Bağlantılar (itch.io, Discord, YouTube) yalnız `build.py` `LINKS`'te ve `index.html` gövdesinde;
  değişince ikisi birlikte.
- **Mantık (logic) sistemi deneyseldir** (kullanıcı, 2026-11-26: henüz olgunlaşmadı): sitede az yer alır,
  geçtiği yerde `.tag-exp` "Experimental" etiketi taşır (Tools'ta iki cümle, ana sayfada yarım cümle,
  kısayol kartlarında başlık etiketi). Tanıtımda öne çıkarılmaz, ekran görüntüsü yok.
- Ana sayfa (`site/index.html`) elle yazılır, İngilizce; özellik metinleri editörün kılavuzunda olanı
  söyler, olmayan özellik ya da fiyat iddiası yazılmaz.
- Dış kütüphane, web fontu, izleme betiği yok; yalnız `site/` altındaki HTML / CSS / JS.
- Ekran görüntüleri `site/img/shot-*.jpg` (1600 × 900, JPEG kalite 90). Kaynağı editör reposunun smoke
  render'ları: geçici, detached bir worktree'de `scripts/smoke_test.ps1 -Only logic_audit`
  (`logic-audit-textured-modeling`, `-sample-1600-all`, `-sample-quad-selected`) ve tam smoke'un
  `levels-view-1600` / `surface-details-1600` render'ları. Godot koşusu ağır iştir: makinede başka CI /
  iniş koşmuyorken. Logo ve ikon editörün `editor-app/ui/brand/`'ından.
- Arayüz durumları dolgu ile gösterilir, renkli kenarlıkla değil. Telefon genişliği (390 px) yatay
  kaydırmasız çalışır.
- **Alan adı** `leveldoteditor.com` (kullanıcının, Cloudflare Registrar; DNS Cloudflare'de): dört A kaydı
  `185.199.108–111.153` ve `www` CNAME `onur-c.github.io`, hepsi **DNS only** (gri bulut). Cloudflare'in
  "proxy" önerisi uygulanmaz: turuncu bulutta GitHub HTTPS sertifikasını yenileyemez. Özel alan adı
  Pages ayarında (`gh api repos/onur-c/leveldoteditor.com/pages`, `cname`, `https_enforced: true`), repoda
  `CNAME` dosyası yok (Actions ile yayında gerekmez). `github.io` adresi ve `www` alan adına yönlenir.
  Alan adı GitHub hesabına doğrulanmış (TXT `_github-pages-challenge-onur-c`); o kayıt silinmez.

## Tuzaklar

- GitHub Pages tarayıcıya 10 dakika önbellek izni verir: CSS değişip HTML yenilenince eski CSS ile yeni
  sayfa karışır (2026-11-26: işaretler resmin altına "1234567" diye düştü). `style.css` / `docs.js`
  bağlantıları bu yüzden `?v=<içerik özeti>` taşır; `build.py` yazar, `check_site.py` sürümsüz ya da eski
  özeti reddeder. CSS / JS değişince `build.py` koş. `build.py` `site/index.html`'i de yeniden yazar: commit'e `site/` bütünüyle girer (2026-11-26: yalnız `site/docs` stage edildi, GitHub denetimi yayını durdurdu).

- Başsız Edge `--window-size=390,…` ile telefonu göstermez (pencere ~500 px'ten daraltılmaz, sayfa kesik
  görünür). Telefon görünümü için sayfayı 390 px genişliğinde bir `<iframe>` içinde render et.
