# Simülasyon kılavuzu — mevcut sime erişme ve gerekirse sıfırdan kurma

Kural (01 §C.2): **her aday önce simde test edilir; simde olumlu ayrışmayan aday siteye gitmez.** Bu yüzden yeni sohbetin ilk teknik işi simi çalışır hâle getirmektir.

---

## 0. En sık neden: yanlış tarayıcı
Sim kodları ve toplanmış veri **Ömer'in kendi Chrome'undaki** IndexedDB'de durur (queenstocks.com kökeni, veritabanı `claude_c29`, store `kv`). Ayrıca QueenStocks oturumu da o Chrome'da açıktır.
- **Claude in Chrome** araçlarını kullan (`mcp__claude-in-chrome__*`). Cowork masaüstü uygulamasının **yerleşik tarayıcısı** ayrı bir profildir: orada ne IDB verisi ne QueenStocks oturumu vardır → "sime erişemiyorum" sorunu buradan çıkar.
- Tercih edilen tarayıcı ayarı yerleşik tarayıcıysa bile Ömer'in Chrome'unu kullanmak için ona sor ("Chrome uzantısını kullanayım mı?").

## 1. Mevcut sime erişim (5 dakika)
1. Chrome'da bir QueenStocks sekmesi aç (test sayfası önerilir: `https://www.queenstocks.com/qs/PortfoyModel/ModelCalistir.aspx`).
2. `03_SITE_KILAVUZU.md` §6'daki `get/set/keys` yardımcılarını tanımla, `await keys()` ile anahtarları listele (çıktı ~1000 karakterle sınırlı: `keys().then(k=>k.filter(x=>/^code|^src_|^fs_/.test(x)).join(','))`).
3. Beklenen kod anahtarları: `code`, `code_b100sim`, `code_b100boot`, `code_b100reader`, `code_b100placebo`, `code_b100fill`, `code_b100tb`, `src_b1worker`, `src_u3worker`, `code4d`, `fs_dc1`, `fs_dx3`, `fs_dx3b`, `c32_formulas`.
4. Sim sekmesini kur: `eval(await get('code_b100boot'))` (Büyüme BIST100 motorunu ve yükleyiciyi tek adımda kurar). Değer BIST100 motoru (`__DF`, `__C1`, `__DX`, `__EXS`; veri `d1_*`) önceki sohbette sim sekmesine yüklenmişti ama **kaydedildiği IDB anahtarının adı DURUM'da yazılı değil**: `keys()` listesinde Büyüme dışındaki kod anahtarlarını tek tek aç (ilk 300 karakter) ve `__DF` tanımını ara. Bulamazsan Büyüme motorunu (`code_b100sim`) şablon alıp §3'e göre Değer sürümünü yeniden kur ve bulduğun/kurduğun anahtarın adını buraya ve DURUM'a yaz.
5. Doğrula: bilinen bir sonucu yeniden üret (örn. Büyüme BIST100 K4a sim sepeti vs site 261 ay; DC1 sim 1,762 mr / site 1,749 mr). Tutmuyorsa kullanma, nedenini bul.
6. Editör işçisi (veri toplama) için bir **BilancoKriterTanim** sekmesinde: `eval(await get('code'))` → `__post(txt, 'GG/AA/YYYY', idxs)` ve `__postAll(...)` hazır olur.

**Yedekle (ilk sohbette bir kez):** IDB'deki kod anahtarlarını bu klasöre al → `araclar/sim_kodlari/<anahtar>.js`. Yol A: sayfada tüm kod anahtarlarını tek JSON Blob olarak indir (dosya indirmek Ömer'in açık onayını gerektirir) → İndirilenler'den bu klasöre taşı. Yol B: her anahtarı 900 karakterlik parçalarla oku + sağlama toplamı, dosyaya yaz (yavaş ama indirme yok). Büyük veri setleri (b1_*, d1_* …) yedeklenmez; gerekirse yeniden toplanır.

---

## 2. Simin mimarisi (nasıl çalışıyor)

```
Site (gerçek)                          Sim (kopya)
───────────                            ───────────
Üyelik modeli 208379 ──► her ayın evreni (b100_mem) + her üyenin SİTE ay getirisi (b100_memret)
Kriter formülü ───────► editörde parçalara ayrılır ──► her ay × her üye için alanlar (b1_AA/YYYY, d1_…)
                                                        │
                           sim motoru: kapılar → katmanlar (tamamlama) → skor → sırala → ilk 5
                                                        │
Site modeli sonucu ◄── kalibrasyon: aynı sepet ay sayısı (hedef ≥ 260/261), sermaye oranı
```

