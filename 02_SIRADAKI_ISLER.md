# Sıradaki işler (30/09/2026 itibarıyla — iş bittikçe güncelle)


> **01/10 10:50 — YENİ PROJE: Dipten Dönüş Stratejisi (BISTTUM)** (Ömer onayladı: evren BISTTUM, ad "Dipten Dönüş Stratejisi"). Klasör `projeler/dipten_donus/` (YOL_HARITASI, DURUM, LITERATUR, ON_KAYIT_TABAN). Literatür bitti; veri toplama (`dd_*`, 4 sekme) ~11:45 biter; sonra teşhis (olay kütüphanesi, yıllık ilk 30/50) → T0 taban (sim + site kalibrasyon) → T1+ ön kayıtlı turlar.

> **01/10 09:05:** Büyüme Katılım denetimi tamam (projeler/buyume_katilim/DENETIM_BUYUME_KATILIM.md, KACAN_KAZANANLAR_BUYUME.md). Yeni standart kural: kaçan kazananlar testi (01_KURALLAR C.9). Değer Katılım denetimi de tamam (projeler/deger_katilim/DENETIM_DEGER_KATILIM.md, KACAN_KAZANANLAR_DEGER.md). İzleme adayları: HA<90 (Büyüme), KZ1 göreli PD/DD (Büyüme). Raporlara 'kaçan kazananlar' ve 'denetim' bölümleri en sonda eklenecek.

> **01/10 10:00:** Aşama 9 (ikinci tur, 12 deneme) bitti — terfi yok; Aşama 8+9 toplam 66 deneme, 1 terfi (Değer + Ortak). Raporlar v3. Sonraki fikir: sitede henüz kullanılmayan veri türleri (yabancı payı, geri alım, temettü, bedelsiz/bedelli duyuruları) — Ömer'e soruldu.

> **01/10 09:10:** Katılım Aşama 8 (farklı düşünce) bitti — `projeler/katilim_gelistirme/`. Büyüme: terfi yok (K10 yerel tepede). Değer: **Değer + Ortak** terfi etti (Büyüme'nin de seçtiği 2 pay; site verisiyle 40,3 mr TL, Sh 1,41). Raporlar v2 (iki Katılım raporu) güncellendi. Kalan: 208538 ↔ 208537 doğrulaması; Ekim revizyonu sonrası seçim kontrolü.

> **01/10 07:15:** **Değer Yatırımı (BISTKATILIM) tamamlandı** — şampiyon D0D (C32 + katmanlı tamamlama; 16 ön kayıtlı deneme terfi etmedi). Yayın: kriter 98394, modeller 208538 (doğrulama testi sürüyor) / 208539 ✓. Rapor `projeler/deger_katilim/BISTKATILIM_Deger_Yatirimi_Raporu_2026-10.pdf`. Kalan: 208538 ↔ 208537 261/261; Ekim revizyonu sonrası iki Katılım stratejisinin Ekim seçimini doğrula (ön seçim: Değer TUPRS+DAPGM, MOPAS, ARASE, SRVGY; Büyüme TUPRS, AHGAZ, ISDMR, BASGZ, RGYAS).

> **01/10 04:40:** Katılım Büyüme şampiyonu **B0D** kesinleşti (HA<90 gölge); yayın adları 98392 / 208534 / 208535 (doğrulama testleri). **Yeni proje: Değer Yatırımı (BISTKATILIM)** — `projeler/deger_katilim/` (aynı metodoloji: iki evren, nakit yok, taban site → sim → teşhis → literatür → ön kayıt → site → rapor). Taban D0 = 208536 (C32 aynen) testte.

> **BIST KATILIM (01/10 02:10):** Büyüme Stratejisi (BIST Katılım) tamamlandı — rapor `projeler/buyume_katilim/`. **Ömer'in kararı bekleniyor:** şampiyon B0D (98383 / 208518) mı, keşif HA<90 (98385 / 208526) mı (öneri: B0D + HA<90 gölge). Ekim revizyonu sonrası güncel Katılım listesiyle Ekim seçimini doğrula (ön seçim DURUM'da).

