"""
van/spec/seating.py
Seat options for the GMC Savana 2500 expedition build.

The seats are the primary interface between the occupants and the van
on 8-10 hour driving days. Getting this right has an outsized impact
on how Kevin and Lisa feel at the end of a day at the trailhead.

INVESTIGATION STATUS: Active — decision pending first long-distance drive.
RECOMMENDATION: Two-phase approach (see RECOMMENDATION constant below).

Options organized by approach:
  1. Cushion overlays      — no commitment, test comfort preferences first
  2. Retrofit heated pads  — heating only, keeps factory seat
  3. Katzkin + Degreez     — full leather + heat/cool, keeps factory structure
  4. Aftermarket captain's — full seat replacement, automotive grade
  5. Semi-truck air ride   — engineered for all-day driving, best fatigue management
"""

# ── STOCK SEAT BASELINE ───────────────────────────────────────────────────────

STOCK_SEAT = {
    "description": (
        "GMC Savana 2500 cargo van factory seating. "
        "Basic vinyl bench or individual vinyl seats depending on configuration. "
        "No heating, no cooling, no lumbar adjustment, no suspension. "
        "Adequate for 30-minute commercial use. Not adequate for 8-hour expedition days."
    ),
    "problems_on_long_days": [
        "No lumbar support — lower back fatigue after 2-3 hours",
        "Vinyl traps heat — Texas departure in July is immediately uncomfortable",
        "No vibration isolation — road vibration transfers directly to spine",
        "Fixed position — no adjustment for body type or driving posture",
        "No cooling — sweat accumulation in hot climates",
    ],
    "verdict": "Replace or significantly upgrade before the 2027 trip.",
}

# ── OPTION 1: CUSHION OVERLAYS ───────────────────────────────────────────────

CUSHION_OVERLAYS = {
    "name":        "Seat Cushion Overlays",
    "description": "Add-on cushions placed on top of the factory seat. Zero installation, zero wiring.",
    "commitment":  "None — fully reversible, no tools required",
    "best_use":    "Phase 1 testing. Learn what actually hurts before investing in a full upgrade.",

    "options": [
        {
            "type":    "Ventilated cooling cushion with vibration",
            "brands":  ["Frost Seat", "Iced Seat", "generic 12V"],
            "features":[
                "12 fans circulating air, 3 cooling speeds",
                "Double vibration lumbar motor — basic massage",
                "Napa leather and breathable mesh cover",
                "12V — wire to lighter socket or dedicated circuit",
                "Automatic on/off when you sit/stand",
            ],
            "cost":     "$50-80 each",
            "weight":   "~2 lbs each",
            "verdict":  "Surprisingly effective in Texas July heat. Good Phase 1 test.",
        },
        {
            "type":    "Memory foam coccyx cutout cushion",
            "brands":  ["Everlasting Comfort", "ComfiLife", "Purple"],
            "features":[
                "Cutout relieves sit bone and coccyx pressure",
                "4-inch memory foam distributes weight evenly",
                "Washable cover",
                "No power required",
            ],
            "cost":     "$35-60 each",
            "weight":   "~2 lbs each",
            "verdict":  "Good for lower back and sit bone fatigue. Layer with cooling cushion.",
        },
        {
            "type":    "Lumbar support roll",
            "brands":  ["Everlasting Comfort", "Xtreme Comforts"],
            "features":[
                "Adjustable strap attaches to seat back",
                "Memory foam or inflatable",
                "Positions at lumbar curve",
            ],
            "cost":     "$25-45 each",
            "weight":   "~1 lb each",
            "verdict":  "Worth having regardless of what else is done. $30 insurance.",
        },
    ],

    "phase_1_kit": {
        "items": [
            "2x ventilated cooling cushion with vibration (~$65 each)",
            "2x memory foam coccyx cushion (~$45 each)",
            "2x lumbar support roll (~$30 each)",
        ],
        "total_cost": "$280 estimated",
        "purpose":    (
            "Drive the van 3-4 hours and note exactly what hurts — lower back, sit bones, heat, "
            "vibration. That data determines which Phase 2 upgrade is actually needed. "
            "Skipping Phase 1 risks buying the wrong $2,000 solution."
        ),
    },
}

# ── OPTION 2: RETROFIT HEATED PADS ───────────────────────────────────────────

