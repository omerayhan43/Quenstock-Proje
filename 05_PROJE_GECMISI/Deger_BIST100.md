# Devir özeti — Değer Yatırımı (BIST100)
Kaynak: projeler/deger_bist100/ (DURUM.md son kayıt 30/09/2026 11:18). Rakamlar dosyalardan aynen; "mr" = milyar TL, başlangıç 100 bin TL.

## 1. Kimlik
- **Amaç:** BISTTUM şampiyonu Değer Yatırımı V1.2-C32'yi (kriter 98194 / model 208224) referans alıp BIST100 evreninde en iyi değer stratejisini kurmak; Büyüme BIST100 projesiyle birebir aynı yöntem (Aşama 0–5b), Aşama 6+ iki BIST100 stratejisiyle birlikte.
- **Evren/ayar:** QueenStocks, hisse kriteri 19024 "Sadece BIST100" (C32'deki 19006 "Herşey Dahil" yerine) + "Geçmiş tarihlerdeki endekslere dahil hisseleri kullan"; 5 hisse, eşit ağırlık, nakit yok, aylık, TL, yayınlanma dönemi, 01/01/2005–25/09/2026 (261 ay).
- **DC1 (kural tabanlı şampiyon):** kriter 98324 / model 208424 = C32 + teknik-önce tamamlama katmanları + PD/DD bonusu ×2. Site 1,749 mr.
- **DX3b (kullanıcının seçtiği, "keşif" etiketli):** kriter 98329 → ad düzeltilmiş kopya 98342 (formüller aynı) / model 208433. Site 3,093 mr (3.092.532.238).
- **C32 → DC1 farkları:** (a) C32 kapıları sıralamanın içinde katman: 0 = hepsi geçiyor, 1 = temel geçiyor (teknik/momentum esnek), 2 = F-Skor 6, 3 = F-Skor 5, 4 = en az koşul kaçıran; çekirdek (FD/FAVÖK>0, F/K<40, PD/DD<8) hiç gevşemez; Temel kutusu "uye = PD() > 0", teknik "C > 0"; kapı adları G sonekli. (b) SkorB = Skor + 0,72 × pdddBonus (PD/DD bonusu ×2). (c) NaN koruması (Büyüme DS3 gibi).
- **DC1 → DX3b farkları (3 değişiklik, DX3'ten farkı yalnız MA):** (1) **Net nakit istisnası** fdOK = FD > 0 veya (FD ≤ 0 ve FAVÖKYıllık > 0), puan platformdaki gibi 100 (K1a); (2) **Göreli değer:** SkorA'da fdfavokSkor yerine degerSkor = FD verimi 0,6 / E-P 0,4, sabit ECDF parçalı doğrusal (13 kırılım; kırılımlar tüm dönem dağılımından → hafif ileriyi görme) (E2b'nin sitede uygulanabilir hâli); (3) teknik MA20>MA75 **korunur** (DX3'te MA20>MA60).
- C32 kapıları (referans): F-Skor ≥ 7 ∧ FD/FAVÖK > 0 ∧ 12-1 momentum > XU100 ∧ HA < 60 ∧ (FAVÖK çeyrek payı > 0,22 ∨ satış büyümesi > 50) ∧ F/K < 40 ∧ teknik 3'ten 2 ∧ PD/DD < 8; teknik editör MA20 > MA75. Puan: FD/FAVÖK ×0,73 + MA75 trend ×0,22 + bonuslar + 4 × (nakit akış verimi eğrisi − 0,5).

## 2. Aşama aşama (tümü 30/09/2026)
| Saat | Aşama | Ne yapıldı / bulgu | Karar |
|---|---|---|---|
| 05:05 | Başlangıç | Kullanıcı isteği; altyapı Büyüme BIST100'den (üyelik modeli 208379, b100_mem, hayalet düzeltme, cmp.py, E1 emülasyonu: 09/2026'daki 27 gerçek çıkışın 23'ü) | — |
| 05:06–05:58 | 0 | D0 = C32 değişmeden, model 208421: 0,667 mr, Sh 0,94, MDD −33,8, kaz %63,2; 71 ay <5 hisse (8 ay tam nakit) | Tamamlama ilk yapısal aday |
| 06:05–07:10 | 1 | d1_ veri seti 261 ay / 24.087 hisse-ay; sim sepeti 260/261 ay site ile aynı (sim 0,649 / site 0,667); teknik MA20>MA75 sitede gerçekten uygulanıyor (yoksa 121/261) | Sim kalibre |
| 07:12 | 2 | Darboğaz F-Skor ≥ 7 (geçme %27, tek engel 2.331 hisse-ay) ve MA20>MA75; en iyi 10'un yalnız %11,6'sı tüm kapıları geçiyor; D0 22 yılın 20'sinde XU100'ü geçiyor | — |
| 07:25 | 3 | Literatür (LIT_A, LIT_B) | Ön kayıt 22 deneme (07:35 sabitlendi) |
| 07:45 | 4 | A1 teknik-önce tamamlama 1,016 (DA1); B5 HA<70, B6 E/P, B10 PD/DD ×2 geçti; C1 = A1+PD/DD×2 1,762 | **DC1 = C32 + tamamlama + PD/DD×2** |
| 07:37–08:50 | 5 | Site: DA1 1,028, DC1 1,749; DC1−DA1 t 2,38 | **DC1 şampiyon** |
| 08:55 | 5b tur 1 | C1+HA eşiği 65/70/75/80 | RED (plato yok) |
| 09:08–09:10 | 5b tur 2 | Söküm (8 kapı) + F-Skor 6/8 | 0 terfi; momentum, F=7, çeyrek FAVÖK çekirdek |
| 09:12–09:14 | 5b tur 3 | Puan ağırlıkları W1–W8 (16) | 0 terfi; puan yerel tepede |
| 09:15–09:17 | 5b tur 4 | Keşif K1a/K1b/K2a/K2b/K3a/K3b | 0 terfi; K1a yakın aday |
| 10:15 | — | YOL_HARITASI "Aşama 5–5b SONUÇ": 36 ön kayıtlı deneme, 0 terfi | Aşama 6 onayı beklendi |
| 09:20–09:25 | 5b tur 5 | Kullanıcı "Daha farklı şeyler dene…" → 14 fikir × 2 = 28 deneme | 0 terfi; E2b yakın aday |
| 09:26–09:35 | 5b tur 6 | 8 klasik değer sistemi + E16 dengeleme sıklığı | Hepsi DC1'in çok gerisinde |
| 09:40 | Keşif (ön kayıt DIŞI) | Yakın adayların birleşimi X1–X3e; X3 3,698 sim | Siteye "keşif" olarak öneri |
| 09:51–10:55 | Keşif site | DX3 2,977 / DX3b 3,093; t 1,23 / 1,45 | DC1 şampiyon kalır; DX3b **alternatif**; DX3 silinecek |
| [saat yok] | Karar | Kullanıcı: DX3b = strateji; Aşama 6+ onaylandı; kriter 98342 oluşturuldu; ad listesi kesinleşti; model/testler tarayıcı engeli nedeniyle yeni oturuma | — |
| [saat yok] | 6a/6b | Çevrimdışı K4a × DX3b korelasyon, 50/50, DSR (Bölüm 6) | — |
Not: DURUM'da Aşama 4 sonuç kaydı 07:45, Aşama 5 başlangıcı 07:37 yazılı (sıra dosyadaki gibi). YOL_HARITASI.md 10:15'ten sonra güncellenmemiş (hâlâ "K4a + DC1 birlikte, onay bekleniyor" diyor).

## 3. Site sonuçları
| Aday | Kriter / model | Site | Sim | Sepet uyumu | Sh | KR | MDD | Kaz. ay | Kriz ort. | <5 hisseli ay | t (tabana göre) | 2015+ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C32 BISTTUM (ref.) | 98194 / 208224 | 777,96 mr | — | — | 1,76 | 0,50 | −37,4 | %77,78 | — | — | — | — |
| D0 | 98194 / 208421 | 0,667 mr | 0,649 | 260/261 | 0,94 | 0,296 | −33,8 | 63,2 | −5,60 | 71 | — | CAGR 05–15/16–26: 37,5/63,7 |
| DA1 | 98323 / 208423 | 1,028 mr | 1,016 | 250/261 (hisse %99,2) | 1,01 | 0,310 | −32,9 | 66,3 | −6,09 | 0 | 1,09 (D0) | fark +2,3 |
| **DC1** | 98324 / 208424 | **1,749 mr** | 1,762 | 241/261 (%98,5) | 1,09 | 0,307 | −33,5 | 68,2 | −5,65 | 0 | **2,38** (DA1) | yıllık %66,6 |
| DX3 | 98328 / 208432 | 2,977 mr | 3,355 | 219/261 (%96,7) | 1,17 | 0,343 | −31,8 | 68,6 | −5,07 | [belirsiz] | 1,23 (DC1) | yıllık %68,1 |
| **DX3b** | 98329→98342 / 208433 | **3,093 mr** | 3,280 | 230/261 | 1,18 (site 1,17) | 0,349 | −31,8 | 68,2 | −5,08 | [belirsiz] | 1,45 (DC1) | yıllık %66,5 |
| Büyüme B0 (ref.) | — / 208377 | 1,80 mr | — | — | 1,09 | 0,27 | −40,1 | — | −4,61 | 33 | — | — |
| Büyüme K4a (ref.) | — / 208419 | 5,85 mr | — | — | 1,26 | 0,29 | −38,6 | %68,6 | −4,29 | 0 | — | — |

Fark istatistikleri (cmp.py, site serileri): **DA1−D0** +2,0 puan/yıl, t 1,09, H1/H2/2015+ +1,6/+2,4/+2,3, top5 −0,2 · **DC1−DA1** +2,4, t 2,38, boot [+0,7, +4,4], H +1,7/+3,2/+2,6, top5 +0,9, Sharpe P>0 %99,7, farklı ay 41 · **DX3−DC1** +2,4, t 1,23, boot [−1,9, +5,5], H +2,9/+2,0/+0,9, top5 −0,0, P>0 %85,7 · **DX3b−DC1** +2,6, t 1,45, boot [−1,4, +5,7], H +4,4/+0,8/−0,0, top5 +0,2, P>0 %86,8 · **DX3−DX3b** −0,2, t −0,15 (MA60 katkısı yok).
DX3b 2015–2026 (Aşama 6a): 40,0 mn, CAGR %66,5, Sh 1,16, MDD −22,8, kaz %66,7.

## 4. Denenen ve elenen fikirler (sim; sermaye mr, DC1 sim tabanı 1,762)
| Fikir | Sonuç | Eleme nedeni |
|---|---|---|
| A2 temel önce gevşer | 0,644, t −0,02, top5 −45 | A1 (1,016) daha iyi |
| B1 sürekli F puanı (F≥5) | 0,554 / 0,537, t −1,1/−1,0 | RED |
| B2 MA20>MA75 yok / C>MA150 | 0,837 / 0,727 | RED (H2 eksi) |
| B3 kötü piyasada teknik yok | 0,859 / 0,975 | RED |
| B4 momentum toleransı 5/10 | 0,752 / 0,719, t −2,5/−2,0 | RED |
| B5 HA<70 → C1+HA<70 | tek başına 1,472 (t 2,13) geçti; C1+HA<70 2,324, t 1,59, top5 −5 | top5 (kural 5); tur 1'de HA 65/75/80 = 1,965/1,899/2,034, plato yok |
| B6 E/P bonusu → C1+E/P | tek başına 1,478 geçti; C1+E/P 1,591/1,608 | C1'den kötü; PD/DD bonusuyla aynı bilgi |
| B7 ROE / B8 dolguda düşük σ / B9 nakit bonusu | 1,294–1,359 / 1,039–1,152 / 1,076–1,019 | RED (t, top5) |
| PD/DD bonusu ×3 | 1,343 | Tepe ×2 |
| Söküm: FD/FAVÖK>0 kaldır | 2,300, t 1,20, top5 −17 | RED; bankalar/net nakit giriyor → K1a'ya dönüştü |
| Söküm: F/K, PD/DD, HA, çeyrek FAVÖK, teknik 3'te 2 | 1,478 / 1,504 / 1,593 / 1,167 / 1,115 | RED; çeyrek FAVÖK ve teknik çekirdek |
| Söküm: 12-1 momentum | 0,843, t −2,22, top5 −112 | En güçlü çekirdek kapı |
| Söküm: MA20>MA75 | 1,180, t −0,90; E1'de 0,634 (DC1 0,359) | RED; E1 notu Aşama 6'ya |
| F-Skor ≥ 6 / ≥ 8 | 0,377 / 0,904 | F=7 keskin tepe |
| Puan ağırlıkları W1–W8 (16) | 15'i sermayeyi düşürdü; W6 OCF ×0 1,803 (+%2); W7 verim 0 → 1,047, t −3,05 | Yerel tepe |
| K1a net nakit (puan 100) / K1b (70) | 2,271 (t 1,22, top5 −14) / 2,047 | t<1,5, top5 → DX3b'ye girdi |
| K2a MA20>MA60 / K2b MA10>MA50 | 2,010 (top5 −27) / 1,083 | RED; K2a DX3'e girdi, sitede katkısı yok |
| K3a/K3b tamamlamada momentum önce | 1,543 / 1,589 | RED |
| E1 finansallar ayrı kapı (PD/DD) | 0,795 / 1,123 | Bankalar bu yapıda zarar |
| E2a göreli değer 4 ölçü / **E2b FD+E/P** | 0,850 / 2,430 (t 0,77, top5 −25) | E2b yakın aday → DX3b'ye girdi |
| E3 momentum bonusu / E4 büyüme önceliği / E20 Büyüme kâr ivmesi | 1,464–1,161 / 1,644–1,534 / 1,229–0,880 | Büyüme sinyalleri zararlı; stratejiler ayrı kalmalı |
| E6 kazanç ivmesi / E7 düşük oynaklık / E8 büyüklük | 1,344–1,258 / 1,171–0,920 / 1,094–1,624 | RED |
| E9 1 ay aşırı ısınma / E11 C/MA75>1,35 cezası / E12 rejim / E13 C>MA100–200 | 0,820–1,360 / 1,711–1,660 / 1,513–1,519 / 1,125–1,515 | RED |
| E22 12 ayda >%150 / >%100 yükselmişi ele | 0,725 / 0,261 | En zararlı; değer getirisi trendi süren ucuzlardan |
| E16 2 / 3 ayda bir dengeleme | 0,659 / 0,991 | Aylık en iyi |
| S1 Sihirli Formül · S2 Edinici çarpanı · S3 Piotroski · S4 QVM | 0,203 · 0,083 · 0,060 · 0,119 (t −2,11…−2,82) | Klasik değer BIST100'de çalışmıyor |
| S5 Değer+mom. 50/50 · S6 Trend değer · S7 Net nakit+mom. · S8 Derin değer | 0,275 · 0,330 · 0,164 · 0,026 | DC1'in 5–70 kat gerisinde |
| Keşif X1 (E2b+K1a) / X2 (E2b+K2a) / X3 (ikisi, ay içi yüzdelik) | 3,077 / 3,133 / 3,698 (t 1,57) | X3 sitede uygulanamaz → X3e |
| X3e FD 0,5/0,5 · 0,4/0,6 · K1b · MA75 (0,5/0,5) · C>MA50/MA10>MA50/MA50>MA150 | 3,412 · 2,625 · 2,798 · 2,112 · 1,187/2,045/1,136 | FD 0,6/E-P 0,4 seçildi (3,355 = DX3) |
| DX3 (site) | 2,977, t 1,23 | DX3b'ye göre gereksiz → silinecek |
| Temettü bonusu, sektöre göreli değer | denenmedi | Literatür önermedi (Ünal 2025; BISTTUM'da zararlı) |

## 5. Yöntem
- **Terfi kuralı v2:** sermaye ≥ +%5 · kazandıran ay ≥ −0,5 puan · Sharpe ≥ · kriz ort. ≥ · 2005–15, 2016–26, 2015+ farkları > 0 · en iyi 5 fark ayı çıkınca > 0 · plato (iki düzey aynı yön) · <5 hisseli ay artmaz · plasebo > %95 · eşli NW t ≥ 1,5 ("güçlü" ≥ 2,8, Bonferroni 20 varyant) · E1 (yeni BIST100 kuralları emülasyonu) olumlu. Simde geçemeyen siteye gitmez.
- **Ön kayıt:** Aşama 4 (ON_KAYIT_ASAMA4.md, 22 deneme, 07:35) ve tur 2–6 sonuç görülmeden DURUM'a yazıldı; her fikir en fazla 2 düzey. Keşif X1–X3e ön kayıt dışı, ~80 denemeden sonra.
- **Sim–site:** D0 0,649/0,667 · DA1 1,016/1,028 · DC1 1,762/1,749 (−%0,7) · DX3 3,355/2,977 (−%11) · DX3b 3,280/3,093 (−%6) → keşif adaylarında sim iyimser ("arama yanlılığının beklenen izi"); DX3b için ileriye dönük fark beklentisi yarıya indirilerek raporlanır.
- **Doğrulama:** editörde ilk 5 = sim: D0 2/2, DA1+DC1 8/8, DX3+DX3b 35/35.
- **İstatistik:** Newey-West t, blok bootstrap %95, H1/H2/2015+, top5 çıkarma, Sharpe farkı bootstrap P>0, plasebo, yıllık Δlog, Deflated Sharpe; Sharpe standart hatası ≈ 0,26 (LIT_B). PBO/CSCV henüz yapılmadı.
- **Literatür özü:** F-Skor büyük hissede zayıflar (prim düşük F'yi elemekten); büyük hissede değer tek başına zayıf, momentumla güçlü; BIST büyük-değer alfası %7,32 (küçük %17,64, Gökçen 2026); temettü BIST'te getiri kaynağı değil; tamamlamada önce teknik gevşer, çekirdek değer hiç gevşemez.

## 6. Aşama 6 bulguları (K4a × DX3b, site serileri, 261 ay)
| 2005–2026 | Son | CAGR | Sh | MDD | Kaz. ay | Kriz | Ulcer | Jensen |
|---|---|---|---|---|---|---|---|---|
| Büyüme K4a | 5,85 mr | %65,6 | 1,26 | −38,6 | %68,6 | −4,29 | 0,536 | 10,3 |
| Değer DX3b | 3,09 mr | %60,9 | 1,18 | −31,8 | %68,2 | −5,08 | 0,525 | 9,3 |
| 50/50 | 4,70 mr | %64,0 | 1,28 | −30,6 | %72,8 | −4,69 | 0,619 | 9,8 |
| XU100 | 5,1 mn | %19,8 | 0,22 | −58,3 | %59,0 | −8,69 | — | 0 |
2015–2026: Büyüme 147,4 mn / %86,1 / Sh 1,51 / −20,6 / %73,0 · Değer 40,0 mn / %66,5 / 1,16 / −22,8 / %66,7 · 50/50 81,4 mn / %76,9 / 1,41 / −18,9 / %75,2.
- **Korelasyon** aylık %80 (kayan 36 ay %69–%89); aktif getiri %58; kriz aylarında %74. Büyüme−Değer +2,9 puan/yıl, t 0,64 (ayırt edilemiyor); 50/50 kazancı risk tarafında.
- **DSR:** Sharpe Büyüme 1,26 / Değer 1,17 / 50/50 1,28; en sert senaryo (N=500, σ=0,30) Büyüme %95, Değer %89, 50/50 %96 → endeks üstü beceri sağlam, ama DC1→DX3b gibi son iyileştirmeleri kanıtlamaz.
- **1 Ekim 2026 BIST100 değişikliği:** 27 giren / 27 çıkan (ekovitrin.com 22/09/2026); Ekim seçimi yeni listeyle yapılmalı, sitenin "Sadece BIST100" listesinin güncellendiği kontrol edilecek.
- **Kalan Aşama 6:** (1) aylık seçimlerle BIST100 Büyüme+Ortak ve maliyet/kapasite (lq_*, cost.js); (2) bir gün gecikme testi; (3) PBO/CSCV (sim deneme matrisi Chrome 'claude_c29' IndexedDB'sinde); (4) Ekim 2026 seçimleri yeni listeyle; (5) canlı ileri test planı. Ayrıca E1'deki MA20>MA75'siz sürüm (0,634 vs 0,359) yeni evrenle yeniden bakılacak.
- **Aşama 7:** kopyala-yapıştır kriterler, site istatistikleri (2005-26 ve 2015-26), iki strateji için PDF rapor; her şey DURUM.md ve YOL_HARITASI.md'ye.

## 7. Bekleyen isimlendirme (yalnız "Farklı Kaydet", bu SIRAYLA)
1. Büyüme Stratejisi (BISTTUM) (2005-2026) — model 208322'den, kriter 98258 formülleri
2. Büyüme Stratejisi (BISTTUM) (2015-2026)
3. Büyüme Stratejisi (BIST100) (2005-2026) — model 208422'den, kriter 98322 formülleri
4. Büyüme Stratejisi (BIST100) (2015-2026)
5. Değer Yatırımı (BISTTUM) (2005-2026) — model 208224'ten, kriter 98194 formülleri
6. Değer Yatırımı (BISTTUM) (2015-2026)
7. Değer Yatırımı (BIST100) (2005-2026) — model 208433'ten, kriter 98342 (=98329 DX3b) formülleri
8. Değer Yatırımı (BIST100) (2015-2026)
- Kriterler dönemden bağımsız: strateji başına 1 kopya, dönem eki olmadan ("Büyüme Stratejisi (BISTTUM)", "Büyüme Stratejisi (BIST100)", "Değer Yatırımı (BISTTUM)", "Değer Yatırımı (BIST100)"). Değer adlarında "Stratejisi" YOK; kullanıcının "Büyme" ve eksik parantezi yazım hatası sayıldı (onaylı). Önce 2015-2026 döneminin nerede ayarlandığı (model/test sayfası) kontrol edilecek. En fazla 2 eşzamanlı test.
- **Doğrulama (2005-2026 orijinallerle birebir):** Büyüme BISTTUM 953.463.410.572 · Değer BISTTUM 777.959.361.011 TL · Büyüme BIST100 5.850.921.769 TL · Değer BIST100 3.092.532.238 (261/261 ay).
- 208422 (kriter 98322) "Büyüme Stratejisi (BIST100)", K4a modeli 208419'un Farklı Kaydet kopyasıdır; 261/261 ay birebir aynı (buyume_bist100/DURUM.md 30/09 06:25).

## 8. Ömer'in bu projeye özel istekleri / kararları
- "Büyüme BIST100'de yaptığımız her şeyi (Aşama 0–5b) Değer Yatırımı stratejisi için de BIST100'de yapmak; kurallar, yöntem ve bakış açısı aynı. Aşama 6 ve sonrası iki BIST100 stratejisiyle birlikte."
- Nakit yok, her ay 5 hisse (tamamlama bu kural gereği; DA1 taban oldu).
- "Daha farklı şeyler dene, hiçbir açık kapı kalmamalı; fark (Büyüme'ye göre) çok fazla." (09:20 → tur 5–6)
- "Götür" (09:51, DX3/DX3b keşif site testi).
- DX3b'yi strateji olarak seçti; Aşama 6+ onayladı; 8 adlık listeyi ve sırasını verdi.
- Öncelik: istikrar ve kazandırma oranı önemli (YOL_HARITASI).
- Devir metnindeki kurallar: "Sitede yalnız "Farklı Kaydet" kullan, mevcut kriter/modellerin üzerine asla kaydetme. Hiçbir şeyi silme; silinecekleri listele, ben silerim. Şifre girme; oturum düşerse https://borfin.com/tr/programs/153/redirect üzerinden gir. Sitede aynı anda en fazla 2 test. Uzun testlerde sık yoklama yapma; başlat, tahmini bitiş süresini söyle, send_later ile ~70 dk sonra kontrol et." · "Bilgisayarımda klasör ARAMA" · "Her şeyi DURUM.md ve YOL_HARITASI.md'ye işle."
- Değişmez kurallar (YOL_HARITASI): önce sim sonra site, kalıcı silme yok, şifre yok, elenen her aday gerekçesiyle, ETA ver, gereksiz sorgu yok.

## 9. Dosyalar (projeler/deger_bist100/)
- DURUM.md — zaman damgalı tam kayıt: tüm aşamalar, tablolar, kararlar, ad listesi, Aşama 6a/6b.
- YOL_HARITASI.md — hedef, değişmez kurallar, aşama listesi; son güncelleme 10:15 (DX3b kararı işlenmemiş).
- ON_KAYIT_ASAMA4.md — Aşama 4 ön kaydı: terfi kuralı v2, A1/A2 tamamlama, B1–B10 (22 deneme).
- YENI_OTURUM_DEVAM.md — yeni oturuma yapıştırılacak devir metni: site işlemleri (seçiciler), ad listesi, doğrulama, kalan Aşama 6–7.
- LIT_A_buyuk_hisse_deger.md — büyük hissede değer/kalite/F-Skor literatürü, 10 fikir, dürüst beklenti.
- LIT_B_kurgu_yeni_kurallar.md — kurgu, tamamlama sırası, yeni BIST100 kuralları, çoklu test, T1–T10 planı, site formül iskeleti.
- Klasörde olmayan referanslar: deger_v11/DURUM.md, deger_v11/LITERATUR.md, buyume_bist100/ (LIT_A, LIT_B, DURUM), cmp.py, IDB 'c32_formulas', d1_ veri seti, b100_mem.

## Aşama 6–7 sonuçları (30/09, ikinci Cowork oturumu; ayrıntı deger_bist100/DURUM.md)
- Sitede yeni adlar: kriterler 98322 (Büyüme BIST100) / 98351 (Değer BIST100); modeller 208456/208458 ve 208461/208462. 2005-26 modelleri orijinallerle (208422, 208433) 261/261 ay birebir.
- Büyüme + Ortak (Ömer'in kuralı): 6,77 mr, yıllık %66,8, Sh 1,28, MDD −32,8, kaz %69,7; Büyüme'ye göre +0,7 puan/yıl (t 0,55); %50/%50: 4,70 mr, Sh 1,285, MDD −30,6, kaz %72,8.
- Maliyet (5 mn TL gerçekçi): B+O 5,1 / B+D 3,9 puan/yıl; kapasite ~50 mn TL. Bir gün gecikme: Büyüme +0,1, Değer −2,0 (t −1,53), B+O +0,5 puan/yıl.
- PBO/CSCV (site finalistleri): Büyüme %3,0 (13 varyant), Değer %6,2 (5 varyant). DSR (500; 0,30): Büyüme %95, Değer %89.
- Rapor: BIST100_Buyume_Deger_Yatirimi_Strateji_Raporu_2026-09.pdf (68 s.).
- Düzeltme (30/09 14:15): EFES ≠ AEFES (Şubat–Mart 2005) → Büyüme + Ortak 6,845 mr, yıllık %66,85, Büyüme'ye göre +0,72 puan/yıl (t 0,59). Değer + Ortak: 5,14 mr, yıllık %64,7, Sh 1,24. Rapor 100 s. (site formatı sayfaları + Ek G–K).
