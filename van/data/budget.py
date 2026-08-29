"""
van/data/budget.py
Line-item costs for the GMC Savana 2500 expedition build.

All prices are estimates as of 2026. Update actuals as purchased.
Status: 'planned' | 'ordered' | 'purchased' | 'installed'
"""

# ── VEHICLE ───────────────────────────────────────────────────────────────────

VEHICLE = {
    "description": "GMC Savana 2500 Extended — used, target purchase",
    "estimated":   12000,
    "actual":      None,
    "status":      "planned",
    "notes":       "Target: 80,000-120,000 miles, clean CarFax, no rust on frame",
}

# ── STAGE 1A — LIGHTWEIGHT LIVING INFRASTRUCTURE ─────────────────────────────

STAGE_1 = [
    # Insulation
    # Insulation — revised stack (VAN-016)
    {"item": "Noico 80mil butyl damping mat (50 sqft)",          "category": "Insulation", "est": 110,  "actual": None, "status": "planned",
     "notes": "Replaces Dynamat — same damping, 70% less cost. Partial coverage of resonant panels only."},
    {"item": "3M Thinsulate SM600L (60 sqft)",                   "category": "Insulation", "est": 250,  "actual": None, "status": "planned",
     "notes": "Cavity fill walls/ceiling/doors. Hydrophobic, removable, no vapor barrier needed."},
    {"item": "XPS rigid foam board 1-inch (10 sheets 4x8)",      "category": "Insulation", "est": 120,  "actual": None, "status": "planned",
     "notes": "Replaces Polyiso. Stable R5/inch at 25F. Walls, ceiling, floor. Friction-fit, removable."},
    {"item": "Great Stuff Gaps and Cracks (3 cans)",             "category": "Insulation", "est": 25,   "actual": None, "status": "planned",
     "notes": "Targeted void sealing only. NOT continuous spray foam application."},
    # Closed-cell spray foam and Dynamat Extreme REMOVED — see VAN-016 and VAN-017
    # Framework
    {"item": "Aluminum Unistrut P1000T — 10 channel runs (wall/ceiling/floor)", "category": "Channel Grid","est": 280,   "actual": None, "status": "planned"},
    {"item": "Stainless spring nuts, bolts, washers — all channel connections", "category": "Channel Grid","est": 80,    "actual": None, "status": "planned"},
    {"item": "Ceiling hardpoint hardware (4x through-bolts, backing plates, seals)", "category": "Channel Grid","est": 85,    "actual": None, "status": "planned"},
    # Walls and ceiling
    {"item": "3mm bamboo plywood panels",          "category": "Walls",         "est": 320,   "actual": None, "status": "planned"},
    {"item": "Flexible bamboo slat cladding",      "category": "Walls",         "est": 180,   "actual": None, "status": "planned"},
    {"item": "ACP panels (water zones)",           "category": "Walls",         "est": 90,    "actual": None, "status": "planned"},
    {"item": "Rubio Monocoat oil finish",          "category": "Walls",         "est": 75,    "actual": None, "status": "planned"},
    # Floor
    # Plywood subfloor REMOVED — lightweight first build, horse mats on van floor directly
    {"item": "Rubber horse stall mats x2 (Tractor Supply)", "category": "Floor","est": 90,    "actual": None, "status": "planned"},
    # Sleep platform
    {"item": "Hemp webbing (1\" natural, 100 ft)", "category": "Sleep",         "est": 95,    "actual": None, "status": "planned"},
    # Lighting — 5 zones
    {"item": "Zone 1 Ambient: LED strip 2700K + frosted channel cover (both ceiling runs)", "category": "Lighting", "est": 90, "actual": None, "status": "planned"},
    {"item": "Zone 2 Reading: 2x adjustable LED puck lights with swivel arm (Unistrut mount)", "category": "Lighting", "est": 65, "actual": None, "status": "planned"},
    {"item": "Zone 3 Work: LED strip 4000K neutral white (mid wall channel both sides)", "category": "Lighting", "est": 80, "actual": None, "status": "planned"},
    {"item": "Zone 4 Night: Red LED strip low floor channel port side", "category": "Lighting", "est": 30, "actual": None, "status": "planned"},
    {"item": "Zone 5 Exterior: 2x weatherproof LED puck lights above rear doors", "category": "Lighting", "est": 45, "actual": None, "status": "planned"},
    {"item": "Lighting rocker panel (MASTER + 5 zone switches, Carling or Blue Sea)", "category": "Lighting", "est": 85, "actual": None, "status": "planned"},
    # Natural fiber accents
    {"item": "Jute rope wrap, hemp canvas curtains, linen lamp shades, storage pockets", "category": "Accents", "est": 120, "actual": None, "status": "planned"},
    {"item": "Bamboo lyocell quilted topper",      "category": "Sleep",         "est": 180,   "actual": None, "status": "planned"},
    # Power — batteries
    {"item": "400Ah LiFePO4 battery bank (Battle Born or equiv)", "category": "Power", "est": 3800, "actual": None, "status": "planned"},
    {"item": "300A ANL master fuse + holder",      "category": "Power",         "est": 45,    "actual": None, "status": "planned"},
    # Power — Victron ecosystem
    {"item": "Victron MultiPlus 12/3000",          "category": "Victron",       "est": 890,   "actual": None, "status": "planned"},
    {"item": "Victron SmartSolar MPPT 100/50",     "category": "Victron",       "est": 220,   "actual": None, "status": "planned"},
    {"item": "Victron Orion-XS 12/12-30A DC-DC",  "category": "Victron",       "est": 185,   "actual": None, "status": "planned"},
    {"item": "Victron Lynx Distributor",           "category": "Victron",       "est": 145,   "actual": None, "status": "planned"},
    {"item": "Victron SmartShunt 500A",            "category": "Victron",       "est": 85,    "actual": None, "status": "planned"},
    # Distribution panels
    {"item": "Blue Sea 12-circuit fused DC panel", "category": "Distribution",  "est": 195,   "actual": None, "status": "planned"},
    {"item": "Blue Sea AC 4-circuit panel",        "category": "Distribution",  "est": 110,   "actual": None, "status": "planned"},
    {"item": "Blue Sea 2506 ground bus bar",       "category": "Distribution",  "est": 35,    "actual": None, "status": "planned"},
    {"item": "Shore power inlet 30A",              "category": "Distribution",  "est": 55,    "actual": None, "status": "planned"},
    # Solar
    {"item": "2x 100W rigid panels + mounts",     "category": "Solar",         "est": 380,   "actual": None, "status": "planned"},
    {"item": "2x Renogy 200W briefcase panels",    "category": "Solar",         "est": 420,   "actual": None, "status": "planned"},
    {"item": "50-ft MC4 extension cables",         "category": "Solar",         "est": 45,    "actual": None, "status": "planned"},
    # Wind turbine pre-wire (install in Stage 3)
    {"item": "Wind turbine pre-wire kit (30A breaker, connector, cable gland)", "category": "Wind Pre-wire", "est": 95, "actual": None, "status": "planned"},
    # Climate
    {"item": "OutEquipPro Summit 2 AC/heat unit",  "category": "Climate",       "est": 1450,  "actual": None, "status": "planned"},
    {"item": "Wired thermostat for Summit 2",      "category": "Climate",       "est": 45,    "actual": None, "status": "planned"},
    {"item": "MaxxAir roof fan",                   "category": "Climate",       "est": 185,   "actual": None, "status": "planned"},
    # Water
    {"item": "30-gallon fresh water tank",         "category": "Water",         "est": 145,   "actual": None, "status": "planned"},
    {"item": "12V demand pump",                    "category": "Water",         "est": 65,    "actual": None, "status": "planned"},
    {"item": "PEX plumbing + SharkBite fittings",  "category": "Water",         "est": 80,    "actual": None, "status": "planned"},
    {"item": "Exterior ball valve + shore fitting", "category": "Water",         "est": 35,    "actual": None, "status": "planned"},
    # Sanitation
    {"item": "Nature's Head composting toilet",    "category": "Sanitation",    "est": 960,   "actual": None, "status": "planned"},
    {"item": "12V vent fan for toilet",            "category": "Sanitation",    "est": 35,    "actual": None, "status": "planned"},
    # Monitoring
    {"item": "SIMARINE PICO battery monitor",      "category": "Monitoring",    "est": 195,   "actual": None, "status": "planned"},
    {"item": "TriMetric 2030",                     "category": "Monitoring",    "est": 145,   "actual": None, "status": "planned"},
    {"item": "Belden shielded cable + Amphenol connectors", "category": "Monitoring", "est": 120, "actual": None, "status": "planned"},
    # Electronics bay — dog hair filtration (VAN-018)
    {"item": "Electronics bay enclosure (plywood + aluminum panel door)", "category": "Electronics Bay", "est": 35, "actual": None, "status": "planned"},
    {"item": "MultiPlus intake filter frames x2 + spare filter media x3",         "category": "Electronics Bay", "est": 25, "actual": None, "status": "planned",
     "notes": "80-120mm panel filter frames. Inspect monthly. With husky, expect fast loading."},
    {"item": "Bay ventilation grilles — intake (filtered) + exhaust (open)",      "category": "Electronics Bay", "est": 15, "actual": None, "status": "planned"},
    # Communications
    {"item": "Cobra 29 LX CB radio",               "category": "Comms",         "est": 95,    "actual": None, "status": "planned"},
    {"item": "Starlink Mini ethernet adapter",     "category": "Comms",         "est": 25,    "actual": None, "status": "planned"},
    {"item": "Garmin inReach Mini 2",              "category": "Comms",         "est": 350,   "actual": None, "status": "planned"},
    {"item": "Neutrik chassis jacks + Amphenol connectors", "category": "Comms","est": 85,    "actual": None, "status": "planned"},
    # Wire, cable, misc
    {"item": "2/0 AWG welding cable (100 ft)",     "category": "Wire",          "est": 180,   "actual": None, "status": "planned"},
    {"item": "4 AWG wire, 10 AWG wire, misc wire", "category": "Wire",          "est": 120,   "actual": None, "status": "planned"},
    {"item": "Heat shrink, terminals, connectors", "category": "Wire",          "est": 85,    "actual": None, "status": "planned"},
    {"item": "Conduit, cable management, labels",  "category": "Wire",          "est": 55,    "actual": None, "status": "planned"},
    {"item": "Misc hardware, fasteners, adhesives","category": "Misc",          "est": 200,   "actual": None, "status": "planned"},
]

