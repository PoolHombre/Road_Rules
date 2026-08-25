# CLAUDE.md
## Road_Rules — Project Context

Read this before touching anything in the repo.

---

## Owner
Kevin McAuley · github.com/PoolHombre · kmcauley@aquasol.com
Wife: Lisa · Dogs: Saki (schnauzer, ESA) · Tango (husky, ADA service animal)

---

## What This Repo Is

Two active projects, one repo:

**Van** — GMC Savana 2500 Extended expedition build, staged in phases.
**Trip** — 2027 Glacier NP road trip, July 15 – August 11, 28 days.

Both are living documents. The van build is in progress. The trip is planned and booked.

---

## Active State

### Van Build
- Stage A (fluids/filters): pending vehicle purchase
- Stage 1 (living infrastructure): planning complete, $18,115
- Stage 2 (safety/expedition): planning complete, $6,550
- Stage 3 (kitchen/comfort/dogs/wind): planning complete, $9,092 — ORDER PRIMUS TURBINE FIRST (4-6 week lead time)
- Stage 4 (dual display): deferred until after first expedition
- Stage C (Wilwood brakes): pending Stage 1 loaded weight — do not spec until weight is known
- Wrap: applied LAST, after all exterior hardware installed

### Trip
- Departure: Thursday July 15, 2027
- Return: Wednesday August 11, 2027
- Glacier: July 28 – August 4 (7 nights)
- Parents at Glacier: July 28 – ~August 1
- Logan Pass shuttle: Tuesday August 3 — book recreation.gov June 3, 2027 at 7:00 PM MDT
- Pioneer Day July 24: Day 10 at Theodore Roosevelt NP, North Dakota ✅ (not Utah)
- Sturgis Rally: Black Hills done July 22, rally starts August 1 ✅ (10 days clear)

---

## Hard Rules — Never Violate These

### Van
- No induction cooktop — outdoor cooking only, permanent rule
- Analog-first — no internal wireless except Starlink (wired ethernet only)
- WiFi disabled on: AC thermostat, cameras, all monitoring systems
- Wrap applied LAST — never before all exterior hardware is installed
- Stage C brake spec requires Stage 1 loaded weight — do not guess the weight

### Trip
- Departure date July 15 is fixed — driven by parents' Glacier schedule
- Glacier dates July 28 – August 4 are fixed — parents' anchor
- Hotel nights: breakfast provided + dinner out — zero cooking, no exceptions
- Dog access: Tango (ADA) has full trail access everywhere; Saki (ESA) is restricted to roads/campgrounds/parking at NPS sites

### Documents
- Changelogs are append-only — never delete or modify existing entries
- All data lives in `trip/data/` or `van/data/` — never embedded in generators
- PDFs: Carlito font, neutral palette, no color coding, mobile-optimized
- No color-coded headers or heavy color blocks in any document

---

## Repo Structure

```
Road_Rules/
├── CLAUDE.md               ← you are here
├── build.py                ← python build.py | --van | --trip
├── requirements.txt
├── Makefile
├── shared/
│   ├── utils.py            ← haversine, crowd scoring, Pioneer Day/Sturgis checks
│   ├── pdf_styles.py       ← Carlito fonts, neutral palette, all styles
│   └── pdf_components.py   ← reusable tables, boxes, headers
├── van/
│   ├── spec/
│   │   ├── stages.py       ← Build stages 1-4 + mechanical A-E
│   │   ├── electrical.py   ← 3-domain architecture, circuit map, power budget
│   │   ├── mechanical.py   ← Mechanical stages A-E (detailed)
│   │   └── exterior.py     ← Wrap spec, Easter eggs, Aluminess hardware
│   ├── data/
│   │   ├── budget.py       ← Line-item costs, running totals by stage
│   │   ├── vendors.py      ← Supplier contacts, lead times, order status
│   │   └── weight.py       ← Weight estimates by stage (gates Stage C)
│   ├── changelog.py        ← Van decisions — append only
│   └── generate_spec.py    ← Builds Van_Build_Master_Spec.pdf
├── trip/
│   ├── data/
│   │   ├── destinations.py ← 16 stops, GPS, crowd ratings, full research
│   │   ├── itinerary.py    ← 28-day confirmed schedule, KEY_DATES
│   │   ├── meals.py        ← 28-day meal plan, Lisa's favorites
│   │   ├── churches.py     ← Catholic churches, Mass times by stop
│   │   └── training.py     ← GB locations, alternatives by stop
│   ├── rules/
│   │   ├── route_rules.py  ← Driving limits, camping hierarchy, fire rules
│   │   └── dog_rules.py    ← ADA vs ESA access by land type and stop
│   ├── companion.py        ← Builds the 28-day companion story
│   ├── changelog.py        ← Trip decisions — append only
│   └── generate_reports.py ← Builds all three trip PDFs
├── tests/
│   ├── test_itinerary.py   ← Date validation, Pioneer Day, Sturgis
│   ├── test_meals.py       ← Meal coverage, hotel rules, favorites schedule
│   └── test_van.py         ← Budget math, stage totals
└── outputs/
    ├── current/            ← Latest build
    └── archive/            ← Date-stamped previous builds
```

---

## Conventions

### Data files
- Plain Python dicts and lists — no JSON, no YAML, no databases
- Keys are consistent across files (stop names match between destinations.py and itinerary.py)
- Comments explain the why, not the what

### Generators
- Read from data files only — no hardcoded content
- Write to `outputs/current/`
- `build.py --archive` copies current to `outputs/archive/YYYY-MM-DD/` before rebuilding

### Changelogs
- Format: `{"id": "TRIP-017", "date": "YYYY-MM", "decision": "...", "reason": "..."}`
- IDs are sequential and never reused
- Next van ID: VAN-011
- Next trip ID: TRIP-017

### Git
- `main` always builds and generates valid PDFs
- Branch for work in progress: `van/stage-2`, `trip/glacier-update`, etc.
- Commit messages: imperative, specific, reference the data file changed
- Push from Claude server using stored token

### PDF style
- Font: Carlito (metrically identical to Calibri)
- Background: white or #F7F7F7 only
- Table headers: #2A2A2A (near-black)
- Accent: #8B6914 (warm gold) — Lisa's favorites only
- No color coding. No rainbow headers. No heavy color blocks.
- Mobile-optimized: 10pt body text, 15pt leading, wide margins

---

## Key People and Animals

| Name  | Role | Notes |
|-------|------|-------|
| Kevin | Builder, driver, planner | kmcauley@aquasol.com |
| Lisa  | Co-pilot, navigator, fifth anniversary honoree | Surprise meals are for her |
| Tango | Husky, ADA service animal | Full trail access everywhere |
| Saki  | Schnauzer, ESA | NPS: roads/campgrounds/parking only |

---

## What NOT to Change Without Asking

- Departure date (July 15) — fixed by parents
- Glacier dates (July 28 – August 4) — fixed by parents
- Logan Pass date (August 3) — shuttle booked June 3
- The outdoor kitchen rule — permanent
- The analog-first philosophy — permanent
- Any changelog entry — append only, never edit