RETROFIT_HEAT = {
    "name":        "Heated Pad Retrofit",
    "description": (
        "Carbon fiber or wire heating elements added to the factory seat foam "
        "under a new or existing cover. Heating only — no cooling."
    ),
    "commitment":  "Low — reversible with effort",
    "best_use":    "Cold mornings only. Montana July at elevation, early starts.",

    "installation": {
        "method":  "Peel-and-stick heating elements applied to seat foam under cover",
        "wiring":  "12V, wire to dedicated fused circuit from Blue Sea DC panel",
        "switch":  "Analog rocker or toggle — consistent with analog-first philosophy",
        "time":    "2-4 hours per seat DIY",
    },

    "brands": [
        {"name": "Rostra Precision Controls", "notes": "OEM supplier to many manufacturers — high quality"},
        {"name": "Saddleman",                 "notes": "Good DIY kits with clear instructions"},
        {"name": "Resistive universal kits",  "notes": "Budget option — quality varies significantly"},
    ],

    "cost":      "$80-180 per seat installed",
    "verdict": (
        "Solves cold mornings only. Does nothing for the 95°F Texas departure. "
        "Best combined with a cooling solution. Standalone only if budget is very tight."
    ),
}

# ── OPTION 3: KATZKIN LEATHER + DEGREEZ HEAT/COOL ───────────────────────────

KATZKIN_DEGREEZ = {
    "name":        "Katzkin Custom Leather + Degreez Heated/Cooled System",
    "description": (
        "Complete replacement of seat upholstery with custom Katzkin leather, "
        "with the Degreez OEM-quality heated and cooled system integrated into "
        "the new perforated leather covers. Keeps the factory seat frame and foam."
    ),
    "commitment":  "High — professional installation, not easily reversed",

    "katzkin_leather": {
        "description": "Custom-fit leather upholstery engineered for specific vehicle year/model",
        "colors":      "120+ colors and materials — can match natural fiber interior aesthetic",
        "natural_options": [
            "Tan / saddle / cognac leather coordinates with bamboo and hemp palette",
            "Perforated versions required for Degreez cooling to work properly",
        ],
        "installation": "Authorized Katzkin installer — Houston has multiple locations",
        "warranty":     "Katzkin factory warranty on materials and installation",
    },

    "degreez_system": {
        "description": (
            "OEM-quality heated and cooled system that installs between the "
            "perforated Katzkin leather cover and the factory foam. "
            "Air drawn from under the seat, through the foam, out through the perforations."
        ),
        "heat_levels":  3,
        "cool_levels":  3,
        "control":      "Single switch per seat — 6 positions total",
        "requires":     "Perforated Katzkin leather — cooling does not work through solid leather or cloth",
        "power":        "12V — wire to dedicated circuits on Blue Sea panel",
        "notes":        "Can be installed on cloth but airflow significantly reduced",
    },

    "cost": {
        "leather_both_seats":    "$800-1,200",
        "degreez_both_seats":    "$600-800",
        "installation_labor":    "$300-500",
        "total_estimated":       "$1,700-2,500",
    },

    "pros": [
        "OEM quality — looks and feels factory",
        "Heat and cool both seats independently",
        "120+ color choices — can match interior palette",
        "Houston installer availability — easy service access",
        "Keeps factory seat structure — no mounting complexity",
        "Increases resale value",
    ],
    "cons": [
        "No vibration isolation — road vibration still transfers to spine",
        "No massage function",
        "Factory foam remains — if foam is worn, the feel doesn't improve much",
        "Cooling requires perforated leather to function properly",
    ],

    "verdict": (
        "The right answer if heat and cool are the primary complaints after Phase 1 testing "
        "and the factory seat structure is still fundamentally comfortable. "
        "Not the right answer if road vibration fatigue is the real problem."
    ),
}

# ── OPTION 4: AFTERMARKET CAPTAIN'S CHAIRS ───────────────────────────────────

CAPTAINS_CHAIRS = {
    "name":        "Aftermarket Automotive Captain's Chairs",
    "description": (
        "Full seat replacement with aftermarket captain's chairs designed "
        "for van and truck applications. Bolts to factory floor mounts "
        "(confirm compatibility for Savana 2500 specifically)."
    ),
    "commitment":  "High — full replacement",

    "brands": [
        {
            "name":     "Captain's Choice",
            "notes":    "Purpose-built for conversion van replacement. FMVSS-207/210 certified.",
            "features": ["Power adjustment", "Heated", "Multiple material options"],
            "cost":     "$600-1,200 each",
        },
        {
            "name":     "Recaro",
            "notes":    "Automotive performance seat. Excellent ergonomics, limited heat/cool options.",
            "features": ["Superior lateral support", "Excellent bolstering", "Some heated versions"],
            "cost":     "$800-2,000 each",
        },
        {
            "name":     "Braun / Vantage Mobility",
            "notes":    "ADA-focused. Swivel and transfer features for Tango access if needed.",
            "features": ["Swivel", "Power adjustment", "ADA compliant"],
            "cost":     "$1,200-2,500 each",
        },
    ],

    "mounting_note": (
        "Confirm floor mount compatibility with the Savana 2500 before ordering. "
        "Rail vs. pedestal configuration varies by van model year and trim. "
        "FMVSS-207/210 certification required for any seating used while the vehicle is in motion."
    ),

    "pros": [
        "Full seat replacement — can select ergonomically superior foam and structure",
        "Clean automotive integration",
        "FMVSS certified for legal compliance",
    ],
    "cons": [
        "No vibration isolation",
        "No massage",
        "Compatibility research required before purchase",
        "Similar cost to semi-truck option without the fatigue management benefits",
    ],

    "verdict": (
        "Middle-ground option. Better ergonomics than stock but no vibration isolation. "
        "The semi-truck air ride seats solve more problems at similar cost "
        "with more fabrication complexity."
    ),
}

