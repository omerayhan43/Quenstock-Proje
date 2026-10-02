# Dipten Dönüş Stratejisi (BISTTUM) — Literatür sentezi (01/10/2026)

## 0. Kapsam ve dürüstlük notu
- 4 paralel ajan (A temel dönüş · B momentum/piyasa onayı · C Türkiye/BIST · D faktör/aşırı uyum), ≈190 doğrulanmış kaynak (yayıncı, NBER, RePEc, SSRN, DergiPark); ayrıntı ve kaynakça `LIT_A…D_*.md`.
- Ortak web arama kotası (≈200) taramanın sonunda doldu; Wiley/SSRN bazı sayfalarda 403/429. Doğrulanamayanlar [DY], PDF özetinden okunan rakamlar [Ö] işaretli. "Her şey okundu" denemez.
- **En büyük boşluk:** BIST'te "zarardan kâra geçiş" ya da "kâr sıçraması" sonrası getiriyi doğrudan test eden çalışma bulunamadı. En yakın kanıt: kazanç sürprizi sonrası kayma (Ahlatcıoğlu-Okay 2021, BIR: 2007–18, 60 günde ≈%2,9 fark [Ö]).

## 1. Dört raporun ortak sonucu (birbirinden bağımsız varıldı)
1. **Tek olay ölçüsü: fiyata ölçekli yıllık kâr değişimi** `ΔE/P = (NetKarYillik() − NetKarYillik("",-4)) / PD()`. Ömer'in iki profilini tek sayıda birleştirir: zarardan kâra (E/P −%5 → +%3 ⇒ 0,08) ve "çarpanı ciddi düşüren sıçrama" (F/K 40 → 13 ⇒ 0,05). Bankalarda da çalışır (FAVÖK gerekmez), negatif/küçük özkaynakta bozulan ROE'den etkilenmez, yüzde büyümenin küçük/negatif tabanda anlamsızlaşmasını önler. Kanıt: kazanç momentumu ve fiyata ölçekli kazanç değişimi (Chan-Jegadeesh-Lakonishok 1996; Novy-Marx 2015; Hou-Xue-Zhang 2020 replikasyonunda ΔROE/SUE ayakta).
2. **Fiyat momentumu skorun ana gövdesi değil, onay kapısı.** Türkiye'de saf fiyat momentumu kırılgan (bazı çalışmalarda negatif; 2005 sonrası pozitif — Gökçen 2026 [Ö]). Kâr dönüşüyle eşleşmiş fiyat hareketi ise literatürle uyumlu (Chordia-Shivakumar 2006; Novy-Marx 2015). Ömer'in "momentum işe yarar" sezgisi bu biçimde destekleniyor.
3. **Dönüşü tahmin etme, raporda gör ve piyasa onaylayınca al.** Sıkıntılı ve kalıcı zarar eden şirketler ortalamada kötü getiri verir (Dichev 1998; Campbell-Hilscher-Szilagyi 2008; Li 2011); getiri "hayatta kalan, ucuz ve iyileşen" grupta.
4. **Sahte kâr korumaları şart:** tek seferlik kalemler (Migros 2017 kârı Kipa satın alma kazancından), kur farkı, varlık satışı, TMS 29 (31/12/2023 sonrası) net parasal pozisyon kazancı. Ucuz teyitler: son çeyrek kârı pozitif, FAVÖK pozitif/artıyor (finansallarda boş → muaf), özkaynak pozitif, işletme nakit akışı > 0.
5. **Sadelik:** 1 sert filtre + 2 kapı (skora sözlük sırasıyla gömülü: `100·A + 10·B + bileşik`) + eşit ağırlıklı, kırpılmış 2–3 bileşenli skor. 5 hisselik konsantre portföyde tek bileşik skor, ardışık sert kapılardan iyi (Ghayur-Heaney-Platt 2018; Fitzgibbons vd. 2017). Sözlük sırası her ay 5 hisseyi garanti eder ve "önce teknik, sonra temel gevşer" kuralıyla birebir uyumludur.
6. **Risk korumaları:** halka açıklık bandı (HA < 60; alt sınır ~20 manipülasyon kalkanı — BIST Alt Pazar balonu, İmisiker-Taş 2013), oynaklık/MAX cezası (BIST'te yüksek oynaklık alfası negatif — Gökçen 2026 [Ö]; MAX etkisi Alkan-Güner 2018), kısa vadeli aşırı uzama cezası.
7. **Momentum çöküşü ve dönüş anı aynı zamana denk gelir** (Daniel-Moskowitz 2016): MA200 ve 6 ay momentum kapıları toparlanmanın ilk ayağını kaçırır; ayı piyasasındaki sinyaller ölü kedi olabilir. Rejim anahtarı yalnız analiz olarak (nakit yok kuralı).

## 2. Vaka düzeltmeleri (doğrulanmış)
- **Migros:** Anadolu Grubu pay alımı 31/12/2014 imza, Rekabet Kurulu onayı 09/07/2015, devir Temmuz 2015. Şirket 2015, 2016, 2018, 2019, 2020'de zarar etti; 2017 kârı Kipa satın alma kazancı (sahte). Gerçek kâra dönüş 2021 (+359 mn TL), sıçrama 2022 (+2,57 mr TL) [Haber/KAP özeti]. → İyi bir algoritma Migros'u 2015'te değil, 2021–22'de almalı; 2017'deki sahte kârda almamalı (FAVÖK/nakit teyidi testi için ideal vaka).
- **THYAO:** pandemi zararından 2021'de kâra dönüş, 2022–23 kâr sıçraması (çarpan sıkışması) — iki profilin ardışık örneği.

## 3. Denenmemiş en iyi fikirler (dört listenin birleşimi, sadelik sırasıyla)
| # | Fikir | Rol | Taslak |
|---|---|---|---|
| 1 | ΔE/P olay ölçüsü (kırpılmış) | kapı A + skor | `d=(NetKarYillik()-NetKarYillik("",-4))/PD();` eşik 0,03–0,08 |
| 2 | Kâr pozitif (TTM) | kapı A parçası | `NetKarYillik()>0` |
| 3 | Piyasa teyidi | kapı B | `C/Mov(C,200,S)>1` · alternatif 6 ay göreli güç, `C/HHV(H,252)>=0.70` |
| 4 | 52 hafta zirveye yakınlık + 6-1 momentum | skor | `C/HHV(H,252)`, `Ref(C,-21)/Ref(C,-126)` |
| 5 | Son çeyrek kârı pozitif / olay tazeliği | koruma | `NetKar("TL",0)>0`, `NetKar("TL",0)>NetKar("TL",-4)` |
| 6 | Faaliyet teyidi (sahte kâr) | koruma | FAVÖK yıllık > 0 ve artıyor (finansal muaf) |
| 7 | Özkaynak > 0 | koruma | `Ozsermaye()>0` |
| 8 | HA bandı | filtre | `HAOran()<60` (+ alt sınır ~20 adayı) |
| 9 | Oynaklık/MAX cezası | skor cezası | `HHV(C/Ref(C,-1),21)>1.09` |
| 10 | Çeyreklik ΔE/P (tazelik) | alternatif olay | `(NetKar("TL",0)-NetKar("TL",-4))/PD()` |
| 11 | ΔROE alternatifi | alternatif olay | `OzsermayeKarlilikYillik()-OzsermayeKarlilikYillik("",-4)>=10` + özkaynak > 0 |
| 12 | 3 yıllık dipten toparlanma | bonus | `C/HHV(H,756)<0.6` ve `C>MA200` |
| 13 | Borç azaltma | bonus | `ToplamBorc()/Aktifler() < ToplamBorc(null,-4)/Aktifler(null,-4)` |
| 14 | Reel satış teyidi | koruma | `NetSatisBuyumeYillik()>Tufe(12)` |

## 4. Önerilen taban iskeleti (Ajan D, sadeleştirilmiş)
```
// Kriter: HAOran() < 60   (Temel: uye = PD() > 0; Teknik: C > 0 — katmanlar sıralamada)
d  = (NetKarYillik() - NetKarYillik("",-4)) / PD();
a  = NetKarYillik() > 0 and d >= 0.05;                 // KAPI A: olay
b  = Teknik.Indicator("C/Mov(C,200,S)","d") > 1;        // KAPI B: piyasa teyidi
s1 = Min(Max(d,0),0.20)/0.20;                          // kâr değişimi
s2 = Min(Max(C/HHV(H,252) - 0.5,0),0.5)/0.5;           // 52h zirveye yakınlık
s3 = Min(Max(Ref(C,-21)/Ref(C,-126) - 1,0),1);         // 6-1 ay momentum
SKOR = 100*a + 10*b + s1 + s2 + s3;
```
Eşikler (0,05, 0,20 tavan) literatürden değil, başlangıç önerisi; teşhis verisiyle (olay kütüphanesi) kontrol edilip **ön kayıtla** sabitlenecek.

## 5. Doğrulama disiplini (Ajan D)
- 5 hisse çok gürültülü: kazandıran ay oranının standart hatası ≈ 2,8 puan, Sharpe'ınki ≈ 0,22 [H]. 21,5 yılla küçük iyileştirmeler için ≈ 25 bağımsız deneme hakkı var → **tur başına en fazla 6 aday, tek değişken, ön kayıt**, final için DSR ≥ 0,95 ve PBO ≤ 0,25.
- NW t ≥ 1,5 eşiği ≈ 8–10 gürültü varyantının beklenen en iyisine eşit → deneme sayacı tutulacak, t* = E[max Z_N] raporlanacak.
- Migros/THYAO ve kaçan kazananlar yalnız teşhis içindir; onlara göre ayar yapmak aşırı uyumdur.
- Hayatta kalma yanlılığı: işlemden kalkan hisseler editörde sorgulanamıyor → sim iyimser olabilir; site testi (tüm geçmiş hisseler dahil) belirleyici. Üyelik modeli 208552 bu farkı ölçmek için.
