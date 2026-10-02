# BRIEF — "Dipten Dönüş" stratejisi (BIST TÜM) için literatür taraması

## Kullanıcının tanımı (Ömer, 01/10/2026)
- Amaç: **dipten dönen ve/veya kârlılığı ciddi ve anlamlı artan** şirketleri portföye almak. Büyüme stratejisi gibi düşünülmeyecek; sert temel kapılar başlangıç noktası değil.
- Profil 1 (dönüş): net kâr / özkaynak kârlılığı (ROE) negatiften pozitife dönen, ROE negatifken ciddi iyileşip pozitife geçen **ve piyasanın da inandığı** (fiyat momentumu) şirketler. Örnekler: Migros (2015 sonu Anadolu Grubu'nun kontrolü almasıyla borçlu/zarar eden şirketten kâra), THYAO (pandemi sonrası 2021–22).
- Profil 2 (kâr sıçraması): kârlılık zaten pozitifken çok ciddi artan, çarpanları (F/K, FD/FAVÖK) ciddi düşürecek düzeyde kâr sıçraması yapan şirketler. "Dar tutma" — farklı hikâyeler de olabilir.
- Kullanıcı momentumun bu şirketlerde çok işe yaradığını düşünüyor.
- **Sadelik şart:** formüller basit, anlaşılır, uygulanabilir; sitede test süresi formül karmaşıklığıyla artıyor (Büyüme stratejisi kadar sade).

## Kısıtlar
- Piyasa: Borsa İstanbul, BIST TÜM evreni (≈220–700 hisse/ay, 2005–2026), finansallar dahil (bankalarda FAVÖK yok).
- Portföy: her ay 5 hisse, eşit ağırlık, aylık yeniden dengeleme, **her zaman yatırımda** (nakit yok; 5'ten az hisse geçerse önce teknik, sonra temel koşullar gevşetilerek tamamlanır).
- Veri: çeyreklik finansallar yayın tarihine göre (point-in-time), günlük fiyat/hacim.
- Öncelik: **kazandıran ay oranı ve istikrar (Sharpe, K-Ratio, kriz ayları) > son sermaye**.
- Platform formül dili (QueenStocks): `OzsermayeKarlilikYillik()`, `OzsermayeKarlilikYillik("",-4)` (4 çeyrek önce), `NetKarYillik()`, `NetKarYillik("",-4)`, `NetKar("TL",0)` (çeyreklik, `-1` önceki çeyrek), `FAVOKYillik()`, `FAVOK("TL",0)`, `EFK("TL",0)`, `NetKarMarjiYillik()`, `FAVOKMarjiYillik()`, `NetSatisBuyumeYillik()`, `FAVOKBuyumeYillik()`, `NetKarBuyumeYillik()`, `NetBorc()`, `NetBorcFavokYillik()`, `ToplamBorc(null,-4)/Aktifler(null,-4)`, `FaizKarsilamaOrani()`, `IsletmeFaaliyetlerdenNakitAkis()`, `SerbestNakitAkis()`, `FK()`, `FDFAVOK()`, `PDDD()`, `PD()`, `HAOran()` (halka açıklık), `Tufe(12)`, `Getiri("s6a","TL")` (6 ay getiri), `Getiri("s2a","TL","XUTUM")` (endeks getirisi), `Teknik.Indicator("C/HHV(H,252)","d")` (MetaStock benzeri: C, H, L, V, Mov(C,200,S), Ref, HHV, LLV, Sum, Stdev, Cum), `IF`, `Abs`, `Floor`, `Log`, `Min`, `Max`. Kullanıcı tanımlı fonksiyon yok; sıralama tek bir skorla yapılır.

## Mevcut stratejiler (bağlam; bunlar "T = denendi" sayılır)
- **Büyüme Stratejisi (K10):** kâr ivmesi + kârlılık + momentum + trend kapıları. Kapılar: ROE > 5, NetBorç/FAVÖK < 4, PD/DD < sınır (ROE'ye bağlı), 2 ay göreli güç > XUTUM, 1 ay getiri > −15, ROE teyidi (ROE ≥ önceki çeyrek veya 4 çeyrek önce), HA < 60, (12 ay getiri ≤ 300 veya PD/DD ≤ 8), E/P ≥ %2,5, C > MA200, C > MA75, MA20 > MA60. Skor: EFK/FAVÖK yıllık değişim, ROE değişimi, EFK büyüme ivmesi, 52 hafta zirveye yakınlık, 6 ay momentum (Ref(C,-21)/Ref(C,-126)), aşırı uzama cezası.
- **Değer Yatırımı (C32):** F-Skor ≥ 7 (9 kriter), FD/FAVÖK > 0, 12-1 ay momentum > XU100, HA < 60, (çeyrek FAVÖK payı > 0,22 veya satış büyümesi > %50), F/K < 40, PD/DD < 8, MA20 > MA75, "düşen bıçak" filtresi (3'te 2: 6 ay getiri ≥ 0, fiyat ≥ 52h dibin 1,5 katı, fiyat ≥ 52h zirvenin %70'i). Skor: FD/FAVÖK, trend, nakit, PD/DD bonusları.
- Bilinen bulgular: HA < 60 (halka açıklık) tek başına en etkili ek; düşen bıçak filtresi kriz yıllarını iyileştirdi; MA20 > MA60 tutuldu; 52 hafta zirveye yakınlık ve dipten uzaklık (1,0–1,3 kat) faydalı; finansallarda FAVÖK boş; TMS 29 (2024+) enflasyon muhasebesi büyüme fonksiyonlarını bozuyor.
- Henüz denenmeyen alan: **dönüş (turnaround) / zarardan kâra geçiş / kâr sıçraması** — bu proje.

## İstenen çıktı (her ajan)
1. Her kalem için tablo: bulgu (yazar, yıl, örneklem, dönem, etki büyüklüğü) | replikasyon / gelişmekte olan piyasa / Türkiye kanıtı | durum (T denendi / P kısmen / N denenmedi — yukarıdaki stratejilere göre) | platform formül dilinde taslak (tek satır, sade) | öncelik (Yüksek/Orta/Düşük) | kapı mı, sıralama mı, bonus mu?
2. "Denenmemiş en iyi 10 fikir" öncelik sırasıyla (sadelik ve uygulanabilirlik ağırlıklı).
3. **Uyarılar:** literatürün dönüş/sıkıntılı şirketler için kırmızı bayrakları (ör. sıkıntılı şirket anomalisi, ölü kedi sıçraması, sahte kâr).
4. Doğrulama kuralı: her kaynak yayıncı/SSRN/RePEc/NBER/DergiPark/Google Scholar sayfasında açılıp kontrol edilir; doğrulanamayan [DY] işaretlenir; PDF özetinden okunan rakam [Ö] işaretlenir; **rakam uydurma**.
5. Dürüst sınırlar bölümü (kaç arama/okuma, hangi kaynaklar açılamadı).
Dil: Türkçe. Çıktıyı belirtilen dosyaya Markdown olarak yaz.