# ── OPTION 5: SEMI-TRUCK AIR RIDE SEATS ─────────────────────────────────────

SEMI_TRUCK_SEATS = {
    "name":        "Semi-Truck Air Ride Seats",
    "description": (
        "Commercial long-haul truck seats designed for all-day driving. "
        "Air suspension in the seat itself isolates the occupant from road vibration. "
        "The most complete solution for fatigue management on 8-10 hour days. "
        "The category most van builders overlook."
    ),
    "commitment":  "High — requires pedestal fabrication to mount in the Savana",

    "why_this_category": (
        "Long-haul truck drivers cover 500-600 miles per day, every day, for years. "
        "The commercial seating industry has spent decades solving exactly the fatigue "
        "problem that expedition van drivers face on a 28-day road trip. "
        "Air suspension in the seat separates the occupant from chassis vibration — "
        "the root cause of end-of-day fatigue that heat/cool alone cannot address."
    ),

    "top_options": [
        {
            "model":      "Bostrom Wide Ride+ Serta",
            "suspension": "Isolating scissor suspension with high-performance adjustable damper",
            "cushion":    "23-inch wide, Serta Cool Action Gel memory foam",
            "heat":       True,
            "cool":       True,
            "massage":    "BackCycler® — slow inflate/deflate lumbar, improves circulation",
            "extras":     ["Air-powered bolsters", "16-inch armrests optional", "Front/rear cushion tilt"],
            "source":     "bostromseating.com or suburbanseats.com",
            "cost_est":   "$1,200-1,800 each",
            "notes":      (
                "The BackCycler system is clinically designed to reduce lower back fatigue "
                "by cycling lumbar support rather than holding a static position. "
                "This is genuinely different from a vibration massage."
            ),
        },
        {
            "model":      "Sears Atlas II DLX with Thermassage",
            "suspension": "Air bellows suspension with adjustable shock and ActiveVRS magnetic ride",
            "cushion":    "Deep cushioning, heavy-duty frame",
            "heat":       True,
            "cool":       True,
            "massage":    "Thermassage — heat and massage combined in seat and backrest",
            "extras":     ["Bellows suspension cover", "Multiple adjustment points"],
            "source":     "suburbanseats.com or 4statetrucks.com",
            "cost_est":   "$1,400-2,000 each",
            "notes":      (
                "The ActiveVRS magnetic ride suspension actively reduces vibrations "
                "rather than passively absorbing them. "
                "Thermassage integrates heat and massage into the same element."
            ),
        },
        {
            "model":      "National Admiral CT",
            "suspension": "Air suspension with triple-chamber adjustable lumbar",
            "cushion":    "Breathable cover, ergonomic design",
            "heat":       True,
            "cool":       True,
            "massage":    "Backcycler® lumbar cycling",
            "extras":     ["Driver swivel option", "Dual adjustable armrests"],
            "source":     "suburbanseats.com",
            "cost_est":   "$1,200-1,700 each",
            "notes":      "Swivel option useful for van life — turn to face rear without exiting.",
        },
        {
            "model":      "ISRI 5030/880",
            "suspension": "European-design air suspension",
            "cushion":    "Genuine leather option, premium adjustability",
            "heat":       True,
            "cool":       True,
            "massage":    False,
            "extras":     ["Swivel option", "Highly adjustable"],
            "source":     "suburbanseats.com",
            "cost_est":   "$1,500-2,200 each",
            "notes":      "ISRI is European OEM standard. No massage but best-in-class adjustability.",
        },
    ],

    "mounting_challenge": {
        "description": (
            "Semi-truck seats mount on a pedestal base designed for Class 6-8 truck cab floors. "
            "The Savana floor has a different mounting pattern. "
            "A pedestal adapter must be fabricated or sourced."
        ),
        "options": [
            "Universal truck seat pedestal base — some have adjustable bolt patterns",
            "Custom fabricated steel pedestal welded to Savana floor mount points",
            "Local fab shop — 2-4 hours work, ~$200-400 in labor + materials",
        ],
        "difficulty": "Moderate — not plug-and-play but straightforward fabrication work",
        "fmvss_note": (
            "Ensure any pedestal fabrication maintains FMVSS-207/210 compliance. "
            "The seat must be rated for the mounting configuration under crash loads. "
            "Use the seat manufacturer's rated pedestal wherever possible."
        ),
    },

    "pros": [
        "Air suspension isolates from road vibration — the root cause of long-day fatigue",
        "Heat and cool both available",
        "BackCycler / Thermassage massage functions address circulation fatigue",
        "Engineered for 8-10 hour days — exactly the use case",
        "Wide 23-inch cushion (Bostrom) accommodates long driving days",
        "Air-adjustable bolsters for custom fit",
        "Swivel options available (National Admiral CT) — useful in van context",
    ],
    "cons": [
        "Requires pedestal fabrication for Savana floor mounting",
        "Higher upfront cost",
        "Designed for truck cabs — aesthetics are commercial, not expedition",
        "Heavier than automotive seats (~60-90 lbs each)",
        "Lisa's preference for aesthetics may not align with commercial seat look",
    ],

    "weight_per_seat":    "60-90 lbs",
    "total_weight_2_seats": "120-180 lbs",
    "cost_2_seats_plus_fab": "$3,200-5,000 estimated",

    "verdict": (
        "The most complete solution for fatigue management on 8-10 hour driving days. "
        "Vibration isolation from the air suspension addresses the problem that "
        "heat/cool alone cannot fix. The commercial aesthetic is the main compromise. "
        "Worth the pedestal fabrication work if Phase 1 testing reveals vibration "
        "fatigue as a primary complaint."
    ),
}

