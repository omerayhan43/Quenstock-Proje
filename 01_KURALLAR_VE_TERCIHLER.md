# Kurallar ve tercihler (ihlal edilemez)

Kaynak: Ömer'in sohbetlerde verdiği talimatlar, bulut hafızası, `projeler/deger_v11/PROTOKOL.md`, `projeler/*/YOL_HARITASI.md`. Çelişki olursa **Ömer'in en son söylediği** geçerlidir; emin değilsen sor.

---

## A. QueenStocks sitesi

1. **Yalnız "Farklı Kaydet".** Mevcut bir kriterin/modelin üzerine asla kaydetme: `btnSave` ve `btnModelKaydet` YASAK; her zaman `btnFarkliKaydet`. Kaydettikten sonra kaynağın hâlâ durduğunu ve yeni ID'yi doğrula.
2. **Hiçbir şeyi silme.** Gereksiz/elenen kriter ve modelleri ilgili `DURUM.md` ve `04_ID_KAYDI.md` içindeki **Silinecekler** listesine yaz; Ömer kendisi siler.
3. **Şifre girme**, hesap/abonelik ayarına dokunma. Oturum düşerse (Login.aspx): https://borfin.com/tr/programs/153/redirect (ya da borfin.com/tr/panel/programs → Queenstocks satırı → "Programa Git"); QueenStocks oturumu kendiliğinden geri gelir.
4. **Aynı anda en fazla 2 site testi.** Üçüncüsü sıraya girer.
5. **Korunan orijinaller** — okunur ve Farklı Kaydet ile kopyalanır, asla değiştirilmez:
   - Değer BAZ: kriter 94555 / model 208000
   - ALFA V4.1 orijinali: 95237 / 203135 ve Ömer'in eski algoritmaları (ALFA V1.4, V2.4, V3.4, V1.1.2, V1.2.2 vb.; liste `04_ID_KAYDI.md`)
   - Şampiyonlar: K10 98258 / 208322 · C32 98194 / 208224 · K4a 98322 / 208422 · DC1 98324 / 208424 · DX3b 98329 / 208433
   - Silinecek adayı olan kopyalar (98320 / 208419 K4a eski adı, 98342 DX3b ad kopyası) **Ömer karar verene kadar korunur**; yalnız listeye yazılır.
6. **Sabit test ayarları:** Bilanço kullanım "Yayınlanma Tarihine Göre" (Hesap Dönemine Göre ileriyi görme yanlılığı yaratır — asla) · 01/01/2005 – 25/09/2026 · Aylık · TL · 5 hisse eşit ağırlık · sıralama büyükten küçüğe.
   - BISTTUM stratejileri: Hisse kriteri "Herşey Dahil" (19006).
   - BIST100 stratejileri: ikinci hisse kriteri "Sadece BIST100" (19024) + **"Geçmiş tarihlerdeki endekslere dahil hisseleri kullan"** işaretli.
   - Model kopyalanınca ayarlar korunur ama her seferinde doğrula.

## B. Strateji tasarım kuralları

1. **5 hisse, eşit ağırlık, aylık yenileme.** Ömer 7/10/15 hisse sürümü istemiyor ("daha fazla hisse getiri sıçraması getirmez, istersem kendim yaparım"). Hisse sayısı, evren veya test dönemi değişikliği → önce sor.
2. **Nakitte kalma yok** ("Nakitte kalmayacağız"): model her ay 5 hisse alır. 5'ten az hisse geçen aylarda tamamlama sırası: **önce teknik koşullar gevşetilir, yetmezse temel** (katman yapısı). Nakit/rejim filtresi yalnız analiz olarak gösterilebilir, uygulama Ömer'in kararı.
3. **TÜFE eşiği (büyüme > Tufe(12)) değiştirilmez** — TMS 29 düzeltmesi yapılmaz, çıta yükseltilmez (Büyüme stratejisi kararı).
4. **Sadelik:** eşit performansta daha sade formül tercih edilir; formüllerin basitliği Ömer için önemli.
5. **Değer projesinde "final yok":** optimizasyon hiç "yeterli" ilan edilmeden sürer; tüm değer yatırımı literatürü taranır, teknik sinyaller temel analizle birleştirilir; odak "kaybedenden kaçın, kazananı yakala".
6. **Bir strateji bitmeden diğerine atlanmaz** ("strateji strateji ilerleyelim"). Sıra Ömer'in kararıdır.

## C. Yöntem (araştırma disiplini)

1. **Önce teşhis ve literatür, sonra veri seti ve yol haritası.** Rastgele parametre oynatmak yok; her değişikliğin ekonomik gerekçesi + verideki kanıtı olmalı.
2. **Önce simülasyon, sonra site.** Her aday simde birebir kopyayla (kapı + sıralama + 5 hisse) test edilir. **Simde olumlu ayrışmayan aday siteye GİTMEZ.** Havuz IC'si ≠ portföy iyileşmesi.
   - **Netleştirme (Ömer, 30/09 23:50):** Taban (Aşama 0 ölçüt modeli, simi kalibre etmek için) hariç **bütün denemeler önce simde**. Taban siteye gönderilirken Ömer'e "bu taban/kalibrasyon testidir" diye önceden söylenir.
