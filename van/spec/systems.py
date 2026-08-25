"""
van/spec/systems.py
Interior systems specification for the GMC Savana 2500 expedition build.

Covers:
  - Unistrut channel grid (reconfigurable interior framework)
  - Sleep platform (hemp webbing, chaise lounge configuration)
  - Lighting plan (5 zones, analog rocker control, master cutoff)
  - Load securing (crates on webbing, structural ceiling hardpoints)
  - Natural fiber accents

DESIGN PHILOSOPHY
  The channel grid is the skeleton. Everything else attaches to it.
  Nothing is permanent that doesn't need to be.
  Heavy fixed storage is deferred — learn what you need first.
  Hemp webbing serves as both sleeping surface and load tie-down grid.
  Crates secure to the webbing. No loose loads while moving.
"""

# ── CHANNEL GRID ─────────────────────────────────────────────────────────────

CHANNEL_GRID = {
    "material":    "Aluminum Unistrut P1000T — 1-5/8\" slotted channel",
    "finish":      "Mill finish aluminum — no paint, no rust",
    "fasteners":   "Stainless steel spring nuts, bolts, and washers throughout",
    "philosophy":  (
        "Every inch of the channel grid is a potential mount point. "
        "Platform legs, lighting, load securing, shelves, and accessories "
        "all attach to the same grid with no dedicated fixed positions. "
        "Reconfigure without tools by sliding and repositioning attachments."
    ),

    "runs": {
        "wall_port": {
            "description": "Three horizontal runs on the driver (port) side wall",
            "positions": [
                {
                    "name":   "Low",
                    "height": "6 inches from floor",
                    "uses":   "Platform leg attachment, low shelf mounts, gear retention",
                },
                {
                    "name":   "Mid",
                    "height": "20 inches from floor",
                    "uses":   "Platform leg attachment, bench/chaise configuration support",
                },
                {
                    "name":   "High",
                    "height": "48 inches from floor",
                    "uses":   "Overhead storage, lighting mount, upper shelf",
                },
            ],
        },
        "wall_starboard": {
            "description": "Three horizontal runs on the passenger (starboard) side wall",
            "positions":   "Mirrors port side — Low / Mid / High at same heights",
        },
        "ceiling": {
            "description": "Two fore-aft runs along the ceiling",
            "positions": [
                {
                    "name":   "Port ceiling",
                    "offset": "12 inches from centerline toward port",
                    "uses":   "Ambient LED strip mount, structural hardpoint base",
                },
                {
                    "name":   "Starboard ceiling",
                    "offset": "12 inches from centerline toward starboard",
                    "uses":   "Ambient LED strip mount, structural hardpoint base",
                },
            ],
        },
        "floor": {
            "description": "Two fore-aft runs along the floor",
            "positions": [
                {
                    "name":   "Port floor",
                    "offset": "6 inches from port wall",
                    "uses":   "Platform leg base, horse mat edge retention",
                },
                {
                    "name":   "Starboard floor",
                    "offset": "6 inches from starboard wall",
                    "uses":   "Platform leg base, horse mat edge retention",
                },
            ],
        },
    },

    "total_runs":  10,   # 3 port wall + 3 starboard wall + 2 ceiling + 2 floor
    "approx_linear_feet": 120,
    "weight_estimate_lbs": 35,
    "cost_estimate": 280,
}

# ── SLEEP PLATFORM ────────────────────────────────────────────────────────────

