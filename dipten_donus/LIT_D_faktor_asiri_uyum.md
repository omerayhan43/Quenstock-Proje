# LIT_D — Faktör Hayvanat Bahçesi, Replikasyon, Makine Öğrenmesi, Aşırı Uyum ve Sade Tasarım

**Proje:** "Dipten Dönüş" stratejisi (BIST TÜM, her ay 5 hisse, eşit ağırlık, her zaman yatırımda) — Ajan D literatür taraması
**Tarih:** 01/10/2026

**İşaretler:**
- **[DY]**: doğrulanamadı (kaynak sayfası açılamadı ya da içerik görülemedi).
- **[Ö]**: rakam PDF'ten ya da ikincil özetten okundu, makalenin kendi özetinde (abstract) geçmiyor. Yön doğru kabul edilebilir, tam değeri birincil tabloda kontrol edilmeli.
- **[H]**: bu raporda benim yaptığım hesap (varsayımsal girdilerle, literatür rakamı değil; formüller kaynaklarda verilen formüllerdir).
- **Durum:** T = denendi (K10/C32'de var), P = kısmen, N = denenmedi.
- **Rol:** Kapı (filtre) / Sıralama (skor bileşeni) / Bonus-Ceza.

---

## 0. Yönetici özeti (10 madde)

1. **Replikasyonda en sağlam "temel değişim" sinyalleri kazanç momentumu ailesindedir.** Hou, Xue ve Zhang (2020) toplam 452 anomaliden %65'inin |t| ≥ 1,96 eşiğini geçemediğini gösteriyor. Buna karşın momentum kategorisindeki ΔROE (dRoe), Abr ve Sue 1 aylık tutuşta güçlü kalıyor [Ö]. Jensen, Kelly ve Pedersen (2023) bu sinyalleri **"Profit Growth"** temasında topluyor: çeyreklik ROE değişimi, SUE, gelir sürprizi, satış ve SG&A farkı, faaliyet nakit akışı değişimi.
2. **Makine öğrenmesi farklı bir sıralama veriyor.** Gu, Kelly ve Xiu (2020) ile Hanauer ve Kalsbach (2023, gelişmekte olan piyasalar) çalışmalarında en önemli değişkenler fiyat trendi (momentum, 52 hafta zirveye yakınlık, kısa vadeli dönüş), likidite ve volatilite. Temel değişim sinyalleri üst sıralarda değil.
   → **Çıkarım:** dönüş stratejisinde **temel değişim stratejinin kimliğidir (kapı)**. **Fiyat trendi teyit ve sıralama** işini yapar. **Volatilite ve likidite koruma** içindir.
3. **Yayın sonrası düşüş ABD'ye özgü görünüyor.** McLean ve Pontiff (2016) ABD'de getirilerin yayın sonrası %58 düştüğünü buluyor. Jacobs ve Müller (2020) ise 39 piyasada güvenilir bir yayın sonrası düşüşün **yalnızca ABD'de** olduğunu gösteriyor. Türkiye'de momentum ve kârlılık primleri **2005 sonrasında anlamlı**, değer primi en güçlüsü (Gökçen 2026, Borsa Istanbul Review).
4. **Sadeliğin lehine kanıt güçlü:**
   - 1/N kuralını tutarlı biçimde yenen bir optimize model yok (DeMiguel, Garlappi ve Uppal 2009).
   - Eşit ağırlıklı stil entegrasyonu karmaşık yöntemlere rakipsiz (Fernandez-Perez, Fuertes ve Miffre 2019).
   - Eşit ağırlıklı "uygunsuz" doğrusal modeller sağlam çalışıyor (Dawes 1979).
   - Birden çok sinyali birleştirmek ağır seçim yanlılığı yaratıyor: n adaydan en iyi k sinyali seçmek, nᵏ aday içinden en iyi tek sinyali seçmek kadar yanlı (Novy-Marx, NBER w21329).
5. **Kapı mı skor mu?** Uzun-tek yönlü (long-only) ve yüksek takip hatalı portföylerde (5 hisse uç bir örnek) tek bileşik skor, ayrı ayrı kapılardan ya da ayrı portföy dilimlerinden genelde iyi ya da en az onlar kadar iyi. Kaynaklar: Fitzgibbons ve diğerleri 2017, Bender ve Wang 2016, Ghayur, Heaney ve Platt 2018 (yüksek takip hatasında). Ancak sağlam testlerle fark her zaman anlamlı değil (Leippold ve Rüegg 2018). **Kapı sayısı 2–3 ile sınırlanmalı, gerisi tek skorda toplanmalı.**
6. **Mevcut terfi kuralındaki "NW t ≥ 1,5" eşiği deneme sayısına bağlanmalı.** Bu eşik, birbirinden bağımsız ve tamamen şansa dayalı **yaklaşık 8–10 denemenin beklenen en iyisine** eşit [H]. Birbirinden bağımsız 10 saf gürültü varyantından en az birinin t ≥ 1,5'i geçme olasılığı %50, 20 varyantta %75 [H]. Önerilen eşik t* ≈ E[max Z_N]: N = 20 için 1,9, N = 50 için 2,3. Final için ek olarak Deflated Sharpe (DSR) ve PBO/CSCV kullanılmalı.
7. **5 hisselik portföy çok gürültülü.** 258 ayda kazandıran ay oranının standart hatası yaklaşık **2,8 puan**, yıllık Sharpe'ın standart hatası yaklaşık **0,22**. Her yarı dönemde Sharpe standart hatası yaklaşık 0,31 [H]. Bu yüzden %72 ile %77 arasındaki fark ya da +0,1 Sharpe, eşleştirilmiş (aylık fark serisi) testler olmadan anlamlı sayılamaz.
8. **Gerçekçi beklenti:**
   - Canlı performans backtest'in altında kalır: JKP'de örnek dışı alfa örnek içinin yaklaşık 2/3'ü [Ö].
   - ABD'de modern dönemde maliyet sonrası ortalama anomali getirisi ayda yaklaşık 4 baz puan (Chen ve Velikov 2023).
   - Momentum, panik sonrası toparlanma aylarında çöker (Daniel ve Moskowitz 2016).
   - Fiyat momentumunu kontrol eden kazanç momentumu ise çökmüyor (Novy-Marx 2015).
9. **Dönüş adaylarına özgü kırmızı bayraklar:**
   - Sıkıntılı şirket anomalisi: sıkıntılı hisseler düşük getiri verir (Campbell, Hilscher ve Szilagyi 2008).
   - Anomali kârlarının büyük kısmı sıkıntılı şirketlerin **kısa** bacağından gelir (Avramov ve diğerleri 2013).
   - MAX/piyango etkisi (Bali, Cakici ve Whitelaw 2011) ve Türkiye'de düşük riskli hisselerin yüksek riskliler üstünde getiri vermesi (Gökçen 2026).
   - Negatif özkaynak + zarar = pozitif ROE tuzağı.
   - Tek seferlik kâr ve TMS 29 bozulmaları.
10. **Önerilen iskelet (Bölüm 8): 1 sert filtre (HA < 60) + 2 kapı (olay: ΔE/P ya da ΔROE; teyit: C > MA200) + 3 bileşenli eşit ağırlıklı skor.** Kapılar skora sözlük sırasıyla gömülür: `100·A + 10·B + bileşik`. Böylece her ay 5 hisse otomatik dolar; önce teknik koşul, sonra temel koşul gevşer.

---

## 1. Yöntem

- **Birincil kaynaklar:** yayıncı, NBER, SSRN, RePEc (IDEAS/EconPapers), DergiPark ve OpenAlex kayıtları açılarak kontrol edildi. Wiley ve SSRN sayfalarının çoğu 403/429 hatası verdi. Bunun yerine aynı makalenin NBER, RePEc ve OpenAlex kayıtlarından özet metni doğrulandı.
- **Doğrulanan kaynak sayısı: 48.** Tam liste Bölüm 13'te. 47 kaynağın künyesi ve özeti ya da ilgili içeriği açıldı. Chordia ve Shivakumar (2006) için yalnız künye doğrulandı, içeriği [DY].
- **Hesaplar:** Bölüm 4'teki hesaplar (beklenen maksimum Sharpe, MinBTL, standart hatalar) kaynak formüllerle Python'da yapıldı. MinBTL formülü, makalenin "5 yıl veriyle 45 konfigürasyon" örneğini yeniden üretiyor (N = 45, hedef Sharpe 1,0 → 5,0 yıl) [H].
- **Platform formülleri:** brief'teki QueenStocks fonksiyonlarıyla yazıldı. Brief'te geçmeyen imzalar **"imza doğrulanmalı"** diye işaretlendi: `Ozsermaye()`, `FAVOKYillik("",-4)`, `NetKar("TL",-5)`, `Teknik.Indicator` içinde `C/Ref(C,-1)`.

---

## 2. Replikasyon: hangi "temel değişim" sinyalleri ayakta kalıyor?

### 2.1 Büyük replikasyon ve çoklu test çalışmaları

| Bulgu (yazar, yıl, örneklem, dönem, etki) | Replikasyon / GP / TR kanıtı | Durum | Platformda karşılığı (tek satır) | Öncelik | Rol |
|---|---|---|---|---|---|
| **Hou, Xue ve Zhang (2020, RFS 33(5))**: 452 anomali, NYSE kırılımları ve piyasa değeri ağırlıklı getiriler. %65'i \|t\| ≥ 1,96'yı, %82'si 2,78 çoklu test eşiğini geçemiyor. İşlem sürtünmesi kategorisinin %96'sı başarısız. Replike olanların büyüklüğü de orijinalden çok küçük. NBER WP sürümü: 447 anomali, %64; t ≥ 3 eşiğinde %85. | Kendisi replikasyon çalışması (ABD). Momentum kategorisinde 57 değişkenin 20'si anlamsız [Ö]. Hayatta kalanlar, 1 aylık tutuşta ve q-faktör modeline göre [Ö]: **dRoe** ayda %0,76 (t = 5,43), q-alfa %0,34 (t = 2,29); **Abr** %0,74 (t = 5,85), q-alfa %0,66; **Sue** %0,47 (t = 3,42) ama q-alfa ≈ 0. Fiyat momentumu R6: %0,82 (6 aylık), %0,55 (12 aylık) [Ö]. | — | ΔROE: `OzsermayeKarlilikYillik() - OzsermayeKarlilikYillik("",-4)` | **Yüksek** | Temel ölçü (kapı + skor) |
| **McLean ve Pontiff (2016, JF 71(1))**: 97 değişken. Getiriler örnek dışında %26, yayın sonrasında %58 düşük. Yayın bilgisiyle yapılan işlemin etkisi yaklaşık %32. Düşüş, örnek içi getirisi yüksek olan ve idiyosenkratik riski yüksek/likiditesi düşük hisselerde daha büyük. | ABD. Veri madenciliğinin üst sınırı %26 olarak tahmin ediliyor. | — | Beklentiyi kırp (Bölüm 6) | Yüksek | Beklenti |
| **Jensen, Kelly ve Pedersen (2023, JF 78(5))**: 153 faktör, 93 ülke, 13 tema, Bayesçi replikasyon. Faktörlerin çoğu replike ediliyor, temaların çoğu teğet portföyde anlamlı ve faktör sayısının çok olması kanıtı güçlendiriyor. | NBER WP (2021): replikasyon oranı ABD %84,0, gelişmiş (ABD hariç) %77,8, **gelişmekte olan %76,5**, dünya %84,9 [Ö]. Örnek dışı alfa ortalaması ayda %0,45'ten %0,31'e iniyor, yani yaklaşık 1/3 düşüş [Ö]. 13 temanın 10'unda replikasyon > %75; istisnalar mevsimsellik, kaldıraç ve büyüklük [Ö, Alpha Architect özeti]. | — | Tema haritası: 2.3 | Yüksek | Sinyal seçimi |
| **Jacobs ve Müller (2020, JFE 135(1))**: 241 anomali, 39 piyasa, 2 milyondan fazla anomali–ülke–ay gözlemi. **Güvenilir yayın sonrası düşüş yalnızca ABD'de.** | Uluslararası piyasalarda anomaliler sürüyor. Arbitraj engelleriyle açıklanan piyasa bölünmüşlüğü öne çıkıyor; veri madenciliği açıklaması zayıflıyor. | — | — | Orta | BIST için olumlu |
| **Jacobs (2016, JFE 122(2))**: Stambaugh–Yu–Yuan yanlış fiyatlama skoru, 45 ülke, 1994–2013. Yanlış fiyatlama dünya genelinde anlamlı; gelişmiş piyasalarda da gelişmekte olanlar kadar yaygın. | 11 anomalinin sıra ortalaması (bileşik skor) uluslararası düzeyde çalışıyor. | — | — | Düşük | Bileşik skor gerekçesi |
| **Harvey, Liu ve Zhu (2016, RFS 29(1))**: yüzlerce faktör test edildiği için yeni bir faktörün **t > 3,0** eşiğini geçmesi gerekir. Yazarlara göre iddia edilen bulguların çoğu muhtemelen yanlış. | Çoklu test çerçevesi. | — | t-eşiğini deneme sayısına bağla (4.7) | **Yüksek** | Doğrulama |
| **Chen ve Zimmermann (2022, CFR 11(2))**: 319 karakteristik açık kaynakla yeniden üretildi. Açıkça anlamlı 161 karakteristiğin %98'i t > 1,96 veriyor. Orijinal ve yeniden üretilen t'ler arasında eğim 0,88, R² %82. Ortalama getiriler sinyalle **monotonik** artıyor. | Hou–Xue–Zhang'a göre daha iyimser: sorun daha çok büyüklüğün küçülmesi ve maliyetler. | — | Sıra kovası monotonluk testi (4.7) | Orta | Doğrulama |
| **Green, Hand ve Zhang (2017, RFS 30(12))**: 94 karakteristik birlikte test edildi. Mikro-cap dışı hisselerde 1980–2014 boyunca yalnız **12'si bağımsız**. 2003'ten beri yalnız **2'si** bağımsız ve hedge getirileri sıfırdan farksız. | ABD. | — | Az sinyal yeterli | Yüksek | Sadelik |
| **Freyberger, Neuhierl ve Weber (2020, RFS 33(5))**: adaptif grup LASSO ile seçim. Önceden bulunan tahminleyicilerin çoğu artımsal bilgi taşımıyor; doğrusal olmayan ilişkiler önemli. | ABD. | — | Kırpma ve eşik gibi basit doğrusal olmayan dönüşümler yeterli | Orta | Sadelik |

### 2.2 Sinyal düzeyi: Profit Growth / Momentum / Quality / Low Risk / Kısa Vadeli Dönüş → dönüş stratejisi

| Bulgu (yazar, yıl, örneklem, dönem, etki) | Replikasyon / GP / TR kanıtı | Durum | Platformda karşılığı (tek satır) | Öncelik | Rol |
|---|---|---|---|---|---|
| **ΔROE (dRoe; JKP niq_be_chg1, çeyreklik ROE'nin 4 çeyrek önceye göre değişimi).** HXZ 2020: ayda %0,76 (t = 5,43) [Ö]. | JKP'de Profit Growth teması; gelişmekte olan piyasalarda tema düzeyinde rakam doğrulanmadı. Türkiye'ye özgü kanıt bulunamadı. | **P** (K10 skorunda ROE değişimi var; ROE'nin negatiften pozitife geçişine izin veren olay kapısı yok) | `OzsermayeKarlilikYillik() - OzsermayeKarlilikYillik("",-4) >= 10` | **Yüksek** | Kapı (olay) + skor |
| **Fiyatla ölçeklenmiş kâr değişimi (ΔE/P, SUE'nin sade hâli).** Chan, Jegadeesh ve Lakonishok (1996): geçmiş getiri ve geçmiş kazanç sürprizi, birbiri kontrol edildikten sonra da güçlü getiri kayması öngörüyor ve sonradan dönüş zayıf. Novy-Marx (2015): fiyat momentumunu açıklayan kazanç momentumu. | van der Hart, Slagter ve van Dijk (2003) gelişmekte olan piyasalarda analist kazanç revizyonu stratejileri; van der Hart, de Zwart ve van Dijk (2005): revizyon stratejisinde 5 yıl boyunca belirgin geri dönüş yok. **Uyarı:** ABD'de PEAD (kazanç açıklaması sonrası kayma) büyük hisselerde 2006'dan beri yok (Martineau 2022). | **N** | `(NetKarYillik() - NetKarYillik("",-4)) / PD() >= 0.05` | **Yüksek** | Kapı (olay) + skor |
| **Abr (kazanç açıklaması çevresinde anormal getiri).** HXZ: ayda %0,74 (t = 5,85), q-alfa %0,66 [Ö]. | Güçlü replikasyon. | N | Platformda açıklama tarihi yok → **uygulanamaz** | Düşük | — |
| **Gelir sürprizi / satış ivmesi (JKP saleq_su).** | Profit Growth teması. | P (C32: satış büyümesi > %50 alternatifi) | `NetSatisBuyumeYillik() > Tufe(12)` | Düşük-Orta | Bonus |
| **Marj değişimi (JKP dsale_dsga, dgp_dsale).** | JKP'de Profit Growth ve Quality temaları. | N | `FAVOKMarjiYillik() > FAVOKMarjiYillik("",-4)` (imza doğrulanmalı) | Orta | Teyit ("sahte kâr" koruması) |
| **Ardışık kâr artışı (JKP ni_inc8q).** | JKP'de **Quality** teması. | N | `IF(NetKar("TL",0)>NetKar("TL",-4),1,0)+IF(NetKar("TL",-1)>NetKar("TL",-5),1,0)` (imza doğrulanmalı) | Orta | Teyit (2 çeyrek üst üste yıllık artış) |
| **Fiyat momentumu 12-1 / 6-1 (JKP ret_12_1, ret_6_1).** | **TR:** momentum 2005'ten sonra anlamlı (Gökçen 2026); 2005–2024 için alfa yılda %11,88 [Ö]. Kaldırım (2017): BIST 100'de 2008–2015 arasında 9–12 aylık oluşum/tutuş momentumu var, 1 hafta atlama ile daha güçlü [Ö]. **Karşı kanıt:** Bildik ve Gülay (2007), İMKB'de karşıt (contrarian) stratejinin yılda yaklaşık %15 getirdiğini buluyor (eski dönem). Gelişmekte olan piyasalar: Doğu Avrupa hariç momentum var (Cakici, Fabozzi ve Tan 2013). | **T** (K10) | `Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d")` | **Yüksek** | Skor |
| **52 hafta zirveye yakınlık (JKP prc_highprc_252d).** George ve Hwang (2004): momentum kârlarının büyük kısmını açıklıyor, geçmiş getiriden daha iyi tahmin ediyor ve uzun vadede geri dönmüyor. | Gelişmekte olan piyasalarda makine öğrenmesinin **1 numaralı** değişkeni (Hanauer ve Kalsbach 2023) [Ö]. | **T** (K10) | `Teknik.Indicator("C/HHV(H,252)","d")` | **Yüksek** | Skor |
| **Ara dönem momentum ret_12_7 (JKP'de Profit Growth temasında).** | Temel momentumla birlikte kümeleniyor. | N | `Teknik.Indicator("Ref(C,-147)/Ref(C,-252)","d")` | Düşük | Bonus |
| **Kısa vadeli dönüş (ret_1_0).** | Gu–Kelly–Xiu: en önemli fiyat trendi grubunda. Bildik–Gülay: İMKB'de 1 aylık karşıt strateji kârlı. | **P** (K10'da "1 ay getiri > −15" ve aşırı uzama cezası) | `IF(Getiri("s1a","TL") > 40, 1, 0)` | Orta | Ceza |
| **MAX / idiyosenkratik volatilite (JKP Low Risk).** Bali, Cakici ve Whitelaw (2011): en yüksek MAX'lı hisseler en düşüklerden ayda %1'den fazla geride. | **TR:** düşük riskli hisseler her risk ölçüsüyle yüksek risklileri geçiyor (Gökçen 2026). Gelişmekte olan piyasalarda idiyosenkratik volatilite makine öğrenmesinin 2 numaralı değişkeni [Ö]. | **N** | `Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")` (imza doğrulanmalı) | Orta | Ceza / koruma |
| **Likidite / devir hızı.** | Gu–Kelly–Xiu: piyasa değeri, dolar hacmi ve alım-satım farkı. Leippold, Wang ve Zhou (2022, Çin): **likidite en önemli değişken**, perakende yatırımcı ağırlığı kısa vadeli öngörülebilirliği artırıyor. | N | `Log(Teknik.Indicator("Mov(C*V,20,S)","d"))` | Orta | Kapı (kapasite) — nominal TL eşiği enflasyonla bozulur |
| **Sıkıntı riski / O-score / F-skor (JKP Quality).** Piotroski (2000); Campbell, Hilscher ve Szilagyi (2008). | Bölüm 11'e bakınız. | **T** (C32 F-skor, düşen bıçak filtresi, K10 NetBorç/FAVÖK) | `NetBorcFavokYillik() < 4` | Orta | Koruma |

### 2.3 JKP'nin 13 teması → "Dipten Dönüş" haritası

Küme üyelikleri JKP *Global Factor Data Documentation*'dan alındı. JKP WP'de 13 tema: Accruals, Debt Issuance, Investment, Leverage, Low Risk, Momentum, Profit Growth, Profitability, Quality, Seasonality, Size, Skewness, Value. Güncel dokümantasyonda "Skewness" yerine **Short-Term Reversal** kümesi var.

| Tema | Örnek JKP sinyalleri | Dönüşteki rolü | Platform karşılığı | Durum |
|---|---|---|---|---|
| **Profit Growth** | niq_be_chg1 (ΔROE çeyreklik), niq_at_chg1 (ΔROA), niq_su (SUE), saleq_su (gelir sürprizi), dsale_dsga, dsale_drec, dsale_dinv, ocf_at_chg1 (Δ faaliyet nakit akışı/aktif), tax_gr1a (vergi gideri sürprizi), ret_12_7, sale_emp_gr1 | **Kimlik (olay kapısı)** + skor | ΔROE, ΔE/P, `NetKar("TL",0)` ile `NetKar("TL",-4)` karşılaştırması, `IsletmeFaaliyetlerdenNakitAkis()` | P/N |
| **Momentum** | ret_12_1, ret_9_1, ret_6_1, ret_3_1, prc_highprc_252d, resff3_12_1 (artık momentum), seas_1_1na | Piyasa teyidi + skor | 6-1 momentum, `C/HHV(H,252)`, C > MA200 | T |
| **Quality** | f_score, ni_inc8q, niq_be, o_score, qmj, cop_at, gp_at, ope_be … | Teyit (ardışık artış), koruma (O-score/F-skor) | F-skor (C32), 2 çeyrek seri | T/N |
| **Low Risk** | ivol_capm_21d, rmax1_21d (MAX), rvol_21d, beta_60m, earnings_variability, zero_trades, turnover_126d | Koruma ve ceza | `HHV(C/Ref(C,-1),21)`, `Stdev(...)` | N |
| **Short-Term Reversal** | ret_1_0, rmax5_rvol_21d, iskew | Ceza (son 1 ayda aşırı sıçrayanlar) | `Getiri("s1a","TL")` | P |
| **Value** | E/P, B/M, EBITDA/EV … | TR'de en güçlü prim (Gökçen 2026). Profil 2'deki "çarpan düşüşü" ΔE/P ile yakalanır | `FK()`, `FDFAVOK()` | T (C32) |
| **Profitability** | ROE düzeyi, kârlılık | Kapıda düzey koşulu (ROE > 0 ya da E > 0) | `OzsermayeKarlilikYillik() > 0` | T |
| **Leverage / Debt Issuance** | borç, ihraç | Koruma (sıkıntılı şirket) | `NetBorcFavokYillik()` | T |

---

## 3. Makine öğrenmesi: en önemli değişkenler hangileri, hangileri dönüşe girer?

| Bulgu (yazar, yıl, örneklem, dönem, etki) | GP / TR kanıtı | Durum | Platformda karşılığı | Öncelik | Rol |
|---|---|---|---|---|---|
| **Gu, Kelly ve Xiu (2020, RFS 33(5))**: yaklaşık 30.000 hisse, 1957–2016, 94 karakteristik, test dönemi 1987–2016 [Ö]. Bütün yöntemler aynı baskın sinyallerde birleşiyor: **momentum, likidite ve volatilitenin varyasyonları** (özette). Makaleye göre en bilgili grup fiyat trendi (hisse momentumu, sektör momentumu, kısa vadeli dönüş). Onu likidite (piyasa değeri, dolar hacmi, alım-satım farkı) ve volatilite/beta izliyor. NN uzun-kısa desil Sharpe: değer ağırlıklı 1,35, eşit ağırlıklı 2,45 [Ö]. | ABD. Kazanç sürprizi ve ROE değişimi baskın değişkenler arasında **değil**. | — | — | Yüksek | Rol dağılımı |
| **Hanauer ve Kalsbach (2023, EMR 55, 101022)**: 32 gelişmekte olan piyasa (Çin A hisseleri hariç), 1990–2021, örnek dışı 2002–2021, 36 karakteristik [Ö]. Doğrusal olmayan modeller doğrusallardan üstün. Arbitraj engeli yüksek hisselerde öngörülebilirlik daha yüksek. Maliyet, açığa satış kısıtı ve yalnız büyük hisseler koşullarında bile net getiri anlamlı. | En önemli değişkenler [Ö, Robeco özeti]: **1) fiyat/52 hafta zirve, 2) idiyosenkratik volatilite, 3) devir hızı.** Momentum, kısa vadeli dönüş, F/K ve kârlılık ilk 15'te. Türkiye'nin örneklemde olup olmadığı doğrulanmadı. | — | `C/HHV(H,252)` (T), volatilite cezası (N) | **Yüksek** | Skor + ceza |
| **Leippold, Wang ve Zhou (2022, JFE 145(2))**: Çin. Likidite en önemli değişken, işlem maliyeti belirleyici. Perakende yatırımcı ağırlığı küçük hisselerde kısa vadeli öngörülebilirliği artırıyor. | BIST de perakende ağırlıklı → kısa vade dönüş ve likidite etkileri muhtemelen önemli (çıkarım, test edilmeli). | N | Likidite tabanı | Orta | Kapı |
| **Freyberger, Neuhierl ve Weber (2020); Green, Hand ve Zhang (2017)** | Az sayıda karakteristik yeterli; doğrusal olmayan dönüşümler önemli. | — | Kırpılmış (Min/Max) bileşenler | Orta | Sadelik |

