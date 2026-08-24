"""
trip/rules/route_rules.py
Governing rules for the 2027 road trip routing and daily planning.
These rules were established during the planning process and validated
through crowd analysis and GPS optimization.
"""

ROUTE_RULES = {

    "max_driving_hours": 5,
    "max_driving_hours_note": (
        "≤5 hours on most days. A small number of departure and arrival legs "
        "run up to 6 hours — these are accepted exceptions on Days 1, 2, and 28."
    ),

    "direction": "clockwise",
    "direction_note": (
        "Clockwise confirmed mathematically optimal. Outbound goes southwest to northwest "
        "(or northwest directly in Plan B). Return sweeps southeast. "
        "Clockwise beats counterclockwise by 249 straight-line miles (~325 driving miles)."
    ),

    "no_backtracking": True,
    "no_backtracking_note": (
        "Every mile driven should move generally toward the next destination. "
        "Detours must be evaluated for their cost in miles and time. "
        "Moab was dropped because it added 220 driving miles of backtracking. "
        "White Sands was dropped for the same reason."
    ),

    "hotel_frequency": "every 4th night maximum",
    "hotel_frequency_note": (
        "Never more than 3 consecutive camp nights outside Glacier. "
        "The Glacier 7-night base camp is the intentional exception. "
        "Hotel nights serve a specific function: hot shower, laundry, real bed. "
        "They are not optional — they sustain the camping quality."
    ),

    "hotel_rules": {
        "breakfast": "Always provided — hotel breakfast or continental. Never cook at a hotel.",
        "dinner":    "Always out at a local restaurant. Never cook at a hotel.",
        "cooking":   "Zero cooking on hotel nights.",
    },

    "driving_day_meals": {
        "breakfast": "At the hotel before checkout or from van supplies.",
        "lunch":     "Van snacks (wraps, fruit, almonds, cheese) or a deli stop in a good town.",
        "dinner":    "Camp dinner if arriving at camp with daylight. Hotel dinner out if hotel night.",
    },

    "camp_arrival": "Before 4pm. Finding a dispersed site in the dark is miserable.",

    "fire_restrictions": (
        "Check inciweb.nwcg.gov every morning during the trip. "
        "July and August are peak fire season across the western US. "
        "Many sites will be under Stage 1 or Stage 2 fire restrictions — "
        "no ground fires, sometimes no charcoal. "
        "The Coleman 2-burner and Jetboil work regardless of restriction level. "
        "Never assume a campfire is allowed without checking."
    ),
}


CAMP_PRIORITY = [
    {
        "rank":  1,
        "type":  "NF/BLM Dispersed",
        "cost":  "Free",
        "notes": (
            "No fees, no reservations, maximum flexibility, dogs on leash, deepest solitude. "
            "Find using onX Maps or FreeRoam app. "
            "Rules: 150 feet from water, use established sites, 14-day limit per 28-day period "
            "on any single National Forest. Pack everything in and out. "
            "Confirm no fire restrictions before building a fire."
        ),
    },
    {
        "rank":  2,
        "type":  "NF/BLM Developed Campground",
        "cost":  "$10-25/night",
        "notes": (
            "Fire rings, vault toilets, water. Some reservable, some first-come. "
            "Dogs on leash throughout. More amenities than dispersed, still away from RV density."
        ),
    },
    {
        "rank":  3,
        "type":  "National Park Campground",
        "cost":  "$20-35/night",
        "notes": (
            "Reservation-based, higher fees, specific dog rules. "
            "Dogs typically allowed in campgrounds and parking areas only — "
            "NOT on backcountry trails (except Tango as ADA service animal). "
            "Worth it for: Sage Creek Badlands (free/primitive), "
            "TRNP Cottonwood (riverside, reservation), Glacier Apgar (hookups)."
        ),
    },
    {
        "rank":  4,
        "type":  "State Park Campground",
        "cost":  "$15-30/night",
        "notes": (
            "Good facilities, hookups often available. Best for recharge nights. "
            "Dogs on leash. Examples: Sylvan Lake (Black Hills), "
            "Boysen Reservoir (near Thermopolis), Tongue River (Miles City)."
        ),
    },
    {
        "rank":  5,
        "type":  "Private Campground",
        "cost":  "$35-60/night",
        "notes": "Last resort only — when logistics require it. Higher cost, lower solitude.",
    },
]


CAMPING_RESOURCES = [
    {"name": "recreation.gov",      "use": "TRNP Cottonwood, Glacier Apgar, Vedauwoo — reservation campgrounds"},
    {"name": "onX Maps",            "use": "Find BLM/NF dispersed spots — shows land ownership boundaries — app required"},
    {"name": "FreeRoam",            "use": "Free camping finder for the van and overlanding community — freeroam.io"},
    {"name": "BLM Montana/Dakotas", "use": "Missouri Breaks, Miles City area, general MT/ND BLM land — blm.gov/montana-dakotas"},
    {"name": "Bighorn NF",          "use": "Camping, fire restrictions, trail info — fs.usda.gov/bighorn"},
    {"name": "Shoshone NF",         "use": "First national forest — Dubois/Cody area — fs.usda.gov/shoshone"},
    {"name": "Medicine Bow NF",     "use": "Snowy Range, Vedauwoo, SE Wyoming — fs.usda.gov/mbrtb"},
    {"name": "Flathead NF",         "use": "Glacier area — dog-friendly trails — fs.usda.gov/flathead"},
    {"name": "InciWeb",             "use": "Fire restriction monitoring — check every morning — inciweb.nwcg.gov"},
]
