# LIT_A — Temel/muhasebe tabanlı dönüş ve kâr sıçraması sinyalleri (Ajan A)

Strateji: "Dipten Dönüş" (BIST TÜM, aylık 5 hisse, eşit ağırlık, her zaman yatırımda)
Hazırlanma: 01/10/2026 · Kapsam: zarardan kâra geçiş, PEAD/kazanç momentumu, kârlılık değişimi, ΔE/P, F/G-Skor, sıkıntı anomalisi, temel sinyaller/kazanç kalitesi, kontrol/yönetim değişikliği, uygulayıcı kaynaklar, Türkiye kanıtı.

**Etiketler:**
- **[DY]:** Kaynak ya da bulgu doğrulanamadı.
- **[Ö]:** Rakam PDF ya da tam metin özetinden okundu (araç özeti), özet sayfasında yok.
- **[İ]:** Rakam ikincil kaynaktan (derleme, blog, dergi haberi) alındı.
- **Etiketsiz rakam:** Yayıncının ya da indeksin (RePEc/EconPapers/SSRN/ScienceDirect/OUP/Springer/DergiPark) özet sayfasında doğrudan görüldü.

**Durum kodları:** T = denendi (K10/C32'de var), P = kısmen, N = denenmedi.

---

## 0. Yönetici özeti (7 madde)

1. **Fiyata ölçeklenmiş kâr değişimi (ΔE/P) iki profili tek ölçüde birleştiriyor.** Profil 1 (zarardan kâra) ve Profil 2 (kâr sıçraması) aynı sayıyla sıralanabiliyor. Net kâr büyüme yüzdesi negatif ya da sıfıra yakın tabanda anlamsız; ΔE/P değil. Literatürdeki "zaman serisi SUE" (Bernard & Thomas 1989; Livnat & Mendenhall 2006) ve ΔROE (Hou-Xue-Zhang) bunun akrabası. Türkiye'de PEAD kanıtı var: 60 günde %2,9 fark (Ahlatcıoğlu & Okay 2021).
2. **Zararı alıp dönüşü beklemek yerine dönüş görüldükten sonra almak gerekiyor.** Yatırımcılar tüm zararları geçici sanıyor. Kalıcı zarar beklenen firmalar sonraki 4 çeyrekte negatif anormal getiri veriyor (Li 2011). Uç zarar açıklayanlar, uç kâr açıklayanların yıllık ≈%21 gerisinde kalıyor (Balakrishnan-Bartov-Faurel 2010). Kural: **son çeyrek net kârı > 0** kapısı.
3. **Sıkıntılı şirketler ortalamada kötü getiri veriyor** (Dichev 1998; Campbell-Hilscher-Szilagyi 2008). Ama sıkıntılı ve **ucuz** olanlarda değer etkisi iki katından fazla (Griffin & Lemmon 2002). Değer stratejileri getirisini "hayatta kalan sıkıntılı" firmaları alarak kazanıyor (Avramov vd. 2013). Dönüş stratejisinin işi bu ayrımı yapmak: ucuz + iyileşen + öz kaynağı pozitif.
4. **Sahte kâr en büyük risk.** Özel kalemler fiyata tam yansımıyor (Burgstahler vd. 2002). Tahakkuk anomalisi BIST'te yalnız kâr eden firmalarda var: %18,58 anormal getiri (Ozkan & Kayalı 2015). BIST'e özgü kaynaklar: kur farkı, varlık satışı ve TMS 29 net parasal pozisyon kazancı. Bunlara karşı **FAVÖK teyidi** (net kâr ≤ FAVÖK ve FAVÖK artıyor) ve **işletme nakit akışı > 0** kapıları öneriliyor.
5. **Kâr momentumu, fiyat momentumunu açıklıyor** (Chordia & Shivakumar 2006; Novy-Marx 2015). Fiyat momentumu kontrol edilince kazanç momentumunun çöküşleri kayboluyor. Bu da Ömer'in "piyasanın da inanması" sezgisini destekliyor: kâr sıçraması **sıralama**, fiyat trendi **kapı/teyit** olarak.
6. **Etki hızlı sönümleniyor.** ABD'de SUE farkı 1 ay tutmada %0,46/ay, 12 ayda %0,08/ay [Ö] (Hou-Xue-Zhang 2020). Kârlılık ortalamaya dönüyor: yılda ≈%38, ortalamadan uzaksa daha hızlı (Fama & French 2000). Aylık dengelemede **taze rapor** ve **uç değer tavanı** önemli.
7. Türkiye'de kârlılık ve momentum faktörleri **2005 sonrası** anlamlı, değer en güçlü faktör: yıllık >%17 (Gökçen 2026, Borsa Istanbul Review). Strateji dönemiyle (2005–2026) örtüşüyor.

---

## 1. Platform formül dili notları (taslakların varsayımları)

- Brief'te ve `dd_forms.json` içinde görülen fonksiyonlar kullanıldı: `NetKarYillik("",-4)`, `NetKar("TL",-k)`, `OzsermayeKarlilikYillik("",-k)`, `ToplamBorcAktif("",-4)`, `Ozsermaye()`, `FD()`, `Aktifler()`, `PD()`, `FAVOKYillik()`, `NetBorcFavokYillik()`, `IsletmeFaaliyetlerdenNakitAkis()`, `NetSatisBuyumeYillik()`, `Tufe(12)`, `Getiri(...)`, `Teknik.Indicator(...)`, `IF`, `Min`, `Max`, `==null`.
- **Sitede doğrulanmalı:**
  - `FAVOKYillik("",-4)`, `FAVOKMarjiYillik("",-4)` ve `NetKarMarjiYillik("",-4)` dönem parametresi (NetKarYillik ile aynı sözdizimi varsayıldı).
  - `IsletmeFaaliyetlerdenNakitAkis()`'ın yıllık (TTM) mı çeyreklik mi olduğu.
  - `ToplamBorcAktif()` biriminin % mi oran mı olduğu.
  - `or` operatörü. Taslaklarda `or` yerine `IF(...)+IF(...)>=1` kullanıldı.
- **Bankalar:** `FAVOKYillik()==null` olunca FAVÖK'e dayalı kapılar **geçer** sayıldı (`IF(FAVOKYillik()==null,1,...)`).
- **Negatif öz kaynak:** Zarar / negatif öz kaynak pozitif ROE üretir. ROE'ye dayalı her sinyal `Ozsermaye()>0` ile korunmalı.

---

## 2. Bulgular tablosu

### A. Zarardan kâra geçiş / zarar dönüşleri

| # | Bulgu (yazar, yıl, örneklem, dönem, etki) | Replikasyon / GOP / TR | Durum | Taslak (tek satır) | Öncelik | Rol |
|---|---|---|---|---|---|---|
| A1 | **Hayn (1995)**, JAE 20(2):125-153. Hissedarın tasfiye opsiyonu nedeniyle zararların kalıcı olması beklenmez. Bu yüzden zararlar kârlara göre geleceğe dair daha az bilgi taşır. Uzun dönemde artan kazanç-tepki katsayısı tamamen zarar etkisinden kaynaklanır. Ortalamaya dönme açıklaması desteklenmez. | Joos & Plesko (2005) ve Li (2011) üzerine kuruldu. TR: doğrudan test bulunamadı. | N | `zararGecmis=NetKarYillik("",-4)<=0;` | Orta | Tasarım ilkesi: **zarar dönemindeki büyüklüğü skora sokma, işaret değişimini kullan** |
| A2 | **Joos & Plesko (2005)**, TAR 80(3):847-870. Bir yıl ileri "zararın dönme olasılığı" modeli. Geçici (dönmesi olası) zararlara fiyat tepkisi daha güçlü. Model değişkenleri (Li 2011 çalışma kağıdından) [Ö]: zarar büyüklüğü, geçmiş kâr, büyüklük, satış büyümesi, "ilk zarar" ve dönüş olasılığı ↑; ardışık zarar serisi ve temettü kesme ↓; temettü ödeme ↑. | Avustralya: Wu (2017), AJM 42(4). Sabit varlık yatırımı dönüş olasılığını artırıyor, arama/Ar-Ge yoğunluğu azaltıyor. Tahmin edilen olasılık, bilgi ortamı zayıf firmalarda sonraki getiriyle ilişkili. | N | `zararSeri=IF(NetKar("TL",-1)<=0,1,0)+IF(NetKar("TL",-2)<=0,1,0)+IF(NetKar("TL",-3)<=0,1,0)+IF(NetKar("TL",-4)<=0,1,0);` | Yüksek | Kapı (ör. `zararSeri<=2`) ya da ceza: **uzun zarar serisi = kalıcı zarar** |
| A3 | **Darrough & Ye (2007)**, RAS 12(1):61-93. Zarar eden firmaların çoğu klasik "sıkıntılı" kalıba uymaz. Değer sürücüsü "gizli varlıklar" (maddi olmayan, Ar-Ge). | BIST'te Ar-Ge yoğun zarar eden firma az; uygulanabilirlik sınırlı. | N | `buyuyenZarar=NetKarYillik()<=0 and NetSatisBuyumeYillik()>Tufe(12);` | Düşük | Yorum: büyüyen zarar ≠ çöken zarar |
| A4 | **Li (2011)**, RAS 16(3):630-667. 1983–2006, 64.539 firma-çeyrek [Ö]. Yatırımcılar tüm zararları geçici sanıyor. Model "kalıcı" diyenler sonraki 4 çeyrekte anlamlı negatif anormal getiri veriyor. Hedge ≈%0,64/ay (≈%7,7/yıl) [Ö]. Çalışma kağıdı sürümü [Ö]: kalıcı tahminlilerin yalnız %8,5'i, geçici tahminlilerin %67,4'ü sonraki çeyrek kârlı. Kalıcı grupta 1 yıl −%12,0. | İngiltere: "Loss persistence and returns in the UK", ABR 46(3) (künye arama sonucundan; sayfa 403) [DY]. | N | `kalici=NetKar("TL",0)<=0 and zararSeri>=3;` | **Yüksek** | Kapı (dışlama). En sade hali: `NetKar("TL",0)>0` |
| A5 | **Balakrishnan, Bartov & Faurel (2010)**, JAE 50(1):20-41. "Zarar/kâr açıklaması sonrası kayma": uç zarar ve uç kâr portföyleri arasındaki yıllıklaştırılmış getiri farkı ≈%21. Risk, büyüklük ve işlem maliyeti kontrollerinden sonra sürüyor. | TR: doğrudan yok. Şimşek & Yıldırım (2020): BIST30'da %50'den büyük kâr/zarar değişimlerinde tepki daha güçlü. | N | `qEP=NetKar("TL",0)/PD();` | **Yüksek** | Kapı (`NetKar("TL",0)>0`) + skor bileşeni |
| A6 | **Kullanıcı tanımı (Profil 1):** ROE negatiften pozitife ve öz kaynak pozitif. Literatür karşılığı: A1–A5 + Piotroski (E1). | — | N | `roeDonus=OzsermayeKarlilikYillik("",-4)<0 and OzsermayeKarlilikYillik()>0 and Ozsermaye()>0;` | Yüksek | Bonus (Profil 2'yi dışlamamak için kapı değil) |

### B. Kazanç sürprizi, PEAD ve kazanç momentumu

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| B1 | **Bernard & Thomas (1989)**, JAR 27 (Ek):1-36. 1974–1986. SUE ondalıklarında iyi/kötü haberde 60 işlem gününde ≈±%2 kayma, ≈%4 çeyreklik / ≈%18 yıllık [İ][Ö] (Fink 2020 derlemesi). | **TR:** Ahlatcıoğlu & Okay (2021), BIR 21(1):92-103, 2007–2018. Yüksek-düşük sürpriz farkı 60 günde %2,9 (zaman serisi), %2,9 (analist), %2,2 (açıklama getirisi). Büyüklük etkiyi azaltıyor. Fama-French modelleri açıklamıyor. ABD'de PEAD zamanla azalıyor (Fink 2020'nin aktardığı Chordia vd. 2014; Richardson vd. 2010). | P (K10'da EFK büyüme ivmesi var; fiyat ölçekli çeyrek sürprizi yok) | `sueP=(NetKar("TL",0)-NetKar("TL",-4))/PD();` | **Yüksek** | Skor / bonus |
| B2 | **Bernard & Thomas (1990)**, JAE 13(4):305-340. Çeyreklik mevsimsel farkların otokorelasyonu 1–3. gecikmede pozitif, 4.'de negatif. Fiyatlar bunu tam yansıtmıyor (kayma bir sonraki açıklamalarda sürüyor) [İ] (Fink 2020). | Türkiye bilgi ortamı: Ahlatcıoğlu & Okay (2019), JCMS 3(2). 2007–2017 kazanç açıklamalarının bilgi içeriği KAP ile artmış. Büyüme firmaları ve büyük sürprizlerde daha çok. | N | `ardisik=NetKar("TL",0)>NetKar("TL",-4) and NetKar("TL",-1)>NetKar("TL",-5);` | Orta | Bonus (iki ardışık iyileşme) |
| B3 | **Chan, Jegadeesh & Lakonishok (1996)**, JF 51(5):1681-1713. Geçmiş getiri ve geçmiş kazanç sürprizi, birbirini kontrol ettikten sonra da gelecekteki kaymayı ayrı ayrı tahmin ediyor. Yüksek fiyat ve kazanç momentumlu hisselerde sonradan tersine dönme az. Analistler de yavaş güncelliyor. | Gelişmiş ve gelişmekte olan piyasalarda yaygın replikasyon (bu taramada ayrıca açılmadı). | P (K10 6 ay momentum + EFK ivmesi) | `ikili=sueP>0 and Getiri("s6a","TL")>0;` | Yüksek | Kapı/teyit |
| B4 | **Chordia & Shivakumar (2006)**, JFE 80(3):627-656. Kazanç momentumu (yüksek-düşük sürpriz) fiyat momentumunun tahmin gücünü kapsıyor. Kazanç momentumu getirisi makro değişkenlerle (GSYH, sanayi üretimi, enflasyon…) ilişkili. | — | P | (B1 ile aynı) | Orta | Kuramsal destek |
| B5 | **Novy-Marx (2015)**, NBER WP 20984. 1975–2012. Kazanç sürprizi (SUE, CAR3) geçmiş getiriyi kesitsel regresyonda kapsıyor. Fiyat momentumunun kazanç momentumuna göre alfası negatif ve anlamlı (t=−2,55) [Ö]. Geçmiş performans kontrol edilince kazanç momentumunun **çöküşleri kayboluyor**, getirisi azalmıyor. | — | P | `skor=Min(dEP,0.3)*100+Min(Getiri("s6a","TL"),150)/10;` | **Yüksek** | Mimari: **temel momentum = sıralama, fiyat momentumu = kapı/ikincil** |
| B6 | **Hou, Xue & Zhang (2020)** "Replicating Anomalies", RFS 33(5):2019-2133 (NYSE kırılımlı, değer ağırlıklı) [Ö]. Sue yüksek-düşük farkı 1/6/12 ay: %0,46/0,16/0,08 ay başına (t=3,48/1,44/0,73). Abr: %0,70/0,33/0,23 (t=5,45/3,41/2,99). Momentum kategorisinde tekrar üretilebilme oranı %63,2. | — | P | Abr vekili: `Getiri("s1a","TL")-Getiri("s1a","TL","XUTUM")` (K10'da 2 aylık göreli güç var) | Orta | Uyarı: **taze rapor önemli, etki 1–3 ayda sönüyor** |
| B7 | **Livnat & Mendenhall (2006)**, JAR 44(1):177-205. Analist tahminli sürprizle kayma, zaman serisi (mevsimsel rastgele yürüyüş) sürprizinden belirgin büyük. Özel kalemler ve düzeltmeler farkı açıklamıyor. | Platformda analist verisi yok. **Fiyata ölçekli mevsimsel sürpriz (sueP) uygulanabilir tek seçenek.** | N | `sueP` (B1) | Yüksek | Ölçüm tercihi |
| B8 | **Jegadeesh & Livnat (2006)**, JAE 41(1-2):147-171. Kazanç sürprizi kontrol edildikten sonra da gelir sürprizi kayma üretiyor. Analistler gelir sürprizini 5–6 ayda sindiriyor. Çalışma kağıdı [Ö]: yüksek gelir+yüksek kazanç sürprizi grubu, düşük-düşük gruba göre 6 ayda +%8,41. | — | P (C32'de satış büyümesi > %50 alternatif koşul) | `realSatis=NetSatisBuyumeYillik()>Tufe(12);` | Yüksek | Kapı/bonus. **Satış teyitli kâr sıçraması** |
| B9 | **Goh & Jeon (2017)**, PBFJ 44:150-159, Kore. Pozitif kazanç haberli hisselerde PEAD, fiyat 52 haftalık zirveye yakınsa belirgin (çapalama). | Gelişmekte olan / Asya piyasası. Mevcut bulguyla uyumlu (K10: 52 hafta zirveye yakınlık faydalı). | P | `zirveSurpriz=IF(sueP>0 and Teknik.Indicator("C/HHV(H,252)","d")>0.85,1,0);` | Orta-Yüksek | Bonus (etkileşim) |

### C. Kârlılık değişimi (ΔROE, brüt kârlılık, kârlılık trendi)

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| C1 | **Hou, Xue & Zhang (2015)** "Digesting Anomalies", RFS 28(3):650-705. Piyasa, büyüklük, yatırım ve **kârlılık (en son çeyrek ROE)** faktörlü q-modeli anomalilerin çoğunu özetliyor. | — | T (K10 ROE > 5, ROE teyidi) | `OzsermayeKarlilikYillik()` | — | Mevcut |
| C2 | **ΔROE (dRoe)**, Hou-Xue-Zhang. 4 çeyreklik ROE değişimi ondalık farkı 1 ay tutmada %0,76/ay (t=5,43) [Ö]; NBER WP 23394 (2017) sürümü. Yayımlanmış sürümde (RFS 2020) Roe %0,68/0,42/0,23 (1/6/12 ay) [Ö]. | — | T (K10 skorunda ROE değişimi) | `dROE=IF(Ozsermaye()>0,OzsermayeKarlilikYillik()-OzsermayeKarlilikYillik("",-4),-99);` | Orta | Skor (zaten var; negatif öz kaynak koruması yeni) |
| C3 | **Novy-Marx (2013)**, JFE 108(1):1-28. Brüt kâr/aktif, getiri tahmininde PD/DD kadar güçlü. Kârlılığı değer stratejisine eklemek, özellikle büyük ve likit hisselerde iyileştiriyor. | **TR:** Gökçen (2026), BIR. Kârlılık 2005 sonrası anlamlı (2005 sonrası alfa %9,7 [Ö]). | N (brüt kâr fonksiyonu brief'te yok) | `fa=FAVOKYillik()/Aktifler();` (vekil) | Düşük-Orta | Bonus (düzey; dönüş stratejisinin özü değil) |
| C4 | **Akbas, Jiang & Koch (2017)**, TAR 92(5):1-32 (künye Crossref'ten). Kârlılık **trendi** (son çeyreklerdeki eğim) getiriyi tahmin ediyor. 1977–2012, yüksek-düşük trend ≈%0,83/ay, 5 yılda tersine dönme yok [İ] (CXO özeti, SSRN 429). | — | N | `trend=IF(OzsermayeKarlilikYillik()>OzsermayeKarlilikYillik("",-4) and OzsermayeKarlilikYillik("",-4)>OzsermayeKarlilikYillik("",-8),1,0);` | Orta | Bonus |
| C5 | **Fama & French (2000)**, J. Business 73(2):161-175. Kârlılık yılda ≈%38 ortalamaya dönüyor. Ortalamanın altındayken ve ortalamadan uzaklaştıkça dönüş daha hızlı (doğrusal değil). | — | N | `dEPc=Min(dEP,0.25);` | **Yüksek** | Uyarı + tavan. Zararlı firmalar yukarı daha hızlı döner (Profil 1 lehine); büyük sıçramalar kısmen geri verir (Profil 2 aleyhine) |
| C6 | **Soliman (2008)**, TAR 83(3):823-853 (künye Curtis vd. 2015 RAS kaynakçasından). DuPont: varlık devir hızındaki değişimin getiriyle ilişkisi [DY: bulgu birincil kaynaktan okunamadı]. | — | N | `devir=NetSatisBuyumeYillik()>0` (vekil; aktif devri fonksiyonu yok) | Düşük | — |

### D. Fiyata ölçeklenmiş kâr değişimi (ΔE/P), kazanç verimi sıçraması, F/K düşüşü

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| D1 | **Ball & Brown (1968)**, JAR 6(2):159-178; **Basu (1977)**, JF 32(3):663-682 (E/P etkisi). Kazanç değişiminin ve E/P'nin getiriyle ilişkisinin kökleri (künyeler RePEc'te doğrulandı; özet yok). | TR: değer (PD/DD) BIST'te en güçlü faktör (Gökçen 2026). | P (C32/K10'da E/P ≥ %2,5, F/K < 40) | `ep=NetKarYillik()/PD();` | — | Mevcut |
| D2 | **Fiyata ölçekli yıllık kâr değişimi (ΔE/P).** Ou & Penman (1989), JAE 11:295-329: tablo kalemlerinden tahmin edilen "bir yıl sonraki kazanç değişiminin yönü" ile 1973–1983'te 2 yıllık ≈%12,5, büyüklüğe göre düzeltilmiş ≈%7,0 getiri. Livnat & Mendenhall (2006) ve Bernard & Thomas (1989) ile aynı aile: **sürprizi fiyatla ölçekle**. | TR PEAD (B1). Platformda zaten hesaplanan alan var (`dd_forms` F2: ep0, ep4, ep8). | **N** (K10 EFK/FAVÖK değişimi yüzde bazlı; fiyata ölçekli net kâr değişimi yok) | `dEP=(NetKarYillik()-NetKarYillik("",-4))/PD();` | **Çok yüksek** | **Ana sıralama skoru.** Negatif tabanda tanımlı; "F/K'yı düşüren kâr sıçraması"nı doğrudan ölçer |
| D3 | **Koşu hızı (run-rate) E/P ivmesi.** Son iki çeyreğin yıllıklaştırılmış kârı TTM'ye göre yüksekse sıçrama henüz TTM'ye tam girmemiş demektir. **Literatürde birebir karşılığı yok:** B1/B2'den türetildi [türetim]. | — | N | `ivme=((NetKar("TL",0)+NetKar("TL",-1))*2-NetKarYillik())/PD();` | Orta | Bonus. Mevsimsellik riski: Q4 etkisi |
| D4 | **F/K sert düşüşü.** Sabit fiyatta F/K düşüşü = E/P artışı = ΔE/P > 0. Zararda F/K tanımsız ya da negatif olduğu için **F/K yerine E/P kullanılmalı**. Lynch (döngüseller): döngü zirvesinde F/K'nın küçülmesi beklenir; çok düşük F/K zirve kârı olabilir [İ]. | — | N | `fkDusus=dEP>0 and Getiri("s6a","TL")>0;` (kâr kaynaklı düşüş + fiyat teyidi) | Yüksek | Kapı/teyit |

### E. Piotroski F-Skor ve Mohanram G-Skor

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| E1 | **Piotroski (2000)**, JAR 38 (Ek):1-41. Yüksek PD/DD'li (çoğu sıkıntılı) firmalarda finansal güçlüleri seçmek getiriyi yılda en az %7 artırıyor. Uzun-kısa portföy 1976–1996'da yılda %23. Getiri küçük/orta, az işlem gören, analist takibi olmayan firmalarda yoğunlaşıyor ve açıklama günlerinde geliyor. Düşük skor −%9,6, yüksek skor +%13,4 [İ] (Chicago Booth Review). 9 sinyal: ROA>0, CFO>0, ΔROA>0, CFO>NI, Δkaldıraç<0, Δcari oran>0, hisse ihracı yok, Δbrüt marj>0, Δvarlık devri>0. | **TR:** Gülcan & Sakınç (2025), Fiscaoeconomia. BIST Sınai 145 firma, 2010–2022: F-Skor ile PD/DD, F/K ve getiri arasında pozitif ilişki. (Doğrudan uzun-kısa getiri testi bulunamadı.) | **T** (C32: F-Skor ≥ 7 kapısı) | Yeni kullanım, yalnız **değişim** sinyallerinden mini skor: `iyi=IF(OzsermayeKarlilikYillik()>OzsermayeKarlilikYillik("",-4),1,0)+IF(IsletmeFaaliyetlerdenNakitAkis()>0,1,0)+IF(IsletmeFaaliyetlerdenNakitAkis()>NetKarYillik(),1,0)+IF(ToplamBorcAktif()<ToplamBorcAktif("",-4),1,0)+IF(NetKarMarjiYillik()>NetKarMarjiYillik("",-4),1,0);` | Orta-Yüksek | Bonus ya da yumuşak kapı (`iyi>=3`). C32'nin ≥7 kapısı dönüş firmalarını (geçen yıl zarar → ROA>0 sinyali eksik) gereksiz eler |
| E2 | **Mohanram (2005)**, RAS 10(2-3):133-170. Düşük PD/DD (büyüme) hisseleri için GSCORE. Getirinin çoğu **kısa** taraftan geliyor. Bağlamsal yaklaşım: yüksek PD/DD'de geleneksel, düşükte büyüme odaklı analiz. | — | N | — | Düşük | Long-only stratejiye katkısı sınırlı. Bağlam dersi: dönüş hisseleri çoğu zaman "değer" tarafında |

### F. Sıkıntılı şirket anomalisi ve sıkıntı × iyileşme etkileşimi

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| F1 | **Dichev (1998)**, JF 53(3):1131-1147. İflas riski ödüllendirilmiyor. Yüksek iflas riskli firmalar 1980'den beri ortalamanın **altında** getiri veriyor. | Uluslararası: Eisdorfer, Goyal & Zhdanov (2018), FM [DY: sayfa açılamadı]. TR: sıkıntı-getiri testi bulunamadı. Yaman & Korkmaz (2023, MUFAD) sıkıntı skorlarını yalnız portföy optimizasyonunda kullanıyor (BIST TÜM, 2017–2022). | P (K10: NB/FAVÖK < 4) | `saglam=Ozsermaye()>0 and IF(FAVOKYillik()==null,1,IF(NetBorcFavokYillik()<5,1,0))==1;` | **Yüksek** | Kapı (dışlama) |
| F2 | **Campbell, Hilscher & Szilagyi (2008)**, JF 63(6):2899-2939. Muhasebe ve piyasa değişkenli dinamik logit. Yüksek başarısızlık olasılıklı hisseler 1981'den beri yüksek oynaklık, beta ve faktör yüklerine rağmen **zayıf** getiri veriyor. | — | N | `sikintiPiyasa=Getiri("s12a","TL")<-40 and Teknik.Indicator("C/HHV(H,252)","d")<0.4;` | Orta | Kapı (dışlama). "Düşen bıçak" filtresi (C32) bunun piyasa tarafını zaten kapsıyor (P) |
| F3 | **Altman (1968)**, JF 23(4):589-609. Z-skor (diskriminant analizi). | TR'de çok sayıda sektör uygulaması (DergiPark), getiri testi değil. | N | Tam Z hesaplanamıyor (işletme sermayesi ve birikmiş kâr fonksiyonu yok). Sade vekil F1 | Düşük | — |
| F3b | **Faiz karşılama (sıkıntı vekili).** Literatürde doğrudan getiri bulgusu açılmadı; Lynch'in dönüş kontrol listesinin "alacaklılara dayanabilir mi" sorusunun vekili. | — | N | `faizOk=IF(FAVOKYillik()==null,1,IF(FaizKarsilamaOrani()>1.5,1,0))==1;` | Orta | Kapı |
| F4 | **Griffin & Lemmon (2002)**, JF 57(5):2317-2336. En yüksek sıkıntı (Ohlson O-skor) grubunda yüksek-düşük PD/DD getiri farkı diğer firmalardakinin **iki katından fazla**. Üç faktör ve temeller açıklamıyor. Sıkıntılı firmalarda açıklama günü tersine dönüşleri en büyük. Etki küçük, az takip edilen firmalarda. | — | N | `pahaliSikinti=ToplamBorcAktif()>80 and PDDD()>4;` (birim kontrolü) | **Yüksek** | Kapı (dışlama): **sıkıntılı + pahalı = en kötü grup**. Sıkıntılı + ucuz + iyileşen = dönüş hedefi |
| F5 | **Avramov, Chordia, Jostova & Philipov (2013)**, JFE 108(1):139-159. Momentum, kredi riski ve oynaklık stratejileri kârını **sıkıntılı firmaları açığa satmaktan** alıyor. Değer stratejileri hayatta kalan sıkıntılı firmaları **almaktan**. Tahakkuk anomalisi tüm kredi riski gruplarında sağlam. | — | — | — | Yüksek | Uyarı: long-only momentum kısa bacağı alamaz. Dönüşte kazanç "hayatta kalan sıkıntılı + ucuz" bacağında |
| F6 | **Agarwal & Taffler (2008)**, Financial Management 37(3):461-484, İngiltere. Momentum büyük ölçüde sıkıntı riskini temsil ediyor; ikisi de sıkıntı bilgisine yetersiz tepkiden geliyor. | GOP: Çin ve İran'da benzer çalışmalar (arama sonucu, açılmadı) [DY]. | — | — | Orta | Uyarı: momentum kapısı aynı zamanda gizli bir sıkıntı filtresi |
| F7 | **Conrad, Kapadia & Xing (2014)**, JFE 113(3):455-475. Yüksek temerrüt riskli firmalar aynı zamanda "ikramiye" (aşırı pozitif getiri) olasılığı taşıyor. **İkramiye olasılığı yüksek hisseler anormal düşük ortalama getiri** veriyor. Etki kurumsal sahipliği düşük, arbitrajı zor hisselerde. | TR'de HA < 60 bulgusu ayrı bir konu; ancak düşük halka açıklık ve piyango talebi birlikte düşünülmeli. | N | `piyango=Getiri("s1a","TL")>60;` (ceza) | Orta | Ceza / uyarı: **ölü kedi + piyango talebi** |
| F8 | **Garlappi & Yan (2011)**, JF 66(3):789-822 (künye doğrulandı). Sıkıntı olasılığıyla beklenen getiri arasında "tümsek" biçimli ilişki ve sıkıntılılarda daha güçlü momentum [DY: özet açılamadı]. | — | — | — | Düşük | — |
| F9 | **Damodaran (2009)** "Valuing Declining and Distressed Companies" (SSRN 1428022; blog özeti açıldı). Gerileyen firma işaretleri: enflasyonun altında satış artışı, daralan marjlar, varlık satışları, kârı aşan temettü/geri alım, aşırı kaldıraç. İndirgenmiş nakit akımı değeri başarısızlık olasılığıyla düzeltilmeli. | — | N | `cokus=NetSatisBuyumeYillik()<Tufe(12) and FAVOKMarjiYillik()<FAVOKMarjiYillik("",-4);` | Orta | Kapı (dışlama): **"dönüş" etiketli ama işi küçülen firmalar** |

### G. Temel sinyaller, borç azaltma, marj, satış ivmesi, kazanç kalitesi (sahte kâr riski)

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| G1 | **Abarbanell & Bushee (1998)**, TAR 73(1):19-45 (SSRN 40740). Stok, alacak, brüt marj, satış gideri, yatırım harcaması, efektif vergi, denetim görüşü ve çalışan başına satış sinyalleri. 12 aylık büyüklüğe göre düzeltilmiş getiri %13,2. Getiri sonraki kazanç açıklamalarında yoğunlaşıyor, 1 yıldan sonra sürmüyor. | — | N | `dMarj=FAVOKMarjiYillik()-FAVOKMarjiYillik("",-4);` | Orta-Yüksek | Bonus ya da teyit: **marj genişlemesi** (Lynch: "maliyetler kesiliyor mu?") |
| G2 | **Sloan (1996)**, TAR 71(3):289-315. Kazancın kalıcılığı tahakkuk payı arttıkça düşüyor. Fiyatlar kazanca "saplanıyor". En düşük tahakkuk alım / en yüksek satım, ilk yıl %10,4 [Ö]. | **TR:** Ozkan & Kayalı (2015), BIR 15(2):115-125. Tüm örneklemde yanlış fiyatlama yok; **zarar edenler çıkarıldığında** tahakkuk anomalisi var, %18,58 anormal getiri. Kaya (2022), ICMR, 2005–2017: nakit akışı ve tahakkuk fiyatlara doğru yansımıyor; FF5 açıklıyor. | P (C32 F-Skor içinde CFO > NI) | `tah=(NetKarYillik()-IsletmeFaaliyetlerdenNakitAkis())/Aktifler();` | **Yüksek** | Ceza ya da kapı (`tah<0.10`). Dönüşte yeni kâr tahakkukla geliyorsa şüpheli |
| G3 | **Ball, Gerakos, Linnainmaa & Nikolaev (2016)**, JFE 121(1):28-45. **Nakit bazlı** faaliyet kârlılığı, tahakkuk içeren kârlılık ölçülerinden daha iyi getiri tahmin ediyor. | — | N | `nakitKar=IsletmeFaaliyetlerdenNakitAkis()/Aktifler();` | Orta | Kapı (`IsletmeFaaliyetlerdenNakitAkis()>0`) ya da bonus |
| G4 | **Burgstahler, Jiambalvo & Shevlin (2002)**, JAR 40(3):585-612. Fiyatlar özel kalemlerin gelecek kazanç etkisini diğer bileşenlerden fazla yansıtsa da **tam yansıtmıyor**. Yalnız özel kalemlerin işaretine dayalı strateji sonraki 4 çeyrekte anlamlı anormal getiri veriyor. | **BIST'e özgü özel kalem kaynakları (literatür değil, gözlem):** kur farkı gelir/gideri, yatırım faaliyetlerinden gelir (varlık ve iştirak satışı, gayrimenkul değerlemesi), vergi geliri, 2024 ve sonrası TMS 29 **net parasal pozisyon kazancı** (net parasal borçlu firmalarda kâr yaratır). | N | `opTeyit=IF(FAVOKYillik()==null,1,IF(NetKarYillik()<=FAVOKYillik() and FAVOKYillik()>FAVOKYillik("",-4),1,0));` | **Çok yüksek** | **Kapı.** Net kâr FAVÖK'ü aşıyorsa kâr büyük olasılıkla faaliyet dışı |
| G5 | **Freeman & Tse (1992)**, JAR 30(2):185-209. Beklenmeyen kazanca fiyat tepkisi doğrusal değil (künye RePEc'te). Büyük sürprizlerin kalıcılığı düşük olduğu için marjinal tepki azalıyor [DY: bu ayrıntı birincil kaynaktan okunamadı]. | — | N | `Min(dEP,0.3)` | Orta | Tavan |
| G6 | **Borç azaltma.** Piotroski Δkaldıraç < 0 sinyali (E1). Lynch: "alacaklıların baskısına dayanabilir mi, borç yapısı ne?" [İ]. Bağımsız bir "borç azaltma getirisi" çalışması bu taramada açılmadı. | Migros örneği: kontrol değişikliği + borç yapısı. | P (K10 NB/FAVÖK < 4) | `delev=ToplamBorcAktif()<ToplamBorcAktif("",-4);` | Orta | Bonus |

### H. Kontrol/sahiplik değişikliği, yeniden yapılanma, yönetim değişikliği

| # | Bulgu | Replikasyon / GOP / TR | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| H1 | **Denis & Denis (1995)**, JF 50(4):1029-1057. Zorunlu üst yönetim ayrılıklarından önce faaliyet performansında büyük düşüş, sonrasında **büyük iyileşme** var. Ayrılıklar çoğunlukla dış baskıyla (blok sahip aktivizmi, satın alma girişimi) oluyor. Ardından yeniden yapılanma ve kontrol işlemleri artıyor. | TR: bulunamadı. | N | Formülle yakalanamaz (yönetim verisi yok) | Düşük | Manuel olay listesi (sadelik ilkesine aykırı) |
| H2 | **Barclay & Holderness (1991)**, JF (cilt/sayı doğrulanmadı). Pazarlıklı blok satışları ortalama %20 (medyan %16) primle; blok işlemleri anormal fiyat artışıyla ilişkili [İ] (Holderness 2003, FRBNY EPR derlemesi). | **Migros (doğrulanan tarihler):** AEH'nin Moonlight/BC Partners'tan %40,25 dolaylı pay alımı 31/12/2014'te imzalandı (26 TL/pay). Rekabet Kurulu onayı 09/07/2015, devrin tamamlanması 15/07/2015 hedefi (Habertürk, Capital, BloombergHT). Brief'teki "2015 sonu" yerine **olay tarihi Temmuz 2015** alınmalı. | N | `HAOran()` yalnız düzey veriyor; geçmiş değer fonksiyonu brief'te yok | Düşük | Manuel. Kural fikri: kontrol değişimi ancak sonrasında **kâr dönüşü raporlanınca** sinyal |
| H3 | **Huson, Malatesta & Parrino (2004)**, JFE, "Managerial succession and firm performance" [DY: SSRN ve Scilit açılamadı]. | — | — | — | Düşük | — |
| H4 | **Greenblatt (1997)**, *You Can Be a Stock Market Genius* (Simon & Schuster tanıtımı). Özel durumlar: bölünmeler, yeniden yapılanmalar, birleşme menkul kıymetleri, rüçhan hakları, yeniden sermayelendirme, iflaslar, risk arbitrajı. | — | N | — | Düşük | Kural fikri: yeniden yapılanma sonrası **ilk temiz kâr çeyreği** = giriş tetiği |

### I. Uygulayıcı kaynaklar (yalnız kural fikri)

| Kaynak | Kural fikri | Taslak |
|---|---|---|
| **Peter Lynch**, *One Up on Wall Street*. Altı sınıf: yavaş büyüyenler, sağlamlar, hızlı büyüyenler, döngüseller, **dönüşler**, varlık oyunları (Trustnet). Dönüş kontrol listesi (Old School Value alıntısı) [İ]: nakit/borç, borç yapısı, zararda ne kadar dayanır, zarar eden birimlerden kurtuldu mu, iş geri geliyor mu, maliyet kesiliyor mu. | (1) borç/sıkıntı kapısı, (2) satış geri geliyor, (3) marj genişliyor, (4) döngüsellerde zirve kârına dikkat | `NetSatisBuyumeYillik()>Tufe(12) and FAVOKMarjiYillik()>FAVOKMarjiYillik("",-4)` |
| **Greenblatt** (H4) | Yeniden yapılanma ya da kontrol değişikliği + ilk temiz çeyrek | Manuel |
| **Damodaran** (F9) | Gerileyen firmayı dönüşten ayır: reel satış ve marj | `cokus` (F9) |

---

## 3. Profil eşlemesi (hangi sinyal hangi profile)

- **Profil 1 (dipten dönüş):**
  - `roeDonus` / `donus`: işaret değişimi.
  - Kapılar: `NetKar("TL",0)>0` (Li; Balakrishnan vd.), `Ozsermaye()>0` ve borç sınırı (Dichev; CHS; Griffin-Lemmon), `opTeyit` (Burgstahler).
  - Bonus: kısa zarar serisi `zararSeri<=2` (Joos-Plesko).
  - Teyit: momentum (Novy-Marx; CJL).
- **Profil 2 (kâr sıçraması):**
  - Ana skor `dEP`, `sueP` (Bernard-Thomas; Livnat-Mendenhall; HXZ).
  - Satış teyidi `realSatis` (Jegadeesh-Livnat), `opTeyit`.
  - Tavan `Min(dEP,0.25–0.3)` (Fama-French 2000; Freeman-Tse).
  - 52 hafta zirve etkileşimi (Goh-Jeon).
- **Ortak:** `dEP` iki profili de doğal olarak üst sıraya taşıyor. Zarardan kâra geçişte ΔE/P büyük çıkar; ayrı bir "dönüş" kapısı gerekmeyebilir, yalnız bonus yeterli olabilir.

---

## 4. Denenmemiş en iyi 10 fikir (sadelik ve uygulanabilirlik ağırlıklı sıra)

| Sıra | Fikir | Taslak | Rol | Dayanak |
|---|---|---|---|---|
| 1 | **ΔE/P ana skor** (TTM net kâr değişimi / piyasa değeri, tavanlı) | `dEP=Min((NetKarYillik()-NetKarYillik("",-4))/PD(),0.3);` | Sıralama | Bernard-Thomas 1989; Livnat-Mendenhall 2006; Ou-Penman 1989; HXZ dRoe; TR PEAD (Ahlatcıoğlu-Okay 2021) |
| 2 | **Sahte kâr kapısı:** net kâr ≤ FAVÖK ve FAVÖK artıyor (bankalar muaf) | `opTeyit=IF(FAVOKYillik()==null,1,IF(NetKarYillik()<=FAVOKYillik() and FAVOKYillik()>FAVOKYillik("",-4),1,0));` | Kapı | Burgstahler vd. 2002; Sloan 1996; TMS 29 / kur farkı gözlemi |
| 3 | **Son çeyrek kâr kapısı** (kalıcı zararı alma) | `NetKar("TL",0)>0` | Kapı | Li 2011; Balakrishnan vd. 2010; Joos-Plesko 2005 |
| 4 | **Dönüş bonusu:** TTM işaret değişimi ya da ROE negatif→pozitif, öz kaynak pozitif | `donus=IF(NetKarYillik()>0 and NetKarYillik("",-4)<=0 and Ozsermaye()>0,1,0);` | Bonus | Hayn 1995; Joos-Plesko 2005; kullanıcı tanımı |
| 5 | **Sıkıntı dışlama:** öz kaynak > 0 ve borç/FAVÖK sınırı | `saglam=Ozsermaye()>0 and IF(FAVOKYillik()==null,1,IF(NetBorcFavokYillik()<5,1,0))==1;` | Kapı | Dichev 1998; CHS 2008; Griffin-Lemmon 2002; Lynch |
| 6 | **Çeyreklik fiyat-ölçekli sürpriz (tazelik)** | `sueP=(NetKar("TL",0)-NetKar("TL",-4))/PD();` | Bonus / ikincil skor | Bernard-Thomas 1989/1990; HXZ 2020 (hızlı sönüm) |
| 7 | **Nakit teyidi** | `IsletmeFaaliyetlerdenNakitAkis()>0` (sıkıysa yalnız ceza) | Kapı (gevşetilebilir) | Piotroski 2000; Ball vd. 2016; Ozkan-Kayalı 2015 |
| 8 | **Reel satış teyidi** (işi büyüyen dönüş) | `NetSatisBuyumeYillik()>Tufe(12)` | Kapı / bonus | Jegadeesh-Livnat 2006; Joos-Plesko (satış büyümesi); Damodaran; Lynch |
| 9 | **Temel momentum sıralar, fiyat momentumu teyit eder** | `skor=dEP*100+IF(Getiri("s6a","TL")>0,2,0);` | Mimari | Novy-Marx 2015; Chordia-Shivakumar 2006; CJL 1996 |
| 10 | **Ardışık iyileşme:** iki çeyrek üst üste yıllık bazda artış | `ardisik=IF(NetKar("TL",0)>NetKar("TL",-4) and NetKar("TL",-1)>NetKar("TL",-5),1,0);` | Bonus | Bernard-Thomas 1990; Akbas vd. 2017 |

**Yedekler:**
- (11) 52 hafta zirve × pozitif sürpriz etkileşimi (Goh-Jeon 2017).
- (12) Koşu hızı E/P ivmesi (D3).
- (13) F-Skor'un 5 değişim sinyalinden mini "iyileşme" skoru (E1). C32'nin ≥7 kapısı yerine.
- (14) Uzun zarar serisi cezası `zararSeri>=3` (A2).
- (15) Çöküş dışlama `cokus` (F9).

**Örnek sade iskelet (test edilmemiş, yalnız fikir bütünlüğü için; sözdizimi sitede denenmeli):**
```
k=NetKar("TL",0)>0 and Ozsermaye()>0 and IF(FAVOKYillik()==null,1,IF(NetKarYillik()<=FAVOKYillik(),1,0))==1;
dEP=Min((NetKarYillik()-NetKarYillik("",-4))/PD(),0.3);
skor=IF(k,dEP*100+IF(NetKarYillik("",-4)<=0,3,0)+IF(Getiri("s6a","TL")>0,2,0),-999);
```
Bonus katsayıları (3, 2) keyfi. Ön kayıtlı test planında ızgara yerine tek bir değer seçilip sabitlenmeli.

---

## 5. Uyarılar: literatürün kırmızı bayrakları

1. **Sıkıntılı şirket anomalisi:** Yüksek iflas ya da başarısızlık riskli hisseler ortalamada **düşük** getiri veriyor (Dichev 1998; Campbell-Hilscher-Szilagyi 2008). "Dipteki" hisse kendiliğinden ucuz değil. Kazanç yalnız **ucuz ve hayatta kalan** sıkıntılılarda (Griffin-Lemmon 2002; Avramov vd. 2013). Sıkıntılı ve pahalı (yüksek PD/DD) en kötü grup.
2. **Kalıcı zarar yanılgısı:** Piyasa zararları geçici sanıyor; kalıcı zarar eden firmalar sonraki yıl düşük getiri veriyor (Li 2011). Uç zarar açıklayanlar uç kâr açıklayanların gerisinde kalıyor (Balakrishnan vd. 2010). **Dönüşü öngörerek değil, raporda görerek al.**
3. **Sahte/tek seferlik kâr:** Özel kalemler fiyata tam yansımıyor (Burgstahler vd. 2002). Tahakkuk payı yüksek kâr kalıcı değil (Sloan 1996). BIST'te tahakkuk anomalisi kâr eden firmalarda %18,58 (Ozkan-Kayalı 2015). BIST riskleri: kur farkı dönüşleri, varlık satış kârı, değerleme artışı, 2024 ve sonrası **TMS 29 net parasal pozisyon kazancı**. FAVÖK ve nakit teyidi şart.
4. **Ortalamaya dönüş:** Kârlılık yılda ≈%38 ortalamaya dönüyor, ortalamadan uzaklaştıkça daha hızlı (Fama-French 2000). Çok büyük sıçramaların bir kısmı geri verilir. Lynch: döngüsellerde en düşük F/K çoğu zaman zirve kârıdır. **ΔE/P'ye tavan** koy, döngüsel sektörlerde zirve riskini kabul et.
5. **Hızlı sönüm ve azalan etki:** SUE etkisi 1 ayda güçlü, 6–12 ayda zayıf [Ö] (HXZ 2020). ABD'de PEAD zamanla azalıyor (Fink 2020 derlemesi). Türkiye'de 60 günlük fark ≈%2,9 ve küçük firmalarda daha güçlü (Ahlatcıoğlu-Okay 2021). Beklenti mütevazı tutulmalı; etki likit olmayan küçük hisselerde toplanabilir.
6. **Ölü kedi sıçraması ve piyango hisseleri:** Sıkıntılı hisseler "ikramiye" olasılığı nedeniyle aşırı fiyatlanıyor ve düşük getiri veriyor (Conrad-Kapadia-Xing 2014). Momentum, sıkıntı riskini temsil edebilir (Agarwal-Taffler 2008). Momentum kârının bir kısmı sıkıntılıların açığa satılmasından geliyor (Avramov vd. 2013). Long-only stratejide bu bacak yok. Fiyat sıçraması **temel teyit olmadan** sinyal sayılmamalı.
7. **Ölçüm tuzakları:**
   - Negatif öz kaynakta ROE işareti yanıltır.
   - Negatif ya da sıfıra yakın tabanda büyüme yüzdesi anlamsız; ΔE/P kullan.
   - Yüksek enflasyonda nominal kâr artışı "sıçrama" gibi görünür. Mutlak eşiklerde `Tufe(12)` ile reelleştir. ΔE/P kesitsel sıralamada bu sorunu kısmen nötrler.
   - TMS 29 geçişi (2023 sonu raporları ve 2024 karşılaştırmaları) 4 çeyreklik farklarda kırılma yaratabilir.
   - Bankalarda FAVÖK yok.
8. **Kontrol değişikliği olayları:** Literatür, yönetim ya da kontrol değişikliği sonrası performans iyileşmesini gösteriyor (Denis-Denis 1995). Ancak platformda bu veri yok. Manuel olay listesi hem sadeliği bozar hem geriye dönük seçim yanlılığı (Migros gibi bilinen başarılar) riski taşır.

---

## 6. Kaynakça ve doğrulama durumu

Açılan sayfa / doğrulama yolu köşeli parantezde. **[DY]** = açılamadı ya da içerik doğrulanamadı.

**Zarar ve dönüş**
- Hayn, C. (1995). The information content of losses. JAE 20(2):125-153. [ScienceDirect özet: https://www.sciencedirect.com/science/article/pii/0165410195003972]
- Joos, P. & Plesko, G. (2005). Valuing loss firms. TAR 80(3):847-870. [SSRN 562043 özeti; MIT yazar sayfası; Crossref künyesi]
- Darrough, M. & Ye, J. (2007). Valuation of loss firms in a knowledge-based economy. RAS 12(1):61-93. [Springer: https://link.springer.com/article/10.1007/s11142-006-9022-z]
- Li, K. K. (2011). How well do investors understand loss persistence? RAS 16(3):630-667. [Springer: https://link.springer.com/article/10.1007/s11142-011-9157-4; ÇK PDF: https://care-mendoza.nd.edu/assets/152066/li.pdf]
- Balakrishnan, K., Bartov, E. & Faurel, L. (2010). Post loss/profit announcement drift. JAE 50(1):20-41. [EconPapers]
- Wu, H. (2017). Probability of loss reversal in Australia. Australian Journal of Management 42(4). [SAGE özet]

**PEAD ve kazanç momentumu**
- Bernard, V. & Thomas, J. (1989). JAR 27 (Ek):1-36. [künye ve DOI 10.2307/2491062: https://iangow.github.io/far_book/pead.html (çevrimiçi ders kitabı, PEAD bölümü); rakamlar Fink 2020'den [İ]]
- Bernard, V. & Thomas, J. (1990). JAE 13(4):305-340. [RePEc]
- Fink, J. (2020). A review of the post-earnings-announcement drift. Uni Graz WP 2020-04. [PDF: https://static.uni-graz.at/fileadmin/sowi/Working_Paper/2020-04_Fink.pdf; yayımlanmış hali JBEF 29 (2021): künye RePEc arama sonucundan]
- Chan, L., Jegadeesh, N. & Lakonishok, J. (1996). Momentum strategies. JF 51(5):1681-1713. [EconPapers]
- Chordia, T. & Shivakumar, L. (2006). Earnings and price momentum. JFE 80(3):627-656. [ScienceDirect özet]
- Novy-Marx, R. (2015). Fundamentally, momentum is fundamental momentum. NBER WP 20984. [Yazar PDF: https://mysimon.rochester.edu/novy-marx/research/FMFM.pdf]
- Hou, K., Xue, C. & Zhang, L. (2020). Replicating anomalies. RFS 33(5):2019-2133. [OUP özet; yazar PDF (RFS sürümü); NBER WP 23394]
- Livnat, J. & Mendenhall, R. (2006). JAR 44(1):177-205. [EconPapers]
- Jegadeesh, N. & Livnat, J. (2006). Revenue surprises and stock returns. JAE 41(1-2):147-171. [ScienceDirect; ÇK PDF NYU]
- Goh, J. & Jeon, B.-H. (2017). PEAD and 52-week high: Evidence from Korea. PBFJ 44:150-159. [RePEc]

**Kârlılık**
- Hou, K., Xue, C. & Zhang, L. (2015). Digesting anomalies. RFS 28(3):650-705. [OUP]
- Novy-Marx, R. (2013). The other side of value. JFE 108(1):1-28. [EconPapers]
- Akbas, F., Jiang, C. & Koch, P. (2017). The trend in firm profitability and the cross-section of stock returns. TAR 92(5):1-32. [Crossref künyesi; rakamlar CXO Advisory'den [İ]; SSRN 429]
- Fama, E. & French, K. (2000). Forecasting profitability and earnings. J. Business 73(2):161-175. [EconPapers]
- Soliman, M. (2008). The use of DuPont analysis by market participants. TAR 83(3):823-853. [künye Curtis vd. 2015 RAS kaynakçası; bulgu [DY]]

**ΔE/P ve temel sinyaller**
- Ball, R. & Brown, P. (1968). JAR 6(2):159-178. [RePEc]
- Basu, S. (1977). JF 32(3):663-682. [RePEc]
- Ou, J. & Penman, S. (1989). JAE 11:295-329. [Columbia Business School sayfası]
- Abarbanell, J. & Bushee, B. (1998). Abnormal returns to a fundamental analysis strategy. TAR 73(1):19-45. [SSRN 40740]
- Sloan, R. (1996). TAR 71(3):289-315. [makale PDF kopyası, JSTOR başlığıyla; 10,4 rakamı [Ö]]
- Ball, R., Gerakos, J., Linnainmaa, J. & Nikolaev, V. (2016). JFE 121(1):28-45. [RePEc]
- Burgstahler, D., Jiambalvo, J. & Shevlin, T. (2002). JAR 40(3):585-612. [RePEc]
- Freeman, R. & Tse, S. (1992). JAR 30(2):185-209. [RePEc künye; içerik ayrıntısı [DY]]

**F/G-Skor**
- Piotroski, J. (2000). JAR 38 (Ek):1-41. [RePEc künye; SSRN 249455 özeti; Chicago Booth Review [İ]]
- Mohanram, P. (2005). RAS 10(2-3):133-170. [Springer]

**Sıkıntı**
- Dichev, I. (1998). JF 53(3):1131-1147. [CAS özet sayfası]
- Campbell, J., Hilscher, J. & Szilagyi, J. (2008). JF 63(6):2899-2939. [RePEc]
- Altman, E. (1968). JF 23(4):589-609. [EconPapers]
- Griffin, J. & Lemmon, M. (2002). JF 57(5):2317-2336. [EconPapers]
- Avramov, D., Chordia, T., Jostova, G. & Philipov, A. (2013). JFE 108(1):139-159. [EconPapers]
- Agarwal, V. & Taffler, R. (2008). Financial Management 37(3):461-484. [RePEc]
- Conrad, J., Kapadia, N. & Xing, Y. (2014). JFE 113(3):455-475. [RePEc]
- Garlappi, L. & Yan, H. (2011). JF 66(3):789-822. [RePEc künye; yazar sayfası; özet [DY]]
- Eisdorfer, A., Goyal, A. & Zhdanov, A. (2018). Financial Management. [DY]
- Damodaran, A. (2009). Valuing declining and distressed companies. SSRN 1428022. [blog özeti açıldı]

**Kontrol ve yönetim değişikliği**
- Denis, D. J. & Denis, D. K. (1995). JF 50(4):1029-1057. [EconPapers]
- Barclay, M. & Holderness, C. (1991). Negotiated block trades and corporate control. JF. [Holderness 2003, FRBNY Economic Policy Review [İ]]
- Huson, M., Malatesta, P. & Parrino, R. (2004). JFE. [DY]
- Migros pay devri tarihleri: Capital (imza 31/12/2014, 26 TL/pay); BloombergHT; Habertürk 10/07/2015 (Rekabet Kurulu onayı 09/07/2015, devir hedefi 15/07/2015).

**Türkiye**
- Ahlatcıoğlu, A. & Okay, N. (2021). Post-earnings announcement drift: Evidence from Turkey. Borsa Istanbul Review 21(1):92-103. [ScienceDirect]
- Ahlatcıoğlu, A. & Okay, N. (2019). Journal of Capital Markets Studies 3(2):179-187. [RePEc]
- Şimşek, H. & Yıldırım, D. (2020). İyi ve kötü kazanç ilanlarına piyasanın tepkisi: Borsa İstanbul'da bir uygulama. Muhasebe Bilim Dünyası Dergisi. [DergiPark]
- Ozkan, N. & Kayalı, M. M. (2015). The accrual anomaly: Evidence from Borsa Istanbul. BIR 15(2):115-125. [RePEc]
- Kaya, E. (2022). Cash flow and accrual anomalies: Evidence from Borsa Istanbul. Indonesian Capital Market Review 14(1). [dergi sayfası]
- Gökçen, U. (2026). Factor investing in the Turkish equity market. Borsa Istanbul Review, makale 100884. [ScienceDirect özet; alt rakamlar [Ö]]
- Gülcan, K. G. & Sakınç, S. Ö. (2025). Piotroski F Skor ile piyasa temelli performans arasındaki ilişkinin Borsa İstanbul'da incelenmesi. Fiscaoeconomia. [DergiPark]
- Yaman, S. & Korkmaz, T. (2023). Optimum portföy seçimi ve finansal başarısızlık modelleri. Muhasebe ve Finansman Dergisi 99. [DergiPark]

**Uygulayıcı**
- Lynch, P. *One Up on Wall Street*. [altı sınıf: Trustnet; dönüş kontrol listesi alıntısı: Old School Value [İ]]
- Greenblatt, J. (1997). *You Can Be a Stock Market Genius*. [Simon & Schuster tanıtım sayfası]

---

## 7. Dürüst sınırlar

- **Arama hacmi:**
  - Bu ajan ≈45 web araması ve ≈80 sayfa açma yaptı. Oturumun ortak arama kotası (200) tarama sonunda doldu; son planlanan arama (BIST'te Piotroski uzun-kısa getiri testi) yapılamadı.
  - Doğrulanan kaynak: ≈45 (yayıncı/indeks özet sayfası açıldı).
  - Kısmi: 7 (yalnız künye ya da ikincil kaynak). Garlappi-Yan, Freeman-Tse, Soliman, Barclay-Holderness, Lynch, Bernard-Thomas 1989 rakamları, Akbas vd. rakamları.
  - [DY]: 4. Huson vd. 2004, Eisdorfer vd. 2018, İngiltere zarar kalıcılığı (ABR 2016), Agarwal-Taffler GOP replikasyonları.
- **Açılamayan siteler:**
  - Wiley Online Library (403); SSRN ve ResearchGate (ilk birkaç istekten sonra 429).
  - Crossref API (2 sorgudan sonra hız sınırı; Soliman sorgusu reddedildi; uyarı gereği tekrar denenmedi).
  - Semantic Scholar (403); Taylor & Francis (403); AAA yayın sitesi (403); global-q/theinvestmentcapm alt sayfaları (robots).
- **Sürüm farkı:** Bazı rakamlar çalışma kağıdı sürümlerinden alındı ve yayımlanmış sürümden farklı olabilir: Li 2011 ÇK, Jegadeesh-Livnat ÇK, HXZ NBER 2017'deki dRoe. Bunlar [Ö] etiketli.
- **Türkiye boşlukları:**
  - BIST'te **zarardan kâra geçişin** sonraki getirisini doğrudan test eden bir çalışma bulunamadı.
  - BIST'te sıkıntı riski-getiri (Dichev/CHS türü) testi bulunamadı.
  - F-Skor'un uzun-kısa getiri testi bulunamadı; yalnız panel ilişki çalışması var.
  - Türkiye kanıtı PEAD, tahakkuk anomalisi ve faktör (kârlılık, momentum, değer) düzeyinde.
- **Uydurma yok:** Taslaklardaki eşikler (0,3 tavan; 0,85 zirve oranı; NB/FAVÖK < 5; borç/aktif > 80; bonus 2–3 puan) literatürden değil, **başlangıç değeri önerisi**. Ön kayıtlı testte sabitlenmeli.
- **Platform sözdizimi:** `FAVOKYillik("",-4)`, `FAVOKMarjiYillik("",-4)`, `NetKarMarjiYillik("",-4)` ve `IsletmeFaaliyetlerdenNakitAkis()` döneminin sitede denenmesi gerekiyor. Brief'te bu parametreli kullanım örneği yok.
