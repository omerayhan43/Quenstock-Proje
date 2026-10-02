# QueenStocks Projesi — BAŞLA BURADAN

Bu klasör, Ömer'in QueenStocks üzerindeki strateji çalışmasının **tüm bağlamıdır**: kurallar, aşama aşama geçmiş, sitedeki bütün kriter/model numaraları, sıradaki işler, araçlar, raporlar ve hafıza yedeği. Yeni bir Claude (Cowork) sohbeti yalnızca bu klasörle, baştan anlatıma gerek kalmadan işe devam edebilmelidir.

Kurulum: 30/09/2026 (önceki uzun sohbetten devredildi). Bu klasör **asıl kaynaktır**; bulut çalışma alanları oturum bitince silinir.

---

## 1. Yeni sohbette ilk adımlar (sırayla)

1. Bu dosyayı sonuna kadar oku.
2. `01_KURALLAR_VE_TERCIHLER.md` — ihlal edilemez kurallar ve Ömer'in çalışma tercihleri.
3. `02_SIRADAKI_ISLER.md` — şu an ne yapılacak, hangi sırayla, hangi doğrulama değerleriyle.
4. `03_SITE_KILAVUZU.md` — tarayıcıda QueenStocks'a dokunmadan önce mutlaka oku.
4b. `07_SIMULASYON_KILAVUZU.md` — simülasyona erişim (Chrome IndexedDB) ve gerekirse sıfırdan kurma. Sim çalışmadan yeni aday test edilmez.
5. Gerektikçe: `04_ID_KAYDI.md` (bütün kriter/model ID'leri), `05_PROJE_GECMISI/` (4 stratejinin özet geçmişi), `projeler/<klasör>/DURUM.md` (ayrıntılı zaman damgalı günlükler).
6. `06_HAFIZA/` — bulut hafızasının yedeği; senkron kuralı `06_HAFIZA/README_SENKRON.md`.
7. `OTURUM_GUNLUGU.md` dosyasına başlangıç satırı yaz (tarih, saat, ne yapacaksın). Bitince ne yaptığını ve yarım kalanı yaz.
8. Ömer'e kısa bir "devir alındı" mesajı ver: şu anki durum + ilk yapacağın iş + tahmini süre.

Bu klasöre erişim: Cowork'te bu klasör sohbete bağlanmış olmalı ("Add folder" / klasör erişim onayı). Bağlı değilse Ömer'den bağlamasını iste; klasörü bilgisayarda aramaya çalışma.

---

## 2. Proje haritası (30/09/2026 itibarıyla)

| Strateji | Evren | Şampiyon | Kriter / Model | Site sonucu (100 bin TL → 09/2026) | Durum | Ayrıntı |
|---|---|---|---|---|---|---|
| **Büyüme Stratejisi (BISTTUM)** | BIST TÜM ("Herşey Dahil" 19006) | K10 | 98258 / 208322 | 953.463.410.572 TL · Sharpe 1,61 · kaz %73,95 · MDD −41,7 | Tamamlandı (final rapor) | `projeler/alfa_v41/`, `05_PROJE_GECMISI/Buyume_BISTTUM.md` |
| **Değer Yatırımı (BISTTUM)** | BIST TÜM | C32 | 98194 / 208224 | 777.959.361.011 TL · Sharpe 1,76 · kaz %77,78 · MDD −37,4 | Beklemede (Ömer "strateji strateji" ilerlemek istedi) | `projeler/deger_v11/`, `05_PROJE_GECMISI/Deger_BISTTUM.md` |
| **Büyüme Stratejisi (BIST100)** | Sadece BIST100 (19024) + geçmiş endeks | K4a | 98322 / 208422 | 5.850.921.769 TL · Sharpe 1,26 · kaz %68,58 · MDD −38,6 | Aşama 5b bitti; Aşama 6 ortak yürüyor | `projeler/buyume_bist100/`, `05_PROJE_GECMISI/Buyume_BIST100.md` |
| **Değer Yatırımı (BIST100)** | Sadece BIST100 + geçmiş endeks | DX3b (Ömer seçti; "keşif" etiketli) | 98329 (ad düzeltilmiş kopya 98342) / 208433 | 3.092.532.238 TL · Sharpe 1,17 (site) · kaz %68,2 · MDD −31,8 | Aşama 6 ortak yürüyor | `projeler/deger_bist100/`, `05_PROJE_GECMISI/Deger_BIST100.md` |

Kural tabanlı Değer BIST100 şampiyonu DC1'dir (98324 / 208424, 1,749 mr). DX3b onu tüm tanımlayıcı ölçülerde geçti ama terfi kuralını geçmedi (t 1,45 < 1,5; 2015+ farkı sıfır); Ömer DX3b'yi seçti.

**Birleşimler**
- BISTTUM %50 K10 + %50 C32 (aylık eşitleme): 1,114 tr, Sharpe 1,87 (29/09 kararı).
- BISTTUM "Büyüme + Ortak": 1,781 tr brüt; 5 mn TL'de maliyet sonrası yıllık %91,0 (50/50: %93,2); kapasite yaklaşık yarısı. Rapor: `projeler/alfa_v41/BISTTUM_Buyume_Deger_Yatirimi_Strateji_Raporu_2026-09.pdf` (85 sayfa).
- BIST100 50/50 (Büyüme K4a + Değer DX3b): 4,70 mr, Sharpe 1,28, MDD −30,6, kaz %72,8; aylık korelasyon %80 (Aşama 6a).

**Ömer'in yatırım planı (kendi kuralı):** Büyüme Stratejisi'nin 5 hissesi alınır; aynı ay Değer Yatırımı Stratejisi'nde de çıkan hisse **2 pay**, diğerleri 1 pay. Ortak hisse yoksa portföy Büyüme Stratejisi'nin kendisidir. Hesap aracı (Claude artifact, Algomer'e eklenmedi): "Büyüme + Ortak Pay Hesabı" — https://claude.ai/artifact/2URNniVpHdQnXpGwbYe5hS ; kaynak `araclar/arac/pay_hesabi.html`.

---

## 3. Klasör yapısı

```
QueenStocks Projesi/
  00_BASLA_BURADAN.md          ← bu dosya
  01_KURALLAR_VE_TERCIHLER.md  ← kurallar, tercihler, yöntem, raporlama
  02_SIRADAKI_ISLER.md         ← yapılacaklar sırası + doğrulama değerleri + silinecekler
  03_SITE_KILAVUZU.md          ← QueenStocks otomasyon kılavuzu (seçiciler, adımlar, tuzaklar)
  04_ID_KAYDI.md               ← tüm kriter/model ID'leri, durumları, silinecekler listeleri
  07_SIMULASYON_KILAVUZU.md    ← sime erişim, mimari, sıfırdan kurma adımları, tuzaklar
  05_PROJE_GECMISI/            ← 4 stratejinin devir özetleri (aşamalar, sonuçlar, elenenler)
  06_HAFIZA/                   ← bulut hafızasının birebir yedeği + senkron kuralı
  OTURUM_GUNLUGU.md            ← her sohbetin ne yaptığı (sona ekle)
  projeler/
    alfa_v41/       ← Büyüme BISTTUM (K10) + birleşimler + BISTTUM raporu (PDF/Excel)
    deger_v11/      ← Değer BISTTUM (C32) + PROTOKOL.md (ilk devir protokolü) + sim/analiz JS'leri
    buyume_bist100/ ← Büyüme BIST100 (K4a) + kopyala-yapıştır kriter metni
    deger_bist100/  ← Değer BIST100 (DC1/DX3b) + Aşama 6 sonuçları
  araclar/          ← Python/JS analiz araçları, site serileri (README içinde)
```

Her `projeler/<klasör>/` içinde: `DURUM.md` (ana günlük, en güncel bilgi en altta), `YOL_HARITASI.md` (aşama planı ve onaylar), ön kayıtlar (`ON_KAYIT_*`), literatür notları (`LIT*`), kriter metinleri (`*.txt`), ekran görüntüleri (`ekran/`).

---

## 4. Terimler sözlüğü

- **mr / tr:** milyar / trilyon TL (100.000 TL başlangıçtan, 01/2005–09/2026, 261 ay).
- **kaz:** kazandıran ay oranı (%). Ömer için sermayeden önemli.
- **kriz:** XU100'ün −%5'ten kötü olduğu ayların (55 ay) portföy ortalaması.
- **Sim / site:** Sim = tarayıcıda (IndexedDB verisiyle) çalışan birebir kopya simülasyon; site = QueenStocks'un kendi testi (~60–70 dk). Önce sim, sonra site.
- **Terfi kuralı v2:** şampiyon değişikliği şartları (tam hali `01_KURALLAR...` §C).
- **Ön kayıt:** denemeler sonuç görülmeden yazılır ve sabitlenir.
- **Keşif:** ön kayıtsız, sonuca bakılarak bulunmuş aday; etiketi korunur, ileriye dönük fark yarıya indirilerek raporlanır.
- **Plasebo:** aynı sayıda rastgele eleme/bonusla karşılaştırma.
- **Temiz mod / 1 gün gecikme:** ay sonu kapanış yerine ertesi gün alım varsayımı.
- **Hayalet:** geçmişte endekste olup bugün listede olmayan hisse (hayatta kalma yanlılığı düzeltmesi).
- **Tamamlama (nakit yok):** 5'ten az hisse geçen ayda önce teknik, sonra temel koşullar gevşetilerek 5'e tamamlama (katmanlar).
- **E1:** 1 Ekim 2026 yeni BIST100 kurallarının emülasyonu.
- **E36:** site aylık getiri serilerinin sıkıştırılmış metin biçimi (3 karakter/ay, taban-36, baz puan + 20000) — `araclar/b100/cmp.py` içindeki `b64()` okur.
- **2 pay:** ortak hisse kuralı (yukarıda).
- **Silinecekler:** Claude'un silmediği, Ömer'in sitede kendisinin sileceği kriter/model listesi.

---

## 5. Bu klasör nasıl güncel tutulur (her sohbet için zorunlu)

1. Yapılan her işi ilgili `projeler/<klasör>/DURUM.md` sonuna **tarih-saatli** yaz (sonuçlar, kararlar, yeni ID'ler, elenenler ve nedenleri).
2. Yeni kriter/model oluşturunca **hemen** `04_ID_KAYDI.md`'ye ekle (ID, ad, ne olduğu, durum).
3. İş sırası değişince `02_SIRADAKI_ISLER.md`'yi güncelle (bitenleri işaretle, yenileri ekle).
4. Aşama/strateji kararı çıkınca ilgili `YOL_HARITASI.md` ve `05_PROJE_GECMISI/` özetini güncelle.
5. **Hafıza ikili kaydı:** bulut hafızaya (memory) yazılan her kalıcı bilgi `06_HAFIZA/` altındaki aynı dosyaya da yazılır; sohbet sonunda `memory_list` ile karşılaştırıp farkları aktar (ayrıntı `06_HAFIZA/README_SENKRON.md`).
6. Sohbet biterken `OTURUM_GUNLUGU.md`'ye özet satırı ekle.
7. Analiz betikleri/seriler üretildiyse `araclar/` altına kopyala.

---

## 6. Çalışma ortamı notları

- **Tarayıcı:** Ömer'in Chrome'u + **Claude in Chrome** uzantısı (`mcp__claude-in-chrome__*`). Cowork uygulamasının yerleşik tarayıcısı ayrı profildir: orada ne QueenStocks oturumu ne sim verisi (IndexedDB) vardır — onu kullanma. QueenStocks oturumu Borfin üzerinden açık tutulur (şifre asla girilmez; bkz. `03_SITE_KILAVUZU.md` §1).
- **IndexedDB 'claude_c29'** (queenstocks.com kökeni, store 'kv'): sim motorları (`code`, `code_b100*`), veri setleri (`b1_*`, `d1_*`, `b100_mem`, `lq_*`, `nd_*`, `a41dates`…), formül metinleri (`fs_*`, `c32_formulas`), site sonuç önbellekleri (`siteres_ID`). Bu veri Chrome'da kalıcıdır; tarayıcı verisi silinirse yeniden toplanması saatler sürer. Anahtar listesi ve kullanım: `03_SITE_KILAVUZU.md` §6.
- **Python:** `araclar/` içindeki betiklerde yol değişkeni (SP / B / S) eski bulut yoluna ayarlı; yeni ortamda bu klasörün yoluna çevir (README).
- **Uzun sohbet uyarısı (30/09 yaşandı):** Çok uzamış bir sohbette tarayıcı işlemleri bir güvenlik kontrolüyle engellendi ve mod değişikliği bunu açmadı; çözüm yeni sohbet oldu. Bu yüzden: büyük bir iş bloğu bitince bu klasörü güncelle; sohbet çok uzarsa Ömer'e yeni sohbete geçmeyi öner — bu klasör sayesinde kayıp olmaz.

---

## 7. Kısa tarihçe (ayrıntı `05_PROJE_GECMISI/`)

- **27–28/09:** Değer Yatırımı V1.1 (BISTTUM) optimizasyonu: BAZ 94555/208000 (215,6 mr) → … → C29 → **C32** (777,96 mr). Protokol v2 (istatistik, plasebo, temiz mod, gerçekçilik).
- **28–29/09:** ALFA V4.1 (Kârlılık + momentum, geniş havuz) → ALFA V5 yeniden tasarım → **K10** (953,5 mr) = "Büyüme Stratejisi". Aşama 1–7 yol haritası, final rapor, gerçekçi uygulama (maliyet/kapasite), K10+C32 birleşimi.
- **29–30/09:** Büyüme BIST100: B0 (1,80 mr) → B0D2 → K2 → K4c → **K4a** (5,85 mr).
- **30/09:** Ağırlık çalışması (50/50 vs tekil eşit), Büyüme+Ortak, BISTTUM raporu güncellendi (85 sayfa), pay hesap aracı.
- **30/09:** Değer BIST100: D0 (0,667 mr) → DA1 → **DC1** (1,749 mr) → keşif DX3/DX3b → Ömer **DX3b**'yi seçti; Aşama 6 onaylandı; Aşama 6a/6b (korelasyon, 50/50, Deflated Sharpe) yapıldı; isimlendirme işi yeni sohbete devredildi.
