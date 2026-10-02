# LIT_B — Teknik / Piyasa Onayı: Dönüş Hikâyesine "Piyasanın İnanması"

**Strateji:** Dipten Dönüş (BIST TÜM, 5 hisse, eşit ağırlık, aylık, her zaman yatırımda)
**Ajan:** B (fiyat momentumu × kazanç momentumu, trend/hacim onayı, momentum çöküşleri)
**Tarih:** 01/10/2026
**İşaretler:** [Ö] = rakam PDF'in araçla çıkarılmış özetinden okundu (tablo satırı tek tek kontrol edilemedi) · [DY] = kaynak açılamadı/doğrulanamadı · Durum: T = denendi (K10/C32), P = kısmen, N = denenmedi

---

## 0. Beş cümlelik özet

1. **Fiyat momentumu büyük ölçüde kazanç momentumunun gölgesi:** Chordia & Shivakumar (2006) ve Novy-Marx (2015) fiyat momentumunun kazanç sürprizi tarafından kapsandığını gösteriyor. Fiyat ve kazanç birlikte kullanıldığında sinyal daha güçlü: Chan ve ark. (1996). Duyuru tepkisi (EAR) ile kazanç sürprizi (SUE) birleşince yıllık yaklaşık %11 anormal getiri elde ediliyor (Brandt ve ark. 2008 [Ö]).
2. **Türkiye'de saf fiyat momentumu kırılgan, uzun vadeli dönüş (karşıt etki) güçlü:** Griffin ve ark. (2003) Türkiye için kazanan−kaybeden farkını −%1,50/ay buluyor [Ö]. Bildik & Gülay, Alper & Aydoğan ve Ünal'ın çalışmaları da karşıt etkiye işaret ediyor. Buna karşılık 2005–2024 için pozitif momentum alfası raporlanıyor (Gökçen 2026 [Ö]) ve PEAD (kâr duyurusu sonrası fiyat kayması) BIST'te de var (Ahlatcıoğlu & Okay 2021). Kanıta en uygun biçim **"temelle (haberle) desteklenen momentum"**.
3. **Dipten dönüş anları, momentum stratejilerinin çöktüğü anlarla aynı:** Daniel & Moskowitz (2016) ve Cooper ve ark. (2004) bunu gösteriyor. 6–12 aylık momentum ve MA200 kapıları dönüşün ilk ayağını kaçırır, bu yüzden bir **piyasa durumu anahtarı** gerekiyor.
4. **Teknik kuralların çoğu veri madenciliğine açık:** BLL'nin (1992) kuralları örneklem dışında anlamsızlaşıyor (Sullivan ve ark. 1999). BIST'te de teknik kuralların maliyet sonrası kazancı ihmal edilebilir düzeyde. Bu yüzden az parametre ve literatürde sabitlenmiş eşikler kullanılmalı.
5. **Uygulayıcı sistemlerin kendi akademik kanıtı yok ya da zayıf:** Weinstein, Minervini, CAN SLIM ve Darvas bu gruba giriyor. Parçalarının (52 hafta zirvesi, hareketli ortalama, göreli güç, kâr sıçraması, hacim şoku) kanıtı ise var.

---

## 1. Kalem kalem bulgular

### A. Fiyat momentumu × kazanç momentumu etkileşimi

