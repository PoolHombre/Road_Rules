"""
van/spec/mechanical.py
Detailed mechanical stage specifications for the GMC Savana 2500 expedition build.

Five stages covering vehicle purchase through post-expedition upgrades.
Stage C (Wilwood brakes) is gated on Stage 1 loaded weight — see van/data/weight.py.
"""

PHILOSOPHY = (
    "The van must be mechanically sound before any build work begins. "
    "Unknown maintenance history on any used vehicle means full refresh at purchase. "
    "Stage B interim brakes keep the van safe during the build period. "
    "Stage C replaces the entire brake system with the Wilwood upgrade after the "
    "build weight is known. Never spec Stage C from estimated weights."
)

STAGES = {

    "A": {
        "name":    "Immediate — Fluids, Filters, Ignition",
        "timing":  "On vehicle purchase — before any other work begins",
        "status":  "planned",
        "items": {
            "Engine": [
                "Engine oil + filter — full synthetic (Mobil 1 or equivalent)",
                "Air filter — K&N reusable or OEM replacement",
                "PCV valve",
                "Spark plugs — NGK Iridium or Denso iridium x8 (6.0L Vortec)",
                "Serpentine belt — inspect and replace if any cracking or glazing",
                "Thermostat — replace preventively regardless of condition",
            ],
            "Cooling": [
                "Coolant flush — drain fully, flush with distilled water, refill with fresh Dex-Cool",
                "Hoses — inspect all upper and lower radiator hoses for cracking, swelling, or soft spots",
                "Water pump — inspect weep hole for evidence of leakage; replace if any sign",
                "Radiator cap — replace preventively (~$8, eliminates a failure mode)",
            ],
            "Transmission": [
                "4L80-E transmission fluid drain and fill — full synthetic Dexron VI",
                "Transmission filter — replace if pan is dropped (do if unknown history)",
            ],
            "Differentials": [
                "Rear differential fluid drain and fill — 75W-90 full synthetic GL-5",
                "Transfer case fluid — if applicable (RWD Savana: confirm no t-case)",
            ],
            "Brakes": [
                "Brake fluid flush — DOT 3 or DOT 4, full system bleed",
                "Parking brake cable — inspect for fraying and free movement",
            ],
            "Other Fluids": [
                "Power steering fluid — flush and refill",
                "Windshield washer fluid",
            ],
            "Electrical": [
                "Battery — load test; replace if below 80% capacity",
                "Battery terminals — clean corrosion, apply dielectric grease",
                "All lights — inspect and replace any failed bulbs",
            ],
            "AFM Disable — PRIORITY ITEM": [
                "Range Technology AFM Disabler (Model A10B) — plug into OBD-II port, done",
                "  · Cost: ~$120. Eliminates AFM cylinder deactivation permanently",
                "  · AFM is the primary cause of oil consumption on the 6.0L Vortec",
                "  · Without disable: lifter failures, oil burning, fouled spark plugs at 100k+",
                "  · With disable: engine runs all 8 cylinders all the time — correct for load use",
                "  · Passive device — unplugs in seconds, leaves no trace, does not void warranty",
                "  · Alternative: HP Tuners or EFILive tune to disable AFM in ECU permanently",
                "  · DO THIS BEFORE THE FIRST DRIVE. Do not run the AFM system at all.",
            ],
            "Inspection": [
                "OBD-II diagnostic scan — document and clear all codes",
                "Visual inspection: frame for rust, exhaust for leaks, CV boots for cracking",
                "Tire inspection — tread depth, sidewall condition, date codes",
                "Check all fluid levels after service",
            ],
        },
        "notes": (
            "Do not skip Stage A. A used van with unknown service history is a liability. "
            "The AFM disable is the single most important item — do it before the first drive. "
            "The cost of Stage A (~$570 including AFM disabler) is insurance against a breakdown "
            "in the Missouri Breaks with no cell service. "
            "Document every service with receipts and mileage. Start the maintenance log."
        ),
    },

    "B": {
        "name":    "Interim — Brakes and Engine Management",
        "timing":  "After Stage A, before heavy load testing or build work begins",
        "status":  "planned",
        "items": {
            "Brakes — Interim (replaced in Stage C)": [
                "Front brake pads — OEM spec, Akebono ProACT or equivalent",
                "Front brake rotors — replace if worn below spec or showing deep grooves",
                "Rear brake shoes — OEM spec replacement",
                "Rear brake drums — inspect for scoring; replace if over max diameter",
                "Brake lines — inspect full run from master cylinder to each wheel for rust, damage",
                "Brake hoses — inspect all four corners for cracking or swelling",
                "Parking brake adjustment — ensure full engagement",
            ],
            "Engine Management": [
                "O2 sensors — replace upstream and downstream if original (4 sensors on 6.0L V8)",
                "Mass airflow sensor — clean with MAF cleaner; replace if readings erratic",
                "Throttle body — clean with throttle body cleaner",
                "Fuel injectors — add Techron concentrate to first tank",
                "EGR valve — inspect for carbon buildup; clean or replace",
            ],
            "Diagnosis": [
                "Clear all OBD-II codes after repair",
                "Road test under load — confirm no new codes",
                "Listen for: exhaust leaks, suspension noise, transmission hesitation",
            ],
        },
        "notes": (
            "Stage B interim brakes use OEM-spec hardware. "
            "These are replaced entirely by the Wilwood Stage C upgrade. "
            "Stage B exists only to keep the van safe during the build period — "
            "do not invest in premium rotors or pads here."
        ),
    },

    "C": {
        "name":    "Wilwood 4-Corner Brake Upgrade + Suspension",
        "timing":  "After Stage 1 build — when actual loaded weight is confirmed",
        "status":  "pending_weight",
        "gate":    "CANNOT BE SPECCED UNTIL STAGE 1 LOADED WEIGHT IS KNOWN. See van/data/weight.py.",
        "items": {
            "Brakes — Front": [
                "Wilwood Dynalite front brake kit — 4-piston, 13-inch rotor",
                "Stainless steel brake lines — front axle",
                "Wilwood brake fluid — DOT 4 or DOT 5.1",
            ],
            "Brakes — Rear": [
                "Wilwood Dynapro rear drum-to-disc conversion",
                "MUST INCLUDE integrated parking brake — specify explicitly when ordering",
                "Stainless steel brake lines — rear axle",
            ],
            "Brake System": [
                "Full system bleed — fresh fluid throughout",
                "Brake bias adjustment — front/rear balance after installation",
                "Road test under controlled conditions before loaded testing",
            ],
            "Suspension": [
                "Bilstein 5100 shocks — front pair (valving spec requires loaded weight)",
                "Bilstein 5100 shocks — rear pair (valving spec requires loaded weight)",
                "Add-a-leaf rear spring pack — number of leaves determined by loaded rear axle weight",
                "Polyurethane control arm bushings — Energy Suspension or Prothane",
                "Sway bar end links — heavy duty",
                "Front alignment after all suspension work",
            ],
            "Transmission Cooling": [
                "External transmission oil cooler — Derale Series 8000 or B&M SuperCooler",
                "Install in front of radiator, in-series with existing cooler",
            ],
        },
        "how_to_spec": (
            "1. Complete Stage 1 build fully. "
            "2. Load van with full operational gear (see van/data/weight.py). "
            "3. Weigh at CAT Scale — get front axle, rear axle, and total. "
            "4. Bring the rear axle weight to Wilwood tech line (805-388-1188) for brake spec. "
            "5. Bring loaded weight to Bilstein for shock valving recommendation. "
            "6. Specify number of add-a-leaf springs based on rear sag measurement. "
        ),
        "notes": (
            "The Wilwood Dynapro rear drum-to-disc conversion must include the "
            "integrated parking brake — this is the critical difference from simpler "
            "conversion kits. The parking brake must be functional for expedition use "
            "on mountain grades. Confirm parking brake integration explicitly with Wilwood "
            "before ordering."
        ),
    },

    "D": {
        "name":    "Ground Kit — Factory and Build Systems",
        "timing":  "Factory grounds concurrent with Stage A. Build system grounds concurrent with Stage 1.",
        "status":  "planned",
        "items": {
            "Factory Ground Refresh (Stage A timing)": [
                "Battery negative → engine block — 2/0 AWG welding cable",
                "Engine block → chassis frame — 2/0 AWG welding cable",
                "Battery negative → chassis frame — 2/0 AWG welding cable",
                "Chassis frame → body driver side — 2/0 AWG welding cable",
                "Chassis frame → body passenger side — 2/0 AWG welding cable",
                "Alternator case → engine block — 2/0 AWG welding cable",
            ],
            "Build System Grounds (Stage 1 timing)": [
                "LiFePO4 battery bank → Blue Sea 2506 ground bus bar — 2/0 AWG",
                "Victron MultiPlus → ground bus bar — 2/0 AWG",
                "Victron SmartSolar MPPT → ground bus bar — 4 AWG",
                "Victron Orion-XS DC-DC → ground bus bar — 4 AWG",
                "Blue Sea DC panel → ground bus bar — 4 AWG",
                "Blue Sea AC panel → ground bus bar — 4 AWG",
                "Blue Sea 2506 ground bus bar → chassis — 2/0 AWG",
            ],
            "Materials": [
                "2/0 AWG welding cable — 100 ft minimum (flexible, more than OFC wire)",
                "4 AWG stranded wire — for smaller aux system connections",
                "Heat shrink terminals — ring type, appropriate gauge for each wire",
                "Dielectric grease — all ground connections",
            ],
        },
        "notes": (
            "Poor factory grounds are the root cause of most electrical gremlins in van builds. "
            "The factory grounds are 30+ year old crimped connections that corrode and loosen. "
            "Replace all of them before building the aux electrical system. "
            "The Blue Sea 2506 ground bus bar is the hub for all build system grounds — "
            "it connects to the chassis via a single large 2/0 AWG cable, keeping "
            "all aux system grounds clean and organized."
        ),
    },

    "E": {
        "name":    "Post-Expedition Upgrades",
        "timing":  "After the first major expedition — based on real-world data",
        "status":  "deferred",
        "items": {
            "Alternator": [
                "High-output alternator — 200A minimum",
                "Nations Alternators or Mechman recommended",
                "Install with upgraded alternator to battery cable — 2/0 AWG minimum",
            ],
            "Heating": [
                "Diesel parking heater — Webasto Airtop 2000 STC or Espar Airtronic D2",
                "Install in driver side floor area with roof exhaust",
                "Fuel tap from main fuel tank — 3/8\" line",
                "Shore power bypass for programming — wired connection only",
            ],
            "Traction": [
                "Limited slip differential — Eaton Truetrac or ARB Air Locker for rear axle",
                "Air compressor for ARB locker if that route chosen",
            ],
            "Power": [
                "Additional battery capacity if power budget proves insufficient",
                "Roof solar upgrade if fixed array proves inadequate",
            ],
        },
        "notes": (
            "Stage E is intentionally deferred. The first major expedition will reveal "
            "actual power consumption patterns, heating needs in cold weather, and "
            "any traction limitations in the field. "
            "Upgrade based on real experience, not speculation. "
            "The diesel heater in particular should wait — the OutEquipPro AC unit "
            "provides heat down to approximately 32°F, which may be sufficient for "
            "the first expedition. Only add diesel heat if the AC heating proves "
            "inadequate for the actual use case."
        ),
    },
}

