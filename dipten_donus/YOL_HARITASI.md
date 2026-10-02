# Dipten Dönüş Stratejisi (BISTTUM) — yol haritası

Başlangıç: 01/10/2026 ~10:10. Çalışma adı: "Dipten Dönüş Stratejisi" (Ömer onaylarsa sitede "Dipten Dönüş Stratejisi (BISTTUM)"). Evren: BIST TÜM (önerildi, Ömer "başlayabilirsin" dedi; BIST100/Katılım sürümleri sonra).

## Ömer'in tanımı (01/10/2026, kendi sözleri özetle)
- Amaç: **dipten dönen ve/veya kârlılığı ciddi ve anlamlı artan** şirketleri portföye almak. Büyüme stratejisi gibi düşünülmeyecek; sert kapılar burada başlangıç noktası değil.
- Örnek profil: kârlılığı negatiften pozitife dönen, özkaynak kârlılığı negatifken ciddi iyileşip pozitife dönen **ve piyasanın da inandığı** (momentum) şirketler. Örnekler: Migros (Anadolu Grubu devri sonrası borçlu/zarar eden şirketten kâra), pandemi sonrası THYAO.
- **Dar tutma:** kârlılığın illa negatiften pozitife dönmesi gerekmez. Pozitifken çok ciddi artan, çarpanları ciddi düşürecek düzeyde kâr sıçraması yapan şirketler de girebilir (dönüş hikâyesi ya da farklı bir hikâye) — algoritma bunları da yakalayabilmeli.
- **Başlangıç algoritması yok; kurguyu Claude tasarlayacak. Basit olacak** (Büyüme stratejisi gibi sade, anlaşılır, uygulanabilir); test süresini ve hesaplamayı uzatmayacak formüller (site test süresi formül karmaşıklığıyla artıyor).
- Momentumun bu tür şirketlerde çok işe yaradığını düşünüyor.

## Sabit kurallar
5 hisse · eşit ağırlık · aylık dengeleme · nakit yok (katmanlı tamamlama: önce teknik, sonra temel gevşer) · 2005–2026 (+2015–2026) · istikrar ve kazandıran ay > sermaye · önce sim sonra site (taban/altyapı testleri hariç) · yalnız Farklı Kaydet · aynı anda en fazla 2 site testi · ön kayıt · terfi kuralı v2 · kaçan kazananlar testi · elenen adaylar gerekçeleriyle (getiriyi artırıp elenenler ayrıca).

## Plan (Ömer'in onayladığı sıra)
0. Kurulum + ön kayıt (tanım, ölçütler).
1. Teşhis — olay kütüphanesi 2005–2026: her yılın ilk 30/50'sinden dönüş / kâr sıçraması profiline uyanlar; zamanlama (kâr dönüşünün yayın tarihi · fiyat dibi · zirve); yanlış pozitifler (ölü kedi).
2. Literatür taraması (paralel ajanlar) → LITERATUR.md + denenmemiş en iyi fikirler.
3. Veri: BISTTUM üyelik/getiri modeli (sitede "hepsi geçer", altyapı testi) + editörden aylık paketlenmiş alanlar (`dd_*`).
4. Taban V1 (sade) + metrik taraması (havuz içi sıra-IC, iki yarı, 2015+).
5. Şampiyon V2: aday metrikler tek tek (kapı / sıralama / bonus), kombinasyonlar, ablasyon; terfi kuralı v2 + plasebo.
6. Site doğrulama (2005–26 ve 2015–26, sim ile 261/261).
7. Denetim: kaçak testi, istenmeyen hisse, açıklar, kaçan kazananlar (dönüş olanlar ve neden kaçtı, ortak hata), maliyet/kapasite, gecikme, DSR/PBO, Büyüme/Değer ile korelasyon ve ortak kullanım.
8. Rapor (BISTTUM_Dipten_Donus_Stratejisi_Raporu_2026-10.pdf) + site adları + Ekim seçimi.

## Ömer'in ek talimatı (01/10 ~11:25) — kapsamlı tarama
- "Çok fazla test edelim": Değer/Büyüme'deki gibi ~10 bin sim denemesi; yalnız simde **anlamlı ayrışanlar** siteye.
- Literatürde olup bakılmayan **hiçbir temel ya da teknik rasyo/metrik kalmayacak**; her metrik hem kapı (temel/teknik) hem sıralama bileşeni hem bonus/ceza olarak, tek tek ve kombinasyonlarla denenecek.
- Sağlamlık şartları: iki dönemde (2005–15, 2016–26) artı · en iyi 5 ay çıkınca artı · eşik plato testi (alt/üst komşu değerlerde ani sıçrama/düşüş yok = şans değil) · plasebo · NW t.
- İstatistiksel olarak anlamlı değilse açıkça belirtilecek; aksiyon Ömer'le birlikte.
## Bunun için yöntem ekleri
1. Metrik kataloğu (`METRIK_KATALOGU.md`): literatür + platformun 480 fonksiyonundan temel ve teknik tüm adaylar; her biri için veri alanı.
2. Ek veri turları (`dd2_*`, `dd3_*`): katalogda olup ilk 25 alanda olmayan metrikler (nakit akışı, FAVÖK/EFK/brüt kâr değişimleri, marj değişimleri, faiz karşılama, cari oran, tahakkuk, F-Skor bileşenleri, oynaklık, MAX, hacim, RSI, 52h tazelik vb.).
3. Tarama hattı: (a) tek metrik IC (iki yarı, 2015+) → (b) her metrik × rol (kapı/sıralama/bonus/ceza) × 3–5 eşik düzeyi birebir sim → (c) ileri seçim + ikili/üçlü kombinasyonlar → (d) sağlamlık filtresi (iki yarı, en iyi 5 ay, plato, plasebo) → (e) çoklu test düzeltmesi: deneme sayacı, t* = E[max Z_N], 2021–26 son dönem bekleme (holdout) kontrolü, final DSR/PBO.
4. Simde geçenler sitede (yalnız Farklı Kaydet, en fazla 2 test).
