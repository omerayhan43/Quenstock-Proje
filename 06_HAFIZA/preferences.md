---
name: preferences
description: How Ömer wants Claude to work — browser automation/token use, memory mirroring to his PC, where project context lives
sources: [chat, cowork]
aliases: []
---
- [stated] In long-running browser automation (e.g. QueenStocks backtests), don't burn tokens with frequent polling/wait loops; start the work, give an ETA, and stop until the next check
- [stated] Wants all memory kept in two places as a safeguard: cloud memory AND the 06_HAFIZA folder in "Masaüstü\QueenStocks Projesi" on his PC; every memory update should be mirrored to both (dual update)
- [stated] QueenStocks strategy project context (rules, history, IDs, next steps) lives in "Masaüstü\QueenStocks Projesi" on his PC; new chats should connect that folder and start by reading 00_BASLA_BURADAN.md there
- [stated] Standard rule for every strategy development ("kaçan kazananlar testi"): for each year 2005–2026, take the year's top 30 (and top 50) best-returning stocks in the universe, check which the algorithm picked, and for the ones it didn't, find why (which gate, or ranked too low) — to catch the algorithm unintentionally eliminating something