# ── STAGE 2 — SAFETY AND EXPEDITION ──────────────────────────────────────────

STAGE_2 = [
    {"item": "Aluminess front winch bumper",       "category": "Bumper",        "est": 1800,  "actual": None, "status": "planned"},
    {"item": "Warn VR EVO 12-S winch",             "category": "Winch",         "est": 650,   "actual": None, "status": "planned"},
    {"item": "Baja Designs driving lights",        "category": "Lighting",      "est": 380,   "actual": None, "status": "planned"},
    {"item": "Rigid Industries flood lights",      "category": "Lighting",      "est": 290,   "actual": None, "status": "planned"},
    {"item": "40-inch LED light bar",              "category": "Lighting",      "est": 180,   "actual": None, "status": "planned"},
    {"item": "Bubba Rope kinetic recovery rope",   "category": "Recovery",      "est": 145,   "actual": None, "status": "planned"},
    {"item": "Factor 55 FlatLink shackle",         "category": "Recovery",      "est": 85,    "actual": None, "status": "planned"},
    {"item": "MAXTRAX recovery boards x2",         "category": "Recovery",      "est": 320,   "actual": None, "status": "planned"},
    {"item": "Hi-Lift jack + base plate",          "category": "Recovery",      "est": 115,   "actual": None, "status": "planned"},
    {"item": "Snatch block and rigging kit",       "category": "Recovery",      "est": 85,    "actual": None, "status": "planned"},
    {"item": "IR thermal camera — front exterior", "category": "Security",      "est": 420,   "actual": None, "status": "planned"},
    {"item": "4x IR perimeter cameras (wired)",    "category": "Security",      "est": 380,   "actual": None, "status": "planned"},
    {"item": "Camera wiring and DVR unit",         "category": "Security",      "est": 180,   "actual": None, "status": "planned"},
    {"item": "Vaultek LifePod 2.0 (handgun)",      "category": "Security",      "est": 220,   "actual": None, "status": "planned"},
    {"item": "SecureIt Fast Box Model 40 (long gun)","category": "Security",    "est": 300,   "actual": None, "status": "planned"},
]