# ── MATERIAL OPTIONS ─────────────────────────────────────────────────────────

MATERIALS = {
    "vinyl": {
        "pros":  ["Durable", "Easy to clean", "Waterproof", "Dog-friendly"],
        "cons":  ["Traps heat in summer", "Cold in winter", "Uncomfortable on long days"],
        "notes": "Stock Savana material. Acceptable for short trips. Wrong for 8-hour days.",
        "dog_compatibility": "Excellent — cleans easily, resists puncture from claws",
    },
    "cloth": {
        "pros":  ["Breathable", "More comfortable than vinyl", "Cooler in summer"],
        "cons":  ["Absorbs odors", "Difficult to clean dog hair and mud", "Fades"],
        "notes": "Better comfort than vinyl but poor dog compatibility.",
        "dog_compatibility": "Poor — hair embeds, odors absorb, cleaning is difficult",
    },
    "leather_genuine": {
        "pros":  ["Premium feel", "Durable", "Ages well", "Easier to clean than cloth"],
        "cons":  ["Hot in summer without perforation and cooling", "Cold in winter", "Can crack without conditioning"],
        "notes": "Best with Degreez cooling system through perforations.",
        "dog_compatibility": "Good — cleans well, resists puncture from small claws (Saki fine, Tango manageable)",
    },
    "leather_perforated": {
        "pros":  ["Required for Degreez cooling to function", "Breathable", "Premium look"],
        "cons":  ["More expensive", "Must be kept conditioned"],
        "notes": "The correct choice if Katzkin + Degreez route is taken.",
        "dog_compatibility": "Good — same as solid leather, perforations don't affect durability",
    },
    "ultra_leather": {
        "pros":  ["More durable than genuine leather", "Easier maintenance", "Lower cost", "Consistent texture"],
        "cons":  ["Less premium feel than genuine leather"],
        "notes": "Used by Bostrom and Sears in commercial truck seats. Extremely durable.",
        "dog_compatibility": "Excellent — designed for commercial use, highly scratch-resistant",
    },
    "gel_memory_foam": {
        "type":  "Cushion material (under cover, not a cover material)",
        "pros":  ["Distributes pressure evenly", "Reduces fatigue", "Conforms to body"],
        "cons":  ["Retains heat without cooling system", "Heavier than standard foam"],
        "notes": "Bostrom Serta Cool Action Gel foam reduces heat retention vs standard memory foam.",
    },
}

# ── DOG COMPATIBILITY ─────────────────────────────────────────────────────────

