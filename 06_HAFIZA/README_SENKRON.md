# Hafıza yedeği ve ikili kayıt kuralı

**Kural (Ömer, 30/09/2026):** Bütün hafıza iki yerde tutulur ve birlikte güncellenir:
1. **Bulut hafızası** (Claude memory — tüm Claude sohbetlerinde, telefon dahil, otomatik okunur).
2. **Bu klasör** (`Masaüstü\QueenStocks Projesi\06_HAFIZA`) — bilgisayardaki birebir yedek.

Dosya düzeni bulut hafızasıyla aynıdır: `profile.md`, `preferences.md`, `areas/*.md`, `topics/*.md`. Satırlar "[stated]" etiketlidir (Ömer'in kendi söylediği).

## Her sohbette yapılacak (bu klasör sohbete bağlıysa)
1. **Başta:** `memory_list` ile bulut dosyalarının listesini ve güncellenme tarihlerini al; bu klasördekilerle karşılaştır. Bulutta daha yeni olanı (ya da burada olmayanı) `memory_read` ile okuyup buraya aynen yaz.
2. **Sohbet boyunca:** bulut hafızasına bilerek bir şey yazıldıysa (Ömer "hatırla/kaydet/unut" dediyse) aynı değişikliği buraya da uygula.
3. **Sonda:** bulut hafızası sohbetten sonra arka planda otomatik güncellenebilir; bu yüzden bir sonraki sohbetin başında 1. adım tekrar yapılır. `SON_SENKRON.txt` dosyasına tarih-saat ve kopyalanan dosyaları yaz.
4. **Silme:** Ömer bir bilgiyi unutturmak isterse iki yerden de silinir.

## Sınırlar (dürüst not)
- Bulut hafızası sohbetten sohbete kalıcıdır; Ömer silmedikçe veya ayarlardan "Generate memory from chats" kapatılmadıkça durur. Buna rağmen yedek, ek güvence içindir.
- Arka plandaki otomatik hafıza güncellemesi yalnız buluta yazar; bilgisayardaki kopya **ancak bu klasör bağlı bir sohbette** güncellenir. Klasör bağlı olmayan (örn. telefondan açılan) sohbetlerdeki değişiklikler bir sonraki bağlı sohbette aktarılır.
- Bu klasördeki dosyalar Claude tarafından otomatik okunmaz; bulut hafızası kaybolursa buradan geri yüklemek için Claude'a "06_HAFIZA'dan hafızayı geri yükle" denir.