SLEEP_PLATFORM = {
    "description": "Full-length hemp webbing sleeping platform on Unistrut frame",
    "length":      "Full van interior length — approximately 90 inches",
    "width":       "Approximately 48 inches (full interior width minus 6\" each side for channel)",

    "frame": {
        "material":    "Aluminum Unistrut P1000T",
        "construction":"Rectangular perimeter frame with cross-members every 18 inches",
        "legs":        "Four legs, each dropping into wall channel at Low or Mid position",
        "adjustment":  "Legs slide in channel — reposition in under 5 minutes, no tools required",
    },

    "surface": {
        "material":       "1-inch natural hemp webbing",
        "pattern":        "Grid — 4-inch spacing in both directions",
        "attachment":     "Woven through perimeter frame and lashed at each crossing",
        "load_rating":    "Platform rated for combined occupant + crate load — spec webbing appropriately",
        "dual_purpose":   (
            "The hemp webbing grid is both the sleeping surface and the load tie-down grid. "
            "Crates and gear secure to the webbing with cam straps. "
            "No separate tie-down hardware needed — the webbing IS the securing system."
        ),
    },

    "topper": {
        "material": "Bamboo lyocell quilted topper",
        "depth":    "3-4 inches",
        "notes":    "Rolls up when platform is in chaise or cargo mode",
    },

    "configurations": {
        "flat": {
            "description": "Full-length sleeping surface",
            "setup":       "All four legs at the same height (all Low or all Mid)",
            "use":         "Sleeping, both dogs on the platform, full gear load",
        },
        "chaise": {
            "description": "Head end raised approximately 30 degrees",
            "setup":       "Head-end legs at Mid channel, foot-end legs at Low channel",
            "use":         "Reading, eating, relaxing — back supported, legs lower",
        },
        "cargo": {
            "description": "Platform folded or removed, full floor access",
            "setup":       "Frame legs removed from channel, platform stored against wall or removed",
            "use":         "Full cargo hauling mode — crates only, no sleeping surface",
        },
    },

    "weight_estimate_lbs": 35,   # frame + webbing + hardware (no DECKED, no subfloor)
    "cost_estimate": 275,        # Unistrut frame + hemp webbing + lyocell topper
}

# ── LOAD SECURING ─────────────────────────────────────────────────────────────

LOAD_SECURING = {
    "philosophy": (
        "No loose loads while the van is moving. "
        "All cargo travels in hard-sided crates secured to the hemp webbing platform. "
        "Cam straps hook through the webbing grid — the webbing IS the tie-down grid. "
        "Crate position on the platform is flexible and determined after walls are up."
    ),

    "crate_securing": {
        "method":    "Cam straps through hemp webbing grid",
        "straps":    "1-inch cam straps with flat hooks — hook through webbing, no hardware needed",
        "rating":    "Match strap rating to crate + contents weight",
        "positions": "TBD — finalize after walls are up and interior is experienced in person",
    },

    "ceiling_hardpoints": {
        "description": (
            "Structural through-bolted hardpoints in the ceiling for securing "
            "crates when stacked or for overhead load retention."
        ),
        "construction": (
            "Through-bolt from interior ceiling channel to van roof structure. "
            "NOT channel-only — must be anchored to van roof ribs or crossmembers. "
            "Use backing plate on exterior roof side to distribute load."
        ),
        "quantity":  4,
        "rating":    "Each hardpoint rated for dynamic load — confirm with fabricator",
        "position":  "TBD — positioned above confirmed crate zone after walls are up",
        "hardware":  "Stainless 3/8\" bolts, stainless backing plates, rubber weatherstrip seal",
    },

    "crate_spec": {
        "notes": (
            "Crate selection TBD. Hard-sided, stackable, and compatible with "
            "cam strap securing through the hemp webbing grid. "
            "Pelican 1650 or similar as baseline reference. "
            "Quantity and arrangement finalized after first interior experience."
        ),
    },
}

# ── LIGHTING PLAN ─────────────────────────────────────────────────────────────

