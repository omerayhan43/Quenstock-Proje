# Kriter / model ID kaydı (QueenStocks)

Her yeni kriter veya model oluşturulduğunda HEMEN buraya eklenir (ID, ad, ne olduğu, durum). Durum etiketleri: şampiyon · seçilen · alternatif · elendi · silinecek (Ömer siler) · orijinal-dokunma · belirsiz.
Kaynaklar: dört projenin DURUM.md dosyaları (30/09/2026 derlemesi). Ayrıntı için ilgili bölüme ve DURUM.md'ye bak.

## Şu an önemli ID'ler

| Strateji | Kriter | Model | Sitedeki ad (30/09) | Durum |
|---|---|---|---|---|
| Büyüme BISTTUM (K10) | 98258 | 208322 | ALFA V5 (Geniş Havuz) K10 | şampiyon · orijinal-dokunma |
| Değer BISTTUM (C32) | 98194 | 208224 | Değer Yatırımı V1.2-C32 (...) | şampiyon · orijinal-dokunma |
| Büyüme BIST100 (K4a) | 98322 | 208422 | Büyüme Stratejisi (BIST100) | şampiyon (208419/98320 ile 261/261 aynı) |
| Büyüme BIST100 (K4a, eski ad) | 98320 | 208419 | K4a | yinelenen kopya — silinecek adayı (karar Ömer'de) |
| Değer BIST100 (DX3b) | 98329 | 208433 | DX3b | seçilen (Ömer) |
| Değer BIST100 (DX3b, ad kopyası) | 98342 | — | Değer Yatırımı Stratejisi (BIST100) | **silinecek** (yerini 98351 aldı, 30/09) |
| Yeni adlı kriterler (30/09) | 98346 · 98322 · 98349 · 98351 | 208452/454 · 208456/458 · 208459/460 · 208461/462 | Büyüme (BISTTUM) · Büyüme (BIST100) · Değer Yatırımı (BISTTUM) · Değer Yatırımı (BIST100) | yayın modelleri (2005-2026 / 2015-2026) |
| Değer BIST100 (DC1) | 98324 | 208424 | DC1 | kural tabanlı şampiyon / referans |
| Değer BAZ (V1.1) | 94555 | 208000 | Değer Yatırımı V1.1 (2005-2026) | orijinal-dokunma |
| ALFA V4.1 orijinali | 95237 | 203135 | ALFA V4.1 (GENIŞ HAVUZ) | orijinal-dokunma |
| BIST100 üyelik modeli | 98295 | 208379 | (hepsi geçer + 100 hisse) | araç — saklanır |
| Hisse kriterleri | 19006 "Herşey Dahil" · 19024 "Sadece BIST100" | | | site evren kriterleri |

## İsimlendirme işiyle oluşturulanlar (30/09 11:15–11:35, ikinci Cowork oturumu)

Kriterler (Farklı Kaydet, THYAO seçili; kaynakla 1.524 alanın tamamı birebir): **98346** Büyüme Stratejisi (BISTTUM) ← 98258 · **98322** Büyüme Stratejisi (BIST100) (mevcut, yeniden kullanıldı) · **98349** Değer Yatırımı (BISTTUM) ← 98194 · **98351** Değer Yatırımı (BIST100) ← 98342 (= 98329 DX3b; yalnız ilk yorum satırı farklı, eski adı içeriyor). Modeller orijinalle alan alan karşılaştırıldı; fark yalnız ad / kriter / başlangıç tarihi. 2015 modellerinde yalnız txtBasDonem = 01/01/2015 (dönem model sayfasında tutuluyor; test sayfası modelden okuyor).

| Ad | Kriter | Model | Sonuç | Orijinalle eşleşme |
|---|---|---|---|---|
| Büyüme Stratejisi (BISTTUM) (2005-2026) | 98346 | 208452 | 953.463.410.572 · kaz %73,95 · Sh 1,61 (11:28–12:12) | ✓ 261/261 ay birebir (208322) |
| Büyüme Stratejisi (BISTTUM) (2015-2026) | 98346 | 208454 | 11.553.688.256 · kaz %78,72 · Sh 2,02 · KR 0,52 (15:43–16:11; başlatan: Ömer/başka oturum) | ✓ 141/141 aynı sepet; Ocak 2015 getirisi farklı |
| Büyüme Stratejisi (BIST100) (2005-2026) | 98322 | 208456 | 5.850.921.769 · kaz %68,58 · Sh 1,26 (11:29–12:17) | ✓ 261/261 ay birebir (208422) |
| Büyüme Stratejisi (BIST100) (2015-2026) | 98322 | 208458 | 145.920.106 · kaz %73,05 · Sh 1,50 · KR 0,39 (13:37–14:01) | ✓ 141/141 ay aynı sepet; yalnız Ocak 2015 getirisi farklı (ayrı test 01/01'den başlatıyor) |
| Değer Yatırımı (BISTTUM) (2005-2026) | 98349 | 208459 | 777.959.361.011 · kaz %77,78 · Sh 1,76 · KR 0,50 (12:36–13:50) | ✓ 261/261 ay birebir (208224) |
| Değer Yatırımı (BISTTUM) (2015-2026) | 98349 | 208460 | 1.172.818.659 · kaz %77,30 · Sh 1,80 · KR 0,87 (15:43–16:43) | ✓ Ömer'in eski C32 2015-26 testiyle aynı |
| Değer Yatırımı (BIST100) (2005-2026) | 98351 | 208461 | 3.092.532.238 · kaz %68,20 · Sh 1,17 · KR 0,35 (12:36–13:34) | ✓ 261/261 ay birebir (208433) |
| Değer Yatırımı (BIST100) (2015-2026) | 98351 | 208462 | 39.545.653 · kaz %66,67 · Sh 1,15 · KR 0,39 (13:50–14:20) | ✓ 141/141 aynı sepet; Ocak 2015 getirisi farklı |

---

# BÖLÜM — Büyüme BISTTUM (projeler/alfa_v41)

Kaynak: `projeler/alfa_v41/` içindeki tüm .md, .txt ve PDF metinleri (30/09/2026 tarandı). Sonuçlar site sonucu (100 bin TL'den, 01/2005–25/09/2026), aksi yazılmadıkça. "←" = Farklı Kaydet kaynağı. mr = milyar TL.
Durum etiketleri: şampiyon / alternatif / elendi / silinecek / kullanıcının orijinali-dokunma / belirsiz.

### A. Kriterler
| ID | Tür | Etiket / ad | Ne olduğu | Sonuç | Durum |
|---|---|---|---|---|---|
| 19006 | kriter (hisse/evren) | "Herşey Dahil" | Model evreni = BIST TÜM (K10_kriterler.txt) | — | kullanıcının orijinali-dokunma (platform evreni) |
| 95237 | kriter | "ALFA V4.1 (Geniş Havuz) Deneme" | Kullanıcının V4.1 geniş havuz kriteri; K0 tabanı; K1/K2/K3 kaynağı (site_*_95237.txt) | 203135'te 145,52 mr; 208271'de 114,6 mr | kullanıcının orijinali-dokunma |
| 93781 | kriter | [ad yok] V4.1 kriter kardeşi | V4.1 ailesi | — | kullanıcının orijinali-dokunma |
| 95358 | kriter | V4.1 (BIST100) | V4.1 kriter kardeşi | — | kullanıcının orijinali-dokunma |
| 95359 | kriter | V4.1 (BIST100 NS) | V4.1 kriter kardeşi | — | kullanıcının orijinali-dokunma |
| 94798 | kriter | V4.1 (KATILIM) | V4.1 kriter kardeşi | — | kullanıcının orijinali-dokunma |
| 93501 | kriter | "3.0.8.6.3.55 (V1 GELİŞMİŞ) (HO<60)" | Kullanıcının V1 kriteri; S5 için yalnız okundu | S5 (V1 sıralaması) kopyada −%74,2 | kullanıcının orijinali-dokunma |
| 95106 | kriter | "1.0.0.0.0.1.275 (Alfa V1.4)" | Yalnız okundu (07:40; 23:30 aktarım taraması) | — | kullanıcının orijinali-dokunma |
| 95107 | kriter | ALFA V2.4 | Yalnız okundu (23:30 aktarım taraması) | — | kullanıcının orijinali-dokunma |
| 95108 | kriter | ALFA V3.4 | Yalnız okundu (23:30) | — | kullanıcının orijinali-dokunma |
| 81535 | kriter | ALFA V1.1.2 1.Öncelik | Yalnız okundu (23:30) | — | kullanıcının orijinali-dokunma |
| 81520 | kriter | ALFA V1.2.2 2.Öncelik | Yalnız okundu (23:30) | — | kullanıcının orijinali-dokunma |
| 93556 | kriter | ALFA V1.4 | Yalnız okundu (23:30) | — | kullanıcının orijinali-dokunma |
| 98223 | kriter | "ALFA V4.1 (Geniş Havuz) K1 - 2h göreli şartı yok" | K1: temelden yalnız "ee and" çıkarıldı (← 95237) | 109,5 mr (K0'a −%4,4) | elendi |
| 98225 | kriter | "ALFA V4.1 (Geniş Havuz) K2 - havuz içi z-skor sıralama" | K2: S4 sıralama (← 95237) | 235,1 mr (K0'a +%105) | elendi (K6A/K10 tarafından aşıldı) |
| 98226 | kriter | "ALFA V4.1 (Geniş Havuz) K3 - M1 kaldıraç yıllık FAVÖK" | K3: M1 düzeltmesi; ara site tabanı; K4/K6 kaynağı (← 95237) | 129,4 mr | alternatif (ara taban) |
| 98227 | kriter | "ALFA V4.1 (Geniş Havuz) K4 - M1 + havuz içi z-skor" | K4: M1 + S4 (← 98226) | 179,0 mr | elendi |
| 98228 | kriter | "ALFA V5 (Geniş Havuz) K6 - kâr ivmesi kademeli" | K6: G3 kapı + evren yüzdelikli kâr ivmesi (← 98226; K6_formuller.txt) | 123,3 mr (ZSkorPercentRank hatası) | elendi |
| 98231 | kriter | "ALFA V5 (Geniş Havuz) K6A - mutlak kâr ivmesi" | K6A: mutlak tavanlı kâr ivmesi (← 98228; K6A_siralama.txt) | 289,3 mr, kaz %73,18, Sh 1,45 | alternatif (eski şampiyon, 11:25) |
| 98247 | kriter | "ALFA V5 (Geniş Havuz) K7 - K6A + 52h zirve + balon veto" | K7 (← 98231) | 241,2 mr | elendi |
| 98252 | kriter | "ALFA V5 (Geniş Havuz) K8 - K7 + F/K<40 kapısı" | K8 (← 98247) | 410,9 mr, kaz %73,18 | elendi (aşıldı) |
| 98257 | kriter | "ALFA V5 (Geniş Havuz) K9 - K8 + MA75 cezası + 6 ay momentum" | K9: pen −10, mom6 w8 (← 98252) | 764,5 mr, kaz %72,80 | alternatif (K10 komşusu) |
| **98258** | kriter | "ALFA V5 (Geniş Havuz) K10" | K10: pen −15, mom6 w8 (kaynak [belirsiz]; K10_kriterler.txt) | **953,5 mr, Sh 1,61, kaz %73,95, MDD −41,7** | **şampiyon** |
| 98265 | kriter | [ad dosyada yok] K11 | K8 temel + K6A sıralama (zirvesiz) (kaynak [belirsiz]) | 474,6 mr | alternatif |
| 98264 | kriter | [ad dosyada yok] K12 | K10, pen −20 (kaynak [belirsiz]) | 634,0 mr | alternatif (K10 komşusu) |
| 98272 | kriter | [ad dosyada yok] K13 | K10, momentum w4 | 592,3 mr | alternatif (K10 komşusu) |
| 98273 | kriter | [ad dosyada yok] K14 | K10, momentum w12 | 646,8 mr | alternatif (K10 komşusu) |
| 98194 | kriter | "Değer Yatırımı V1.2-C32 (C29 + nakit akış verimi bonus4 + PDDD<8)" | C32 = Değer Yatırımı Stratejisi (Değer projesi); %50/%50 ve Büyüme + Ortak'ın ikinci ayağı | 777.959.361.011 TL, Sh 1,76 (site), kaz %77,78 | şampiyon (Değer projesi) — dokunma |

### B. Modeller
| ID | Tür | Etiket / ad | Ne olduğu | Sonuç | Durum |
|---|---|---|---|---|---|
| 203135 | model | "ALFA V4.1 (GENIŞ HAVUZ) Deneme (2005-2026)" | Kullanıcının V4.1 modeli (kriter 95237), 01/01/2005–08/07/2026 | 145.521.745.159 TL, Sh 1,32, kaz %68,48, MDD −42,9 | kullanıcının orijinali-dokunma |
| 202426 | model | V4.1 (2005-2026, Herşey Dahil) | Diğer V4.1 modeli | — | kullanıcının orijinali-dokunma |
| 202444 | model | V4.1 (Herşey Dahil) | Diğer V4.1 modeli | — | kullanıcının orijinali-dokunma |
| 203358 | model | V4.1 (BIST100) | Diğer V4.1 modeli | — | kullanıcının orijinali-dokunma |
| 202427 | model | V4.1 (KATILIM) | Diğer V4.1 modeli | — | kullanıcının orijinali-dokunma |
| 202425 | model | V4.1 (2015-2026) | Diğer V4.1 modeli | — | kullanıcının orijinali-dokunma |
| 208271 | model | "ALFA V4.1 (GENIŞ HAVUZ) K0 Taban (2005-2026)" | K0: 203135'ten Farklı Kaydet, bitiş 25/09/2026, kriter 95237; K1-K6 modellerinin kaynağı | 114,6 mr, Sh 1,27, kaz %67,82 | alternatif (referans taban) |
| 208275 | model | "ALFA V4.1 (GENIŞ HAVUZ) K1 2h göreli yok (2005-2026)" | K1 (← 208271; kriter 98223) | 109,5 mr | elendi |
| 208286 | model | "ALFA V4.1 (GENIŞ HAVUZ) K2 havuz içi z-skor (2005-2026)" | K2 (← 208271; kriter 98225) | 235,1 mr, kaz %71,26, Sh 1,38 | elendi (aşıldı) |
| 208287 | model | "ALFA V4.1 (GENIŞ HAVUZ) K3 M1 düzeltme (2005-2026)" | K3 (← 208271; kriter 98226) | 129,4 mr, kaz %68,20, MDD −47,0 | alternatif (ara taban) |
| 208288 | model | "ALFA V4.1 (GENIŞ HAVUZ) K4 M1 + havuz içi z-skor (2005-2026)" | K4 (← 208271; kriter 98227) | 179,0 mr, kaz %69,3 | elendi |
| 208289 | model | "ALFA V5 (GENIŞ HAVUZ) K6 kâr ivmesi kademeli (2005-2026)" | K6 (← 208271; kriter 98228) | 123,3 mr, kaz %70,50 | elendi |
| 208292 | model | "ALFA V5 (GENIŞ HAVUZ) K6A mutlak kâr ivmesi (2005-2026)" | K6A (← 208289; kriter 98231); K7/K8/K9 modellerinin kaynağı | 289,3 mr, Sh 1,45, MDD −40,3 | alternatif (eski şampiyon) |
| 208309 | model | [ad dosyada yok] K7 | K7 (← 208292; kriter 98247) | 241,2 mr | elendi |
| 208310 | model | [ad dosyada yok] K8 | K8 (← 208292; kriter 98252) | 410,9 mr | elendi (aşıldı) |
| 208321 | model | [ad dosyada yok] K9 | K9 (← 208292; kriter 98257) | 764,5 mr | alternatif (K10 komşusu) |
| **208322** | model | [ad dosyada yok] K10 | K10 = Büyüme Stratejisi (kriter 98258; kaynak [belirsiz]) | **953,5 mr; 2015-26: 11,31 mr, Sh 2,03** | **şampiyon** |
| 208326 | model | [ad dosyada yok] K11 | K11 (kriter 98265) | 474,6 mr, MDD −40,7 | alternatif |
| 208325 | model | [ad dosyada yok] K12 | K12 (kriter 98264) | 634,0 mr | alternatif (K10 komşusu) |
| 208337 | model | [ad dosyada yok] K13 | K13 (kriter 98272) | 592,3 mr | alternatif (K10 komşusu) |
| 208338 | model | [ad dosyada yok] K14 | K14 (kriter 98273) | 646,8 mr | alternatif (K10 komşusu) |
| 208224 | model | C32 (Değer Yatırımı Stratejisi) | Değer projesinin şampiyon modeli (kriter 98194) | 778,0 mr, KR 0,496, MDD −37,4 | şampiyon (Değer projesi) — dokunma |

### C. ID'si olmayan kurgular / notlar
- **%50/%50 (Büyüme + Değer)** ve **Büyüme + Ortak**: sitede ayrı model YOK (site ağırlıklı portföy desteklemiyor); 208322 + 208224 aylık site getirilerinden hesaplandı (1,114 tr / 1,781 tr).
- **K5**: yalnız formül taslağı (K5_siralama_formulu.txt); editörde 4 tarihte doğrulandı, tam site testi yapılmadı → ID yok.
- **K4 formülü** önce IDB'ye 's4m1_site_formula' olarak yazıldı (QueenStocks ID'si değil).
- Kullanıcının kendi C32 2015-2026 testi (28/09 23:57'de çalışıyordu): model ID dosyalarda yok; sonucu `projeler/alfa_v41/ekran/C32_2015-2026_istatistik.png`: 1.172.818.659 TL, 141 ay, kazandıran 109 (%77,30), Sharpe 1,80. Sitedeki model listesinde adıyla bulunup ID buraya yazılmalı.
- QueenStocks ID'si OLMAYAN sayılar: 2132721760 (maliyet motoru tarayıcı sekmesi), 202312 (TMS 29 dönem eşiği DonemYil×100+DonemAy), 91043 / 91593 (DergiPark URL'leri).

### D. "Silinecekler" listeleri (dosyalardan aynen)
Klasördeki hiçbir dosyada (DURUM, YOL_HARITASI, FINAL_RAPOR, GERCEKCI_UYGULAMA, LITERATUR, LIT2_A/B, BRIEF'ler, .txt'ler, iki PDF'in metni) "silinecek(ler)" başlıklı bir liste veya bir ID'yi silinecek olarak işaretleyen satır YOK ("silin", "temizl", "çöp", "arşiv" araması). Bu yüzden tabloda hiçbir ID "silinecek" durumunda değil.
Dosyalardaki ilgili kural (aynen):
- DURUM.md satır 9: "Sabit kurallar (değer projesinden devralınan): baz kriter/modelin üzerine ASLA kaydetme (yalnız Farklı Kaydet); aynı anda en fazla 2 site testi; şifre girilmez; kalıcı silme yok; model her zaman alır; önce simülasyon sonra site; 5 hisse."
- YOL_HARITASI.md "Değişmez kurallar": "… yalnız Farklı Kaydet, korunan objeler ve kaynak doğrulaması · şifre yok · kalıcı silme yok · …"

---

# BÖLÜM — Değer BISTTUM (projeler/deger_v11)

Kaynak: projeler/deger_v11/DURUM.md ve PROTOKOL.md (LITERATUR.md'de ID yok). Sonuçlar site testinden (dönem sonu sermaye · Sharpe); "Mr" = milyar TL, "B" = milyar (dosyadaki yazımla). Durum sütunu dosyadaki karara göre; dosyada açık değilse [belirsiz].

| ID | Tür | Etiket | Ne olduğu | Sonuç | Durum |
|---|---|---|---|---|---|
| 94555 | kriter | BAZ | Değer Yatırımı V1.1 orijinal kriteri (F≥7, m12, mg, HA<60; FD/FAVÖK sırası) | 215,6 Mr · 1,53 | kullanıcının orijinali — dokunma |
| 208000 | model | BAZ | Değer Yatırımı V1.1 (2005-2026) orijinal modeli | 215.610.976.077 · 1,53 | kullanıcının orijinali — dokunma |
| 98056 | kriter | T1 | Değer Yatırımı V1.1-T1 (ROA Kalite): sıralamaya roaSkor×0,30 | 20,9 Mr · 1,25 | silinecek |
| 208036 | model | T1 | Değer Yatırımı V1.1-T1 ROA Kalite (2005-2026) | 20,9 Mr · 1,25 | silinecek |
| 98057 | kriter | T2 | Değer Yatırımı V1.1-T2 (Momentum): sıralamaya momSkor×0,20 | 30,7 Mr · 1,24 | silinecek |
| 208037 | model | T2 | Değer Yatırımı V1.1-T2 Momentum (2005-2026) | 30,7 Mr · 1,24 | silinecek |
| 98061 | kriter | T3 | OCF yıllık (FAVOK→FAVOKYillik, baz üzerinde) | 176,4 Mr · 1,54 | elendi (SINIRDA/BEKLET; silinecekler listesinde yok) |
| 208042 | model | T3 | T3 modeli | 176,4 Mr · 1,54 | elendi (listede yok) [belirsiz] |
| 98062 | kriter | T4 | Değer Yatırımı V1.1-T4 (Fskor8) | 0,58 Mr · 0,82 | silinecek |
| 208043 | model | T4 | Değer Yatırımı V1.1-T4 Fskor8 (2005-2026) | 0,58 Mr · 0,82 | silinecek |
| 98064 | kriter | T5 | Değer Yatırımı V1.1-T5 (Saf FDFAVOK) | 79,0 Mr · 1,41 | silinecek |
| 208049 | model | T5 | Değer Yatırımı V1.1-T5 Saf FDFAVOK (2005-2026) | 79,0 Mr · 1,41 | silinecek |
| 98066 | kriter | T6 | Değer Yatırımı V1.1-T6 (Fskor6) | 35,6 Mr · 1,36 | silinecek |
| 208054 | model | T6 | Değer Yatırımı V1.1-T6 Fskor6 (2005-2026) | 35,6 Mr · 1,36 | silinecek |
| 98071 | kriter | T7 | Değer Yatırımı V1.1-T7 (NetBorc FAVOK 3) | 171,9 Mr · 1,50 | silinecek |
| 208068 | model | T7 | Değer Yatırımı V1.1-T7 NetBorc FAVOK 3 (2005-2026) | 171,9 Mr · 1,50 | silinecek |
| 98072 | kriter | T8 | Değer Yatırımı V1.1-T8 (Mov200) | 166,8 Mr · 1,49 | silinecek |
| 208069 | model | T8 | Değer Yatırımı V1.1-T8 Mov200 (2005-2026) | 166,8 Mr · 1,49 | silinecek |
| 98077 | kriter | T9 | Değer Yatırımı V1.1-T9 (PDDD 0.5) | 205,8 Mr · 1,51 | silinecek |
| 208075 | model | T9 | Değer Yatırımı V1.1-T9 PDDD 0.5 (2005-2026) | 205,8 Mr · 1,51 | silinecek |
| 98078 | kriter | T10 | Değer Yatırımı V1.1-T10 (Son ay getirisi puani) | 203,7 Mr · 1,50 | silinecek |
| 208076 | model | T10 | Değer Yatırımı V1.1-T10 Son ay getirisi (2005-2026) | 203,7 Mr · 1,50 | silinecek |
| 98082 | kriter | T11 | Değer Yatırımı V1.1-T11 (Tahakkuk 0.19) | 201,7 Mr · 1,52 | silinecek |
| 208080 | model | T11 | Değer Yatırımı V1.1-T11 Tahakkuk 0.19 (2005-2026) | 201,7 Mr · 1,52 | silinecek |
| 98083 | kriter | T12 | Çeyrek FAVÖK q>0,29 (BAZ üzerine) | 349,3 Mr · 1,52 | eski şampiyon (KABUL → T13'e devretti) |
| 208081 | model | T12 | T12 modeli | 349.310.005.067 · 1,52 | eski şampiyon |
| 98092 | kriter | T13 | q>0,22 (T12 plato alt komşu) | 355,0 Mr · 1,58 | eski şampiyon |
| 208086 | model | T13 | T13 modeli | 354.951.769.323 · 1,58 | eski şampiyon |
| 98093 | kriter | T14 | Değer Yatırımı V1.1-T14 (Ceyrek FAVOK 0.40) | 42,1 Mr · 1,34 | silinecek |
| 208087 | model | T14 | Değer Yatırımı V1.1-T14 Ceyrek FAVOK 0.40 (2005-2026) | 42,1 Mr · 1,34 | silinecek |
| 98098 | kriter | C01 | Değer Yatırımı V1.2-C01 (m12 kaldir) — T12 üzerine | çalıştırılmadı | silinecek (kullanılmadı) |
| 208095 | model | C01 | Değer Yatırımı V1.2-C01 m12 kaldir (2005-2026) | çalıştırılmadı | silinecek (kullanılmadı) |
| 98099 | kriter | C02 | Değer Yatırımı V1.2-C02 (Tahakkuk 0.19) — T12 üzerine | çalıştırılmadı | silinecek (kullanılmadı) |
| 208096 | model | C02 | Değer Yatırımı V1.2-C02 Tahakkuk 0.19 (2005-2026) | çalıştırılmadı | silinecek (kullanılmadı) |
| 98100 | kriter | C03 | T13 + m12 kaldır (q0,22) | 392,4 Mr · 1,63 | eski şampiyon / baz (kullanıcı kararı 27/09 21:50) |
| 208098 | model | C03 | C03 modeli | 392.383.340.440 · 1,63 | eski şampiyon |
| 98101 | kriter | C04 | Değer Yatırımı V1.2-C04 (q0.22 Tahakkuk 0.19) | 328,4 Mr · 1,58 | silinecek |
| 208099 | model | C04 | Değer Yatırımı V1.2-C04 q0.22 Tahakkuk 0.19 (2005-2026) | 328,4 Mr · 1,58 | silinecek |
| 98105 | kriter | T15 | Değer Yatırımı V1.2-T15 (q0.22 Mov10-50) | 38,9 Mr · 1,31 | silinecek |
| 208105 | model | T15 | Değer Yatırımı V1.2-T15 q0.22 Mov10-50 (2005-2026) | 38,9 Mr · 1,31 | silinecek |
| 98106 | kriter | T16 | Değer Yatırımı V1.2-T16 (q0.22 Mov50-150) | 23,4 Mr · 1,28 | silinecek |
| 208106 | model | T16 | Değer Yatırımı V1.2-T16 q0.22 Mov50-150 (2005-2026) | 23,4 Mr · 1,28 | silinecek |
| 98120 | kriter | C05 | Değer Yatırımı V1.2-C05 (C03 + FAVÖK YoY>1) | 127,7 Mr · 1,51 | silinecek |
| 208120 | model | C05 | Değer Yatırımı V1.2-C05 FAVOK YoY (2005-2026) | 127,7 Mr · 1,51 | silinecek |
| 98121 | kriter | C06 | Değer Yatırımı V1.2-C06 (C03 + reel FAVÖK YoY>TÜFE) | 94,5 Mr · 1,45 | silinecek |
| 208121 | model | C06 | Değer Yatırımı V1.2-C06 reel FAVOK YoY (2005-2026) | 94,5 Mr · 1,45 | silinecek |
| 98122 | kriter | C07 | C03 + F/K<40 (null geçer) | 487,6 Mr · 1,63 | eski şampiyon |
| 208125 | model | C07 | C07 modeli | 487.612.424.467 · 1,63 | eski şampiyon |
| 98123 | kriter | C08 | C03 + PD/NakitAkış<35 | 429,6 Mr · 1,64 | elendi (BİLGİ; silinecekler listesinde yok) |
| 208126 | model | C08 | C08 modeli | 429,6 Mr · 1,64 | elendi (listede yok) [belirsiz] |
| 98125 | kriter | C09 | Değer Yatırımı V1.2-C09 (C03 + FK<50) | 394,8 Mr · 1,60 | silinecek |
| 208128 | model | C09 | Değer Yatırımı V1.2-C09 FK50 (2005-2026) | 394,8 Mr · 1,60 | silinecek |
| 98126 | kriter | C10 | Değer Yatırımı V1.2-C10 (C03 + FK<35) | 416,2 Mr · 1,60 | silinecek |
| 208129 | model | C10 | Değer Yatırımı V1.2-C10 FK35 (2005-2026) | 416,2 Mr · 1,60 | silinecek |
| 98127 | kriter | C11 | Değer Yatırımı V1.2-C11 (C03 + FK<45) | 441,5 Mr · 1,61 | silinecek |
| 208130 | model | C11 | Değer Yatırımı V1.2-C11 FK45 (2005-2026) | 441,5 Mr · 1,61 | silinecek |
| 98137 | kriter | C12 | Değer Yatırımı V1.2-C12 (FK40 + NetKar<=3.5xFAVOK) | 490,9 Mr · 1,63 | silinecek |
| 208145 | model | C12 | Değer Yatırımı V1.2-C12 FK40 NetKar (2005-2026) | 490,9 Mr · 1,63 | silinecek |
| 98138 | kriter | C13 | Değer Yatırımı V1.2-C13 (FK40 + q VEYA satis buyume) | 538,6 Mr · 1,66 | silinecek |
| 208146 | model | C13 | Değer Yatırımı V1.2-C13 FK40 qVEYAsatis (2005-2026) | 538,6 Mr · 1,66 | silinecek |
| 98139 | kriter | C14 | Değer Yatırımı V1.2-C14 (FK40 + NetKar + q VEYA satis) | 548,3 Mr · 1,66 | silinecek |
| 208147 | model | C14 | Değer Yatırımı V1.2-C14 FK40 NetKar qVEYAsatis (2005-2026) | 548,3 Mr · 1,66 | silinecek |
| 98140 | kriter | C15 | Değer Yatırımı V1.2-C15 (FK40 + q VEYA satis sartsiz) | 592,9 Mr · 1,67 | eski şampiyon / GETİRİ HATTI referansı (kullanıcı "C15 kabul" 28/09) — AMA Silinecekler listesinde de var → [belirsiz: çelişki, silmeden önce kullanıcıya sor] |
| 208148 | model | C15 | Değer Yatırımı V1.2-C15 FK40 qVEYAsatis sartsiz (2005-2026); C19 vb. yeni modeller bundan türetildi | 592.903.396.088 · 1,67 | aynı çelişki [belirsiz] |
| 98150 | kriter | C16 | C07 + F-Skor OCF yıllık | 431,7 Mr · 1,68 | elendi (SINIRDA; risk-profili alternatifi) |
| 208168 | model | C16 | C16 modeli | 431,7 Mr · 1,68 | elendi (SINIRDA) |
| 98152 | kriter | C17 | C15 + F-Skor OCF yıllık (temel) | 429,2 Mr · 1,70 | eski şampiyon (İSTİKRAR HATTI) / alternatif |
| 208169 | model | C17 | C17 modeli | 429.172.760.150 · 1,70 | eski şampiyon / alternatif |
| 98153 | kriter | C18 | C15 + yalnız s4 yıllık OCF | 387,3 Mr · 1,68 | elendi (C17 gerisinde) |
| 208170 | model | C18 | C18 modeli | 387,3 Mr · 1,68 | elendi |
| 98156 | kriter | C19 | C17 + sıralamada da yıllık OCF | 254,2 Mr · 1,63 | elendi (RED) |
| 208173 | model | C19 | C19 modeli (208148'den türetildi) | 254,2 Mr · 1,63 | elendi (RED) |
| 98159 | kriter | C20 | C15 + (Fskor VEYA FskorYıllık ≥7) | 407,1 Mr · 1,69 | elendi (NÖTR) |
| 208175 | model | C20 | C20 modeli | 407,1 Mr · 1,69 | elendi (NÖTR) |
| 98160 | kriter | C21 | C17 − q filtresi | 346,3 Mr · — | elendi (RED) |
| 208177 | model | C21 | C21 modeli | 346,3 Mr · — | elendi (RED) |
| 98161 | kriter | C22 | C17 + F/K<45 | 426,5 Mr · — | elendi (NÖTR; plato teyidi) |
| 208178 | model | C22 | C22 modeli | 426,5 Mr · — | elendi (NÖTR) |
| 98162 | kriter | C23 | C17 + gerçek işletme nakit akışı (hibrit, kapı) | site testi yok (sim x3,81, −%45) | belirsiz (kuruldu; site testi ERTELENDİ) |
| 208179 | model | C23 | C23 modeli | site testi yok | belirsiz (ertelendi) |
| 98163 | kriter | C24 | C23 + sıralamada gerçek CFO | site testi yok (sim x3,84) | belirsiz (ertelendi) |
| 208180 | model | C24 | C24 modeli | site testi yok | belirsiz (ertelendi) |
| 98164 | kriter | C29 | C17 + teknik 3'te 2 (6ay≥0 / dip×1,5 / zirve≥%70) | 520,3B · 1,72 | eski şampiyon / alternatif; C32 bundan Farklı Kaydet |
| 208181 | model | C29 | C29 modeli | 520.305.126.289 · 1,72 | eski şampiyon / alternatif |
| 98165 | kriter | C28 | C17 + (6ay≥0 VEYA dip×1,5) VE zirve≥%70 (kullanıcı isteği) | 510,3B · 1,70 | elendi (RED, kaz −1,14) |
| 208182 | model | C28 | C28 modeli | 510,3B · 1,70 | elendi (RED) |
| 98167 | kriter | C30 | C29, 6 ay eşiği ≥5 | 422,0B · 1,71 | elendi (RED) |
| 208185 | model | C30 | C30 modeli | 422,0B · 1,71 | elendi (RED) |
| 98168 | kriter | C31 | C29, 6 ay eşiği ≥7 | 432,4B · 1,72 | elendi (RED) |
| 208186 | model | C31 | C31 modeli | 432,4B · 1,72 | elendi (RED) |
| 98184 | kriter | T99 | Ölçüm testi: C29 kapısı + sıralama = son 1 gün getirisi (C/Ref(C,-1)); strateji adayı değil | sermaye dosyada yok; sonuç: ileriyi görme YOK | belirsiz (ölçüm testi; silinecekler listesinde yok) |
| 208207 | model | T99 | T99 modeli | — | belirsiz (ölçüm testi) |
| 98194 | kriter | C32 | Değer Yatırımı V1.2-C32 (C29 + nakit akış verimi bonus4 + PDDD<8) | 777.959.361.011 · 1,76 | **ŞAMPİYON** (kullanıcı kararı 28/09 ~20:20) |
| 208224 | model | C32 | C32 modeli (208181'den Farklı Kaydet; ad dosyada yok) | 777.959.361.011 · 1,76 | **ŞAMPİYON** |
| 98199 | kriter | C33 | Değer Yatırımı V1.2-C33 (C29 + nakit akış verimi bonus5) — PD/DD sınırı yok | 654,1 milyar · 1,73 | elendi (kazandırma −2 ay, anlamlılık) |
| 208236 | model | C33 | C33 modeli (208181'den Farklı Kaydet) | 654,1 milyar · 1,73 | elendi |

**ID'si olmayan etiketler (sitede kriter/model kurulmadı):** C25 (C17 + zirve≥0,70 & dip≥1,3 — site adayı), C26 (zirve≥0,70 & dip≥1,2), C27 (C17 + 6ay≥0 VEYA dip≥1,5 — yerine C29 kuruldu), C34 (C29 üzerine değer bileşimi; formül IDB 'f_sira_C34', kullanıcı kararıyla beklemede), C35 (C32 + FD/FAVÖK<0,75 ele — yalnız kullanıcı isterse).

---

### Dosyalardaki "Silinecekler" listesi (aynen)
Bağlam (dosyalardan aynen):
- DURUM.md tur günlüğü: "27/09 13:12 — Kullanıcı: kötü sonuçlar sitede silinsin istedi → Claude silemez; 'Silinecekler' listesi tutuluyor."
- DURUM.md kullanıcı kararları (27/09 15:07): "İstisnalar değişmez: şifre girme (oturum düşerse kullanıcı girer), kalıcı silme (Silinecekler listesi)."
- PROTOKOL.md EK: "Kullanıcı isteği: reddedilen varyantlar sitede silinmeli → Claude kalıcı silme yapmaz; DURUM.md 'Silinecekler' listesine yazar, kullanıcı siler."
- Listenin tarihi: dosyada liste için ayrı tarih yok; kayıt 27/09 13:12'de başladı, son satırlar (C09–C15, C10/C11, C02) 28/09 sabahına kadar eklendi [belirsiz]. Silecek kişi: **kullanıcı (Ömer), sitede elle**.

DURUM.md "## Silinecekler (kullanıcı sitede elle siler — Claude kalıcı silme yapmaz)":

| Varyant | Kriter ID / ad | Model ID / ad |
|---|---|---|
| T1 | 98056 · Değer Yatırımı V1.1-T1 (ROA Kalite) | 208036 · Değer Yatırımı V1.1-T1 ROA Kalite (2005-2026) |
| T2 | 98057 · Değer Yatırımı V1.1-T2 (Momentum) | 208037 · Değer Yatırımı V1.1-T2 Momentum (2005-2026) |
| T4 | 98062 · Değer Yatırımı V1.1-T4 (Fskor8) | 208043 · Değer Yatırımı V1.1-T4 Fskor8 (2005-2026) |
| T5 | 98064 · Değer Yatırımı V1.1-T5 (Saf FDFAVOK) | 208049 · Değer Yatırımı V1.1-T5 Saf FDFAVOK (2005-2026) |
| T6 | 98066 · Değer Yatırımı V1.1-T6 (Fskor6) | 208054 · Değer Yatırımı V1.1-T6 Fskor6 (2005-2026) |
| T7 | 98071 · Değer Yatırımı V1.1-T7 (NetBorc FAVOK 3) | 208068 · Değer Yatırımı V1.1-T7 NetBorc FAVOK 3 (2005-2026) |
| T8 | 98072 · Değer Yatırımı V1.1-T8 (Mov200) | 208069 · Değer Yatırımı V1.1-T8 Mov200 (2005-2026) |
| T9 | 98077 · Değer Yatırımı V1.1-T9 (PDDD 0.5) | 208075 · Değer Yatırımı V1.1-T9 PDDD 0.5 (2005-2026) |
| T10 | 98078 · Değer Yatırımı V1.1-T10 (Son ay getirisi puani) | 208076 · Değer Yatırımı V1.1-T10 Son ay getirisi (2005-2026) |
| T11 | 98082 · Değer Yatırımı V1.1-T11 (Tahakkuk 0.19) | 208080 · Değer Yatırımı V1.1-T11 Tahakkuk 0.19 (2005-2026) |
| T14 | 98093 · Değer Yatırımı V1.1-T14 (Ceyrek FAVOK 0.40) | 208087 · Değer Yatırımı V1.1-T14 Ceyrek FAVOK 0.40 (2005-2026) |
| C01 (kullanılmadı) | 98098 · Değer Yatırımı V1.2-C01 (m12 kaldir) | 208095 · Değer Yatırımı V1.2-C01 m12 kaldir (2005-2026) |
| C04 | 98101 · Değer Yatırımı V1.2-C04 (q0.22 Tahakkuk 0.19) | 208099 · Değer Yatırımı V1.2-C04 q0.22 Tahakkuk 0.19 (2005-2026) |
| T15 | 98105 · Değer Yatırımı V1.2-T15 (q0.22 Mov10-50) | 208105 · Değer Yatırımı V1.2-T15 q0.22 Mov10-50 (2005-2026) |
| T16 | 98106 · Değer Yatırımı V1.2-T16 (q0.22 Mov50-150) | 208106 · Değer Yatırımı V1.2-T16 q0.22 Mov50-150 (2005-2026) |
| C05 | 98120 · Değer Yatırımı V1.2-C05 (C03 + FAVÖK YoY>1) | 208120 · Değer Yatırımı V1.2-C05 FAVOK YoY (2005-2026) |
| C06 | 98121 · Değer Yatırımı V1.2-C06 (C03 + reel FAVÖK YoY>TÜFE) | 208121 · Değer Yatırımı V1.2-C06 reel FAVOK YoY (2005-2026) |
| C09 | 98125 · Değer Yatırımı V1.2-C09 (C03 + FK<50) | 208128 · Değer Yatırımı V1.2-C09 FK50 (2005-2026) |
| C12 | 98137 · Değer Yatırımı V1.2-C12 (FK40 + NetKar<=3.5xFAVOK) | 208145 · Değer Yatırımı V1.2-C12 FK40 NetKar (2005-2026) |
| C13 | 98138 · Değer Yatırımı V1.2-C13 (FK40 + q VEYA satis buyume) | 208146 · Değer Yatırımı V1.2-C13 FK40 qVEYAsatis (2005-2026) |
| C14 | 98139 · Değer Yatırımı V1.2-C14 (FK40 + NetKar + q VEYA satis) | 208147 · Değer Yatırımı V1.2-C14 FK40 NetKar qVEYAsatis (2005-2026) |
| C15 | 98140 · Değer Yatırımı V1.2-C15 (FK40 + q VEYA satis sartsiz) | 208148 · Değer Yatırımı V1.2-C15 FK40 qVEYAsatis sartsiz (2005-2026) |
| C10 | 98126 · Değer Yatırımı V1.2-C10 (C03 + FK<35) | 208129 · Değer Yatırımı V1.2-C10 FK35 (2005-2026) |
| C11 | 98127 · Değer Yatırımı V1.2-C11 (C03 + FK<45) | 208130 · Değer Yatırımı V1.2-C11 FK45 (2005-2026) |
| C02 (kullanılmadı) | 98099 · Değer Yatırımı V1.2-C02 (Tahakkuk 0.19) | 208096 · Değer Yatırımı V1.2-C02 Tahakkuk 0.19 (2005-2026) |

Dosyalarda başka "silinecekler" listesi yok.

**Devir notu (dosyadan değil, bu özetin gözlemi):** (1) C15 (98140/208148) listede olduğu hâlde sonradan kullanıcı kararıyla şampiyon/baz oldu ve 208148 yeni modeller için şablon olarak kullanıldı → silinmeden önce kullanıcıya sorulmalı. (2) Liste 28/09 sabahından sonra güncellenmemiş; elenen T3, C08, C16, C18–C22, C28, C30, C31, C33, ertelenen C23/C24 ve ölçüm testi T99 listede yok — eklenip eklenmeyeceği kullanıcı kararı [belirsiz].

---

# BÖLÜM — Büyüme BIST100 (projeler/buyume_bist100)

Kaynak: projeler/buyume_bist100/ (DURUM.md, YOL_HARITASI.md, LIT_A, kriter/). Sonuçlar site sonucudur ("sim" yazan hariç). Son sermaye 100 bin TL ile, 2005-01…2026-09.

Durumlar DURUM.md'deki "Silinecekler listesi"ne (04:45'te güncellenmiş) ve 05:33'teki kullanıcı kararına göre verildi. 04:45 listesinde K4c "şampiyon", K4a "alternatif" yazıyor. Kullanıcı 05:33'te K4a'yı şampiyon seçti (98322 / 208422). Buna göre K4c alternatif oldu; K4a kopyası (98320 / 208419) yinelenen kopya olarak kaldı.

### Evren (hisse kriteri) ID'leri
| ID | Tür | Etiket | Ne olduğu | Sonuç | Durum |
|---|---|---|---|---|---|
| 19024 | hisse kriteri | Sadece BIST100 | Kullanılan evren (geçmiş endeks kutusu chEndeksGecmis ile) | — | kullanılıyor |
| 19005 | hisse kriteri | BİST100 | Site seçeneği | — | kullanılmadı |
| 19002 | hisse kriteri | BİST_100 (QPS_Hisse) | Site seçeneği | — | kullanılmadı |

### Kriter ID'leri
| ID | Tür | Etiket | Ne olduğu | Sonuç | Durum |
|---|---|---|---|---|---|
| 98258 | kriter | K10 | Büyüme Stratejisi, BISTTUM referansı (B0 modelinin kriteri) | BISTTUM 953,5 mr, Sh 1,61 | referans (dokunulmaz) |
| 98194 | kriter | C32 | Değer Yatırımı BISTTUM (formül özeti kontrol edildi, değişmedi) | — | referans |
| 98295 | kriter | üyelik | "BIST100 üyelik tespiti - hepsi geçer (PD sıralı)"; temel PD>0, sıralama PD, teknik C>0 | — | altyapı; modeli 208379 saklanacak [kriter listede ayrıca yok] |
| 98302 | kriter | Ş1 | "Büyüme BIST100 Ş1 - K10 + TMS29 büyüme eşiği düzeltmesi" | 2,030 mr | silinecek (elenen ara aday) |
| 98303 | kriter | K1 | "Büyüme BIST100 K1 - Ş1 + 12-6 ay XU100 göreli momentum + 2a kapısı XU100 (keşif)" | 2,540 mr | silinecek (elenen ara aday) |
| 98304 | kriter | K1b | B0 + 12-6 ay XU100 göreli momentum + 2a kapısı XU100, TMS düzeltmesiz | 2,224 mr | saklanacak (modeli listede) |
| 98307 | kriter | B0D | "Büyüme BIST100 B0D - K10 + 5 hisseye tamamlama (1: teknik yok, 2: ROE düşmüyor esnek, 3: en az kapı)" | 154,1 mn (hatalı, NaN) | silinecek (hatalı) |
| 98308 | kriter | K1bD | "K1bD - K1b + 5 hisseye tamamlama" | 230,9 mn (hatalı, NaN) | silinecek (hatalı) |
| 98312 | kriter | B0D2 | B0D + NaN koruması | 1,851 mr | saklanacak (modeli listede) |
| 98313 | kriter | K1bD2 | K1bD + NaN koruması | 2,267 mr | saklanacak (modeli listede) |
| 98316 | kriter | K2 | K1bD2 − F/K kapısı | 3,165 mr | saklanacak (eski şampiyon) |
| 98317 | kriter | B0D3 | B0D2 − F/K kapısı (karşılaştırma) | 2,098 mr | saklanacak (modeli listede) |
| 98318 | kriter | K3a | K2, C>MA200 yerine C>MA150 | 3,576 mr | silinecek (elenen ara aday) |
| 98319 | kriter | K3b | K3a + C>MA75 yerine C>MA100 | 3,923 mr | saklanacak (yedek aday) |
| 98320 | kriter | K4a | K3b + T8 (öncelikte FAVÖK koşulu yok) + C3 (kötü piyasada MA150 yok) | 5,851 mr | 04:45'te "alternatif". 05:33'ten sonra yinelenen kopya: silinecekler listesine eklenebilir (kullanıcı karar verir) |
| 98321 | kriter | K4c | K3b + T8 | 5,217 mr | alternatif (04:45–05:33 arası şampiyondu) |
| **98322** | kriter | **Büyüme Stratejisi (BIST100)** | K4a'nın Farklı Kaydet kopyası (98320'den; 2.546 karakter, sağlama toplamı eşleşti) | 5.850.921.769 TL | **ŞAMPİYON** |

### Model ID'leri
| ID | Tür | Etiket | Ne olduğu (kriter) | Sonuç | Durum |
|---|---|---|---|---|---|
| 208322 | model | K10 | Büyüme Stratejisi BISTTUM (98258) | 953,5 mr, Sh 1,61 | referans (dokunulmaz) |
| 208377 | model | B0 | "Büyüme BIST100 B0 - K10 taban, Sadece BIST100 (2005-2026)" (98258; 208322'den, yalnız evren değişti) | 1,802 mr · Sh 1,087 · MDD −40,1 · <5 hisseli ay 33 | saklanacak |
| 208379 | model | üyelik | Üyelik modeli (98295, N=100, Sadece BIST100, geçmiş endeks) | 261 ay × 100 hisse, 303 farklı hisse | saklanacak |
| 208389 | model | Ş1 | TMS düzeltmeli (98302) | 2,030 mr · Sh 1,105 | silinecek (elenen ara aday) |
| 208390 | model | K1 | Ş1 + K1b değişiklikleri (98303) | 2,540 mr · Sh 1,134 | silinecek (elenen ara aday) |
| 208391 | model | K1b | 98304 | 2,224 mr · Sh 1,115 | saklanacak |
| 208396 | model | B0D | 98307, NaN sıralama hatası | 154,1 mn · Sh 0,75 | silinecek (hatalı) |
| 208397 | model | K1bD | 98308, NaN sıralama hatası | 230,9 mn · Sh 0,78 | silinecek (hatalı) |
| 208403 | model | B0D2 | 98312 | 1,851 mr · Sh 1,077 | saklanacak |
| 208404 | model | K1bD2 | 98313 | 2,267 mr · Sh 1,103 | saklanacak |
| 208415 | model | K2 | 98316 | 3,165 mr · Sh 1,164 | saklanacak (eski şampiyon) |
| 208416 | model | B0D3 | 98317 | 2,098 mr · Sh 1,108 | saklanacak |
| 208417 | model | K3a | 98318 | 3,576 mr · Sh 1,189 | silinecek (elenen ara aday) |
| 208418 | model | K3b | 98319 | 3,923 mr · Sh 1,209 · MDD −43,6 | saklanacak (yedek aday) |
| 208419 | model | K4a | 98320 | 5.850.921.769 TL · Sh 1,261 · MDD −38,6 | 04:45'te "alternatif". 05:33'ten sonra yinelenen kopya: silinecekler listesine eklenebilir (kullanıcı karar verir) |
| 208420 | model | K4c | 98321 | 5.217.022.273 TL · Sh 1,248 · MDD −41,5 | alternatif (04:45 listesinde "şampiyon") |
| **208422** | model | **Büyüme Stratejisi (BIST100)** | 98322 (208419'dan; ayarlar aynı) | 5.850.921.769 TL · Sh 1,26 · kaz %68,58 · 261/261 ay K4a ile aynı | **ŞAMPİYON (referans model)** |
| — | model | ALFA V4.1 BIST100 | "ALFA V4.1 (GENIŞ HAVUZ) (BIST100) (2005-2026)", kullanıcının önceki denemesi (03/08/2026); kriterleri "(BIST100)" ve "(BIST100 NS)" | — | [belirsiz: ID dosyalarda yok] |

### Bağlantılı dış ID'ler (deger_bist100/ dosyalarından; Aşama 6 ve adlandırma için)
| ID | Tür | Etiket | Ne olduğu | Durum |
|---|---|---|---|---|
| 208224 | model | C32 | Değer Yatırımı BISTTUM (98194); adlandırma kopyası buradan alınacak | referans |
| 98329 / 208433 | kriter / model | DX3b | Değer Yatırımı BIST100 (3,093 mr); Aşama 6'da K4a ile birlikte incelendi | Değer şampiyonu (kullanıcı kararı) |
| 98342 | kriter | — | "Değer Yatırımı Stratejisi (BIST100)" (98329'dan) | yeni ada göre gereksiz kalırsa silinecekler listesine eklenecek |

### Silinecekler listeleri (dosyalardan aynen)
DURUM.md, 29/09 23:41 kaydı:
> - Kriter 98312 (B0D2), 98313 (K1bD2). Model 208403 (B0D2) ve 208404 (K1bD2) 23:47'de başladı; tahmini bitiş ~00:30. 208396/208397 hatalı sürüm (silinecekler listesine).

DURUM.md, "## Silinecekler listesi (kullanıcı kendisi siler; güncel)":
> - Hatalı: model 208396, 208397 · kriter 98307, 98308.
> - Elenen ara adaylar: model 208389 (Ş1), 208390 (K1), 208417 (K3a) · kriter 98302, 98303, 98318.
> - Saklanacaklar (04:45 güncel): 208377 (B0), 208379 (üyelik), 208391 (K1b), 208403 (B0D2), 208404 (K1bD2), 208415 (K2, eski şampiyon), 208416 (B0D3), 208418 (K3b), **208420 (K4c, şampiyon)**, **208419 (K4a, alternatif)**.

DURUM.md, 30/09 05:33 kaydı:
> - Silinecekler listesine eklenebilir (kullanıcı karar verir): 208419/98320 (K4a keşif adı — yeni ad doğrulanınca yinelenen kopya).

(Değer tarafında ilgili: deger_bist100/DURUM.md ve YENI_OTURUM_DEVAM.md — "98342 yeni adla gereksiz kalırsa silinecekler listesine ekle." Kural: "Hiçbir şeyi silme; silinecekleri listele, ben silerim.")

---

# BÖLÜM — Değer BIST100 (projeler/deger_bist100)

Kaynak: projeler/deger_bist100/ içindeki DURUM.md, YOL_HARITASI.md, ON_KAYIT_ASAMA4.md, YENI_OTURUM_DEVAM.md (LIT_A/LIT_B'de yalnız 208421 geçiyor). Sonuçlar dosyalardan aynen; site = QueenStocks testi, 2005–2026, 5 hisse.

### Kriter ID'leri (bilanço/sıralama kriteri)
| ID | Tür | Etiket | Ne olduğu | Sonuç (varsa) | Durum |
|---|---|---|---|---|---|
| 98194 | kriter | C32 | BISTTUM şampiyonu Değer Yatırımı V1.2-C32; D0'ın kriteri (değişmeden); DA1/DC1 buradan Farklı Kaydet; ad listesi #5–6 formül kaynağı | model 208224 ile | referans (BISTTUM şampiyonu) |
| 98258 | kriter | Büyüme BISTTUM | Ad listesi #1–2 formül kaynağı ("Büyüme Stratejisi (BISTTUM)") | — | referans (başka proje) |
| 98322 | kriter | Büyüme BIST100 | Ad listesi #3–4 formül kaynağı ("Büyüme Stratejisi (BIST100)") | — | referans (başka proje) [belirsiz: K4a ile ilişkisi bu klasörde yazmıyor] |
| 98323 | kriter | DA1 | C32 + teknik-önce tamamlama katmanları (nakit yok, her ay 5 hisse) | model 208423 | elendi (ara taban; DC1 ile aşıldı) — silme listesinde yok |
| 98324 | kriter | DC1 | DA1 + PD/DD bonusu ×2 (SkorB = Skor + 0,72 × pdddBonus) | model 208424 | **şampiyon** (kural tabanlı) |
| 98328 | kriter | DX3 | DC1 + net nakit istisnası + göreli değer (FD 0,6 / E-P 0,4, ECDF) + MA20>MA60 | model 208432 | **silinecek** |
| 98329 | kriter | DX3b | DX3 ile aynı ama MA20>MA75 | model 208433 | **seçilen** (terfi kuralını geçmedi, "keşif"/alternatif; kullanıcı seçti) |
| 98342 | kriter | DX3b kopyası | "Değer Yatırımı Stratejisi (BIST100)" — 98329'dan Farklı Kaydet; formüller aynı, yalnız sıralamanın ilk yorum satırı ve ad değişti | — (test edilmedi) | seçilen; yeni ada ("Değer Yatırımı (BIST100)") göre gereksiz kalırsa **silinecek** (koşullu) |

### Hisse (evren) kriteri ID'leri
| ID | Tür | Etiket | Ne olduğu | Sonuç | Durum |
|---|---|---|---|---|---|
| 19006 | hisse kriteri (ddlModelHisseKriter) | Herşey Dahil | C32 BISTTUM modelinin (208224) evreni | — | referans |
| 19024 | hisse kriteri (ddlModelHisseKriter) | Sadece BIST100 | Tüm BIST100 modellerinin evreni ("geçmiş endeks" chEndeksGecmis işaretli) | — | kullanımda |

### Model ID'leri
| ID | Tür | Etiket | Ne olduğu | Sonuç (varsa) | Durum |
|---|---|---|---|---|---|
| 208224 | model | C32 BISTTUM | Değer Yatırımı V1.2-C32, Herşey Dahil (kriter 98194); D0'ın kaynağı; ad listesi #5–6 kaynağı | 777,96 mr, Sh 1,76, KR 0,50, MDD −37,4, kaz %77,78 (Aşama 0 tablosu); başlangıç notu: "site 738 mr sim tabanı, kazandırma %78,5, Sharpe 1,77"; doğrulama değeri 777.959.361.011 TL (kesin: deger_v11/DURUM.md tablo "Dönem sonu sermaye") | referans (BISTTUM şampiyonu) |
| 208322 | model | Büyüme BISTTUM | Ad listesi #1–2 kaynağı (kriter 98258) | doğrulama değeri 953.463.410.572 | referans (başka proje) |
| 208377 | model | Büyüme B0 | Büyüme · K10 değişmeden, Sadece BIST100 | 1,80 mr, Sh 1,09, KR 0,27, MDD −40,1, kriz −4,61, CAGR 39,9/76,5, 33 ay <5 hisse | referans (başka proje) |
| 208379 | model | üyelik | Her ayın gerçek BIST100 üyeleri (üyelik listesi b100_mem için) | — | altyapı |
| 208419 | model | Büyüme K4a (eski ad) | K4a keşif adı; 208422 "Büyüme Stratejisi (BIST100)" bunun Farklı Kaydet kopyası (261/261 aynı) | 5,85 mr, Sh 1,26, KR 0,29, MDD −38,6, kriz −4,29, kaz %68,6, CAGR 43,9/91,3, 0 ay <5 | referans (başka projenin şampiyonu) |
| 208421 | model | D0 | C32 değişmeden, Sadece BIST100 + geçmiş endeks (208224'ten; yalnız evren 19006 → 19024) | 0,667 mr, Sh 0,94, KR 0,296, MDD −33,8, kaz %63,2, kriz −5,60, 71 ay <5 hisse | elendi (Aşama 0 tabanı) — silme listesinde yok |
| 208422 | model | Büyüme BIST100 | Ad listesi #3–4 kaynağı (kriter 98322); doğrulama "Büyüme BIST100 = model 208422 sonucu" | 5.850.921.769 TL, Sh 1,26, kaz %68,58 — 208419 ile 261/261 ay birebir (buyume_bist100/DURUM.md 30/09 06:25) | Büyüme BIST100 şampiyon modeli (referans) |
| 208423 | model | DA1 | Kriter 98323 (208421'den) | 1,028 mr (sim 1,016), Sh 1,01, KR 0,310, MDD −32,9, kaz 66,3, kriz −6,09, 0 ay <5; DA1−D0 t 1,09 | elendi (ara taban) — silme listesinde yok |
| 208424 | model | DC1 | Kriter 98324 (208421'den) | 1,749 mr (sim 1,762), Sh 1,09, KR 0,307, MDD −33,5, kaz 68,2, kriz −5,65, 0 ay <5, 2015+ yıllık %66,6; DC1−DA1 t 2,38 | **şampiyon** (kural tabanlı) |
| 208432 | model | DX3 | Kriter 98328 (208424'ten) | 2,977 mr (sim 3,355), Sh 1,17, KR 0,343, MDD −31,8, kaz 68,6, kriz −5,07, 2015+ yıllık %68,1; DX3−DC1 t 1,23 | **silinecek** |
| 208433 | model | DX3b | Kriter 98329 (208424'ten); ad listesi #7–8 kaynağı | 3,093 mr = 3.092.532.238 (sim 3,280), Sh 1,18 (sitede 1,17), KR 0,349, MDD −31,8, kaz 68,2, kriz −5,08, 2015+ yıllık %66,5; DX3b−DC1 t 1,45 | **seçilen** ("Değer Yatırımı (BIST100)") |

### Henüz oluşturulmamış (ID yok)
- 8 model: ad listesi #1–8 (Büyüme BISTTUM, Büyüme BIST100, Değer Yatırımı BISTTUM, Değer Yatırımı BIST100 × 2005-2026 / 2015-2026).
- 4 kriter kopyası: "Büyüme Stratejisi (BISTTUM)", "Büyüme Stratejisi (BIST100)", "Değer Yatırımı (BISTTUM)", "Değer Yatırımı (BIST100)".
- Not: DURUM.md'deki önceki plan (98258→"Büyüme Stratejisi (BISTTUM)", 98194→"Değer Yatırımı Stratejisi (BISTTUM)", modelleri 208322/208224'ten; 208433'ten "Değer Yatırımı Stratejisi (BIST100)" modeli) kesin ad listesiyle değiştirildi.
- QueenStocks dışı sayı: 92006 (LIT_A/LIT_B'de DergiPark dergi sayısı numarası; ID değil).

### Silinecekler (dosyalardan aynen)
- DURUM.md (30/09 10:55 kaydı): "Silinecekler (kullanıcı silecek): kriter 98328 + model 208432 (DX3; DX3b'ye göre gereksiz)."
- DURUM.md (ad listesi notları): "98342 ("Değer Yatırımı Stratejisi (BIST100)") yeni ada göre gereksiz kalırsa silinecekler listesine eklenecek."
- YENI_OTURUM_DEVAM.md: "98342 yeni adla gereksiz kalırsa silinecekler listesine ekle."
- Kural (YENI_OTURUM_DEVAM.md): "Hiçbir şeyi silme; silinecekleri listele, ben silerim."

---



## Büyüme Stratejisi (BIST KATILIM) — 30/09/2026 gece
| ID | Tür | Ad | Not |
|---|---|---|---|
| 19025 | hisse kriteri (mevcut, Ömer'in) | Sadece BISTKATILIM | Endeks: BIST KATILIM TUM (değiştirilmedi) |
| 208514 | model | BISTKATILIM TUM uyelik tespiti - hepsi gecer, 400 hisse, Sadece BISTKATILIM, gecmis endeks (2005-202… | 208379'dan Farklı Kaydet; kriter 98295, hisse kriteri 19025, geçmiş endeks ✓. Amaç: her ayın Katılım Tüm üyeleri + site getirileri; üyelik geçmişinin başlangıcı. Test 23:15 başladı |
| 98383 | temel kriter | Büyüme Stratejisi (BISTKATILIM) B0D - K10 katmanli tamamlama | 98322'den Farklı Kaydet. Temel `uye = PD() > 0`, Teknik `C > 0`; Sıralama: K10 kapıları katman olarak (fnR: a,b,d,h,j,k,bb,ucuz; fnRoe; teknik MA200/MA75/MA20-60; XUTUM) + K10 SKOR; DS = SK − 100000·TI − (TI=3 ise 2000·NF) |
| 208517 | model | Büyüme Stratejisi (BISTKATILIM) B0 - K10 aynen, gecmis endeks (2005-2026) | 208452'den Farklı Kaydet; kriter 98346, hisse kriteri 19025, geçmiş endeks ✓. Taban (tamamlamasız). Test 30/09 23:44 → 00:07: ×2,020 mn (202.033.920.791 TL) · kaz %70,11 · Sh 1,43 · KR 0,35 · Ulcer 0,77 · sim 256/261 |
| 208518 | model | Büyüme Stratejisi (BISTKATILIM) B0D - K10 katmanli tamamlama, gecmis endeks (2005-2026) | 208452'den Farklı Kaydet; kriter 98383, hisse kriteri 19025, geçmiş endeks ✓. Taban (nakit yok, 5'e tamamlama). Test 30/09 23:47 → 00:53: ×1,449 mn (144.919.691.558 TL) · kaz %71,26 · Sh 1,41 · KR 0,30 · Ulcer 0,73 · sim 255/261 |
| 208525 | model | Büyüme Stratejisi (BISTKATILIM) B0D - K10 katmanli tamamlama, gecmis endeks (2015-2026) | 208454'ten Farklı Kaydet; kriter 98383, 19025, geçmiş endeks ✓, 01/01/2015. Rapor (2015–26 site formatı). Test 01/10 00:41 → 01:24: 1.374.568.759 TL (×13.746) · kaz %72,34 · Sh 1,56 · KR 0,60 · Ulcer 1,35 · 141/141 ay 208518 ile aynı sepet |
| 98385 | temel kriter | Büyüme Stratejisi (BISTKATILIM) B0D + HA<90 (kesif) | 98383'ten Farklı Kaydet; tek fark `k=HAOran()<90;` (keşif, ön kayıt dışı) |
| 208526 | model | Büyüme Stratejisi (BISTKATILIM) B0D + HA<90 (kesif), gecmis endeks (2005-2026) | 208452'den Farklı Kaydet; kriter 98385, 19025, geçmiş endeks ✓. Aşama 5 doğrulama. Test 00:54 → 01:53: 385.719.832.822 TL (×3,857 mn; B0D'nin ×2,66'sı) · kaz %72,03 · Sh 1,48 · KR 0,28 · Ulcer 0,81 · sim 252/261 |
Not: 30/09 22:38–22:39'da sitede "Büyüme Stratejisi (BISTTUM) (2005-2026) (HA<50)" ve "(2015-2026) (HA<50)" modelleri oluşturulup test edildi — Ömer'in ya da başka bir oturumun işi; bu oturum dokunmadı.
| 98392 | temel kriter | Büyüme Stratejisi (BISTKATILIM) | 98383'ten Farklı Kaydet (01/10 04:30); editörler birebir (20 / 2386 / 6) — **ŞAMPİYON yayın kriteri** |
| 208534 | model | Büyüme Stratejisi (BISTKATILIM) (2005-2026) | 208518'den Farklı Kaydet, kriter 98392; test 01/10 04:37 başladı — **ŞAMPİYON (yayın)** |
| 208535 | model | Büyüme Stratejisi (BISTKATILIM) (2015-2026) | 208525'ten Farklı Kaydet, kriter 98392, 01/01/2015 — test sırada |

## Değer Yatırımı (BIST KATILIM) — 01/10/2026
| ID | Tür | Ad | Not |
|---|---|---|---|
| 208536 | model | Değer Yatırımı (BISTKATILIM) D0 - C32 aynen, gecmis endeks (2005-2026) | 208459'dan Farklı Kaydet; kriter 98349 (C32, değişmeden), hisse kriteri 19025 + geçmiş endeks, 5 hisse. Taban. Test 01/10 04:37 → 05:09: 50.902.427.610 TL · kaz %69,26 (257 ay) · Sh 1,39 · KR 0,38 · Ulcer 0,70 · sim 254/261 |
| 98393 | temel kriter | Değer Yatırımı (BISTKATILIM) D0D - C32 katmanli tamamlama | 98323 (Değer BIST100 DA1) Farklı Kaydet; yalnız ilk yorum satırı değişti (formül birebir) — taban (nakit yok) |
| 208537 | model | Değer Yatırımı (BISTKATILIM) D0D - C32 katmanli tamamlama, gecmis endeks (2005-2026) | 208536'dan Farklı Kaydet; kriter 98393, 19025 + geçmiş endeks. Test 01/10 05:50 → 06:58: 20.062.779.378 TL · kaz %69,35 · Sh 1,32 · KR 0,33 · Ulcer 0,57 · sim 254/261 — **ŞAMPİYON (rapor serisi)** |
| 98394 | temel kriter | Değer Yatırımı (BISTKATILIM) | 98393'ten Farklı Kaydet; formül birebir (sıralama 4214 karakter, hash 24624667 ✓) — **ŞAMPİYON yayın kriteri** |
| 208538 | model | Değer Yatırımı (BISTKATILIM) (2005-2026) | Farklı Kaydet ile; kriter 98394, 19025 + geçmiş endeks; test 01/10 06:59 → 08:14: 20.062.779.378 TL · kaz %69,35 · Sh 1,32 · KR 0,33 · Ulcer 0,57 — **ŞAMPİYON (yayın)**; 208537 ile 261/261 aynı sepet ve getiri ✓ |
| 208539 | model | Değer Yatırımı (BISTKATILIM) (2015-2026) | Kriter 98394, 19025 + geçmiş endeks, 01/01/2015. Test → 06:58: 297.837.914 TL · kaz %69,50 · Sh 1,50 · KR 0,57 · Ulcer 1,03 · 141/141 ay 208537 ile aynı sepet ✓ |
Not (01/10 05:33): 208534 ↔ 208518 261/261 ve 208535 ↔ 208525 141/141 aynı sepet + getiri ✓ (yayın adları doğrulandı).

## Dipten Dönüş Stratejisi (BISTTUM) — 01/10/2026
| ID | Tür | Ad | Not | Durum |
|---|---|---|---|---|
| 208552 | model | BISTTUM uyelik tespiti - hepsi gecer, 800 hisse, Hersey Dahil (2005-2026) | 208514'ten Farklı Kaydet; kriter 98295 (hepsi geçer), N=800, hisse kriteri 19006, yayınlanma, aylık. Altyapı: her ayın BISTTUM üyeleri + site getirileri | test 10:0x başladı — saklanacak |
