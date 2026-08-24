"""
van/changelog.py
Every significant van build decision, what was decided, and why.
Append new entries at the bottom. Never delete existing entries.
"""

CHANGELOG = [

    {
        "id":       "VAN-001",
        "date":     "2026-08",
        "decision": "Platform — GMC Savana 2500 Extended, RWD, 155-inch wheelbase",
        "reason": (
            "RWD confirmed superior to AWD/FWD for expedition use. "
            "Transmission and driveshaft layout provides superior ground clearance "
            "and field serviceability. No transaxle complexity. "
            "Extended wheelbase (155 in) provides maximum cargo length for the DECKED system "
            "and sleep platform while remaining under the critical vehicle length thresholds "
            "for Going-to-the-Sun Road (21 feet)."
        ),
        "alternatives_considered": [
            "Ford Transit AWD — rejected: transaxle reduces ground clearance and serviceability",
            "Mercedes Sprinter 4x4 — rejected: parts availability in remote areas",
            "Ram ProMaster — rejected: FWD only, wrong for expedition use",
        ],
    },

    {
        "id":       "VAN-002",
        "date":     "2026-08",
        "decision": "Power system — Victron ecosystem, 400Ah LiFePO4, dual solar",
        "reason": (
            "Victron is the industry standard for serious off-grid builds. "
            "The ecosystem (MultiPlus, SmartSolar, Orion-XS, Lynx, SmartShunt) "
            "integrates natively and provides detailed monitoring. "
            "400Ah provides 3,840Wh usable at 80% DoD — sufficient for AC overnight "
            "with next-day solar recovery on driving days. "
            "Dual solar (200W fixed + 400W deployable briefcase) covers stationary camp days."
        ),
        "alternatives_considered": [
            "Renogy system — rejected: less integration, weaker monitoring",
            "Battleborn BMS only — rejected: no ecosystem monitoring",
        ],
    },

    {
        "id":       "VAN-003",
        "date":     "2026-08",
        "decision": "AC — OutEquipPro Summit 2 only. WiFi disabled. Wired thermostat only.",
        "reason": (
            "The Summit 2 is a purpose-built 12V DC rooftop unit at 6.3-inch profile and 45 lbs. "
            "It is the only AC unit in the build — no secondary unit, no diesel heater in Phase 1. "
            "WiFi and app connectivity are disabled per the analog-first philosophy. "
            "Wired thermostat provides reliable control without wireless dependency."
        ),
        "alternatives_considered": [
            "Zero Breeze Mark 2 — rejected: insufficient BTU for a van this size",
            "Webasto diesel heater as primary climate — deferred to Stage E",
        ],
    },

    {
        "id":       "VAN-004",
        "date":     "2026-08",
        "decision": "Outdoor kitchen only. No induction cooktop. No interior cooking of any kind.",
        "reason": (
            "Cooking indoors in a sealed van creates moisture, odor, fire risk, and CO risk. "
            "The outdoor-only kitchen rule eliminates all of these. "
            "The Coleman 2-burner, cast iron, and Dutch oven handle everything needed. "
            "This rule is permanent and non-negotiable."
        ),
        "explicitly_excluded": [
            "Induction cooktop",
            "Propane burner inside the van",
            "Toaster",
            "K-cup / pod coffee maker",
            "Countertop blender",
        ],
    },

    {
        "id":       "VAN-005",
        "date":     "2026-08",
        "decision": "Wind turbine — Primus AIR Silent X 440W on 27-ft tilt-up guyed tower. Pre-wire Stage 1, install Stage 3.",
        "reason": (
            "The Primus AIR Silent X is rated for low wind speeds and produces meaningful power "
            "in 8-12 mph winds common at elevated camp sites (Bighorns, Medicine Bow, Montana). "
            "The 27-ft tilt-up guyed tower deploys and stows in under 30 minutes by one person. "
            "Pre-wiring in Stage 1 costs ~$95 and saves hours of rework in Stage 3. "
            "Mast sections stow in a weatherproof vinyl bag on the passenger-side rack rail. "
            "Turbine body and blade bag store in the Aluminess roof box."
        ),
        "order_note": "ORDER THE TURBINE FIRST — 4-6 week lead time gates Stage 3.",
    },

    {
        "id":       "VAN-006",
        "date":     "2026-08",
        "decision": "Wilwood 4-corner brake upgrade in Stage C. Interim stock brakes in Stage B.",
        "reason": (
            "The Wilwood Dynapro rear drum-to-disc conversion includes an integrated parking brake — "
            "the critical requirement for expedition use on mountain grades. "
            "Simpler disc conversion kits omit the parking brake. "
            "Stage B installs stock replacement pads/shoes as an interim measure to keep the van "
            "safe during the build period. Stage C replaces everything with the Wilwood system "
            "after Stage 1 build weight is finalized — spring rate and shock valving depend on "
            "the actual loaded vehicle weight."
        ),
    },

    {
        "id":       "VAN-007",
        "date":     "2026-08",
        "decision": "Three-zone vinyl wrap with eight Easter eggs. Applied LAST.",
        "reason": (
            "The three-zone wrap (ColorFlow blue-green upper / Satin Khaki Green mid / Matte Adobe lower) "
            "references the colors of the western American landscape the van is built for. "
            "Eight Easter eggs in petroglyph/sumi-e style (sea turtle, eagle, bison, saguaro, "
            "wave form, mountain silhouette, wolf, single star) are personal totems. "
            "The wrap is applied LAST — after all exterior hardware (Aluminess bumper, rack, "
            "cameras, solar, AC unit) is permanently installed. Wrapping before hardware "
            "installation guarantees damage."
        ),
        "wrap_sequence": "1. All hardware installed. 2. PPF on front/rockers. 3. Wrap applied.",
    },

    {
        "id":       "VAN-008",
        "date":     "2026-08",
        "decision": "Floor — rubber horse stall mats from Tractor Supply, removable.",
        "reason": (
            "4'x6' rubber horse stall mats from Tractor Supply (~$90 each) are durable, "
            "grippy, easy to clean, and completely removable. They sit on the 3/4-inch marine "
            "plywood subfloor without adhesive. Dogs track in dirt and water — mats can be "
            "pulled out and hosed down. Commercial van flooring alternatives are glued down "
            "and cannot be removed without damage."
        ),
    },

    {
        "id":       "VAN-009",
        "date":     "2026-08",
        "decision": "Dog systems — Gunner Kennel G1 for Tango, Sleepypod for Saki.",
        "reason": (
            "Tango is a husky with ADA service animal status — full park trail access everywhere. "
            "Saki is a schnauzer with ESA status — restricted to roads, campgrounds, and parking "
            "at NPS sites. This distinction is critical for trip planning. "
            "The Gunner Kennel G1 bolts to the DECKED system for crash safety. "
            "Saki's Sleepypod doubles as her travel bed at camp. "
            "The ADA/ESA distinction is respected in all destination planning."
        ),
    },

    {
        "id":       "VAN-010",
        "date":     "2026-08",
        "decision": "Analog-first philosophy — no wireless except Starlink (wired ethernet only).",
        "reason": (
            "Wireless systems fail in remote locations, consume standby power, create security "
            "vulnerabilities, and add software dependency. The van is built for places where "
            "cell service is unavailable. All critical systems are hardwired: AC thermostat, "
            "cameras, displays, monitoring. Starlink connects via the official wired ethernet "
            "adapter — the WiFi antenna is disabled. The Garmin inReach Mini 2 provides "
            "satellite emergency communication independent of all other systems."
        ),
    },

    # ── ADD NEW ENTRIES BELOW ──────────────────────────────────────────────────
]