**Dönüş stratejisine girecek ML değişkenleri:**
1. **52 hafta zirveye yakınlık** (skor). Gelişmekte olan piyasalarda 1 numara [Ö]; dönüş hikâyesinde "piyasa inanıyor" sinyalini zaten taşıyor.
2. **6-1 ay momentum** (skor). Son ay atlanır, böylece kısa vadeli dönüşten arınır.
3. **Kısa vadeli dönüş** (ceza). Son 1 ayda aşırı sıçrayan hisse ertesi ay geri verme eğiliminde.
4. **Volatilite/MAX** (ceza ya da koruma). Türkiye'de yüksek risk düşük getiri (Gökçen 2026).
5. **Likidite** (kapasite kapısı). Asıl gerekçe getiri değil uygulanabilirlik.

Temel değişim sinyalleri ML önem sıralamasında üstte olmasa da replikasyonda sağlam (Hou–Xue–Zhang dRoe, Abr). Ayrıca kullanıcının tanımladığı stratejinin **özünü** oluşturuyor. Bu yüzden skorun bir bileşeni değil, **olay kapısı** olarak kullanılmalı.

---

## 4. Doğrulama protokolü (5 hisse, aylık, 2005–2026 ≈ 258 ay)

### 4.1 Gürültünün büyüklüğü [H]
Hesaplar Lo (2002) yaklaşımıyla, bağımsız ve aynı dağılımlı getiri varsayımıyla yapıldı (SE = standart hata).
- **Kazandıran ay oranı:** p = 0,72 için SE = √(p(1−p)/258) ≈ **0,028**, yani %72 ile %77 arası yaklaşık 1,8 SE. Gerçek test, iki varyantın **aynı aylardaki** farklarına bakan eşleştirilmiş testtir (işaret testi ya da fark serisi t).
- **Yıllık Sharpe (1,2):** SE ≈ √((1 + SR²/2)/T)·√12 ≈ **0,22**. Yarım dönem (129 ay) için ≈ **0,31**.
- **Sharpe'ın yıllıklaştırılması:** pozitif otokorelasyon yıllık Sharpe'ı %65'e kadar şişirebilir (Lo 2002). √12 ile çarpmak ancak özel koşullarda geçerli. Bu yüzden Newey–West (NW) ve aylık seri kullanılmalı.