# ── STAGE 3 — KITCHEN, COMFORT, DOGS, WIND ───────────────────────────────────

STAGE_3 = [
    # Wind turbine — ORDER FIRST
    {"item": "Primus AIR Silent X 440W wind turbine", "category": "Wind",       "est": 1200,  "actual": None, "status": "planned",
     "notes": "ORDER FIRST — 4-6 week lead time"},
    {"item": "Primus 27-ft tilt-up guyed tower kit",  "category": "Wind",       "est": 850,   "actual": None, "status": "planned"},
    {"item": "Primus Digital Control Panel",           "category": "Wind",       "est": 145,   "actual": None, "status": "planned"},
    {"item": "Mast storage bag (weatherproof vinyl)",  "category": "Wind",       "est": 55,    "actual": None, "status": "planned"},
    # Roof and exterior
    {"item": "Aluminess roof rack",                "category": "Roof",           "est": 1650,  "actual": None, "status": "planned"},
    {"item": "Aluminess deluxe storage box",       "category": "Roof",           "est": 480,   "actual": None, "status": "planned"},
    # Awning system — full three-side coverage (VAN-019)
    {"item": "Alu-Cab 270° Shadow Awning RHS — passenger side (2.6m, 10m² coverage)",
     "category": "Awning", "est": 1050, "actual": None, "status": "planned",
     "notes": "Covers rear + full passenger side. 45-second deploy, one person, freestanding. Mounts to Aluminess rack via load bar brackets (included or separate)."},
    {"item": "Alu-Cab roof rack load bar brackets for 270° awning",
     "category": "Awning", "est": 85,   "actual": None, "status": "planned"},
    {"item": "OVS HD Nomadic 180° awning LHS — driver side",
     "category": "Awning", "est": 650,  "actual": None, "status": "planned",
     "notes": "Overhead cover for Shower Cube on driver side. Combined with 270° RHS: full rear + both sides covered. Each deploys independently."},
    {"item": "Alu-Cab Shower Cube + LHS roof rack mounting brackets",
     "category": "Awning", "est": 550,  "actual": None, "status": "planned",
     "notes": "9kg. Mounts to LHS (driver side) rack under OVS 180 awning. Separate shower zone from kitchen. 43L x 36W x 74-94H inches open."},
    # Refrigeration
    {"item": "Dometic CFX3 45L compressor fridge/freezer", "category": "Fridge","est": 950,   "actual": None, "status": "planned"},
    # Kitchen
    {"item": "Coleman 2-burner propane stove",     "category": "Kitchen",        "est": 75,    "actual": None, "status": "planned"},
    {"item": "Lodge cast iron skillet 12\"",       "category": "Kitchen",        "est": 35,    "actual": None, "status": "planned"},
    {"item": "Lodge cast iron griddle",            "category": "Kitchen",        "est": 35,    "actual": None, "status": "planned"},
    {"item": "Lodge cast iron Dutch oven 6qt",     "category": "Kitchen",        "est": 60,    "actual": None, "status": "planned"},
    {"item": "Lodge cast iron stovetop waffle iron","category": "Kitchen",       "est": 35,    "actual": None, "status": "planned"},
    {"item": "Jetboil Flash backpacking stove",    "category": "Kitchen",        "est": 95,    "actual": None, "status": "planned"},
    {"item": "Instant Pot Duo Mini 3qt",           "category": "Kitchen",        "est": 65,    "actual": None, "status": "planned"},
    # Dogs
    {"item": "Gunner Kennel G1 (Tango)",           "category": "Dogs",           "est": 380,   "actual": None, "status": "planned"},
    {"item": "Sleepypod Mobile Pet Bed (Saki)",    "category": "Dogs",           "est": 135,   "actual": None, "status": "planned"},
    {"item": "Ruffwear harnesses x2",              "category": "Dogs",           "est": 110,   "actual": None, "status": "planned"},
    {"item": "K9 Sport Sack carrier (Saki)",       "category": "Dogs",           "est": 95,    "actual": None, "status": "planned"},
    {"item": "Canine first aid kit",               "category": "Dogs",           "est": 45,    "actual": None, "status": "planned"},
    {"item": "Dog booties, Musher's Secret, misc", "category": "Dogs",           "est": 55,    "actual": None, "status": "planned"},
    {"item": "Vittles Vault food storage",         "category": "Dogs",           "est": 35,    "actual": None, "status": "planned"},
]

