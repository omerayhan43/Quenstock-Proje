# Dipten Dönüş (BISTTUM) — DURUM (zaman damgalı kayıt)

## 01/10 10:10 — Başlangıç
- Ömer planı onayladı ("başlayabilirsin"); ek notlar YOL_HARITASI.md'de (dar tutma: kâr sıçraması + çarpan düşüşü de dahil; sade, hızlı formül).
- Altyapı: mevcut IDB `u3_AA/YYYY` (262 ay, BISTTUM kapanışları + K10 maskesi), `a41dates` (ay → sıralama tarihi), işçi kodu `src_u3worker` / `__postR`.

## 01/10 10:50 — Literatür + veri + altyapı
- **Literatür tamam:** LITERATUR.md (sentez) + LIT_A–D. Ortak sonuç: ΔE/P = (TTM net kâr − 4 çeyrek önceki TTM net kâr)/PD tek olay ölçüsü; momentum onay kapısı; sahte kâr korumaları; sade iskelet (1 filtre + 2 kapı skora gömülü + 3 bileşen).
- **Site altyapı testi:** model **208552** "BISTTUM uyelik tespiti - hepsi gecer, 800 hisse, Hersey Dahil (2005-2026)" (208514'ten Farklı Kaydet; kriter 98295, N=800, hisse kriteri 19006). Test 10:0x'te başladı. Amaç: her ayın BIST TÜM üyeleri + site getirileri (işlemden kalkan hisseler dahil).
- **Veri (IDB):** `dd_forms` (5 paketlenmiş formül: F1 ROE 0/−1/−4/−8 + net kâr marjı · F2 E/P 0/−4/−8, çeyreklik kâr işaret bitleri, FAVÖK/FD · F3 PD/DD, F/K, FD/FAVÖK, NetBorç/FAVÖK, HA · F4 C/HHV252, C/LLV252, C/HHV756, C/MA200, MA50/MA200 · F6 log PD, borç/aktif 0/−4, log 20g işlem hacmi, satış büyümesi), `dd_need` (ay → u3'te kapanışı olan hisseler, ort. 378), `dd_lists` (4 sekme listesi), kayıtlar `dd_AA/YYYY` (262 ay, 10/2026 dahil). İşçi kodu `src_ddworker` (`__ddRun(list)`), 4 sekmede ~84 sn/ay. 10:40'ta 77/262 ay; tahmini bitiş ~11:45.
- **Getiri doğrulaması:** u3 kapanışlarından ay getirisi, Büyüme BISTTUM (208452) site seçimlerinde 1.221/1.225 hisse-ay ±0,5 puan içinde (ort. mutlak fark 0,008 puan; yalnız Ocak 2005 farklı). Site seçimlerinin %5,3'ü (69/1.294) bugün işlem görmeyen (hayalet) hisse → sim bunları puanlayamaz; site testi belirleyici.
- **Sim kodu (IDB):** `code_dd` (DD.load, DD.run, DD.stats, DD.pair), `code_ddteshis` (DD.event olay çalışması, DD.winners), `code_ddt0` (T0). Kazananlar listesi `dd_winners` (her yıl ilk 50, u3 kapanışlarıyla).
- Ön kayıt: ON_KAYIT_TABAN.md (T0).

## 01/10 13:05 — Teşhis (tam dönem, 254/262 ay) + T0 taban + üyelik verisi
- **Üyelik modeli 208552 okundu** (IDB `siteres_208552`): 261 ay, ayda 245–590 üye, site getirileriyle. Veri olan aylarda site üye-aylarının %5,8'i bugün işlem görmeyen (hayalet) hisse. Sim artık **site getirileri ve site evreni** ile çalışıyor (`code_ddsite`).
- **Olay çalışması** (tüm hisse-aylar, ileri getiri; "fark" = ortalama − kesit medyanı, puan; isabet = getiri > 0 oranı):
  | Grup | n | 1 ay fark | 12 ay fark | 12 ay isabet |
  |---|---|---|---|---|
  | Tümü | 93.894 | 2,6 | 27,5 | %65 |
  | Kâr sıçraması (P2: E/P₋₄>0, ΔE/P≥0,03) | 19.349 | 3,0 | 28,4 | %73 |
  | P2 + C>MA200 | 13.072 | 3,4 | 31,4 | %73 |
  | Dönüş (P1: kâr/ROE negatiften pozitife) | 13.734 | 3,0 | 29,0 | %61 |
  | P1 + C>MA200 | 7.036 | 3,5 | 32,9 | %61 |
  | ΔE/P ≥ 0,10 | 14.579 | 3,3 | 34,6 | %68 |
  | ΔE/P < −0,05 (kâr çöküşü) | 19.688 | 2,3 | 31,1 | %65 |
  Yorum: MA200 teyidi iki profili de iyileştiriyor; kâr sıçraması isabetli, dönüş piyango profilli (ortalama yüksek, isabet düşük); kâr çöküşünün 12 ay farkı yüksek → ortalamaya dönüş/hayatta kalma etkisi, dikkat.
- **Kazananlar:** her yılın ilk 30'unun %72'si yıl içinde P1/P2 profilinde — ama evrenin %68'i de → gevşek tanım ayırt etmiyor; sürekli ölçü (ΔE/P büyüklüğü) ve teyitler gerekli. T0 ilk 30'ların 140/630'unu (%22) en az bir ay aldı.
- **T0 taban (sim, site getirisi, 254 ay):** 1,18 mr TL · CAGR %55,7 · Sharpe 0,93 · kazandıran %63,8 · K-Ratio 0,21 · MDD −%53,6 · kriz ort. −%5,21 · 2005–15 %33,5 / 2016–26 %84,0 · 248/254 ay 5 hissenin hepsi A∧B katmanından. Büyüme/Değer BISTTUM'un belirgin altında → geliştirme gerekli (taban beklendiği gibi).
- **İkinci veri turu başladı:** `dd2_forms` (F7 nakit akışı verimi, serbest nakit akışı verimi, FAVÖK değişimi/PD, EFK çeyrek değişimi/PD, net kâr çeyrek değişimi/PD · F8 FAVÖK ve brüt marj 0/−4, faiz karşılama · F9 cari oran, nakit/net kâr, ROIC, temettü verimi, bedelli · F10 oynaklık 60g, MAX 21g, hacim 5/60, zirve tazeliği, 3 yıl dipten uzaklık · F11 beta, işlem yaşı, C/MA20, 60 günde yukarı gün sayısı, 3 ay zirveye uzaklık). İşçiler ilk tur bitince otomatik başlar (`src_ddworker2`, `dd2_AA/YYYY`).
- Metrik kataloğu: `araclar/METRIK_KATALOGU.md` (ortak araç).

## 01/10 14:00 — Tarama 1. aşama (dd alanları, 41 metrik)
- Veri: `dd_` 262/262 ✓. `dd2_` 55/262 (devam). F9'da bedelli alanı bazı hisselerde HATA (IF iki kolu da hesaplıyor) → F9 sonra `||` kısa devreyle yeniden toplanacak; F7, F8, F10, F11 temiz.
- T0 (site getirisi, 261 ay): 0,97 mr · CAGR %52,5 · Sh 0,87 · kaz %63,6 · KR 0,21 · MDD −%53,6.
- **Tek metrik sıra-IC** (site evreni, 1 ay ileri, t): FAVÖK/FD +6,5 (t 11,2) · FD/FAVÖK −6,9 · F/K⁻¹ +5,7 · E/P +6,1 · ΔROE (1 çeyrek) +3,8 (t 8,8) · son çeyrek kâr>0 +3,6 · ROE +4,9 · PD/DD⁻¹ +4,3 · ΔE/P +2,8 (t 6,0) · 52h zirveye yakınlık +4,6 (t 4,7) · likidite −4,0 (küçük/sığ hisseler önde) · fiyat momentumu (1–12 ay) ≈ 0 (t < 1,3). Hepsi iki yarıda aynı işaretli (ROE düzeyi ve son çeyrek 2016+ zayıf).
- **Rol taraması:** 41 metrik × 10 rol/düzey = 410 birebir sim (sayaç N≈420). Ön filtre (fark>0, iki yarı>0, en iyi 5 ay çıkınca>0, kaz ≥ taban−0,5, Sharpe ≥ taban, t ≥ 1,5): **19 geçti.** En iyiler:
  | Aday | son (mr) | Sh | kaz | KR | fark (puan/yıl) | t | yarılar | en iyi 5 ay yok |
  |---|---|---|---|---|---|---|---|---|
  | likidite en düşük %20 kapı | 31,5 | 1,18 | 67,8 | 0,23 | 16,0 | 2,32 | 8,8/23,3 | 9,1 |
  | borç azaltma (borç/aktif düşüşü) kapı üst %40 | 10,5 | 1,16 | 70,5 | 0,33 | 10,9 | 1,73 | 8,9/13,0 | 5,6 |
  | borç azaltma skor ×2 | 6,5 | 1,11 | 69,0 | 0,36 | 8,7 | 1,79 | 10,1/7,3 | 3,6 |
  | FAVÖK/FD skor ×2 | 5,7 | 1,13 | 66,3 | 0,24 | 8,1 | 1,76 | 7,9/8,3 | 3,6 |
  | son çeyrek kârı > 0 skor ×2 | 6,6 | 1,09 | 65,5 | 0,27 | 8,8 | 1,80 | 8,3/9,3 | 3,0 |
  | net borç/FAVÖK düşük kapı üst %40 | 6,2 | 1,12 | 67,4 | 0,38 | 8,5 | 1,61 | 13,5/3,4 | 4,1 |
- **Anlamlılık:** ≈420 denemede şans eşiği t* ≈ 3,5; hiçbir tek aday bunu geçmiyor (en yüksek 2,32). Tek başına hiçbiri "kanıtlanmış" değil → 2. aşama kombinasyon + dd2 metrikleri. Likidite kapısı uygulanabilirlik/manipülasyon riski taşır (kapasite testi şart).
- Kod: `code_ddscan` (DD.derive, DD.ic, DD.evalP, DD.withMetric); sonuçlar `dd_scan1`.

## 01/10/2026 ~15:10 — Tarama 2b: ileri seçim (dd alanları, sitesiz)
- Oturum düştü (QS + borfin yönlendirmesi "error"). dd2 55/262'de durdu; şifre girilmedi, Ömer'den giriş istendi.
- Yöntem: T0 üzerine her adımda 532 aday (38 metrik × 2 yön × K0.2/0.4/0.6/0.8, S1/S2, C0.2; liq ve lpd kapasite nedeniyle ayrı). Seçim yalnız 2005–2020 (IS); 2021–26 dokunulmaz (OOS). Terfi: IS NW t ≥ 2,0 + iki yarı + en iyi 5 ay çıkınca + kazandırma/Sharpe kötüleşmez.
- Adım 1: dTBA-S2 (borç/aktif düşüşü bonusu) IS t 2,22, fark +11,7 puan/yıl; plato komşusu S1 t 1,48; OOS +3,9 puan, t 0,39. Tam dönem: 7,91mr, CAGR 68,0, Sh 1,13, kaz 69,3, KR 0,36, MDD −60,9.
- Adım 2: geçen aday yok (en iyi roe0+K0.2 t 1,84 ama fark ~0).
- Diğer IS adayları: fdf-K0.8 t 2,08 (OOS −1,0), dTBA-K0.6 t 1,82, nbf cezası t 1,74 (OOS −5,9).
- Liq-K0.8 (ayrı): IS t 2,59, OOS +5,0 puan t 0,35.
- Deneme sayacı: 811 + 1.050 = 1.861; t* ≈ √(2 ln 1861) ≈ 3,9. **Hiçbir aday istatistiksel olarak anlamlı değil**; OOS'ta hepsi zayıf. T0 iskeleti sağlam, eklemeler gürültü düzeyinde.
- Sonraki: oturum açılınca dd2 (nakit akışı, FAVÖK değişimi, çeyreklik kâr, risk/MAX vb.) toplanacak ve aynı hatla taranacak.
