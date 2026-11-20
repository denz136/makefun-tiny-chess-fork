# tiny-chess-01 entry notes
Engine: MTD search, delta-encoded pst, king-safety guard.
Fork basis: sunfish classic (GPL-3.0-only, see LICENSE).
Search budget: 55000 nodes, deterministic, no clock.
Move guard: king-safety ok() with first-legal fallback.