# ── PLATFORM RATIONALE ────────────────────────────────────────────────────────

PLATFORM_RATIONALE = {
    "vehicle":   "GMC Savana 2500 Extended, 155-inch wheelbase, RWD",
    "engine":    "6.0L Vortec V8 (L96)",
    "decision":  "2026-08",

    "why_savana_over_alternatives": {
        "core_argument": (
            "For a 28-day expedition through rural Montana, North Dakota, and Wyoming, "
            "the decisive question is not which van is most sophisticated. "
            "It is which van a small-town mechanic with a standard parts truck can fix "
            "by morning when something goes wrong at 9pm outside Miles City. "
            "The answer is the Savana every time."
        ),
        "vs_ford_transit": (
            "Transit is a capable platform with a proper high roof — the main thing "
            "the Savana lacks. The 3.7L naturally aspirated V6 is the reliable engine choice "
            "on the Transit; the EcoBoost turbo adds power but also turbo replacement risk "
            "documented by fleet mechanics. Ford has 2,991 dealers nationwide — good coverage. "
            "The Transit 3.7L is genuinely underpowered in a loaded extended van at elevation "
            "on Montana passes. Not a dealbreaker but a real consideration. "
            "The Savana wins on simplicity, payload capacity, and parts ubiquity."
        ),
        "vs_mercedes_sprinter": (
            "The Sprinter diesel reaches 300,000-400,000 miles and is the dream platform "
            "for full-time van life. But only 277 Mercedes van dealers nationwide. "
            "Real-world consequence: owners in rural areas drive 2-3 hours each way to a "
            "dealer for repairs, waiting days or weeks for European parts. "
            "In the Missouri Breaks or on the Rocky Mountain Front, the nearest Sprinter "
            "capable shop could be 200+ miles away. "
            "The Sprinter is not the wrong van. It is the wrong van for this specific use case."
        ),
        "savana_advantages": [
            "6.0L Vortec is the same engine block used in Silverado HD trucks — any shop in America knows it",
            "Parts available at every AutoZone, NAPA, O'Reilly, and Rock Auto in the country",
            "Architecture unchanged since 1996 — mechanics who worked on it in 2000 can work on it today",
            "Cast-iron block, pushrod V8, no turbo, no DEF, no AdBlue — minimum failure modes",
            "Shared drivetrain with GM HD trucks — enormous used parts ecosystem",
            "Highest payload capacity of the three platforms",
            "Lowest purchase price used — more budget for the build",
        ],
        "savana_disadvantages": [
            "No high roof — must crawl in (significant quality-of-life compromise)",
            "Fuel economy: 12-14 mpg loaded — worst of the three platforms",
            "No AWD available after 2014 — RWD only on modern examples",
            "Interior width slightly narrower than Transit or Sprinter",
            "No standing room — limits certain build configurations",
        ],
    },

    "why_60_vortec": (
        "The L96 6.0L Vortec is overbuilt for its application. "
        "Cast-iron cylinder block with 6-bolt main bearing caps, heavy-duty timing chain "
        "validated for 200,000 miles, LS engine architecture shared with the Corvette and Camaro. "
        "These engines routinely reach 300,000+ miles with proper maintenance. "
        "The primary reliability risk is the AFM (Active Fuel Management) cylinder deactivation "
        "system — which is eliminated with a $120 plug-in disabler at purchase."
    ),
}

