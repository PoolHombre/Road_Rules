"""
shared/utils.py
Utility functions used across both van and trip modules.
"""

import math
from datetime import date, timedelta


# ── GEOGRAPHY ────────────────────────────────────────────────────────────────

def haversine(lat1, lon1, lat2, lon2):
    """
    Straight-line distance between two GPS coordinates in miles.
    Uses the haversine formula for accuracy over short to medium distances.
    """
    R = 3958.8  # Earth radius in miles
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def route_distance(stops, destinations):
    """
    Total straight-line miles for an ordered list of stop names.
    destinations: dict of name -> (lat, lon)
    stops: list of names including start and end
    """
    total = 0.0
    for i in range(len(stops) - 1):
        lat1, lon1 = destinations[stops[i]]
        lat2, lon2 = destinations[stops[i + 1]]
        total += haversine(lat1, lon1, lat2, lon2)
    return total


def estimated_driving_miles(straight_line_miles, factor=1.3):
    """
    Estimated actual driving miles from straight-line distance.
    1.3x is the standard factor for the western US road network.
    """
    return straight_line_miles * factor


# ── DATE MATH ────────────────────────────────────────────────────────────────

def trip_date(departure: date, day_number: int) -> date:
    """Return the calendar date for a given trip day (1-indexed)."""
    return departure + timedelta(days=day_number - 1)


def day_of_week(departure: date, day_number: int) -> str:
    """Return the weekday name for a given trip day number."""
    return trip_date(departure, day_number).strftime("%A")


def is_weekend(departure: date, day_number: int) -> bool:
    """True if the given trip day falls on Friday, Saturday, or Sunday."""
    return trip_date(departure, day_number).strftime("%A") in ("Friday", "Saturday", "Sunday")


def format_date(d: date) -> str:
    return d.strftime("%a %b %d")


# ── CROWD SCORING ─────────────────────────────────────────────────────────────

# Crowd scores on a 1-10 scale by destination.
# weekday_score, weekend_score
CROWD_PROFILES = {
    "Wichita":            (2, 3),
    "Sioux Falls":        (2, 3),
    "Badlands":           (7, 10),
    "Black Hills":        (6, 9),
    "Theodore Roosevelt": (4, 6),
    "Miles City":         (1, 1),
    "Missouri Breaks":    (2, 2),
    "Fort Benton":        (2, 2),
    "Glacier":            (7, 10),
    "Helena":             (2, 3),
    "Thermopolis":        (2, 4),
    "Bighorns":           (2, 3),
    "Cody":               (3, 5),
    "Medicine Bow":       (2, 3),
    "Oklahoma":           (2, 3),
}


def crowd_score(stop_name: str, departure: date, day_number: int) -> float:
    """
    Return the crowd score (1-10) for a given stop on a given trip day.
    Lower is better.
    """
    profile = CROWD_PROFILES.get(stop_name, (5, 7))
    if is_weekend(departure, day_number):
        return profile[1]
    return profile[0]


def score_itinerary(itinerary: list, departure: date) -> float:
    """
    Score a full itinerary.
    itinerary: list of (stop_name, nights)
    Returns total crowd score — lower is better.
    """
    total = 0.0
    day = 1
    for stop_name, nights in itinerary:
        for n in range(nights):
            total += crowd_score(stop_name, departure, day + n)
        day += nights
    return total


def find_optimal_departure(itinerary: list, month: int = 7, year: int = 2027) -> tuple:
    """
    Try all departure dates in the given month and return the one with
    the lowest total crowd score.
    Returns (best_date, best_score).
    """
    import calendar
    _, days_in_month = calendar.monthrange(year, month)
    results = []
    for day_num in range(1, days_in_month + 1):
        try:
            start = date(year, month, day_num)
            score = score_itinerary(itinerary, start)
            results.append((start, score))
        except ValueError:
            continue
    return min(results, key=lambda x: x[1])


# ── SPECIAL DATE CHECKS ───────────────────────────────────────────────────────

def check_pioneer_day(departure: date, itinerary: list) -> dict:
    """
    Check whether Pioneer Day (July 24) falls in Utah.
    Utah stops: ['Salt Lake City', 'St. George', 'Moab', 'Bonneville']
    Returns dict with date, day_number, stop, in_utah flag.
    """
    utah_stops = {"Salt Lake City", "St. George", "Moab", "Bonneville"}
    pioneer_day = date(departure.year, 7, 24)
    if pioneer_day < departure:
        return {"in_utah": False, "note": "Pioneer Day before departure"}

    day = 1
    for stop_name, nights in itinerary:
        for n in range(nights):
            if trip_date(departure, day + n) == pioneer_day:
                in_utah = stop_name in utah_stops
                return {
                    "date": pioneer_day,
                    "day_number": day + n,
                    "stop": stop_name,
                    "in_utah": in_utah,
                    "note": "⚠️  IN UTAH ON PIONEER DAY" if in_utah else "✅  Not in Utah",
                }
        day += nights
    return {"in_utah": False, "note": "Pioneer Day not within trip dates"}


def check_sturgis(departure: date, itinerary: list, year: int = 2027) -> dict:
    """
    Check whether Black Hills stops overlap with the Sturgis Rally.
    Rally runs approximately August 1-10 annually.
    """
    rally_start = date(year, 8, 1)
    rally_end = date(year, 8, 10)
    black_hills_stops = {"Black Hills", "Badlands", "Rapid City"}

    conflicts = []
    day = 1
    for stop_name, nights in itinerary:
        for n in range(nights):
            d = trip_date(departure, day + n)
            if stop_name in black_hills_stops and rally_start <= d <= rally_end:
                conflicts.append((day + n, d, stop_name))
        day += nights

    return {
        "conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "note": f"⚠️  {len(conflicts)} Sturgis conflict(s)" if conflicts else "✅  Clear of Sturgis",
    }