### 4.2 Deflated Sharpe Ratio (Bailey ve López de Prado 2014, JPM 40(5))
**Formül.** SR̂ aylık (yıllıklaştırılmamış), T ay sayısı, γ̂₃ çarpıklık, γ̂₄ basıklık (ham; normal dağılımda 3).

```
DSR = Φ( (SR̂ − SR₀) · √(T−1) / √(1 − γ̂₃·SR̂ + ((γ̂₄ − 1)/4)·SR̂²) )
SR₀ = √V[{SR̂ₙ}] · ( (1−γ)·Φ⁻¹(1 − 1/N) + γ·Φ⁻¹(1 − 1/(N·e)) ),   γ ≈ 0,5772 (Euler–Mascheroni)
```

- N: **bağımsız** deneme sayısı.
- V[{SR̂ₙ}]: denenen varyantların Sharpe'larının varyansı.
- Karar: **DSR ≥ 0,95** ise "seçim yanlılığı ve normal olmayan dağılım düzeltmesinden sonra gerçek Sharpe > 0" denir.
- Makaledeki örnek: yıllık SR 2,5, 5 yıllık günlük veri (T = 1250), N = 88. DSR ≈ 0,90, yani %95 eşiğinin altında [Ö].

**Uygulama.** Offline simülasyonda her varyantın aylık getiri serisi zaten var. Turdaki bütün varyantların Sharpe'larından V hesaplanır; N yerine korelasyonla düzeltilmiş "etkin N" kullanılır (kümeleme ya da sabit-durum sayımı).

**Örnek [H]** (varsayım: T = 258, çarpıklık 0,3, basıklık 5, varyantların aylık Sharpe standart sapması 0,10):
- N = 100, yıllık SR 1,2 → DSR 0,93 (geçmez).
- N = 100, yıllık SR 1,5 → DSR 0,997 (geçer).
- N = 30, yıllık SR 1,2 → DSR 0,99 (geçer).

**Önemli:** stratejilerin mutlak Sharpe'ı (yaklaşık 1,2–1,5) şans düzeyinin çok üstünde. Asıl sorun varyantlar arasındaki **küçük iyileştirmeler**. DSR'yi **fark serisine** de uygulayın (varyant − taban). "İyileştirme Sharpe'ı"nın şanstan büyük olup olmadığını bu söyler.

### 4.3 PBO / CSCV (Bailey, Borwein, López de Prado ve Zhu 2017, J. Computational Finance 20(4))
1. **M matrisi:** T × N (aylar × varyantlar), aylık getiriler. Bir turdaki bütün aday varyantlar sütun olur.
2. **Bölme:** M satır bazında eşit büyüklükte, çift sayıda S parçaya bölünür. Yazarların önerisi S = 16. Bizde 258 ayla S = 16 yaklaşık 16 aylık bloklar demek; S = 10 ise yaklaşık 26 aylık bloklar.
3. **Kombinasyonlar:** S parçadan S/2'lik bütün kombinasyonlar alınır. C(16,8) = 12.870, C(10,5) = 252 [H].
4. **Eğitim/test:** her kombinasyon c için eğitim kümesi J = seçilen S/2 blok, test kümesi J̄ = kalan blokların tamamı.
5. **Seçim:** J üzerinde en iyi varyant n* bulunur (ör. Sharpe ya da kullanıcının birincil ölçüsü).
6. **Göreli sıra:** n*'ın J̄ içindeki göreli sırası ω̄_c = sıra/(N+1) hesaplanır. Logit λ_c = ln(ω̄_c/(1−ω̄_c)).
7. **PBO = P(λ ≤ 0):** örnek içinde en iyi olanın örnek dışında medyanın altında kalma oranı.
8. **Tamamlayıcı ölçüler:**
   - Performans bozulması: örnek içi ve örnek dışı performans arasındaki regresyon eğimi.
   - Kayıp olasılığı: P(örnek dışı R_n* < 0).
   - Stokastik baskınlık: seçim yöntemi rastgele seçimden iyi mi?

