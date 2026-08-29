"""
van/spec/exterior.py
Exterior wrap, Easter eggs, PPF, and Aluminess hardware specification.

CRITICAL RULE: The wrap is applied LAST.
After the front bumper, roof rack, storage box, cameras, solar panels,
AC unit, and all other exterior hardware are permanently installed.
Wrapping before hardware installation guarantees damage. No exceptions.
"""

WRAP_RULE = (
    "The wrap is applied ABSOLUTELY LAST. "
    "Every piece of exterior hardware must be permanently installed before "
    "the wrap shop appointment is scheduled. "
    "This includes: Aluminess front bumper, roof rack, storage box, "
    "rooftop AC unit, all solar panels and mounts, all cameras, "
    "awning hardware, and any other exterior attachments. "
    "Sequence: 1. All hardware installed.  2. PPF applied.  3. Wrap applied."
)

# ── THREE-ZONE COLOR SCHEME ───────────────────────────────────────────────────

ZONES = {
    "upper": {
        "area":        "Roof and upper body panels above the belt line",
        "film":        "Avery Dennison SW900 ColorFlow",
        "color":       "Fresh Spring (252-S)",
        "effect":      "Blue-to-green color shift depending on viewing angle and lighting",
        "finish":      "Gloss",
        "notes":       "ColorFlow films are viewing-angle dependent — the shift from blue to green "
                       "is most pronounced in direct sunlight at a 45-degree angle.",
    },
    "mid": {
        "area":        "Mid body — main body panels below belt line to rocker panels",
        "film":        "Avery Dennison SW900",
        "color":       "Satin Khaki Green",
        "effect":      "Matte sage green — flat finish, low reflectivity",
        "finish":      "Satin",
        "notes":       "The dominant color of the van. References the Montana prairie and BLM landscape.",
    },
    "lower": {
        "area":        "Lower body, rocker panels, wheel arches",
        "film":        "Avery Dennison SW900",
        "color":       "Matte Adobe",
        "effect":      "Warm earth tone — matte finish, dusty appearance",
        "finish":      "Matte",
        "notes":       "Lower zone takes the most road debris. Matte finish hides minor abrasion "
                       "better than gloss. References the desert and canyon country.",
    },
}

# ── EASTER EGGS ───────────────────────────────────────────────────────────────
# Eight small symbols embedded in the wrap.
# Style: petroglyph or sumi-e — monochromatic, 2-4 inches, subtle.
# These are personal totems, not decorations. Their locations are not marked.
# Only someone looking closely will find them.

