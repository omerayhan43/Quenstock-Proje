---
name: deger-yatirimi
description: Değer Yatırımı V1.1 value-investing strategy optimization project on QueenStocks — Ömer's ongoing work and how he wants it run
sources: [cowork]
aliases: [Değer Yatırımı V1.1, Değer Yatırımı, Değer Yatırımı Stratejisi, C32]
---
- [stated] Ongoing project: optimizing his "Değer Yatırımı V1.1" BIST value strategy (F-Skor + FD/FAVÖK based) via 2005-2026 backtests on QueenStocks; hands it to Claude to run autonomously while he's away
- [stated] Wants rejected/bad test variants cleared from the QueenStocks site so they don't clutter it, with the history and reasons kept in a markdown log
- [stated] QueenStocks site rules: only use "Farklı Kaydet" (never overwrite existing criteria/models); don't delete anything — list what should be deleted and he deletes it himself; never enter passwords; at most 2 tests running on the site at once
- [stated] Model should always buy stocks every month — no holding-cash rule
- [stated] No "final" stage: wants optimization to continue indefinitely, never declaring it good enough; explore the full value-investing literature and combine technical signals with fundamentals; focus on avoiding losers and capturing winners
- [stated] Delegates accept/reject decisions on variants to Claude: review site backtest results and compare the stocks bought, then accept what's reasonable; no need to ask for approvals
- [stated] Before building any new dataset, do literature research and diagnose gaps first, then set a roadmap
- [stated] Prioritizes stability and win rate over raw final capital (e.g. a higher win rate like 77% vs 72% matters more to him than extra return)
- [stated] Accesses QueenStocks through his Borfin account: if the QueenStocks session drops, go to the Borfin page and open QueenStocks from there — no password needed
- [stated] Wants every variant pre-evaluated in the offline simulation before spending a site backtest on it
- [stated] Keeps the portfolio at 5 stocks for now; doesn't want 10-stock versions — says more names won't bring a return jump and he can do that himself if he ever wants
- [stated] When variants are eliminated after simulation, wants them reported as eliminated per the rule; if an eliminated option increased returns, wants the reason for eliminating it told to him
- [stated] Declared variant C32 the new champion version of the strategy
- [stated] Put Değer Yatırımı work on hold to focus on the Kârlılık + momentum strategy, preferring to advance one strategy at a time
- [stated] Plans a BIST100 version of the Değer Yatırımı Stratejisi using the same rules and methodology as the Büyüme BIST100 build (all stages up to Aşama 6); Aşama 6 onward will evaluate the two BIST100 strategies (Büyüme + Değer) together
- [stated] Building a BISTKATILIM (Katılım Tüm) version of the Değer Yatırımı Stratejisi with the same methodology as the Katılım Büyüme build
- [stated] Delegated the Katılım champion choice to Claude ("istatistiksel olarak anlamlı ve mantıklı olan"); Katılım Değer outcome under that delegation: D0D (C32 + katmanlı tamamlama, every month 5 stocks), site names kriter 98394 "Değer Yatırımı (BISTKATILIM)", models 208538 (2005-2026) / 208539 (2015-2026); role = second leg of Büyüme + Ortak
- [stated] Asked (01/10) to keep improving both Katılım strategies by "thinking differently" in simulation, with reports prepared only at the end; outcome of that round under his delegation: "Değer + Ortak" (Değer's 5 picks, 2 shares if Büyüme also picked it) promoted as the Değer usage rule; no promotion for Büyüme