# ── 6.0L VORTEC KNOWN ISSUES AND PURCHASE CHECKLIST ─────────────────────────

L96_KNOWN_ISSUES = {
    "priority_1_afm": {
        "issue":      "Active Fuel Management (AFM) — cylinder deactivation",
        "severity":   "HIGH — address immediately at purchase",
        "symptoms":   [
            "Oil consumption — 1+ quart per 1,000-2,000 miles",
            "Lifter failures — ticking, misfires, rough idle",
            "Fouled spark plugs from oil burning",
            "Check engine light with cylinder misfire codes",
        ],
        "cause": (
            "AFM deactivates cylinders 1, 4, 6, 7 at light throttle to save fuel. "
            "The collapsing lifters used for AFM are a known failure point. "
            "Oil consumption accelerates as rings wear from the constant activation/deactivation. "
            "This is GM's most documented reliability issue on the 6.0L platform."
        ),
        "fix": (
            "Range Technology AFM Disabler (Model A10B) — $120, plug-and-play OBD-II device. "
            "Disables AFM permanently without touching the ECU. "
            "Passive device — unplugs in seconds, leaves no ECU trace. "
            "Alternative: ECU tune via HP Tuners or EFILive — permanent, no dongle required. "
            "DO THIS BEFORE THE FIRST DRIVE."
        ),
        "prevention": "Disable AFM at purchase. Use full synthetic oil. Change at 5,000 miles max.",
    },

    "priority_2_oil_consumption": {
        "issue":    "Excessive oil consumption (high-mileage examples)",
        "severity": "MEDIUM — monitor closely",
        "symptoms": ["Burning more than 1 qt per 3,000 miles", "Blue smoke at startup", "Fouled plugs"],
        "cause":    "Worn piston rings (often AFM-related), clogged PCV valve, valve stem seals",
        "fix":      "PCV valve replacement ($15), fresh oil every 5,000 miles, monitor consumption. If rings are the cause, engine rebuild or replacement.",
        "purchase_check": "Ask seller: 'How often do you add oil between changes?' Any answer over 1 quart per 5,000 miles is a red flag.",
    },

    "priority_3_throttle_body": {
        "issue":    "Throttle body sensor failure",
        "severity": "LOW-MEDIUM — common, cheap fix",
        "symptoms": ["Surging idle", "Reduced power mode", "Hesitation on acceleration", "Check engine light"],
        "fix":      "Throttle body cleaning ($15 DIY) or replacement ($80-200). Easy job.",
        "purchase_check": "Scan for codes before purchase. P0121-P0123 are throttle position sensor codes.",
    },

    "priority_4_knock_sensors": {
        "issue":    "Knock sensor failure",
        "severity": "LOW — symptoms only under load",
        "symptoms": ["Check engine codes P0327/P0332", "Retarded timing under load", "Slight power loss"],
        "cause":    "Sensors mounted under the intake manifold — exposed to heat cycling",
        "fix":      "Replacement requires intake removal. $200-400 at a shop. Not difficult DIY.",
        "purchase_check": "Scan for P0327/P0332 codes. If present, factor repair cost into offer.",
    },

    "priority_5_exhaust_manifold": {
        "issue":    "Exhaust manifold gasket leaks / cracked manifolds",
        "severity": "MEDIUM — ticking sound, fumes risk",
        "symptoms": ["Ticking sound at startup (disappears when warm)", "Exhaust smell in cab", "Visible soot near exhaust ports"],
        "fix":      "Manifold gasket replacement ($150-300 parts + labor). Manifold replacement if cracked.",
        "purchase_check": "Listen for ticking at cold start. Inspect manifold studs for rust/breaks.",
    },

    "priority_6_water_pump": {
        "issue":    "Water pump failure",
        "severity": "MEDIUM — preventive replacement warranted",
        "symptoms": ["Coolant leak from weep hole", "Overheating", "Bearing noise"],
        "fix":      "Water pump replacement — Stage A preventive item if original. $100-200 DIY.",
        "purchase_check": "Check for evidence of coolant leaks around the pump. Check coolant color and condition.",
    },
}

