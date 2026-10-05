# QueenStocks — Tüm Metrik Madenciliği ve Yerel Kalıcı Altyapı (Cowork görev promptu)

> **Hazırlanma notu ve öncelik kuralı:** Bu prompt 05/10/2026'da bir Claude Code bulut oturumunda hazırlandı. O oturumun siteye ve Chrome'a erişimi yoktu. İçindeki rakamlar klasördeki dosyaların **01/10/2026** durumundan alındı. **Önce klasördeki güncel dosyaları oku.**
> - **Olgularda** (rakam, ID, ilerleme, 01/10 sonrası gelişmeler) klasördeki güncel dosyalar bu prompttan önce gelir.
> - **Yöntemde ve görev tanımında** bu prompt (Ömer'in 05/10 talimatı ve kabul ettiği süzgeç çerçevesi) eski dosya kurallarının üstündedir. Bu promptun **açıkça değiştirdiği** kurallar: (a) büyük veri setleri de diske yedeklenir (07 §1 değişir); (b) BISTTUM'un evren ve getiri kaynağı üyelik modeli 208552'dir (07 §2'deki "BISTTUM'da bu yapılamaz" cümlesi geçersiz); (c) Dipten Dönüş'ün "tur başına en fazla 6 aday" kuralı yalnız ön kayıtlı elle turlar (Bölüm 3) içindir; Ömer 01/10 11:25'te tarama için bu sınırı kaldırdı ("çok fazla test edelim, ~10 bin"); tam taramada (Bölüm 5) yerini aile/eşik mekanizması alır; (d) Şampiyon V2'nin üstüne kilitli kasa, deneme sayısıyla yükselen eşik, sahte metrik kontrolü ve en fazla 3–4 ekleme sınırı gelir; (e) sim–site için "%90 aynı sepet" alt sınırı eklenir.
> - Bir çelişki görürsen DURUM'a yaz, ilgili dosyayı (01, 07, ön kayıt) güncelle; emin değilsen Ömer'e sor. **Ömer'in en son sözü her şeyin üstündedir.**

---

## Ömer için kısa özet

1. Önce bilgisayarına kalıcı bir altyapı kurulacak: sim kodları ve toplanan bütün veri `Masaüstü\QueenStocks Projesi` klasörüne dosya olarak yazılacak, sim Python'da tarayıcısız çalışacak. Veri toplama ve site testleri yine Chrome'da yapılır; ama Chrome düşerse iş kaldığı yerden sürer, hiçbir şey baştan kurulmaz.
2. Sonra Dipten Dönüş Stratejisi bugünkü yöntemle nihai algoritmasına kadar bitirilecek.
3. Ardından 3 nihai stratejide (Dipten Dönüş, Büyüme K10, Değer C32) QueenStocks'taki **bütün** metrikler 2005–2026 için her ay ve her hisse için toplanacak, hiçbiri atlanmayacak.
4. Bu metriklerin hepsi simde ve makine öğrenmesinde denenecek. Şampiyon V2'yi ve üstüne eklenen sıkı şans süzgecini geçenler adım adım algoritmaya eklenecek, sonra sitede test edilecek. V2'yi geçip yalnız şans süzgecine takılanlar da sana ayrı tabloda gösterilecek; karar senin.
5. Gerçekçi beklenti: kusursuz seçim çıkmaz. 1–3 gerçek metrik ve ölçülü bir iyileşme beklenir. Hiçbir şey çıkmaması da değerli bir sonuçtur, "her şeyi denedik" demektir.
6. Süre (kaba tahmin, ölçümle netleşir): kurulum birkaç gün; tüm metrik veri toplama kesintisiz çalışırsa ~1–2 hafta, oturum düşmeleriyle takvimde 2–5 hafta; strateji başına madencilik birkaç gün + site testleri. Toplam birkaç hafta. Bu sürede bilgisayar geceleri açık kalmalı.

**Ömer, bunu şöyle kullan:** Bu dosyayı indir ve `Masaüstü\QueenStocks Projesi` klasörüne koy. Cowork'te yeni bir sohbet aç, klasörü "Add folder" ile bağla, dosyayı sohbete sürükle ve şunu yaz: *"Bu dosyadaki görevi uygula. Bölüm 0'dan başla."*