| # | Bulgu (yazar, yıl, örneklem, dönem, etki) | Replikasyon / GP / Türkiye | Durum | Platform taslağı (tek satır) | Öncelik | Rol |
|---|---|---|---|---|---|---|
| A1 | **Chan, Jegadeesh & Lakonishok (1996)**, JF 51(5):1681–1713. NYSE/AMEX/Nasdaq, 1977–1993. Geçmiş getiri ve geçmiş kazanç sürprizi, birbirini kontrol ettikten sonra bile gelecekteki getiriyi ayrı ayrı öngörüyor. Analist tahminleri yavaş ayarlanıyor, özellikle kötü performanslı hisselerde. Takip eden 6 ayda fark: R6 10.–1. ondalık %8,8; SUE %6,8. 3×3 iki yönlü sıralamada (getiri+SUE) en iyi−en kötü %8,1/6 ay ve ilk yılda ≈%11,5 (tek boyutlu 9.–2. ondalık %6,3) [Ö]. Güçlü fiyat+kazanç momentumlu hisselerde 2–3. yılda belirgin tersine dönme yok [Ö]. | Chordia-Shivakumar 2006 ve Novy-Marx 2015 bulguyu genişletiyor. Türkiye'de iki yönlü sıralama yok; PEAD var (A4). | P (K10 kâr ivmesi ile 6 ay momentumu birleştiriyor ama dönüş evreninde değil) | `k=IF(NetKarYillik()>NetKarYillik("",-4),1,0)*IF(Getiri("s6a","TL")>Getiri("s6a","TL","XUTUM"),1,0);` | Yüksek | Kapı |
| A2 | **Chordia & Shivakumar (2006)**, JFE 80(3):627–656. Fiyat momentumu, kazanç momentumunun sistematik bileşeni tarafından yakalanıyor. Yüksek−düşük kazanç sürprizi portföyü, geçmiş getirinin öngörü gücünü kapsıyor. Portföy getirisi GSYH, sanayi üretimi ve enflasyon gibi gelecekteki makro değişkenlerle ilişkili. | ABD. Türkiye'de test yok. | P | `s=OzsermayeKarlilikYillik()-OzsermayeKarlilikYillik("",-4);` (ana sıralama temel değişim; fiyat yalnızca onay) | Yüksek | Sıralama (temel) + kapı (fiyat) |
| A3 | **Novy-Marx (2015)**, NBER WP 20984 (1975–2012). Kesitsel regresyonda kazanç sürprizi (SUE, CAR3) geçmiş getiriyi kapsıyor. UMD %0,64/ay (t=3,03); SUE %0,59 (t=7,14); CAR3 %0,53 (t=8,42). Maliyet sonrası Sharpe: UMD 0,33, SUE 0,55 [Ö]. Fiyat momentumundan arındırılmış kazanç momentumu daha az oynak ve çöküşsüz. | Dergi yayını bulunamadı (WP). Türkiye'de yok. | P | Fiyat momentumu skora ağır girmesin, "çelişmeme" kapısı olsun: `fk=IF(Getiri("s6a","TL")>0,1,0);` | Yüksek | Kapı (gevşek) |
| A4 | **Brandt, Kishore, Santa-Clara & Venkatachalam (2008)**, SSRN WP 909563, 1987–2004. Kâr duyurusu etrafındaki 3 günlük anormal getiriye (EAR) göre kurulan strateji yıllık %6,3, SUE stratejisi %5,6 anormal getiri veriyor. İkisi büyük ölçüde bağımsız; birlikte yıllık ≈%11 [Ö]. **"Piyasanın inanması"nın en doğrudan ölçüsü bu.** | **Türkiye: Ahlatcıoğlu & Okay (2021)**, Borsa Istanbul Review 21(1):92–103, BIST 2007–2018. PEAD var: 60 günlük fark %2,9 (zaman serisi/analist sürprizi) ve %2,2 (EAR) [Ö]. Büyük firmalarda daha küçük. | P (bildirim tarihi yoksa en yakın vekil, K10'daki 2 ay göreli güç kapısı) | `ear=Getiri("s2a","TL")-Getiri("s2a","TL","XUTUM");` (dönüş çeyreğinden sonraki 1–2 ayda >0) | Yüksek | Kapı / bonus |
| A5 | **Ahmed & Safdar (2018)**, Accounting & Finance 58(S1):3–43. Temeller geçmiş fiyatla tutarsızsa momentum tersine dönüyor. Finansal tablo analiziyle filtrelenmiş momentum, saf momentumu zamanın %80'inden fazlasında geçiyor. | ABD. | N | `tut=IF(Getiri("s6a","TL")>0,IF(OzsermayeKarlilikYillik()>OzsermayeKarlilikYillik("",-4),1,0),0);` | Yüksek | Kapı |
| A6 | **Chan (2003)**, JFE 70(2):223–260, 1980–1999. Kamuya açık haber sonrası fiyat aynı yönde kaymaya devam ediyor (özellikle kötü haberde, 12 aya kadar). Haber olmadan gelen uç hareketler ise ilk ayda tersine dönüyor (≈−%2) [Ö]. **Savor (2012)**, JFE 106(3):635–659: analist raporuyla gelen şoklar sürüyor, bilgisiz şoklar tersine dönüyor; süreklilik yalnızca fiyat ve tavsiye yönü aynıysa var. | İki bağımsız ABD çalışması aynı yönde. | N | `hk=IF(Getiri("s1a","TL")>25,IF(NetKarYillik()>NetKarYillik("",-4),1,0.8),1);` (çarpan: haberi olmayan sert 1 aylık sıçramayı cezalandır) | Orta | Ceza/çarpan |
| A7 | **Huang, Zhang, Zhou: "Twin Momentum"** (SSRN 2894068). Temel ve fiyat momentumunun birleşimi. | — | — | — | — | **[DY]** PDF 403 verdi; rakam yok. |

### B. Değer + momentum ("ucuz ve iyileşen")

| # | Bulgu | Replikasyon / GP / Türkiye | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| B1 | **Asness (1997)**, FAJ 53(2):29–36. Değer ve momentum hisseler arasında negatif korelasyonlu ama ikisi de getiriyi bağımsız olarak öngörüyor. **Değer en güçlü, düşük momentumlu (kaybeden) hisselerde**; momentum en güçlü pahalı hisselerde. Dönüş adayları çoğunlukla geçmişin kaybedenleri olduğundan bu kümede ucuzluk sıralaması daha çok işe yarar. | AMP 2013 bulguyu globale taşıyor (B2). | P (C32 FD/FAVÖK kullanıyor ama dönüş evreninde değil) | `ep=NetKarYillik()/PD();` (yalnızca dönüş/sıçrama kümesi içinde sırala) | Orta | Sıralama |
| B2 | **Asness, Moskowitz & Pedersen (2013)**, JF 68(3):929–985. 8 piyasa/varlık sınıfı, 1972–2011; değer ve momentum primi her yerde var. Hisse piyasalarında aralarındaki korelasyon ≈ −0,60; 50/50 küresel kombinasyonun Sharpe oranı 1,42 [Ö]. | Türkiye örneklemde yok. **Gökçen (2026)**, Borsa Istanbul Review: değer primi yılda %17'nin üzerinde (1994–2024) ve 2005 sonrası alfa %12,52 [Ö]. Momentum "karışık" (H bölümü). | P | `vm=(NetKarYillik()/PD())*Teknik.Indicator("C/HHV(H,252)","d");` (ucuz **ve** zirveye yakın, yani piyasanın inandığı) | Yüksek | Sıralama |

### C. 52 hafta zirvesi, dipten uzaklık, uzun vadeli dönüş

| # | Bulgu | Replikasyon / GP / Türkiye | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| C1 | **George & Hwang (2004)**, JF 59:2145–2176, 1963–2001. 52 hafta zirvesine yakınlık, momentum kârının büyük kısmını açıklıyor. 6/6 strateji: 52H %0,45/ay, JT %0,48, MG (sektör) %0,45 [Ö]. 52H getirisi kalıcı, yani uzun vadede tersine dönmüyor; JT ise sonraki 12 ayda −%0,13/ay geri veriyor [Ö]. 52H stratejisi Ocak'ta sert negatif [Ö]. | **Liu, Liu & Ma (2011)**, JIMF 30(1):180–204: 20 ülkenin 18'inde kârlı, 10'unda anlamlı, uzun vadede tersine dönmüyor; ancak işlem maliyeti sonrası çoğunda anlamsız (Türkiye yok). **Türkiye: Özkan (2021)**, MAKÜ İİBF 8(2):704–719, BIST 2007–2016: 52H portföyleri pozitif ama istatistiksel olarak anlamsız. Kullanıcının kendi testinde faydalı bulundu. | T | `z=Teknik.Indicator("C/HHV(H,252)","d");` | (T) | Sıralama |
| C2 | **Bhootra & Hur (2013)**, JBF 37(10):3773–3782. 52H zirvesine **yakın zamanda** ulaşan hisseler, zirveyi uzun süre önce görenlerden daha iyi performans gösteriyor (en iyi−en kötü ondalık %0,70/ay). Bu zamanlama bilgisi, 52H yakınlık stratejisinin getirisini ikiye katlıyor. | ABD. | N | Dönüş hisseleri için 6 ay varyantı: `tz=IF(Teknik.Indicator("HHV(H,21)/HHV(H,126)","d")>=1,1,0);` (6 ay zirvesi son 1 ayda yapılmış = tabandan kırılım) | Yüksek | Bonus |
| C3 | **Huddart, Lang & Yetman (2009)**, Management Science 55(1):16–31. Fiyat geçmiş işlem aralığının üst ya da alt sınırını geçtiğinde hacim belirgin artıyor. Aralık ne kadar uzun süredir geçilmemişse etki o kadar büyük; küçük firmalarda daha güçlü; geçişin ardından pozitif getiri geliyor. | ABD. | N | `kr=IF(Teknik.Indicator("C/HHV(H,252)","d")>0.97,IF(Teknik.Indicator("Mov(V,5,S)/Mov(V,60,S)","d")>1.5,1,0),0);` | Orta | Bonus |
| C4 | **Jeon & Byun (2023)**, FAJ 79(2). Momentum 52H yakınlığına göre nötrleştirildiğinde çöküşler büyük ölçüde azalıyor: Temmuz 1932'de WML −%74,06 iken −%9,61; en kötü ay −%74 → −%24; çarpıklık −1,89 → 0,13; Sharpe ≈%80 artış [Ö]. Çöküş riski 52H'den uzaktaki kaybedenlerin sert toparlanmasından geliyor. Yalnızca alım yapan bir strateji için anlamı: toparlanmada önce dipteki hisseler koşar. | ABD. | P (K10'da hem 52H hem 6 ay momentum var) | Momentum bileşeni olarak ham getiri yerine `z` (C1) kullan | Orta | Sıralama tercihi |
| C5 | **De Bondt & Thaler (1985)**, JF 40(3):793–805, NYSE 1926–1982. Son 36 ayın kaybedenleri sonraki 36 ayda piyasayı ≈%19,6 geçiyor; kazananlar ≈%5,0 geride kalıyor; fark %24,6 (t=2,20). Kaybedenlerin getirisi Ocak'ta yoğunlaşıyor (ilk ay %8,1) [Ö]. **Jegadeesh & Titman (1993)**: momentum getirisi 12. ayda %9,5 iken 36. ayda ≈%4'e iniyor [Ö]. | **Türkiye'de güçlü:** Bildik & Gülay (SSRN WP 2002 / IRF 2007), İMKB 1991–2000: kaybedenler kazananları ≈%15/yıl (%1,14/ay) geçiyor. Alper & Aydoğan (2017), MFD, 2001–2015: 1 yıllık vadede kaybedenler ≈%29, 5 yıllıkta ≈%19 önde [Ö]. Ünal (2021), IJMEB, 1997–2020: en iyi %20'lik dilim sonraki dönemde ortalamanın altında; karşıt strateji işliyor. | N | `b3=IF(Teknik.Indicator("C/HHV(H,756)","d")<0.6,1,0)*IF(Teknik.Indicator("C/Mov(C,200,S)","d")>1,1,0);` (3 yıl zirvesinden derin düşüş **ve** trend dönmüş) | Yüksek | Bonus (tek başına asla kapı değil: düşen bıçak riski) |
| C6 | **Dipten uzaklık** (`C/LLV(L,252)`). Minervini şablonu ≥1,30 öneriyor; C32 ≥1,5 kullanıyor; kullanıcı 1,0–1,3 aralığını faydalı buldu. Belirli bir eşik için akademik kanıt bulunamadı. Yakın kavram: alt sınırın geçilmesi hacim artışıyla birlikte geliyor (Huddart ve ark. 2009). | — | T | `ll=Teknik.Indicator("C/LLV(L,252)","d");` | (T) | Kapı |

### D. Trend filtreleri, hareketli ortalamalar, hacim onayı

| # | Bulgu | Replikasyon / GP / Türkiye | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| D1 | **Brock, Lakonishok & LeBaron (1992)**, JF 47(5):1731–1764, DJIA 1897–1986. Hareketli ortalama ve kırılım kuralları: al sinyallerinin getirisi daha yüksek ve daha az oynak, sat sinyallerinin getirisi negatif. | **Sullivan, Timmermann & White (1999)**, JF 54(5):1647–1691: veri madenciliği düzeltmesiyle 1987–1996 örneklem dışında en iyi kural bile anlamsız (p≈%12). **Türkiye:** ISE-100 üzerinde 223 kural (Marmara Ü. tezi) maliyet sonrası ihmal edilebilir; Korkmaz (2022, İÜ tezi), BIST30 2010–2020: göstergeler al-tut stratejisini tutarlı biçimde geçemiyor. | T | `t=Teknik.Indicator("C/Mov(C,200,S)","d")>1;` | (T) | Kapı |
| D2 | **Han, Yang & Zhou (2013)**, JFQA 48(5):1433–1461. Oynaklığa göre sıralanmış portföylerde hareketli ortalama zamanlaması al-tut stratejisini belirgin geçiyor. Yüksek oynaklıklı portföylerde anormal getiri momentumdan büyük; piyasa zamanlaması, duyarlılık ya da likidite ile açıklanamıyor. **Dönüş hisseleri genelde oynak olduğundan trend filtresi en çok bu kümede değer katar.** | ABD; kullanılan hareketli ortalama uzunluğu özet sayfasında yok **[DY]**. | P | `t50=Teknik.Indicator("C/Mov(C,50,S)","d")>1;` (oynak dönüş kümesinde ek kısa vadeli trend kapısı) | Orta | Kapı |
| D3 | **Avramov, Kaplanski & Subrahmanyam (2021)**, Review of Financial Economics 39(2):127–145. MAD = HO21/HO200. Değer ağırlıklı alfa ≈%9/yıl; momentum, 52H ve kârlılığın ötesinde öngörü gücü var; uzun bacak daha güçlü. ABD 1977–2015: ertesi ay getirisi en düşük dilimde %0,84, en yüksekte %1,92 ve neredeyse monoton [Ö]. 2001–2015'te momentum, 52H ve trend etkileri kaybolurken MAD anlamlı kalıyor (t=2,80) [Ö]. | Uluslararası analiz 2001+ [Ö]; Türkiye yok. | P (K10'da HO20>HO60 yalnızca kapı olarak var) | `mad=Teknik.Indicator("Mov(C,21,S)/Mov(C,200,S)","d");` | Yüksek | Sıralama / bonus |
| D4 | **Lee & Swaminathan (2000)**, JF 55(5):2017–2069, 1965–1995. Yüksek devir hızı cazibe (glamour) hissesi, düşük devir hızı değer hissesi özelliği taşıyor. Yüksek hacimli kazananlar daha hızlı tersine dönüyor. "Erken evre" (düşük hacimli kazanan − yüksek hacimli kaybeden) 1. yılda %14,33, 2–3. yılda da pozitif. "Geç evre" 1. yılda %4,69, 2–5. yılda negatif [Ö]. **Dönüşün erken evresi: fiyat yükseliyor ama devir hızı henüz düşük.** | ABD. | N | `dh=Teknik.Indicator("Mov(C*V,60,S)","d")/PD();` (devir hızı vekili; PD birimini kontrol et; çok yüksekse ceza) | Düşük-Orta | Ceza |
| D5 | **Gervais, Kaniel & Mingelgrin (2001)**, JF 56(3):877–919. Bir gün ya da bir hafta olağandışı **yüksek** hacim gören hisseler sonraki ay değer kazanıyor, düşük hacimliler kaybediyor (görünürlük etkisi). D4 hacmin **düzeyiyle**, D5 hacim **şokuyla** ilgili; ikisi çelişmez. | Huddart ve ark. 2009 destekliyor. | N | `hv=IF(Teknik.Indicator("Mov(V,5,S)/Mov(V,60,S)","d")>1.5,1,0);` | Orta | Bonus |
| D6 | **Da, Gurun & Warachka (2014)**, RFS 27(7):2171–2218. Bilgi küçük parçalar hâlinde sürekli geldiğinde momentum daha güçlü ve tersine dönmüyor. Ölçü: ID = sgn(getiri)×(%negatif gün − %pozitif gün). 6 ay elde tutmada sürekli bilgi %5,94, kesikli bilgi −%2,07, fark %8,01 [Ö]. **Aşırı uzama cezası "sıçramalı" yükselişe uygulanmalı, düzgün yükselişe değil.** | ABD. | N | `fip=Teknik.Indicator("Sum(C>Ref(C,-1),126)","d")/126;` (pozitif gün oranı; boolean `Sum` desteğini platformda doğrula) | Orta | Sıralama / bonus |

### E. Uygulayıcı sistemler: kanıt var mı?

| # | Sistem / bulgu | Akademik kanıt | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| E1 | **Weinstein aşama analizi** (kitap 1988 **[DY]**, açılmadı). Aşama 1: yataylaşan 30 haftalık hareketli ortalama etrafında taban. Aşama 2: fiyatın yükselen 30 haftalık HO'nun üstüne hacimle kırması ve göreli gücün artması. **Aşama 1'den 2'ye geçiş, dipten dönüşün teknik tanımı.** | Doğrudan test: Roskill, "Does Weinstein Stage Analysis Beat a Moving Average?" (SSRN 7429238), **[DY]**: SSRN 429 hatası verdi, içerik okunamadı. Parçaların kanıtı: HO filtresi (D1–D3), kırılım+hacim (C3, D5), göreli güç (JT 1993). | N | `w=IF(Teknik.Indicator("C/Mov(C,150,S)","d")>1,IF(Teknik.Indicator("Ref(C,-126)/Ref(Mov(C,150,S),-126)","d")<1,1,0),0);` (bugün HO150 üstünde, 6 ay önce altındaydı = taze aşama 2; `Ref(Mov())` iç içe kullanımını doğrula) | Yüksek | Bonus (veya kapı) |
| E2 | **Minervini trend şablonu.** Kitap (2013) **[DY]**; kriterler ikincil kaynaktan alındı: C > HO50, HO150, HO200; HO50 > HO150 > HO200; HO200 yükseliyor; fiyat 52H zirvesinin %25 yakınında; 52H dibinin en az %30 üstünde (RS ≥70 şartı **[DY]**). VCP için akademik test bulunamadı. | Bağımsız akademik test yok. Parçaları: hareketli ortalamalar (D1–D3), 52H (C1). **Sorun:** "zirvenin %25 yakınında" şartı dipten dönüşün erken evresini dışlıyor. | P (K10: C>HO200, C>HO75, HO20>HO60) | `ms=IF(Teknik.Indicator("Mov(C,50,S)/Mov(C,200,S)","d")>1,IF(Teknik.Indicator("C/LLV(L,252)","d")>=1.3,1,0),0);` | Orta | Kapı |
| E3 | **O'Neil CAN SLIM** (AAII özeti). C: çeyreklik hisse başına kâr, geçen yılın aynı çeyreğine göre ≥%18–20 ve hızlanıyor. A: 3 yıl yıllık bileşik ≥%25 ve ROE ≥%17. N: konsolidasyon sonrası yeni zirve. L: göreli güç ≥80. I: kurumsal sahiplik. M: piyasa yönü. | **Lutey, Crum & Rayome (2014)**, J. Accounting & Finance: basitleştirilmiş CAN SLIM, NASDAQ-100, 1999–2013, yıllık %14,21'e karşı endeks %3,82 [Ö]. Ancak hayatta kalma yanlılığı var, örneklem dışı test yok. Parçaların karşılığı: C ≈ SUE/PEAD (A1, A4), N ≈ 52H (C1), L ≈ momentum, M ≈ piyasa durumu (F2). **A kriteri (3 yıl istikrarlı büyüme) dönüş profilini dışlar; C+L+M uygun.** | P | `c=IF(NetKarYillik()>Max(NetKarYillik("",-4),0)*1.25,1,0);` (geçen yıl zarardaysa her kâr geçer → Profil 1; kârdaysa +%25 → Profil 2. Çeyreklik varyant: `NetKar("TL",0)` / `NetKar("TL",-4)`) | Yüksek | Kapı |
| E4 | **Darvas kutusu.** Bulkowski testi (557 hisse + 104 BYF, 2001–2010): günlük ölçekte etkisiz. En iyi (haftalık) yapılandırma bile S&P 500'ün yatay kaldığı dönemde al-tut'u geçemedi (−%0,7) [Ö]. | Akademik test yok; uygulayıcı testi olumsuz. Parça: 52H kırılımı (C1–C3). | N | `dv=IF(Teknik.Indicator("HHV(H,21)/HHV(H,252)","d")>=1,1,0);` | Düşük | Bonus |

### F. Kriz/şok sonrası toparlanma ve momentum çöküşleri (bu strateji için kritik)

| # | Bulgu | Replikasyon / GP / Türkiye | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| F1 | **Daniel & Moskowitz (2016)**, JFE 122(2):221–247, ABD 1927–2013 + uluslararası. Momentum çöküşleri kısmen öngörülebilir: panik dönemlerinde, piyasa düşüşü ve yüksek oynaklık sonrasında, **piyasa toparlanırken** oluyor. Temmuz–Ağustos 1932: kaybedenler +%232, kazananlar +%32. Mart–Mayıs 2009: kaybedenler +%163, kazananlar +%8 [Ö]. Kaybeden ondalığın betası 3'ü aşabiliyor [Ö]. Dinamik momentum Sharpe ≈1,19, statik 0,60 [Ö]. **Yorum: dipten dönüşü önce derin kaybedenler götürür; 6–12 ay momentum şartı bu ilk ayağı kaçırır.** | **Barroso & Santa-Clara (2015)**, JFE 116(1):111–120: momentumun riski zamanla değişiyor ve öngörülebilir; risk yönetimi çöküşleri neredeyse ortadan kaldırıyor, Sharpe ≈2 katına çıkıyor. | N | `m6g=IF(Getiri("s12a","TL","XUTUM")<Tufe(12),1,IF(Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d")>1,1,0));` (piyasa 12 ayda reel düştüyse 6 ay momentum kapısını uygulama) | Yüksek | Rejim anahtarı |
| F2 | **Cooper, Gutierrez & Hameed (2004)**, JF 59(3):1345–1365, 1929–1995. Önceki 36 ayda piyasa yükseldiyse momentum %0,93/ay, düştüyse −%0,37/ay. Uzun vadeli tersine dönmeler yükselen piyasa sonrasında görülüyor. | Griffin ve ark. (2003) momentumun iyi ve kötü makro dönemlerde sürdüğünü buluyor; ancak Türkiye satırı negatif (H). | N | `up=IF(Getiri("s12a","TL","XUTUM")>Tufe(12),1,0);` (36 aylık getiri platformda varsa onu kullan **[platformda doğrula]**) | Orta | Rejim |
| F3 | **Goulding, Harvey & Mazzoleni (2023)**, JFE 149(3):378–406. Yavaş (12 ay) ve hızlı (1 ay) zaman serisi momentumu dört döngü tanımlıyor: Boğa, Düzeltme, Ayı, **Toparlanma** (yavaş negatif, hızlı pozitif). İkisini karıştıran ara hızdaki momentum koşulsuz pozitif alfa üretiyor. Aynı yazarların FAJ (2023) "Breaking Bad Trends" çalışması: dönüş noktası sıklığında 1 standart sapma artış, yıllık getiride ≈8,9 puan düşüşle ilişkili; dinamik yaklaşım 2009–2019'da %3,4, statik %0,3 [Ö]. | Piyasa düzeyinde, ABD ve çok varlıklı. | N | `reb=IF(Getiri("s12a","TL","XUTUM")<Tufe(12),IF(Getiri("s1a","TL","XUTUM")>0,1,0),0);` (1 = Toparlanma durumu) | Yüksek | Rejim |
| F4 | **Ding, Levine, Lin & Xie (2021)**, JFE 141(2):802–830, 61 ekonomi, 6.700+ firma. Pandemi öncesi finansalı güçlü firmalar (daha çok nakit ve kullanılmamış kredi, düşük borç, yüksek kârlılık) COVID'de daha az düştü. **Ramelli & Wagner (2020)**, RCFS 9(3):622–655: borç ve nakit, Fed müdahalesinden sonra da önemli değer sürücüleriydi. **Yorum:** şok sonrası dönüş adayında önce "hayatta kalma", sonra toparlanma (THYAO 2021–22 tipi). | Uluslararası. | P (K10'da NetBorç/FAVÖK<4) | `hk2=IF(NetBorcFavokYillik()<4,1,0);` (finansallarda FAVÖK boş, `IF(x==null,1,...)` ile geçir) | Orta | Kapı |