# ── PRE-PURCHASE INSPECTION CHECKLIST ────────────────────────────────────────

PURCHASE_INSPECTION = {
    "must_do_before_buying": [
        "OBD-II scan — document every stored and pending code before negotiating",
        "Oil check — pull dipstick: color (should be amber, not black), level, any milkiness (head gasket)",
        "Coolant check — color (orange Dex-Cool), level, no oily sheen (head gasket)",
        "Cold start — listen for: AFM tick, exhaust manifold tick, lifter noise, knocking",
        "Full throttle test — brief, listen for knock or hesitation, watch for smoke",
        "Transmission — smooth shifts through all gears, no slipping, no shudder",
        "Frame inspection — lie under the van, look for rust, cracks, bent sections",
        "Ask oil change interval and last change date — sellers who don't know are red flags",
        "Ask about AFM oil consumption specifically: 'Does it burn oil between changes?'",
        "Carfax and service records — verify claimed maintenance history",
    ],
    "target_mileage":     "80,000 – 120,000 miles",
    "target_year":        "2010-2019 (post-AFM introduction, pre-end of Vortec production)",
    "red_flags": [
        "Any misfire codes (P030x) — lifter or AFM failure likely",
        "Oil consumption over 1 quart per 3,000 miles",
        "Milky oil or coolant — head gasket failure",
        "Frame rust in Texas is rare but check rear sections and crossmembers",
        "Unknown service history with high mileage",
        "Previous fleet use with deferred maintenance (check fleet decal ghosts)",
    ],
    "price_target":       "$10,000 – $15,000 for a clean example in target mileage range",
    "negotiation_note": (
        "Any code or known issue found in the inspection is a negotiating point. "
        "AFM lifter noise means a future repair of $1,500-3,000 — deduct accordingly. "
        "A clean van at $13,000 is better than a questionable van at $10,000."
    ),
}
