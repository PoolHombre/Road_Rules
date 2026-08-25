"""
van/spec/electrical.py
Three-domain electrical architecture for the GMC Savana 2500 expedition build.

Domain 1: Factory vehicle electrical
Domain 2: Auxiliary 12V DC system
Domain 3: 120V AC system
"""

PHILOSOPHY = (
    "Analog-first, hardwired, no internal wireless except Starlink "
    "(wired ethernet only). Three isolated electrical domains with "
    "no direct connection between Domain 1 (factory) and Domain 2 (aux). "
    "All systems field-serviceable. All connections labeled."
)

DOMAINS = {

    1: {
        "name":        "Factory Vehicle Electrical",
        "description": "OEM wiring, alternator, starter, factory fuse box. Untouched.",
        "connection":  "Isolated from Domain 2 via 40A inline fuse on the DC-DC charger input",
        "components": [
            "OEM alternator",
            "OEM starter and solenoid",
            "OEM fuse block",
            "Factory lighting and accessories",
        ],
    },

    2: {
        "name":        "Auxiliary 12V DC System",
        "description": "All van build 12V loads. Isolated from factory wiring.",
        "protection":  "300A ANL master fuse at the battery positive terminal",
        "components": {
            "Battery":      "400Ah LiFePO4 bank (Battle Born or equivalent)",
            "Bus":          "Victron Lynx Distributor",
            "Inverter":     "Victron MultiPlus 12/3000 — 250A DC breaker",
            "Solar MPPT":   "Victron SmartSolar MPPT 100/50",
            "DC-DC":        "Victron Orion-XS 12/12-30A — 60A ANL on output",
            "Wind":         "Primus AIR Silent X 440W — 30A DC breaker",
            "Distribution": "Blue Sea 12-circuit fused DC panel",
            "Monitoring":   "Victron SmartShunt 500A, SIMARINE PICO, TriMetric 2030",
        },
        "circuits": [
            {"id": 1,  "load": "OutEquipPro AC unit",         "fuse": "30A"},
            {"id": 2,  "load": "MaxxAir roof fan",            "fuse": "15A"},
            {"id": 3,  "load": "Dometic CFX3 fridge/freezer", "fuse": "20A"},
            {"id": 4,  "load": "Water pump",                  "fuse": "10A"},
            {"id": 5,  "load": "Lighting — interior",         "fuse": "10A"},
            {"id": 6,  "load": "Lighting — exterior",         "fuse": "15A"},
            {"id": 7,  "load": "Starlink ethernet adapter",   "fuse": "10A"},
            {"id": 8,  "load": "CB radio",                    "fuse": "10A"},
            {"id": 9,  "load": "Cameras — perimeter",         "fuse": "10A"},
            {"id": 10, "load": "Helm display station",        "fuse": "15A"},
            {"id": 11, "load": "USB charging — 12V outlets",  "fuse": "15A"},
            {"id": 12, "load": "Spare",                       "fuse": "20A"},
        ],
    },

    3: {
        "name":        "120V AC System",
        "description": "Shore power and inverter AC loads. No induction cooktop.",
        "panel":       "Blue Sea AC 4-circuit panel",
        "circuits": [
            {"id": 1, "load": "OutEquipPro AC unit (dedicated)", "breaker": "20A"},
            {"id": 2, "load": "General outlets — left side",     "breaker": "15A"},
            {"id": 3, "load": "General outlets — right side",    "breaker": "15A"},
            {"id": 4, "load": "Spare",                           "breaker": "20A"},
        ],
        "explicitly_excluded": [
            "Induction cooktop — no 240V and no high-draw cooking loads of any kind",
            "Electric water heater",
            "Any load over 20A continuous",
        ],
        "notes": (
            "The outdoor-only kitchen rule means no high-draw cooking appliances "
            "exist in Domain 3. The AC panel serves the AC unit, device charging, "
            "and laptop power only."
        ),
    },
}

LABELING = {
    "method": "Dymo label maker on all breakers and circuit positions",
    "directory": "Laminated circuit directory mounted adjacent to each panel",
    "cable_tags": "Heat-shrink labels at both ends of every conductor",
}