### G. Kısa vadeli dönüş ve aşırı uzama

| # | Bulgu | Replikasyon / GP / Türkiye | Durum | Taslak | Öncelik | Rol |
|---|---|---|---|---|---|---|
| G1 | **Jegadeesh (1990)**, JF 45(3):881–898: aylık getirilerde anlamlı negatif birinci derece otokorelasyon; 1934–87'de uç ondalıklar arası fark %2,49/ay. **Lehmann (1990)**, QJE 105(1):1–28: haftalık kazanan ve kaybedenlerde belirgin tersine dönme. Jegadeesh & Titman (1993) bu etkiden kaçınmak için 1 hafta atlıyor. **Novy-Marx (2012)**, JFE 103(3):429–453: momentumu 12–7 ay önceki performans sürüklüyor. **Goyal & Wahal (2015)**, JFQA 50(6):1237–1267: bu "yankı" 37 ülkede tutarlı değil; ABD'deki desen −2. aydaki kısa vadeli dönüşten kaynaklanıyor. | Uluslararası: 12–7 ay yankısı tutmuyor. | T (K10: `Ref(C,-21)/Ref(C,-126)`; 1 ay > −15 kapısı) | `m6=Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d");` | (T) | Sıralama |
| G2 | **Bali, Cakici & Whitelaw (2011)**, JFE 99(2):427–446. Son 1 aydaki en yüksek günlük getiri (MAX) ile beklenen getiri arasında anlamlı negatif ilişki; en düşük ve en yüksek MAX grupları arasındaki fark >%1/ay. | **Türkiye: Alkan & Guner (2018)**, JIFMIM 55:211–223: BIST'te yüksek MAX'lı hisseler düşük MAX'lılardan belirgin kötü performans gösteriyor. Etki bireysel yatırımcının tercih ettiği hisselerde ve iyimserlik dönemlerinde daha güçlü; açığa satış yasağında fark büyüyor. | P (K10'da uzama cezası var ama MAX tabanlı değil) | `mx=IF(Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")>1.09,0.8,1);` (son 1 ayda tavana yakın gün varsa ×0,8; BIST günlük marjına göre eşiği kontrol et) | Yüksek | Ceza/çarpan |
| G3 | **Aşırı uzama ile MAD çelişkisi.** ABD'de MAD'in en üst dilimi de en iyi getiriyi veriyor (D3), yani mekanik bir "uzaklık cezası" ABD kanıtıyla çelişiyor. Türkiye'de karşıt etki (C5) ve MAX etkisi (G2) güçlü. **Uzlaştırma:** sıçramalı uzamayı cezalandır (MAX, haberi olmayan 1 aylık sıçrama: A6), düzgün trendi cezalandırma (MAD, FIP). | — | P | G2 + A6 birlikte | Orta | Ceza tasarımı |

