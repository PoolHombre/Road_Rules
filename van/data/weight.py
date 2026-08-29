"""
van/data/weight.py
Weight estimates for the GMC Savana 2500 expedition build.

This file gates Stage C (Wilwood brake upgrade + suspension).
Stage C cannot be specced until the actual Stage 1 loaded weight is known.
Do not guess. Weigh the van at a truck scale after Stage 1 is installed.

Truck scales: CAT Scale locations at most Pilot/Flying J truck stops.
Cost: ~$12. Ask for the printed ticket — front axle + rear axle + total.

GVWR for Savana 2500: 8,600 lbs
Payload capacity:     approximately 2,400-2,600 lbs (varies by config)
"""

# ── BASE VEHICLE ──────────────────────────────────────────────────────────────

BASE_VEHICLE = {
    "description":       "GMC Savana 2500 Extended curb weight (estimated)",
    "estimated_lbs":     5400,   # typical Savana 2500 extended curb weight
    "actual_lbs":        None,   # weigh on purchase — front + rear axle ticket
    "notes":             "Weigh before any build work begins. Get front/rear split.",
}

# ── STAGE 1 WEIGHT ADDITIONS ──────────────────────────────────────────────────
# Estimated weights for major Stage 1 components.
# These are the components that affect suspension and brake spec.

STAGE_1_COMPONENTS = [
    # Heavy items — these drive the spring rate and brake spec
    {"item": "400Ah LiFePO4 battery bank",       "est_lbs": 110,  "actual_lbs": None},
    {"item": "Victron MultiPlus 12/3000",         "est_lbs": 14,   "actual_lbs": None},
    # DECKED VG2 REMOVED — deferred to later stage (200-275 lbs, $1,850)
    {"item": "Nature's Head composting toilet",   "est_lbs": 28,   "actual_lbs": None},
    {"item": "Insulation — Noico damping mat (50 sqft @ 0.12 lbs/sqft)",  "est_lbs": 6,    "actual_lbs": None},
    {"item": "Insulation — Thinsulate SM600L (60 sqft @ 0.05 lbs/sqft)",  "est_lbs": 3,    "actual_lbs": None},
    {"item": "Insulation — XPS rigid board (10 sheets, 1-inch)",          "est_lbs": 18,   "actual_lbs": None},
    {"item": "Insulation — Great Stuff foam (3 cans, minimal material)",  "est_lbs": 2,    "actual_lbs": None},
    # Note: Original estimate was 65 lbs (included Dynamat + spray foam + Polyiso + Thinsulate)
    # New stack (Noico + XPS + Thinsulate + targeted Great Stuff): ~29 lbs — saves ~36 lbs
    {"item": "Bamboo wall panels + cladding",     "est_lbs": 45,   "actual_lbs": None},
    {"item": "Horse stall mats x2 (no subfloor — mats on van floor directly)", "est_lbs": 40, "actual_lbs": None},
    {"item": "Unistrut framework (aluminum)",      "est_lbs": 35,   "actual_lbs": None},
    {"item": "Wiring, cable, connectors",         "est_lbs": 40,   "actual_lbs": None},
    {"item": "Water tank (empty)",                "est_lbs": 15,   "actual_lbs": None},
    {"item": "Plumbing components",               "est_lbs": 12,   "actual_lbs": None},
    {"item": "OutEquipPro Summit 2 AC unit",      "est_lbs": 45,   "actual_lbs": None},
    {"item": "Solar panels (2x 100W rigid)",      "est_lbs": 28,   "actual_lbs": None},
    {"item": "Distribution panels (Blue Sea x2)", "est_lbs": 8,    "actual_lbs": None},
    {"item": "CB radio, Starlink adapter, misc",  "est_lbs": 10,   "actual_lbs": None},
    {"item": "Sleep platform + hemp webbing",     "est_lbs": 20,   "actual_lbs": None},
    {"item": "Misc hardware, fasteners",          "est_lbs": 20,   "actual_lbs": None},
    {"item": "Lighting system — 5 zones (strips, pucks, panel)", "est_lbs": 7, "actual_lbs": None},
    {"item": "Ceiling hardpoints hardware (4x through-bolts, backing plates)", "est_lbs": 3, "actual_lbs": None},
    {"item": "Natural fiber accents (jute, hemp canvas, linen)", "est_lbs": 4, "actual_lbs": None},
]

# ── STAGE 2 WEIGHT ADDITIONS ──────────────────────────────────────────────────

STAGE_2_COMPONENTS = [
    {"item": "Aluminess front bumper 85 lbs, stock bumper removed ~85 lbs — net 0 lbs", "est_lbs": 0, "actual_lbs": None},
    {"item": "Warn VR EVO 12-S winch",            "est_lbs": 95,   "actual_lbs": None},
    {"item": "Lighting (all)",                    "est_lbs": 20,   "actual_lbs": None},
    {"item": "Recovery gear (full kit)",          "est_lbs": 55,   "actual_lbs": None},
    {"item": "Cameras + DVR + wiring",            "est_lbs": 15,   "actual_lbs": None},
    {"item": "Safe (Vaultek LifePod)",            "est_lbs": 4,    "actual_lbs": None},
    {"item": "Safe (SecureIt Fast Box 40)",       "est_lbs": 22,   "actual_lbs": None},
]

