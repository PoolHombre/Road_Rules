"""
van/spec/stages.py
GMC Savana 2500 expedition build — all stages.

Build stages 1-4 cover the van conversion itself.
Mechanical stages A-E cover vehicle maintenance and upgrades.
Both are required before the van is expedition-ready.
"""

# ── VEHICLE ───────────────────────────────────────────────────────────────────

VEHICLE = {
    "make":       "GMC",
    "model":      "Savana 2500",
    "trim":       "Extended",
    "wheelbase":  "155 inches",
    "drivetrain": "RWD",
    "engine":     "6.0L Vortec V8",
    "notes":      (
        "RWD confirmed optimal over AWD/FWD for expedition use. "
        "Transmission and driveshaft layout provides superior ground clearance "
        "and field serviceability. No transaxle complexity."
    ),
}


# ── MECHANICAL STAGES (A–E) ───────────────────────────────────────────────────
# Complete before or during early build phases.
# Stage A and D are concurrent with Stage 1 build work.

MECHANICAL_STAGES = {

    "A": {
        "name":    "Immediate — Fluids, Filters, Ignition",
        "timing":  "On vehicle purchase — before any other work",
        "items": [
            "Engine oil + filter (full synthetic)",
            "Transmission fluid drain and fill",
            "Transfer case fluid (if applicable)",
            "Differential fluid (front and rear)",
            "Coolant flush and refill",
            "Power steering fluid",
            "Brake fluid flush",
            "Air filter (engine)",
            "Cabin air filter",
            "Spark plugs — iridium x8 (NGK or Denso)",
            "Serpentine belt inspection and replacement if needed",
            "All hoses — inspect for cracking, swelling, leaks",
            "Thermostat replacement (preventive)",
            "Water pump inspection",
            "PCV valve",
            "Fuel filter (if accessible)",
        ],
        "notes": "Do not skip. Unknown maintenance history on any used vehicle means full refresh.",
    },

    "B": {
        "name":    "Interim — Brakes and Engine Management",
        "timing":  "After Stage A, before heavy load testing",
        "items": [
            "OBD-II diagnostic scan — clear codes, document findings",
            "Brake pad replacement (stock hardware, interim)",
            "Brake shoe replacement (rear drums, interim)",
            "O2 sensors — replace upstream and downstream if original",
            "Mass airflow sensor cleaning or replacement",
            "Throttle body cleaning",
            "Fuel injector cleaning",
            "Battery load test and replacement if needed",
            "Alternator output test",
            "Inspect brake lines for rust or damage",
            "Parking brake adjustment",
        ],
        "notes": (
            "Interim brake work uses stock hardware. Stage C replaces all of this "
            "with the Wilwood 4-corner upgrade. Stage B keeps the van safe during "
            "the build period."
        ),
    },

    "C": {
        "name":    "Wilwood 4-Corner Brake Upgrade + Suspension",
        "timing":  "After Stage 1 build — when final van weight is known",
        "items": [
            # Brakes
            "Wilwood Dynalite front brake kit — 4-piston, 13-inch rotor",
            "Wilwood Dynapro rear drum-to-disc conversion — with integrated parking brake",
            "Stainless steel brake lines — full replacement front and rear",
            "Brake bias bar adjustment after installation",
            "Full brake bleed — fresh fluid throughout",
            # Suspension
            "Bilstein 5100 shocks — front and rear",
            "Add-a-leaf rear spring pack (account for van build weight)",
            "Polyurethane control arm bushings",
            "Sway bar end links",
            "Alignment after suspension work",
            # Transmission cooling
            "External transmission oil cooler — Derale or B&M",
        ],
        "notes": (
            "The Wilwood rear drum-to-disc conversion includes an integrated parking brake — "
            "this is the critical difference from simpler disc conversion kits. "
            "The parking brake must be functional for expedition use on grades. "
            "Do not install until Stage 1 build weight is finalized — "
            "spring rate and shock valving depend on loaded vehicle weight."
        ),
    },

    "D": {
        "name":    "Electrical Refresh + Ground Kit",
        "timing":  "Concurrent with Stage 1 build",
        "items": [
            # Factory grounds — 2/0 AWG welding cable throughout
            "Battery negative → engine block",
            "Engine block → chassis frame",
            "Battery negative → chassis frame",
            "Chassis frame → body (driver side)",
            "Chassis frame → body (passenger side)",
            "Alternator case → engine block",
            # Aux system grounds — Stage 1 build systems
            "LiFePO4 battery bank → ground bus bar",
            "Victron MultiPlus → ground bus bar",
            "Victron SmartSolar MPPT → ground bus bar",
            "Victron Orion-XS DC-DC → ground bus bar",
            "Blue Sea DC distribution panel → ground bus bar",
            "Helm display station → ground bus bar",
            "Blue Sea 2506 ground bus bar → chassis",
        ],
        "cable":  "2/0 AWG welding cable throughout. 4 AWG for smaller aux system connections.",
        "notes": (
            "Factory ground refreshes should be done before Stage 1 electrical work begins. "
            "A poor factory ground is the root cause of most electrical gremlins in van builds. "
            "The aux system ground bus bar (Blue Sea 2506) is the hub for all build system grounds."
        ),
    },

    "E": {
        "name":    "Post-Expedition Upgrades",
        "timing":  "After the first major trip — based on real-world experience",
        "items": [
            "High-output alternator — 200A (Nations Alternators or Mechman)",
            "Diesel parking heater — Webasto or Espar (Airtronic or Airtop)",
            "Limited slip differential — rear axle",
            "Roof-mounted solar upgrade if fixed array proves insufficient",
            "Additional battery capacity if power budget falls short",
        ],
        "notes": (
            "Stage E is intentionally deferred. The first major trip will reveal actual "
            "power consumption, heating needs, and traction limitations. "
            "Upgrade based on data, not speculation."
        ),
    },
}