3. **Ön kayıt:** denenecekler, düzeyler ve kabul kuralı sonuçlar görülmeden yazılıp sabitlenir (`ON_KAYIT_*.md`). Ön kayıt dışı bulunan aday "keşif" etiketi taşır; ileriye dönük fark yarıya indirilerek raporlanır.
4. **Terfi kuralı v2** (şampiyon değişikliği için hepsi gerekli):
   1. Son sermaye ≥ şampiyon × 1,05
   2. Kazandıran ay ≥ şampiyon − 0,5 puan
   3. Sharpe ≥ şampiyon; kriz ayları ortalaması ≥ şampiyon
   4. 2005–15, 2016–26 ve 2015+ ayrı ayrı olumlu
   5. En iyi 5 ay çıkarılınca fark hâlâ olumlu
   6. Plato: komşu düzeyler aynı yönde (tek sivri tepe değil)
   7. 5'ten az hisseli ay sayısı artmaz
   8. Plasebo (200 tohum, aynı sayıda rastgele değişiklik) %95'in üstünde
   9. Anlamlılık (uygulamadaki biçimiyle): eşli Newey-West t ≥ 1,5 → terfi edebilir. 1 ≤ t < 1,5 → diğer maddeleri geçiyorsa "zayıf" etiketiyle siteye gidebilir ama karar site sonucuna bağlıdır ve terfi için site farkı da kuralı geçmelidir (Büyüme BIST100 K3b/K4 böyle değerlendirildi; Değer BIST100 DX3b t 1,45 ile terfi etmedi, seçim Ömer'in kararı oldu). t < 1 → reddedilir. Çoklu test sonrası "güçlü" ≈ t 2,8. Deneme sayacı tutulur; final aday için Deflated Sharpe raporlanır. (Değer BISTTUM PROTOKOL v2'de "t ≥ 1,5 veya plasebo %95 üstü" yazıyordu; BIST100 projelerinde yukarıdaki biçim kullanıldı.)
   10. BIST100 için: yeni kurallar emülasyonu (E1) her adayda raporlanır ve olumlu olmalı
   11. Temiz mod (1 gün gecikme) ve gerçekçi (maliyetli) hesapta da olumlu