POWER_BUDGET = {
    "description": "Daily power budget for a typical summer camp day",
    "loads": [
        {"load": "Dometic CFX3 fridge — average",        "watts": 40,  "hours": 24, "wh": 960},
        {"load": "OutEquipPro AC — eco mode overnight",   "watts": 400, "hours": 5,  "wh": 2000},
        {"load": "Lighting, phones, laptop",              "watts": 50,  "hours": 4,  "wh": 200},
        {"load": "Water pump, misc",                      "watts": 20,  "hours": 0.5,"wh": 10},
    ],
    "total_with_ac_wh":     3170,
    "total_without_ac_wh":  1170,
    "usable_bank_wh":       3840,   # 400Ah × 12V × 80% DoD
    "solar_harvest_wh":     2700,   # 600W × 4.5 peak hours (Montana July)
    "alternator_wh_per_day": 600,   # Orion-XS 30A × 12V × ~1.7 hrs driving
    "notes": (
        "With AC running overnight, the bank will draw down and rely on the "
        "next morning's solar + driving to recover. On hot non-driving days "
        "at low elevation, deploy the remote 400W briefcase array. "
        "At elevation (Bighorns, Medicine Bow) AC is rarely needed and the "
        "bank easily maintains itself on solar alone."
    ),
}

# ── ELECTRONICS BAY — DOG HAIR FILTRATION ────────────────────────────────────

ELECTRONICS_BAY = {
    "description": (
        "Enclosed bay housing all Victron components. "
        "The MultiPlus 12/3000 has an internal cooling fan — the only component "
        "in the system that actively pulls air through itself. "
        "Without filtration, a husky in a sealed van will load the MultiPlus "
        "fan with hair within days. Dog hair on electronics is a thermal and "
        "reliability risk. The electronics bay is the solution."
    ),

    "risk_map": {
        "Victron MultiPlus 12/3000": {
            "cooling":    "Internal fan — actively pulls air through the unit",
            "risk":       "HIGH — fan draws dog hair into inverter/charger internals",
            "action":     "Filtered intake vent required",
        },
        "Victron SmartSolar MPPT 100/50": {
            "cooling":    "Passive heatsink only — no fan, no airflow through unit",
            "risk":       "Low — hair accumulates on fins but does not enter unit",
            "action":     "Enclosed bay ventilation sufficient; wipe fins periodically",
        },
        "Victron Orion-XS 12/12-30A": {
            "cooling":    "Passive heatsink",
            "risk":       "Low",
            "action":     "Enclosed bay ventilation sufficient",
        },
        "Victron Lynx Distributor": {
            "cooling":    "Passive",
            "risk":       "None",
            "action":     "None",
        },
        "Blue Sea panels": {
            "cooling":    "Passive",
            "risk":       "None",
            "action":     "None",
        },
        "LiFePO4 battery bank": {
            "cooling":    "Passive",
            "risk":       "None — batteries don't care about hair",
            "action":     "None",
        },
    },

    "bay_construction": {
        "material":     "3/4-inch plywood or aluminum panel — simple enclosure with removable door",
        "location":     "Forward of the sleep platform, against the driver-side bulkhead",
        "ventilation": {
            "intake":   "Low position on bay wall — filtered panel vent",
            "exhaust":  "High position on bay wall — unfiltered (exhaust, not intake)",
            "airflow":  "Natural convection — hot air rises, no powered fan required",
        },
    },

    "multiplus_filtration": {
        "method":       "Filtered intake cover over the MultiPlus fan intake grille",
        "filter_media": "Washable polyester foam filter media — same material as HVAC pre-filters",
        "hardware":     "Computer panel filter frame, 80mm or 120mm, fits over intake grille",
        "sources":      [
            "Comair Rotron panel filter — available on Amazon/Digikey, $8-15 each",
            "Or: pantyhose stretched over intake — field-proven, free, replaces in 30 seconds",
        ],
        "inspection":   "Every 30 days — with a husky in the van, expect fast loading",
        "replacement":  "Wash or replace filter media. Keep 3 spares on hand.",
        "spare_count":  3,
    },

    "thermal_note": (
        "Every 10°C rise in electronics temperature reduces component life by ~50% "
        "(Arrhenius equation). Dog hair blocking airflow is a direct thermal risk. "
        "The MultiPlus is the most sensitive component to hair accumulation. "
        "30-day filter inspection is a maintenance calendar item — not optional."
    ),

    "maintenance_schedule": {
        "monthly":    "Inspect and clean MultiPlus intake filter",
        "quarterly":  "Wipe MPPT and Orion heatsink fins",
        "annually":   "Full electronics bay inspection — check all connections for corrosion",
    },
}