# ── BUILD STAGES (1–4) ────────────────────────────────────────────────────────

BUILD_STAGES = {

    1: {
        "name":   "Stage 1A — Lightweight Living Infrastructure",
        "budget": 15800,
        "items": {
            "Insulation": [
                # Sound damping — bare metal panels
                "Noico 80mil butyl damping mat — all bare metal panels",
                "  · Same damping performance as Dynamat Extreme at 70% less cost and weight",
                "  · Adhesive-backed, partial coverage (resonant panels only, not every inch)",
                # Cavity fill — walls, ceiling, curved surfaces, doors
                "3M Thinsulate SM600L — all wall/ceiling cavities and door panels",
                "  · Hydrophobic — moisture passes through, does not trap or hold",
                "  · No vapor barrier needed — van metal is exterior-side vapor barrier",
                "  · Removable, inspectable, does not bond to metal",
                "  · 1.5 inch depth in cavities, 0.8 inch in doors and headliner",
                # Continuous thermal layer — walls and ceiling
                "XPS rigid foam board (pink/blue, e.g. Owens Corning Foamular) — walls and ceiling",
                "  · Replaces Polyiso — R-value stable at 25°F (Polyiso degrades to R3.5 in cold)",
                "  · 1-inch panels, cut to fit, friction-fit behind wall panels",
                "  · Fully removable — no adhesive to metal, no permanent bond",
                # Floor
                "XPS rigid foam board 1-inch — floor under horse mats",
                "  · High compressive strength — does not crush under load",
                "  · Sits loose on van floor, horse mats hold it in place",
                # Gap sealing — targeted only
                "Great Stuff Gaps and Cracks foam — void sealing only (targeted, not full spray)",
                "  · ONLY for: seam gaps between panels, penetrations, and irregular voids",
                "  · NOT applied continuously to van metal — spray foam is permanently bonded",
                "  · Full closed-cell spray foam application explicitly rejected:",
                "    - Bonds permanently to van metal — kills access to wiring and rust inspection",
                "    - Moisture trapped behind imperfect bonds causes hidden rust",
                "    - Body shops will not work behind spray-foamed panels",
            ],
            "Channel Grid — Reconfigurable Interior Framework": [
                "Aluminum Unistrut P1000T — 10 total runs (see van/spec/systems.py)",
                "Wall channels: 3 horizontal runs per side (Low 6\", Mid 20\", High 48\")",
                "Ceiling channels: 2 fore-aft runs (12\" from centerline each side)",
                "Floor channels: 2 fore-aft runs (6\" from each wall)",
                "All connections: stainless steel spring nuts, bolts, and washers",
                "Jute rope wrap on exposed Unistrut at contact height — edge protection",
            ],
            "Walls and Ceiling": [
                "3mm bamboo plywood panels — full wall and ceiling coverage",
                "Flexible bamboo slat cladding — accent panels",
                "ACP (aluminum composite panel) — water exposure zones",
                "Acoustic panels — echo control",
                "Rubio Monocoat — natural oil finish throughout",
                "Hemp canvas storage pockets — hung from high wall channel, repositionable",
            ],
            "Floor": [
                "2x rubber horse stall mats (4'x6', ~$90 Tractor Supply) — removable",
                "NO plywood subfloor — mats sit directly on van floor (lightweight first build)",
            ],
            "Sleep Platform": [
                "Unistrut perimeter frame with cross-members every 18 inches",
                "Four legs — drop into wall channel at Low or Mid position, no tools required",
                "Full-length — approximately 90 inches fore-aft, 48 inches wide",
                "1-inch natural hemp webbing grid — 4-inch spacing, dual purpose:",
                "  · Sleeping surface (with bamboo lyocell topper)",
                "  · Load tie-down grid — cam straps hook through webbing to secure crates",
                "Bamboo lyocell quilted topper — rolls up in cargo/chaise mode",
                "Configurations: Flat (sleep) / Chaise (head end raised 30 degrees) / Cargo (floor clear)",
                "NO DECKED drawer system — lightweight first build, floor storage is crates only",
            ],
            "Power": [
                "400Ah LiFePO4 battery bank (Battle Born or equivalent)",
                "Victron MultiPlus 12/3000 inverter/charger",
                "Victron SmartSolar MPPT 100/50",
                "Victron Orion-XS 12/12-30A DC-DC charger (alternator)",
                "Victron Lynx distributor bus",
                "Victron SmartShunt 500A",
                "Blue Sea 12-circuit fused DC panel",
                "Blue Sea AC 4-circuit panel",
                "Blue Sea 2506 ground bus bar",
                "300A ANL master fuse",
                "Shore power inlet — 30A",
            ],
            "Solar": [
                "2x 100W rigid panels — fixed roof mount",
                "2x Renogy 200W briefcase panels — remote deployable",
                "50-ft MC4 cables for remote array",
            ],
            "Wind Turbine Pre-Wire (Stage 1 only — install in Stage 3)": [
                "30A DC breaker — dedicated turbine circuit",
                "Anderson Powerpole connector",
                "Cable gland through roof",
                "~$95 total pre-wire cost",
            ],
            "Climate": [
                "OutEquipPro Summit 2 AC/heat — 10,000 BTU cool / 4,500 BTU heat",
                "12V DC rooftop unit — 6.3-inch profile, 45 lbs",
                "Wired thermostat — WiFi/app disabled (analog-first philosophy)",
                "MaxxAir roof fan — ventilation",
            ],
            "Water": [
                "30-gallon fresh water tank",
                "12V demand pump",
                "PEX plumbing with SharkBite fittings",
                "Exterior 3/4-inch ball valve + shore water fitting",
            ],
            "Sanitation": [
                "Composting toilet — Nature's Head or OGO",
                "Positioned behind driver seat, facing rearward",
                "Curtain on Unistrut slider for privacy",
                "12V vent fan",
            ],
            "Monitoring": [
                "SIMARINE PICO battery monitor",
                "TriMetric 2030 — secondary monitoring",
                "Belden shielded twisted pair cable — all signal runs",
                "4 organized cable bundles",
            ],
            "Communications": [
                "Cobra 29 LX CB radio",
                "Starlink Mini — wired ethernet only (WiFi disabled)",
                "Garmin inReach Mini 2 — satellite emergency communicator",
                "Neutrik chassis jacks — all external audio/data ports",
                "Amphenol connectors — field-serviceable throughout",
            ],
            "Lighting — 5 Zones (see van/spec/systems.py for full detail)": [
                "Zone 1 AMBIENT: LED strip 2700K warm white, both ceiling channels, frosted diffuser",
                "Zone 2 READING: 2x adjustable LED puck lights on high wall channel at bed head",
                "Zone 3 WORK: LED strip 4000K neutral white, mid wall channel both sides",
                "Zone 4 NIGHT: Red LED strip, low floor channel port side — preserves night vision",
                "Zone 5 EXTERIOR: 2x weatherproof LED puck lights above rear doors",
                "Control panel: analog rockers near side door — MASTER + 5 zone switches",
                "MASTER cutoff: large rocker, kills all lighting circuits — top of panel",
            ],
            "Load Securing": [
                "Ceiling hardpoints: 4x through-bolted structural points above crate zone",
                "  · Through-bolt to van roof ribs — NOT channel-only",
                "  · Stainless 3/8\" bolts + backing plates + rubber weatherstrip seal",
                "  · Position TBD — finalize after walls are up",
                "Crate securing: cam straps through hemp webbing grid — no loose loads while moving",
                "Crate selection TBD — Pelican 1650-class or equivalent, hard-sided, stackable",
            ],
            "Natural Fiber Accents": [
                "Jute rope wrap on exposed Unistrut at contact height",
                "Hemp canvas toilet privacy curtain on Unistrut slider",
                "Linen diffuser shades on Zone 2 reading puck lights",
                "Hemp canvas side door privacy curtain — tension rod, removable",
                "Hemp canvas storage pockets — hung from high wall channel",
            ],
        },
        "deferred_to_later_stage": [
            "DECKED VG2 drawer system (~200-275 lbs, $1,850) — heavyweight fixed storage, "
            "deferred until first expedition reveals actual storage needs",
            "Plywood subfloor ($85, ~40 lbs) — horse mats sit directly on van floor",
        ],
        "notes": (
            "Stage 1A is the lightweight-first build. The channel grid (Unistrut) is the "
            "reconfigurable skeleton — everything attaches to it, nothing is fixed permanently. "
            "The hemp webbing platform serves as both sleeping surface and load tie-down grid. "
            "Heavy fixed storage (DECKED) is deferred until after the first expedition. "
            "The wind turbine pre-wire costs $95 and saves hours of rework in Stage 3. "
            "Ceiling hardpoints are structural through-bolts to van roof ribs — not channel-only. "
            "Crate position finalized after walls are up and interior is experienced in person."
        ),
    },

    2: {
        "name":   "Safety and Expedition Equipment",
        "budget": 6550,
        "cumulative_budget": 24665,
        "items": {
            "Bumper and Winch": [
                "Aluminess front winch bumper",
                "Warn VR EVO 12-S winch — 12,000 lb capacity",
            ],
            "Lighting": [
                "Baja Designs driving lights",
                "Rigid Industries flood lights",
                "40-inch LED light bar",
            ],
            "Recovery": [
                "Bubba Rope kinetic recovery rope",
                "Factor 55 FlatLink shackle",
                "MAXTRAX recovery boards (x2)",
                "Hi-Lift jack with base plate",
                "Snatch block and rigging kit",
            ],
            "Security and Surveillance": [
                "IR thermal camera — exterior front",
                "4x IR perimeter cameras — all corners, wired (no WiFi)",
                "Vaultek LifePod 2.0 — handgun safe",
                "SecureIt Fast Box Model 40 — rifle/long gun",
            ],
        },
        "notes": (
            "All cameras are wired — no wireless transmission. "
            "Security is hardened, not convenient. "
            "The winch bumper is the first Aluminess piece installed — "
            "the roof rack and storage box come in Stage 3."
        ),
    },

    3: {
        "name":   "Kitchen, Comfort, Dogs, Wind",
        "budget": 9092,
        "cumulative_budget": 33757,
        "items": {
            "Wind Turbine (ORDER FIRST — 4-6 week lead time)": [
                "Primus AIR Silent X 440W wind turbine",
                "Primus 27-ft tilt-up guyed tower kit",
                "Primus Digital Control Panel",
                "Mast sections storage: weatherproof vinyl bag, passenger-side rack rail",
                "Turbine body and blade bag: Aluminess roof box",
            ],
            "Roof and Exterior": [
                "Aluminess roof rack",
                "Aluminess deluxe storage box (turbine body storage)",
                # Awning system — full three-side coverage (see VAN-019)
                "Alu-Cab 270° Shadow Awning — RHS (passenger side)",
                "  · Covers rear barn doors + full passenger side simultaneously",
                "  · 10 m² (107 sq ft) shade, 315gsm polyester, 600mm water column",
                "  · Deploys in 45 seconds, one person, no poles, no guy wires",
                "  · Four heavy-duty aluminum arms, freestanding",
                "  · Silver reflective coating — noticeable temperature drop underneath",
                "  · Mounts to Aluminess roof rack via universal load bar brackets",
                "Roam or OVS HD Nomadic 180° awning — LHS (driver side)",
                "  · Covers driver side independently",
                "  · Deployed with the 270° RHS: full rear + both sides covered",
                "  · Each awning deploys independently — use one or both as needed",
                "  · Mounts to front section of Aluminess roof rack, driver side",
                "Alu-Cab Shower Cube",
                "  · Mounts to RHS roof rack brackets adjacent to the 270° awning",
                "  · 9kg aluminum + stainless construction, quick-drying Taffeta fabric",
                "  · Open: 43\" L × 36\" W × 74-94\" H (adjustable height)",
                "  · Closed: 41\" L × 4.7\" W × 7.4\" H — compact stowed profile",
                "  · Use as: shower room, changing room, privacy room, toilet enclosure",
                "  · Locking arms for wind stability, dual-side zipper entry",
                "  · Shower water: gravity bag + 12V pump from 30-gal tank",
            ],
            "Refrigeration": [
                "Dometic CFX3 45L compressor fridge/freezer",
            ],
            "Kitchen — Outdoor Only": [
                "Coleman 2-burner propane stove",
                "Lodge cast iron skillet (12-inch)",
                "Lodge cast iron griddle",
                "Lodge cast iron Dutch oven (6-quart)",
                "Lodge cast iron stovetop waffle iron",
                "Jetboil Flash backpacking stove — backup",
                "Instant Pot Duo Mini 3-quart",
                "Vitamix 5-speed immersion blender",
                "Citrus juicer",
                "Mandoline slicer",
            ],
            "Kitchen — Explicitly NOT Included": [
                "NO induction cooktop — outdoor cooking only, no exceptions",
                "NO toaster",
                "NO K-cup or pod coffee maker",
                "NO countertop blender",
            ],
            "Dog Systems": [
                "Gunner Kennel G1 — Tango (husky, ADA service animal)",
                "Sleepypod Mobile Pet Bed — Saki (schnauzer, ESA)",
                "Ruffwear harnesses — both dogs",
                "Adaptil DAP spray — calming",
                "Through a Dog's Ear playlist — van audio",
                "Vittles Vault airtight food storage",
                "K9 Sport Sack carrier — Saki",
                "Musher's Secret paw protection wax",
                "Canine first aid kit",
                "Dog booties — hot surface protection",
                "Water bowls — collapsible x3",
            ],
        },
        "notes": (
            "ORDER THE PRIMUS AIR SILENT X TURBINE FIRST. "
            "Lead time is 4-6 weeks and it gates the rest of Stage 3. "
            "The outdoor-only kitchen rule is permanent and non-negotiable. "
            "The van has no interior cooking — no exceptions."
        ),
    },

    4: {
        "name":   "Dual Display System (Phase 2)",
        "budget": 2500,
        "cumulative_budget": 36257,
        "items": {
            "Hardware": [
                "Industrial fanless PC — ruggedized",
                "Custom PCB — sensor integration",
                "Helm display — passenger side dash (diagnostics, nav)",
                "Engineering display — cargo area (systems monitoring)",
            ],
            "Capability": [
                "Full vehicle diagnostics on both displays",
                "Credential authentication required for configuration changes",
                "Both displays capable of full system view",
                "Wired throughout — no wireless",
            ],
        },
        "notes": (
            "Stage 4 is Phase 2 of the build — deferred until after the first expedition. "
            "The pre-wire for both display stations is completed in Stage 1. "
            "Install Stage 4 after real-world use reveals actual monitoring needs."
        ),
    },
}