> **GÜNCEL DURUM (30/09 14:00):** 2005-2026 dört model doğrulandı ✅; 2015-2026 testleri sürüyor; Aşama 6 ✅; Aşama 7 kriterler ✅, BIST100 PDF raporu taslak ✅ (Ek F 2015-26 ve Ekim seçimleri eklenecek). Kalan: 2015-26 testleri → rapor Ek F; 01/10 sabahı Ekim seçimleri (§3) → rapor 11.4; silinecekler listesi Ömer'de.
>
> **Önceki not (30/09 12:40, ikinci Cowork oturumu):** §1b ve §1c TAMAM — kriterler 98346 / 98322 / 98349 / 98351, modeller 208452 / 208454 / 208456 / 208458 / 208459 / 208460 / 208461 / 208462 (ayrıntı `04_ID_KAYDI.md`). **Yeniden oluşturma.** §1d: 208452 + 208456 11:28'de başladı; 208459 + 208461, sonra 2015 modelleri sırada. §2: 1, 2, 3, 4, 7 yapıldı (farklı yöntemle, bkz. `projeler/deger_bist100/DURUM.md` sonu); 5–6 (yeni liste + Ekim seçimleri) 01/10 sabahına planlı. §3: kopyala-yapıştır kriter metni yazıldı (`projeler/deger_bist100/kriter/`).

Sıra: **1 → 2 → 3**. 1 bitmeden 2'ye geçme (Ömer: "önce bunları yap, daha sonra diğer aşamaları arka planda ilerlet"). Diğer projelerin açık işleri (4) Ömer istemeden başlatılmaz.

---

## 0. Her yeni sohbetin ilk teknik adımları
1. Tarayıcı olarak **Claude in Chrome**'u (Ömer'in Chrome'u) kullan; yerleşik tarayıcıda QueenStocks oturumu ve sim verisi yok.
2. QueenStocks oturumunu doğrula (ModelCalistir sayfası kullanıcı adıyla açılıyor mu); düşmüşse Borfin yönlendirmesi.
3. Sime eriş: `07_SIMULASYON_KILAVUZU.md` §1 (IDB `claude_c29` anahtarlarını listele, `code_b100boot` ile sim sekmesini kur, bilinen bir sonucu yeniden üret).
4. İlk sohbette bir kez: IDB kod anahtarlarını `araclar/sim_kodlari/` altına yedekle (07 §1 "Yedekle").

## 1. İsimlendirme + yeniden test (ÖNCELİK — Ömer onayladı)

### 1-ön. Mükerrer kayıt kontrolü (önce bu)
Ömer bu işi `YENI_OTURUM_DEVAM.md` metniyle başka bir sohbette başlatmış olabilir. Hiçbir şey oluşturmadan önce: kriter listesinde (`[id$=ddlKulOranTanim]` seçenek metinleri) 4 kriter adını, model listesinde (ModelCalistir sayfasındaki satırlar) 8 model adını ara. Var olanların ID'lerini `04_ID_KAYDI.md`'ye yaz ve **yeniden oluşturma**; test durumlarını (bitti/çalışıyor/başlamadı) kontrol et, yalnız eksikleri tamamla.

Amaç: dört stratejinin sitede Ömer'in formatında adlandırılmış kriter ve modelleri olsun; her strateji için 2005-2026 ve 2015-2026 modeli. **Yalnız Farklı Kaydet**, formüller değişmez, orijinallere dokunulmaz.