EASTER_EGGS = [
    {
        "id":      1,
        "subject": "Sea turtle",
        "meaning": "Lisa's favorite animal. The reason the trip starts.",
        "style":   "Sumi-e brushstroke",
        "size":    "3 inches",
        "color":   "Monochromatic — same tone as surrounding panel, etched or debossed effect",
        "location":"TBD — artist recommendation",
    },
    {
        "id":      2,
        "subject": "Eagle",
        "meaning": "The American West. Freedom. The open road.",
        "style":   "Petroglyph — geometric, simplified",
        "size":    "3 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
    {
        "id":      3,
        "subject": "Bison",
        "meaning": "The Dakotas. The return of a species. Sage Creek at dawn.",
        "style":   "Petroglyph",
        "size":    "3 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
    {
        "id":      4,
        "subject": "Saguaro cactus",
        "meaning": "Texas and the Southwest — where the trip begins and ends.",
        "style":   "Sumi-e brushstroke",
        "size":    "2.5 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
    {
        "id":      5,
        "subject": "Wave form",
        "meaning": "The Missouri River. Lewis and Clark. Water flowing to three oceans.",
        "style":   "Petroglyph — abstract wave or river symbol",
        "size":    "2 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
    {
        "id":      6,
        "subject": "Mountain silhouette",
        "meaning": "Glacier. The Crown of the Continent. The destination.",
        "style":   "Sumi-e — simple mountain outline",
        "size":    "3 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
    {
        "id":      7,
        "subject": "Wolf",
        "meaning": "Tango. The north. The wild things that still exist.",
        "style":   "Petroglyph",
        "size":    "3 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
    {
        "id":      8,
        "subject": "Single star",
        "meaning": "The fifth anniversary. The night sky above Sage Creek. Home.",
        "style":   "Simple — four or five point star",
        "size":    "2 inches",
        "color":   "Monochromatic",
        "location":"TBD",
    },
]

# ── PAINT PROTECTION FILM ─────────────────────────────────────────────────────

PPF = {
    "areas": [
        "Front fascia — full coverage (most stone chip exposure)",
        "Hood — leading edge at minimum, full hood preferred",
        "Lower body rocker panels — full length",
        "Wheel arch lips — front and rear",
        "Side mirrors",
    ],
    "film":     "XPEL Ultimate Plus or 3M Scotchgard Pro Series",
    "finish":   "Matte PPF under matte wrap, gloss PPF under gloss sections",
    "timing":   "PPF applied before wrap — wrap wraps over PPF edges",
    "notes":    (
        "PPF protects the body metal before the vinyl wrap is applied. "
        "Stone chips on the front fascia are inevitable on western highways. "
        "PPF absorbs them without damaging the paint underneath. "
        "If the wrap is ever removed, the paint underneath is pristine."
    ),
}

# ── ALUMINESS HARDWARE ────────────────────────────────────────────────────────

ALUMINESS = {
    "front_bumper": {
        "description": "Aluminess front winch bumper for Savana 2500",
        "includes":    ["Winch mount (centered)", "D-ring mounts x2", "Skid plate"],
        "material":    "Marine-grade aluminum — no rust, no paint required",
        "lead_time":   "8-12 weeks custom fabrication",
        "timing":      "Stage 2 — installed before wrap",
        "notes":       "Measure the Warn VR EVO 12-S winch dimensions before ordering "
                       "to confirm the mount opening fits.",
    },
    "roof_rack": {
        "description": "Aluminess roof rack for Savana extended",
        "includes":    ["Full-length rack", "Mounting hardware", "Wind fairing"],
        "material":    "Marine-grade aluminum",
        "lead_time":   "8-12 weeks custom fabrication",
        "timing":      "Stage 3 — installed before wrap",
        "load_rating": "500 lbs dynamic",
        "notes":       "Specify the exact wheelbase (155 inches) and confirm solar panel "
                       "mounting provisions when ordering.",
    },
    "storage_box": {
        "description": "Aluminess deluxe storage box — roof-mounted",
        "purpose":     "Stores Primus wind turbine body and blade bag when not deployed",
        "material":    "Marine-grade aluminum, weatherproof seal",
        "lead_time":   "8-12 weeks custom fabrication",
        "timing":      "Stage 3 — installed with roof rack, before wrap",
        "notes":       "Confirm internal dimensions accommodate the Primus AIR Silent X "
                       "turbine body and folded blade bag before ordering.",
    },
    "ordering_note": (
        "All three Aluminess pieces can be ordered simultaneously to save on shipping. "
        "Lead time is 8-12 weeks — order at Stage 1 start so Stage 2 and 3 hardware "
        "arrives when needed. Call (619) 449-7110 to confirm current lead times."
    ),
}

# ── WRAP SHOP REQUIREMENTS ────────────────────────────────────────────────────

WRAP_SHOP = {
    "requirements_before_booking": [
        "Aluminess front bumper installed",
        "Aluminess roof rack installed",
        "Aluminess storage box installed",
        "OutEquipPro Summit 2 AC unit installed",
        "All solar panels and mounts installed",
        "All cameras installed (thermal + 4 perimeter)",
        "MaxxAir roof fan installed",
        "Primus wind turbine cable gland installed through roof",
        "Alu-Cab 270° Shadow Awning RHS mounted to Aluminess roof rack",
        "180° side awning LHS mounted to Aluminess roof rack",
        "OVS HD Nomadic 180° awning mounted to LHS (driver side) roof rack",
        "Alu-Cab Shower Cube mounted to LHS roof rack brackets (driver side)",
        "Any other exterior hardware permanently installed",
        "PPF applied to all specified areas",
        "Vector art files delivered to shop in AI or EPS format",
    ],
    "shop_requirements": [
        "3+ years experience with color-shift films",
        "Can work with Avery Dennison SW900 ColorFlow",
        "Portfolio of complex multi-tone vehicle wraps",
        "Ability to cut and position custom easter egg artwork",
        "Climate-controlled installation bay",
    ],
    "deliverables_to_shop": [
        "Avery Dennison color codes for all three zones",
        "Vector files (AI or EPS) for all 8 Easter egg designs",
        "Zone boundary diagram showing where each color meets",
        "PPF documentation showing what is already protected",
    ],
    "budget_range":    "$7,000 – $8,000",
    "artist_budget":   "$300 – $600 for vector art commission",
    "artist_brief": (
        "Commission a graphic artist to create vector files for 8 small symbols "
        "in a consistent petroglyph/sumi-e style. All monochromatic. 2-4 inches each. "
        "The style should reference Plains Indian petroglyphs and Japanese sumi-e brushwork — "
        "not cartoon, not tribal pattern, not logo. Simple, ancient-feeling, personal."
    ),
}
