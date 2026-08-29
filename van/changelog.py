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


    {
        "id":       "VAN-011",
        "date":     "2026-08",
        "decision": "Adopted lightweight-first philosophy — Stage 1 renamed Stage 1A",
        "reason": (
            "Heavy fixed storage systems (DECKED VG2 drawer system, plywood subfloor) "
            "removed from Stage 1. DECKED weighs 200-275 lbs and costs $1,850 — "
            "the single heaviest non-essential item in the build. "
            "A lightweight first expedition provides real data on what storage is actually needed "
            "before committing to fixed systems. Floor storage in Stage 1A is hard-sided crates "
            "only — flexible, repositionable, no weight penalty. "
            "Plywood subfloor also dropped — horse stall mats sit directly on van floor. "
            "Both items deferred to a later stage pending first-expedition experience."
        ),
        "alternatives_considered": [
            "Keep DECKED — rejected: 200-275 lbs and $1,850 for a system that may not match actual needs",
            "Lighter drawer system — rejected: still fixed weight and cost before needs are known",
            "No storage system ever — rejected: deferred, not abandoned, will revisit after first trip",
        ],
    },

    {
        "id":       "VAN-012",
        "date":     "2026-08",
        "decision": "Unistrut channel grid expanded to 10 runs — reconfigurable interior skeleton",
        "reason": (
            "The channel grid (3 wall runs per side + 2 ceiling + 2 floor = 10 total) "
            "makes the entire interior reconfigurable without tools. "
            "Platform legs drop into wall channels at different heights for flat/chaise/cargo modes. "
            "Lighting mounts on ceiling and high wall channels. "
            "Structural ceiling hardpoints through-bolted to van roof ribs for load securing. "
            "Nothing is permanent that doesn't need to be. "
            "The contrast between industrial aluminum channel and natural bamboo/hemp surfaces "
            "is intentional — functional skeleton, natural finish."
        ),
    },

    {
        "id":       "VAN-013",
        "date":     "2026-08",
        "decision": "Hemp webbing platform is dual-purpose: sleeping surface AND load tie-down grid",
        "reason": (
            "The hemp webbing grid serves two functions: "
            "(1) sleeping surface with bamboo lyocell topper, "
            "(2) load securing grid — cam straps hook through the webbing to secure crates. "
            "No separate tie-down hardware needed. No loose loads while moving. "
            "Crates are hard-sided, stackable, and secured to the webbing. "
            "Crate position on the platform is TBD — will be finalized after walls are up "
            "and the interior is experienced in person. "
            "Ceiling hardpoints (4x through-bolted to van roof ribs) provide additional "
            "securing for stacked crates — positioned above the crate zone after walls are up."
        ),
    },

    {
        "id":       "VAN-014",
        "date":     "2026-08",
        "decision": "5-zone lighting plan with analog rocker panel and master cutoff",
        "reason": (
            "Five lighting zones covering all interior use cases: "
            "Zone 1 Ambient (2700K warm, ceiling channels, frosted diffuser), "
            "Zone 2 Reading (adjustable puck lights at bed head, Unistrut-mounted), "
            "Zone 3 Work (4000K neutral, mid wall channel, cargo mode), "
            "Zone 4 Night (red LED floor strip, non-disruptive, preserves night vision), "
            "Zone 5 Exterior (weatherproof pucks above rear doors, camp lighting). "
            "Analog rocker panel near the side door — MASTER cutoff (large rocker, top position) "
            "kills all lighting circuits. Individual zone rockers below. "
            "Consistent with analog-first philosophy — no smart lighting, no app control. "
            "One habit: flip master when leaving the van. Good battery discipline."
        ),
    },

    {
        "id":       "VAN-015",
        "date":     "2026-08",
        "decision": "Front bumper weight corrected — net change is ~0 lbs, not +185 lbs",
        "reason": (
            "Original weight estimate had Aluminess front bumper at 185 lbs with no credit "
            "for the stock bumper removed. "
            "Research confirmed: Aluminess front bumper for Savana/Express = 85 lbs. "
            "Stock Savana front bumper assembly = approximately 85 lbs. "
            "Net weight change from the bumper swap alone: approximately 0 lbs. "
            "The winch (95 lbs) is what actually adds weight to the front axle. "
            "Weight estimate corrected in van/data/weight.py. "
            "Combined with DECKED removal, Stage 1A loaded weight estimate improved "
            "by approximately 250-350 lbs vs original Stage 1 estimates."
        ),
    },


    {
        "id":       "VAN-016",
        "date":     "2026-08",
        "decision": "Insulation stack overhauled — Noico + XPS + Thinsulate + targeted Great Stuff",
        "reason": (
            "Original stack (Dynamat + closed-cell spray foam + Polyiso + Thinsulate) "
            "had two materials that were wrong for the build: "
            "1. Closed-cell spray foam bonds permanently to van metal. "
            "If wiring needs access, rust appears behind a panel, or a leak develops under the foam, "
            "it must be chipped and scraped out by hand. A vehicle that vibrates, flexes, and "
            "needs 20 years of maintenance access is not a house. Spray foam is the most common "
            "regret reported by experienced van builders. Replaced with targeted Great Stuff "
            "for void sealing only — not continuous application to van metal. "
            "2. Polyiso loses R-value in cold. At 25F, effective R drops to ~3.5/inch vs rated 6.5/inch. "
            "Montana overnight lows in late July at elevation routinely hit 35-45F. "
            "Polyiso is losing half its performance exactly when it is needed most. "
            "Replaced with XPS rigid board — R-value stable at 25F. "
            "Dynamat replaced with Noico 80mil — same damping performance, 70% less cost and weight. "
            "New stack: Noico (damping) + Thinsulate SM600L (cavity fill) + "
            "XPS (continuous thermal layer) + Great Stuff (targeted voids only). "
            "Everything is removable and inspectable. Van metal access preserved."
        ),
        "alternatives_considered": [
            "Keep spray foam — rejected: permanent bond kills access forever, rust risk",
            "Keep Polyiso — rejected: R-value collapses to 3.5/inch at 25F — Montana July mornings",
            "Aerogel blanket — considered: R10/inch is compelling but $10-11/sqft is prohibitive for full coverage. Reserve for specific tight spots in Stage 2 if needed.",
            "Sheep's wool — considered: natural material but same R-value as Thinsulate, moisture absorption risk, harder to source",
        ],
    },

    {
        "id":       "VAN-017",
        "date":     "2026-08",
        "decision": "Electronics bay with filtered ventilation — dog hair protection for MultiPlus",
        "reason": (
            "The Victron MultiPlus 12/3000 has an internal cooling fan — it actively pulls air "
            "through the unit. A husky (Tango) in a sealed van produces continuous hair in the air. "
            "Dog hair accumulating on the MultiPlus fan and internal components is a thermal and "
            "reliability risk. Every 10C rise in electronics temperature reduces component life by "
            "~50% (Arrhenius equation). "
            "Solution: enclosed electronics bay for all Victron components. "
            "Filtered intake vent (low position, natural convection) keeps hair out of the bay. "
            "Additional filter directly over the MultiPlus intake grille. "
            "Filter media: washable polyester foam, 80-120mm panel filter frames. "
            "Field backup: pantyhose over the MultiPlus intake — free, replaces in 30 seconds, "
            "field-proven in marine and RV applications. "
            "Maintenance: inspect filter monthly — with a husky, expect fast loading. "
            "The SmartSolar MPPT 100/50 and Orion-XS are passively cooled and lower risk "
            "but benefit from the enclosed bay regardless."
        ),
        "alternatives_considered": [
            "No protection — rejected: husky hair is continuous and will clog the MultiPlus fan",
            "Powered filtered enclosure — rejected: adds complexity and power draw; natural convection is sufficient",
            "Custom-printed fan housing (Etsy, Victron community) — available option for the MPPT if throttling becomes an issue in summer",
        ],
    },


    {
        "id":       "VAN-018",
        "date":     "2026-08",
        "decision": "Platform confirmed — GMC Savana 2500 6.0L Vortec. AFM disable mandatory at purchase.",
        "reason": (
            "Full platform comparison conducted: Savana 2500 vs Ford Transit vs Mercedes Sprinter. "
            "Decision criterion: which platform can a small-town mechanic fix at 9pm in rural Montana. "
            "Savana wins on expedition serviceability — 6.0L Vortec components available at any AutoZone "
            "in any town, serviceable by any shop without special tooling, architecture unchanged since 1996. "
            "Ford Transit 3.7L naturally aspirated is the reliable Transit engine choice (no turbo) but "
            "is underpowered loaded at elevation on Montana passes. EcoBoost adds turbo risk documented "
            "by fleet mechanics. "
            "Mercedes Sprinter diesel reaches 300,000-400,000 miles but only 277 dealers nationwide — "
            "documented real-world cases of 200-mile tows to the nearest capable shop in rural areas. "
            "The Savana high roof absence is a genuine quality-of-life compromise — crawl-in entry "
            "is the price paid for serviceability everywhere. "
            "The 6.0L Vortec primary reliability risk is the AFM (Active Fuel Management) "
            "cylinder deactivation system — causes lifter failures, oil consumption, fouled plugs. "
            "Fix: Range Technology AFM Disabler ($120 OBD-II plug-in device) before the first drive. "
            "With AFM disabled and proper maintenance, the 6.0L routinely reaches 300,000+ miles. "
            "Full documentation: van/spec/mechanical.py — PLATFORM_RATIONALE, L96_KNOWN_ISSUES, "
            "PURCHASE_INSPECTION."
        ),
        "alternatives_considered": [
            "Ford Transit 3.7L — good platform, better interior, underpowered loaded at elevation",
            "Ford Transit 3.5L EcoBoost — adds power, adds turbo failure risk per fleet mechanics",
            "Mercedes Sprinter 2500 diesel — best longevity, worst rural serviceability",
            "Ram ProMaster — FWD only, wrong for expedition use, rejected early",
        ],
    },


    {
        "id":       "VAN-019",
        "date":     "2026-08",
        "decision": "Awning system replaced — Alu-Cab 270° RHS + 180° LHS + Alu-Cab Shower Cube",
        "reason": (
            "Original spec had a Roam 8-ft side awning and annex room (~$670, ~20 lbs). "
            "This only covered one side of the van. "
            "Kevin's intent was a 270° awning with shower module providing full coverage "
            "around the back half of the van. "
            "No single-unit 360° awning exists — the geometry of a hinge-based system "
            "prevents wrapping all three sides from one mounting point. "
            "Solution: two-awning system providing equivalent full coverage. "
            "PRIMARY: Alu-Cab 270° Shadow Awning RHS (passenger side, $1,050) — "
            "covers rear barn doors and full passenger side simultaneously in one 45-second "
            "deploy. 10 m² (107 sq ft), 315gsm polyester, 600mm water column, freestanding, "
            "silver reflective coating. Shower Cube mounts on LHS (driver side) under the OVS 180 awning. "
            "SECONDARY: 180° awning LHS (driver side, $650) — covers driver side independently. "
            "Deployed together: full rear + both sides covered. "
            "SHOWER: Alu-Cab Shower Cube ($550) mounts to RHS rack adjacent to the 270° awning. "
            "9kg aluminum/stainless, 43in x 36in x 74-94in open, adjustable height, "
            "dual-side zipper entry, locking arms. Use as shower, changing room, or privacy cube. "
            "Shower water from 30-gallon tank via gravity bag or 12V pump. "
            "Total awning system: ~$2,335, ~93 lbs. "
            "vs original Roam spec: ~$670, ~20 lbs. "
            "Delta: +$1,665, +73 lbs for: full three-side coverage, shower capability, "
            "private changing area, and 45-second one-person deploy."
        ),
        "alternatives_considered": [
            "Single 270° awning one side only — rejected: leaves rear or one full side uncovered",
            "Two 270° awnings LHS + RHS — considered: gives double-covered rear but +100 lbs and ~$2,200 awnings alone, more than needed",
            "OVS 360° system (two 180° units) — considered: good coverage but rear join is panels not solid, and no shower module integration",
            "Keep Roam 8-ft — rejected: only covers one side, no shower provision",
        ],
    },

    # ── ADD NEW ENTRIES BELOW ──────────────────────────────────────────────────
]