LIGHTING = {
    "control_philosophy": (
        "Analog rocker switches only. No smart lighting, no app control, no dimmers "
        "with digital interfaces. One master cutoff kills all lighting circuits. "
        "Individual zone rockers for granular control. "
        "Single labeled panel near the side door — findable in the dark."
    ),

    "control_panel": {
        "location":    "Near the sliding side door, at comfortable arm height from the platform",
        "type":        "Carling Technologies or Blue Sea rocker panel",
        "switches": [
            {"label": "MASTER",   "function": "Kills all lighting circuits — large rocker, top position"},
            {"label": "AMBIENT",  "function": "Zone 1 — overhead ambient LED strips"},
            {"label": "READING",  "function": "Zone 2 — adjustable reading/task puck lights"},
            {"label": "WORK",     "function": "Zone 3 — utility LED strips, mid wall channel"},
            {"label": "NIGHT",    "function": "Zone 4 — red floor strip, non-disruptive"},
            {"label": "EXTERIOR", "function": "Zone 5 — rear door exterior lights"},
        ],
        "master_note": (
            "The MASTER switch is physically larger and in a distinct position from the zone switches. "
            "One switch, everything off. Standard habit: flip master when leaving the van. "
            "Good battery discipline — no zone left on accidentally."
        ),
    },

    "zones": {
        "zone_1_ambient": {
            "name":        "Overhead Ambient",
            "description": "Warm general illumination for the full interior",
            "fixture":     "LED strip, 2700-3000K warm white",
            "location":    "Both ceiling channels, full length",
            "diffuser":    "Frosted aluminum channel cover — no bare LED dots",
            "color_temp":  "2700K — warm, not clinical",
            "control":     "AMBIENT rocker on panel",
            "wiring":      "Dedicated circuit from Blue Sea DC panel, 10A fuse",
            "weight_est":  "2 lbs",
            "cost_est":    90,
        },
        "zone_2_reading": {
            "name":        "Reading / Task",
            "description": "Adjustable directed light for reading in bed",
            "fixture":     "Two LED puck lights with adjustable arm, warm white",
            "location":    "High wall channel, port and starboard — positioned at head end of platform",
            "adjustment":  "Swivel arm allows direction — mounts in Unistrut, repositionable",
            "control":     "READING rocker on panel (both lights on same circuit)",
            "wiring":      "Dedicated circuit, 10A fuse",
            "weight_est":  "1 lb",
            "cost_est":    65,
            "notes":       "Positioned so each occupant has their own reading light without disturbing the other",
        },
        "zone_3_work": {
            "name":        "Work / Utility",
            "description": "Bright task lighting for cargo mode and utility work",
            "fixture":     "LED strip, 4000K neutral white, higher lumen output",
            "location":    "Mid wall channel, both sides, full length",
            "color_temp":  "4000K — neutral white for accurate color rendering",
            "control":     "WORK rocker on panel",
            "wiring":      "Dedicated circuit, 15A fuse",
            "weight_est":  "2 lbs",
            "cost_est":    80,
            "notes":       "Bright enough for actual work. Not used during sleeping hours.",
        },
        "zone_4_night": {
            "name":        "Night / Navigation",
            "description": "Non-disruptive low light for middle-of-night movement",
            "fixture":     "Red LED strip, low output",
            "location":    "Low floor channel, port side, full length",
            "color_temp":  "Red — preserves night vision, does not wake a sleeping partner",
            "control":     "NIGHT rocker on panel",
            "wiring":      "Dedicated circuit, 10A fuse",
            "weight_est":  "0.5 lbs",
            "cost_est":    30,
            "notes":       (
                "Red light for: dog exits at 3am, finding the toilet, "
                "navigating without waking Lisa. "
                "Low enough not to be visible from outside through cracks."
            ),
        },
        "zone_5_exterior": {
            "name":        "Exterior / Camp",
            "description": "Camp lighting at the rear doors",
            "fixture":     "Two LED puck lights, warm white, weather-resistant",
            "location":    "Above rear doors, exterior mount — wired through door frame",
            "trigger":     "EXTERIOR rocker on panel (manual, not motion-activated — analog-first)",
            "wiring":      "Dedicated circuit, 10A fuse, weatherproof connectors",
            "weight_est":  "1 lb",
            "cost_est":    45,
            "notes":       (
                "Illuminates the camp area behind the van when rear doors are open. "
                "Manual switch only — no motion sensor, no automatic triggering. "
                "Turn on when needed, turn off when done."
            ),
        },
    },

    "wiring": {
        "runs":        "All lighting circuits run in Belden shielded cable in organized loom",
        "connectors":  "Deutsch DT series at all fixtures — weatherproof, field-disconnectable",
        "labels":      "Heat shrink label at both ends of every conductor",
        "total_circuits": 5,
        "total_fuses":    5,
        "panel_source":   "Blue Sea 12-circuit DC panel — circuits 5 and 6 reserved for lighting",
    },

    "total_weight_estimate_lbs": 7,
    "total_cost_estimate":       310,
}

# ── NATURAL FIBER ACCENTS ─────────────────────────────────────────────────────