### H. Türkiye kanıtı (özet)

| Kaynak | Dönem | Bulgu |
|---|---|---|
| Rouwenhorst (1999), JF 54(4):1439–1464 | Türkiye 1989– | 20 gelişmekte olan piyasada momentum var; ülkeler eşit ağırlıklı ortalama %0,58/ay (t=3,78). **Türkiye kazanan−kaybeden %0,48/ay, t=0,57 (anlamsız)** [Ö] |
| Griffin, Ji & Martin (2003), JF 58(6):2515–2547 | Türkiye 1988– | **Türkiye WML −%1,50/ay (t=−2,20); kazanan %0,61, kaybeden %2,11** [Ö]. Gelişmekte olan piyasa ortalaması %0,27/ay [Ö] |
| Cakici, Fabozzi & Tan (2013), EMR 16:46–65 | 1990–2011 | 18 gelişmekte olan piyasa: değer her yerde, momentum Doğu Avrupa dışında her yerde. Türkiye'nin dahil olup olmadığı ve hangi bölgede sayıldığı **[DY]** |
| Bildik & Gülay (SSRN WP 2002; IRF 2007) | 1991–2000 | Kaybedenler kazananları ≈%15/yıl geçiyor; karşıt strateji kârlı |
| Alper & Aydoğan (2017), Muhasebe ve Finansman Dergisi | 2001–2015 | Karşıt strateji tüm vadelerde momentumdan iyi; 1 yılda ≈%29, 5 yılda ≈%19 fark [Ö] |
| Ünal (2021), IJMEB | 1997–2020 | En iyi %20'lik dilim sonra ortalamanın altına düşüyor; karşıt strateji işliyor |
| Ünal (2022), Gazi İktisat ve İşletme Dergisi 8(3):443–455 | 2008–2020 | Yazarın aktarımıyla "son çalışmalar momentumun BIST'te geçerli olmadığını bildiriyor"; faktör momentumu ek getiri sağlamıyor |
| **Gökçen (2026), Borsa Istanbul Review** | 1994–2024 | Momentum 1995–2024 için güvenilir değil, **2005–2024 için %11,88 alfa** [Ö]. Değer >%17/yıl. Kârlılık 2005 sonrası %9,70 alfa [Ö]. Rejim değişimine işaret ediyor |
| Özkan (2021), MAKÜ İİBF 8(2) | 2007–2016 | 52H zirve portföyleri pozitif ama anlamsız; brüt kârlılık anlamlı |
| Ahlatcıoğlu & Okay (2021), BIR 21(1) | 2007–2018 | PEAD var; EAR tabanlı 60 günlük fark %2,2 [Ö] |
| Alkan & Guner (2018), JIFMIM 55 | — | MAX/piyango etkisi BIST'te güçlü |
| Korkmaz (2022, İÜ tezi); Marmara Ü. tezi (ISE-100) | 2010–2020; — | Teknik göstergeler/kurallar maliyet sonrası al-tut'u tutarlı geçemiyor |