- **Tarihler:** portföy sıralama tarihi = önceki ayın son işlem günü (örn. Temmuz 2024 portföyü → 28/06/2024; site kriterleri ayın 1'i itibarıyla değerlendiriyor olabilir, bkz. G6). Ay getirisi = **ay sonu kapanış / önceki ay sonu kapanış − 1** (`Getiri("s1a")` DEĞİL — G2 hatası). Tarih listesi site sonucundaki dönemlerden alınır (IDB `a41dates`: ay → tarih).
- **Getiri kaynağı:** en güvenilir yol sitenin kendi getirisidir. BIST100'de üyelik modeli (kriter 98295 "hepsi geçer" + 100 hisse + Sadece BIST100 + geçmiş endeks) her ay 100 üyenin hepsini "seçtiği" için ModelSonucDetay'dan her üyenin site getirisi okunur → sim getirileri siteyle birebir. BISTTUM'da (≈700 hisse) bu yapılamaz: editörde kapanış fiyatlarıyla hesaplanır ve site seçimleriyle doğrulanır.
- **Hayalet düzeltmesi:** editörün hisse listesi (`lstHisse`) yalnız bugün işlem görenleri içerir; kotasyondan çıkmış hisseler (SODA, ANACM, TRKCM…) editörde değerlendirilemez (500 hatası). Çözüm (hibrit kopya): sitenin seçiminde olup listede olmayan hisse "hayalet" olarak site getirisi ve site sırasıyla havuza eklenir. BIST100'de hayaletli sim 260/261 ay aynı sepet verdi (hayaletsiz 186/261).
- **Skor birebir kopya:** site sıralama formülü sim'de aynı ağırlık ve sınırlarla yeniden yazılır; kontrol: editörde birkaç tarih × hisse için site SKOR'u ile sim SKOR'u eşit mi (örn. 218/218, 2.842/2.842). Ay içi yüzdelik (ZSkorPercentRank) sitede güvenilmez → sabit ECDF/eşik kullanılır.
- **Tamamlama (nakit yok):** kapı sonuçları bit maskesi olarak saklanır; motor katmanlarla 5'e tamamlar (0: hepsi geçer · 1: teknik eksik · 2: esnek temel · 3: en az kapı kaçıran, kalan kapı × ceza). Sıralama formülünün kendisi de sitede bu katmanları uygular (Temel kutusu `uye = PD() > 0;`, Teknik `C > 0;`, kapılar Sıralama'da).

---

## 3. Sıfırdan kurma (IDB kaybolduysa) — adım adım
Çalışan örnek kodlar bu klasörde: `projeler/deger_v11/dsjob.js` (veri işi + `__post/__postAll`), `kacak_worker.js` (evrensel veri toplayıcı, `__idb/__put/__get`), `analiz_motoru.js` (sim motoru: `__RUN`, `__VAL` sepet eşleşmesi, `__CLEAN` temiz mod, `__PLAC` plasebo, `__ECDF`, `__RANK`), `sim.js` (ilk basit sim), `an.js` (site sonuç okuyucu). Bunları şablon al; BIST100 sürümü aynı mantıkla yazılmıştı.

