"""
trip/data/itinerary.py
Confirmed 28-day itinerary for the 2027 Glacier NP road trip.

Departure: Thursday, July 15, 2027
Return:    Wednesday, August 11, 2027

Dates fixed by parents' Glacier schedule:
  Parents arrive Glacier: July 28
  Parents depart Glacier: ~August 1
  Kevin and Lisa depart Glacier: August 4
"""

from datetime import date

DEPARTURE = date(2027, 7, 15)
RETURN    = date(2027, 8, 11)

# Each entry: (stop_name, nights, sleep_type, drive_note)
# stop_name must match a key in destinations.py
# sleep_type: 'hotel' | 'camp' | 'base' | 'home'

ITINERARY = [
    # Day 1
    ("Wichita",          1, "hotel",  "~450 mi / ~6 hrs via I-35 N from Houston"),
    # Day 2
    ("Sioux Falls",      1, "hotel",  "~460 mi / ~6 hrs via I-135 N → I-90 E"),
    # Days 3-4
    ("Badlands",         2, "mixed",  "~350 mi / ~5 hrs via I-90 W — camp Night 1, hotel Night 2"),
    # Days 5-7
    ("Black Hills",      3, "camp",   "~100 mi / ~1.5 hrs via SD-44"),
    # Days 8-10
    ("Theodore Roosevelt", 3, "mixed","~275 mi / ~4.5 hrs via I-90 W → I-94 W — hotel Night 1, camp Nights 2-3"),
    # Day 11
    ("Miles City",       1, "camp",   "~200 mi / ~3.5 hrs via I-94 W"),
    # Days 12-13
    ("Missouri Breaks",  2, "camp",   "~250 mi / ≤5 hrs via US-191 N each day"),
    # Day 14: Fort Benton is a lunch stop on the drive to Glacier
    ("Fort Benton",      0, "transit","~120 mi to Fort Benton, then ~150 mi to Glacier"),
    # Days 14-20 (7 nights at Glacier, arrival July 28)
    ("Glacier",          7, "base",   "≤3 hrs from Choteau via US-89 → MT-2"),
    # Day 21
    ("Helena",           1, "hotel",  "~200 mi / ≤5 hrs via US-2 → I-15 S"),
    # Days 22-23
    ("Thermopolis",      2, "camp",   "Day 22: ~200 mi via I-15 S → US-287. Day 23: ~150 mi via US-26 → WY-789 → US-20"),
    # Day 24
    ("Bighorns",         1, "camp",   "~120 mi / ~2.5 hrs via US-16 (Ten Sleep Canyon)"),
    # Day 25
    ("Cody",             1, "hotel",  "~90 mi / ~3 hrs via US-14 or US-14A"),
    # Day 26
    ("Medicine Bow",     1, "camp",   "~250 mi / ≤5 hrs via WY-120 → I-25 S → WY-130"),
    # Days 27-28
    ("Oklahoma",         1, "hotel",  "≤5 hrs each leg — two routing options"),
    # Day 28
    ("Houston",          0, "home",   "~500 mi / ~6 hrs via I-35 S → I-45 S"),
]


# ── DERIVED SCHEDULE ──────────────────────────────────────────────────────────

def build_schedule():
    """
    Return a list of dicts, one per night, with:
    {day, date, stop, night_number, sleep_type, drive_note}
    """
    from shared.utils import trip_date, format_date
    schedule = []
    day = 1
    night = 1
    for stop, nights, sleep_type, drive_note in ITINERARY:
        if nights == 0:
            continue
        for n in range(nights):
            d = trip_date(DEPARTURE, day + n)
            schedule.append({
                "day":         day + n,
                "date":        d,
                "date_str":    format_date(d),
                "stop":        stop,
                "night":       night + n,
                "sleep_type":  sleep_type,
                "drive_note":  drive_note if n == 0 else "Local",
            })
        day   += nights
        night += nights
    return schedule


# ── KEY DATES ─────────────────────────────────────────────────────────────────

KEY_DATES = {
    "departure":          date(2027, 7, 15),
    "glacier_arrive":     date(2027, 7, 28),
    "glacier_depart":     date(2027, 8,  4),
    "parents_arrive":     date(2027, 7, 28),
    "parents_depart":     date(2027, 8,  1),  # approximate
    "logan_pass":         date(2027, 8,  3),
    "logan_pass_booking": date(2027, 6,  3),  # 7pm MDT
    "pioneer_day":        date(2027, 7, 24),  # Day 10 — at TRNP, North Dakota ✅
    "sturgis_start":      date(2027, 8,  1),  # Black Hills done July 22 ✅
    "return":             date(2027, 8, 11),
}