**Çıkarım:** Kullanıcının "momentum bu şirketlerde çok işe yarıyor" sezgisi saf fiyat momentumu olarak değil, **kâr dönüşüyle eşleşmiş fiyat hareketi** olarak kanıtla uyumlu (A1–A6, PEAD Türkiye). BIST'te uzun vadeli karşıt etkinin güçlü olması (C5), dipte bekleyen hisseler için rüzgârın arkadan estiğini gösteriyor. Zamanlama ise trend onayı (E1, D3) ve rejim anahtarıyla (F1–F3) yapılmalı.

---

## 2. Denenmemiş en iyi 10 fikir (sadelik ve uygulanabilirliğe göre sıralı)

| Sıra | Fikir | Tek satır taslak | Kanıt | Rol |
|---|---|---|---|---|
| 1 | **Kâr dönüşü/sıçraması × fiyat onayı (ikili kapı).** Tek koşul iki profili de kapsıyor. | `k=IF(NetKarYillik()>Max(NetKarYillik("",-4),0)*1.25,1,0)*IF(Getiri("s3a","TL")>Getiri("s3a","TL","XUTUM"),1,0);` | A1–A5, E3-C; Türkiye PEAD | Kapı |
| 2 | **Reel piyasa rejimi anahtarı.** Piyasa 12 ayda reel düştüyse 6 ay momentum kapısı kalkar; dönüşün ilk ayağı kaçmaz. | `m6g=IF(Getiri("s12a","TL","XUTUM")<Tufe(12),1,IF(Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d")>1,1,0));` | F1–F3 | Rejim kapısı |
| 3 | **MAD sıralaması** (tek çağrı, düzgün trend). | `mad=Teknik.Indicator("Mov(C,21,S)/Mov(C,200,S)","d");` | D3 | Sıralama/bonus |
| 4 | **MAX/tavan cezası** (Türkiye kanıtı var). | `mx=IF(Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")>1.09,0.8,1);` | G2, Alkan-Guner | Çarpan |
| 5 | **Taze aşama-2 geçişi** (dipten dönüşün teknik tanımı). | `w=IF(Teknik.Indicator("C/Mov(C,150,S)","d")>1,IF(Teknik.Indicator("Ref(C,-126)/Ref(Mov(C,150,S),-126)","d")<1,1,0),0);` | E1, D1–D2 | Bonus |
| 6 | **Ucuz ve inanılan:** E/P × 52H yakınlığı. | `vm=(NetKarYillik()/PD())*Teknik.Indicator("C/HHV(H,252)","d");` | B1–B2, C1 | Sıralama |
| 7 | **Uzun vadeli kaybeden bonusu** (yalnızca trend dönmüşse). | `b3=IF(Teknik.Indicator("C/HHV(H,756)","d")<0.6,1,0)*IF(Teknik.Indicator("C/Mov(C,200,S)","d")>1,1,0);` | C5 + Türkiye karşıt etki | Bonus |
| 8 | **Zirve tazeliği:** 6 ay zirvesi son 1 ayda yapılmış (tabandan kırılım). | `tz=IF(Teknik.Indicator("HHV(H,21)/HHV(H,126)","d")>=1,1,0);` | C2, C3 | Bonus |
| 9 | **Anormal hacim onayı.** | `hv=IF(Teknik.Indicator("Mov(V,5,S)/Mov(V,60,S)","d")>1.5,1,0);` | D5, C3 | Bonus |
| 10 | **Habere bağlı kısa vade cezası:** temel haber yoksa sert 1 aylık sıçramayı cezalandır. | `hk=IF(Getiri("s1a","TL")>25,IF(NetKarYillik()>NetKarYillik("",-4),1,0.8),1);` | A6, G1 | Çarpan |

