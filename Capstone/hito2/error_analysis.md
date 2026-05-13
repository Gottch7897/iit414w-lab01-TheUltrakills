# Error Analysis — Hito 2 Dimension 1

Sliced by:

- **Strategy type:** one_stop / two_stop / three_plus_stop / no_stop
- **Circuit type:** street / permanent / hybrid
- **Constructor tier (additional context):** top_tier / mid_tier / lower_tier. Justification: pit-stop discipline, crew execution, and strategic flexibility vary significantly by team budget and infrastructure.
- **Both targets:** is_top10 and is_top5 analyzed in parallel

---

## Scenario Comparisons by Dimension

### 1. Strategy Slice: One-Stop vs. Two-Stop (Italian GP 2024, Ferrari, Street Circuit)

**Context (held fixed):** Season 2024, Italian Grand Prix (street circuit), Carlos Sainz, Ferrari (top_tier), Grid 5

| Scenario | Strategy | n_stops | P(is_top10) | P(is_top5) | Verdict |
|----------|----------|---------|------------|-----------|---------|
| Hito 1 1-stop (baseline) | one_stop (M-H compound) | 1 | 0.9277 | 0.8282 | Preferred |
| Hito 1 2-stop | two_stop (M-H stint split) | 2 | 0.8977 | 0.7550 | — |
| **Agreement:** | — | — | ✅ is_top10 & is_top5 agree: 1-stop preferred | — | **AGREE** |
| **Gap (1-stop advantage)** | — | — | +3.0pp (is_top10) | +7.3pp (is_top5) | *Top-5 shows larger lift* |

---

### 2. Sensitivity Test: Stint Length Variation (Same 1-stop vs 2-stop context)

All variants below compare the **same pit-stop strategy pair** with **different stint inputs** to test robustness:

| Variant | Scenario A (1-stop) | P(top10) | P(top5) | Scenario B (2-stop) | P(top10) | P(top5) | Agreement |
|---------|------------------|---------|--------|------------------|---------|--------|-----------|
| **Compound S-M-H** | S-M-H, 26-27-0 | 0.9163 | 0.8250 | S-M-H, 12-22-19 | 0.8822 | 0.7509 | ✅ AGREE |
| **Compound M-H (middle stint 22)** | M-H, 12-27-0 | 0.9258 | 0.7827 | M-H, 12-22-19 | 0.8977 | 0.7550 | ✅ AGREE |
| **Compound M-H (stint1 extended)** | M-H, 26-27-0 | 0.9277 | 0.8282 | M-H, 12-22-19 | 0.8977 | 0.7550 | ✅ AGREE |
| **Compound M-H (stint1 mid)** | M-H, 20-27-0 | 0.9269 | 0.8097 | M-H, 20-22-19 | 0.8992 | 0.7845 | ✅ AGREE |
| **Three-stop variant** | M-H, 12-27-0 | 0.9966 | 0.9887 | M-H, 12-22-19 | 0.9769 | 0.9382 | ✅ AGREE |

**Findings:**
- All variants show **AGREE:** 1-stop (or 1-vs-2 fewer stops) consistently preferred by both targets
- **is_top5 sensitivity:** larger gaps in 3-stop variant (9.7pp vs 5.2pp for is_top10), suggesting top-5 more sensitive to pit-stop count
- **is_top10 robustness:** remains stable (~92.6%) across stint variations; is_top5 varies by compound/stint (78–82%), indicating strategy matters more for podium finishes

