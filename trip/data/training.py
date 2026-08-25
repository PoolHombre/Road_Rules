"""
trip/data/training.py
BJJ / Gracie Barra locations and training alternatives by stop.

Verify all locations at graciebarra.com before the trip — the network
expands continuously and this data may be stale by July 2027.

Training philosophy on the road:
- Prioritize GB when available — drop-in fees typically $20-30
- Trail running with Tango on camp days — he is the running partner
- Hotel bodyweight circuits when no gym is available
- Swimming at rivers and lakes counts — Flathead, Yellowstone, Missouri
- The trip averages 8-12 hiking miles on active days — real training
"""

# ── CONFIRMED LOCATIONS ───────────────────────────────────────────────────────

CONFIRMED = [
    {
        "stop":     "Tulsa, OK",
        "school":   "Gracie JJ Tulsa",
        "address":  "2911 E 91st St, Tulsa, OK 74137",
        "website":  "gracietulsa.com",
        "phone":    "(918) 994-5425",
        "type":     "Gracie Academy Certified",
        "drop_in":  True,
        "fee":      "$25 estimated",
        "trip_day": "27 (if routing through Tulsa)",
        "notes":    "Gracie Academy Certified — highest credential in the Gracie lineage. "
                    "Call ahead to confirm drop-in availability.",
    },
    {
        "stop":     "Oklahoma City, OK",
        "school":   "Lovato's School of BJJ",
        "address":  "4322 NW 39th St, Oklahoma City, OK 73112",
        "website":  "lovatobjj.com",
        "type":     "World-class — not GB brand",
        "drop_in":  True,
        "fee":      "$30 estimated",
        "trip_day": "27 (if routing through OKC)",
        "notes":    "Rafael Lovato Jr. — multiple world champion. Not GB branded but world-class. "
                    "Call ahead for drop-in availability.",
    },
]

# ── CHECK BEFORE TRIP — LIKELY BUT UNCONFIRMED ────────────────────────────────

CHECK_BEFORE_TRIP = [
    {
        "stop":    "Wichita, KS",
        "notes":   "Growing city — GB likely has a location by 2027. Check graciebarra.com.",
        "trip_day": 1,
    },
    {
        "stop":    "Sioux Falls, SD",
        "notes":   "Growing rapidly — check graciebarra.com before trip.",
        "trip_day": 2,
    },
    {
        "stop":    "Rapid City, SD",
        "notes":   "Tourist destination with year-round population — check graciebarra.com.",
        "trip_day": "3-4",
    },
    {
        "stop":    "Bismarck, ND",
        "notes":   "Most likely ND city to have a GB location. ~100 mi east of Medora.",
        "trip_day": "8-10 (not on direct route)",
    },
    {
        "stop":    "Great Falls, MT",
        "notes":   "Mid-size Montana city — check graciebarra.com.",
        "trip_day": "13 (if routing through Great Falls)",
    },
    {
        "stop":    "Helena, MT",
        "notes":   "State capital — possible GB location. Check graciebarra.com.",
        "trip_day": 21,
    },
    {
        "stop":    "Fort Collins, CO",
        "notes":   "Large university city — likely has GB. Check graciebarra.com if routing through Colorado.",
        "trip_day": "27 (if routing through Colorado)",
    },
]

# ── NO BJJ AVAILABLE ─────────────────────────────────────────────────────────

NO_BJJ = [
    {"stop": "Badlands / Rapid City area", "trip_day": "3-4", "alternative": "Bodyweight circuit at hotel. Morning hike in the Badlands before heat."},
    {"stop": "Black Hills / Custer",       "trip_day": "5-7", "alternative": "Black Hills NF trail run with Tango. Sunday Gulch Trail (3.8 mi)."},
    {"stop": "Medora / TRNP",              "trip_day": "8-10","alternative": "Little Missouri Grassland trail run. Buck Hill (0.2 mi) for a quick 360° view."},
    {"stop": "Miles City, MT",             "trip_day": 11,    "alternative": "Active recovery. Walk the Yellowstone River BLM with both dogs. Let Tango swim."},
    {"stop": "Missouri Breaks / Fort Benton","trip_day":"12-13","alternative": "River walk, swimming with Tango in the Missouri. Rocky Mountain Front hike near Choteau."},
    {"stop": "Glacier area",               "trip_day":"14-20","alternative": "Flathead NF trail hike (Day 16 — both dogs). Grinnell Glacier hike Day 19 (Kevin + Tango)."},
    {"stop": "Thermopolis / Dubois, WY",   "trip_day":"22-23","alternative": "Shoshone NF trail hike. River Bend Bark Park off-leash run for the dogs."},
    {"stop": "Bighorn Mountains",          "trip_day": 24,    "alternative": "Bighorn NF trail run or hike. Cold nights at elevation — run to warm up at dawn."},
    {"stop": "Cody, WY",                   "trip_day": 25,    "alternative": "Hotel gym if available. Shoshone River access for a morning walk."},
    {"stop": "Medicine Bow / Laramie, WY", "trip_day": 26,    "alternative": "UW BJJ clubs may have open mat — check. Snowy Range alpine hike from camp."},
]

# ── HOTEL BODYWEIGHT CIRCUIT ──────────────────────────────────────────────────

HOTEL_CIRCUIT = {
    "description": "25-minute bodyweight circuit for hotel rooms with no gym",
    "rounds": 3,
    "rest_between_rounds": "90 seconds",
    "exercises": [
        {"name": "Push-up pyramid",   "sets": "1-2-3-4-5-4-3-2-1", "notes": "Full range, controlled descent"},
        {"name": "Squat pyramid",     "sets": "1-2-3-4-5-4-3-2-1", "notes": "Pause at bottom"},
        {"name": "Plank hold",        "duration": "60 seconds",     "notes": "Hollow body position"},
        {"name": "Hip escapes",       "reps": "10 each side",       "notes": "BJJ guard retention drill on the carpet"},
        {"name": "Technical stand-up","reps": "10 each side",       "notes": "BJJ movement drill"},
        {"name": "Dead bug",          "reps": "10 each side",       "notes": "Core stability"},
    ],
    "notes": "This fits in any hotel room with no equipment. Adapt based on energy level after driving days.",
}

# ── OPEN WATER SWIMMING ───────────────────────────────────────────────────────

SWIMMING_SPOTS = [
    {"location": "Yellowstone River, Miles City",    "day": 11, "notes": "BLM access, cottonwood groves. Tango swims."},
    {"location": "Missouri River, James Kipp BLM",   "day": 12, "notes": "Swim in the actual Lewis and Clark river. Tango swims."},
    {"location": "Lake McDonald, Glacier",           "day": 15, "notes": "Turquoise glacier water. Cold. Worth it."},
    {"location": "Flathead Lake",                    "day": 19, "notes": "Largest freshwater lake west of Mississippi. Dogs welcome at shore parks."},
    {"location": "Boysen Reservoir, near Thermopolis","day":23, "notes": "Warm reservoir. Dogs welcome. After the hot springs."},
    {"location": "Wyoming rivers",                   "day": 22, "notes": "Wind River or Dubois area streams. Cold mountain water."},
]