# ── STAGE 3 WEIGHT ADDITIONS ──────────────────────────────────────────────────

STAGE_3_COMPONENTS = [
    {"item": "Primus AIR Silent X turbine",       "est_lbs": 13,   "actual_lbs": None},
    {"item": "Primus 27-ft tower kit",            "est_lbs": 45,   "actual_lbs": None},
    {"item": "Aluminess roof rack",               "est_lbs": 95,   "actual_lbs": None},
    {"item": "Aluminess storage box",             "est_lbs": 35,   "actual_lbs": None},
    {"item": "Alu-Cab 270° Shadow Awning RHS (2.6m)",           "est_lbs": 53, "actual_lbs": None},
    {"item": "Alu-Cab Shower Cube + mounting brackets",          "est_lbs": 22, "actual_lbs": None},
    {"item": "180° side awning LHS (Roam or OVS HD Nomadic)",   "est_lbs": 18, "actual_lbs": None},
    # Total awning system: ~93 lbs vs original Roam 8-ft + annex ~28 lbs
    # Weight increase: +65 lbs for full three-side coverage + shower capability (see VAN-019)
    {"item": "Dometic CFX3 45L fridge",           "est_lbs": 33,   "actual_lbs": None},
    {"item": "Cast iron cookware (full set)",      "est_lbs": 38,   "actual_lbs": None},
    {"item": "Jetboil + Instant Pot + misc kitchen","est_lbs": 12,  "actual_lbs": None},
    {"item": "Dog kennels (Gunner G1 + Sleepypod)","est_lbs": 22,  "actual_lbs": None},
    {"item": "Dog gear, misc",                    "est_lbs": 15,   "actual_lbs": None},
]

# ── OPERATIONAL LOADS (not build weight, but affects brake spec) ──────────────

OPERATIONAL = {
    "fresh_water_full_lbs":     250,   # 30 gallons × 8.34 lbs/gal
    "fresh_water_half_lbs":     125,
    "food_and_supplies_lbs":    80,
    "clothing_gear_lbs":        120,
    "tools_spare_parts_lbs":    60,
    "briefcase_solar_lbs":      25,
    "occupants_lbs":            400,   # 2 adults estimated
    "dogs_lbs":                 95,    # Tango ~65 lbs + Saki ~30 lbs
    "total_operational_est":    1030,
}

# ── GVWR AND PAYLOAD ─────────────────────────────────────────────────────────

GVWR = {
    "gvwr_lbs":            8600,
    "notes":               "Savana 2500 GVWR. Do not exceed.",
}


# ── CALCULATIONS ──────────────────────────────────────────────────────────────

def stage_weight(components, use_actual=False):
    """Sum estimated or actual weights for a component list."""
    total = 0
    for c in components:
        val = c.get("actual_lbs") if use_actual else c.get("est_lbs", 0)
        if val is not None:
            total += val
    return total


def estimated_loaded_weight_after_stage(stage: int) -> dict:
    """
    Return estimated total loaded weight after a given build stage,
    including full operational load.
    """
    base = BASE_VEHICLE["estimated_lbs"]
    s1 = stage_weight(STAGE_1_COMPONENTS) if stage >= 1 else 0
    s2 = stage_weight(STAGE_2_COMPONENTS) if stage >= 2 else 0
    s3 = stage_weight(STAGE_3_COMPONENTS) if stage >= 3 else 0
    ops = OPERATIONAL["total_operational_est"]
    total = base + s1 + s2 + s3 + ops
    payload = total - base
    remaining_payload = GVWR["gvwr_lbs"] - total
    return {
        "base_vehicle_lbs":   base,
        "stage_additions_lbs": s1 + s2 + s3,
        "operational_lbs":    ops,
        "total_lbs":          total,
        "payload_used_lbs":   payload,
        "gvwr_lbs":           GVWR["gvwr_lbs"],
        "remaining_payload":  remaining_payload,
        "over_gvwr":          remaining_payload < 0,
    }


WEIGH_INSTRUCTIONS = """
HOW TO WEIGH THE VAN — REQUIRED BEFORE STAGE C

1. Find a CAT Scale: pilot.com/content/scale-locator.aspx
   (Most Pilot/Flying J truck stops have them. Cost: ~$12.)

2. Pull onto the scale with the van in its Stage 1 fully-loaded state:
   - Full fresh water tank
   - All tools and gear loaded as for a trip
   - Both dogs and both people in the van

3. Request the printed ticket. It will show:
   - Steer axle weight (front)
   - Drive axle weight (rear)
   - Total gross weight

4. Record all three numbers in this file:
   BASE_VEHICLE['actual_lbs'] = total_from_ticket
   (and update STAGE_1_COMPONENTS actuals as needed)

5. Bring this data to the brake shop for Stage C spec.
   The Wilwood spring rate and shock valving are calculated from
   the loaded rear axle weight specifically.

Do not spec Stage C from the estimated weights. Weigh the actual van.
"""
