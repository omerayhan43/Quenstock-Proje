---
name: algomer
description: Algomer desktop app for BIST portfolio management — architecture, modules, infrastructure
sources: [backfill]
aliases: [ALFA Terminal, Gerçek Portföy, Real Portfolio module]
---
- [stated] FastAPI + PyWebView local Windows desktop application for BIST portfolio management
- [stated] Previously named "ALFA Terminal"
- [stated] Manages five proprietary screening algorithms, algorithmic paper portfolios, and a real money portfolio module
- [stated] Real Portfolio (Gerçek Portföy) module is fully architected: TWR calculation, benchmark comparison, financial freedom progress tracking
- [stated] Architectural principles are strict: algorithm outputs must be bit-for-bit reproducible (SHA-256 verified), no functional regressions tolerated, pages must render correctly (verified via jsdom)
- [stated] Next step: eliminate the Fintables Excel dependency by fetching financial statements directly from KAP, with 27 specific fields identified across five algorithms
- [stated] Infrastructure: deployed to an Oracle Cloud Always Free Ubuntu VM (Frankfurt)
- [stated] Infrastructure: dynamic TÜFE/İTO sourcing from TCMB
- [stated] Infrastructure: ING fund NAV fetching with T+1 logic
- [stated] Infrastructure: live price quote layer with outlier protection
- [stated] Benchmarks (BIST100, USD, Altın, BTC, S&P500) use 1 August 2026 as the reference date