Kaba kural (literatür değil, öneri): **PBO ≤ 0,25** kabul, 0,25–0,50 şüpheli, **> 0,50** aşırı uyum. Yazarlar granülerlik için N'in 10'dan belirgin biçimde büyük olmasını öneriyor [Ö]. Küçük turlarda (N ≈ 6) PBO kaba kalır; bu yüzden turlar birleştirilerek ailece hesaplanmalı.

### 4.4 Minimum backtest uzunluğu (MinBTL; Bailey ve diğerleri 2014, Notices AMS 61(5))
`MinBTL ≈ ((1−γ)Φ⁻¹(1−1/N) + γΦ⁻¹(1−1/(Ne)))² / E[max SR]²  <  2·ln(N) / E[max SR]²` (yıl; SR yıllık)

- Makaledeki ifade: "5 yıllık veriyle 45 konfigürasyona bakmak bile yanıltabilir." Formül tam bunu veriyor: N = 45, hedef SR 1,0 → **5,0 yıl** [H].
- 21,5 yılda sıfır yetenekli N stratejinin **beklenen en iyi yıllık Sharpe'ı** [H]:

| N | 10 | 20 | 45 | 100 | 200 | 500 |
|---|---|---|---|---|---|---|
| Şanstan beklenen max yıllık SR | 0,34 | 0,41 | 0,48 | 0,55 | 0,60 | 0,66 |

- **İyileştirmeler için MinBTL** [H]. Varsayım: aylık fark ortalaması d, fark standart sapması s.

| d / s | İyileştirme SR'si (yıllık) | N = 10 | N = 20 | N = 50 | 21,5 yılda en fazla bağımsız deneme |
|---|---|---|---|---|---|
| %0,3 / %3 | 0,35 | 20,7 yıl | 30,1 yıl | 43,2 yıl | **≈ 10** |
| %0,5 / %4 | 0,43 | 13,2 yıl | 19,3 yıl | 27,6 yıl | **≈ 25** |
| %0,5 / %3 | 0,58 | 7,4 yıl | 10,8 yıl | 15,5 yıl | ≈ 150 |
| %1,0 / %5 | 0,69 | 5,2 yıl | 7,5 yıl | 10,8 yıl | ≈ 860 |

→ **Ayda +%0,3–0,5 gibi küçük iyileştirmeler için bütün projede yalnızca 10–25 bağımsız deneme hakkı var.** Bu, ön kayıt ve tur başına aday sınırının sayısal gerekçesi.

### 4.5 Walk-forward, iki yarı ve genişleyen pencere
- **İki yarı (2005–2015 / 2016–2026):** saf gürültü bir varyantın iki yarıda birden iyileşme gösterme olasılığı, yarılar bağımsızsa yaklaşık %25. Tek başına zayıf bir süzgeç, t eşiğiyle birlikte güçlü.
- **İleri yönlü seçim (walk-forward):** düzeyler (eşikler) yalnız 2005–2015'te seçilir ve kilitlenir; 2016–2026 dokunulmamış test olur. Sonra ters yön denenir (2016–2026'da seç, 2005–2015'te sına). Bu, S = 2 olan CSCV'ye denk.
- **Rejim bloğu:** 2024+ (TMS 29) ayrı raporlanmalı. Enflasyon muhasebesi temel değişim ölçülerini bozuyor (brief).

### 4.6 Ön kayıt (Harvey 2017, JF 72(4))
Harvey'nin önerisi: veriye bakmadan önce ekonomik gerekçe, hipotez ve veri yöntemi yazılır, sonuçların **hepsi** raporlanır. p = 0,05 (z = 1,96) için minimum Bayes faktörü 0,147; eşit önsel olasılıkla "Bayesçi p" ≈ 0,13 [Ö] (exp(−1,96²/2) = 0,147 olarak doğrulandı [H]). Yani p = 0,05, sıfır hipotezinin hâlâ yaklaşık %13 olasılıkla doğru olması demek.

**Pratik ön kayıt şablonu** (her tur için tek sayfa): hipotez · aday listesi (en fazla 6) · düzeyler · birincil ölçü · kabul kuralı · tur sayacı N (kümülatif) → turun **sonunda** bütün adayların sonuçları loga yazılır, elenenler dahil.

### 4.7 Terfi kuralı: mevcut kural ve önerilen ekler

| Ölçüt | Mevcut | Önerilen | Gerekçe |
|---|---|---|---|
| Son sermaye | ≥ taban + %5 | Aynı | Kullanıcı kuralı |
| Kazandıran ay oranı | ✓ | ≥ taban **ve** eşleştirilmiş işaret testi negatif olmamalı | SE ≈ 2,8 puan [H] |
| Sharpe / K-Ratio | ✓ | ≥ taban (ikisi de) | Kullanıcı önceliği |
| Kriz ayları | ✓ | Önceden sabitlenmiş kriz ayı listesi; toplam getiri ≥ taban | Daniel ve Moskowitz (2016) |
| İki yarı | ✓ | İki yarıda da aylık fark ortalaması > 0 | Saf gürültü için ≈ %25 geçiş [H] |
| Plasebo | ✓ | Aynı kapı havuzundan rastgele 5 hisse × 1000; aday ≥ %90'ını geçmeli | Kapı mı skor mu iş yapıyor, ayırır |
| **NW t (fark serisi)** | ≥ 1,5 | **≥ max(1,5; t\*(N_tur))**, t\* = E[max Z_N] | 1,5 ≈ 8–10 saf şans denemesinin beklenen en iyisi [H] |
| **Komşu sıra (yeni)** | — | 6–10. sıradaki 5'li portföy de tabanın 6–10'unu geçmeli; sıra kovalarında (1–5, 6–10, 11–15, …) getiri **monoton** düşmeli | Chen ve Zimmermann (2022): sinyalde monotonluk; 5 hissede sıra gürültüsünü ayırır |
| **Kaçan kazananlar (kullanıcı kuralı)** | ✓ | Yalnız **teşhis**; bulgudan doğan değişiklik ön kayda girer ve öbür yarıda sınanır | Geriye bakış aşırı uyumu |
| **Final (yeni)** | — | Şampiyon için DSR ≥ 0,95 (N = projedeki bütün denemeler); aday ailesinde PBO ≤ 0,25 | Bailey ve López de Prado |

**t\* tablosu** (E[max Z_N], bağımsız denemeler; Monte Carlo ile kontrol: N = 10 için 1,54, N = 20 için 1,86) [H]:

| N (turdaki aday) | 3 | 5 | 6 | 8 | 10 | 12 | 15 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| t\* | 0,85 | 1,19 | 1,30 | 1,46 | 1,57 | 1,66 | 1,77 | 1,90 | 2,07 | 2,28 |

Saf gürültüde t ≥ 1,5'i geçme olasılığı aday başına %6,7. N = 10 için en az bir sahte geçiş olasılığı **%50**, N = 20 için **%75**, N = 50 için %97 [H]. Varyantlar birbiriyle korelasyonlu olduğundan etkin N daha küçüktür. Yine de **"tur başına en fazla 6 aday"** kuralı t ≥ 1,5'i makul kılar (t\*(6) = 1,30).

Harvey ve Liu (2015, *Backtesting*, JPM) "her Sharpe'a %50 kesinti" yaklaşımını reddediyor. Önerdikleri kesinti doğrusal değil: sınırdaki stratejiler sert, çok güçlü olanlar hafif cezalandırılıyor.

---

## 5. Basit kurallar ve karmaşık modeller

| Bulgu (yazar, yıl, örneklem, dönem, etki) | Kanıt | Durum | Platformda karşılığı | Öncelik | Rol |
|---|---|---|---|---|---|
| **DeMiguel, Garlappi ve Uppal (2009, RFS 22(5))**: 7 veri setinde 14 model. Sharpe, kesinlik eşdeğeri getiri ve devir hızında **hiçbiri 1/N'yi tutarlı biçimde yenemiyor**. Örnek ortalama-varyans modelinin 1/N'yi geçmesi için 25 varlıkta yaklaşık 3000 ay, 50 varlıkta yaklaşık 6000 ay veri gerekiyor. | Tahmin hatası, çeşitlendirme kazancını yok ediyor. | T (eşit ağırlık) | 5 hisse eşit ağırlık **korunmalı** | Yüksek | Kurgu |
| **Dawes (1979, Am. Psychologist 34(7))**: eşit ağırlıklı "uygunsuz" doğrusal modeller tahminde şaşırtıcı biçimde sağlam. | Psikometri ve karar bilimi klasiği. | N | Skor = bileşenlerin **eşit ağırlıklı** toplamı | **Yüksek** | Skor |
| **Fernandez-Perez, Fuertes ve Miffre (2019, JBF 105)**: dört varlık sınıfında stil entegrasyonu. **Eşit ağırlıklı entegrasyon** riske göre düzeltilmiş performansta rakipsiz ve devir hızı düşük. | Optimizasyon, rotasyon ve zamanlama yöntemleri ondan iyi değil. | N | Eşit ağırlıklı bileşik skor | Yüksek | Skor |
| **Stambaugh ve Yuan (2017, RFS 30(4))**: 11 anomalinin **sıra ortalaması** iki "yanlış fiyatlama" faktörü üretiyor; 4 ve 5 faktörlü alternatiflerden iyi. | Jacobs (2016): aynı skor 45 ülkede çalışıyor. | N | Kesitsel sıra fonksiyonu yok → **kırpılmış (0–1) dönüşüm** sıranın vekili | Orta | Skor |
| **Asness, Moskowitz ve Pedersen (2013, JF 68(3))**: 8 piyasa ve varlık sınıfında değer ve momentum primi. Değer ile momentum birbiriyle **negatif korelasyonlu**. | Basit birleşim çeşitlendirme sağlıyor. | P | Temel (ΔE/P) + fiyat (momentum) bileşenleri tek skorda | Orta | Skor |
| **Asness, Frazzini ve Pedersen (2019, RAST 24(1))**: kârlılık, büyüme ve güvenlik bileşenlerinden oluşan kalite bileşik skoru (QMJ); ABD ve 24 ülkede anlamlı. | Basit bileşik skor tasarımı. | P (C32 F-skor) | — | Düşük | — |
| **Piotroski (2000, JAR 38)**: 9 ikili kriterin eşit ağırlıklı toplamı (F-skor). | En bilinen sade bileşik örnek. | T (C32) | — | — | — |
| **Novy-Marx (2015, NBER w21329)**: çok sinyalli strateji seçimi ağır aşırı uyum yanlılığı taşıyor; n adaydan en iyi k'yı birleştirmek, nᵏ adaydan en iyi tekini seçmek kadar yanlı. Özetteki örnekler: 20 adaydan en iyi 3 ≈ 1780 adaydan en iyi tek; 40 adaydan en iyi 5 ≈ yarım milyon adaydan en iyi tek [Ö, Alpha Architect]. | Kritik t değerleri standart düzeyin "birkaç katı" olabilir. | — | Skor bileşen sayısını 3'te **sabitle**, bileşenleri ön kayıtla seç | **Yüksek** | Doğrulama |
| **DeMiguel, Martín-Utrera, Nogales ve Uppal (2020, RFS 33(5))**: işlem maliyetleri dikkate alındığında anlamlı karakteristik sayısı 6'dan 15'e çıkıyor, çünkü farklı sinyallerin işlemleri birbirini kısmen götürüyor. | Bileşik skorun devir hızını düşürmesi lehine. | — | Bileşik skor > ardışık kapılar (devir hızı) | Orta | Kurgu |

