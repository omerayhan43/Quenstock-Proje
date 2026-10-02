# Ön kayıt — Taban T0 (01/10/2026 10:45, sonuçlar görülmeden yazıldı)

Kaynak: LITERATUR.md §4 (Ajan D iskeleti, dört raporun ortak sonucu). Eşikler literatürden değil, başlangıç önerisi; değiştirilmeden taban olarak ölçülür.

## T0 tanımı
- Evren: BIST TÜM (sitede "Herşey Dahil" 19006), her ay 5 hisse, eşit ağırlık, aylık, nakit yok.
- Sert filtre: `HAOran() < 60`.
- Kapı A (olay): `NetKarYillik() > 0` ve `ΔE/P = (NetKarYillik() − NetKarYillik("",-4)) / PD() ≥ 0,05`.
- Kapı B (piyasa teyidi): `C / Mov(C,200,S) > 1`.
- Skor: `100·A + 10·B + s1 + s2 + s3`
  - s1 = min(max(ΔE/P, 0), 0,20) / 0,20
  - s2 = min(max(C/HHV(H,252) − 0,5, 0), 0,5) / 0,5
  - s3 = min(max(Ref(C,-21)/Ref(C,-126) − 1, 0), 1)  (simde ay sonu kapanışlarıyla: C[m−1]/C[m−6])
- Sözlük sırası katmanlı tamamlamayı kendiliğinden yapar: A∧B → A∧¬B (teknik gevşer) → ¬A∧B (temel gevşer) → kalan.

## Ölçülecekler (taban için kabul kuralı yok; referans)
Son sermaye, CAGR, Sharpe, K-Ratio, kazandıran ay %, MDD, kriz ayları (XU100 < −%5) ortalaması, 2005–15 / 2016–26 / 2015+ CAGR, A∧B katmanından dolan ay oranı, Büyüme (208452) ve Değer (208459) BISTTUM ile korelasyon.

## Sonraki turların kuralları (Ajan D önerisi, kabul)
Tur başına en fazla 6 aday, tek değişken, önce sim; terfi kuralı v2 (01_KURALLAR C.4) + plasebo + deneme sayacı (t* raporu); final DSR ≥ 0,95, PBO ≤ 0,25. Aday listesi teşhis sonrası ayrı ön kayıtla (ON_KAYIT_T1.md) sabitlenecek.
