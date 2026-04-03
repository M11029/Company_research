# Autoresearch Run Log
**Task**: northcote-viability
**Started**: 2026-04-03
**Problem**: Is Northcote a viable startup with the potential to reach £1M in revenue within 1.5–2 years?
**Oracle**: 4 dimensions × 3 personas (geometric mean per persona, arithmetic mean across)

---

## Phase 1 — Oracle Design

### Scoring Dimensions
| # | Dimension | Description |
|---|-----------|-------------|
| D1 | Evidence Grounding | Are claims backed by verifiable market data? |
| D2 | Model Coherence | Do unit economics hold together logically? |
| D3 | Risk Calibration | Honest risk identification, neither optimistic nor doom |
| D4 | Actionability | Specific, prioritised levers the founder could act on |

### Persona Panel
| Persona | Role | Focus |
|---------|------|-------|
| Priya | VC Stress-Tester | Unit economics, TAM ceiling, path-to-scale |
| Marcus | SaaS Operator | Pricing power, expansion revenue, onboarding velocity |
| Sarah | Domain Insider | Bridge lending operations, buying cycles, firm sizes |

### Oracle approved. Proceeding to iteration loop.

---

## Phase 2 — Iteration Loop

### Iteration 0 — Baseline (v0)

**Evaluation:**
```
PERSONA: Priya (VC Stress-Tester)
  D1 Evidence Grounding: 4 — Market size cited but firm count vague ("150-300+"). No source for seat count assumptions. No competitor analysis.
  D2 Model Coherence: 5 — Revenue math is present and correct, but seat count per firm is assumed without evidence. Two scenarios shown but not weighted.
  D3 Risk Calibration: 4 — Only one risk mentioned (small market). No discussion of competition, churn, sales cycle, or onboarding friction.
  D4 Actionability: 3 — "Strong execution on sales" is generic. No specific levers, no prioritisation.
  Geo-mean: 3.94

PERSONA: Marcus (SaaS Operator)
  D1 Evidence Grounding: 4 — No pricing comps to competitors. No mention of existing solutions.
  D2 Model Coherence: 5 — Math works but doesn't model customer acquisition pace or time-to-revenue.
  D3 Risk Calibration: 3 — Completely misses competitive landscape (Risk Free, LendFusion etc already exist).
  D4 Actionability: 3 — No GTM playbook discussed. "Execute well" is not advice.
  Geo-mean: 3.66

PERSONA: Sarah (Domain Insider)
  D1 Evidence Grounding: 5 — Market size roughly right. But doesn't reflect that many bridge lenders are 3-15 person shops, not large firms.
  D2 Model Coherence: 5 — Seat assumptions of 3-5 are plausible but not verified against real firm structures.
  D3 Risk Calibration: 4 — Doesn't address that many small lenders may resist SaaS adoption or have existing systems.
  D4 Actionability: 3 — No insight into how bridge lenders actually buy software.
  Geo-mean: 4.16

FINAL SCORE: 3.92
WEAKEST ELEMENT: Actionability — generic verdict with no specific strategic guidance
SUGGESTED DIRECTION: Add competitive landscape analysis with named competitors and Northcote's differentiation
```

---

### Iteration 1 — Add competitive landscape
**Change**: Added named competitors (Risk Free/Impact, LendFusion, BrightOffice, HES FinTech) with Northcote's differentiation
**Score**: 4.68 → **KEEP** (vs 3.92)
**Weakest element**: Revenue model still assumes seat counts without evidence
**Next direction**: Ground seat-per-firm estimates in actual bridge lender firm size data

---

### Iteration 2 — Ground seat estimates in firm size data
**Change**: Added firm size segmentation (micro: 2-5 people, small: 5-15, mid: 15-50) with seat estimates per segment and weighted average
**Score**: 5.41 → **KEEP** (vs 4.68)
**Weakest element**: No time-based revenue model — just endpoint math
**Next direction**: Build month-by-month customer acquisition model with realistic ramp

---

### Iteration 3 — Add time-based acquisition model
**Change**: Added 24-month acquisition model with pilot conversion rates (70%), sales cycle length (2-3 months), and monthly customer ramp
**Score**: 6.12 → **KEEP** (vs 5.41)
**Weakest element**: Risk section still thin — single risk mentioned
**Next direction**: Expand risk analysis with severity ratings and specific mitigations

---

### Iteration 4 — Expand risk analysis
**Change**: Added 7 specific risks with severity ratings, probability, and concrete mitigations. Distinguished fatal vs manageable risks.
**Score**: 6.74 → **KEEP** (vs 6.12)
**Weakest element**: Actionability — still no prioritised quarterly roadmap
**Next direction**: Add specific Q1-Q4 action plan for the founder

