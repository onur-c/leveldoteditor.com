# Leveldot site

Leveldot Editor'ün herkese açık statik sitesi: tanıtım ana sayfası (özet, ekran görüntüleri, itch.io /
Discord / YouTube bağlantıları) ve editörün kendi kullanıcı belgelerinden üretilen dokümantasyon. GitHub
Pages'te `site/` klasöründen yayımlanır.

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

## Komutlar

| İş | Komut |
|---|---|
| Belgeleri yeniden üret | `python scripts/build.py` (editör reposunun `master`'ından okur; yol: `--source`, `$env:LEVELDOT_EDITOR_REPO` ya da git-ignored `.source-path` ilk satırı) |
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
- **Belgelerin tek kaynağı editör reposudur** (`docs/MANUAL.md`, `LINK-GODOT.md`, `SHORTCUTS.md`,
  `TUTORIAL.md`; F1'de de onlar görünür). `site/docs/*.html` üretilir, elle düzenlenmez; metin hatası
  editör reposunda düzeltilir, sonra `build.py` koşulur. Hangi belgeden hangi sayfa: `build.py` `PAGES`.
- **Ortak üst bar ve alt bilgi** `build.py`'deki `header()` / `footer()`'dadır; `site/index.html`'de
  `<!-- header -->` / `<!-- footer -->` işaretleri arasına o yazar. Bağlantılar (itch.io, Discord,
  YouTube) yalnız `build.py` `LINKS`'te ve `index.html` gövdesinde; değişince ikisi birlikte.
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

## Tuzaklar

- Başsız Edge `--window-size=390,…` ile telefonu göstermez (pencere ~500 px'ten daraltılmaz, sayfa kesik
  görünür). Telefon görünümü için sayfayı 390 px genişliğinde bir `<iframe>` içinde render et.