**Yedek adaylar (daha düşük öncelik):** FIP pozitif gün oranı (D6; boolean `Sum` desteğine bağlı), Lee-Swaminathan devir hızı cezası (D4; PD birimi belirsiz), oynaklığa bağlı kısa trend kapısı (D2), Barroso & Santa-Clara tipi oynaklık eğimi (F1), CAN SLIM-C'nin çeyreklik varyantı (E3).

**Örnek sade teknik katman** (temel skor diğer ajanlardan gelir; en fazla 6 satır):
```
k=IF(NetKarYillik()>Max(NetKarYillik("",-4),0)*1.25,1,0)*IF(Getiri("s3a","TL")>Getiri("s3a","TL","XUTUM"),1,0);
m6g=IF(Getiri("s12a","TL","XUTUM")<Tufe(12),1,IF(Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d")>1,1,0));
mad=Teknik.Indicator("Mov(C,21,S)/Mov(C,200,S)","d");
mx=IF(Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")>1.09,0.8,1);
tz=IF(Teknik.Indicator("HHV(H,21)/HHV(H,126)","d")>=1,1,0);
IF(k*m6g==1,(TEMEL_SKOR+mad+0.1*tz)*mx,0);
```
**Ön kayıt önerisi:** Eşikler (1,25 / 21–200 / 1,09 / 21–126) literatürden sabitlendi. Optimize etmeden 2005–2015 ve 2016–2026 dönemleri ayrı ayrı test edilmeli (bkz. Uyarı 5).

---

## 3. Uyarılar: dönüş ve sıkıntılı şirketlerde kırmızı bayraklar