### 1a. Önce kontrol et
- 2015-2026 dönemi sitede nerede ayarlanıyor: model sayfasındaki `txtBasDonem` / `txtBitDonem` mi, test sayfasındaki `txtBasTar` / `txtBitTar` mı (ikisi de olabilir; ikisini de 01/01/2015 yap ve kaydedilen modelde kaldığını doğrula). Bitiş her zaman 25/09/2026.
- İpucu: Ömer'in sitede kendi çalıştırdığı bir **C32 2015-2026 testi** var (28/09; sonucu `projeler/alfa_v41/ekran/C32_2015-2026_istatistik.png`: 1.172.818.659 TL, 141 ay, kazandıran 109 = %77,30, Sharpe 1,80). Model listesinde bu modeli bul, açıp 2015 başlangıcının model sayfasında mı test sayfasında mı tutulduğunu ondan öğren; ID'sini `04_ID_KAYDI.md`'ye yaz.
- Dört kaynak modelin ayarlarını oku ve not et: tüm hisse kriteri dropdown'ları (`[id*=ddlModelHisseKriter]`, birden fazla), `chEndeksGecmis`, 5 hisse, yayınlanma, aylık, sıralama. Yeni modeller bunlarla **birebir** aynı olmalı. Kaynak modellerin sitede görünen adlarını da `04_ID_KAYDI.md`'ye yaz (208322'nin adı dosyalarda kayıtlı değil — kontrolü ID ile yap).

### 1b. Kriter kopyaları (Temel Analiz Kriterlerim; strateji başına 1, dönem eki yok)
| Sıra | Kaynak kriter | Yeni ad |
|---|---|---|
| 1 | 98258 (K10) | Büyüme Stratejisi (BISTTUM) |
| 2 | 98322 (K4a) | Büyüme Stratejisi (BIST100) — **98322'nin adı zaten bu; yeni kopya gerekmez**, 98322'yi kullan |
| 3 | 98194 (C32) | Değer Yatırımı (BISTTUM) |
| 4 | 98342 (= 98329, DX3b) | Değer Yatırımı (BIST100) |

Her kopyada: kaynağı yükle → üç editörün metnini değiştirmeden bırak → adı yaz → `lstHisse`'de THYAO seç → Farklı Kaydet → yeni ID'yi oku → üç editör metninin uzunluğu/sağlama toplamı kaynakla aynı mı kontrol et → `04_ID_KAYDI.md`'ye yaz.
Sonra: 98342 ("Değer Yatırımı Stratejisi (BIST100)") yeni adla gereksiz kalır → Silinecekler listesine ekle.
Not: 98342'nin sıralama kutusundaki ilk **yorum satırı** eski adı içerir ("// Değer Yatırımı Stratejisi (BIST100) = DX3b: …"). Yorum formül değildir; yeni kopyada yalnız bu satırı "// Değer Yatırımı (BIST100) = DX3b: …" yapmak serbesttir (formül satırlarına dokunma). 98329 (orijinal DX3b) kaynak alınırsa bu sorun yoktur.

### 1c. Model kopyaları (Portföy Model Oluşturma; bu SIRAYLA Farklı Kaydet)
| Sıra | Kaynak model | Yeni model adı | Kriter | Dönem |
|---|---|---|---|---|
| 1 | 208322 | Büyüme Stratejisi (BISTTUM) (2005-2026) | 1b-1 yeni ID | 01/01/2005–25/09/2026 |
| 2 | 208322 | Büyüme Stratejisi (BISTTUM) (2015-2026) | 1b-1 yeni ID | 01/01/2015–25/09/2026 |
| 3 | 208422 | Büyüme Stratejisi (BIST100) (2005-2026) | 98322 | 01/01/2005–25/09/2026 |
| 4 | 208422 | Büyüme Stratejisi (BIST100) (2015-2026) | 98322 | 01/01/2015–25/09/2026 |
| 5 | 208224 | Değer Yatırımı (BISTTUM) (2005-2026) | 1b-3 yeni ID | 01/01/2005–25/09/2026 |
| 6 | 208224 | Değer Yatırımı (BISTTUM) (2015-2026) | 1b-3 yeni ID | 01/01/2015–25/09/2026 |
| 7 | 208433 | Değer Yatırımı (BIST100) (2005-2026) | 1b-4 yeni ID | 01/01/2005–25/09/2026 |
| 8 | 208433 | Değer Yatırımı (BIST100) (2015-2026) | 1b-4 yeni ID | 01/01/2015–25/09/2026 |

BISTTUM modellerinde hisse kriteri "Herşey Dahil" (19006); BIST100 modellerinde ikinci hisse kriteri 19024 "Sadece BIST100" + "Geçmiş tarihlerdeki endekslere dahil hisseleri kullan" işaretli; hepsi 5 hisse. Model kaydında kriter dropdown'u değişince postback olur — sonra adı yaz, ayarları doğrula, Farklı Kaydet, ~9 sn, `hidModelId` oku.

### 1d. Testler (en fazla 2 eşzamanlı; her biri ~60–70 dk; toplam ~4–5 saat)
Önerilen sıra: 7 + 3 → 1 + 5 → 8 + 4 → 2 + 6. Her başlatmada ETA ver ve `send_later` ile ~70 dk sonra kontrol kur (yoklama döngüsü yok).

### 1e. Doğrulama değerleri
2005-2026 modelleri orijinalle **birebir** aynı olmalı (261/261 ay aynı sepet ve getiri):
- Büyüme BISTTUM: 953.463.410.572 TL (K10, 208322)
- Değer BISTTUM: 777.959.361.011 TL (C32, 208224; bazı notlarda kesilmiş "777,95 mr" diye geçer)
- Büyüme BIST100: 5.850.921.769 TL (K4a; 208419 ve 208422 birebir aynı)
- Değer BIST100: 3.092.532.238 TL (DX3b, 208433)

2015-2026 modelleri için beklenen yaklaşık değerler (100.000 TL, 01/2015'ten, 141 ay; site aylık serilerinden bileşik hesap, bağımsız denetimde sapma ≤ %0,12): Büyüme BISTTUM ≈ 11,31 mr · Değer BISTTUM ≈ 1,174 mr (Ömer'in kendi site testi: **1.172.818.659 TL**, Sharpe 1,80, kazandıran %77,30) · Büyüme BIST100 ≈ 147,4 mn · Değer BIST100 ≈ 40,0 mn. Büyük sapma varsa aylık sepetleri 2005-2026 modelinin 2015+ aylarıyla karşılaştır ve nedeni raporla.

**1 Ekim 2026 sonrası uyarısı:** BIST100 listesi 1 Ekim'de değişiyor (27 giren/27 çıkan) ve site verisi güncellenebilir. Test bu tarihten sonra çalışırsa "261/261 birebir" bozulabilir: fark çıkarsa önce hangi ay ve hisselerde olduğunu bul; son aylarda/yeni liste kaynaklıysa veri güncellemesi olarak raporla, geçmiş aylarda ise ayarları yeniden kontrol et.

### 1f. Kayıt
Her yeni ID → `04_ID_KAYDI.md`; sonuçlar → `projeler/deger_bist100/DURUM.md` (isimlendirme bölümü) ve ilgili projenin DURUM.md'si; Ömer'e kısa tablo (ad, ID, sonuç, orijinalle eşleşme ✓/✗). Site tarzı istatistik görselleri istenirse 2005-2026 ve 2015-2026 için hazırla.

---

## 2. Aşama 6'nın kalanı — iki BIST100 stratejisi birlikte (arka planda)

Yapıldı (30/09, çevrimdışı, `projeler/deger_bist100/DURUM.md` sonu): korelasyon (%80), 50/50 (Sharpe 1,28, MDD −30,6, kaz %72,8), Deflated Sharpe (en sert senaryo Büyüme %95, Değer %89), yıllık tablo, alt dönemler, 1 Ekim 2026 BIST100 değişikliği (27 giren / 27 çıkan) kaydı. Betik: `araclar/b100/asama6.py`.

Kalanlar (tarayıcı gerekli):
1. **Aylık seçimler:** K4a (208422) ve DX3b (208433) için ModelSonucDetay'dan 261 aylık sepetler → BIST100 **Büyüme + Ortak** (ortak hisse 2 pay) ve 50/50'nin gerçek sepet hesabı.
2. **Maliyet ve kapasite (BIST100 likiditesiyle):** IDB `lq_*` likidite verisi ve `araclar/cost.js` (`__COSTLOAD` / `__COSTRUN`) modeliyle; BISTTUM çalışmasındaki senaryolar (1 mn, 5 mn, 10 mn TL) ve raporlama biçimi `projeler/alfa_v41/GERCEKCI_UYGULAMA.md`.
3. **Bir gün gecikme testi** (temiz mod): sim `__DF` P.off parametresi (sim sekmesinde `code_b100boot` ile kurulur) — K4a, DX3b, 50/50.
4. **PBO / CSCV:** simdeki deneme matrisi (IDB sim sonuçları) ile; deneme sayısı Değer BIST100 ~90 sim + site, Büyüme BIST100 DURUM'da.
5. **Yeni BIST100 evreniyle test:** 1 Ekim 2026 listesi (girenler dahil); sitenin "Sadece BIST100" listesinin güncellendiği ilk iş gününü kontrol et; E1 emülasyonundaki MA20>MA75'siz sürüm notu (0,634 vs 0,359) yeniden değerlendirilecek.
6. **Ekim 2026 seçimleri:** iki stratejinin Ekim portföyü (yeni listeyle) + Büyüme+Ortak payları.
7. **Canlı ileri test planı:** Ekim 2026'dan itibaren her ay seçimler ve gerçekleşen getiriler kaydedilir (örneklem dışı); dosya önerisi `projeler/canli_takip.md` (ay, strateji, 5 hisse, pay, alış fiyatı/tarihi, ay sonu getiri, site ile fark).
8. (İsteğe bağlı) BISTTUM stratejileriyle korelasyon.

## 3. Aşama 7 — final (iki BIST100 stratejisi)
- Kopyala-yapıştır kriter metinleri: Büyüme'ninki var (`projeler/buyume_bist100/kriter/Buyume_Stratejisi_BIST100_kriter.txt`); **Değer BIST100 için yok** → editörden 98342/yeni kriterin üç kutusunu okuyup `projeler/deger_bist100/kriter/Deger_Yatirimi_BIST100_kriter.txt` olarak aynı biçimde yaz.
- Site istatistikleri (2005–26 ve 2015–26) — yeni adlandırılmış modellerden.
- PDF rapor: iki BIST100 stratejisi + birlikte kullanım (BISTTUM raporunun biçimi: `projeler/alfa_v41/BISTTUM_..._Raporu_2026-09.pdf`; üretim hattı `araclar/rapor/`).
- `YOL_HARITASI.md` (buyume_bist100, deger_bist100) ve `05_PROJE_GECMISI/` güncellenir.

## 4. Diğer projelerde açık işler (Ömer istemeden başlatma)
- **Değer BISTTUM (C32):** beklemede. Canlı ileri test Ekim 2026'dan; C34 (C29 üzerine değer bileşimi, IDB `f_sira_C34`) beklemede; zayıf adaylar (EBITY ağırlığı, FD/FAVÖK<0,75 = C35) yalnız Ömer isterse; sağlamlık planı Ömer'le konuşulacak.
- **Kârlılık + momentum dar havuz:** Değer dosyası beklemeye alınırken (28/09 23:35) sıradaki olarak anılmıştı; güncel önceliği Ömer'e sor.
- **Büyüme BISTTUM (K10):** Büyüme + Ortak mı 50/50 mi — portföy ~5 mn TL'ye yaklaşınca maliyet karşılaştırması yeniden; ~10 mn üstünde 50/50 veya karışım. İsteğe bağlı: ortak hisse 3–4 pay, bilinçli K10 payı (60/40).
- **Planlı:** BIST50 ve BIST30 sürümleri.

## 5. Silinecekler (Ömer siler — özet; tam liste `04_ID_KAYDI.md`)
- Değer BIST100: kriter 98328 + model 208432 (DX3). İsimlendirme bitince: 98342.
- Büyüme BIST100: 208396/208397, 98307/98308, 208389/208390/208417, 98302/98303/98318; 208419/98320 (K4a eski adı — yeni ad doğrulandı; karar Ömer'de).
- Değer BISTTUM: 28/09 sabahı listesi (25 satır) — **dikkat:** listede C15 (98140/208148) var ama C15 sonradan şampiyon oldu ve sonraki modeller 208148'den türetildi; ayrıca sonraki elenenler listede yok → Ömer'le netleştir, silmeden önce sor.
