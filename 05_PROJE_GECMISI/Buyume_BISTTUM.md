# DEVİR-TESLİM ÖZETİ — Büyüme Stratejisi (BISTTUM)
Kaynak klasör: `projeler/alfa_v41/` · Hazırlanma: 30/09/2026 · Tüm sayılar dosyalardan kopyalandı; emin olunamayan yer [belirsiz].
Kısaltmalar: mr = milyar TL, tr = trilyon TL (100 bin TL başlangıçtan) · kaz = kazandıran ay % · J = en iyi 5 olumlu ay çıkarılınca · t = eşli Newey-West t.

## 1. Kimlik
- **Strateji:** Büyüme Stratejisi (eski adlar: ALFA V4.1 Geniş Havuz → ALFA V5 Geniş Havuz; "Kârlılık + Momentum"). Kullanıcının tanımı: "büyüme + kârlılık + momentum".
- **Evren:** BIST TÜM = QueenStocks "Herşey Dahil" hisse kriteri (19006), ~700 hisse (editörde bugün işlem gören 696). İleride BIST100/50/30 sürümleri planlı.
- **Test:** 01/01/2005–25/09/2026 (261 ay), aylık, 5 hisse eşit ağırlık, nakit yok, TL, sıralama büyükten küçüğe, bilanço "Yayınlanma Tarihine Göre" (Aşama 1a; K10_kriterler.txt'de "dönemine/tarihine" diye muğlak yazılmış).
- **Amaç/öncelik:** istikrar + kazandırma oranı > sermaye (ŞAMPİYON KURALI v2); sonra K-Ratio.
- **Şampiyon: K10** — kriter **98258** "ALFA V5 (Geniş Havuz) K10" / model **208322** (model adı dosyada yok [belirsiz]; seri deseni "ALFA V5 (GENIŞ HAVUZ) K… (2005-2026)"). Raporda adı "Büyüme Stratejisi".
- **Formül ana hatları** (tam metin: `K10_kriterler.txt`; ayrıca PDF rapor Ek A):
  - Temel kapı (9, hepsi VE): a ROE>5 · b FAVÖKYıllık>0 ve NetBorç/FAVÖKYıllık<4 (M1) · d PD/DD<8 (ROE>90 ise 8+(ROE−90)×0,07) · h 2 ay getiri > XUTUM · j 1 ay > −15 · roeTeyit (ROE ≥ önceki çeyrek veya geçen yıl) · k HAOran<60 · bb balon vetosu (12 ay ≤%300 veya PD/DD≤8) · ucuz NetKarYıllık/PD ≥ 0,025 (F/K≤40).
  - Teknik: C>MA200, C>MA75, MA20>MA60.
  - Sıralama: SKOR = tam×1000 + karIvmesi. tam = ee (2h getiri > XUTUM 2h −10) ve f (satış büyümesi > Tufe(12)) ve (gx veya hx) ve efkTeyit. karIvmesi = 100 + 25×(pE+pF+pR+pI+pZ) + pen75 + mom6; p = x/(1+|x|); ölçekler EFK yıllık değişim 0,7 · FAVÖK 0,6 · ROE değişimi 2 puan · EFK büyüme ivmesi 10 puan · 52h zirve (C/HHV252−1)/0,0865; veri yoksa pE–pI −1, pZ 0; pen75 = −15 (C/MA75>1,35); mom6 = 8 × (Ref(C,−21)/Ref(C,−126)−1, ±1'de kesik).
- **Uygulama kararları:** 29/09 18:50 %50 K10 + %50 C32 (Değer: kriter 98194 / model 208224) ayrı portföy, aylık eşitleme. 30/09 raporda "Strateji sahibinin planı: Büyüme + Ortak" (K10'un 5 hissesi, C32'de de çıkan 2 pay).

## 2. Aşama aşama ilerleyiş
**Öncesi — gece, ön kayıtlı plan (28/09 23:50 – 29/09 06:50)**
- 23:50 Başlangıç: 95237/203135 (Temmuz, 145,5 mr). Kopya kuruldu; yeni site tabanı K0 208271 → 114,6 mr, kaz %67,82 (en kötü ay −%31,05, 09/2026). Formül denetimi (yıl içi kümülatif FAVÖK/EFK, NetBorç/FAVÖK mevsimselliği). 00:50 literatür + ön kayıtlı plan (Aşama 0-6).
- 01:45-04:15 M1-M3, S1, Aşama 2-4 (yapısal/veto/bonus), S5: kural v2'yi geçen yok. ee ablasyonu kopyada +%73,6 → K1 sitede −%4,4 → J kuralı eklendi. M9: ilk gün farkı +%0,17/ay → alım ay sonu kapanışta. BrutEFK/İFNA 2016 öncesi boş. Eylül 2026 çöküşü (KTLEV −%79, PRDGS −%48,9). 04:15 oturum düştü → borfin redirect.
- 04:50 S4 (havuz içi ±3σ z-skor) ZAYIF GEÇER (+%249, kaz +5,75, t 1,50) → K2. 05:55 kullanıcı M1'i benimsedi → K3. 06:08 kalan ön kayıtlılar elendi. 06:50 M7: TMS 29 sonrası büyüme kapılarında çift deflasyon; düzeltme getiriyi düşürdü → sert eşik korundu.

**Yeniden tasarım — ALFA V5 (29/09 07:00 – 14:30)**
- 07:05 "algoritmayla oynamak serbest": geniş havuz keşfi → sermayeyi KAPI yapıyor. 07:10 K3 129,4 mr → yeni taban. 08:00-08:15 havuz içinde fiyat momentumunun IC'si ≈0; "kâr ivmesi" sıralaması → K6.
- 08:55 K2 235,1 mr (+%105). 09:40 K6 123,3 mr (kopya 333,6). 09:55 kök neden: ZSkorPercentRank backtest'te kapı havuzu içinde ve bazı aylarda herkese 0 ("çöküş") → mutlak tavanlı puana geçiş.
- 11:08 K6A 289,3 mr (örtüşme %89,3); 11:25 şampiyon. 11:35-12:10 raw7, E/P, F/K, teknik set, V1 cezaları → K7, K8 (+F/K<40), K9/K10 (MA75 cezası −10/−15 + mom6 w8). Sim ~1,4-1,8× iyimser → "hüküm site".
- 13:06 K9 764,5 / K10 953,5 mr; 13:50-14:30 K11-K14 komşuluğu → K10 sivri tepe, beklenti ~650 mr.

**Yol haritası (onay 29/09 ~14:45)**
- A1 (15:20) kaçak: sızıntı yok, 1 gün geç ×1,110, DSR ≈%100, PBO %10, rastgele 300 portföyün %100'ünden iyi; K10−K6A t≈2,0. A2: volatilite iki kuyruğu da ayırıyor → veto işe yaramaz. A3 (~17:30): kaçan kazananların %82,0'ı kapıda; kapı esnetme iyileştirmiyor. A4 (~18:30): yeni adaylar ve rejim terfi etmedi. A5 (~16:10): LIT2. A6: yalnız K10+C32 ayrı portföy istikrarı artırdı. A7: FINAL_RAPOR; 18:50 %50/%50 kararı; yol haritası kapandı.

**Sonrası:** ~20:00 gerçekçi uygulama · 29-30/09 PDF rapor (DURUM'da 65 sayfa; güncel dosya 85 sayfa) · 23:30-23:55 eski ALFA aktarım taraması (29 deneme, hiçbiri geçmedi) · 30/09 ortak hisse çalışması + Büyüme + Ortak.

## 3. Site sonuçları (100 bin TL'den, 01/2005–25/09/2026)
| Model | Kriter / model | Son sermaye | Sharpe | MDD | Kaz % | Kriz | K-Ratio | 2015+ / not |
|---|---|---|---|---|---|---|---|---|
| **K10 (şampiyon)** | 98258 / 208322 | **953,5 mr** | 1,61 | −41,7 | 73,95 | [belirsiz] | 0,24 (0,243) | 2015-26: 11,31 mr, Sh 2,03, KR 0,529, MDD −18,9, kaz 78,7 |
| V4.1 başlangıç (Temmuz) | 95237 / 203135 | 145,52 mr | 1,32 | −42,9 | 68,48 | 78 | 0,27 | bitiş 07/2026 |
| K0 taban | 95237 / 208271 | 114,6 mr | 1,27 | −42,9 | 67,82 | 78,3 | — | 2015+ 1.124,8 mn |
| K1 ee yok | 98223 / 208275 | 109,5 mr | 1,27 | −42,9 | 68,58 | 75,5 | — | 2015+ 1.045,9 mn |
| K2 S4 z-skor | 98225 / 208286 | 235,1 mr | 1,38 | −42,6 | 71,26 | 121,6 | — | K0'a göre 2015+ +%85 |
| K3 M1 | 98226 / 208287 | 129,4 mr | 1,28 | −47,0 | 68,20 (K6A tablosunda 68,46) | 89,6 | 0,25 | K0'a göre 2015+ +%41,1 |
| K4 M1+S4 | 98227 / 208288 | 179,0 mr | — | −41,8 | 69,3 | — | — | |
| K6 | 98228 / 208289 | 123,3 mr | 1,29 | −44,2 | 70,50 | 186,9 | — | çöküş hatası; hatasız tahmin ~155,8 |
| K6A (eski şampiyon) | 98231 / 208292 | 289,3 mr | 1,45 | −40,3 | 73,18 | — | 0,25 | K3'e göre 2015+ 2,88× |
| K7 | 98247 / 208309 | 241,2 mr | — | — | 72,41 | — | — | |
| K8 | 98252 / 208310 | 410,9 mr | — | −41,7 | 73,18 | — | — | yarılar +22/+16, t 0,64, J −31 |
| K9 (pen −10) | 98257 / 208321 | 764,5 mr | — | — | 72,80 | — | — | K6A'ya +%164, t 1,60 |
| K11 (zirvesiz) | 98265 / 208326 | 474,6 mr | — | −40,7 | 73,95 | — | — | K6A'ya +%64 |
| K12 pen −20 / K13 w4 / K14 w12 | 98264/208325 · 98272/208337 · 98273/208338 | 634,0 / 592,3 / 646,8 mr | — | −41,7 | 73,95 / 73,18 / 73,18 | — | — | K10 komşuluğu |
| C32 Değer | 98194 / 208224 | 778,0 mr | 1,77 | −37,4 | 77,8 | — | 0,496 | 2015-26: 1,17 mr, Sh 1,82, KR 0,877, MDD −29,6 |
| %50/%50 | hesap | 1,114 tr | 1,87 | −36,3 | 77,4 | — | 0,339 | 2015-26: 4,30 mr, Sh 2,15, KR 0,754, MDD −13,8, kaz 80,9 |
| Büyüme + Ortak | hesap (site modeli yok) | 1,781 tr | 1,71 | −41,8 | 73,95 | — | 0,253 | 2015-26: 16,51 mr, yıllık %178,0, Sh 2,15, KR 0,57, MDD −18,93 |

K10 ek: Treynor 24,80 · Jensen 18,30 · Beta 0,80 · Ulcer oranı 0,74 · Std 12,22 · 193/68 ay · ort. kâr 11,71 / zarar −6,33 · yıllık bileşik %109,4. Yıllık %: 152 −2 8 23 110 101 8 69 18 182 106 30 200 58 134 381 118 617 284 101 199 120.

## 4. Büyüme + Değer birleşimleri
- **%50/%50 (K10+C32, ayrı portföy, aylık eşitleme):** korelasyon 0,62-0,63; 1,114 tr, Sh 1,87, KR 0,339, MDD −36,3, kaz 77,4; 22/22 yıl pozitif ve BIST100 üstü. Karışım: sermaye tepesi %60 K10 (1,125 tr), Sharpe tepesi %30-40 (1,88); K-Ratio Değer payıyla artar. Tek modelde birleştirme (B1-B4, karma) −%14…−%98 → önerilmez.
- **Ortak hisse 2 pay vs tekil eşit bölme:** 1,114 tr vs 755,2 mr (1,48×), yıllık %110,9 vs %107,1, Sharpe 1,86/1,79, MDD −36,3/−38,1. 161 ayda ortak hisse var; ortak hisseler ayda +2,01 puan fazla. t 1,89, bootstrap %95,8, 16/6 yıl önde; en iyi 10 ay çıkınca ≈0. Çarpan 1→2→3→4: 755→1.069→1.353→1.604 mr. "10 pay" kuralı 1,069 tr vs 50/50 kuralı 1,114 tr (t 0,98). Öneri: 2 pay koru; 3-4 pay önerilmedi (yoğunlaşma %27-33).
- **Büyüme + Ortak** (K10'un 5 hissesi; C32'de de çıkan 2 pay; 1 ortakta %33,3/%16,7): 1,781 tr, yıllık %115,5, Sh 1,71, MDD −41,8, en kötü 12 ay −%20,0. K10'a göre +2,9 log puan/yıl (t 2,20, bootstrap %99, yarılar +2,4/+3,3, J +1,4) — "en güçlü tekil bulgu". %50/%50'ye göre tüm dönemde anlamsız (t 0,58; 2005-15'te 50/50 +6,8, 2016-26'da B+O +11,3 puan/yıl); 2015-26 +11,4 puan, t 2,17. Değer + Ortak 1,040 tr (t 1,01). B+O, Büyüme ile %99 korele.
- **Gerçekçi uygulama (komisyon 0, 5 mn TL):** %50/%50 yıllık %93,2 TL (reel %63,4, $ %64,3, Sh 1,61, MDD −38,8, 166 mr; maliyet %8,4). B+O %91,0 (reel %61,5, Sh 1,40, MDD −43,3, 128,8 mr; maliyet %11,6 = makas 4,4 + fiyat etkisi 6,7 + tavan/taban 0,5; devir %124). Kapasite B+O / B+D yıllık: 1 mn 98,4 / 97,8 · 5 mn 91,0 / 93,2 · 10 mn 85,5 / 89,8 · 25 mn 75,1 / 83,1 · 100 mn 48,7 / 66,0 · 250 mn 21,4 / 47,6. Devir K10 1,214, C32 0,992, birleşik 1,055. 1 gün gecikme: K10 +0,6, C32 −5,7, birleşik −2,5 puan; B+O etkilenmiyor (%115,5→%116,2). Öneri: ~5 mn'de yeniden karşılaştır, ~10 mn üstünde %50/%50 veya karışım.
- **Planlama beklentisi:** reel yıllık %25-45 (ortası ~%35).

## 5. Denenen ve elenen fikirler
| Fikir | Sonuç | Eleme nedeni |
|---|---|---|
| M1 kaldıraç yıllık FAVÖK | kopya +%23,9; site K3 +%12,9 | Kural v2'yi geçmedi ama kullanıcı benimsedi (K10'da var) |
| M2, M3, M4, M5, M6, M8a/b | −%3,1 / −%5,8 / +%7,0 / +%2,7 / −%3,2 / 0 / −%13,3 | Etkisiz; t ≈0 |
| M7a/M7b TMS 29 eşik | −%42,4 / −%46,9 | Doğru düzeltme ama getiri düşüyor; sert eşik korundu |
| S1a/S1b k-of-n kapı | −%97,5 / −%98,5 | Felaket |
| ee (2h göreli) kaldır = K1 | kopya +%73,6; site −%4,4 | Sitede tutmadı |
| S2a/S2b değer ağırlığı, S3 sade sıralama, S5 V1 sıralaması | −%38,1 / −%21,3 / −%50,7 / −%74,2 | Sermaye ve 2. yarı düşüyor |
| S4 z-skor (K2), K4, K6 | site +%105 / 179,0 / 123,3 mr | K6A/K10 aştı; K6'da yüzdelik hatası |
| B1a 52h zirve kapısı, B1b puan | −%34,1 / +%8,6 | B1b 16-26 −%11,7, t 0,06 |
| B2, B3a/b, B4, B5 | −%11,3 / +%15,3 / −%24,0 / +%23,7 / −%7,0 | t şans düzeyi, J negatif |
| A1 devir×momentum, A2 tahakkuk, A3 aşırı kazanan | −%2,8…−%90,8 | Havuzu boşaltıyor / kazananları kesiyor |
| A4 tavan kilidi, A5 ihraç, A6 MAX, A7 HA<15, A8 | kopya +%35 / +%11,5 / +%21,5 / +%68 / −%40,2 | SA veya 2016-26 negatif; A6a izlemede |
| B7 rejim, B8 düşük oynaklık, B9 hacim şoku, B11 mevsimsellik | −%19,6 / −%49,0 / −%30,7 / −%38,0 | B8 kaz +3,45 ama sermaye yarı |
| Katı PD/DD (istisna kaldır) | +%34,4, t 1,4 | 9 örnek; kanıt değil (V1 +%15 tekrar) |
| Geniş havuz tasarımları (W, G/P/M, Wmin, D4; kademeli T1-T6, C1-C3) | 0,4-21,8 mr (taban 110,6); T −%18…−%60; C1 +%60,9 | Kapıyı gevşetmek sermayeyi düşürüyor; C1 t 0,50, J −%50 |
| D1 SUE, D2 ROE, D3 E/P, D5 volatilite | −%27 / −%41 / +%26 / +%9 | Sharpe düşüyor / şans; D4+V3 → K7 |
| V2 MAX veto, V4 3 ay veto, D6 2h cezası | +%5 / −%83 / −%43 | Son 10 yıl negatif; kazananları kesiyor |
| E/P puan biçimleri; ek kapılar (SUE>0, ROE>10/15, oynaklık, 52h<%75, PD/DD>5, HA<20) | −%94…+%18; SUE>0 +%16 | Kural v2'ye yakın değil; SUE>0 izlemede |
| Teknik set T1-T11 (Minervini, CAN SLIM, RSI, VCP, MA) | −%99…+%13 | Havuzu daraltıyor; RS puanı ve çeyrek kâr ≥%25 izlemede |
| V1 tarzı elemeler (MA75>%40 veto, V1 paketi) | −%77 / −%59 | Elemek zararlı, hafif ceza yararlı (→K9/K10) |
| Aşama 2-3: volatilite vetosu, kapı esnetme, öncelik çıkarma | −%2…−%98 | Kapı tasarımı doğrulandı |
| Aşama 4: FIP, oynaklık-mom, DSRI, stok, HA değişimi, bayatlık, lowr, sueA; rejim | −%16…−%94 (sueA<0 +%9); rejim +%37 / komşu −%40 | K10'u geçmedi; rejim sivri tepe |
| Hisse sayısı 6-10; tek-model birleşim | −%65…−%96; −%14…−%98 | Getiri düşüyor, istikrar kazancı sınırlı |
| O1-O12 (ceza modülleri, PD/DD kademe, FAVÖK ivme vb.), G1/G1b/G2/G3/G4 | −%93…+%15 (G1b +%15, t 0,72) | 29 denemenin hiçbiri terfi kuralını geçmedi |
| Ortak hisse 3-4 pay | 1.353 / 1.604 mr | Geçmişe bakılarak bulundu; yoğunlaşma |

## 6. Yöntem
- **Şampiyon kuralı v2:** sermaye ≥ +%5, kaz ≥ −0,5, Sharpe ≥, kriz ≥; iki yarı (2005-15, 2016-26) ve 2015+ > 0; temiz modda (1 gün geç) > 0; plasebo %95 üstü veya t_NW ≥ 1,5 (t ≥ 2 GÜÇLÜ, değilse ZAYIF). ALFA eki: 5'ten az hisseli ay en fazla +6. 03:10'da J eki. Çoklu test: tekil terfi için t ≈ 3.
- **Sim → site:** simde olumlu ayrışmayan siteye gitmez; en fazla 2 eşzamanlı site testi; yalnız "Farklı Kaydet". Kopya sadakati: K6A'da hisse örtüşmesi %89,3; hayalet hisseler site seçimlerinin ~%5'i; editörden alınamıyor. Sonuç: sim ~1,4-1,8× iyimser, hüküm site.
- **Platform bulguları:** ZSkorPercentRank = PERCENTRANK.INC (kesilmiş), backtest'te kapı havuzu içinde, çöküş hatası; Stats.Average/StdDeviation etkilenmiyor; `null−1` = −1; değişken adı "fk" platform F/K ile çakışıyor; Farklı Kaydet için lstHisse'de ≥1 hisse seçili olmalı.
- **İstatistik:** t_NW, J, plasebo, havuz sarsma, işaret testi, bölünmüş örneklem, CSCV/PBO, DSR, blok bootstrap, IC, komşuluk haritası.
- **Maliyet modeli:** yarım makas (Abdi-Ranaldo) × hsMul + k×σ×√(emir/ADV) + tavan/taban kilidi + temettü stopajı; sermaye TÜFE ile o tarihe çevrildi; senaryolar iyimser (k 0,3) / gerçekçi (0,6) / kötümser (1,0 + 1,5× makas + 1 gün geç). Maliyet 0'da site birebir.

## 7. Açık işler / bekleyenler
- Büyüme + Ortak mı %50/%50 mi: planlanan B+O; portföy ~5 mn TL'ye yaklaşınca maliyet karşılaştırması yeniden; ~10 mn üstünde %50/%50 veya karışım.
- İsteğe bağlı ön kayıtlı testler (öneri): ortak hisse 3-4 pay; bilinçli K10 payı (ör. 60/40). Kullanıcının istemediği: nakit/rejim filtresi, sektör sınırı.
- Denenmemiş literatür fikirleri: tampon (F6), trend kalitesi (F7), koşullu düşük oynaklık (F4), açıklama öncesi yükseliş, geç raporlayan vetosu.
- İzleme: esnek PD/DD istisnasıyla giren hisseler; A6a MAX üst %5; SUE>0; RS puanı; çeyrek kâr ≥%25; Değer'in 2025-26 yavaşlaması.
- Doğrulanmamış: getirilere temettü dahil mi; gün içi fiyatla tarama mümkün mü; "Büyüme + Ortak Pay Hesabı" aracının yeri [belirsiz]. Planlı: BIST100/50/30 sürümleri.

## 8. Ömer'in bu projeye özel istekleri, kuralları, kararları
- "önce geniş havuz; konu sende, planı biliyorsun" (28/09 23:50). Öncelik: istikrar + kazandırma oranı.
- "Ben uyuyorum; sabaha kadar simülasyon ve gerekli testleri yap, kuralları biliyorsun; gerekirse internetten veri al; otomasyona bağla, kontrol ede ede git." (00:45)
- "M1 doğrusunu yapalım esnek PD/DD kalsın." (05:55)
- "Algoritmayla oynamak serbest. Havuzu tıpkı değer yatırımındaki gibi geniş tutup 5'ten az hisse bulunan ay sayısını azaltıp ilerleyebiliriz… Sonuçta baştan yaratacağız. Unutma bu strateji büyüme stratejisi: büyüme + kârlılık + momentum." (07:00)
- ALFA V1.4 sıralamasını önerdi (07:40). "simülasyon %90 tutmalı, önce bunu çöz" (09:55). K6A şampiyon, "Geliştirmeye devam, durmak yok." (11:25). Teknik metrikler (Minervini, CAN SLIM, MA) sıralamada ve kapıda, çok kombinasyonlu (11:40).
- "E/P'yi neden eledin, K7 ile farklı biçimlerde dene", "hepsini hem sıralamada hem kapıda deniyor musun?" (11:50). V1'deki MA75 cezası, 2/6 ay momentum puanı (12:10).
- Yol haritasını onayladı; Aşama 3 (kaçan kazananlar) onun önerisi. Onaysız izin yalnız K10+C32 birleşik; hisse sayısı, nakit/rejim, sektör sınırı sorulacak.
- Tek algoritmada birleştirme ve 5→10 hisse testlerini istedi (sim; önerilmedi). 18:50: %50/%50; nakit/rejim ve sektör sınırı testlerini istemedi.
- Gerçekçi uygulama: komisyon 0, 1-10 mn TL. İsimler: K10 = Büyüme Stratejisi, C32 = Değer Yatırımı Stratejisi, %50/%50 = Büyüme + Değer Yatırımı Stratejisi; dosya adı BISTTUM. Eski ALFA aktarım taraması istedi (23:30). 30/09 plan: Büyüme + Ortak.
- Değişmez kurallar: baz kriter/modelin üzerine asla kaydetme (yalnız Farklı Kaydet); en fazla 2 site testi; şifre girilmez; kalıcı silme yok; 5 hisse / nakit yok; evren değişikliği onaysız yok; önce sim sonra site; elenenler gerekçesiyle raporlanır; kontrol ETA ile, gereksiz sorgu yok; aşama sonu kısa rapor + DURUM.md. Oturum düşerse borfin.com/tr/programs/153/redirect. Türkçe, abartısız beklenti.

## 9. Klasördeki dosyalar
- `DURUM.md` ana günlük (28/09 23:50 → 29/09 23:55) · `YOL_HARITASI.md` Aşama 1-7 planı ve değişmez kurallar · `FINAL_RAPOR.md` sonuç + karışım tablosu + %50/%50 kararı · `GERCEKCI_UYGULAMA.md` maliyet/kapasite/gecikme ve uygulama kuralları.
- `LITERATUR.md` — 1. literatür taraması (4 ajan), ~30 aday, ön kayıtlı test planı, sonuç eki.
- `LIT2_A_istikrar.md` / `LIT2_B_kaybeden.md` — 2. tur literatür (istikrar F1-F7; kaybeden vetoları). `BRIEF_literatur*.md` — ajan brifleri.
- `K10_kriterler.txt` — şampiyon tam formül + model ayarları · `K5_siralama_formulu.txt` — K5 taslağı (S4 + zayıf halka dolgu; tam site testi yapılmadı).
- `K6_formuller.txt` — K6 tam formül · `K6A_siralama.txt` — K6A sıralaması · `site_*_95237.txt` — kullanıcının orijinal V4.1 kriteri 95237 (temel/sıralama/teknik) · `site_temel_K5_M1_M7a.txt` — M1 + M7a temel taslağı.
- `BISTTUM_Buyume_Deger_Yatirimi_Strateji_Raporu_2026-09.pdf` — kapsamlı rapor (Büyüme + Ortak dahil).
- `Buyume_Deger_Ortak_Hisse_Agirlik_Calismasi.pdf` — ortak hisse ağırlığı çalışması (11 sayfa).
- `Buyume_Deger_Ortak_Hisse_Aylik_Detay.xlsx` — 261 ay hisse/ağırlık detayı (Özet, Aylık, HisseAy).
- `Buyume_ortak_site_istatistik_2005-2026.png` / `_2015-2026.png` — B+O site formatında istatistik sayfaları.
- `ekran/`: `Birlesik_K10_C32_2005-2026` / `_2015-2026` (.png/.html) %50/%50 istatistik sayfaları · `K10_site_istatistik.jpg`, `K10_site_yillik_aylik.jpg`, `K10_portfoy_istatistik_tam.png/.html` K10 site istatistikleri · `K6A_site_istatistik.png` · `C32_2015-2026_istatistik.png`, `C32_2015-2026_yillik_aylik.jpg` (C32 2015-26; hangi model [belirsiz]) · `Gercekci_Uygulama_K10_C32.png`.