# ── EXTERIOR WRAP ─────────────────────────────────────────────────────────────

EXTERIOR = {
    "wrap_timing": "LAST — after all hardware is installed. Never before.",
    "budget_range": "$7,000 – $8,000",
    "material": "Avery Dennison SW900 series",
    "zones": {
        "upper": {
            "area":    "Roof and upper body",
            "color":   "ColorFlow Gloss Fresh Spring (252-S)",
            "effect":  "Blue-green color-shift depending on viewing angle",
        },
        "mid": {
            "area":    "Mid body",
            "color":   "SW900 Satin Khaki Green",
            "effect":  "Matte sage green",
        },
        "lower": {
            "area":    "Lower body, rocker panels",
            "color":   "SW900 Matte Adobe",
            "effect":  "Matte earth tone",
        },
    },
    "easter_eggs": [
        {"subject": "Sea turtle",         "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Eagle",              "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Bison",              "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Saguaro cactus",     "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Wave form",          "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Mountain silhouette","style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Wolf",               "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
        {"subject": "Single star",        "style": "petroglyph/sumi-e", "size": "2-4 inches", "color": "monochromatic"},
    ],
    "ppf": "Paint protection film — front fascia, lower body, rocker panels",
    "artist_commission": "$300 – $600 for vector art files",
    "notes": (
        "Eight Easter eggs embedded in the wrap. All are monochromatic, 2-4 inches, "
        "in petroglyph or sumi-e style — subtle enough that only close inspection reveals them. "
        "The vector art must be commissioned before the wrap shop appointment."
    ),
}


# ── BUDGET SUMMARY ────────────────────────────────────────────────────────────

BUDGET = {
    "vehicle_purchase":       12000,
    "stage_1":                15800,  # Stage 1A — lightweight first build (was 18115, DECKED and subfloor removed)
    "stage_2":                 6550,
    "stage_3":                 9092,
    "stage_4":                 2500,
    "exterior_wrap_low":       7000,
    "exterior_wrap_high":      8000,
    "mechanical_stages_AE":    4500,  # estimated
}


def cumulative_budget(through_stage: int, include_vehicle=True) -> int:
    total = BUDGET["vehicle_purchase"] if include_vehicle else 0
    for s in range(1, through_stage + 1):
        total += BUILD_STAGES[s]["budget"]
    return total
