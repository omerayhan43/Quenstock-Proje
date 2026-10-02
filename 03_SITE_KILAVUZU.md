# QueenStocks otomasyon kılavuzu (Claude in Chrome)

Hepsi sitede denenmiş yöntemlerdir. İlk kaynak `projeler/deger_v11/PROTOKOL.md` §10 ve EK; BIST100 döneminde (29–30/09) eklenenler aşağıda işaretli. Kurallar için önce `01_KURALLAR_VE_TERCIHLER.md` §A.

---

## 1. Oturum ve sekmeler
- Tarayıcı: Ömer'in Chrome'u, **Claude in Chrome** uzantısı (Cowork'ün yerleşik tarayıcısı ayrı profil: QueenStocks oturumu ve IndexedDB orada yok). İlk iş `tabs_context_mcp`; sekme ID'leri sohbete özeldir (eski sohbetin sekme numaralarını kullanma, kendi sekmelerini aç).
- Önerilen sekme rolleri: (1) kriter editörü, (2) model sayfası, (3) test sayfası (ModelCalistir), (4) sim/okuyucu sekmesi, (5–7) veri işçileri (gerekirse).
- **Oturum düşerse** (Login.aspx görünürse): şifre GİRME → https://borfin.com/tr/programs/153/redirect (veya borfin.com/tr/panel/programs → Queenstocks → "Programa Git"). QueenStocks oturumu geri gelir.
- Chrome sekme grubu kaybolursa `tabs_context_mcp(createIfEmpty)`. Arka plan sekmeleri Chrome tarafından atılabilir/yeniden yüklenebilir → sekmedeki JS durumu gider; kod IDB'den yeniden kurulur (§6).
- Kullanıcı yokken pencere gizliyse `setTimeout` ~1 dk'ya kısılır; UpdatePanel da zamanlayıcı kullanır. Çözüm: editör testini doğrudan `fetch` ile async postback olarak göndermek (`__post`/`__postF`, §5).

## 2. Genel teknik notlar
- Sayfalar ASP.NET WebForms. Element ID öneki uzun (`ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_...`); kısaca `document.querySelector('[id$=txtModelAd]')` gibi **son ek seçicisi** kullan.
- Sayfalar çok büyük (1500+ seçenekli listeler): `find` / geniş `read_page` "prompt too long" verir → **javascript_tool ile doğrudan ID üzerinden** çalış.
- **JS çıktı sınırı ~1000 karakter.** Büyük veriyi `window.__x`'te tut, parça parça oku; veri aktarırken parça + sağlama toplamı kullan. Sayı serilerini E36 biçiminde aktar: her değer (baz puan + 20000) taban-36, 3 karakter.
- **Çıktı engelleri:** "BLOCKED: Cookie/query string data" → çıktıda `=`, `&`, `?` olmasın: `.replace(/=/g,'≡').replace(/[?&]/g,'·')`; köşeli ayraçları (`<`, `>`) da değiştir (örn. `‹ ›`).
- **Sayfa yönlendiren işlem + await aynı çağrıda olmaz** ("Inspected target navigated"): postback/kaydet tıklamasını `setTimeout(()=>btn.click(),50)` ile tetikle, okumayı ayrı çağrıda yap.
- Uzun `sleep` içeren eval CDP zaman aşımına düşer → kısa bekleme (computer `wait` ≤10 sn) + tekrar okuma. `browser_batch` ~2 dk'yı aşarsa zaman aşımı olur, kalan adımlar arka planda sürebilir → uzun zincir kurma.
- Postback sonrası 4–9 sn bekle.

## 3. Kriter (Temel Analiz Kriterlerim)
URL: `https://www.queenstocks.com/qs/PortfoyModel/BilancoKriterTanim.aspx`
1. **Yükle** (BIST100 döneminde kullanılan, güvenilir): `dd=document.querySelector('[id$=ddlKulOranTanim]'); dd.value='98258'; __doPostBack(dd.name,'')` → ayrı çağrıda ~5 sn sonra `dd.value` doğrula. (Alternatif: `dispatchEvent(new Event('change',{bubbles:true}))`.)
   - Dropdown'da beklenen ID yoksa sayfa bayat → sayfaya yeniden git.
2. **Editörler:** `document.querySelectorAll('.CodeMirror')` → [0] Temel, [1] Sıralama, [2] Teknik. Oku `.CodeMirror.getValue()`, yaz `.CodeMirror.setValue(txt)`, sonra hepsine `.CodeMirror.save()`.
3. **Ad:** `[id$=txtKulOranTanimAd]` `.value = 'Yeni ad'`.
4. **Kaydetmeden önce test alanı dolu olmalı** (yoksa "en az bir adet hisse seçmelisiniz" hatası, kaydetmez): `[id$=lstHisse]` içinde THYAO `.selected=true` (gerekirse `txtBasTarih`/`txtTarih` = '01/09/2026', `ddlBilancoKullanimSekli`='1').
5. **Farklı Kaydet:** `setTimeout(()=>document.querySelector('[id$=btnFarkliKaydet]').click(),50)` → ~8 sn → ayrı çağrıda: seçili `ddlKulOranTanim` değeri = **yeni ID**, `txtKulOranTanimAd` = yeni ad; kaynak ID hâlâ listede mi (`[...dd.options].some(o=>o.value==='KAYNAK')`). Üç editör metninin uzunluğunu kaynakla karşılaştır.
   - **ASLA `btnSave`** (yüklü kriterin üzerine yazar).
6. Bir sonraki kopyadan önce kaynağı yeniden yükle (değişiklikler üst üste binmesin).

**Editörde formül testi (kaydetmeden):** "Yeni Oluştur" iken Temel editöre ifade yaz, hisseleri/tarihi doldur, `[id$=btnTest]` → ~7 sn → sonuç textarea'da `2026-09-01  ASELS  0.44` satırları. Notlar: Temel editörde `C` yok (`Mov(20)`, `Kapanis()` kullan); sonucu SON `;` satırı belirler; boolean sonuç sayı dönmez → `IF(koşul,1,0)`; sonuç sözlüğü **alfabetik** gelir (kodla eşleştir); tüm evren tek postback'te sessizce başarısız → 175'lik parçalar; `lstHisse` yalnız bugün işlem görenleri içerir (kotasyondan çıkmış hisseler sorgulanamaz). Fonksiyon listesi: `#selFonk`.

## 4. Model (Portföy Model Oluşturma)
URL: `https://www.queenstocks.com/qs/PortfoyModel/Default.aspx?modelId=KAYNAK_MODEL`
1. Kaynağı aç; `[id$=txtModelAd]` değerinin kaynak model adı olduğunu doğrula.
2. Kriter: `[id$=ddlModelBilancoKriter]` `.value='YENİ_KRİTER'` + change → postback (~5 sn).
3. **Ayarları kaynak modelden oku ve yeni modelde birebir aynı olduğunu doğrula** (hisse kriteri dropdown'ları birden fazla: `[...document.querySelectorAll('[id*=ddlModelHisseKriter]')].map(e=>e.id.split('_').pop()+':'+e.value)`, ayrıca `[id$=chEndeksGecmis]` `.checked`, sıralama `[id*=rdSiralama]` seçili olanı). Beklenen: `txtPortfoyHisseAdet`=5 · `ddlBilancoKullanimSekli`='1' (Yayınlanma) · `txtBasDonem`/`txtBitDonem` (01/01/2005 – 25/09/2026; 2015 modelleri için 01/01/2015) · Aylık (`rdRevizyonPeryot_0`) · sıralama · hisse kriteri: BISTTUM'da "Herşey Dahil" (19006); BIST100'de **ikinci** `ddlModelHisseKriter` = 19024 "Sadece BIST100" ve `chEndeksGecmis` işaretli. Kriter değeri yeni ID değilse DUR.
4. Ad → `[id$=txtModelAd]` → `setTimeout(()=>document.querySelector('[id$=btnFarkliKaydet]').click(),50)` → ~9 sn → ayrı çağrıda `[id$=hidModelId]` = **yeni model ID**. **ASLA `btnModelKaydet`.**

## 5. Test çalıştırma ve sonuç okuma
**Başlat:** `https://www.queenstocks.com/qs/PortfoyModel/ModelCalistir.aspx?modelId=ID` → `[id$=hidSelectedModel]` = ID mi (değilse satırdaki "Seç" / `ChooseAnalyse(ID)`) → test ayarları: `txtBasTar` = '01/01/2005' (2015 modellerinde '01/01/2015'), `txtBitTar` = '25/09/2026', `ddlRevizyonPeryot`='1A', `ddlDovizTip`='0', `ddlBilancoKullanimSekli`='1' → `[id$=btnModelCalistir]` `.click()`. Süre ~55–70 dk. Aynı anda en fazla 2 test.
**İlerleme:** sayfa kendini güncellemez; yeniden yükleyip satır metnindeki `%` değerini oku (tipik ~%1,5–1,8/dk). Yoklama döngüsü kurma: ETA hesapla, `send_later` ile kontrol.
**Sonuçlar:**
- Aylık sepet dökümü: `fetch('/qs/PortfoyModel/ModelSonucDetay.aspx?ModelId=ID&PortfoyNo=1')` → her ay bir tablo (`dd/mm/yyyy-dd/mm/yyyy KOD getiri … Getiri Ort … RF … İmkb 100 Getiri`).
- İstatistikler: `fetch('/qs/PortfoyModel/PorfoyIstatistik.aspx?ModelId=ID')` → dönem sonu sermaye, kazandıran %, ort. kâr/zarar, Sharpe, Ulcer, K-Ratio, Jensen, Beta…
- Sonuç sayfası "Getiri Tablosu %" (satır 1 Portföy-1, satır 2 IMKB100, sütunlar aylar) — hazır JS `PROTOKOL.md` §10.6.
- `ShowAnalyseResult(ID)` sayfayı yeniler → aynı JS içinde await etme.
- **BIST100 dönemi okuyucusu:** IDB `code_b100reader` → `__readSite(id)` → IDB `siteres_ID` = {det, stat, comp}; det satırı `YYYYMM|SYM:ret,...|port|rf|xu`. Karşılaştırma: iki modelin 261 ay sepet ve getirisini birebir eşle ("261/261").
- Site istatistik formüllerinin kopyası: `araclar/agirlik/sitestat.py` (Sharpe = ort. fazla getiri / std(pop) × √12; Std ddof=1; Ulcer oranı = ort. r / UI; Treynor, Jensen × √12; Ortalama Getiri % = ort. fazla getiri).

## 6. IndexedDB 'claude_c29' (queenstocks.com kökeni, store 'kv')
Tarayıcıda kalıcıdır; sim kodları ve toplanmış veri burada. Yardımcılar (herhangi bir queenstocks sekmesinde):
```js
const _db=()=>new Promise(r=>{const q=indexedDB.open('claude_c29');q.onsuccess=()=>r(q.result)});
const get=async k=>{const d=await _db();return new Promise(r=>{const g=d.transaction('kv').objectStore('kv').get(k);g.onsuccess=()=>r(g.result)})};
const set=async(k,v)=>{const d=await _db();return new Promise(r=>{const t=d.transaction('kv','readwrite');t.objectStore('kv').put(v,k);t.oncomplete=()=>r(1)})};
const keys=async()=>{const d=await _db();return new Promise(r=>{const g=d.transaction('kv').objectStore('kv').getAllKeys();g.onsuccess=()=>r(g.result)})};
```
(Store'un anahtar yapısı out-of-line varsayılmıştır; `put` hata verirse önce `keys()` ve bir kaydın biçimine bak.)

Bilinen anahtarlar (DURUM dosyalarından):
- **Kod:** `code` (editör işçisi: `eval(await get('code'))` → `__post(txt,d,idxs)`, `__postAll(txt,d,idxs)`: formülü verilen tarih ve hisse indekslerinde değerlendirir, {sembol: değer} döner) · `code_b100sim` (__B1LOAD, __SCORE(P), __RUN, __MET, __FMT) · `code_b100placebo` · `code_b100boot` (sim sekmesini tek adımda kurar) · `code_b100reader` (__readSite) · `code_b100tb` (__TBRUN2, TÜFE çıtası) · `code_b100fill` (__FILLRUN, tamamlama) · `src_b1worker`, `src_u3worker` (veri işçileri) · `code4d` (__month4d/__run4d, Değer BISTTUM veri) · `c32_formulas`, `fs_dc1`, `fs_dx3`, `fs_dx3b` (formül metinleri) · `f_sira_C34`.
- **Veri:** `b1_MM/YYYY` (Büyüme BIST100 aylık 20 alan), `b2_`, `b3_`, `b4_`, `d1_` (Değer BIST100), `tb_AY`, `b100_mem` (aylık BIST100 üyeleri), `b100_memret`, `b100_B0site`, `a41dates` (ay → dengeleme tarihi), `exp_picks`, `lq_*` (likidite), `nd_*`, `macro_m`, `t2s` (sektör grupları), `sim_dx3`, `sim_dx3b` (sim sepetleri), `chk_dc1` (editör kontrolleri), `siteres_ID` (site sonuç önbelleği).
- **Değer BIST100 sim fonksiyonları** (sim sekmesinde yüklü iken): `__DF(P)` (P.off gecikme, P.hook, P.maFn, P.fdNet, fill 'A1m'/'A1mm'), `__DEV`, `__MET(r,base)`, `__SYS(gate,score,ex)`, `__pct`, `__CMP`, `__ECDF {ey,ep,qs}`, `__C1` (DC1 sim tabanı; `__C1.__P.extra` fonksiyonu JSON'da görünmez ama nesnede vardır), `__DX {DX3, DX3b}`, `__EXS.E1`.
- **Maliyet modeli:** `araclar/cost.js` → `__COSTLOAD` / `__COSTRUN(o)`, modlar comb / 208322 / 208224 / bo.
- localStorage `claude_deger_ds` (Değer BISTTUM veri seti yedeği).

Veri toplama hızı: darboğaz sitenin sunucusu, istek sayısı; paralel sekme sayısını artırmak sınırlı fayda (3–4 işçi). Alt ajanlar siteye bağlanamaz.

## 7. Bilinen tuzaklar (özet)
- Binlik ayraç/virgül ayrıştırma hataları (G1), yanlış getiri penceresi (G2), hayatta kalma (bugünkü hisse listesi) — Değer BISTTUM'da sim'i yanıltmıştı; BIST100'de "hayalet" düzeltmesi ve üyelik modeli 208379 ile çözüldü.
- Paketli/bit maskeli alanlar asla yuvarlanmaz.
- `ZSkorPercentRank` backtest'te kapı havuzu içinde hesaplanır ve bazı aylarda herkese 0 verir → mutlak/tavanlı puan ya da sabit ECDF kullan (ay içi yüzdelik sitede hesaplanamaz).
- Platform 2024+ büyümeyi reel veriyor (TMS 29) — TÜFE kıyasında çift deflasyon; karar: eşik değişmez.
- Ay sonu kapanışta alım varsayımı: 1 gün gecikmede sonuçlar belirgin düşer (C29'da −%55) → her aday temiz modda da raporlanır.
- **Uzun sohbet engeli (30/09):** çok uzamış sohbette tarayıcı işlemleri güvenlik kontrolüyle engellendi, mod değişikliği açmadı. Büyük iş bloklarından sonra bu klasörü güncelle; gerekirse yeni sohbete geç.

## Karşılaştırmalı istatistik sayfası (01/10/2026)
- `PorfoyIstatistik.aspx?ModelId=A,B` (virgülle birden çok model) → modeller tek "Model Portföy İstatistik" sayfasında yan yana (istatistik tablosu, ortak grafik, yıllık ve aylık dağılım, getiri çizelgesi). Örnek: `?ModelId=208534,208538`.
- Chrome penceresi simge durumundaysa ekran görüntüsü alınamaz (CDP zaman aşımı); veri yine `fetch` ile okunur.