1. **Editör işçisini kur** (BilancoKriterTanim sekmesi): `dsjob.js`'nin ilk satırlarındaki `__P`, `__post`, `__postAll` tanımları. `__post(txt, d, idxs)`: formülü Temel editöre yazar, `lstHisse`'de indeksleri seçer, tarihi ve "Yayınlanma" ayarını doldurur, `btnTest`'e basar, sonuç textarea'sındaki `yyyy-mm-dd KOD değer` satırlarını {KOD: değer} olarak döner. Parça boyu ≤170–175 hisse. Pencere gizliyken zamanlayıcılar yavaşlar → fetch ile async postback sürümü (`__postF`: FormData(aspnetForm) + `ScriptManager1='…BilancoKriterTanim1$UpdatePanel1|'+btnTest.name`, `__ASYNCPOST=true`, başlık `X-MicrosoftAjax: Delta=true`) daha hızlı ve arka planda çalışır.
2. **Evren ve getiriler:** BIST100 → üyelik modelini sitede çalıştır (208379 hazır; sonucu ModelSonucDetay'dan oku) → `b100_mem` (ay → 100 kod) ve `b100_memret` (ay → kod:site getirisi). BISTTUM → `lstHisse` (bugünkü ~696 kod) + hayalet listesi (site seçimlerinden).
3. **Alanları tasarla:** stratejinin formülünü parçalara ayır: her kapı bir bit (maske), sıralamanın her bileşeni ayrı sayı. Bir ayda tek postback'le birden çok alan almak için formülün son satırında paketle (örn. `g = Fskor*100 + m12*1 + mg*2 + (HA<60)*4 + tek*8`). Sayıları yuvarlama; bit maskelerini asla. Binlik ayraçlı çıktıları (`4,917,500,000`) temizle (G1).
4. **Toplama işini başlat:** 3–4 editör sekmesi, her biri farklı ay aralığı (sondan geriye / baştan ileriye). Her ay sonucu IDB'ye `önek_AA/YYYY` anahtarıyla yazılır (kaldığı yerden devam edebilsin). Hız BIST100'de ~46 sn/ay/sekme (261 ay × 20 alan ≈ 1 saat, 4 sekme). Darboğaz sunucu: sekme sayısını artırmak yerine istek sayısını azalt (sektör fonksiyonlarını sektör başına bir temsilciyle iste — değerleri grupta birebir aynı).
5. **Motoru yaz:** her ay: havuz = üyeler (+ hayaletler) → kapılar/katmanlar → skor → azalan sırala (eşitlikte sitenin sırasını koru) → ilk 5 → ay getirisi = 5 site getirisinin ortalaması. Parametre nesnesi `P` ile varyant tanımla (eşik, ağırlık, ek kapı/bonus, `P.off` gecikme).
6. **Kalibre et:** şampiyonun site modeliyle ay ay sepet karşılaştır (`__VAL` gibi): hedef ≥ 260/261 aynı sepet; farkları sınıflandır (hayalet, eşit puan, kapı farkı, veri eksikliği). Sim/site sermaye oranını raporla. Kalibrasyon tutmadan hiçbir sim sonucuna güvenme.
7. **Ölçüm seti:** son sermaye, CAGR (2005–15 / 2016–26), Sharpe (site formülü), K-Ratio, MDD, kazandıran ay %, kriz ayları ort. (XU100 < −%5), <5 hisseli ay, eşli fark (yıllık log puan) + NW t, H1/H2/2015+, en iyi 5 ay çıkınca fark, plasebo (200 tohum, aynı sayıda rastgele sepet değişikliği), plato (komşu düzeyler), E1 (1 Ekim 2026 BIST100 kuralları emülasyonu), temiz mod (1 gün gecikme).
8. **Python'a aktar:** aylık seriyi E36 ile dışarı al (`03_SITE_KILAVUZU.md` §2) → `araclar/b100/cmp.py` ile bağımsız doğrulama.

---

## 4. Tuzaklar (hepsi yaşandı)
- **G1** binlik ayraçlı sayı → parseFloat yanlış okur. **G2** `Getiri("s1a")` sitenin ay getirisi değil. **G3** null: karşılaştırmada false, toplamada 0 (F-skor/OCF bozulabilir). **G4/G5** bugünkü hisse listesi → hayatta kalma yanlılığı (hayalet düzeltmesi). **G6** site kriterleri ayın 1'i itibarıyla değerlendiriyor olabilir; getiri önceki ay sonundan başlar.
- `Getiri(p,"TL","XU100")` **endeksin kendi getirisini** döndürür (göreli değil): göreli için `Getiri(p,"TL") - Getiri(p,"TL","XU100")`.
- Editör sonuç sözlüğü alfabetik gelir; boolean sonuç sayı dönmez (`IF(koşul,1,0)`); sonucu SON `;` satırı belirler; Temel editörde `C` yok (`Mov(20)`, `Kapanis()`); `Teknik.Indicator("MetaStock ifadesi","d")` teknik ifadeler için.
- TMS 29 (2024+): platform karşılaştırmalı tutarları reel saklıyor → büyüme fonksiyonları 2024+ reel.
- Havuz IC'si ≠ 5 hisselik portföy iyileşmesi: her aday birebir kopyada test edilir.
- Sim sitede iyimser çıkabilir (Değer BIST100: DX3 −%11, DX3b −%6; DC1 −%0,7) — arama yanlılığı; raporla.
- Uzun `await` + sayfa yönlendirmesi aynı JS çağrısında olmaz; arka plan sekmeleri atılabilir → her şeyi IDB'ye yaz, sekme yeniden yüklenince koddan yeniden kur.