1. **Türkiye'de saf fiyat momentumu kırılgan.** Griffin ve ark. Türkiye için −%1,50/ay buluyor [Ö]. Bildik & Gülay, Alper & Aydoğan ve Ünal karşıt etki buluyor. 2005 sonrası pozitif bulgu (Gökçen 2026) rejime bağlı. 6–12 aylık fiyat getirisine skorda büyük ağırlık vermek risklidir; fiyat "onay/çelişmeme" kapısı olarak kullanılmalı (Novy-Marx 2015).
2. **Momentum çöküşü ile dipten dönüş aynı anda olur** (Daniel & Moskowitz 2016; Cooper ve ark. 2004). 2009 Mart–Mayıs tipi toparlanmalarda liderlik derin kaybedenlerdedir; 6 ay momentum + HO200 kapıları ilk 3–6 ayı kaçırır. Tersi de geçerli: ayı piyasası sürerken "dipten dönüş" sinyalleri ölü kedi sıçraması olabilir. Düşen piyasada momentum negatif (Cooper ve ark.), haber olmadan gelen sert hareketler tersine döner (Chan 2003; Savor 2012). Rejim anahtarı ve temel teyit birlikte şart.
3. **Sıkıntılı şirket anomalisi.** Yüksek iflas olasılıklı hisseler düşük getiri ve yüksek oynaklık sunuyor (Campbell ve ark. 2008, JF 63(6)). Momentum kârı ve çöküşü düşük kredi notlu firmalarda yoğunlaşıyor (Avramov ve ark. 2007, JF 62(5)). Uç zarar açıklayan firmalar sonrasında da kötü gidiyor: uç zarar ile uç kâr portföyleri arasındaki fark yıllık ≈%21 (Balakrishnan ve ark. 2010, JAE 50(1)). **Sonuç:** kâra geçiş beklenti değil, açıklanmış olmalı; özkaynak pozitif, borç taşınabilir olmalı.
4. **ROE ve "sahte kâr" artefaktları.** Negatif özkaynak ile zarar bir araya gelince ROE pozitif görünür; "ROE negatiften pozitife" kapısı `Ozsermaye()>0` olmadan yanıltır. Tek seferlik gelirler (varlık satışı, kur farkı, TMS 29 parasal kazanç) fiyatı bir çeyrek kandırabilir. Fiyat tepkisi (EAR) bunun bir kısmını ayıklar ama yetmez; FAVÖK veya esas faaliyet teyidi gerekir (bankalarda FAVÖK yok).
5. **Veri madenciliği.** BLL kuralları örneklem dışında anlamsızlaştı (Sullivan ve ark. 1999); BIST'te teknik kurallar maliyet sonrası ≈0. Teknik katmanda ≤3–4 kural, literatürde sabit eşikler kullan ve bölünmüş dönemlerde test et.
6. **Uygulayıcı sistemlerin kanıtı zayıf.** Darvas al-tut'u geçemedi (Bulkowski [Ö]). CAN SLIM testinde hayatta kalma yanlılığı var. Minervini/VCP için bağımsız test yok. Weinstein makalesi doğrulanamadı. "Zirvenin %25 yakınında" ve "3 yıl istikrarlı büyüme" şartları dönüş profilini dışlar.
7. **Piyango/tavan etkisi.** BIST'te yüksek MAX'lı hisseler kötü performans gösteriyor (Alkan & Guner 2018). Dönüş hikâyeli küçük hisselerde tavan serileri sık; ceza uygulanmalı.
8. **Enflasyon.** Nominal TL'de piyasa durumu ve büyüme eşikleri yanıltıcı; TÜFE ile reel karşılaştırma yapılmalı (`Tufe(12)`). 2024+ dönemde TMS 29 büyüme fonksiyonlarını bozuyor.
9. **Likidite ve maliyet.** Momentum küçük ve az takip edilen hisselerde daha güçlü (Hong ve ark. 2000, JF 55(1)); ancak 52H kârları maliyet sonrası çoğu piyasada anlamsız (Liu ve ark. 2011). Halka açıklık <60 kapısının yanında bir likidite tabanı da konmalı (`Mov(C*V,20,S)`).
10. **Ocak mevsimselliği.** Kaybedenlerin dönüşü Ocak'ta yoğunlaşıyor (De Bondt & Thaler [Ö]); 52H stratejisi Ocak'ta negatif (George & Hwang [Ö]). BIST'te ay bazında kontrol edilmeli.

---

## 4. Dürüst sınırlar