**Az parametre neden aşırı uyumu azaltır?**
- Her eşik ve ağırlık, bir arama boyutudur. 3 bileşenli, eşit ağırlıklı ve önceden kırpma sınırları yuvarlak sayılarla seçilmiş bir skorda serbest parametre yok denecek kadar azdır.
- K10'daki gibi 12 kapı ve 6 ağırlıklı bileşenin her biri ayrı bir N katkısı yapar. Novy-Marx'ın nᵏ kuralına göre etkin arama uzayı katlanarak büyür.
- **Plato kuralı (genel uygulama, kaynak değil):** eşik, en iyi sonucun tepesinden değil, komşu düzeylerin de iyi olduğu düzlüğün ortasından seçilmeli.

---

## 6. Dönüş stratejileri için gerçekçi beklenti

| Bulgu (yazar, yıl, örneklem, dönem, etki) | Anlamı | Durum | Platformda karşılığı | Öncelik | Rol |
|---|---|---|---|---|---|
| Hou–Xue–Zhang: dRoe, Abr ve Sue 1 aylık tutuşta en güçlü; ufuk uzadıkça zayıflıyor [Ö] | Sinyal "taze olay" iken değerli → **olay tazeliği** koşulu | P (K10 ROE teyidi) | `NetKar("TL",0) > NetKar("TL",-4)` | Orta | Kapı ek |
| McLean–Pontiff: yayın sonrası −%58 (ABD); JKP: örnek dışı alfa yaklaşık 1/3 düşük [Ö] | **Canlı performans için backtest'i aşağı çek.** Kaba kural (öneri): canlıda Sharpe'ın yarısı ile üçte ikisi arası | — | — | Yüksek | Beklenti |
| Jacobs–Müller 2020: ABD dışında güvenilir yayın sonrası düşüş yok | BIST'te primler sürebilir | — | — | Orta | Beklenti |
| **Gökçen (2026, Borsa Istanbul Review 100884)**: 14 tahminleyici, BIST. Değer en güçlü (yılda %17'nin üstünde). Büyüklük, kârlılık ve momentum **yalnız 2005'ten beri** anlamlı. Düşük risk yüksek riski geçiyor. Enflasyon ve kur riski primleri açıklamıyor. Uzun-tek yönlü çok faktörlü portföy, gelişmekte olan piyasalar endeksine göre dolar bazında %13 alfa ve 0,64 Sharpe veriyor. | **En doğrudan TR kanıtı.** Momentum alfası 2005–2024'te yılda %11,88 [Ö] | — | — | **Yüksek** | Beklenti |
| Chen ve Velikov (2023, JFQA 58(3)): 204 anomali; alım-satım farkı, yayın sonrası etki ve modern ticaret dönemi hesaba katıldığında **ortalama anomali net ayda 4 baz puan**, en güçlüleri en fazla 10 baz puan, birleşimler yaklaşık 20 baz puan. | ABD uzun-kısa. Long-only ve 5 hisselik konsantrasyon farklı ama yön uyarıcı. | — | — | Orta | Beklenti |
| Novy-Marx ve Velikov (2016, RFS 29(1)): aylık tek yönlü devir hızı < %50 olan anomalilerin çoğu maliyet sonrası anlamlı kalıyor; daha yüksek devirlilerin azı kalıyor. **En etkili basit maliyet azaltıcı: al/tut bandı.** | 5 hisse aylık → devir hızı yüksek olabilir | N | "Elde tutulan hisse ilk 10'da kalıyorsa tut" (platform desteği belirsiz) | Orta | Kurgu |
| Martineau (2022, CFR 11(3–4)): ABD'de PEAD büyük hisselerde 2006'dan, mikro-cap'lerde son yıllarda kayboldu. | Kazanç sürprizi primleri piyasa geliştikçe eriyor → 2016–2026 yarısını ayrı izle | — | — | Orta | Uyarı |
| van der Hart ve diğerleri (2003; 2005): değer, momentum ve kazanç revizyonu stratejileri gelişmekte olan piyasalarda büyük kurumsal yatırımcı kısıtlarında bile anlamlı. Açıklama risk değil davranışsal. | Gelişmekte olan piyasalarda kazanç momentumu destekleniyor | — | — | Orta | Beklenti |
| **Daniel ve Moskowitz (2016, JFE 122(2))**: momentum çöküşleri piyasa düşüşü ve yüksek volatilite sonrasındaki "panik" durumlarında, toparlanmayla birlikte geliyor. Dinamik momentum alfayı ve Sharpe'ı yaklaşık iki katına çıkarıyor. | Dönüş adayları yüksek betalı; panik sonrası toparlanmada momentum kapısı (MA200) geç kalır | P (düşen bıçak filtresi) | Kriz rejiminde momentum ağırlığını azalt: `IF(Getiri("s12a","TL","XUTUM") < 0, …)` | Düşük | Rejim |
| **Novy-Marx (2015, NBER w20984)**: fiyat momentumunun başarısı kazanç momentumundan geliyor. Geçmiş getiri kontrol edilerek kurulan kazanç momentumu stratejisi volatiliteyi düşürüyor ve **momentum çöküşlerini ortadan kaldırıyor**. | Skorda temel bileşen ağırlığı fiyat momentumunu bastırmamalı | N | Skorda ΔE/P bileşeni | Yüksek | Skor |
| **Avramov, Chordia, Jostova ve Philipov (2013, JFE 108(1))**: fiyat momentumu, kazanç momentumu ve diğer anomali kârları **kredi koşulları kötüleşen yüksek riskli şirketlerdeki kısa pozisyonlardan** geliyor. Değer stratejileri ise ayakta kalan sıkıntılı şirketlerin uzun pozisyonundan kazanıyor. Tahakkuk anomalisi istisna. | Long-only dönüş stratejisi kazanç momentumu priminin büyük kısmını alamaz. Kazanç, **değer benzeri "ayakta kalan sıkıntılı"** bacaktan gelir → piyasa teyidi ve sağkalım kanıtı şart | — | — | **Yüksek** | Uyarı |

---

## 7. Kapı (filtre) mı, sıralama (skor) mı?

| Bulgu (yazar, yıl, örneklem, dönem, etki) | Sonuç | Durum | Platformda karşılığı | Öncelik | Rol |
|---|---|---|---|---|---|
| **Fitzgibbons, Friedman, Pomorski ve Serban (2017, J. Investing 26(4))**: long-only stil yatırımında "portföy karışımı" ile "entegre portföy" (tek bileşik sıra) karşılaştırması. Yazarlar **entegrasyonu** öneriyor. | Ayrı dilimler bir faktörde iyi, ötekinde kötü hisseleri alıyor | P | Tek skor | Yüksek | Kurgu |
| **Bender ve Wang (2016, JPM 42(5))**: aşağıdan yukarı (menkul kıymet düzeyinde birleşik) kurulum daha iyi; faktörler arası etkileşim performansı anlamlı biçimde etkiliyor. | Entegre lehine | — | — | Orta | Kurgu |
| **Ghayur, Heaney ve Platt (2018, FAJ 74(3))**: düşük-orta takip hatasında portföy karışımı, **yüksek takip hatasında sinyal karışımı** (tek skor) daha iyi. | 5 hisse = çok yüksek takip hatası → tek skor lehine | — | — | **Yüksek** | Kurgu |
| **Leippold ve Rüegg (2018, EFM 24(5))**: sağlam testlerle entegre yaklaşım lehine kanıt yok; entegre yaklaşım düşük risk anomalisine daha duyarlı. | Fark büyük değil → sadelik ve devir hızı belirleyici olsun | — | — | Orta | Kurgu |
| **van der Hart, Slagter ve van Dijk (2003)**: gelişmekte olan piyasalarda çok değişkenli seçim performansı artırıyor. | Bileşik seçim gelişmekte olan piyasalarda işe yarıyor | — | — | Orta | Kurgu |
| **Novy-Marx (2015, w21329)**: her ek sinyal arama uzayını katlıyor. | Kapı sayısı da bir sinyal sayısıdır | — | — | Yüksek | Doğrulama |

**Sentez: tasarım ilkeleri**
1. **Kapı yalnız 3 iş için:**
   - (a) Stratejinin **kimliğini** tanımlamak: dönüş ya da kâr sıçraması olayı.
   - (b) **Asimetrik koruma**: getiriyle ilişkisi doğrusal ya da monoton olmayan riskler (HA < 60, negatif özkaynak, düşen bıçak).
   - (c) **Uygulanabilirlik**: likidite.
2. **Geri kalan her şey tek bileşik skorda:** eşit ağırlık, kırpılmış ve 0–1'e ölçeklenmiş bileşenler.
3. **Kesişim (ardışık sert kapılar) yerine skor:** her sert eşik bir "uçurum" yaratır (ΔROE 9,9 elenir, 10,0 girer) ve havuzu açlığa sokar. Kullanıcının V1.4 deneyiminde ayda yaklaşık 3 hisse geçiyordu. Skor bu süreksizliği yumuşatır.
4. **Kapıları skora sözlük sırasıyla gömmek** (`100·A + 10·B + bileşik`), kesişimin seçiciliğini ve skorun her zaman 5 hisse doldurmasını birleştirir.

---

## 8. Önerilen sade kurgu iskeleti

**Yapı:** 1 sert filtre + 2 kapı (skora gömülü) + 3 bileşenli eşit ağırlıklı skor. Tek kriter satırı, tek skor formülü.

```
// ── KRİTER (sert filtre, tek satır) ─────────────────────────────
HAOran() < 60

// ── SIRALAMA SKORU (tek formül) — Taban T0: ΔE/P sürümü ────────
e0 = NetKarYillik();
e4 = NetKarYillik("",-4);
d  = IF(e0==null, 0, IF(e4==null, 0, (e0 - e4) / PD()));        // ΔE/P: kâr değişimi / piyasa değeri
a  = IF(e0 > 0, IF(d >= 0.05, 1, 0), 0);                          // KAPI A (olay): kâr pozitif + ΔE/P ≥ %5
m  = Teknik.Indicator("C/Mov(C,200,S)","d");
b  = IF(m==null, 0, IF(m > 1, 1, 0));                             // KAPI B (piyasa teyidi): C > MA200
h  = Teknik.Indicator("C/HHV(H,252)","d");
r  = Teknik.Indicator("Ref(C,-21)/Ref(C,-126)","d");
s1 = Min(Max(d, 0), 0.20) / 0.20;                                 // temel ivme   (0–1)
s2 = IF(h==null, 0, Min(Max(h - 0.5, 0), 0.5) / 0.5);             // 52h zirveye yakınlık (0–1)
s3 = IF(r==null, 0, Min(Max(r - 1, 0), 1));                       // 6-1 ay momentum (0–1)
100*a + 10*b + s1 + s2 + s3;
```

**Alternatif olay ölçüsü A1 (ΔROE), ön kayıtlı aday.** `d`, `a` ve `s1` satırlarının yerine geçer. `Ozsermaye()` için imza doğrulanmalı:

```
r0 = OzsermayeKarlilikYillik();  r4 = OzsermayeKarlilikYillik("",-4);  oz = Ozsermaye();
d  = IF(r0==null, 0, IF(r4==null, 0, Min(r0 - r4, 100)));
a  = IF(oz==null, 0, IF(oz > 0, IF(r0 > 0, IF(d >= 10, 1, 0), 0), 0));   // negatif özkaynak tuzağına karşı
s1 = Min(Max(d, 0), 40) / 40;
```

**Neden bu tasarım?**
- **ΔE/P tek değişkenle iki profili birden kapsar.**
  - Profil 1 (zarardan kâra): ör. E/P −%5'ten +%3'e çıkınca d = 0,08.
  - Profil 2 ("çarpanı ciddi düşüren sıçrama"): ör. F/K 40'tan (E/P %2,5) 13'e (E/P %7,5) inince d = 0,05.
- **ΔE/P bankalarda da çalışır** (FAVÖK gerekmez) ve küçük ya da negatif özkaynakta ROE'nin bozulmasından etkilenmez.
- **Yüzde büyüme yerine fark/PD:** küçük ya da negatif tabanda yüzde büyüme anlamsızlaşır.
- **Kırpma (Min/Max):** aşırı uç değerler (tek seferlik kâr, çok küçük PD) skoru ele geçiremez.
- **Sözlük sırası:** her ay 5 hisse garanti. Doldurma sırası A∧B → A∧¬B (önce teknik gevşer) → ¬A∧B (sonra temel gevşer) → kalan. Bu, kullanıcının "katmanlı tamamlama" kuralıyla birebir uyumlu.
- **Bileşenler** literatürün en sağlam üçlüsü: kazanç momentumu (Hou–Xue–Zhang, Novy-Marx), 52 hafta zirve (George–Hwang, Hanauer–Kalsbach) ve 6-1 momentum (JKP, Gökçen). Ağırlıklar eşit (Dawes, Fernandez-Perez ve diğerleri).

---

## 9. Ön kayıtlı test planı

**Genel kurallar:**
- Her tur taban ya da güncel şampiyondan **tek değişken** değiştirir. Tur başına **en fazla 6 aday**; bu durumda t\*(6) = 1,30, kural tabanı 1,5.
- Turlar sırayla yapılır. Bir turda en fazla 1 terfi olur ve önceki turlara geri dönülmez.
- Kümülatif deneme sayacı N bütün projede tutulur: DSR için N = bütün adaylar.
- Önce offline simülasyon; yalnız terfi adayları siteye gider.
- Kaçan kazananlar testi her terfi adayında **teşhis** amaçlı yapılır.

| Tur | Hipotez | Adaylar (düzeyler) | Sabit tutulan |
|---|---|---|---|
| **T0 (taban)** | İskelet (Bölüm 8) | ΔE/P ≥ 0,05 · C > MA200 · HA < 60 · s1+s2+s3 | — |
| **T1 – Olay ölçüsü ve eşiği** | Temel olayın tanımı | 1a ΔE/P ≥ 0,03 · 1b ΔE/P ≥ 0,08 · 1c ΔROE ≥ 5 · 1d ΔROE ≥ 10 · 1e ΔROE ≥ 15 · 1f çeyreklik ΔE/P: `(NetKar("TL",0)-NetKar("TL",-4))/PD() >= 0.0125` | B, C, skor |
| **T2 – Piyasa teyidi** | "Piyasanın da inanması" (kullanıcının momentum hipotezi = **H1**) | 2a B yok (H1'in doğrudan testi) · 2b C > MA100 · 2c 6 ay göreli güç: `Getiri("s6a","TL") > Getiri("s6a","TL","XUTUM")` · 2d `C/HHV(H,252) >= 0.70` | A, C, skor |
| **T3 – Skor bileşenleri** | Eşit ağırlıklı üçlü | 3a s2+s3 (temel yalnız kapıda) · 3b s1 tek · 3c s1+s3 · 3d s1+s2+s3 − kısa vade dönüş cezası `IF(Getiri("s1a","TL")>40,1,0)` | Kapılar |
| **T4 – Korumalar** | Sahte kâr, düşen bıçak, risk | 4a olay tazeliği `NetKar("TL",0) > NetKar("TL",-4)` (a'ya çarpan) · 4b operasyonel teyit `IF(FAVOKYillik()==null,1,IF(FAVOKYillik()>FAVOKYillik("",-4),1,0))` · 4c C32'nin düşen bıçak filtresi (3'te 2) · 4d MAX cezası `IF(Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")>1.09,0.5,0)` | Şampiyon |

Not: 3d ve 4d'deki ceza terimleri skordan **çıkarılır** (`… + s1 + s2 + s3 - ceza`). Ceza ≤ 1 olduğu için hisse kendi katmanında (A/B) kalır, yalnızca katman içindeki sırası düşer.

**Toplam:** yaklaşık 19 aday. MinBTL tablosuna göre ayda yaklaşık %0,5'lik iyileştirmeler için 21,5 yıl veriyle yaklaşık 25 bağımsız deneme hakkı var [H]. Plan bu bütçenin içinde.

**Kabul kuralı:** Bölüm 4.7'deki tablonun **tamamı**. Özetle:
1. Sermaye ≥ taban × 1,05.
2. Kazandıran ay oranı ≥ taban.
3. Sharpe ≥ taban ve K-Ratio ≥ taban.
4. Kriz ayları toplamı ≥ taban.
5. İki yarıda da fark > 0.
6. Plasebo: rastgele 5'li portföylerin ≥ %90'ını geçmeli.
7. NW t (fark, 6 gecikme) ≥ max(1,5; t\*).
8. Komşu sıra (6–10) da iyileşmeli.

**Proje sonunda:** şampiyon için DSR ≥ 0,95 ve bütün aday ailesinde PBO ≤ 0,25 (CSCV, S = 10).

**Durdurma kuralı:** bütçe (yaklaşık 25 bağımsız deneme) dolduğunda yeni aday eklenmez. Ek fikirler yeni ön kayıtla ve **yalnız 2016–2026 verisi kilitli tutularak** denenir.

---

## 10. Denenmemiş en iyi 10 fikir (sadelik ve uygulanabilirlik sırasıyla)

| # | Fikir | Neden (kaynak) | Formül | Durum | Rol |
|---|---|---|---|---|---|
| 1 | **ΔE/P'yi tek olay ölçüsü yapmak** (iki profil, bankalar dahil) | Kazanç momentumu en sağlam Profit Growth sinyali (Hou–Xue–Zhang; Chan–Jegadeesh–Lakonishok; Novy-Marx 2015) | `(NetKarYillik()-NetKarYillik("",-4))/PD() >= 0.05` | N | Kapı + skor |
| 2 | **Kapıları skora sözlük sırasıyla gömmek** | Kesişimin seçiciliği ile her zaman 5 hisse doldurmayı birleştirir (Ghayur ve diğerleri; Fitzgibbons ve diğerleri) | `100*a + 10*b + bileşik` | P | Kurgu |
| 3 | **Eşit ağırlıklı, kırpılmış 3 bileşenli skor** (ΔE/P, 52 hafta zirve, 6-1 momentum) | Dawes 1979; Fernandez-Perez ve diğerleri 2019; Novy-Marx w21329 | `s1+s2+s3` | P | Skor |
| 4 | **Negatif ya da küçük özkaynak koruması** (ROE tuzağı) | Zarar ve negatif özkaynak birlikte pozitif ROE üretir (muhasebe aritmetiği) | `IF(Ozsermaye()>0, …, 0)` | N | Kapı |
| 5 | **Olay tazeliği:** son çeyrekte yıllık bazda kâr artışı | Hou–Xue–Zhang: sinyal kısa ufukta güçlü [Ö] | `NetKar("TL",0) > NetKar("TL",-4)` | P | Kapı ek |
| 6 | **Terfi eşiğini deneme sayısına bağlamak** (t\* = E[max Z_N]) + final DSR/PBO | Harvey–Liu–Zhu; Bailey ve López de Prado; Novy-Marx | Offline sim | N | Doğrulama |
| 7 | **Komşu sıra (6–10) ve sıra kovası monotonluk testi** | Chen ve Zimmermann (2022): getiriler sinyalde monotonik | Offline sim | N | Doğrulama |
| 8 | **Kısa vadeli dönüş cezası** (son 1 ayda > %40) | Gu–Kelly–Xiu; Bildik–Gülay; Leippold–Wang–Zhou (perakende) | `IF(Getiri("s1a","TL")>40,1,0)` | P | Ceza |
| 9 | **MAX/volatilite cezası** | Bali ve diğerleri 2011; Gökçen 2026 (TR düşük risk); Hanauer–Kalsbach idiyosenkratik volatilite #2 [Ö] | `IF(Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")>1.09,0.5,0)` | N | Ceza |
| 10 | **Al/tut bandı:** elde tutulan hisse ilk 10'da kalıyorsa tutulur | Novy-Marx ve Velikov 2016: en etkili basit maliyet azaltıcı; sıra gürültüsünü de azaltır | Platform desteği belirsiz | N | Kurgu |

Yedekte düşük öncelikli fikirler: ara dönem momentum ret_12_7 bonusu; kriz rejiminde momentum ağırlığını azaltma (Daniel–Moskowitz); likidite tabanı (nominal TL eşiği enflasyonla bozulduğu için önce bir göreli ölçü gerekir).

---

## 11. Uyarılar (kırmızı bayraklar)

1. **Sıkıntılı şirket anomalisi** (Campbell, Hilscher ve Szilagyi 2008, ABD, 1981 sonrası): sıkıntılı hisseler beklenmedik biçimde düşük getiri verirken daha volatil ve daha yüksek betalı. Dönüş adaylarının çoğu bir süre önce bu gruptaydı → **piyasa teyidi (B) ve kâr pozitifliği (e0 > 0) birlikte** şart. Yalnız "ROE iyileşiyor" yetmez.
2. **Anomali kârı çoğunlukla kısa bacaktan geliyor** (Avramov ve diğerleri 2013). Long-only bir dönüş stratejisi, akademik uzun-kısa kazanç momentumu priminin büyük kısmını alamaz. Gerçekçi kaynak, "ayakta kalan sıkıntılı" şirketlerdeki değer benzeri yeniden fiyatlama.
3. **Ölü kedi sıçraması ve piyango hisseleri.** Bali ve diğerleri (2011): MAX yüksek hisseler ayda %1'den fazla geride. Gökçen (2026): Türkiye'de düşük risk yüksek riski geçiyor. Bildik–Gülay (2007): İMKB'de 1 aylık karşıt strateji kârlı. → Son ay sıçraması ve tavan serisi cezalandırılmalı.
4. **Momentum çöküşü** (Daniel ve Moskowitz 2016): panik sonrası toparlanmada geçmişin kaybedenleri yükselir. MA200 teyidi ilk toparlanma aylarını kaçırır, tutulan kazananlar ise göreli olarak çöker. Kriz ayları ayrıca raporlanmalı. Kazanç momentumu ağırlığı çöküşü azaltır (Novy-Marx 2015).
5. **Sahte kâr ve tek seferlik kalemler:** varlık satışı, kur kazancı, TMS 29 parasal kazanç. Net kâr sıçrar ama faaliyet kârı sıçramaz. Önlemler: kırpma (s1 ≤ 0,20), operasyonel teyit (aday 4b), 2 çeyrek seri. Sloan (1996) tahakkuk anomalisi bu literatürün klasiği [DY, bu oturumda açılmadı]. Avramov ve diğerlerine göre tahakkuk anomalisi bütün kredi riski gruplarında kârlı kalıyor.
6. **Negatif özkaynak ile ROE tuzağı:** zarar ve negatif özkaynak birlikte pozitif ROE verir; küçük özkaynakta ROE patlar. ΔROE sürümünde `Ozsermaye() > 0` şart, değer kırpılmalı.
7. **Baz etkisi:** `NetKarBuyumeYillik()` gibi yüzde büyüme ölçüleri, taban negatif ya da sıfıra yakınken anlamsız. Fark/PD ya da fark/özkaynak kullanılmalı.
8. **TMS 29 (2024+):** enflasyon muhasebesi değişim ölçülerini bozuyor (brief). 2024–2026 ayrı raporlanmalı; o dönemde terfi kararı tek başına verilmemeli.
9. **Hayatta kalan yanlılığı (sağkalım):** QueenStocks BIST TÜM evreninde **işlemden kaldırılan ve iflas eden** hisselerin geçmişte bulunup bulunmadığı **doğrulanmalı**. Dönüş stratejileri sıkıntılı hisse aldığı için bu yanlılığa en duyarlı strateji tipi.
10. **Geriye bakış aşırı uyumu:** stratejiyi Migros 2016 ve THYAO 2021–22 gibi örnekleri yakalayacak biçimde ayarlamak, ya da kaçan kazananlar listesinden eşik türetmek aynı örneklemde bakarak seçmek demek. Örnekler yalnız **makullük kontrolü** olarak kullanılmalı; her değişiklik ön kayıtla öbür yarıda sınanmalı.
11. **Sinyal erimesi:** McLean–Pontiff ABD'de −%58; Martineau ABD'de PEAD'in büyük hisselerde kaybolduğunu buldu. BIST'te Jacobs–Müller'e göre düşüş beklenmez, ama KAP ve algoritmik işlemler 2016–2026'da sürüklenmeyi azaltmış olabilir → yarılar ayrı izlenmeli.
12. **5 hisse = gürültü:** kazanma oranı standart hatası yaklaşık 2,8 puan, Sharpe standart hatası yaklaşık 0,22 [H]. Tek bir hissenin ilk 5'e girip girmemesi yılı değiştirebilir → komşu sıra testi ve plasebo şart.

---

## 12. Dürüst sınırlar

- **Arama ve okuma:** yaklaşık 25 web araması yapıldı; oturumun web arama bütçesi doldu, sonrası yalnız doğrudan URL ile ilerledi. Yaklaşık 70 sayfa ya da PDF açma girişiminin yaklaşık 55'i başarılı oldu.
- **Açılamayanlar:**
  - Wiley (JF tam metin; 403), SSRN (çoğu 429), Bildik–Gülay Wiley sayfası (403; özet RePEc'ten okundu), AMS Notices PDF'i (403; künye OpenAlex'ten, "45 konfigürasyon" ifadesi EurekAlert basın bülteninden).
  - Hanauer–Kalsbach tam metni açılamadı; değişken önem sırası Robeco özetinden [Ö]. Türkiye'nin örneklemde olup olmadığı doğrulanmadı.
- **Doğrulanamayan içerik:**
  - JKP'de **gelişmekte olan piyasalar için tema bazında** (Profit Growth) replikasyon oranı.
  - JKP'nin JF yayınlanmış sürümündeki kesin oranlar; WP sürümünün rakamları kullanıldı [Ö].
  - Chordia ve Shivakumar (2006) özeti (yalnız künye); Sloan (1996) [DY].
- **Künye tutarsızlığı:** Fitzgibbons ve diğerleri (2017), AQR sayfasında JPM, pm-research kaydında *Journal of Investing* 26(4):153 olarak geçiyor. Burada ikincisi kullanıldı.
- **Platform imzaları doğrulanmadı:** `Ozsermaye()`, `FAVOKYillik("",-4)`, `FAVOKMarjiYillik("",-4)`, `NetKar("TL",-5)`, `Teknik.Indicator("HHV(C/Ref(C,-1),21)","d")`, `Getiri("s6a","TL","XUTUM")`, `Getiri("s12a","TL","XUTUM")`. Sitede ya da simülasyonda tek tek denenmeli.
- **[H] hesapları** bağımsız ve aynı dağılımlı getiri ile bağımsız deneme varsayar. Gerçekte varyantlar korelasyonlu olduğundan etkin N daha küçüktür; tablolar muhafazakâr üst sınır olarak okunmalı. MAX cezasındaki 1,09 eşiği BIST günlük fiyat limitine göre seçilmiş bir örnek; ön kayıtla sabitlenmeli.
- Türkiye'ye özgü **kazanç momentumu ya da PEAD** çalışması bu oturumda bulunamadı (arama bütçesi). Bu boşluk Ajan A/B'nin taramasıyla kapatılmalı.

---

## 13. Kaynakça (doğrulama durumu ve bağlantılar)

| # | Kaynak | Doğrulama |
|---|---|---|
| 1 | Hou, K., Xue, C., Zhang, L. (2020). Replicating Anomalies. *RFS* 33(5): 2019–2133. [NBER w23394](https://www.nber.org/papers/w23394) · [OpenAlex](https://api.openalex.org/works/doi:10.1093/rfs/hhy131) · [NBER PDF](https://www.nber.org/system/files/working_papers/w23394/w23394.pdf) | ✓ özet; momentum rakamları [Ö] |
| 2 | McLean, R. D., Pontiff, J. (2016). Does Academic Research Destroy Stock Return Predictability? *JF* 71(1): 5–32. [OpenAlex](https://api.openalex.org/works/doi:10.1111/jofi.12365) · [RePEc](https://ideas.repec.org/a/bla/jfinan/v71y2016i1p5-32.html) | ✓ özet |
| 3 | Jensen, T. I., Kelly, B., Pedersen, L. H. (2023). Is There a Replication Crisis in Finance? *JF* 78(5): 2465–2518. [NBER w28432](https://www.nber.org/papers/w28432) · [RePEc](https://ideas.repec.org/p/nbr/nberwo/28432.html) · [WP PDF](https://www.nber.org/system/files/working_papers/w28432/w28432.pdf) · [Dokümantasyon (kümeler)](https://jkpfactors.s3.amazonaws.com/documents/Documentation.pdf) | ✓ özet; oranlar [Ö] |
| 4 | Jacobs, H., Müller, S. (2020). Anomalies across the globe: Once public, no longer existent? *JFE* 135(1): 213–230. [RePEc](https://ideas.repec.org/a/eee/jfinec/v135y2020i1p213-230.html) | ✓ |
| 5 | Harvey, C. R., Liu, Y., Zhu, H. (2016). …and the Cross-Section of Expected Returns. *RFS* 29(1): 5–68. [NBER w20592](https://www.nber.org/papers/w20592) · [OpenAlex](https://api.openalex.org/works/doi:10.1093/rfs/hhv059) | ✓ |
| 6 | Gu, S., Kelly, B., Xiu, D. (2020). Empirical Asset Pricing via Machine Learning. *RFS* 33(5): 2223–2273. [NBER w25398](https://www.nber.org/papers/w25398) · [PDF](https://dachxiu.chicagobooth.edu/download/ML_BKP.pdf) | ✓ özet; Sharpe ve örneklem [Ö] |
| 7 | Hanauer, M. X., Kalsbach, T. (2023). Machine learning and the cross-section of emerging market stock returns. *EMR* 55: 101022. [RePEc](https://ideas.repec.org/a/eee/ememar/v55y2023ics1566014123000274.html) · [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4287550) · [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1566014123000274) · [Robeco özeti](https://www.robeco.com/en-int/insights/2023/10/using-machine-learning-for-emerging-market-equity-returns) | ✓ özet; değişken sırası [Ö] |
| 8 | Leippold, M., Wang, Q., Zhou, W. (2022). Machine learning in the Chinese stock market. *JFE* 145(2): 64–82. [EconPapers](https://econpapers.repec.org/RePEc:eee:jfinec:v:145:y:2022:i:2:p:64-82) | ✓ |
| 9 | Bailey, D. H., López de Prado, M. (2014). The Deflated Sharpe Ratio. *JPM* 40(5): 94–107. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551) · [PDF](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) | ✓; örnek [Ö] |
| 10 | Bailey, D. H., Borwein, J., López de Prado, M., Zhu, Q. J. (2017). The Probability of Backtest Overfitting. *J. Computational Finance* 20(4). [PDF](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) · [RePEc](https://ideas.repec.org/a/rsk/journ0/2471206.html) | ✓; sayfa numaraları [DY] |
| 11 | Bailey, D. H., Borwein, J., López de Prado, M., Zhu, Q. J. (2014). Pseudo-Mathematics and Financial Charlatanism. *Notices of the AMS* 61(5): 458–471. [EurekAlert](https://www.eurekalert.org/news-releases/817304) · [OpenAlex](https://api.openalex.org/works/doi:10.1090/noti1105) | ✓ künye; formül [H] ile tutarlı |
| 12 | DeMiguel, V., Garlappi, L., Uppal, R. (2009). Optimal Versus Naive Diversification. *RFS* 22(5): 1915–1953. [RePEc](https://ideas.repec.org/a/oup/rfinst/v22y2009i5p1915-1953.html) | ✓ |
| 13 | Daniel, K., Moskowitz, T. J. (2016). Momentum Crashes. *JFE* 122(2): 221–247. [RePEc](https://ideas.repec.org/a/eee/jfinec/v122y2016i2p221-247.html) | ✓ |
| 14 | Novy-Marx, R. (2015). Fundamentally, Momentum is Fundamental Momentum. NBER w20984. [NBER](https://www.nber.org/papers/w20984) | ✓ |
| 15 | Novy-Marx, R. (2015). Backtesting Strategies Based on Multiple Signals. NBER w21329. [NBER](https://www.nber.org/papers/w21329) · [Alpha Architect özeti](https://alphaarchitect.com/2016/06/28/backtesting-strategies-based-multiple-signals-beware-overfitting-biases/) | ✓; sayısal örnekler [Ö] |
| 16 | Novy-Marx, R., Velikov, M. (2016). A Taxonomy of Anomalies and Their Trading Costs. *RFS* 29(1): 104–147. [NBER w20721](https://www.nber.org/papers/w20721) | ✓ |
| 17 | Chen, A. Y., Velikov, M. (2023). Zeroing In on the Expected Returns of Anomalies. *JFQA* 58(3): 968–1004. [Cambridge](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/zeroing-in-on-the-expected-returns-of-anomalies/945133D5A3ECEEAF466AEE91551FD225) | ✓ |
| 18 | Martineau, C. (2022). Rest in Peace Post-Earnings Announcement Drift. *CFR* 11(3–4): 613–646. [RePEc](https://ideas.repec.org/a/now/jnlcfr/104.00000122.html) | ✓ |
| 19 | Chen, A. Y., Zimmermann, T. (2022). Open Source Cross-Sectional Asset Pricing. *CFR* 11(2): 207–264. [RePEc](https://ideas.repec.org/a/now/jnlcfr/104.00000112.html) | ✓ |
| 20 | Green, J., Hand, J. R. M., Zhang, X. F. (2017). The Characteristics that Provide Independent Information about Average U.S. Monthly Stock Returns. *RFS* 30(12): 4389–4436. [RePEc](https://ideas.repec.org/a/oup/rfinst/v30y2017i12p4389-4436..html) | ✓ |
| 21 | Freyberger, J., Neuhierl, A., Weber, M. (2020). Dissecting Characteristics Nonparametrically. *RFS* 33(5): 2326–2377. [EconPapers](https://econpapers.repec.org/RePEc:oup:rfinst:v:33:y:2020:i:5:p:2326-2377.) | ✓ |
| 22 | DeMiguel, V., Martín-Utrera, A., Nogales, F. J., Uppal, R. (2020). A Transaction-Cost Perspective on the Multitude of Firm Characteristics. *RFS* 33(5): 2180–2222. [RePEc](https://ideas.repec.org/a/oup/rfinst/v33y2020i5p2180-2222..html) | ✓ |
| 23 | Harvey, C. R. (2017). Presidential Address: The Scientific Outlook in Financial Economics. *JF* 72(4): 1399–1440. [RePEc](https://ideas.repec.org/a/bla/jfinan/v72y2017i4p1399-1440.html) · [PDF](https://people.duke.edu/~charvey/Media/2018/SSRN-id2893930.pdf) | ✓; MBF [Ö] + [H] |
| 24 | Harvey, C. R., Liu, Y. (2015). Backtesting. *JPM* (Fall 2015). [PDF](https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF) | ✓ |
| 25 | Lo, A. W. (2002). The Statistics of Sharpe Ratios. *FAJ* 58(4): 36–52. [RePEc](https://ideas.repec.org/a/taf/ufajxx/v58y2002i4p36-52.html) | ✓ |
| 26 | Gökçen, U. (2026). Factor investing in the Turkish equity market. *Borsa Istanbul Review*, 100884. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2214845026001043) | ✓ özet; momentum alfası [Ö] |
| 27 | Bildik, R., Gülay, G. (2007). Profitability of Contrarian Strategies: Evidence from the Istanbul Stock Exchange. *IRF* 7(1–2): 61–87. [RePEc](https://ideas.repec.org/a/bla/irvfin/v7y2007i1-2p61-87.html) | ✓ |
| 28 | Kaldırım, Y. (2017). Momentum Anomaly: Research in BIST 100 Index. *Muhasebe ve Finansman Dergisi* (özel sayı). [DergiPark PDF](https://dergipark.org.tr/tr/download/article-file/436187) | ✓; rakamlar [Ö] |
| 29 | van der Hart, J., Slagter, E., van Dijk, D. (2003). Stock Selection Strategies in Emerging Markets. *JEF* 10(1–2): 105–132. [RePEc](https://ideas.repec.org/p/tin/wpaper/20010009.html) | ✓ |
| 30 | van der Hart, J., de Zwart, G., van Dijk, D. (2005). The success of stock selection strategies in emerging markets: Is it risk or behavioral bias? *EMR* 6(3): 238–262. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1566014105000373) | ✓ |
| 31 | Cakici, N., Fabozzi, F., Tan, S. (2013). Size, value, and momentum in emerging market stock returns. *EMR* 16: 46–65. [EconPapers](https://econpapers.repec.org/article/eeeememar/v_3a16_3ay_3a2013_3ai_3ac_3ap_3a46-65.htm) | ✓ |
| 32 | Jacobs, H. (2016). Market maturity and mispricing. *JFE* 122(2): 270–287. [RePEc](https://ideas.repec.org/a/eee/jfinec/v122y2016i2p270-287.html) | ✓ |
| 33 | Stambaugh, R. F., Yuan, Y. (2017). Mispricing Factors. *RFS* 30(4): 1270–1315. [EconPapers](https://econpapers.repec.org/RePEc:oup:rfinst:v:30:y:2017:i:4:p:1270-1315.) | ✓ |
| 34 | Asness, C., Moskowitz, T., Pedersen, L. H. (2013). Value and Momentum Everywhere. *JF* 68(3): 929–985. [RePEc](https://ideas.repec.org/a/bla/jfinan/v68y2013i3p929-985.html) · [AQR](https://www.aqr.com/Insights/Research/Journal-Article/Value-and-Momentum-Everywhere) | ✓ |
| 35 | Asness, C., Frazzini, A., Pedersen, L. H. (2019). Quality minus junk. *RAST* 24(1): 34–112. [RePEc](https://ideas.repec.org/a/spr/reaccs/v24y2019i1d10.1007_s11142-018-9470-2.html) | ✓ |
| 36 | Chan, L. K. C., Jegadeesh, N., Lakonishok, J. (1996). Momentum Strategies. *JF* 51(5): 1681–1713. [RePEc](https://ideas.repec.org/a/bla/jfinan/v51y1996i5p1681-1713.html) | ✓ |
| 37 | Chordia, T., Shivakumar, L. (2006). Earnings and price momentum. *JFE* 80(3): 627–656. [RePEc](https://ideas.repec.org/a/eee/jfinec/v80y2006i3p627-656.html) | künye ✓, içerik [DY] |
| 38 | Piotroski, J. D. (2000). Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers. *JAR* 38 (Suppl.): 1–41. [OpenAlex](https://api.openalex.org/works/doi:10.2307/2672906) | künye ✓ |
| 39 | Dawes, R. M. (1979). The robust beauty of improper linear models in decision making. *American Psychologist* 34(7): 571–582. [OpenAlex](https://api.openalex.org/works/doi:10.1037/0003-066X.34.7.571) | ✓ |
| 40 | George, T. J., Hwang, C.-Y. (2004). The 52-Week High and Momentum Investing. *JF* 59(5): 2145–2176. [RePEc](https://ideas.repec.org/a/bla/jfinan/v59y2004i5p2145-2176.html) | ✓ |
| 41 | Bali, T. G., Cakici, N., Whitelaw, R. F. (2011). Maxing out: Stocks as lotteries and the cross-section of expected returns. *JFE* 99(2): 427–446. [RePEc](https://ideas.repec.org/a/eee/jfinec/v99y2011i2p427-446.html) | ✓ |
| 42 | Campbell, J. Y., Hilscher, J., Szilagyi, J. (2008). In Search of Distress Risk. *JF* 63(6): 2899–2939. [RePEc](https://ideas.repec.org/a/bla/jfinan/v63y2008i6p2899-2939.html) | ✓ |
| 43 | Avramov, D., Chordia, T., Jostova, G., Philipov, A. (2013). Anomalies and financial distress. *JFE* 108(1): 139–159. [RePEc](https://ideas.repec.org/a/eee/jfinec/v108y2013i1p139-159.html) | ✓ |
| 44 | Fitzgibbons, S., Friedman, J., Pomorski, L., Serban, L. (2017). Long-Only Style Investing: Don't Just Mix, Integrate. *J. Investing* 26(4): 153–164. [AQR](https://www.aqr.com/Insights/Research/White-Papers/Long-Only-Style-Investing) | ✓ (dergi adı tutarsızlığı not edildi; sayfa aralığı [DY]) |
| 45 | Bender, J., Wang, T. (2016). Can the Whole Be More Than the Sum of the Parts? *JPM* 42(5): 39–50. [OpenAlex](https://api.openalex.org/works/doi:10.3905/jpm.2016.42.5.039) | ✓ |
| 46 | Ghayur, K., Heaney, R., Platt, S. (2018). Constructing Long-Only Multifactor Strategies: Portfolio Blending vs. Signal Blending. *FAJ* 74(3): 70–85. [CFA Institute](https://rpc.cfainstitute.org/research/financial-analysts-journal/2018/faj-v74-n3-5) | ✓ |
| 47 | Leippold, M., Rüegg, R. (2018). The mixed vs the integrated approach to style investing: Much ado about nothing? *EFM* 24(5): 829–855. [RePEc](https://ideas.repec.org/a/bla/eufman/v24y2018i5p829-855.html) | ✓ |
| 48 | Fernandez-Perez, A., Fuertes, A.-M., Miffre, J. (2019). A comprehensive appraisal of style-integration methods. *JBF* 105: 134–150. [RePEc](https://ideas.repec.org/a/eee/jbfina/v105y2019icp134-150.html) | ✓ |
| — | Sloan, R. (1996). Do stock prices fully reflect information in accruals and cash flows about future earnings? *Accounting Review* 71(3) | [DY] |