DOG_COMPATIBILITY = {
    "Tango": {
        "breed":  "Husky",
        "weight": "~65 lbs",
        "issues": ["Heavy shedding", "Large claws", "Likes to lean on surfaces"],
        "notes":  (
            "Tango's primary impact on seats is hair accumulation and claw marks. "
            "Ultra-leather and genuine leather both resist his claws better than vinyl. "
            "Perforated leather traps hair in the holes — consider this before choosing "
            "perforated upholstery on areas where Tango sits. "
            "Tango typically travels in the Gunner kennel in the cargo area — "
            "not in the cab seats — so cab seat material is primarily for Kevin and Lisa."
        ),
    },
    "Saki": {
        "breed":  "Schnauzer",
        "weight": "~30 lbs",
        "issues": ["Minimal shedding (schnauzers don't shed much)", "Small but sharp claws"],
        "notes":  (
            "Saki's Sleepypod doubles as her travel bed — she may occasionally sit on the "
            "passenger lap or seat. Minor impact on seat material. "
            "Any material that works for Kevin and Lisa is fine for Saki."
        ),
    },
    "recommendation": (
        "Keep dog travel in the cargo area in kennels. The cab seats are for people. "
        "If a dog does ride in the cab occasionally, ultra-leather is the most durable "
        "and easiest to clean. Avoid perforated leather on any surface where "
        "Tango's hair will accumulate — it embeds in the perforations."
    ),
}

# ── PHASED RECOMMENDATION ─────────────────────────────────────────────────────

RECOMMENDATION = {
    "philosophy": (
        "Same as the build philosophy — lightweight and low-commitment first. "
        "Learn what actually hurts before spending real money. "
        "The stock seat's problems on long days are predictable, but which problem "
        "matters most (heat, vibration, lumbar, cooling) varies by person and route. "
        "Phase 1 costs $280 and generates the data that makes Phase 2 correct."
    ),

    "phase_1": {
        "name":    "Test and Learn",
        "timing":  "Before the 2027 trip — drive 3-4 hours and note exactly what hurts",
        "cost":    "~$280",
        "items": [
            "2x ventilated cooling cushion with vibration lumbar (~$65 each)",
            "2x memory foam coccyx cutout cushion (~$45 each)",
            "2x lumbar support roll (~$30 each)",
        ],
        "diagnostic_questions": [
            "Is lower back pain the primary issue? → Lumbar and foam upgrade",
            "Is heat the primary issue? → Katzkin + Degreez",
            "Is vibration fatigue the primary issue? → Semi-truck air ride seats",
            "Is sit bone pressure the primary issue? → Coccyx cushion + memory foam upgrade",
        ],
    },

    "phase_2_if_heat_is_the_problem": {
        "name":    "Katzkin Custom Leather + Degreez",
        "timing":  "After first road trip, before 2027 departure",
        "cost":    "$1,700-2,500",
        "notes":   (
            "Choose perforated tan/saddle/cognac leather to coordinate with the "
            "bamboo and natural fiber interior palette. "
            "Houston has multiple authorized Katzkin installers. "
            "Katzkin can verify Savana 2500 fit before ordering."
        ),
    },

    "phase_2_if_vibration_is_the_problem": {
        "name":    "Bostrom Wide Ride+ Serta or Sears Atlas II DLX",
        "timing":  "After first road trip, before 2027 departure",
        "cost":    "$3,200-5,000 including pedestal fabrication",
        "notes":   (
            "Bostrom Wide Ride+ is the starting recommendation — "
            "BackCycler lumbar system, air suspension, heat/cool, 23-inch cushion. "
            "Requires pedestal fabrication for Savana floor mounting (~$400 fab shop). "
            "Commercial aesthetic is the main compromise. "
            "Confirm headroom with seat installed — truck seats sit higher than automotive."
        ),
    },

    "phase_2_if_budget_is_tight": {
        "name":    "Retrofit heated pads + better cushions",
        "timing":  "Any time",
        "cost":    "$300-500",
        "notes":   "Heated pads for cold mornings, upgraded foam cushion for comfort. Simple.",
    },

    "decision_gate": (
        "Do not decide on Phase 2 until after driving the van at least 4 hours "
        "on a highway with the Phase 1 cushions. "
        "The answer will be obvious by mile 200."
    ),
}

# ── BUDGET PLACEHOLDER ────────────────────────────────────────────────────────

BUDGET = {
    "phase_1_cushions":             280,
    "option_katzkin_degreez":      2100,   # midpoint estimate
    "option_semi_truck_seats":     4000,   # midpoint including fab
    "option_retrofit_heat_only":    320,
    "option_captains_chairs":      2000,   # midpoint estimate
}