- **Hacim:** ≈60 web araması yapıldı (oturumun arama kotası doldu; Savor 2012 araması yapılamadı, RePEc'ten doğrudan açıldı) ve ≈85 sayfa/PDF açıldı.
- **Doğrulanan kaynaklar:** 53 akademik/uygulayıcı kaynak yayıncı, RePEc/EconPapers, NBER, SSRN, DergiPark, ScienceDirect özet sayfası ya da yazarın PDF'i üzerinden açıldı. Buna ek olarak 3 ikincil/uygulayıcı sayfa (AAII, Bulkowski, Minervini şablon özeti) kullanıldı.
- **[DY] olanlar:** Roskill (Weinstein, SSRN 429); Huang-Zhang-Zhou "Twin Momentum" (403); Weinstein (1988), Minervini (2013), O'Neil ve Darvas kitapları (açılmadı; kriterler ikincil kaynaktan); Minervini RS ≥70 şartı; Han-Yang-Zhou'da kullanılan HO uzunluğu; Cakici ve ark.'da Türkiye'nin durumu; Bildik & Gülay'ın IRF 2007 sayfası (Wiley 403, SSRN WP özeti kullanıldı); BDDK Dergi'deki momentum makalesi (robots engeli); Wiley JF sayfaları (403, RePEc kullanıldı).
- **[Ö] rakamları:** PDF'ler araçla özetlenerek okundu. Proxy bazı alan adlarını (ör. gyanresearch) engellediği için yerel `pdftotext` ile tablo kontrolü yapılamadı. Türkiye satırları (Rouwenhorst, Griffin ve ark.) tek okumadan geliyor; karar vermeden önce tablodan teyit edilmeli.
- **Yayın durumu:** Novy-Marx (2015) için dergi yayını bulunamadı (NBER WP). Brandt ve ark. (2008) SSRN WP olarak alındı.
- **Platform sözdizimi doğrulanmadı:** `Teknik.Indicator` içinde boolean (`C>Ref(C,-1)`) ve `Ref(Mov(...))` iç içe kullanımı, `Getiri("s36a")` ve `Tufe(12)` birimi (% mi oran mı) test edilmeli.
- **Genelleme sınırı:** Etki büyüklüklerinin çoğu ABD kaynaklı. Hiçbiri bu stratejinin BIST evreninde (5 hisse, aylık, her zaman yatırımda) test edilmedi; beklentiler buna göre düşürülmeli.

---

## 5. Kaynakça (açılan sayfalar)

- Chan, Jegadeesh, Lakonishok (1996): https://econpapers.repec.org/RePEc:bla:jfinan:v:51:y:1996:i:5:p:1681-1713 ; PDF: http://www-stat.wharton.upenn.edu/~steele/Courses/434/434Context/Momentum/MomentumStrategiesJF96.pdf
- Chordia, Shivakumar (2006): https://www.sciencedirect.com/science/article/abs/pii/S0304405X05002175
- Novy-Marx (2015): https://www.nber.org/papers/w20984
- Brandt, Kishore, Santa-Clara, Venkatachalam (2008): https://www.anderson.ucla.edu/documents/areas/fac/finance/ear.pdf
- Ahmed, Safdar (2018): https://ideas.repec.org/a/bla/acctfi/v58y2018is1p3-43.html
- Chan (2003): https://ideas.repec.org/a/eee/jfinec/v70y2003i2p223-260.html ; WP: http://www.econ.yale.edu/~shiller/behfin/2001-05-11/chan.pdf
- Savor (2012): https://ideas.repec.org/a/eee/jfinec/v106y2012i3p635-659.html
- Asness (1997): https://rpc.cfainstitute.org/en/research/financial-analysts-journal/1997/the-interaction-of-value-and-momentum-strategies
- Asness, Moskowitz, Pedersen (2013): https://ideas.repec.org/a/bla/jfinan/v68y2013i3p929-985.html ; postprint: https://research-api.cbs.dk/ws/files/44523827/lasse_heje_pedersen_value_and_momentum_postprint.pdf
- George, Hwang (2004): https://www.bauer.uh.edu/tgeorge/papers/gh4-paper.pdf
- Liu, Liu, Ma (2011): https://www.sciencedirect.com/science/article/abs/pii/S0261560610001099
- Bhootra, Hur (2013): https://econpapers.repec.org/RePEc:eee:jbfina:v:37:y:2013:i:10:p:3773-3782
- Huddart, Lang, Yetman (2009): https://ideas.repec.org/a/inm/ormnsc/v55y2009i1p16-31.html
- Jeon, Byun (2023): https://epublications.marquette.edu/cgi/viewcontent.cgi?article=1168&context=fin_fac
- De Bondt, Thaler (1985): https://ideas.repec.org/a/bla/jfinan/v40y1985i3p793-805.html ; PDF: http://efinance.org.cn/cn/fm/Does%20the%20Stock%20Market%20Overreact.pdf
- Jegadeesh, Titman (1993): https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf
- Brock, Lakonishok, LeBaron (1992): https://ideas.repec.org/a/bla/jfinan/v47y1992i5p1731-64.html
- Sullivan, Timmermann, White (1999): https://ideas.repec.org/a/bla/jfinan/v54y1999i5p1647-1691.html ; PDF: https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Sullivan_Timmermann_White.pdf
- Han, Yang, Zhou (2013): https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/new-anomaly-the-crosssectional-profitability-of-technical-analysis/B9E41049F2E55B4F274D46E72ECA8E29
- Avramov, Kaplanski, Subrahmanyam (2021): https://ideas.repec.org/a/wly/revfec/v39y2021i2p127-145.html ; WP: https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Avramov-Kaplanski-Subra_2018_SSRN-id3111334.pdf
- Lee, Swaminathan (2000): https://www.lsvasset.com/pdf/research-papers/Price-Momentum-Trad-Vol-2000.pdf
- Gervais, Kaniel, Mingelgrin (2001): https://sites.duke.edu/sgervais/research/gervais-kaniel-mingelgrin-2001/
- Da, Gurun, Warachka (2014): https://academicweb.nd.edu/~zda/Frog.pdf
- Daniel, Moskowitz (2016): https://www.kentdaniel.net/papers/published/jfe_16.pdf
- Barroso, Santa-Clara (2015): https://econpapers.repec.org/RePEc:eee:jfinec:v:116:y:2015:i:1:p:111-120
- Cooper, Gutierrez, Hameed (2004): https://scholarbank.nus.edu.sg/handle/10635/44524
- Goulding, Harvey, Mazzoleni (2023, JFE): https://econpapers.repec.org/article/eeejfinec/v_3a149_3ay_3a2023_3ai_3a3_3ap_3a378-406.htm ; FAJ: https://people.duke.edu/~charvey/Research/Published_Papers/P167_Breaking_bad_trends.pdf
- Ding, Levine, Lin, Xie (2021): https://ideas.repec.org/a/eee/jfinec/v141y2021i2p802-830.html
- Ramelli, Wagner (2020): https://ideas.repec.org/a/oup/rcorpf/v9y2020i3p622-655..html
- Jegadeesh (1990): https://econpapers.repec.org/RePEc:bla:jfinan:v:45:y:1990:i:3:p:881-98
- Lehmann (1990): https://ideas.repec.org/a/oup/qjecon/v105y1990i1p1-28..html
- Novy-Marx (2012): https://econpapers.repec.org/RePEc:eee:jfinec:v:103:y:2012:i:3:p:429-453
- Goyal, Wahal (2015): https://ideas.repec.org/a/cup/jfinqa/v50y2015i06p1237-1267_00.html
- Bali, Cakici, Whitelaw (2011): https://www.nber.org/papers/w14804
- Alkan, Guner (2018): https://ideas.repec.org/a/eee/intfin/v55y2018icp211-223.html
- Hong, Lim, Stein (2000): https://www.nber.org/papers/w6553
- Avramov, Chordia, Jostova, Philipov (2007): https://ideas.repec.org/a/bla/jfinan/v62y2007i5p2503-2520.html
- Campbell, Hilscher, Szilagyi (2008): https://ideas.repec.org/a/bla/jfinan/v63y2008i6p2899-2939.html
- Balakrishnan, Bartov, Faurel (2010): https://ideas.repec.org/a/eee/jaecon/v50y2010i1p20-41.html
- Rouwenhorst (1999): https://ideas.repec.org/p/ysm/somwrk/ysm97.html ; PDF: http://depot.som.yale.edu/icf/papers/fileuploads/2501/original/98-95.pdf
- Griffin, Ji, Martin (2003): https://gyanresearch.wdfiles.com/local--files/alpha/Momentum.pdf
- Cakici, Fabozzi, Tan (2013): https://ideas.repec.org/a/eee/ememar/v16y2013icp46-65.html
- Gökçen (2026): https://www.sciencedirect.com/science/article/pii/S2214845026001043
- Bildik, Gülay (2002 WP): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=302299
- Alper, Aydoğan (2017): https://dergipark.org.tr/en/download/article-file/428034
- Ünal (2021): https://dergipark.org.tr/tr/pub/ijmeb/issue/64257/832584
- Ünal (2022): https://dergipark.org.tr/tr/download/article-file/1940898
- Özkan (2021): https://dergipark.org.tr/en/pub/makuiibf/article/790900
- Ahlatcıoğlu, Okay (2021): https://www.sciencedirect.com/science/article/pii/S2214845020300508
- Korkmaz (2022, tez): https://nek.istanbul.edu.tr/ekos/TEZ/ET003240.pdf
- ISE teknik analiz tezi (Marmara): https://openaccess.marmara.edu.tr/entities/publication/0200fc08-12ae-4b1b-a2f0-85a04180bb27
- Lutey, Crum, Rayome (2014): http://www.na-businesspress.com/JAF/LuteyM_LWeb14_5_.pdf
- AAII CAN SLIM: https://www.aaii.com/journal/article/william-oneil-can-slim-approach-to-selecting-growth-stocks
- Bulkowski, Darvas: https://thepatternsite.com/Darvas.html
- Minervini şablon özeti (ikincil): https://kasauti.in/blog/methodology/minervini/
- [DY] Roskill, Weinstein: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7429238
- [DY] Huang, Zhang, Zhou, Twin Momentum: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2894068