# ── STAGE 4 — DUAL DISPLAY SYSTEM ────────────────────────────────────────────

STAGE_4 = [
    {"item": "Industrial fanless PC — ruggedized",     "category": "Display",   "est": 850,   "actual": None, "status": "deferred"},
    {"item": "Custom PCB — sensor integration",        "category": "Display",   "est": 350,   "actual": None, "status": "deferred"},
    {"item": "Helm display — passenger side dash",     "category": "Display",   "est": 480,   "actual": None, "status": "deferred"},
    {"item": "Engineering display — cargo area",       "category": "Display",   "est": 380,   "actual": None, "status": "deferred"},
    {"item": "Wiring, mounts, misc",                  "category": "Display",   "est": 180,   "actual": None, "status": "deferred"},
    {"item": "Software development",                   "category": "Display",   "est": 260,   "actual": None, "status": "deferred"},
]

# ── MECHANICAL STAGES ─────────────────────────────────────────────────────────

MECHANICAL = {
    "A": {"description": "Fluids, filters, ignition + AFM disable", "est": 570, "actual": None, "status": "planned", "notes": "Includes $120 Range Technology AFM Disabler — priority item, do before first drive"},
    "B": {"description": "Interim brakes, engine management",  "est": 380,   "actual": None, "status": "planned"},
    "C": {"description": "Wilwood 4-corner brake upgrade + suspension",
          "est": 2800,  "actual": None, "status": "pending_weight",
          "notes": "Cannot be specced until Stage 1 loaded weight is known"},
    "D": {"description": "Ground kit (factory + aux systems)", "est": 320,   "actual": None, "status": "planned"},
    "E": {"description": "Post-expedition upgrades",           "est": 3800,  "actual": None, "status": "deferred"},
}