NATURAL_ACCENTS = {
    "philosophy": (
        "Natural materials where they make sense — not as decoration but as "
        "functional choices that happen to look and feel right. "
        "Jute, hemp, linen, and bamboo alongside the aluminum Unistrut. "
        "The contrast between the industrial channel grid and the natural "
        "fiber surfaces is intentional."
    ),
    "items": [
        {
            "item":     "Jute rope wrap on exposed Unistrut sections",
            "location": "Any Unistrut section that would otherwise be a bare "
                        "edge at contact height — platform perimeter, corner sections",
            "function": "Edge protection, tactile warmth, reduces hard contact points",
            "notes":    "Wrap tightly with 3/8\" natural jute rope, secure with waxed twine",
        },
        {
            "item":     "Hemp canvas toilet privacy curtain",
            "location": "Composting toilet area — curtain on Unistrut slider",
            "function": "Privacy partition, slides fully open when not in use",
            "notes":    "Natural hemp canvas, unbleached, grommeted top edge "
                        "on Unistrut-mounted curtain track",
        },
        {
            "item":     "Linen diffuser shades for reading lights",
            "location": "Zone 2 reading puck lights",
            "function": "Softens and diffuses the directional LED — warm, not harsh",
            "notes":    "Simple linen sleeve over the puck light housing. "
                        "Removable for cleaning.",
        },
        {
            "item":     "Hemp canvas side door curtain",
            "location": "Sliding side door interior — for privacy at camp",
            "function": "Privacy and light control when the van is stationary",
            "notes":    "Tension rod mount — removable, no permanent attachment",
        },
        {
            "item":     "Natural fiber storage pockets",
            "location": "High wall channel, both sides — hung from Unistrut",
            "function": "Small items: phone, book, water bottle, headlamp",
            "notes":    "Hemp canvas pockets with Unistrut hook attachment — repositionable",
        },
    ],
    "cost_estimate": 120,
    "weight_estimate_lbs": 4,
}

# ── STAGE 1A SYSTEMS SUMMARY ─────────────────────────────────────────────────

STAGE_1A_SUMMARY = {
    "channel_grid":     {"weight_lbs": 35,  "cost": 280},
    "sleep_platform":   {"weight_lbs": 35,  "cost": 275},
    "lighting":         {"weight_lbs": 7,   "cost": 310},
    "natural_accents":  {"weight_lbs": 4,   "cost": 120},
    "load_securing":    {"weight_lbs": 5,   "cost": 85},   # hardpoint hardware only
}


def systems_weight():
    return sum(v["weight_lbs"] for v in STAGE_1A_SUMMARY.values())


def systems_cost():
    return sum(v["cost"] for v in STAGE_1A_SUMMARY.values())

# ── ELECTRONICS BAY ───────────────────────────────────────────────────────────

ELECTRONICS_BAY = {
    "description": (
        "Simple enclosed bay for all Victron components. "
        "Protects electronics from dog hair, dust, and moisture. "
        "The MultiPlus 12/3000 is the only component with an internal cooling fan — "
        "it actively pulls air and will accumulate dog hair without filtration. "
        "All other Victron components are passively cooled."
    ),
    "construction": {
        "material":   "3/4-inch plywood or 1/8-inch aluminum panel",
        "door":       "Removable panel — tool-free access preferred (quarter-turn fasteners)",
        "location":   "Forward of sleep platform, against driver-side bulkhead",
        "finish":     "Paint or seal interior surfaces — no bare wood near electronics",
    },
    "ventilation": {
        "intake_vent": {
            "position":   "Low on bay wall (cool air enters at bottom)",
            "type":       "Panel filter frame — 80-120mm with washable foam media",
            "filter":     "Polyester foam filter media — same spec as HVAC pre-filter",
            "sources":    "Comair Rotron panel filter ($8-15) or pantyhose (free, field-proven)",
        },
        "exhaust_vent": {
            "position":   "High on bay wall (hot air exits at top)",
            "type":       "Open grille or louvered vent — no filter on exhaust",
            "note":       "Hot air rises naturally — no powered fan needed for this enclosure",
        },
    },
    "multiplus_filter": {
        "description": "Additional filter directly over the MultiPlus 12/3000 intake grille",
        "reason":      "MultiPlus fan actively pulls air — highest individual risk in the system",
        "method":      "80mm or 120mm panel filter frame mounted over fan intake grille",
        "maintenance": "Inspect monthly. Wash or replace filter media. Keep 3 spares.",
        "field_option":"Pantyhose over intake — free, replaces in 30 seconds, genuinely effective",
    },
    "maintenance": {
        "30_day":   "Inspect and clean MultiPlus intake filter — husky hair loads it fast",
        "90_day":   "Wipe MPPT and Orion-XS heatsink fins with dry cloth",
        "annual":   "Full bay inspection — check all connections and terminals for corrosion",
    },
    "cost_estimate": 45,   # plywood/aluminum + filter frames + spare filter media
    "weight_estimate_lbs": 6,
}

# Update summary to include electronics bay
STAGE_1A_SUMMARY["electronics_bay"] = {"weight_lbs": 6, "cost": 45}
