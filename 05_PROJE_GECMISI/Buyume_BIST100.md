# Devir özeti — Büyüme Stratejisi (BIST100)
Kaynak: projeler/buyume_bist100/ (DURUM.md son kayıt 30/09 06:25); Aşama 6a/6b: deger_bist100/DURUM.md. Rakamlar dosyalardan aynen.

## 1. Kimlik
- **Amaç:** BISTTUM Büyüme Stratejisi'ni (K10; kriter 98258 / model 208322; 953,5 mr, Sharpe 1,61) likit BIST100 evrenine uyarlayıp orada en iyi büyüme stratejisini kurmak.
- **Evren:** "Sadece BIST100" (19024) + "Geçmiş tarihlerdeki endekslere dahil hisseleri kullan" işaretli · 5 hisse, eşit ağırlık, aylık, TL, reel hayır, bilanço yayınlanma dönemine göre, 01/01/2005–25/09/2026.
- **Şampiyon:** K4a, sitede **"Büyüme Stratejisi (BIST100)"**, kriter **98322** / model **208422**. 98320/208419 (K4a) ile birebir: 261/261 ay aynı sepet ve getiri, 5.850.921.769 TL, Sharpe 1,26, kazandıran ay %68,58.
- **Formül (kriter/…_kriter.txt):** Temel `uye = PD() > 0`, Teknik `C > 0`. Bütün kapılar Sıralama'da katman olarak çalışır, böylece her ay 5 hisse dolar.
  - Temel kapılar (7): ROE > 5 · FAVÖK > 0 ve NetBorç/FAVÖK < 4 · PD/DD < 8 (ROE > 90 ise gevşer) · 2 ay getiri > XU100 · 1 ay getiri > −15 · HA < 60 · balon (12 ay ≤ 300 veya PD/DD ≤ 8). Ayrıca roeTeyit (ROE önceki çeyreğe ya da 4 çeyrek öncesine göre düşmüyor). F/K hesaplanıyor ama kapı değil.
  - Teknik: [XU100 12 ay < 0 VEYA C > MA150] · C > MA100 · MA20 > MA60.
  - Katmanlar: 0 hepsi · 1 temel tam · 2 yalnız roeTeyit eksik · 3 en az kapı (kalan kapı × 2000 ceza).
  - Öncelik `tam` (+1000): 2 hafta getiri > XUTUM − 10 ∧ satış büyümesi > Tufe(12) ∧ EFK teyidi.
  - Kâr ivmesi = 100 + 25·(pE+pF+pR+pI+pZ) + pen75 + mom6. Bileşenler: EFK ve FAVÖK yıllık değişimi, ROE değişimi, EFK ivmesi, 52 hafta zirve (x/(1+|x|)). pen75: C/MA75 > 1,35 ise −15. mom6: 8·clip(12-6 ay XU100'e göreli).
  - NaN koruması: hesaplanamayan hisse −900000.
- **K10'dan farklar:** (1) evren BIST100 + geçmiş üyelik · (2) 2 ay göreli güç kıyası XUTUM → XU100 · (3) momentum 6-1 → 12-6 ay XU100'e göreli · (4) F/K kapısı kaldırıldı · (5) kapılar katmanda; 5'e tamamlama sırası: teknik yok → ROE düşmüyor esnek → en az kapı · (6) C>MA200 → MA150 ve C>MA75 → MA100 (pen75 aynı) · (7) öncelikten "FAVÖK ∨ brüt+EFK > TÜFE" çıkarıldı (T8) · (8) kötü piyasada MA150 koşulu yok (C3). TÜFE çıtası ve TMS 29 davranışı K10 ile aynı.

## 2. Aşama aşama ilerleyiş
- **Aşama 0 — Taban (29/09 20:00–20:45).** B0 = K10 aynen (208377): 1,80 mr, Sh 1,08, MDD −40,1; XU100'e göre yılda +27,0 puan (t 5,8), K10 BISTTUM'a göre −28,8 (t −4,3). **Havuz açlığı:** 33 ayda 5'ten az hisse; 5 ay 0 hisse, yani fiilen nakit. Üyelik modeli 208379: 261 ay × 100 hisse. Kullanıcı kuralı: Aşama 6'ya onaysız geçilmez.
- **Aşama 1–2 — Veri ve teşhis (✅ 21:50).** Aylık 20 alan (b1_). Hayalet düzeltmeli sim B0 ile 260/261 ay aynı. En bağlayıcı kapı 2 ay göreli güç (%46 geçiyor); ortalama havuz 10,9. **TMS 29:** platform 2024+ büyümeyi reel veriyor, bu yüzden "büyüme > TÜFE" fiilen sert (f geçme 2023 %77 → 2025 %15). BISTTUM K10'da yalnız raporlandı.
- **Aşama 3 — Literatür (LIT_A/LIT_B).** Büyük hissede anomaliler zayıf; sağlam kalanlar orta vadeli momentum, kazanç momentumu, kârlılık. BIST100 kanıtı: 9-12 ay momentum çalışıyor, 3-6 ay çalışmıyor; değer de çalışıyor. 1 Ekim 2026 oynaklık kuralı → sağlamlık testi zorunlu. Beklenti: BISTTUM getirisine ulaşılmaz.
- **Aşama 4 — Ön kayıtlı (ön kayıt ~21:00, sonuç 21:50–22:00).** 25 denemede 0 terfi (kazanç birkaç aya yığılıyor, t < 1,5). C4 TMS düzeltmesi → Ş1. C1/C2 oynaklık/ATR tavanı sağlamlığı geçemedi. Keşif: K1, K1b.
- **Aşama 5 — Site (22:00–22:31).** Ş1 2,030 · K1 2,540 · K1b 2,224 mr. **22:05:** TMS düzeltmesi geri çekildi (BISTTUM simde ×14,33 → ×6,41). Şampiyon B0, K1b aday. 22:25 TÜFE çıtası taraması → çıta değişmez.
- **Aşama 5b — Geliştirme (22:40 → 30/09 06:25).**
  - 22:40 "nakit yok": 396 koşuluk tamamlama taraması. B0D/K1bD NaN hatası 23:47'de düzeltildi. **00:32:** B0D2 1,851 / K1bD2 2,267, şampiyon B0D2.
  - 01:55 kullanıcı: "Aşama 6'ya geçme, geliştirmeye devam". Kapı sökümü → F/K kaldırıldı. **02:45:** K2 3,165 mr şampiyon.
  - Tur 2b/2c/2c-F/2c-G/2d (47+11+3+6+9): 0 terfi. **03:45:** K3b (MA150+MA100) 3,923, t 0,94 → yedek.
  - **04:45:** K4c 5,217 (K2'ye göre t 2,00, kural ✓) şampiyon; K4a 5,851 alternatif (rejim anahtarının katkısı t 0,62).
  - **05:05:** yeni kurallar emülasyonunda K4a önde.
  - **05:33:** kullanıcı K4a'yı şampiyon seçti → 98322/208422. **06:25:** birebir doğrulandı.
- **Aşama 6a/6b (30/09, çevrimdışı; kullanıcı Aşama 6+'yı onayladı).** K4a × Değer DX3b: korelasyon %80 · 50/50: 4,70 mr, Sh 1,28, MDD −30,6, kaz %72,8 · Büyüme − Değer +2,9 puan/yıl, t 0,64 · DSR en sert senaryoda (N=500, σ=0,30) Büyüme %95.

## 3. Site sonuçları (Sadece BIST100 + geçmiş endeks, 2005-01…2026-09, 100 bin TL)
| Etiket (model) | Sermaye | Sharpe | K-R | MDD | Kaz % | Kriz | CAGR 05–15/16–26 | 2015+ | <5 ay | Sim |
|---|---|---|---|---|---|---|---|---|---|---|
| XU100 | 5,07 mn | 0,22 | — | −58,3 | — | −8,69 | %19,8 (tüm) | — | — | — |
| B0 (208377) | 1,802 mr | 1,087 | 0,274 | −40,1 | 68,36 | −4,61 | 39,9/76,5 | 58,5 mn, Sh 1,25 | 33 | 1,93 |
| Ş1 (208389) | 2,030 | 1,105 | 0,268 | −40,1 | 68,75 | −4,57 | 39,9/78,5 | — | 33 | 2,17 |
| K1 (208390) | 2,540 | 1,134 | 0,275 | −40,1 | 68,75 | −4,39 | 41,0/80,8 | — | 33 | 2,83 |
| K1b (208391) | 2,224 | 1,115 | 0,282 | −40,1 | 68,36 | −4,44 | 41,0/78,5 | — | 33 | 2,48 |
| B0D2 (208403) | 1,851 | 1,077 | 0,267 | −41,6 | 68,20 | −4,99 | 38,6/78,6 | — | 0 | 1,90 |
| K1bD2 (208404) | 2,267 | 1,103 | 0,272 | −45,1 | 68,20 | −4,77 | 39,6/80,7 | — | 0 | 2,42 |
| K2 (208415) | 3,165 | 1,164 | 0,271 | −45,1/−45,0* | 68,58 | −4,55 | 40,1/85,7 | — | 0** | 3,38 |
| B0D3 (208416) | 2,098 | 1,108 | 0,258 | −41,6 | 68,97 | −4,87 | 37,8/81,8 | — | 0** | 2,15 |
| K3a (208417) | 3,576 | 1,189 | 0,274 | −43,6 | 68,97 | −4,63 | 41,1/86,5 | — | 0** | 4,10 |
| K3b (208418) | 3,923 | 1,209 | 0,265 | −43,6 | 68,97 | −4,50 | 40,4/89,1 | — | 0** | 4,66 |
| **K4c (208420)** alternatif | 5,217 | 1,248 | 0,274 | −41,5 | 68,97 | −4,32 | 42,1/91,8 | — | 0 | 5,16 |
| **K4a (208419=208422)** şampiyon | 5,851 | 1,261 | 0,287 | −38,6 | 68,58 | −4,29 | 43,9/91,3 | 147,4 mn, CAGR %86,1, Sh 1,51, MDD −20,6 | 0 | 6,02 |

\* DURUM'daki iki tabloda farklı. \*\* Tamamlamalı sürüm; sayı ayrıca yazılmamış [belirsiz, 0 olmalı]. Hatalı sürümler: B0D (208396) 154,1 mn · K1bD (208397) 230,9 mn.
- **Eşli farklar (site, puan/yıl):** K4c − K2 +2,3 (t 2,00, boot [+0,7; +4,6], top5 +0,9) · K4a − K2 +2,8 (t 2,10) · K4a − K4c +0,5 (t 0,62, H2 −0,2) · K3b − K2 +1,0 (t 0,94).
- **Yeni kurallar emülasyonu (E1, sim):** K4a 0,95 · K4c 0,83 · K3b 0,77 · K1bD2 0,71 · K2 0,61 mr.

## 4. Denenen ve elenen fikirler
| Fikir | Sonuç (sim, aksi yazmıyorsa) | Eleme nedeni |
|---|---|---|
| A1a/A1b en az kapıyla doldurma | 1,38 mr, MDD −47,7/−48,0 | 2008'de nakit koruyordu; yerine kademeli tamamlama |
| A2 2a kıyası XU100 · B1 momentum ufku | 2,11/2,14 · 2,20/2,22/2,53 | Kural 5 (top5 eksi); A2b + B1c sonra K1b'ye girdi |
| B2 risk ayarlı mom. · B3 FD/FAVÖK · B4 ivme çarpanı · B5 reel ROE | 2,18/2,46 · 2,55/1,91 · 2,33/2,41/2,21 · 1,54/2,62 | top5 −3 · H1 −1 · kriz, H1/H2 · Sharpe/kriz |
| B6 aşırı yükseliş · B7 BIST30 · B8 HA/MA75 gevşetme · B9 eşik küçültme | 2,05/2,24 · 1,86 (<5 ay: 98)/2,53 · 2,22/2,41/1,82 · 1,99/1,42 | sermaye · H1 −8 · H2 −14/−11 · sermaye |
| C1/C2 oynaklık/ATR tavanı · C3 7/10 hisse | 0,88/0,82 · 0,74/0,45 [evren belirsiz] | Sağlamlık (≥%70) yok · 5 hisse en iyisi |
| Ş1 TMS 29 düzeltmesi | site 2,030 | Kullanıcı itirazı + BISTTUM'da −80 puan |
| TÜFE çıtasını yükseltme (240 varyant) | f ile −%15…−%49 | Tek artı (×2) gürültü, plato yok |
| B0D3 (B0D2 − F/K) | site 2,098 | H1 −6; F/K etkisi yalnız K1b ile güçlü |
| Tur 2b: 47 ağırlık/eşik/MA | En iyisi C>MA150 4,10 | top5 −6, kriz; NetBorç/FAVÖK<3 3,53 eşik altı |
| Tur 2c: hacim, düşük oynaklık, rejimde momentum kısma, likidite | Hepsi taban altı | Zararlı |
| Tur 2c: 2–3 ayda bir dengeleme | −%60…95 | Sinyaller hızlı eskiyor |
| Tur 2c: C3 kötü rejimde teknik yok | 4,52, top5 −7 | İzleme; K4a'ya girdi |
| 2c-F net pay ihracı · 2c-G sektöre göreli | 3,63 (4 ay fark)/3,47/3,02 · 1,91–2,88 | Gürültü (F3 temettü etkisi) · hepsi zararlı |
| 2d öncelik puanı 0/25/50/100 · T6/T7/T9 | 1,76…3,55 · 3,50/2,11/2,78 | Kaldırmak −%48 · zararlı/gürültü; T8 sonra K4c'ye |
| K3a / K3b site | 3,576 (t 0,71) / 3,923 (t 0,94) | top5 eksi; K3b yedek |
| Platformda yapılamayan | — | Sektör momentumu, sektör başına sınır, tampon, endekse ilk giriş filtresi |

## 5. Yöntem
- **Terfi kuralı v2 (ON_KAYIT_ASAMA4 §3):**
  1. Sermaye ≥ şampiyon × 1,05.
  2. Kazandıran ay ≥ şampiyon − 0,5 puan.
  3. Sharpe ≥ şampiyon; kriz ayı ort. (XU100 < −%5) ≥ şampiyon.
  4. 2005–15, 2016–26 ve 2015+ ayrı ayrı olumlu.
  5. En iyi 5 ay çıkınca fark olumlu.
  6. Plato: komşu düzeyler aynı yönde (biri geçerse diğeri ≥ −%5).
  7. 5'ten az hisseli ay sayısı artmaz.
  8. Plasebo (200 tohum) %95 üstü.
  9. Deneme sayacı + final için DSR. Eşli t ≥ 1,5 beklenir; t < 1 "zayıf".

  Ek: simde geçemeyen siteye gitmez. Ön kayıt dışı keşif yalnız sitede, bütün maddelerle (top5 ve t ≥ 1,5 dahil) terfi eder. Izgarada çoğunluk yoksa "sivri tepe". Sağlamlık: sermayenin ≥ %70'i, Sharpe'ın ≥ %90'ı korunmalı.
- **Ön kayıt:** Aşama 4 (25), Tur 2b (47), 2c (11), 2c-F, 2c-G, 2d, K3b platosu. Deneme sayacı Aşama 5'te ≈ 298; K4'te "≈150 deneme", Bonferroni ≈ 3,4.
- **Sim–site kalibrasyonu:**
  - Hayalet düzeltmesi.
  - B0 sim ×19.286 / site ×18.015, 260/261 ay aynı.
  - Site/sim oranı: B0 0,933, Ş1 0,935, K1/K1b 0,90. K3b'de sim %16 iyimser. K4c 5,16 → 5,217, K4a 6,02 → 5,851.
  - Her site formülü önce editörde sim ile karşılaştırıldı (K4a/K4c 8/8).
- **İstatistik:**
  - Eşli aylık log fark: NW t, 12 aylık blok bootstrap.
  - H1/H2/2015+ ve top5 çıkınca fark.
  - Sharpe farkı bootstrap P(>0), plasebo, walk-forward (K3b), PSR/DSR.
  - E1 emülasyonu: 09/2026'daki 27 çıkıştan 23'ünü yakalıyor.

## 6. Açık işler
- **Adlandırma (deger_bist100/YENI_OTURUM_DEVAM.md):** 208422'den "Büyüme Stratejisi (BIST100) (2005-2026)" ve "(2015-2026)" modelleri açılacak; 2005-26 sonucu 208422 ile birebir olmalı. Kriter adı zaten 98322'de; yeni kopya gerekir mi [belirsiz]. 2015-26 döneminin sitede nerede ayarlandığı önce kontrol edilecek.
- **Aşama 6'nın kalanı (tarayıcı gerekli):**
  1. Büyüme+Ortak ve maliyet/kapasite.
  2. 1 gün gecikme.
  3. PBO/CSCV (IDB 'claude_c29').
  4. 1 Ekim listesiyle (27 giren / 27 çıkan) Ekim seçimleri.
  5. Gerçek yeni evren testi.
  6. Canlı ileri test planı.
  7. BISTTUM stratejileriyle korelasyon.
- **Aşama 7:** kopyala-yapıştır kriterler, site istatistikleri (2005–26 ve 2015–26), PDF rapor (iki strateji).
- **Silinecekler:** kullanıcı siler (liste ID dosyasında); 208419/98320 kararı kullanıcıda.
- **Riskler:**
  - K4'ün parçaları ön kayıt dışı → ileride fark küçülebilir.
  - Yeni evrende getiriler belirgin düşük (geçmiş seçimlerin %19–20'si dışlanacak hisseler).

## 7. Ömer'in istekleri ve kararları
- **Değişmezler:**
  - 5 hisse, eşit ağırlık, **nakit yok**, aylık.
  - Sitede yalnız "Farklı Kaydet"; en fazla 2 eşzamanlı test.
  - Silme yok: "silinecekleri listele, ben silerim". Şifre yok.
  - ETA ver, gereksiz sorgu yok. "Yeterli" denmeyecek.
- 29/09: "Aşama 6'ya kullanıcı onayı olmadan geçilmez."
- 22:00: "TMS 29 gerçekten hata mı; standart algoritma; 2024–26'da mevcut hal bizim için daha olumlu değil mi?" → K10 büyüme koşulları değişmedi.
- 22:14: "TÜFE çıtasını yükseltirsek ne olur — tek tek, çiftli, neredeyse tüm kombinasyonlar … (enflasyon düşünce çok hisse girecek)" → çıta değişmedi.
- 22:40: nakit yok, her ay 5 hisse; "önce teknik gevşet, yetmezse temel".
- 01:55: "Aşama 6'ya geçme, geliştirmeye devam".
- 05:05: sıradaki Değer BIST100 (aynı yöntem); Aşama 6 iki stratejiyle birlikte; E1 standart ölçüt.
- 05:33: "K4A şampiyon; sitede adını Büyüme Stratejisi (BIST100) yapıp tekrar test ederiz."
- Aşama 6+ onaylandı. Onaylı adlar "Büyüme Stratejisi (BIST100) (2005-2026)/(2015-2026)"; kriter adında dönem eki yok.

## 8. Araçlar ve dosyalar
**Python (scratchpad/b100/):**
- an.py — site serisini okur; standart metrikler (summ/fmt) ve eşli fark (NW t, blok bootstrap).
- cmp.py — aday ile şampiyonun site serilerini kıyaslar: Δ, t, H1/H2/2015+, top5, Sharpe farkı, PSR/DSR, yıllık fark.
- b0.py — B0, K10 ve XU100 özetleri; hisse sayısı dağılımı, boş aylar, eşli testler.
- kiyas.py — K4c/K4a site istatistiklerinden fark sütunlu HTML, oradan PNG üretir (ekran/K4c_K4a_karsilastirmali_istatistik.png).
- asama6.py — Aşama 6a/6b: K4a × DX3b korelasyon, 50/50, site istatistikleri, PSR/DSR, alt dönemler → asama6_out.json.

**Veri:**
- b0_site.txt, ser/ (b0d2, k2, k3a, k3b, k4a, k4c ve Değer serileri), k4a_siralama.txt/k4a_raw.txt, site_formulas.json.
- Bağımlılıklar: rapor/data.py, agirlik/sitestat.py.
- Sim motoru ve ham veri Chrome IDB 'claude_c29' içinde.

**Klasör:**
- DURUM.md, YOL_HARITASI.md, ON_KAYIT_ASAMA4.md, TUFE_CITASI_ANALIZI.md, LIT_A_buyuk_hisse.md, LIT_B_bist100.md.
- kriter/Buyume_Stratejisi_BIST100_kriter.txt: kopyala-yapıştır kriter ve model ayarları.
- ekran/: K4a_site_istatistik.jpg ve K4c_site_istatistik.jpg (site istatistikleri) · K4a_K4c_site_kiyaslama.jpg (sitede kıyas) · K4c_K4a_karsilastirmali_istatistik.png (kiyas.py çıktısı).

## Aşama 6–7 sonuçları (30/09, ikinci Cowork oturumu; ayrıntı deger_bist100/DURUM.md)
- Sitede yeni adlar: kriterler 98322 (Büyüme BIST100) / 98351 (Değer BIST100); modeller 208456/208458 ve 208461/208462. 2005-26 modelleri orijinallerle (208422, 208433) 261/261 ay birebir.
- Büyüme + Ortak (Ömer'in kuralı): 6,77 mr, yıllık %66,8, Sh 1,28, MDD −32,8, kaz %69,7; Büyüme'ye göre +0,7 puan/yıl (t 0,55); %50/%50: 4,70 mr, Sh 1,285, MDD −30,6, kaz %72,8.
- Maliyet (5 mn TL gerçekçi): B+O 5,1 / B+D 3,9 puan/yıl; kapasite ~50 mn TL. Bir gün gecikme: Büyüme +0,1, Değer −2,0 (t −1,53), B+O +0,5 puan/yıl.
- PBO/CSCV (site finalistleri): Büyüme %3,0 (13 varyant), Değer %6,2 (5 varyant). DSR (500; 0,30): Büyüme %95, Değer %89.
- Rapor: BIST100_Buyume_Deger_Yatirimi_Strateji_Raporu_2026-09.pdf (68 s.).
- Düzeltme (30/09 14:15): EFES ≠ AEFES (Şubat–Mart 2005) → Büyüme + Ortak 6,845 mr, yıllık %66,85, Büyüme'ye göre +0,72 puan/yıl (t 0,59). Değer + Ortak: 5,14 mr, yıllık %64,7, Sh 1,24. Rapor 100 s. (site formatı sayfaları + Ek G–K).