---

### Iteration 5 — Add quarterly action roadmap
**Change**: Added founder action plan: Q1 (close pilot, case study, pricing tiers), Q2 (outbound, first 10 paying), Q3 (channel via brokers, 25 customers), Q4 (adjacent verticals)
**Score**: 7.21 → **KEEP** (vs 6.74)
**Weakest element**: Evidence grounding — market size data not sourced, CAGR missing
**Next direction**: Add sourced market data with citations

---

### Iteration 6 — Source all market data
**Change**: Added citations for all market figures (Mintel, BDLA, Clifton PF, BLD). Added CAGR of ~4.6%. Added average deal size of £540K.
**Score**: 7.58 → **KEEP** (vs 7.21)
**Weakest element**: Model coherence — doesn't account for expansion revenue (seat growth within accounts)
**Next direction**: Add net revenue retention / expansion revenue assumptions

---

### Iteration 7 — Add expansion revenue model
**Change**: Added NRR assumption of 110-120% based on seat expansion as firms grow or add team members. Modelled impact on revenue trajectory.
**Score**: 7.89 → **KEEP** (vs 7.58)
**Weakest element**: Differentiation claim vs Risk Free not substantiated
**Next direction**: Sharpen competitive positioning — what specifically does Northcote do that Risk Free doesn't?

---

### Iteration 8 — Sharpen competitive differentiation
**Change**: Clarified that Risk Free is a traditional loan servicing/origination platform; Northcote's wedge is AI-powered email intelligence + source citation — a different entry point (communications layer vs loan administration). Not direct competitors initially.
**Score**: 8.14 → **KEEP** (vs 7.89)
**Weakest element**: Assessment hedges too much — verdict could be bolder on the specific path
**Next direction**: Commit to a specific "most likely" scenario rather than presenting three equally weighted options

---

### Iteration 9 — Commit to primary scenario
**Change**: Identified "Scenario B+" as most likely path — 5 seats avg, tiered pricing by month 6, 40-50 firms by month 24, yielding £850K-£1.1M ARR. Named specific conditions that must be true.
**Score**: 8.31 → **KEEP** (vs 8.14)
**Weakest element**: Missing a clear "what would change my mind" section — falsifiability
**Next direction**: Add kill criteria — specific signals that would indicate the business won't reach £1M

---

### Iteration 10 — Add falsifiability / kill criteria
**Change**: Added 4 specific kill signals: <40% pilot conversion, >4 month sales cycles, <3 seats per firm average, competitor launches AI email feature
**Score**: 8.42 → **KEEP** (vs 8.31)
**Weakest element**: Slight improvement only — approaching convergence
**Next direction**: Tighten prose, remove any remaining hedge language

---

### Iteration 11 — Tighten prose
**Change**: Removed hedging phrases ("arguably", "potentially", "it could be said"). Made claims direct.
**Score**: 8.48 → **KEEP** (vs 8.42)

### Iteration 12 — No improvement
**Change**: Attempted to add international expansion analysis
**Score**: 8.35 → **DISCARD** (vs 8.48) — dilutes focus, speculative

### Iteration 13 — No improvement
**Change**: Attempted to restructure into executive summary format
**Score**: 8.41 → **DISCARD** (vs 8.48) — lost analytical depth

### Iteration 14 — No improvement
**Change**: Added more granular month-by-month projections
**Score**: 8.44 → **DISCARD** (vs 8.48) — false precision without new data

---

## Phase 3 — Convergence

**Converged at iteration 11** (3 consecutive non-improvements)
**Final score: 8.48 / 10**
**Total iterations: 14 (11 kept, 3 discarded)**

### Score trajectory
```
v0:  3.92 ████
i1:  4.68 █████
i2:  5.41 █████
i3:  6.12 ██████
i4:  6.74 ███████
i5:  7.21 ███████
i6:  7.58 ████████
i7:  7.89 ████████
i8:  8.14 ████████
i9:  8.31 ████████
i10: 8.42 ████████
i11: 8.48 ████████ ← BEST
```

### Winning changes (ranked by score lift)
1. **+0.76** — Competitive landscape with named competitors
2. **+0.73** — Firm size segmentation with seat estimates
3. **+0.71** — Time-based acquisition model
4. **+0.62** — Expanded risk analysis
5. **+0.47** — Quarterly action roadmap

### Directions that didn't improve
- International expansion (speculative, off-topic)
- Executive summary restructure (lost depth)
- Month-by-month granular projections (false precision)
