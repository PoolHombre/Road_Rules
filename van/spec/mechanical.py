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
            "Inspection": [
                "OBD-II diagnostic scan — document and clear all codes",
                "Visual inspection: frame for rust, exhaust for leaks, CV boots for cracking",
                "Tire inspection — tread depth, sidewall condition, date codes",
                "Check all fluid levels after service",
            ],
        },
        "notes": (
            "Do not skip Stage A. A used van with unknown service history is a liability. "
            "The cost of Stage A (~$450) is insurance against a breakdown in the Missouri Breaks "
            "with no cell service. "
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