### Bilgisayar başında olman gereken anlar (Cowork sana önceden haber verir)
1. Bölüm 0: sorulara cevap (telefondan da olur).
2. Bölüm 1: klasöre yazma izni — iki kısa tıklama (bir kez hemen, bir kez Chrome'u kapatıp açınca), ya da indirme ayarı (1–2 dk).
3. Bölüm 2: Python kontrolü/kurulumu ve `.bat` dosyalarına çift tıklama (5–10 dk, istersen).
4. Gece çalışmasından önce bir kez: uyku ayarı, Chrome bellek tasarrufu istisnası, Windows Update duraklatma (adımlar Bölüm 0'da).
5. QueenStocks oturumu düşer ve Borfin yönlendirmesi de açılmazsa giriş yapma.
6. Bölüm 3 ve 7'de şampiyon kararları.

### Ömer'e gerçekçi beklenti
Yüzlerce metriği binlerce şekilde denersek, bazıları **şans eseri** iyi görünür. Bunun önüne geçmek için: veri üçe bölünecek; son ~6 yıl (Ocak 2021–Eylül 2026, 69 ay) kilitli kasada tutulacak ve en sonda **bir kez** açılacak; deneme sayısı arttıkça başarı eşiği yükselecek; havuza bilerek sahte metrikler konup süzgecin bunları eleyip elemediği ölçülecek. Makine öğrenmesi şampiyon olmayacak, yalnız fikir verecek; bulduğu şey sade bir kurala çevrilip simde Şampiyon V2 ile sınanacak.
Literatürdeki kaba kurala göre canlıda Sharpe (risk başına getiri) testte görülenin yarısı ile üçte ikisi arasında beklenir. Taramayla bulunan **ek** iyileşmelerde düşüş daha büyük olabilir (sınırda kalan bulgular sert kırpılır — Harvey–Liu); buna simin siteye göre iyimserliği de eklenir. Bu yüzden ek iyileşmenin canlıda yarıdan azı beklenmelidir. 21 yıllık veride ayda +%0,3–0,5'lik küçük bir iyileşmeyi şanstan ayırmak için yalnız 10–25 bağımsız deneme "hakkı" vardır; binlerce deneme yaptığımız için eşik yükselir ve büyük olasılıkla yalnız önceden gerekçesi olan (literatür/katalog) metriklerden ya da büyük ve her dönemde tutarlı farklardan gerçek bulgu çıkar. Bu yüzden "az ama sağlam" hedefleniyor.

---

## Cowork için görev

Bu bölüm sana, yani Cowork'e (Claude) yazıldı. Ömer yazılım bilmiyor. Ona Türkçe, kısa ve rakamlı yaz. Teknik ayrıntıyı dosyalara ve kendi kayıtlarına koy.

Bu promptu ilk iş klasöre kaydet: `projeler/tum_metrik/GOREV_PROMPTU.md`. Sohbet düşerse yeni sohbet buradan devam eder.

### Ömer ne istiyor (kendi sözleri, yazımı düzeltilmiş, anlamı aynen)

> (1) "Biz burada önce ilgili strateji hakkında literatür çalışması yapıyorduk. Sonra bu çalışmanın bulgularıyla metrik araştırması yapıp QueenStocks'tan ilgili metrikleri çekiyorduk. Sonra bu metrikleri önce (siteden önce) kendi simülasyonumuzda test ediyorduk. Şampiyon V2 diye bir kriterimiz vardı: 2005–2015 ve 2015–2026 yarılarının ikisinde de anlamlı artan, istatistiksel olarak anlamlı, sermayeyi büyüten, bu artışı tek bir yıla yığmayan ve en iyi kazanan 5 ayı çıkarsak bile artıda kalan algoritmayı şampiyon yapıyorduk. Literatür tarafı bitince seçilen her hisseye tek tek iniyorduk: 2005–2026 arasında seçilen hisselerde istemediğimiz bir temel özellik ya da bilançoda görmediğimiz bir kaçak var mı diye bakıyor, algoritmamızın zayıf yönünü hisse seçimlerinden anlamaya çalışıyorduk. Buradan bir şey çıkarsa bu tür hisseleri nasıl eleyeceğimizi düşünüp kapıya ya da sıralamaya bir şey ekliyor, simülasyonda test ediyorduk; anlamlı ayrışma varsa şampiyon ilan ediyorduk, yoksa 'buradan bir şey çıkmadı' diyorduk. Daha sonra ilgili stratejiye göre 2005–2026 arasında her yılın en çok kazandıranlarına bakıyorduk: hangi hisseyi neden bulamamışız? Bir kaçak varsa tespit edip yine simülasyonda test ediyorduk. Buralardan anlamlı bir şey çıkarsa sitede test edilmeye layık görülüyordu. Bu kurgunun işlemesi için simülasyonun site sonuçlarıyla %90 oranında benzer olması gerekiyordu."
>
> (2) "Bazı metrikler/rasyolar literatürde olmamasına rağmen algoritmaya çok anlamlı biçimde olumlu seçimler yaptırdı. QueenStocks'ta kullanılan TÜM metrikleri 2005–2026 arasında her ay ve her hisse için çekelim, hiçbir metriği atlamadan. Sonra bu metriklerin hepsini makine öğrenmesiyle de test edelim, Şampiyon V2 kuralını sağlayanları ayıralım, sonunda bunları siteye teste verelim ve çıkan her metriği adım adım algoritmamızın üstüne ekleyip kombine ederek ilerleyelim. Böylece hiçbir metriği atlamamış, QueenStocks'ta yapılabilecek her şeyi denemiş oluruz, hem de çok hızlı."
>
> (3) "Makine öğrenmesini senin önerdiğin şekilde kullanmak istiyorum: şampiyonun kendisi olarak değil, fikir kaynağı olarak. Bulunanlar sade kurala çevrilir, simde Şampiyon V2 ile test edilir."
>
> (4) "Bunu simülasyonun sonunda uygularız. Dipten Dönüş Stratejisi için en nihai algoritmayı belirledikten sonra, nihai olarak belirlediğimiz 3 stratejiyi bu tüm metrik kurgusuyla yaparız. Buradan belki literatürde olmayan anlamlı şeyler çıkar ve algoritmamız anlamlı biçimde ayrışır."
>
> (5) "Şampiyon V2 kriterlerini eksik vermiş olabilirim, Cowork bunu zaten biliyor. Benim yazdıklarımı yazarsan sadece gidip onu uygular; bu noktada kendi bildiğini yapacak şekilde yazmamız lazım."
>
> (6) "Bu yapıyı benim bilgisayarımda kursun istiyorum. Benim bilgisayarımda olsun, çünkü bazen Chrome düşüyor ve simülasyonu baştan kurmak zorunda kalıyor."
>
> (7) "Çok detaylı olsun, yapacaklarımız adım adım yazsın, görevleri adım adım böl."

Ömer önceki sohbette şu çerçeveyi kabul etti: **"çok deneyen şans eseri bulur"**. Tam tarama yapılır ama süzgeç sıkı tutulur: üçlü veri bölümü (eğitim / doğrulama / kilitli kasa), deneme sayısıyla yükselen eşik, ekonomik açıklaması olmayan bulguya "keşif" etiketi, en fazla 3–4 ekleme, kasa yalnız en sonda ve **bir kez** açılır. ML fikir kaynağıdır. Gerçekçi beklenti 1–3 gerçek metriktir.

### Şampiyon V2: tam ve bağlayıcı metin dosyadadır

**Bağlayıcı tek kaynak:** `01_KURALLAR_VE_TERCIHLER.md` §C.4 "Terfi kuralı v2". **Onu dosyadan kelimesi kelimesine oku ve uygula; hiçbir maddeyi atlama.** Ömer'in (1) numaralı sözü özettir; orada olmayan maddeler (kazandıran ay, Sharpe ve kriz, plato, 5'ten az hisseli ay, plasebo, temiz mod ve maliyet, t kademeleri) de geçerlidir. 05 dosyalarında aynı kural "Şampiyon kuralı v2" / "ŞAMPİYON KURALI v2 (PROTOKOL v2)" adıyla geçer; Ömer'in "Şampiyon V2" dediği budur. Bulut hafızanda ya da strateji DURUM dosyalarında V2'ye dair burada ve §C.4'te olmayan bir madde biliyorsan onu da uygula ve Ömer'e göstererek §C.4'e işle; çelişkide daha sıkı olan geçerlidir.

01/10 itibarıyla §C.4'ün metni (yalnız hatırlatma; dosyada daha yeni hali varsa o geçerlidir):

> 1. Son sermaye ≥ şampiyon × 1,05
> 2. Kazandıran ay ≥ şampiyon − 0,5 puan
> 3. Sharpe ≥ şampiyon; kriz ayları ortalaması ≥ şampiyon
> 4. 2005–15, 2016–26 ve 2015+ ayrı ayrı olumlu
> 5. En iyi 5 ay çıkarılınca fark hâlâ olumlu
> 6. Plato: komşu düzeyler aynı yönde (tek sivri tepe değil)
> 7. 5'ten az hisseli ay sayısı artmaz
> 8. Plasebo (200 tohum, aynı sayıda rastgele değişiklik) %95'in üstünde
> 9. Anlamlılık (uygulamadaki biçimiyle): eşli Newey-West t ≥ 1,5 → terfi edebilir. 1 ≤ t < 1,5 → diğer maddeleri geçiyorsa "zayıf" etiketiyle siteye gidebilir ama karar site sonucuna bağlıdır ve terfi için site farkı da kuralı geçmelidir (Büyüme BIST100 K3b/K4 böyle değerlendirildi; Değer BIST100 DX3b t 1,45 ile terfi etmedi, seçim Ömer'in kararı oldu). t < 1 → reddedilir. Çoklu test sonrası "güçlü" ≈ t 2,8. Deneme sayacı tutulur; final aday için Deflated Sharpe raporlanır. (Değer BISTTUM PROTOKOL v2'de "t ≥ 1,5 veya plasebo %95 üstü" yazıyordu; BIST100 projelerinde yukarıdaki biçim kullanıldı.)
> 10. BIST100 için: yeni kurallar emülasyonu (E1) her adayda raporlanır ve olumlu olmalı
> 11. Temiz mod (1 gün gecikme) ve gerçekçi (maliyetli) hesapta da olumlu

Dikkat edilecek noktalar:
- **Yarılar:** Ömer "2005–2015 / 2015–2026" dedi. Dosyada 2005–15, 2016–26 ve ayrıca 2015+ olarak üç dilim var; dosyadakini uygula.
- **"Tek yıla yığılmasın":** 4. ve 5. maddelerle karşılanır. Ek olarak her adayda "farkın yıllara dağılımı" raporlanır; tek yıl farkın %60'ından fazlasını taşıyorsa aday "şüpheli" sayılır (Değer'in mekanizma kontrolü).
- **Strateji ekleri ve öncelik kuralı:** Büyüme BISTTUM'un ALFA eki (5'ten az hisseli ay en fazla +6), "03:10 J eki" (ayrıntı `projeler/alfa_v41/DURUM.md`) ve "tekil terfi için t ≈ 3" notu; Dipten Dönüş'ün "DSR ≥ 0,95, PBO ≤ 0,25" eki geçerlidir. **Bir ek ile 01 §C.4 çelişirse daha sıkı olan uygulanır.** Kuralı gevşeten ekler — Değer'in 28/09 kullanıcı eki (eski "Kabul 7.3"e bağlı: kazandırma ≥ +2 puan, Sharpe ≥ ve kriz ≥ ise sermaye %15'e kadar düşebilir, bir alt dönemde tolerans −6) ve Büyüme/Değer BISTTUM'daki "plasebo VEYA t" biçimi — yalnız Ömer onaylarsa ve yalnız "V2 hükmü" sütununda kullanılır (Bölüm 0, soru 6). Şans süzgecinde (Süzgeç-1, 2, 5) her zaman sıkı biçim geçerlidir.
- **İki hükümlü tablo:** her aday için "V2 hükmü" ve "şans süzgeci hükmü" yan yana raporlanır. "V2 geçti – şans süzgeci geçmedi" listesi Ömer'e ayrı verilir; bunları siteye gönderip göndermeme kararı Ömer'indir (01 §C.8, §D.2); böyle bir aday "zayıf/keşif" etiketi taşır.
- **Ad çakışması:** Dipten Dönüş `YOL_HARITASI.md` dosyasında "5. Şampiyon V2" bir **aşamanın** adıdır. Bu promptta "Şampiyon V2" dendiğinde **terfi kuralı v2** kastedilir.
- **Yeni sıkılaştırmalar V2'nin yerine değil, üstüne gelir.** Kasa (2021–26) ve t* Dipten Dönüş yol haritasında zaten var (yöntem ekleri 3e) ve Tarama 2b'de uygulandı. Yeni olanlar: 2016–2020 doğrulama dilimi, sahte metrik kontrolü, önsel gerekçe aileleri ve en fazla 3–4 ekleme. Bunlar Bölüm 5.0'da ön kayda yazılarak resmîleşir ve 01 §C'ye "C.10 Tüm metrik süzgeci" olarak işlenir (Ömer'e göstererek). Bunların V2'ye göre yeni olduğunu Ömer'e açıkça söyle.

### Değişmez kurallar (ayrıntı: 01 §A–§H, 03, 07)

- Sitede yalnız **Farklı Kaydet** (`btnFarkliKaydet`); `btnSave` ve `btnModelKaydet` yasak. Korunan orijinallere dokunulmaz (01 §A.5). 04_ID_KAYDI'nda durumu şampiyon, orijinal-dokunma, yayın ya da araç-saklanır olan hiçbir kriter/modelin üzerine yazılmaz. Özellikle: şampiyon orijinalleri K10 98258 / 208322 · C32 98194 / 208224 · K4a 98322 / 208422 · DC1 98324 / 208424 · DX3b 98329 / 208433 · Değer BAZ 94555 / 208000 · ALFA V4.1 95237 / 203135; yayın kopyaları BISTTUM 98346 / 208452 / 208454, 98349 / 208459 / 208460 · BIST100 98322 / 208456 / 208458, 98351 / 208461 / 208462 · Katılım 98392 / 208534 / 208535, 98394 / 208538 / 208539 · üyelik modelleri 208379, 208514, 208552. Güncel tam liste 04'tedir. Hesap ve abonelik ayarlarına dokunma (01 §A.3).
- **Hiçbir şey silinmez.** Silinmesi gerekenler 04_ID_KAYDI.md ve ilgili DURUM.md'deki "Silinecekler" listesine yazılır; Ömer sitede kendisi siler. IDB'de de hiçbir anahtar silinmez (geri yükleme testi ayrı bir test veritabanında yapılır, Bölüm 2A).
- **Şifre girilmez.** Oturum düşerse https://borfin.com/tr/programs/153/redirect. Yine açılmazsa dur ve Ömer'e haber ver.
- Aynı anda **en fazla 2 site testi.** Test başlatmadan önce ModelCalistir sayfasında o an çalışan **bütün** testleri say (Ömer'inkiler ve başka oturumlarınkiler dahil); toplam 2 ise bekle. **Yoklama döngüsü kurulmaz:** testi başlat, ETA ver, `send_later` ile ~70 dk sonra kontrol et.
- Sabit test ayarları: 5 hisse, eşit ağırlık, aylık, **nakit yok** (katmanlı tamamlama: önce teknik, sonra temel gevşer), "**Yayınlanma Tarihine Göre**", 01/01/2005–25/09/2026, TL, BISTTUM için 19006. TÜFE eşiği değişmez. (Tek istisna Bölüm 5.6'daki 2005–2020 kalibrasyon modelleri; bunlar Ömer'e önceden "kalibrasyon testi" diye söylenir, 01 §C.2.)
- **Ön kayıt** sonuç görülmeden yazılır. Ön kayıt dışı bulgu "**keşif**" etiketi taşır, ileriye dönük farkı yarıya indirilerek raporlanır (01 §C.3). Bu promptta "keşif" kelimesi **yalnız bu etiket** için kullanılır; veri dönemi 2005–2015'in adı "**eğitim dönemi**"dir.
- Öncelik: **istikrar ve kazandıran ay > son sermaye**, sonra Sharpe/K-Ratio ve kriz koruması. Sadelik esastır.
- **Strateji strateji ilerle** (01 §B.6). Simde olumlu ayrışmayan aday siteye gitmez (01 §C.2). Havuz IC'si portföy iyileşmesi demek değildir.
- **Kaçan kazananlar testi** (01 §C.9, `code_kzwin`) her şampiyon ve şampiyon adayında yapılır.
- **Çift hafıza kaydı:** bulut hafızası ve `06_HAFIZA/` birlikte güncellenir (01 §G).
- Raporlar Türkçe, kısa ve rakamlı. Korelasyonlar yüzde verilir (0,80 değil %80; 01 §D.4). Anlamsız sonuç "anlamsız" diye söylenir. Şampiyon ilanı **Ömer'in kararıdır** (01 §C.8).
- Alt ajanlar siteye bağlanamaz. Site ve Chrome işleri sende kalır; alt ajanlara yalnız dosya ve Python işi verilir.
- Pencere simge durumunda ya da arka plandayken (zamanlayıcılar yavaşlar) `__postF` kullanılır. Gizli (Incognito) pencere **hiçbir zaman** kullanılmaz; orada ne oturum ne IDB vardır.

### Adlar (karışmasın diye)
- **Eğitim dönemi** 2005–2015 (alt yarılar 2005–2009 / 2010–2015) · **Doğrulama** 2016–2020 · **Kasa** 2021–01…2026-09 (69 ay).
- **Süzgeç-1 … Süzgeç-6:** Bölüm 5.5'teki süzgeç adımları (Büyüme'deki K1–K10 varyantları ve DD'deki S1/S2 skor kodlarıyla karışmasın).
- **Öncelik-1/2/3:** hasat katmanları (Bölüm 4.4). Ek olarak **Öncelik-0:** K10/C32 kalibrasyonu için eksik alanlar (Bölüm 2B).
- **FSA yolu** (klasöre doğrudan yazma), **İndirme yolu** (Blob indirme), **Parça yolu** (900 karakter). 07 §1'deki eski "Yol A/Yol B" etiketlerini de bu adlarla değiştir.

### Genel akış
Bölüm 0 → 1 → 2A → 3 (Dipten Dönüş nihai) → 4 (hasat, üç strateji için bir kez) → her strateji için sırayla [2B (yalnız K10/C32) → 5 → 6-A → kasa → 7 → 6-B → Ömer'in kararı] → 8. Bir strateji Ömer'in kararıyla (ya da "geçen yok" kararıyla) kapanmadan sıradakine geçilmez. Ayrıntılı strateji içi sıra: Bölüm 5.8.

---

## Bölüm 0 — Başlangıç: oku, envanter çıkar, Ömer'e sor

**Amaç:** güncel durumu öğrenmek ve başlamadan gereken onayları almak.

**Yapılacaklar:**
1. `00_BASLA_BURADAN.md` protokolünü uygula. **Tam oku:** 00, 01, 02, 03, 07, `OTURUM_GUNLUGU.md`'nin son 10 satırı, `projeler/dipten_donus/` içindeki DURUM.md, YOL_HARITASI.md, ON_KAYIT_TABAN.md ve LITERATUR.md (sentez). **Yalnız gereken bölümü grep ile oku:** LIT_A–D (özellikle Süzgeç-4 ve ön kayıt sırasında), 04_ID_KAYDI, 05_PROJE_GECMISI, `araclar/METRIK_KATALOGU.md`. Bağlamı şişirme: uzun sohbette tarayıcı işlemleri engellenebiliyor (00 §6, 03 §7). Hafıza senkronunu yap (`memory_list` → farklar → `06_HAFIZA`).
2. Klasörde şunların **var olduğunu doğrula** ve eksikleri listele: `araclar/METRIK_KATALOGU.md`, `araclar/b100/cmp.py`, `araclar/agirlik/sitestat.py`, `araclar/cost.js`, `araclar/sim_kodlari/`, `projeler/deger_v11/` (sim.js, kacak_worker.js, analiz_motoru.js…), `projeler/dipten_donus/` (yoksa kökte `dipten_donus/` ara; bulduğun yolu DURUM'a yaz).
3. 01/10'dan sonra ne olduğunu çıkar. dd2 hâlâ 55/262 mi? Yeni şampiyon veya ID var mı?
4. **Disk ve OneDrive:** klasör yolunda OneDrive geçiyor mu, boş disk kaç GB? İkisini DURUM'a yaz. OneDrive altındaysa ya da boş alan 30 GB'ın altındaysa `veri/` klasörünü OneDrive dışına (ör. `C:\QueenStocks_veri\`) almayı ve Cowork'e ikinci klasör olarak bağlamayı öner; alternatif: `veri/` için "Bu cihazda her zaman tut" + hasat süresince eşitlemeyi duraklatmak. Kod ve md dosyaları yerinde kalır.
5. Chrome: `tabs_context_mcp` çağır. Cowork'ün yerleşik tarayıcısını değil, **Claude in Chrome**'u kullan. queenstocks.com sekmesinde IDB `claude_c29` / `kv` için `keys()` çalıştır ve anahtar sayısını önek bazında çıkar (`code_*`, `src_*`, `fs_*`, `u3_*`, `dd_*`, `dd2_*`, `siteres_*`, `b1_*`, `d1_*`, `lq_*`…). `navigator.storage.estimate()` sonucunu ve `navigator.storage.persisted()` durumunu DURUM'a yaz.
6. **Kalıcı kararları kaydet:** Ömer'in bu görevdeki kalıcı kararlarını bulut hafızasına VE `06_HAFIZA/preferences.md`'ye aynı [stated] satırlarıyla yaz, `SON_SENKRON.txt`'yi güncelle: (1) bir strateji nihai olunca "tüm metrik kurgusu" uygulanır, QueenStocks'taki hiçbir metrik atlanmaz; (2) ML şampiyon değil fikir kaynağıdır, bulgular sade kurala çevrilip simde V2 ile sınanır; (3) sim ile site en az %90 aynı sepet vermelidir; (4) kod ve veri diskte asıl kaynaktır, IDB ara bellektir; (5) tam tarama + sıkı süzgeç (eğitim/doğrulama/kasa, deneme sayısıyla yükselen eşik, en fazla 3–4 ekleme, kasa bir kez).
7. `projeler/tum_metrik/YOL_HARITASI.md` dosyasını oluştur (Bölüm 0–8 özeti ve durum işaretleri). `02_SIRADAKI_ISLER.md`'nin en üstüne "Aktif iş: Tüm Metrik (projeler/tum_metrik/GOREV_PROMPTU.md)" satırını ekle.
8. Ömer'e **tek mesajda** aşağıdaki soruları sor; cevapları `projeler/tum_metrik/DURUM.md`'ye yaz.

**Ömer'e sorulacaklar (tek mesaj, kısa):**
1. "Nihai 3 strateji = **Dipten Dönüş (nihai sürüm)**, **Büyüme Stratejisi BISTTUM (K10)**, **Değer Yatırımı BISTTUM (C32)**. Evren önce **BISTTUM**; BIST100 ve Katılım sürümlerini sonra soracağım. Sıra: önce Dipten Dönüş, sonra Büyüme K10, sonra Değer C32. Doğru mu?"
2. "Tüm metrik veri toplama (hasat) sitenin sunucusunu Dipten Dönüş işleriyle paylaşır. Kurulumun sonunda kısa bir hız ölçümü yapıp sana net süreyi söyleyeceğim. Hasat Dipten Dönüş bitmeden geceleri arka planda başlasın mı, yoksa sonra mı? Not: hasat yüz binlerce istek demek; bu normal kullanımın çok üstünde ve sağlayıcı (Borfin/QueenStocks) hesabı kısıtlayabilir. Bu yüzden hızı düşük tutacağım; istersen günlük bir üst sınır da koyarım. Kabul ediyor musun?"
3. "Bilgisayarındaki klasöre yazabilmem için iki kez ~10 saniyelik tıklaman gerekecek (bir kez şimdi, bir kez Chrome'u kapatıp açınca). Hangi saatte bilgisayar başında olabilirsin?"
4. "Hasat ölçümlere göre büyük olasılıkla 1–3 hafta sürecek (pilottan sonra net süre vereceğim). Gece gözetimsiz çalışmasına onay veriyor musun? Oturum gece düşerse sabah giriş yapman gerekebilir. Bilgisayarda bir kez şunları yap: (a) Ayarlar → Sistem → Güç → Ekran ve uyku → 'Prize takılıyken uyku moduna geç: Hiçbir zaman'; (b) Chrome → Ayarlar → Performans → Bellek Tasarrufu → 'Bu siteleri her zaman etkin tut' listesine queenstocks.com ekle; (c) Ayarlar → Windows Update → 'Güncellemeleri duraklat' (hasat süresince)."
5. "Bilgisayarında Python var mı, bakalım: Başlat'a 'cmd' yaz, açılan siyah pencereye `python --version` yazıp Enter'a bas, çıkan satırı bana gönder (Algomer'den kurulu olabilir). Yoksa 5 dakikalık kurulumu adım adım yazarım (python.org → Windows installer → 'Add python.exe to PATH' işaretli → Install; ya da tek satır: `winget install -e --id Python.Python.3.12`). İstemezsen motor benim ortamımda çalışır; kod ve veri yine senin klasöründe kalır."
6. "Değer için 28/09'da verdiğin gevşetme (kazandırma 2 puan artar, Sharpe ve kriz kötüleşmezse sermaye %15'e kadar düşebilir; bir alt dönemde −6 tolerans) ve Büyüme/Değer'deki 'plasebo VEYA t' biçimi tüm metrik çalışmasında da geçerli mi, yoksa 01'deki sıkı biçim mi?"
7. (Disk durumu gerektiriyorsa) "Klasörün OneDrive içinde / disk dolu; veriyi `C:\QueenStocks_veri` klasörüne koyup onu da Cowork'e bağlamanı isteyeceğim. Uygun mu?"

**Çıktı:** `projeler/tum_metrik/DURUM.md` (ilk kayıt), `GOREV_PROMPTU.md`, `YOL_HARITASI.md`, IDB anahtar envanteri (DURUM'da önek, adet, tahmini boyut), disk/OneDrive notu.
**Bitti ölçütü:** dosyalar okundu, eksikler listelendi, IDB envanteri çıkarıldı, hafıza kaydı yapıldı, Ömer soruları yanıtladı.
**Ömer'e rapor:** 5–8 satır: durum, eksik dosyalar, cevaplara göre plan ve ilk ETA. Ayrıca bir satır: "C32 kalibrasyonu riskli (geçmişte 231/261)."

---

## Bölüm 1 — Yerel klasör yapısı ve IDB → disk aktarımı

**Amaç:** Chrome veya IDB silinse bile **hiçbir kod ve veri kaybolmasın**. Asıl kaynak disk olur, IDB yalnız ara bellek. 07 §1'deki "büyük veri setleri yedeklenmez" kuralı değişir; 07'yi güncelle.

**1.1 Klasör yapısı** (mevcut dosyalara dokunma, yalnız ekle):
- `veri/ham/<önek>/<AA-YYYY>.ndjson`: ay başına, önek/katman başına **tek dosya** (her satır bir paket). Paket eklendikçe yeni sürüm yazılır, manifest güncellenir. Mevcut veri setleri `veri/ham/<önek>/` altına aynı düzenle.
- `veri/islenmis/`: Python çıktıları (Bölüm 4.7: aile başına Parquet / metrik başına .npy).
- `veri/manifest/`: `manifest.csv` (ad, bayt, SHA-256, kayıt sayısı, şema sürümü, hasat tarih-saati), `kuyruk.csv`, `ilerleme.json`.
- `veri/denemeler/<strateji>/`: deneme fark serileri (Bölüm 5.3).
- `araclar/sim_kodlari/`: IDB'deki **tüm** `code_*`, `src_*`, `fs_*` ve benzeri kod anahtarlarının birebir yedeği (`<anahtar>.js`).
- `araclar/sim_py/`: Python sim motoru · `araclar/kurulum/`: geri yükleme ve ortam betikleri.
- `projeler/tum_metrik/`: DURUM, YOL_HARITASI, ON_KAYIT_*, METRIK_ENVANTERI, DENEME_SAYACI, CANLI_IZLEME.csv, `raporlar/`, `gizli/`.

**1.2 Aktarım yolunu pilotla seç** (önce 1 kod anahtarı + 1 aylık veri dosyasıyla):
- **FSA yolu (File System Access API), tercih edilen:**
  1. Ömer bilgisayar başındayken sayfaya "Klasörü bağla" butonu koy. Ömer tıklar, açılan pencerede Masaüstü > `QueenStocks Projesi` klasörünün **kendisini** seçer (Masaüstünün kendisi seçilemez) ve "Dosyaları düzenlemeye izin ver" der. Windows penceresine ve Chrome izin balonuna sen tıklayamazsın; Ömer'e tek cümleyle tarif et.
  2. Hemen ardından Chrome'u kapatıp açtır, butona yeniden tıklat; çıkan balonda **"Her ziyarette izin ver"** seçilsin. Dizin tutamacı IDB'de saklanır. `handle.queryPermission({mode:'readwrite'})` "granted" dönmeden FSA yolu tamam sayılmaz.
  3. Yazma kuralı: işçi **önce diske** yazar. Her yazımdan önce `queryPermission` kontrol edilir; "granted" değilse veri IDB tamponuna (`tm_buf_*`) yazılır, anahtar `disk_bekleyen` listesine eklenir ve iş durmaz. İzin geri gelince `__diskFlush()` bekleyenleri yazar ve manifesti günceller. Her kontrolde `disk_bekleyen` sayısını raporla.
- **İndirme yolu (Blob indirme):** ön koşullar: (a) Ömer Chrome'da Ayarlar → İndirilenler → Konum'u `QueenStocks Projesi\veri\gelen` yapar (ya da İndirilenler klasörünü de sohbete "Add folder" ile bağlar) — sen yalnız bağlı klasörleri görebilirsin; (b) "İndirmeden önce her dosyanın nereye kaydedileceğini sor" kapalı olmalı; (c) "birden çok dosya indirme"ye bir kez izin verilir; (d) dosya adları benzersiz (`<önek>_<AA-YYYY>_<zaman>.json`, " (1)" eklerini önler); taşıdıktan sonra SHA-256 manifestle karşılaştırılır.
- **Parça yolu (900 karakter + sağlama):** yavaş; yalnız kod anahtarları için son çare.
- FSA ve İndirme yolu ikisi de çalışmazsa: yalnız kod anahtarlarını Parça yoluyla al, Bölüm 2'ye geçme, DURUM'a yaz ve Ömer'le birlikte çöz.
- Hangi yolun çalıştığını, hızını ve sorunları DURUM'a yaz. Bölüm 1'in başında `navigator.storage.persist()` çağır.

**1.3 Serileştirme ve tür denetimi:** her anahtar için önce tür denetimi yap: `typeof` ve constructor adı; Map/Set/TypedArray/Date/Blob/fonksiyon var mı; NaN/Infinity sayısı. JSON'a güvenle dönmeyenleri etiketli biçimle yaz (`{"__t":"Map","v":[...]}`, TypedArray → base64 + tür adı, NaN/Infinity → etiketli). **Gidiş-dönüş testi:** diskteki dosyayı tarayıcıda geri oku, çöz ve IDB'deki orijinalle derin karşılaştır. Eşleşmeyen anahtar "yedeklenmedi" sayılır.

**1.4 Manifest:** her dosya için SHA-256 (tarayıcıda `crypto.subtle.digest`) diskteki dosyanınkiyle eşleşmeli.

**1.5 Mevcut her şeyi diske al:** kod anahtarlarının tamamı ve veri setleri (`u3_*`, `dd_*`, `dd2_*`, `siteres_*`, `a41dates`, `dd_need`, `dd_lists`, `dd_winners`, `dd_scan1`, `b100_mem*`, `b1_*`–`b4_*`, `d1_*`, `lq_*`, `nd_*`, `macro_m`, `t2s`, `tb_*`, `ny_*`, `kc_*`, `pb2_*` ve envanterde çıkan diğerleri), localStorage'daki `claude_deger_ds`. Değer BIST100 motorunun (`__DF`) anahtar adı kayıtlı değil; kod anahtarlarında ara, bulduğunu 07'ye yaz.

**1.6 Yeni toplama işlerinin kuralı:** bundan sonra her toplama işi **diske** yazar (1.2/3); hasatın ham verisi IDB'ye yazılmaz (IDB'de yalnız kuyruk, ilerleme ve disk yazımı başarısızsa tampon). İşçi kodlarını (`src_*`) buna göre güncelle; yeni sürümü yeni anahtar adıyla sakla, eskisini silme.

**1.7 Ön hız ölçümü (kısa, Ömer'in 2. ve 4. sorusunu rakamla yanıtlamak için):** editördeki `#selFonk` listesini JS ile oku (fonksiyon sayısı) ve 1 ay × ~40 fonksiyon (her kategoriden en az 2) ölçümü yap (≤1 saat): postback süresi, paket yoğunluğu (hassasiyet kaybı olmadan postback başına alan), 175'lik parçada hata oranı. Kaba süre: `Saat = Σ_ay ⌈o ayın üyeleri / 175⌉ × (alan sayısı / paket yoğunluğu) × postback süresi / sekme sayısı / 3600`. Ömer'e öncelik katmanı başına saat ve gün olarak bildir. Tam pilot Bölüm 4.4'tedir.

**Çıktı:** klasör yapısı, `araclar/sim_kodlari/*.js`, `veri/ham/**`, `veri/manifest/manifest.csv`, DURUM'da aktarım yolu kararı ve ön süre tahmini.
**Bitti ölçütü:** IDB envanterindeki her anahtar diskte var; SHA %100 **ve** gidiş-dönüş %100; anahtar sayısı IDB = disk.
**Ömer'e rapor:** "X kod anahtarı ve Y veri anahtarı (Z MB) diske alındı, doğrulama %100. Artık Chrome düşse de veri kaybolmaz. Hasat ön tahmini: ~N gün."

---

## Bölüm 2 — Python sim motoru, kalibrasyon ve geri yükleme

Bölüm 2 ikiye bölünür. **Bölüm 3'e geçmek için yalnız 2A gerekir.** 2B, K10 ya da C32'nin madenciliğine başlamadan hemen önce (ya da hasat sürerken paralel) yapılır.

### 2A — Bölüm 3'ten önce zorunlu (kısa tut, ETA ver)
2A Dipten Dönüş'ü bir günden fazla geciktirecekse Ömer'e "önce Dipten Dönüş'ü bitireyim mi?" diye sor.

**2A.1 Genel motor** (`araclar/sim_py/`): tek bir genel motor yaz: havuz (üyeler + hayaletler) → kapı bitleri → katmanlı tamamlama → skor → azalan sırala (eşitlikte site sırası korunur) → ilk 5 → ay getirisi = 5 site getirisinin ortalaması. Varyantlar `P` benzeri parametre nesnesiyle (gecikme dahil). Önce yalnız Dipten Dönüş motorlarının (`code_dd`, `code_ddsite`, `code_ddscan`, `code_kzwin`, plasebo) Python karşılığını yaz. BIST100 motorları (`code_b100sim`, `__DF`) bu görevde **port edilmez**, yalnız diske yedeklenir (Ömer BIST100 sürümlerini isterse taşınır). Maliyet için `araclar/cost.js` (`__COSTRUN` modları) ve `lq_*` Python'a taşınır; tek bir aday üzerinde JS ile aynı sonucu verdiği gösterilir.
- Ölçüm seti 07 §3.7–8: son sermaye, CAGR (2005–15 / 2016–26 / 2015+), Sharpe (site formülü, `sitestat.py`), K-Ratio, MDD, kazandıran ay %, kriz ayları ortalaması, <5 hisseli ay, eşli fark + Newey-West t (gecikme 6), en iyi 5 ay çıkınca fark, plasebo (200 tohum), plato, temiz mod (1 gün gecikme), maliyetli hesap, farkın yıllara dağılımı.
- **Kasa kilidi (teknik):** motorda `KASA_BASLANGIC = 2021-01`. `kasa_ac=False` iken bu tarihten sonraki ayların getirileri NaN olur ve hiçbir çıktıya girmez. `kasa_ac=True` yalnız `projeler/tum_metrik/KASA_ACILIS.csv`'ye tarih-saat, strateji ve aday listesi yazılarak çağrılabilir. JS=Python ve kalibrasyon testleri yalnız **mevcut şampiyonla** tam dönem koşar.
- **Hız hedefi:** tek sim ≤ 20 ms ve çok çekirdekli çalışma (aylar × hisseler numpy dizisi; şampiyon skoru önceden hesaplı; varyant yalnız bir sütunu değiştirir). Ölçülen sim/sn'yi ve beklenen N için tur süresini (saat) raporla.

**2A.2 Nerede çalışır:**
- Zorunlu: motor Cowork'ün kod ortamında, bağlı klasörden çalışır; bütün girdi ve çıktı klasörde durur. `araclar/kurulum/ortam_kontrol.py` her yeni sohbette paketleri kontrol eder, eksikse `requirements.txt`'den kurar (pandas, numpy, pyarrow, scikit-learn, lightgbm, shap, statsmodels).
- Ömer'in PC'sinde Python varsa (Bölüm 0, soru 5): `KUR.bat` (Python yoksa Ömer'e kurulum adımlarını gösterir) ve `CALISTIR_*.bat`. **10 dakikadan uzun işler** (büyük taramalar, ML) tercihen bu `.bat`'larla Ömer'in PC'sinde çalışır ve her 1.000 denemede bir kayıt alarak kaldığı yerden devam eder; Cowork ortamı kısa analiz ve doğrulama içindir. `.venv` OneDrive dışında kurulur. Yollar göreli; eski araçlardaki SP/B/S yol değişkenlerini klasör yoluna çevir (00 §6).

**2A.3 JS = Python eşdeğerliği (DD T0):** aynı girdiyle JS (`code_ddsite`) ve Python 261/261 ay aynı sepet, sermaye farkı ≤ %0,1. Referans T0: 0,97 mr, Sharpe 0,87, kazandıran %63,6.

**2A.4 Geri yükleme prosedürü** (`araclar/kurulum/idb_geri_yukle.js` + 07'ye yeni bölüm, metni Bölüm 8.5):
- Doğrulama testi: diskteki **tüm** kod anahtarlarını ve 3 aylık veriyi **ayrı bir test veritabanına** (`claude_c29_geritest`) geri yükle; buradan DD simini kur ve T0'ı yeniden üret (0,97 mr, Sh 0,87, kaz %63,6). Orijinal `claude_c29`'a dokunma, hiçbir anahtar silme.

**2A bitti ölçütü:** JS = Python 261/261 (DD T0); geri yükleme testi başarılı; yeni bir Cowork sohbetinde motor yalnız klasörden kuruldu ve DD T0'ı yeniden üretti; (Python kuruluysa) Ömer'in PC'sinde `.bat` ile bir sim koştu.

### 2B — K10 ve C32 kalibrasyonu (o stratejinin Bölüm 5'inden hemen önce)
1. **Veri kontrolü:** K10 ve C32'nin kapı bitleri ve skor bileşenleri 261 ay için var mı? (`u3_` yalnız kapanışlar + K10 maskesi tutuyor; K10 sıralaması için karIvmesi'nin 5 sürekli bileşeni, pen75, mom6 gerekir; C32 verisi eski `kacak_worker` / `code4d` / localStorage `claude_deger_ds`'te.) Eksikse ön kayıtlı olarak `k10_` / `c32_` alanlarını hasat kuyruğuna **Öncelik-0** katmanı olarak ekle (~25 alan ≈ 1,5 saat) ve süreyi Ömer'e bildir.
2. Motora K10 ve C32 strateji tanımlarını (P nesneleri) ekle. JS=Python karşılaştırması aranmaz; doğrudan **site sepetiyle** kalibre edilir: K10 208322 / 208452, C32 208224 / 208459 (2005–2026). Evren ve getiri: `siteres_208552` (261 ay, hayaletler dahil).
3. **Hedef ≥ 260/261 aynı sepet** (01 §C.6a). Ömer'in "%90 benzer" sözü **mutlak alt sınırdır** (≥ 235/261). 235–259 arasında farkları sınıflandır (hayalet, eşit puan, kapı farkı, veri eksiği, ZSkorPercentRank çöküşü, ECDF düğümleri), Ömer'e "devam mı, düzelt mi" diye sor. 235'in altında o stratejinin madenciliği başlamaz; yalnız o strateji bekler. C32 için: "C32 geçmişte 231/261'de kalmıştı, şimdi X/261; düzeltmeyi deneyeyim mi, C32'yi atlayalım mı?" Geçmiş: C29 232/261, C32 231/261, K6A örtüşmesi %89,3, BIST100 hayaletli 260/261; Büyüme BISTTUM'da sim ~1,4–1,8× iyimserdi. Sim/site sermaye oranını raporla.
4. **Skor eşitliği:** birkaç tarih × hisse için editördeki site SKOR'u ile Python SKOR'u eşit olmalı.

**Çıktı:** `araclar/sim_py/*`, `projeler/tum_metrik/raporlar/KALIBRASYON.md`, `araclar/kurulum/*`, güncel 07.
**Ömer'e rapor:** kalibrasyon tablosu (strateji | aynı sepet | sim/site sermaye | fark nedenleri) + tek satırlık karar.

> Büyük iş bloğu bitti. Bütün dosyaları güncelle. Sohbet uzadıysa Ömer'e yeni sohbet öner ve "devam cümlesi" ver (Bölüm 8.4).

---

## Bölüm 3 — Dipten Dönüş'ü nihai algoritmaya kadar bitir

**Amaç:** Dipten Dönüş'ü bugünkü yöntemle (Ömer'in (1) numaralı döngüsü) bitirmek. Bu promptun asıl konusu değildir; ayrıntı `projeler/dipten_donus/DURUM.md` ve `YOL_HARITASI.md`'dedir. **Yalnız 2A'yı bekler**; taramalar Python motoruyla koşulur.

**Yapılacaklar** (yol haritasındaki sırayla):
1. **dd2'yi tamamla:** dd2 55/262 ayda durmuştu. F9'daki bedelli alanının HATA'sını `||` kısa devreyle düzelt, kalan ayları topla; her ay diske (ve gerekirse IDB tamponuna) yazılsın.
2. `ON_KAYIT_T1.md`'yi **sonuç görmeden** yaz ("tur başına en fazla 6 aday" kuralı bu elle turlarda geçerlidir). dd2 metriklerini aynı hatla tara. Deneme sayacı N = 1.861'den devam eder (`dipten_donus/DURUM.md` "01/10 ~15:10 Tarama 2b" kaydı).
3. Şampiyon V2 aşaması (aday metrikler, kombinasyon, ablasyon), terfi kuralı v2 + plasebo. Her terfi önerisinde V2 kararının yanında t, t*(N) (DD DURUM'daki gibi ≈ √(2 ln N); yalnız rapor, eşik değil), DSR de raporlanır (Bölüm 3 t ≥ 1,5 ile, Bölüm 5 aile eşiğiyle çalışır; bu farkı Ömer'e açıkla).
4. **Hisse hisse denetim** ve **kaçan kazananlar** (01 §C.9). Bulgu varsa ön kayıtlı deneme olarak simde test et, yoksa "çıkmadı" de.
5. **Site:** 2005–26 ve 2015–26 modelleri, Farklı Kaydet, en fazla 2 test, ETA + `send_later`. Sim–site sepet karşılaştırması: Ömer'in şartı ≥ %90 (≥ 235/261), hedef ≥ 260/261; sim iyimserliği.
6. Denetim: maliyet/kapasite (likidite kapısı uyarısı), 1 gün gecikme, DSR/PBO, korelasyon. Ardından rapor.

**Çıktı:** dd2_ 262/262 (disk), `ON_KAYIT_T1.md`, tarama raporları, `dipten_donus/DURUM.md`, 04'teki nihai kriter/model ID'leri (2005–26 ve 2015–26), `raporlar/KALIBRASYON.md`'de DD satırı. YOL_HARITASI'nın 8. adımı (PDF rapor, site adları, Ekim seçimi) için Ömer'e sor: tüm metrik çalışmasından önce mi, sonra mı?
**Bitti ölçütü:** Ömer Dipten Dönüş'ün nihai algoritmasını **kendisi** ilan etti; ID'ler 04'te; Python sim bu site modeliyle ≥ 260/261 (alt sınır 235).
**Ömer'e rapor:** her tur sonunda tablo + karar + sıradaki iş + ETA.

---

## Bölüm 4 — TÜM METRİK HASADI (BISTTUM, 2005–2026, her ay × her hisse)

**Amaç:** QueenStocks'taki bütün metrikleri hiçbirini atlamadan toplayıp diske koymak. Hasat üç strateji için **bir kez** yapılır.

### 4.1 Envanter
- Editördeki `#selFonk` listesinin **tamamını** JS ile oku (~480 fonksiyon). Ekle: sektör fonksiyonları; `araclar/METRIK_KATALOGU.md` ve LIT_A/B/C'de adı geçip taranmamış metrikler; `Teknik.Indicator("MetaStock ifadesi","d")` ile alınacak teknik ifadelerin **sonlu listesi** (ON_KAYIT_HASAT'a yazılır): RSI, MACD, Stoch, ROC, ATR, ADX, CCI, MFI, OBV, Bollinger genişliği, Mov, HHV/LLV, Stdev × 4.2'deki dönemler.
- Her fonksiyon için: ad, kategori, parametreler, dönüş tipi, temel/teknik, tarihsel hesaplanabilir mi, PIT sonucu (4.3), "mevcut" işareti (dd_, dd2_, u3_'te zaten var mı).
- **Sonuç görülmeden** doldurulacak sütunlar, **her strateji için ayrı** (DD / K10 / C32): **önsel gerekçe** (kaynak: DD için `dipten_donus/` LIT_A–D; K10 için `projeler/alfa_v41/` LITERATUR ve LIT2_A/B; C32 için `projeler/deger_v11/` LITERATUR ve PROTOKOL; ortak `METRIK_KATALOGU`; yoksa "yok") ve **beklenen yön** (+/−/bilinmiyor). Bir stratejinin literatür dosyası yoksa ya da zayıfsa, hasat sonuçları görülmeden önce o strateji için literatür taraması yap (Ömer'in döngüsünün ilk adımı; varsa `strateji-literatur-taramasi` becerisi). Bu dosyanın SHA-256'sı ON_KAYIT_HASAT'a yazılır. Aile A/B ayrımı (5.0) buradan gelir.
- **Hiçbiri sessizce atlanmaz:** dışarıda kalan her fonksiyonun gerekçesi yazılır (tarihsel hesaplanamıyor / hata veriyor / zamana göre değişmiyor / kaçak / başka metrikle birebir aynı).
- Çıktı: `projeler/tum_metrik/METRIK_ENVANTERI.csv`.

### 4.2 Türetme kuralları (ön kayıtlı, sonuç görmeden)
- **Editörden yalnız İLKEL alanlar çekilir:** her temel fonksiyonun düzeyi (0) ve yıllık gecikmesi (−4) ile paydalar (PD, aktif, özkaynak, satış). −1 ve −8 için pilotta "aylık düzey serisinden türetme" editör değeriyle karşılaştırılır; ≥ %99 eşleşirse Python'da türetilir, eşleşmezse editörden çekilir.
- Oranlar, farklar, ÷PD/÷aktif sürümleri ve yüzdelikler **Python'da** hesaplanır. Final adaylar için birebir formül editörden ayrıca alınır ve fark raporlanır.
- **Teknikler:** günlük kapanış ve hacim serisi (gerekirse yüksek/düşük) 2002–2026 için bir kez çekilir (~6.000 işlem günü × 2–3 parça; süreyi pilotta ölç). Göstergeler standart dönemlerle (20/50/200 gün, 1/3/6/12 ay) Python'da hesaplanır. Pilotta 20 tarih × hisse × 10 gösterge `Teknik.Indicator` değeriyle karşılaştırılır; ≥ %99 eşleşmeyen gösterge (düzeltilmiş fiyat, Wilder yumuşatması gibi) editörden çekilir.
- TL düzey metrikleri (PD, işlem hacmi, tutarlar) enflasyonla kayar: yalnız kesit içi sıra olarak ya da TÜFE'ye bölünmüş sürümleriyle kullanılır; sabit eşiğe yalnız ölçekten bağımsız oranlar çevrilir.
- Kurallar `ON_KAYIT_HASAT.md`'ye yazılır, **sonra** toplam metrik sayısı hesaplanır ve Ömer'e bildirilir.

### 4.3 Kaçak ve zaman noktası (PIT) denetimi
Site testi bu sızıntıyı ölçmez (site de aynı fonksiyonu kullanır); **tek koruma bu denetimdir.** Her fonksiyon için METRIK_ENVANTERI'ne `pit_test` sütunu:
- Her metrik "Yayınlanma Tarihine Göre" ve **sıralama tarihi = önceki ayın son işlem günü** (`a41dates`) ile alınır.
- **(T1) Zaman değişkenliği:** 10 hisse için 2006, 2012, 2020 ve 2025'te değerlendir. Hiçbirinde değişmiyorsa "zamana göre değişmiyor" → madencilikten çıkar. Hisselerin %80'inden fazlasında 2005–2026 boyunca hiç değişmiyorsa "bugünkü değer olabilir → şüpheli". Pay sayısı, halka açıklık, sektör, pazar/endeks ve işlem yaşı fonksiyonlarını özellikle denetle.
- **(T2) Yayın sınırı:** KAP yayın tarihi bilinen 10 şirket-dönem için yayından 1–2 iş günü önce ve sonra sorgula. Yeni dönemin değeri yayından önce görünüyorsa "kaçak".
- **(T3) Revizyon:** 2023/9 dönem değerini 12/2023 tarihinde sorgula, KAP'ta ilk yayımlanan (TMS 29 öncesi) rakamla karşılaştır; fark varsa geçmiş yeniden yazılmış → şüpheli.
- **(T4)** Sıralama tarihinden sonraki dönemi isteyen parametreler (+1 vb.) reddedilir.
- "Şüpheli" metrikler taranabilir ama süzgeci geçse bile terfi edemez ve siteye gitmez. Süzgeç-1'de en yüksek t'li ilk 20 aday ayrıca elle PIT kontrolünden geçer.
- **TMS 29:** −1/−4/−8 karşılaştırması 2023/12–2024/9 geçişini kesen temel türevler "TMS-kırılma" etiketi alır (platform 2024+ karşılaştırmalı tutarları reel saklıyor, 07 §4).

### 4.4 Pilot, süre, hız sınırı ve katmanlar
- **Pilot iki parçalı:** (a) hata taraması: 1 tarih × 1 parça (≤175 hisse) × envanterdeki TÜM fonksiyonlar (HATA, boş ya da sabit dönenleri ayır; T1 ile birlikte). (b) hız ve hassasiyet: 3 ay (2005, 2015, 2025'ten birer ay) × ~40 fonksiyon. Ölç: formül-ay başına sekme-saniye; dönen ondalık basamak sayısı (küçük değerli metrikleri ×10.000 ölçekleyip karşılaştır); paketleme kaybı. Bit maskeleri **asla** yuvarlanmaz; binlik ayracı temizle (G1).
- Her ay yalnız **o ayın üyeleri** sorgulanır (208552 üyeleri ∩ `lstHisse`; dd_need ort. 378 → ayda 2–3 parça), tam lstHisse değil. Envanterde "mevcut" işaretli alanlar yeniden çekilmez (pilotta 1 ayda eşitliği doğrula). Paket şablonu: `dd_` yöntemi (F1–F11).
- **ETA** = ay × formül × parça × saniye / sekme; Ömer'e **gün** olarak bildir. Toplam 72 saati aşıyorsa katmanla; her katmanın saat tahmini ve bitiş tarihi ayrı yazılır:
  - **Öncelik-1:** bütün temel fonksiyonlar, düzey + yıllık gecikme · **Öncelik-2:** günlük fiyat/hacim serisi ve editörden çekilmesi gereken teknikler · **Öncelik-3:** kalan varyantlar.
- **Deneme bütçesi:** hasattan önce TÜM katmanların toplam deneme bütçesi (N_plan) hesaplanır ve ön kayda yazılır; eşikler baştan N_plan ile hesaplanır. Bir katmandan vazgeçilirse N_plan düşürülmez. Öncelik-1 gelince Süzgeç-1 elemesi başlayabilir, ama **hiçbir ekleme (5.6) ve kasa işlemi**, o strateji için planlanan tüm katmanlar toplanıp elemeden geçmeden yapılmaz. Ömer beklemek istemezse, kasadan sonra gelen katmanların adayları "kasa kullanıldı" etiketi alır ve canlı ileri izlemeye bırakılır.
- **Hız sınırı ve hesap güvenliği:** toplam en fazla 4 sekme; site testi koşarken 2'ye iner. Sekme başına istekler arası en az X saniye (X pilotta ölçülür, ön kayda yazılır); toplam hız pilot hızının %80'iyle sınırlı. Ardışık 3 hata, 500 yanıtı ya da yanıt süresi pilot ortalamasının 3 katını aşarsa: o sekme önce 10 dk, sonra iki katına çıkarak en çok 1 saat bekler. 10 dakikada 10 hata, Login.aspx, captcha/uyarı ya da beklenmeyen sayfa görülürse bütün işçiler durur (`tm_pause`), durum `ilerleme.json`'a yazılır ve Ömer'e haber verilir. Günlük istek sayısı, hata oranı ve ortalama yanıt süresi DURUM'a yazılır.
- **Paralel plan** (DURUM'a yaz): Ömer onaylarsa hasat Öncelik-1, ön ölçüm biter bitmez geceleri başlar; Python ve DD sim işleri gündüz paralel yürür.

### 4.5 Gözetimsiz çalışma (iş defteri)
- **İş defteri:** IDB `tm_queue` + diskte `veri/manifest/kuyruk.csv`. Görev = (katman, formül no, ay, parça); durum bekliyor/alındı/bitti/hata, deneme sayısı, saat. Sekmeler sabit ay aralığı değil, kuyruktan görev çeker (IDB transaction kilidiyle). 15 dakikadan eski "alındı" görevler kuyruğa geri bırakılır.
- **Görev ancak şu doğrulamalardan sonra "bitti" olur:** (1) dönen hisse sayısı = istenen; (2) yanıtta Login.aspx/pageRedirect yok; (3) "HATA" yok ya da hisse bazında kaydedildi; (4) parçanın tamamı null değil. Aynı parça 3 kez hata verirse ikiye bölünür (175 → 88).
- **Kalp atışı:** her işçi `window.__tmRun` bayrağı tutar ve IDB'ye `tm_hb_<sekme>` zaman damgası yazar. İşçiler her 10 dakikada diske `veri/manifest/ilerleme.json` yazar (biten görev, `disk_bekleyen`, hata sayısı, son yanıt saati).
- **Kontrol:** `send_later` ile; tarayıcıya girmeden önce yalnız `ilerleme.json` tek çağrıda okunur. Sıklık gündüz 2–3 saatte bir, gece en çok 1 kez. Son yanıt 30 dakikadan eskiyse tarayıcıya girilir ve Bölüm 8.5 kurtarma sırası uygulanır.
- Oturum düşerse borfin yönlendirmesini dene; açılmazsa **dur**, Ömer'e haber ver; şifre girme.
- Hasat izlemesi için her gün yeni ve kısa bir sohbet açılır (devam cümlesiyle, Bölüm 8.4).

### 4.6 Evren, getiri, hayaletler ve eksik veri
- Evren ve getiri: BISTTUM üyelik modeli 208552'nin site getirileri.
- **Hayaletlerin** (bugün işlem görmeyen hisseler, üye-ayların ~%5,8'i) metrikleri editörden alınamaz. Kapsamayı ay ay raporla; hayaletleri site sırasıyla havuzda tut.
- **HAYALET VE EKSİK VERİ KURALI (ön kayıt):** yeni metrik, hayalette ve o ay verisi olmayan hissede **NÖTR** sayılır: kapıda "geçer" (şampiyondaki durumu korunur), bonus ve cezada 0, ağırlıklı bileşende o ayın kesit medyanı. G3 null davranışı (karşılaştırma=false) madencilikte **kullanılmaz**; yalnız siteye gidecek formülün sim kopyasında taklit edilir ve aradaki fark raporlanır. Her aday için: şampiyona göre değişen hisse-ayların kaçı hayalet ya da verisiz. "Veri var mı" göstergesinin kendisi sinyal olarak kullanılamaz (ön kayıtta ayrı hipotez olarak yazıldıysa istisna).

### 4.7 Kalite kontrolü ve işlenmiş veri
- Metrik başına eksik veri oranı, uç değerler, null davranışı (G3; `null−1 = −1`), alfabetik sonuç sözlüğü eşlemesi.
- **Her paket formülü için** en az 1 rastgele tarih × hisse, paketsiz tek alanlık editör testiyle karşılaştırılır (tek hisselik postback ~5 sn; 500 paket ≈ 45 dk). Ayrıca her katmandan 2005, 2015 ve 2025'ten birer ay tam karşılaştırılır.
- **Tutarlılık:** hasat bitince ilk hafta çekilen aylardan rastgele 3 ay × 50 paket yeniden çekilip karşılaştırılır (platform 2024+ tutarları reel yeniden saklıyor, yeni bilançolar geliyor). Farkı %1'i aşan ailelerde 2024+ ayları yeniden çekilir.
- **İşlenmiş veri uzun tablo değildir:** aile başına sütunlu Parquet (`veri/islenmis/tm/aile=<aile>/part.parquet`; satır = ay × hisse, sütun = metrik, float32) ya da metrik başına .npy; ay ve hisse dizinleri ayrı dosyada. Python yalnız gereken sütunları okur.
- Uç değer kırpma sınırları, z-skor/ECDF tabloları ve ölçekleme **yalnız 2005–2020** verisiyle hesaplanır ve ön kayda dondurulur (kasa dağılım yoluyla da sızmasın).

**Çıktı:** `METRIK_ENVANTERI.csv`, `ON_KAYIT_HASAT.md`, `veri/ham/tm_*`, `veri/islenmis/tm/`, `raporlar/HASAT_KALITE.md`.
**Bitti ölçütü:** envanterdeki her metrik ya toplandı ya gerekçeli olarak dışarıda; manifest %100; kalite kontrolü geçti.
**Ömer'e rapor:** "N fonksiyon → M metrik toplandı, K dışarıda (gerekçeli), kapsama %X, süre Y gün, disk Z GB."

---

## Bölüm 5 — MADENCİLİK (tam tarama, sıkı süzgeç), her strateji için ayrı

Sıra: Dipten Dönüş (nihai) → Büyüme K10 → Değer C32 (Bölüm 0, soru 1'deki cevaba göre). Her strateji Bölüm 5.8'deki sırayla tamamlanır.

### 5.0 Ön kayıt (sonuç görmeden)
`projeler/tum_metrik/ON_KAYIT_TUM_METRIK_<strateji>.md`. Zorunlu maddeler:
- Veri bölümü, roller, eşik düzeyleri ve plato komşuları, ekleme sınırı, durdurma kuralı, turda "en iyi aday" sıralama ölçütü (2005–2020 NW t), kasa kabul kuralı (5.6).
- **Aileler:** Aile A = önsel gerekçesi ve beklenen yönü envanterde yazılı metrik×rol kombinasyonları (≲100); Aile B = geri kalan her şey. Hata bütçesi: A %4, B %1; testler tek yönlü (yön A'da envanterden, B'de eğitim döneminde bulunan yön).
- **N tanımları:** ham N ve N_etkin (aynı metrik-rolün eşik komşuları ve iki yönü tek aile; deneme fark serileri arasında |ρ| > %90 olanlar tek kümede). N_plan (4.4). K10 ve C32 için başlangıç sayacı geçmiş deneme sayısıdır: C32 ≈ 5.800 (05/Deger_BISTTUM); K10'un sayısı 05'te yazılı değil (yalnız "29 deneme" gibi parçalar var) → `projeler/alfa_v41/DURUM.md`'den say, bulunamazsa ihtiyatlı bir üst tahmin kullan ve "tahmin" diye yaz. DD için 1.861 + Bölüm 3.
- **Güç tablosu:** şampiyonun fark serisi oynaklığıyla, seçilen eşiklerde %50 güçle yakalanabilecek en küçük yıllık fark (MDE, puan/yıl) A ve B için. Taramadan ÖNCE Ömer'e: "Bu tasarım yılda ≈ +X puanın altındaki gerçek iyileşmeleri göremez." B için MDE gerçekçi değilse (> 15 puan/yıl), B'nin karar testi sonuç görülmeden BH-FDR'ye (q %10) çevrilir.
- Sahte metrik sayısı ve türleri, ML ayarları (tek hedef, sabit hiperparametreler), NW gecikmesi = 6.
- Sonradan değişiklik olursa tarih-saatle "ön kayıt değişikliği" eklenir; o noktadan sonraki bulgular "keşif" sayılır.

### 5.1 Veri bölümü ve kasa
- **Eğitim** 2005–2015 · **Doğrulama** 2016–2020 · **Kilitli kasa** 2021–2026. Kasa getirileri ve kasa dönemi metrik dağılımı (kırpma sınırları, ECDF, kümeleme, ML ölçeklemesi, yüzdelikten sabit eşiğe çeviri) **hiçbir hesapta** kullanılmaz; teknik kilit Bölüm 2A.1. Kasa strateji başına **bir kez** açılır; açılış `KASA_ACILIS.csv`'ye tarih-saatle yazılır, ikinci açılış olamaz.
- Sabit eşik / ECDF çevirisi (ZSkorPercentRank sitede çöküş yaşatıyor, 03 §7) **kasa açılmadan** yapılır; kasa siteye gidecek sabit eşikli sürümü sınar.
- **Ömer'e açıkla:** "Senin V2'n iki yarıya bakar. Bu ek kilit, binlerce denemede gerçekten dokunulmamış bir dönem bırakmak içindir. En sonda tam Şampiyon V2 yine 2005–2026 üzerinde uygulanır."
- **Kasada önceden görülmüş listesi** (strateji başına): dd ve dd2 alanları (01/10 taramasında tam dönemle görüldü; Tarama 2b'de 2021–26 ayrıca açıldı), Bölüm 3 adayları, 05_PROJE_GECMISI'ndeki K10/C32 denemelerinin metrikleri, METRIK_KATALOGU'nda tam dönem sonucu yazılı olanlar ve |ρ| > %90 aile üyeleri. Bunlar taranır, ama kasa sonuçları "bağımsız onay" sayılmaz; raporda ayrı tabloda verilir, terfileri için canlı ileri izleme ya da Ömer'in açık kararı gerekir.

### 5.2 Negatif kontrol (sahte metrikler)
- **Üretim:** (1) kimlik permütasyonu: her sahte için hisse → metrik serisi eşlemesi tüm dönem boyunca tek bir rastgele permütasyonla değiştirilir (kalıcılık korunur); (2) zaman kaydırma: gerçek seri hisse içinde ≥ 36 ay dairesel kaydırılır; (3) AR(1) rastgele seri, kalıcılığı gerçek metriklerin medyanına eşit. **En az 200 sahte**; adları gerçeklerle aynı biçimde gizli kod; sahteler ML'e de girer.
- Eşleme `projeler/tum_metrik/gizli/sahte_anahtar.csv`'de; tarama kodu bu dosyayı **okumaz**.
- **Kullanım:** (a) global test: her aşamada "eğitim t > 2 olan gerçek metrik oranı" sahtelerdeki oranla karşılaştırılır; fark yoksa "havuzda sinyal yok" denir. (b) ampirik sıfır dağılımı: Süzgeç-1 eleme eşiği = max(ön kayıtlı eşik, sahte t'lerin %99'luk dilimi). Bu kural mekaniktir ve önceden yazılır; sonuçlara bakıp eşik değiştirilmez. Süzgeç kararları **betikle otomatik** verilir; listeyi elle düzenleme.

### 5.3 Tarama hattı (hepsi şampiyonun ÜSTÜNE, 5 hisselik birebir portföy simiyle)
Havuz IC'si yalnız eler; karar her zaman 5 hisselik portföy simindedir.
- **(a) Korelasyon kümelemesi (önce):** korelasyonu %90'ın üstünde olan metrikler aile sayılır (yalnız 2005–2020 verisiyle). Temsilci **sonuç görülmeden** seçilir (en yüksek kapsama, eşitse en sade formül) ve ön kayda yazılır. Diğer üyeler atılmaz: envanterde "X ailesi, temsilci Y, korelasyon %9x" notuyla kalır ve IC'de ölçülür. Temsilci Süzgeç-1'i geçerse ailenin diğer üyeleri de aynı rollerle denenir ve sayaca eklenir.
- **(b) IC elemesi:** eğitim döneminde sıra-IC, şampiyonun aday havuzunda (havuz < 30 hisseyse evren genelinde); iki alt yarıda aynı işaret; eşik aile sayısına göre √(2 ln N_aile). IC karar vermez, yalnız eler.
- **(c) Metrik × rol** (yalnız IC'yi geçen ailelerde): kapı (alt/üst %20/%40/%60/%80), sıralama bileşeni (ağırlık), bonus, ceza × 2 yön × 3–5 eşik (plato komşuları). Ay içi yüzdelik eşikler aramada kullanılabilir; çeviri 5.1'e göre.
- **(d) İkili kombinasyon:** yalnız elemeyi geçenlerde; sayaca denenen çift sayısı değil **C(n_elemeye_giren, 2)** eklenir. Kombinasyonlar eğitimde üretilir, yalnız Süzgeç-2'de karara bağlanır.
- **Deneme sayacı:** her deneme bir `deneme_id` alır. `DENEME_SAYACI.csv` sütunları: deneme_id, zaman, ön kayıt sürümü, strateji, metrik, aile (A/B), rol, parametre JSON'u, eğitim t, alt yarılar, doğrulama t, sonuç. Aylık fark serisi (kasa açılmadan önce yalnız 2005–2020, 192 ay, float32) `veri/denemeler/<strateji>/tur_<k>.npy`'ye yazılır (satır = deneme_id). 200 bin deneme ≈ 150 MB.

### 5.4 Makine öğrenmesi (fikir kaynağı)
- **Veri:** yalnız eğitim dönemi. Satırlar: her ayın şampiyon havuzunun TÜMÜ (o ayın üyeleri, ~250–450 hisse → ~40–50 bin satır); şampiyon sırası bir özellik olarak eklenir. Şampiyon havuzunun ilk 30–50'si ayrı bir değerlendirme kesiti olarak raporlanır.
- **Hedef (tek):** sonraki ayın ay içi getiri sırası (yüzdelik).
- **Özellikler:** 5.3(a) aile temsilcileri (aile içinden en fazla 2 üye daha; toplam ≤ 300–400) + sahte metrikler (gölge özellik). Eksik değer nötr doldurulur; eksiklik göstergesi özellik olarak verilmez.
- **Model:** gradyan artırma (LightGBM ya da sklearn HistGradientBoosting); hiperparametreler ön kayıtta sabit. Ayar gerekirse yalnız eğitim içinde iç zaman serisi doğrulamasıyla (ör. 2005–2012 eğitim, 2013–2015 erken durdurma); doğrulama ve kasa kullanılmaz. Genişleyen pencere: ilk eğitim 2005–2007 (36 ay), örnek dışı tahminler 2008–2015 (96 ay), model yıllık yeniden eğitilir; her ay için yalnız getirisi o aydan **önce** gerçekleşmiş etiketler kullanılır (1 ay ambargo).
- **Önem:** permütasyon önemi (aile bazında gruplanmış) ve SHAP, yalnız ileri yürüyen **örnek dışı** tahminlerden; etkileşimler ve kısmi bağımlılık (`raporlar/ML_<strateji>.md`). Bir özellik "fikir" sayılır ancak: önemi sahtelerin %95'lik diliminin üstünde, örnek dışı dönemin iki yarısında (2008–2011 / 2012–2015) ayrı ayrı ilk 20'de ve 5 farklı tohumda ilk 20'ye en az 4 kez giriyorsa.
- **Sade kurala çeviri:** her fikir tek eşik, tek bonus ya da tek ceza biçiminde yazılır, "ML kaynaklı" etiketi taşır. **ML kuralları Süzgeç-1'i atlar** (eğitim onların eğitim verisidir); doğrudan Süzgeç-2'ye girer ve yalnız **2016–2020**'de, ML fikir sayısı üzerinde Holm düzeltmesiyle, fark > 0 şartıyla sınanır. Deneme sayacına tüm özellik sayısı kadar katkı yapar.
- **ML modelinin kendisi şampiyon olmaz, siteye gitmez.** (Katılım Aşama 9'daki "öğrenen sıralama"da terfi çıkmamıştı: `OTURUM_GUNLUGU.md` 01/10 09:20 satırı; ayrıntı `projeler/buyume_katilim/DURUM.md`.)

### 5.5 Süzgeç (Süzgeç-1, 2, 3, 5, 6 eleme şartıdır; Süzgeç-4 yalnız etikettir)
- **Süzgeç-1, eleme (eğitim 2005–2015):** iki alt yarıda fark > 0 ve eğitim NW t ≥ 1,5 (Aile A) / ≥ 2,0 (Aile B), ayrıca ≥ sahte t'lerin %99'luk dilimi. Turda en çok 30 aday eğitim t sırasıyla Süzgeç-2'ye geçer.
- **Süzgeç-2, karar testi:** 2005–2020 birleşik NW t ≥ t*(aile) **ve** doğrulama 2016–2020 farkı > 0 (aynı yön). t* = tek yönlü Bonferroni eşiği Φ⁻¹(1 − α_aile / N_etkin_aile): N_A ≈ 30–100 için ≈ 3,0–3,4 (V2'deki "çoklu test sonrası güçlü ≈ 2,8" ile aynı mertebe); N_B ≈ 10⁴ için ≈ 4,8. √(2 ln N) ve E[max Z_N] yalnız "şanstan beklenen en iyi" olarak raporlanır, eşik değildir. Holm aile bazlı hatayı (FWER), BH yanlış keşif oranını (FDR) denetler; BH seçildiyse Ömer'e "geçenlerin ~%10'u şans olabilir" diye açıklanır.
- **Süzgeç-3, V2'nin diğer maddeleri** (2005–2020 üzerinde): son sermaye, kazandıran ay, Sharpe, kriz, en iyi 5 ay çıkınca, plato, <5 hisseli ay, plasebo, temiz mod, maliyet, farkın yıllara dağılımı. Ek: fark serisi, hayalet ya da verisiz hissenin **değişmediği** aylar alt kümesinde de > 0 olmalı.
- **Süzgeç-4, etiket (eleme değil):** Ömer'in amacı literatürde olmayan ama anlamlı metrikleri bulmaktır; literatür karşılığı olmayan aday elenmez. Etiket envanterden **mekanik** gelir: "literatür destekli" = önsel gerekçesi olan ve bulunan yönü beklenen yönle aynı olan aday; diğer tümü "yalnız veri kaynaklı / keşif" (ileriye dönük fark yarıya indirilir, bir ekonomik yorum denemesi yazılır). Sonradan bulunan gerekçe raporda "sonradan yorum" başlığıyla yazılır ve etiketi değiştirmez.
- **Süzgeç-5, kasa:** 5.6'daki tek açılış.
- **Süzgeç-6, tam dönem Şampiyon V2:** 2005–2026 üzerinde, 01 §C.4'ün tam hali ve strateji ekleriyle; yalnız kasada kabul edilen önek için geçti/kaldı kapısıdır. DSR ≥ 0,95 ve PBO ≤ 0,25 yalnız Dipten Dönüş'te bağlayıcıdır (ON_KAYIT_TABAN); K10 ve C32'de V2'nin dediği gibi raporlanır. Sahte metrik ve komşu sıra testleri kalibrasyon ve rapor içindir, kendiliğinden eleme şartı değildir.

### 5.6 Adım adım ekleme ve tek kasa açılışı
- **Aday zinciri (kasa kapalıyken):** her turda Süzgeç-1–4'ü geçenlerden ön kayıtlı ölçüte göre (2005–2020 NW t) en iyi tek aday **aday zincirine** (sim tabanı) eklenir. Bu şampiyon ilanı değildir. Tarama yeni taban üzerinde yalnız 2005–2020 ile tekrarlanır. En fazla 3–4 ekleme; geçen kalmayınca durulur. "En iyi aday" tam dönem verisiyle **seçilmez**. Formül sadeliği ve site test süresi gözetilir.
- **Her eklemeden önce:** adayın metriğini editörde kontrol et (en az 50 tarih × hisse, sim = editör). Yeni zincir adımının **2005–2020 tarih aralıklı** bir kalibrasyon modelini sitede çalıştır (01/01/2005–31/12/2020; Ömer'e önceden "kalibrasyon testi" de; kasa dönemi görülmez) ve sepet eşleşmesini doğrula (hedef ≥ 191/192, alt sınır %90 = 173/192). Sim iyimserliğini ekleme başına raporla.
- **Kasa dizisi:** turlar bitince ön kayda kilitli dizi yazılır: Ş0 → Ş0+m1 → Ş0+m1+m2 → … Kasa **tek seferde** açılır ve dizinin tamamı ölçülür. **Kabul kuralı** (önceden yazılı): her eklemenin kasa farkı > 0, kasa NW t ≥ 1,0, ve 2021–2023 alt diliminde de fark > 0 olan en uzun önek kabul edilir; kasada yönü eksi olan adım ve sonrakiler düşer, yerine yeni aday aranmaz. Kasa kararı 2021–2023 ve 2024–2026 alt dilimlerinde ayrı raporlanır; yalnız 2024–26 sayesinde olumlu çıkan aday "TMS şüpheli" etiketi alır ve terfi edemez. Kasa sonucu sırayı değiştirmez, yalnız kabul/red verir.
- Kasa açıldıktan sonra yeni tur yapılırsa sonuçları "kasa yok — keşif" etiketi taşır ve yalnız canlı ileri izlemeye alınabilir.

### 5.7 Final istatistikler
- **DSR:** V[SR] ve N_etkin 2005–2020 deneme matrisinden; final aday için önce 2005–2020'de, kasa açıldıktan sonra tam dönemde raporlanır (bu rapor karar değiştirmez). **PBO/CSCV:** turun TÜM adaylarıyla (yalnız geçenlerle değil, en çok ~1.000 aday ailesi), S = 10, 2005–2020 üzerinde (≤ 0,25 kabul, 0,25–0,50 şüpheli, > 0,50 aşırı uyum).
- Bağımsız doğrulama `araclar/b100/cmp.py` (HAC t, blok bootstrap, Sharpe farkı bootstrap, DSR, PBO). Ek (LIT_D): komşu sıra (6–10. sıradaki 5'li de tabanı geçmeli), sıra kovalarında monotonluk.
- Final şampiyonun örnek içi farkı raporda "ileri seçimle şişmiş" notuyla verilir; tek güvenilir ölçü kasa (bir kez) ve canlı ileri izlemedir.

### 5.8 Her strateji için zorunlu sıra
5.0 ön kayıt → 5.3–5.4 tarama ve ML (2005–2020) → **Bölüm 6-A** (mevcut şampiyonun 2005–2020 seçimleri ve kazananları; fikirler ön kayda girer) → Süzgeç-1–4 → 5.6 zincir → Süzgeç-5 kasa (bir kez; 5'in ve 6-A'nın finalistleri birlikte) → Süzgeç-6 → **Bölüm 7** site (tam dönem site testleri yalnız kasa açıldıktan sonra) → **Bölüm 6-B** → Ömer'in kararı → sıradaki strateji.

**Çıktı:** `ON_KAYIT_TUM_METRIK_<strateji>.md`, `DENEME_SAYACI.csv`, `veri/denemeler/`, `KASA_ACILIS.csv`, `raporlar/TARAMA_<strateji>.md`, `ML_<strateji>.md`, `SUZGEC_<strateji>.md` (her aşamada kaç gerçek ve kaç sahte geçti).
**Bitti ölçütü:** strateji için ya 1–4 eklemeli bir aday zinciri kasadan geçti ya da gerekçeli "geçen yok" kararı var.
**Ömer'e rapor:** tablo (aday | aile | rol | eğitim t | doğrulama | 2005–20 t / t* | kasa | V2 | etiket); ayrı tablolar: **getiriyi artırıp elenenler**, **"V2'yi geçen ama yalnız yeni süzgeçlere takılanlar"** (kasa açıldıktan sonra her aday için tam dönem V2: aday | rol | V2 madde madde | takıldığı yeni şart | fark puan/yıl | t; Ömer bu tabloya bakarak kararı değiştirebilir), "kasada önceden görülmüş" adaylar; sahte metrik sonucu, ham N, N_etkin, t*.

---

## Bölüm 6 — Hisse hisse denetim ve kaçan kazananlar (mevcut şampiyon + varsa aday zinciri)

**Amaç:** Ömer'in döngüsünü tüm metrik verisiyle uygulamak. Bölüm 5'te aday çıksa da çıkmasa da her stratejide **mevcut şampiyonun** seçimleri üzerinde yapılır; aday zinciri varsa aynı denetim onun için tekrarlanır ve iki sonuç yan yana verilir.

**Zamanlama:**
- **6-A (kasa açılmadan, tercih edilen):** yalnız 2005–2020 seçimleri ve yıllık kazananlarıyla. 2021–2026 seçimlerine ve kazananlarına **bakma**. Fikirler ön kayda yazılır; kaçan kazananlardan türetilen eşik türetildiği yıllarda değil öbür dönemde sınanır (2005–2015'te üret, 2016–2020'de sına ya da tersi; LIT_D). Sonra kasa dizisine (5.6) normal aday olarak girer.
- **6-B (kasa ve site sonrası):** nihai aday ve şampiyon için 2005–2026 tam denetim + kaçan kazananlar raporu (01 §C.9). Buradan çıkan her fikir "keşif — kasa yok" etiketi alır, farkı yarıya indirilerek raporlanır, yalnız canlı ileri izlemeye alınır; kasa ikinci kez kullanılmaz.

**Yapılacaklar:**
1. **Otomatik bayraklar** (hasat verisinden): tek seferlik kâr (|ΔNetKâr| ≫ |ΔFAVÖK|), negatif özkaynak + ROE tuzağı, NetBorç/FAVÖK aşırı, HA < %15, TMS 29 sıçraması, manipülasyon belirtisi (tavan serisi + düşük hacim vb.). Elle inceleme yalnız bayraklı hisse-aylar ile en çok kazandıran ve kaybettiren 50 hisse-ay için. Rapora bayrak türüne göre ~1.305 hisse-ayın dağılımı yazılır. Değer'in "kaçak kataloğu v2" dersini hatırla: kaçak sanılanlar bazen getiri kaynağıydı.
2. Bulgu varsa onu eleyen bir kapı ya da sıralama eki tasarla: ön kayıt → sim → Bölüm 5 süzgeci. Anlamlı değilse "çıkmadı".
3. **Kaçan kazananlar** (01 §C.9, `code_kzwin` → Python): her yılın ilk 30 ve ilk 50'si **208552 site getirilerinden (hayaletler dahil)** kurulur, u3 kapanışlarından değil. Alınanlar için kaç ay alındığı ve o aylardaki getiri; alınmayanlar için neden: (a) kapıda kaldı — hangi kapılar, kaç ay; (b) sıralamada 6. ve sonrası — en iyi sırası; (c) verisi yok / evrende değil. Özet: kapı başına "kaçan kazananlarda kalma oranı / evren ortalaması".
4. Tüm metrik verisiyle: kaçan kazananları ayıran bir metrik var mı? Varsa aynı süzgeçten geçer ve sayaca eklenir; doğrudan kural değişikliği değildir.

**Çıktı:** `raporlar/DENETIM_<strateji>.md`, `raporlar/KACAN_KAZANANLAR_<strateji>.md`.
**Bitti ölçütü:** her yıl ve her kaçış nedeni için tablo var; her bulgu ya test edildi ya gerekçeyle bırakıldı.
**Ömer'e rapor:** kısa tablo + "şu çıktı / çıkmadı" + karar önerisi.

---

## Bölüm 7 — Site testi

**Amaç:** simde süzgeci geçen adayların sitede uygulanabilir sürümünün simle aynı davrandığını doğrulamak. **Site testi bağımsız kanıt değildir** (aynı 2005–2026 geçmişini kullanır), simin doğruluğunu ölçer. Bağımsız kanıt yalnız kasa (bir kez) ve **canlı ileri izlemedir**.

**Yapılacaklar:**
1. Siteye yalnız simde süzgeci geçenler gider (ve Ömer'in "V2 geçti – şans süzgeci geçmedi" tablosundan seçtikleri, "zayıf/keşif" etiketiyle).
2. **Editör doğrulaması:** kriteri editörde kur, birkaç tarih × hisse için sim skoru = site skoru. **Farklı Kaydet**; adlandırma 01 §F ve 04 kurallarına uyar; yeni ID'yi **hemen** 04'e yaz.
3. 2005–26 ve 2015–26 modellerini kur (03 §4–5). **En fazla 2 test** (bütün çalışan testler sayılır). ETA + `send_later`.
4. Sonuçları `__readSite` ile oku (`siteres_ID`), diske de yaz. **Sim–site:** ay ay sepet karşılaştır; Ömer'in şartı ≥ %90 (≥ 235/261), hedef ≥ 260/261; sim/site sermaye oranı. %90'ın altındaysa adayın sim sonucu güvenilmez sayılır: farkları sınıfla (hayalet, eşit puan, kapı farkı, ECDF düğümü, veri eksiği), sim kopyasını düzelt; aday kararı site sonucuna göre verilir; fark aynı aileden sonraki adaylar için DURUM'a not edilir. **Sim iyimserliğini** raporla (Değer BIST100'de −%0,7 ile −%11).
5. Formül karmaşıklığının site test süresine etkisini raporla.
6. Terfi kararı Ömer'indir. Zayıf adayda (1 ≤ t < 1,5) site farkı da V2'yi geçmeden terfi önerme.
7. **Canlı ileri izleme:** 10/2026'dan başlayarak her ay şampiyonun ve terfi adayının kağıt portföyü `projeler/tum_metrik/CANLI_IZLEME.csv`'ye yazılır. Terfi kararında kaç aylık canlı veri olduğu belirtilir.
8. **Ömer yeni şampiyon ilan ederse:** 01 §F adlandırmasıyla yeni kriter ve 2005–26 / 2015–26 yayın modelleri Farklı Kaydet ile oluşturulur, ID'ler hemen 04'e. Eski yayın kopyaları Ömer karar verene kadar korunur (Silinecekler'e yalnız öneri). 05_PROJE_GECMISI ve ilgili strateji PDF raporu (`araclar/rapor/` hattı) güncellenir; canlı takip ve sonraki ay seçimi yeni şampiyonla yapılır. K10 ya da C32 değiştiyse "Büyüme + Ortak" 2 pay kuralına etkisi (ortak hisse sayısı, geçmiş sonuç) Ömer'e tabloyla bildirilir.

**Çıktı:** `raporlar/SITE_<strateji>.md`, güncel 04, `CANLI_IZLEME.csv`.
**Bitti ölçütü:** her finalistin site sonucu ve V2 değerlendirmesi hazır; Ömer kararını verdi.
**Ömer'e rapor:** yan yana tablo (şampiyon | aday | fark): sermaye, kazandıran ay, Sharpe, MDD, kriz, 2005–15 / 2016–26 / 2015+, en iyi 5 ay çıkınca, sim–site aynı sepet.

---

## Bölüm 8 — Raporlama, kayıt, devam ve kurtarma

### 8.1 Her aşama sonunda Ömer'e
Kısa tablo + karar + sıradaki iş + ETA. "Getiriyi artırıp elenenler" ve "V2'yi geçip yeni süzgeçlere takılanlar" ayrı tablolarda. Elenen her aday "simülasyon testi sonrası kurala göre elendi" + takıldığı şartla bildirilir. Anlamsız olan "anlamsız" diye söylenir. Sahte metrik sonuçları raporlanır.

### 8.2 Her sohbette zorunlu kayıtlar (00 §5)
- `projeler/tum_metrik/DURUM.md` tarih-saatli kayıt; `YOL_HARITASI.md` ve `02_SIRADAKI_ISLER.md` güncel; yeni ID hemen 04'e; `OTURUM_GUNLUGU.md`'ye satır; `05_PROJE_GECMISI/` güncel.
- Hafıza çift kaydı + `SON_SENKRON.txt`. Hafızaya yalnız kalıcı kararlar gider; formül, ID ve sonuç proje dosyalarında.
- Betikler `araclar/` altına, veri manifesti güncel.
- **Klasör kendi kendine yeterli kalsın:** 00 §3 klasör yapısına yeni klasörleri (`veri/`, `projeler/tum_metrik/`, `araclar/sim_py/`, `araclar/kurulum/`), 00 §6'ya "sim kodları ve veri artık diskte: `araclar/sim_kodlari`, `veri/`; geri yükleme `araclar/kurulum/idb_geri_yukle.js`" notunu ekle. Ömer'e göstererek: 01 §C'ye "C.10 Tüm metrik süzgeci", §C.6a'ya "%90 alt sınır (≥ 235/261)", 07'ye "disk asıl kaynak" ve "Chrome/IDB düşerse" bölümlerini yaz.

### 8.3 Final: "Tüm Metrik Madenciliği Raporu"
Dosya: `projeler/tum_metrik/raporlar/TUM_METRIK_RAPORU.md`. Her strateji için ayrı bölüm:
- kaç fonksiyon / kaç metrik toplandı, kaçı gerekçeyle dışarıda (PIT dahil), kapsama
- ham N, N_etkin, t*(A), t*(B), MDE; her süzgeçte kaç gerçek / kaç sahte geçti
- ML fikirleri ve sade kural sonuçları
- eklenenler ve tek tek etkileri, kasa sonucu (açılış sayısı = 1, 2021–23 / 2024–26), DSR, PBO
- site sonucu, sim–site aynı sepet, sim iyimserliği
- "V2'yi geçip yalnız yeni süzgeçlere takılanlar" tablosu; "kasada önceden görülmüş" tablo
- dürüst beklenti: canlıda Sharpe kabaca testtekinin yarısı ile üçte ikisi arasında beklenir (LIT_D kaba kuralı); taramayla bulunan ek iyileşmede düşüş daha büyük olabilir; "keşif" etiketli farklar yarıya indirilerek verilir (01 §C.3)
- "literatürde olmayan" bulgular ayrı listelenir, ekonomik yorum denemesiyle ("sonradan yorum")

### 8.4 Uzun sohbet ve devam
- Uzun sohbetlerde tarayıcı işlemleri güvenlik kontrolüyle engellenebiliyor (03 §7). Her bölüm sonunda bütün dosyaları güncelle ve Ömer'e bir "devam cümlesi" ver: *"QueenStocks Projesi klasörünü bağladım. projeler/tum_metrik/GOREV_PROMPTU.md ve DURUM.md'yi oku, Bölüm X adım Y'den devam et."* Uzun sohbette tarayıcı engeli çıkarsa hemen yeni sohbete geç.
- **Yeni sohbette yalnız** `GOREV_PROMPTU.md`, `tum_metrik/DURUM.md` (son kayıt), 00, 01, 03 ve o anki bölümün gerektirdiği dosyalar okunur; sonra `tabs_context_mcp`. Eski sohbetin sekme numaralarını kullanma.

### 8.5 Chrome/IDB düşerse — kurtarma sırası (07'ye de yaz)
0. `tabs_context_mcp` çağır.
1. Oturumu kontrol et; Login.aspx görünüyorsa borfin yönlendirmesini kullan; açılmazsa dur, Ömer'e yaz.
2. Her işçi sekmesinde `window.__tmRun` ve IDB'deki `tm_hb_<sekme>` kalp atışına bak. Son 3 dakika içindeyse işçi **ÇALIŞIYOR**, yeniden başlatma (aynı sekmede iki döngü = çift istek).
3. Değilse kodu **DİSKTEN** (`araclar/sim_kodlari/`) kur; IDB'de yoksa IDB'ye de yaz.
4. Kalan işleri disk manifestinden ve `kuyruk.csv`'den hesapla: SHA'sı tutan ay/parça bitmiş sayılır.
5. Disk iznini `queryPermission` ile kontrol et; "prompt" ise IDB tamponuna yaz, `disk_bekleyen` kuyruğunu kullan ve Ömer'e tek cümlelik izin talimatı ver.
6. `navigator.storage.persist()` çağır.
7. IDB tamamen silindiyse: `araclar/kurulum/idb_geri_yukle.js` ile diskten geri yükle (2A.4'te sınanmış prosedür).

---

## Kısa kontrol listesi (her adımdan önce kendine sor)
- Ön kaydı sonuç görmeden yazdım mı? Deneme sayacına ve seri dosyasına ekledim mi?
- Kasa verisine dokundum mu? (Strateji başına bir kez, bütün eklemeler seçildikten sonra; dağılım hesapları da 2005–2020.)
- Bu karar 5 hisselik portföy simine mi dayanıyor, yoksa yalnız IC'ye mi?
- Şampiyon V2'nin **tam hali** (01 §C.4) ve üstündeki süzgeçler uygulandı mı? İki hüküm yan yana raporlandı mı?
- Hayalet/verisiz hisse nötr mü sayıldı? PIT şüphelisi mi?
- Veri diskte mi? Manifest güncel mi? `disk_bekleyen` boş mu?
- Sitede yalnız Farklı Kaydet mi kullandım? Çalışan bütün testler dahil en fazla 2 test mi var? Şifre girmedim mi? Hiçbir şey silmedim mi?
- Ömer'e kısa, Türkçe ve rakamlı rapor verdim mi?