5. **Bağımsız doğrulama:** site aylık serileri Python araçlarıyla yeniden hesaplanır (eşli HAC t, blok bootstrap, Sharpe farkı bootstrap, Deflated Sharpe, PBO, yıllık Δlog) — `araclar/b100/cmp.py`.
6a. **Simülasyon:** sime erişim ve sıfırdan kurma `07_SIMULASYON_KILAVUZU.md`'de. Sim kalibre değilse (şampiyonla ≥ 260/261 aynı sepet) sonuçlarına güvenilmez.
6. **Editör doğrulaması:** her yeni formül sitede birkaç tarih ve hissede, sim sonucuyla birebir eşleşene kadar kontrol edilir (editör sonuç sözlüğü alfabetik gelir; kodla eşleştir, sırayla değil).
7. **Aşama onayı:** Ömer "onayım olmadan geçme" dediği aşamaya onaysız geçilmez (örn. Aşama 6 onayı 30/09'da verildi, yalnız BIST100 için). Test öncesi sorulacaklar: hisse sayısı 7/10, nakit/rejim filtresi, sektör sınırı.
8. **Karar yetkisi (Değer BISTTUM):** Ömer varyant kabul/red kararlarını Claude'a bırakmıştı (site sonuçlarını ve alınan hisseleri karşılaştırıp makul olanı kabul et). Ama şampiyon ilanları ve strateji seçimleri (C15, C32, K4a, DX3b) Ömer'in kararı olarak kaydedildi — sınırda durumda öner, kararı ona bırak.

9. **Kaçan kazananlar testi (Ömer, 01/10/2026 — standart kural):** her strateji ve her şampiyon adayı için 2005–2026'nın **her yılında**, o yılın evrenindeki en iyi getiren **ilk 30 (ve ilk 50)** hisse alınır; algoritma bunları o yıl aldı mı (kaç ay, o aylardaki getiri), almadıysa neden: (a) kapıda kaldı — hangi kapılar, kaç ay; (b) kapıları geçti ama sıralamada 6. ve sonrası — en iyi sırası; (c) verisi yok / evrende değil. Özet: kapı başına "kaçan kazananlarda kalma oranı / evren ortalaması". Amaç: algoritmanın istemeden bir şeyi elemesini yakalamak. Bulgular doğrudan kural değişikliği değildir; yalnız ön kayıtlı deneme fikri üretir (kapı kaldırma/gevşetme ablasyonu + terfi kuralı). Rapora ayrı bölüm olarak girer. Kod: IDB `code_kzwin`; örnek çıktı `projeler/buyume_katilim/KACAN_KAZANANLAR_BUYUME.md`.

## D. Raporlama

1. **Türkçe, kısa, rakamlı.** Her tur sonunda tablo + karar + sıradaki iş + tahmini bitiş saati (ETA).
2. **Elenenler gerekçeyle:** "simülasyon testi sonrası kurala göre elendi" + hangi şarta takıldığı. **Getiriyi (sermayeyi) artırıp elenen** her aday ayrı tabloda gerekçesiyle bildirilir; Ömer kararı değiştirebilir.
3. **Öncelik sırası:** istikrar ve kazandırma oranı > son sermaye (ör. %77 kazandırma, %72'ye göre ek getiriden önemli). Sonra Sharpe / K-Ratio, kriz koruması.
4. **Korelasyonlar yüzde** olarak verilir (0,80 değil %80).
5. **Dürüstlük:** beklenti abartılmaz; istatistiksel olarak anlamsız farklar "anlamsız" diye söylenir; sim–site farkı (iyimserlik) raporlanır. Ömer "hayal aleminde miyiz" diye sorduğunda gerekçeli, dürüst cevap istedi.
6. Site tarzı istatistik istenirse sitedeki formüllerin kopyası kullanılır (`araclar/agirlik/sitestat.py`): 2005–2026 ve 2015–2026.

## E. Zaman ve token disiplini

1. Uzun testlerde **sık yoklama/bekleme döngüsü yok**: başlat → ETA ver → dur; kontrolü `send_later` (bu sohbete zamanlanmış mesaj) ile kur (~70 dk sonra). Site testi ~60–70 dk.
2. Ekran görüntüsü yalnız gerektiğinde, küçük ölçekte; veri JavaScript ile metin olarak çekilir.
3. Ajanlar (alt ajanlar) siteye bağlanamaz; bağımsız analiz, literatür ve doğrulama için kullanılır, tarayıcı işçileri başladıktan sonra birlikte başlatılır.

## F. İsimlendirme (sitedeki adlar)

**Güncel format (Ömer, 30/09 — onaylı):** model adları ve Farklı Kaydet sırası:
1. Büyüme Stratejisi (BISTTUM) (2005-2026)
2. Büyüme Stratejisi (BISTTUM) (2015-2026)
3. Büyüme Stratejisi (BIST100) (2005-2026)
4. Büyüme Stratejisi (BIST100) (2015-2026)
5. Değer Yatırımı (BISTTUM) (2005-2026)
6. Değer Yatırımı (BISTTUM) (2015-2026)
7. Değer Yatırımı (BIST100) (2005-2026)
8. Değer Yatırımı (BIST100) (2015-2026)

Notlar (onaylı): Değer adlarında "Stratejisi" kelimesi yok. Kriterler dönemden bağımsız: strateji başına bir kriter, dönem eki olmadan ("Büyüme Stratejisi (BISTTUM)", "Büyüme Stratejisi (BIST100)", "Değer Yatırımı (BISTTUM)", "Değer Yatırımı (BIST100)"). Formüller değişmez.

Stratejilerin genel adları: K10 = "Büyüme Stratejisi"; C32 = "Değer Yatırımı Stratejisi"; ikisinin %50/%50 birleşimi = "Büyüme + Değer Yatırımı Stratejisi". Evren etiketi dosya adlarında "BISTTUM" / "BIST100". İleride BIST50 ve BIST30 sürümleri planlı.

Deneme adları (eski düzen): Değer BISTTUM `Değer Yatırımı V1.1-Txx (...)` / `V1.2-Cxx (...)`; Büyüme BISTTUM `ALFA V5 (GENIŞ HAVUZ) Kxx`; BIST100 denemeleri kısa kodlarla (B0, K4a, D0, DC1, DX3b...). Yeni denemelerde bu kodlar ad içinde kalabilir; şampiyon/yayın modelleri yukarıdaki güncel formatı kullanır.

## G. Hafıza

1. **İkili kayıt (Ömer, 30/09):** bulut hafızası (memory) ve bu klasördeki `06_HAFIZA/` birlikte güncellenir. Bulut hafızaya yazılan her kalıcı bilgi `06_HAFIZA/` altına da yazılır. Ayrıntı: `06_HAFIZA/README_SENKRON.md`.
2. Proje bilgisi (formül, ID, sonuç) bu klasördeki dosyalarda tutulur; hafızaya yalnız kalıcı kararlar ve tercihler gider.

## H. Ömer hakkında (çalışma bağlamı)

- BIST yatırımcısı; kantitatif hisse seçimi bağımsız projesi (meslek değil). Yazılım bilmiyor; kodun tamamı Claude'da.
- Algomer: kendi masaüstü portföy uygulaması (FastAPI + PyWebView). Pay hesabı aracı şimdilik Algomer'e eklenmeyecek.
- Genelde telefondan da takip eder; bilgisayar başında değilken tarayıcı/izin sorunları çözülemeyebilir — ona net, kısa talimat ver.
