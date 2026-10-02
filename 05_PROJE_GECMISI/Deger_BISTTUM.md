# DEVİR ÖZETİ — Değer Yatırımı Stratejisi (BIST TÜM) — şampiyon C32
Kaynak: projeler/deger_v11/ (DURUM.md son kayıt 29/09 00:30; PROTOKOL.md; LITERATUR.md). Rakamlar dosyalardan aynen alındı; emin olunmayan yerler [belirsiz].

## 1. Kimlik
- **Strateji:** Değer Yatırımı V1.1 (2005-2026) → varyantlar "V1.1-Txx" / "V1.2-Cxx". Piotroski F-Skor ≥7 + momentum kapısı + halka açıklık <%60 havuzundan **en düşük FD/FAVÖK'lü 5 hisse**. Site: QueenStocks.
- **Evren / ayar:** Hisse Kriteri "Herşey Dahil" (BIST TÜM), 5 hisse eşit ağırlık, TL, Yayınlanma Tarihine Göre, 01/01/2005–25/09/2026, aylık yenileme, nakitte tutma YOK (model her ay hisse alır).
- **Amaç (PROTOKOL §0):** değer felsefesine sadık kalarak dönem sonu sermaye → kazandırma % → Sharpe → K-Ratio; kriz yılı savunmasını bozmadan. 28/09 sabahtan itibaren kullanıcı önceliği: **kazandırma % ≈ Sharpe/K > kriz koruması > sermaye.**
- **Şampiyon: C32** — kriter **98194** "Değer Yatırımı V1.2-C32 (C29 + nakit akış verimi bonus4 + PDDD<8)" / model **208224** (C29 modeli 208181'den Farklı Kaydet; model adı dosyada yazılı değil [belirsiz]). Kullanıcı kararı 28/09 ~20:20. Soy: BAZ → T12 → T13 → C03 → C07 → C15 → C17 → C29 → C32.
- **Orijinal (dokunulmaz):** BAZ kriter 94555 / model 208000 (PROTOKOL kural 1: asla değiştirilmez, yalnız "Farklı Kaydet").

**C32 formülünün ana hatları** (temel editörde tüm koşullar SON `;` satırında and ile birleşir):
- Temel kapılar: (1) F-Skor ≥7 (9 madde; s2/s4'te OCF vekili = `FAVOKYillik() − ΔNetİşletmeSermayesi` — C17'den beri yıllık) ve `FDFAVOK() > 0` · (2) mg: 12-1 ay getirisi > XU100'ün 12-1'i (mutlak m12 şartı C03'te kaldırıldı) · (3) `HAOran() < 60` · (4) qok: `FAVOK()/FAVOKYillik() > 0.22 || NetSatisBuyumeYillik() > 50` · (5) fkok: `FK()` null (zarar) veya < 40 · (6) teknik "3'te 2": t6 = 6 ay getiri ≥0 (null geçer), tdp = `C/LLV(C,250)` ≥1,5, tzr = `C/HHV(C,250)` ≥0,70; `t6+tdp+tzr >= 2` · (7) pdok: `PDDD()` null veya < 8.
- Teknik kriter: `Mov(C,20) > Mov(C,75)`.
- Sıralama: SkorA = fdfavokSkor×0,73 + trendSkor×0,22 + nakitBonus×0,72 + pdddBonus×0,72 + superKalite×0,72 + (s2=1 ise 5)×0,72; **Skor = SkorA + 4×(cfpe − 0,5)**, cfpe = 1/PDNakitAkis'in havuz yüzdelik eğrisi (ECDF, 7 düğüm). fdfavokSkor: FD/FAVÖK ≤0,5→100, ≥15→0, arası (1−log(FD/FAVÖK)/log15)×100; trendSkor = (Kapanış−Mov75)/Mov75 %, 0–30 kırpık; nakitBonus ocfRasyo >0,15:5 / >0,08:3 / >0:1; pdddBonus PD/DD <1,5:5, <3:3; superKalite F≥9 & ocfRasyo>0,15 & PD/DD<2 → 15. Sıralamadaki F-Skor/OCF ÇEYREK `FAVOK()` ile kalır (C19 dersi).
- **Tam metin:** klasörde tek parça hâlinde YOK. Baz metin PROTOKOL.md §3; değişiklikler DURUM.md durum tablosu (C03, C07, C15, C16/C17 satırları), 28/09 11:25 C29 formül satırı ve 18:25 "SİTE" paragrafı (C32). ECDF düğüm değerleri klasörde yok [belirsiz — sitede kriter 98194 / tarayıcı IDB].

## 2. Aşama aşama ilerleyiş
1. **27/09 13:01 devir** (BAZ 215,6 Mr). **T1–T11 tekli testler (13:10–19:10):** T1 ROA, T2 momentum, T4 F≥8, T5 saf FD/FAVÖK, T6 F≥6, T7–T11 RED; T3 yıllık OCF SINIRDA/BEKLET. Dersler: FD/FAVÖK sırasını seyrelten her puan zararlı; F7, HA60, Mov20/75 "keskin tepe" (aşırı uyum riski).
2. **Sim veri seti DS1 (14:25–19:05, 261 ay):** 36 ayda %96 eşleşme; 90 filtre taramasında iki yarıda pozitif 7 filtre (q>0,29, tahakkuk, pd…).
3. **Ölçüm hijyeni — q filtresi:** 19:10 T12 (q>0,29) KABUL 349,3 Mr (+%62); 20:26 plato → T13 (q>0,22) 355,0 Mr şampiyon, T14 (0,40) çöküş.
4. **C03 (m12 kaldır):** SINIRDA → **kullanıcı 21:50 "C03 yeni baz"** (392,4 Mr). C04 RED; T15/T16 teknik plato RED (23:11).
5. **F/K (DS2 taraması):** C05/C06 FAVÖK YoY RED (28/09 00:30). **C07 F/K<40 KABUL 01:50** (487,6 Mr); plato C09/C10/C11 → 05:52 C07 kalıcı. DS3 → C12 (NÖTR); VEYA taraması → C13/C14/C15 RED (04:30, tek yıl bağımlılığı). C08 bilgi.
6. **Kullanıcı "C15 kabul" (28/09 sabah)** → baz C15 (592,9 Mr). Öncelik değişti (%77 kazandırma). C16 SINIRDA (07:13) → **C17 şampiyon 08:30/08:35** (429,2 Mr, Kaz %77,39; İSTİKRAR HATTI; C15 getiri hattı referansı). C18 geride; C19 RED, C20 NÖTR (10:05); C21 RED, C22 NÖTR (11:28). DS5 olay, DS6 kalibrasyon, DS7 → C23/C24 gerçek CFO site testi ERTELENDİ (11:15, sim −%45).
7. **Kaçak analizi v1 (~10:40, K1–K7)** ve **teknik taraf (~11:05):** teknik kapı yoksa −%93; guru stratejileri kötü; 266 koşul × VE/VEYA taraması → "düşen bıçak" teması → C27 → 3 koşulun tüm birleşimleri → **C29 (3'te 2) 12:49 ŞAMPİYON** (520,3B, +%21); C28 (kullanıcı isteği) RED.
8. **Sim altyapısının yeniden kurulumu (~13:45–17:35):** C30/C31 sitede RED → eski sim YÖN'de de yanılmış. Kök nedenler: G1 binlik virgül ayrıştırma, G2 yanlış getiri penceresi, G4'/G5 hayatta kalma (bugünkü hisse listesi). Çözüm: kacak_worker.js ile 3 sekmede evrensel veri + "hayalet" hisseli **hibrit kopya** → 261 ayda C29 232/261 birebir (%88,9), sermaye 501,1B (site 520,3B). **T99 ölçüm testi (15:35–17:10): İLERİYİ GÖRME YOK**; site önceki ay sonu kapanışıyla seçiyor. Temiz mod (1 gün geç alım): C29 −%55. **Kullanıcı kararı 16:10:** her aday önce simde; olumlu değilse site hakkı yok.
9. **Kaçak kataloğu v2 + bayraklar (17:40–17:51):** hiçbir düzeltme kural v2'yi geçmedi; "negatif FAVÖK/FD" tipi kaçaklar seçimlere hiç ulaşmıyor. Kaçak denetimi kapandı. Minervini tam şablon (17:47) anlamlı zararlı.
10. **Literatür turu (LITERATUR.md; ön kayıt 17:55):** havuz IC taraması (18:15) çoğu sinyal güçlü; ama uygulama simünde 115 varyantın 105'i C29'u kötüleştirdi (18:20). Değer ailesi sağlamlık (18:25) → **C32 adayı (CFP ECDF w4 + PD/DD<8): sim +%48,8, t(NW) 1,57, ZAYIF.** Site testi 18:33 başladı.
11. **C32 site sonucu (20:25):** 777.959.361.011 (+%49,5; sim tahmini +%48,8) → **kullanıcı: "C32 yeni şampiyon."** C33 (w5, PD/DD yok) 22:30 sonucu elendi. C34 beklemede.
12. **C32 üzerine araştırmalar (19:20–29/09 00:30), hepsi elendi:** Değer ailesi 2.0 (bileşim, F/NS, sektöre göreli, EBITY) · 15 aile derin analizi (elenenler_derin_analiz.xlsx) · yapısal testler (tampon, sıra ağırlığı) · FD/FAVÖK "aşırı ucuz" düzeltmesi (H1 sıfır değişiklik; veto 0,75 ZAYIF, benimseme önerilmedi) · sıralama ağırlıkları (yerel optimum) · 13 puanlama yöntemi · K+M kaynaklı P adayları · 2 haftada bir yenileme (−%53). 21:25 ablasyon kullanıcıca iptal.
13. **28/09 23:35 KULLANICI KARARI: değer yatırımı BEKLEMEDE** — "strateji strateji ilerleyelim"; önce K+M (kârlılık+momentum) DAR havuz. Deneme sayacı ~470 (bu faz); proje boyunca sıralama/filtre denemesi ≈ 5.800.

## 3. Site sonuçları — şampiyon ve önemli alternatifler
Kriz Σ = kriz yılları (2008, 2011, 2013, 2015, 2018) getiri toplamı; dosyada "kriz ayı ortalaması" diye bir ölçü yok. "—" = dosyada yok.

| Sürüm (model) | Dönem sonu | Sharpe | K | MDD | Kaz. % | Kriz Σ | CAGR 05-15 / 16-26 | 2015+ |
|---|---|---|---|---|---|---|---|---|
| BAZ (208000) | 215.610.976.077 | 1,53 | 0,38 | — | %72,41 | 171 | 76,9 / 112,9 | — |
| T13 (208086) | 354.951.769.323 | 1,58 | 0,40 | — | %71,65 | 178 | 83,3 / 115,0 | — |
| C03 (208098) | 392.383.340.440 | 1,63 | 0,45 | — | %73,18 | 182 | 87,6 / 111,9 | — |
| C07 (208125) | 487.612.424.467 | 1,63 | 0,45 | — | %72,80 | 182 | 88,7 / 114,9 | — |
| C15 (208148) getiri hattı | 592.903.396.088 | 1,67 | 0,47 | — | %73,95 | 183 | 90,7 / 116,5 | — |
| C16 (208168) | 431,7 Mr | 1,68 | 0,46 | — | %77,01 | 207 | 83,5 / 118,6 | — |
| C17 (208169) istikrar hattı | 429.172.760.150 | 1,70 | 0,49 | — | %77,39 | 205 | 84,6 / 117,1 | — |
| C20 (208175) | 407,1 Mr | 1,69 | 0,49 | — | %76,63 | 208 | 84,6 / 116,1 | — |
| C28 (208182) | 510,3B | 1,70 | 0,44 | — | %76,25 | 221 | 84,1 / 121,2 | — |
| C29 (208181) | 520.305.126.289 | 1,72 | 0,45 | −%36,3 | %77,01 (201/261) | 219,4 | 84,3 / 121,3 | kaz %75,89 · Sh 1,783 |
| C30 (208185) | 422,0B | 1,71 | 0,43 | — | %77,39 | — | — | — |
| C31 (208186) | 432,4B | 1,72 | 0,43 | — | %77,01 | — | — | — |
| C33 (208236) | 654,1 milyar | 1,73 | 0,48 | −%36,3 | %76,25 (199) | 231,6 | — | C29'a göre sermaye +%4,9 |
| **C32 (208224) ŞAMPİYON** | **777.959.361.011** | **1,76** | **0,50** | −%37,4 | **%77,78 (203/261)** | **243,8** | — (C29'a göre sermaye +%32,1 / +%13,2) | kaz %77,30 · Sh 1,793 · sermaye C29'a göre +%11,8 |

C32 ek: Jensen 17,50, Ulcer 1,07, Beta 0,81; C29'a eşli fark +0,169 puan/ay, t(NW) 1,62; en iyi 5 ay farkın %92'si; yıllar 11 iyi / 9 kötü / 2 eşit; 2023–2026'da C29'un biraz gerisinde. Sim bağımsız doğrulama (Python): C32 745,7B vs C29 kopya 501,1B, blok bootstrap p 0,086, Holm p 0,35 → "istatistiksel olarak ANLAMLI DEĞİL".

## 4. Denenen ve elenen fikirler
| Fikir | Sonuç | Eleme nedeni |
|---|---|---|
| T1 ROA sırası ×0,30 / T2 12-1 momentum ×0,20 | 20,9 / 30,7 Mr | sıralamayı seyreltiyor; iki yarıda −20 CAGR / DNbeat 78→68 |
| T3 yıllık OCF (baz), C16 (C07 üzerinde) | 176,4 / 431,7 Mr | sermaye −%18 / −%11; C15 üzerinde C17 olarak benimsendi |
| T4 F≥8, T6 F≥6 | 0,58 / 35,6 Mr | havuz çöküşü; F7 keskin tepe |
| T5 saf FD/FAVÖK | 79,0 Mr | trend+bonuslar değer katıyor |
| T7 NetBorç/FAVÖK<3, T8 Mov200, T9 PD/DD>0,5, T10 son ay puanı | 171,9 / 166,8 / 205,8 / 203,7 Mr | şart 1–2 sağlanmadı |
| T11 / C04 tahakkuk<0,19 | 201,7 / 328,4 Mr | kayıp; literatürde ABD dışı zayıf |
| T14 q>0,40 | 42,1 Mr | uçurum |
| T15/T16 teknik Mov10/50, 50/150 | 38,9 / 23,4 Mr | Mov20/75 keskin tepe |
| C05/C06 FAVÖK YoY (nominal/reel) | 127,7 / 94,5 Mr | büyüme şartı ucuz toparlanma adaylarını eliyor |
| C09/C10/C11 F/K 50/35/45 | 394,8 / 416,2 / 441,5 Mr | plato, tepe 40 (C07) |
| C08 PD/NakitAkış<35 | 429,6 Mr | F/K'nın zayıf versiyonu |
| C12 NetKâr≤3,5×FAVÖK | 490,9 Mr | +%0,7 nötr |
| C13/C14 q VEYA satış büyümesi | 538,6 / 548,3 Mr | kural 6: kazanç 2026 tek yıl (ATATP) |
| C18 yalnız s4 yıllık / C19 sıralamada yıllık OCF | 387,3 / 254,2 Mr | C17 gerisinde / −%41 (F-Skor kapıda yıllık, sıralamada çeyrek) |
| C20 Fskor VEYA FskorY / C22 F/K<45 | 407,1 / 426,5 Mr | ek değer yok (nötr) |
| C21 q filtresini kaldır | 346,3 Mr | −%19; q hâlâ değerli |
| C23/C24 gerçek CFO hibrit | sim x3,81 (−%45) | site testi ertelendi |
| C28 (6ay VEYA dip) VE zirve≥%70 | 510,3B | kazandırma −1,14 |
| C30/C31 6 ay eşiği 5/7 | 422,0 / 432,4B | −%19 / −%17 (eski sim yanıldı) |
| C33 NA verimi w5, PD/DD kapısı yok | 654,1 milyar | kazandırma −2 ay, t 1,04; C32 her ölçüde iyi |
| Kapı gevşetme (mg, HA, tek, F6), bayrak cezaları, sıra-1 tuzak kuralı, tutma bonusu, sektör başına 1 hisse | sim negatif | her koşul değerli; plato yok |
| DS2–DS4 metrikleri (RSI, CCI, beta, hacim, FD/Satış, sektör göreli, ÖzKar, marj, nakit dönüşümü, faiz karşılama, döviz, temettü, net-net, varlık büyümesi, 60g zirve, MACD) | iki yarıda pozitif eşik yok | çoklu test ≈5.400; gürültü |
| DS5 olay: pay artışı (serg<1,2) / son 12 ay bedelli eleme | −0,89/−0,80 · −0,51/+0,07 (log, iki yarı) | Türkiye'de sermaye artışı çoğu bedelsiz (olumlu) |
| Rejim anahtarı (TÜFE yüksekken aşırı ısınmışı ele) | C17'de 16-26 −1,5…−2,3 | C03'teki bulgu tersine döndü |
| Guru: Weinstein, 52h zirve ≥0,9, trending value, RSI | −%44…−%95 | sim |
| Minervini tam şablon (8/8, 7/8, 6/8, RS≥70/50) | −%10,2…−%97,2, t≈−3 | değer, momentumu tamamlanmışta en kötü |
| Kaçak v2: HA<15, sermaye +%20, net nakit, FK null, CFO<0, stok yok | −%14…−%96,8 | "kaçak" sanılanlar getiri kaynağı |
| HA<50 / holding hariç / holding+petrol+bina hariç | +%62,4 / +%41,1 / +%34,9 | kriz, kazandırma, 2005-15 şartları; evren değişikliği |
| Literatür sinyalleri (MAX, TAIL, SD, SUE, ACC, GPA, ISS, TURN, zarar geçmişi, REC, ID, RMOM, MAD, VCP, yaş, mevsimsellik) | 115 varyantın 105'i kötü | havuz IC ≠ 5 hisse portföy (düşük risk −%17…−%87, SUE bonus −%56…−%79) |
| ACC (kazanç ivmesi) veto %10 | +%62,1 | kazandırma −4 ay; tek tepe (komşular negatif) |
| FD/FAVÖK<1 / <0,75 vetosu | +%11,5 (C29) / +%20,7 (C32) | Sharpe/kriz; tek tepe, TRENJ/TRMET yığılması (ZAYIF) |
| Değer ailesi 2.0 C32 üzerine (V2 bileşim, E/P, BM, F/NS, FD/NS, sektöre göreli PD/NA-FD/FAVÖK-PD/DD, EBITY, VALUE3/3S) | çoğu negatif; EBITY ECDF w2 +7,2 | kriz şartı (−3), dar tepe |
| Tampon "kazananı tut" K7/K10/K15; sıra ağırlığı | +%9,4 / −%43,3 / −%63,3; −%41,9 | kazandırma −2,7, 2005-15 −%24,6 |
| C32 sıralama ağırlık taraması (27) | 23 kötü; FD/FAVÖK ×0,9 +26,3 | kriz şartı; yerel optimum |
| 13 puanlama yöntemi (yüzdelik, çarpımsal, iki aşamalı, lojistik, topluluk) | −%5,2…−%97,1 | mutlak log ucuzluk + tavanlı trend en iyi |
| K+M kaynaklı P3, P6, P8a-d, P9a-c | −%1,1…−%92,6 | büyüme şartı kazananları atıyor |
| 2 haftada bir yenileme (B) / 15'inde aylık (C) | −%53 / −%83 | tüm ölçüler negatif |

## 5. Yöntem
- **Şampiyon–meydan okuyan:** her test o anki şampiyona tek değişkenli fark; varyant yalnız "Farklı Kaydet"; aynı anda en fazla 2 site testi (~55 dk); token disiplini (poll yok, zamanlanmış kontrol).
- **Kabul 7.3 (eski):** sermaye ≥+%5 (veya Sharpe +0,05 & K +0,02); iki alt dönemde CAGR −1'den kötü değil; Sharpe en fazla −0,02; kazandırma en fazla −1; kriz Σ en fazla −10; mekanizma kontrolü (tek yıl >%60 → şüpheli); havuz sağlığı. 7.4: parametre platosu, faz başına ≤6 test, 20. testten sonra %5→%8, mezarlık, sadelik. **Kullanıcı eki (28/09):** kazandırma ≥+2, Sharpe ≥, kriz ≥ ise sermaye %15'e kadar düşebilir; bir alt dönemde tolerans −6.
- **ŞAMPİYON KURALI v2 (PROTOKOL v2):** sermaye ≥+%5, kazandırma ≥−0,5, Sharpe ≥, kriz ≥ + eşli t ≥1,5 veya plasebo %95 üstü + iki yarı ve 2015+ olumlu + temiz/gerçekçi modda olumlu. t<2 → "ZAYIF"; güçlü aday için t(NW) ≥2.
- **Sim → site (kullanıcı 16:10):** önce birebir/hibrit kopyada sim; olumlu ayrışmayan aday site hakkı kazanmaz. Sitede uygulanabilir biçim (sabit eşik / ECDF) simde ayrıca test edilir (v2.1-3).
- **Sim altyapısı:** eski DS1–DS7 (localStorage, lstHisse) G1/G2/G4 hatalı → yeni kopya kacak_worker.js (IDB 'claude_c29', 3 sekme, ~73 sn/ay) + hayalet hisseler; C29 232/261 ay birebir, C32 231/261. Python araç seti (29 test) bağımsız doğrulama.
- **İstatistik:** eşli aylık log fark t (Newey-West), blok bootstrap GA, Ledoit-Wolf Sharpe farkı, Holm düzeltmesi, plasebo (veto: aynı sayıda rastgele eleme; bonus: aynı ağırlıkta rastgele bonus, 199 çekiliş), walk-forward (2005-15 seç → 2016-26 test), ızgara platosu, ilk 5 ay payı, Deflated Sharpe/PBO, deneme defteri, ön kayıt. Havuz IC (Spearman) yalnız ön eleme (v2.1-1).
- **Temiz mod** (1 gün geç alım) zorunlu kontrol; seviye düşer, sıralama değişmez.

## 6. Açık işler / bekleyenler
- Değer dosyası BEKLEMEDE (28/09 23:35); öncelik K+M DAR havuz.
- Canlı ileri test Ekim 2026'dan (her ay seçimler kaydedilir); gerçek hayata taşıma (kapanış seansında alım).
- EBITY w2–2,5 ve FD/FAVÖK<0,75 (C35 adayı): yalnız ön kayıt + canlı takiple; C35 site testi kullanıcı isterse. Canlı takipte C32'nin FD/FAVÖK<0,75 seçimleri işaretlensin.
- C34 (C29 üzerine değer bileşimi): kullanıcı kararıyla beklemede (IDB 'f_sira_C34'; editör doğrulaması yok).
- "Sağlamlık ve anlama" planı md. 2–6 (rastgele portföy, 2023–26 geride kalma/TMS 29, rejim, DSR+PBO, istikrar metrikleri): kullanıcıyla konuşulacak, kendiliğinden başlatılmayacak. Ablasyon iptal.
- 5/7/10/15 hisse, sektör/holding evreni: kullanıcı kararı. C23/C24 site testi ertelendi. Makine öğrenmesi (düşük beklenti). Ay sonu seçim avantajının mekanizması bilinmiyor (ALFA'da look-ahead testi planlı). Bedelsiz ayrıştırma fikri (DS5 notu).
- Silinecekler listesi C02'de bitiyor; sonraki elenenler (C16, C18–C24, C28, C30, C31, C33, T99, T3, C08) listede yok ve C15 listede olduğu hâlde sonradan şampiyon oldu → kullanıcıyla netleştirilmeli [belirsiz].

## 7. Ömer'in bu projeye özel istek, kural ve kararları
- 27/09 20:30 KALICI: "Final yok." Geliştirme durmaz, tüm değer literatürü + teknik taraf taranır. 23:40: "dünyanın en iyi değer stratejisi; tüm literatür, tüm alınan hisseler".
- 28/09 sabah: "İstikrar ve getiri optimumu çok önemli; kazandırma %72→%77 çıkıyorsa benim için %77 daha önemli."
- Nakitte tutma yok — model her ay hisse alsın. Portföy büyüklüğü/evren/dönem değişikliği kullanıcıya sorulur.
- 27/09 15:07: tüm onaylar verildi; istisnalar: şifre girme, kalıcı silme. Kötü sonuçlar silinsin (13:12) → Claude silmez, "Silinecekler" listesi, kullanıcı elle siler.
- Oturum düşerse: "Borfin sayfasından Queenstocks'a gir, şifre istemez".
- 27/09 14:40 ana iş akışı: alınan hisseler + geçmiş aylar → kaybedeni eleyen/kaçırılan kazananı ekleyen revizyon → sim → site. 14:44: literatür tercih edilir ama şart değil (≥3 hisse, ≥2 yıl; "literatür destekli"/"yalnız veri kaynaklı" etiketi; değer çerçevesinde kal). 14:01: teşhis için süre sorun değil.
- Kararlar: 21:50 "C03 yeni baz" · 00:48 sim tablosundaki 5 varyant sitede test edilsin · 00:52 C07–C15 kararı Claude'a · sabah "C15 kabul" · ~20:20 "C32 yeni şampiyon".
- 00:55: yeni veri seti kurmadan önce literatür araştırması + teşhis eksikliklerine göre yol haritası. 07:40: "sıradaki teşhiste yerinde dene, denemekten geri durma". 10:55: "site testinden önce sim ile önden görüyorduk, neden şimdi yapmıyoruz?"
- 16:10: her aday önce simde; simde olumlu ayrışmayan site testi hakkı kazanmaz. 15:00: tüm eski sim kararları yeni kopyayla yeniden test edilsin. PROTOKOL v2: "dürüst ol, eksiklerimiz ne".
- 19:35 raporlama kuralı: elenen her aday için "simülasyon testi sonrası kurala göre elendi" + takıldığı şart; sermayeyi artırıp elenenler ayrı tabloda — kullanıcı kararı her zaman önceliklidir.
- 21:25: "Kural çıkarma iptal, sonrasını konuşuruz; bunun getiriye bir etkisi yok." (öncelik: getiriyi etkileyen işler). 21:15: "veri bitince testleri koş, sonucu yaz".
- 23:35: "strateji strateji ilerleyelim" — değer beklemede, K+M DAR havuz önce.
- Yöntem notları: temel editörde sonucu SON `;` satırı belirler; F-Skor sıralamada da kullanılıyor uyarısı; kısa, rakamlı, Türkçe rapor; test beklerken poll yok.

## 8. Klasördeki dosyalar
| Dosya | Ne |
|---|---|
| DURUM.md | Ana canlı günlük: durum tablosu, şampiyonlar, sonuçlar, mezarlık, silinecekler, kullanıcı kararları, tur günlüğü |
| PROTOKOL.md | Araştırma protokolü: kurallar, baz formüller (§3), kabul şartları, site mekaniği, v2/v2.1/v2.2 |
| LITERATUR.md | 28/09 literatür taraması (13 tema haritası, A/B aday listesi, Türkiye uyarıları, ön kayıtlı plan) |
| C29_hisse_secimleri.xlsx | C29 seçimleri (sayfalar: Özet, C29 Seçimler, C17 ile Farklar, Tüm Pozisyonlar, Hisse Özeti); DURUM'da anılmıyor |
| elenenler_derin_analiz.xlsx | Sermayeyi artırıp elenen 15 ailenin derin analizi (Ozet, Yillik, Fark_C29 + aile sayfaları) |
| analiz_motoru.js | Sim/analiz motorunun kalıcı kopyası (+ IDB 'code_engine') |
| kacak_worker.js | Evrensel veri işçisi (hibrit kopya; 3 sekme, IDB 'claude_c29') |
| lit_worker3.js | 2. tur (literatür sinyalleri) veri işçisi |
| sim.js | Eski simülasyon kodu (__SIM, __skor, __run) |
| an.js | Sonuç okuma (__an(id), __anRun: ModelSonucDetay + PorfoyIstatistik) |
| analiz.js | Sonuç sayfası "Getiri Tablosu"ndan aylık/yıllık seri okuyan betik [belirsiz — DURUM'da anılmıyor] |
| dsjob.js / dsjob2.js | Veri seti (DS1) toplama işleri, __GATE kapı formülüyle [belirsiz] |
| metjob.js / jobs.json | Kötü aylar × 5 hisse iş listesi (metrik teşhis sorgusu) [belirsiz] |
| gate.json / kombine.json | Kapı formülü / kombine formül metni (JSON) |
| kombine.txt | Kombine formül (kapı dışı −2, teknik dışı −1, aday = Skor) |
| run_prefix.js | Kriter editöründe formül çalıştırma yardımcısı (__run) |
| baz_portfoy_raw.txt | Baz modelin aylık hisse dökümü (ModelSonucDetay) |
| kiyas_C17_C28_C29.png / .jpg | C17–C28–C29 üçlü kıyas ekran görüntüsü |
| portfoy_istatistik_C17_C28_C29 / C29_C30_C31 / C32_C29 / C33_C32_C29 .jpg | Site portföy istatistik ekran görüntüleri |
