"""
van/data/vendors.py
Supplier contacts, lead times, and order status for the van build.

Update 'status' as items are ordered and received.
Status: 'not_ordered' | 'ordered' | 'received' | 'installed'
"""

VENDORS = {

    # ── ELECTRICAL — VICTRON ECOSYSTEM ───────────────────────────────────────

    "victron": {
        "name":     "Victron Energy",
        "website":  "victronenergy.com",
        "buy_from": "altE (altEstore.com) or Victron dealer — do not buy grey market",
        "lead_time":"1-5 days from altE (in stock)",
        "notes":    "All Victron components should be purchased together for warranty and compatibility",
        "items": [
            {"part": "MultiPlus 12/3000",      "sku": "PMP122305010",  "status": "not_ordered"},
            {"part": "SmartSolar MPPT 100/50", "sku": "SCC110050210",  "status": "not_ordered"},
            {"part": "Orion-XS 12/12-30A",     "sku": "ORI122430020",  "status": "not_ordered"},
            {"part": "Lynx Distributor",        "sku": "LYN060102000",  "status": "not_ordered"},
            {"part": "SmartShunt 500A",         "sku": "SHU050150050",  "status": "not_ordered"},
        ],
    },

    # ── ELECTRICAL — BLUE SEA ─────────────────────────────────────────────────

    "blue_sea": {
        "name":     "Blue Sea Systems",
        "website":  "bluesea.com",
        "buy_from": "Amazon, West Marine, or bluesea.com direct",
        "lead_time":"1-5 days",
        "notes":    "Use Blue Sea throughout for panels and bus bars — consistent quality",
        "items": [
            {"part": "12-circuit fused DC panel",  "model": "5026",   "status": "not_ordered"},
            {"part": "AC 4-circuit panel",         "model": "8077",   "status": "not_ordered"},
            {"part": "2506 ground bus bar",        "model": "2506",   "status": "not_ordered"},
            {"part": "30A ANL fuse holder",        "model": "5182",   "status": "not_ordered"},
        ],
    },

    # ── BATTERIES ────────────────────────────────────────────────────────────

    "battle_born": {
        "name":     "Battle Born Batteries",
        "website":  "battlebornbatteries.com",
        "phone":    "(855) 292-2831",
        "lead_time":"1-2 weeks (in stock typically)",
        "notes":    "4x 100Ah 12V LiFePO4 in parallel = 400Ah bank. "
                    "Alternatively: 2x 200Ah. Confirm BMS specs with Victron compatibility.",
        "status":   "not_ordered",
    },

    # ── WIND TURBINE — ORDER FIRST ────────────────────────────────────────────

    "primus_wind": {
        "name":         "Primus Wind Power",
        "website":      "primuswindpower.com",
        "phone":        "(720) 684-4000",
        "email":        "info@primuswindpower.com",
        "lead_time":    "4-6 WEEKS — order before any other Stage 3 items",
        "urgency":      "CRITICAL — this is the longest lead time item in the entire build",
        "items": [
            {"part": "AIR Silent X 440W turbine",      "model": "1-ARXS-10-48", "status": "not_ordered"},
            {"part": "27-ft tilt-up guyed tower kit",  "model": "Tower-27",     "status": "not_ordered"},
            {"part": "Digital Control Panel",           "model": "DCP",          "status": "not_ordered"},
        ],
        "notes": (
            "Call to confirm availability before ordering — sometimes backordered. "
            "Order the turbine body, blades, tower kit, and control panel in one order. "
            "The pre-wire in Stage 1 (30A breaker, Anderson connector, cable gland) "
            "must be installed before the turbine arrives."
        ),
    },

    # ── ALUMINESS ────────────────────────────────────────────────────────────

    "aluminess": {
        "name":     "Aluminess Products",
        "website":  "aluminess.com",
        "phone":    "(619) 449-7110",
        "lead_time":"8-12 weeks — custom fabricated to order",
        "notes":    "Custom aluminum products. Measure twice. Lead time is long — order early. "
                    "Three pieces: front winch bumper (Stage 2), roof rack (Stage 3), storage box (Stage 3). "
                    "All three can be ordered at once to save on shipping.",
        "items": [
            {"part": "Front winch bumper — Savana 2500", "status": "not_ordered"},
            {"part": "Roof rack — Savana extended",      "status": "not_ordered"},
            {"part": "Deluxe storage box",               "status": "not_ordered"},
        ],
    },

    # ── WINCH ─────────────────────────────────────────────────────────────────

    "warn": {
        "name":     "Warn Industries",
        "website":  "warn.com",
        "buy_from": "Amazon, Summit Racing, or 4WP",
        "lead_time":"1-5 days",
        "items": [
            {"part": "VR EVO 12-S winch", "model": "103255", "status": "not_ordered"},
        ],
    },

    # ── BRAKES — WILWOOD ──────────────────────────────────────────────────────

    "wilwood": {
        "name":     "Wilwood Engineering",
        "website":  "wilwood.com",
        "phone":    "(805) 388-1188",
        "lead_time":"2-4 weeks (some kits in stock)",
        "notes":    (
            "DO NOT ORDER until Stage 1 loaded weight is known. "
            "The rear drum-to-disc conversion must include the integrated parking brake — "
            "specify this explicitly when ordering. "
            "Call tech line to confirm correct kit for Savana 2500 with the build weight data."
        ),
        "status":   "pending_weight_data",
        "items": [
            {"part": "Dynalite front brake kit — 13\" rotor",              "status": "pending_weight"},
            {"part": "Dynapro rear drum-to-disc WITH integrated parking brake", "status": "pending_weight"},
            {"part": "Stainless steel brake lines (full set)",              "status": "pending_weight"},
        ],
    },

    # ── SUSPENSION ────────────────────────────────────────────────────────────

    "bilstein": {
        "name":     "Bilstein",
        "website":  "bilstein.com",
        "buy_from": "Amazon, Rock Auto, or bilstein.com",
        "lead_time":"1-5 days",
        "notes":    "Bilstein 5100 shocks for Savana 2500. Confirm spring rate with build weight.",
        "status":   "pending_weight_data",
        "items": [
            {"part": "5100 front shocks (pair)",  "status": "pending_weight"},
            {"part": "5100 rear shocks (pair)",   "status": "pending_weight"},
        ],
    },

    # ── CLIMATE ──────────────────────────────────────────────────────────────

    "outequippro": {
        "name":     "OutEquipPro",
        "website":  "outequippro.com",
        "lead_time":"2-4 weeks",
        "notes":    "Summit 2 AC/heat unit. 12V DC rooftop. 10,000 BTU cool / 4,500 BTU heat. "
                    "Purchase with the wired thermostat. WiFi/app features are disabled on install — "
                    "wired thermostat only, per analog-first philosophy.",
        "items": [
            {"part": "Summit 2 DC AC unit",    "status": "not_ordered"},
            {"part": "Wired thermostat",        "status": "not_ordered"},
        ],
    },

    # ── REFRIGERATION ────────────────────────────────────────────────────────

    "dometic": {
        "name":     "Dometic",
        "website":  "dometic.com",
        "buy_from": "Amazon, REI, Camping World",
        "lead_time":"1-5 days (in stock)",
        "items": [
            {"part": "CFX3 45L compressor fridge/freezer", "model": "CFX3 45", "status": "not_ordered"},
        ],
    },

    # ── SANITATION ────────────────────────────────────────────────────────────

    "natures_head": {
        "name":     "Nature's Head",
        "website":  "natureshead.net",
        "lead_time":"1-2 weeks",
        "items": [
            {"part": "Nature's Head composting toilet", "status": "not_ordered"},
        ],
    },

    # ── MONITORING ───────────────────────────────────────────────────────────

    "simarine": {
        "name":     "Simarine",
        "website":  "simarine.net",
        "buy_from": "Amazon or simarine.net direct",
        "lead_time":"1-2 weeks",
        "items": [
            {"part": "PICO battery monitor", "status": "not_ordered"},
        ],
    },

    # ── SAFETY / RECOVERY ─────────────────────────────────────────────────────

    "factor_55": {
        "name":     "Factor 55",
        "website":  "factor55.com",
        "lead_time":"1-5 days",
        "items": [
            {"part": "FlatLink shackle", "model": "00020", "status": "not_ordered"},
        ],
    },

    "maxtrax": {
        "name":     "MAXTRAX",
        "website":  "maxtrax.com.au",
        "buy_from": "Amazon US or maxtrax.com",
        "lead_time":"1-2 weeks",
        "items": [
            {"part": "MKII recovery boards (pair) — orange", "status": "not_ordered"},
        ],
    },

    # ── COMMUNICATIONS ────────────────────────────────────────────────────────

    "garmin": {
        "name":     "Garmin",
        "website":  "garmin.com",
        "buy_from": "Amazon, REI, Best Buy",
        "lead_time":"1-5 days",
        "notes":    "inReach Mini 2 requires a Garmin satellite subscription. "
                    "Activate before departure. Test two-way messaging before the trip.",
        "items": [
            {"part": "inReach Mini 2", "status": "not_ordered"},
        ],
    },

    # ── ROAM ─────────────────────────────────────────────────────────────────

    "roam": {
        "name":     "Roam Adventure Co",
        "website":  "roamadventureco.com",
        "lead_time":"1-2 weeks",
        "items": [
            {"part": "8-ft awning",    "status": "not_ordered"},
            {"part": "Awning room annex","status": "not_ordered"},
        ],
    },

    # ── WRAP ──────────────────────────────────────────────────────────────────

    "wrap_shop": {
        "name":     "TBD — local Houston area wrap shop",
        "website":  "TBD",
        "lead_time":"2-4 weeks (schedule after all hardware installed)",
        "notes":    (
            "Get quotes from 3 shops minimum. Bring the Avery Dennison color specs: "
            "SW900 ColorFlow Fresh Spring (252-S) upper / Satin Khaki Green mid / Matte Adobe lower. "
            "The artist vector files must be delivered to the shop before scheduling. "
            "DO NOT schedule until ALL exterior hardware is installed — no exceptions."
        ),
        "status":   "not_started",
    },

    # ── DOG GEAR ─────────────────────────────────────────────────────────────

    "gunner": {
        "name":     "Gunner Kennels",
        "website":  "gunnerkennels.com",
        "lead_time":"1-2 weeks",
        "notes":    "G1 kennel for Tango (husky). Measure Tango's standing height and length "
                    "before ordering to confirm correct size.",
        "items": [
            {"part": "G1 kennel — large", "status": "not_ordered"},
        ],
    },
}


def items_to_order_now():
    """Return vendors with items that should be ordered immediately."""
    urgent = []
    for vendor_key, vendor in VENDORS.items():
        if "urgency" in vendor:
            urgent.append((vendor_key, vendor))
    return urgent


def items_pending_weight():
    """Return all items that cannot be ordered until Stage 1 weight is known."""
    pending = []
    for vendor_key, vendor in VENDORS.items():
        if vendor.get("status") == "pending_weight_data":
            pending.append((vendor_key, vendor))
        for item in vendor.get("items", []):
            if "pending_weight" in item.get("status", ""):
                pending.append((vendor_key, item))
    return pending


def order_status_summary():
    """Return count of items by status across all vendors."""
    counts = {"not_ordered": 0, "ordered": 0, "received": 0, "installed": 0}
    for vendor in VENDORS.values():
        for item in vendor.get("items", []):
            status = item.get("status", "not_ordered")
            if status in counts:
                counts[status] += 1
    return counts