# ── EXTERIOR WRAP ─────────────────────────────────────────────────────────────

WRAP = {
    "vinyl_wrap":         {"est": 7500,  "actual": None, "status": "planned", "notes": "Three-zone ColorFlow/Satin Khaki/Matte Adobe"},
    "ppf_front_rockers":  {"est": 850,   "actual": None, "status": "planned", "notes": "Paint protection film — front fascia, lower body, rockers"},
    "artist_commission":  {"est": 450,   "actual": None, "status": "planned", "notes": "Vector art for 8 Easter eggs — petroglyph/sumi-e style"},
}

# ── SUMMARY ───────────────────────────────────────────────────────────────────

def stage_total(stage_list, use_actual=False):
    """Sum estimated or actual costs for a stage item list."""
    total = 0
    for item in stage_list:
        val = item.get("actual") if use_actual else item.get("est", 0)
        if val is not None:
            total += val
    return total


def budget_summary(use_actual=False):
    """Return a dict of stage totals and the grand total."""
    return {
        "vehicle":       VEHICLE.get("actual" if use_actual else "estimated", 0) or 0,
        "stage_1":       stage_total(STAGE_1, use_actual),
        "stage_2":       stage_total(STAGE_2, use_actual),
        "stage_3":       stage_total(STAGE_3, use_actual),
        "stage_4":       stage_total(STAGE_4, use_actual),
        "mechanical_AE": sum(v.get("actual" if use_actual else "est", 0) or 0
                             for v in MECHANICAL.values()),
        "wrap":          sum(v.get("actual" if use_actual else "est", 0) or 0
                             for v in WRAP.values()),
    }


def grand_total(use_actual=False):
    return sum(budget_summary(use_actual).values())


def items_by_status(status):
    """Return all line items across all stages with the given status."""
    all_items = STAGE_1 + STAGE_2 + STAGE_3 + STAGE_4
    return [item for item in all_items if item.get("status") == status]


def items_needing_order():
    """Return items that should be ordered now — planned status with order notes."""
    all_items = STAGE_1 + STAGE_2 + STAGE_3 + STAGE_4
    return [item for item in all_items
            if item.get("status") == "planned"
            and "order" in item.get("notes", "").lower()]
