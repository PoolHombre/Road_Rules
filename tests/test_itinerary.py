"""
tests/test_itinerary.py
Validate the trip itinerary — dates, key events, schedule integrity.
These tests lock in the confirmed planning decisions so they can never
silently regress when data files are updated.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from datetime import date

from shared.utils import (haversine, trip_date, is_weekend,
                           check_pioneer_day, check_sturgis, format_date)
from trip.data.itinerary import (ITINERARY, KEY_DATES, build_schedule,
                                  DEPARTURE, RETURN)
from trip.data.destinations import DESTINATIONS
from trip.rules.dog_rules import DOGS


# ── DEPARTURE AND RETURN ──────────────────────────────────────────────────────

def test_departure_date():
    """Departure must be Thursday July 15, 2027 — fixed by parents' schedule."""
    assert DEPARTURE == date(2027, 7, 15), f"Departure is {DEPARTURE}, must be 2027-07-15"
    assert DEPARTURE.strftime("%A") == "Thursday", "Departure must be a Thursday"


def test_return_date():
    """Return must be Wednesday August 11, 2027."""
    assert RETURN == date(2027, 8, 11), f"Return is {RETURN}, must be 2027-08-11"
    assert RETURN.strftime("%A") == "Wednesday", "Return must be a Wednesday"


def test_trip_is_28_days():
    """Trip must be exactly 28 days."""
    delta = (RETURN - DEPARTURE).days
    assert delta == 27, f"Trip is {delta+1} days, must be 28"  # 27 nights = 28 days


# ── KEY DATES ─────────────────────────────────────────────────────────────────

def test_glacier_arrive():
    """Glacier arrival must be July 28 — same day parents arrive."""
    assert KEY_DATES["glacier_arrive"] == date(2027, 7, 28)
    assert KEY_DATES["glacier_arrive"].strftime("%A") == "Wednesday"


def test_glacier_depart():
    """Glacier departure must be August 4."""
    assert KEY_DATES["glacier_depart"] == date(2027, 8, 4)
    assert KEY_DATES["glacier_depart"].strftime("%A") == "Wednesday"


def test_glacier_is_7_nights():
    """Glacier stay must be exactly 7 nights."""
    nights = (KEY_DATES["glacier_depart"] - KEY_DATES["glacier_arrive"]).days
    assert nights == 7, f"Glacier is {nights} nights, must be 7"


def test_parents_arrive_same_day_as_kevin():
    """Parents must arrive Glacier same day as Kevin and Lisa."""
    assert KEY_DATES["parents_arrive"] == KEY_DATES["glacier_arrive"]


def test_logan_pass_is_tuesday():
    """Logan Pass day must be a Tuesday — best weekday crowd profile."""
    assert KEY_DATES["logan_pass"] == date(2027, 8, 3)
    assert KEY_DATES["logan_pass"].strftime("%A") == "Tuesday"


def test_logan_pass_booking_date():
    """Logan Pass shuttle booking opens June 3 (60 days before August 3)."""
    assert KEY_DATES["logan_pass_booking"] == date(2027, 6, 3)
    delta = (KEY_DATES["logan_pass"] - KEY_DATES["logan_pass_booking"]).days
    assert delta == 61, f"Booking window is {delta} days, expected ~60"


# ── PIONEER DAY ───────────────────────────────────────────────────────────────

def test_pioneer_day_not_in_utah():
    """
    Pioneer Day (July 24) must NOT fall in Utah.
    On the July 15 departure, Day 10 is at Theodore Roosevelt NP in North Dakota.
    """
    simple_itinerary = [(stop, nights) for stop, nights, *_ in ITINERARY]
    result = check_pioneer_day(DEPARTURE, simple_itinerary)
    assert not result["in_utah"], (
        f"Pioneer Day conflict: {result.get('note')} — "
        "departure date may have changed, check itinerary"
    )


def test_pioneer_day_is_day_10():
    """Pioneer Day July 24 must fall on Day 10 of the trip."""
    pioneer_day = date(2027, 7, 24)
    day_num = (pioneer_day - DEPARTURE).days + 1
    assert day_num == 10, f"Pioneer Day falls on Day {day_num}, expected Day 10"


def test_pioneer_day_location():
    """Pioneer Day must be at Theodore Roosevelt NP."""
    schedule = build_schedule()
    day_10 = next((e for e in schedule if e["day"] == 10), None)
    assert day_10 is not None
    assert day_10["stop"] == "Theodore Roosevelt", (
        f"Day 10 is at '{day_10['stop']}', must be Theodore Roosevelt"
    )


# ── STURGIS RALLY ─────────────────────────────────────────────────────────────

def test_sturgis_clear():
    """
    Black Hills must be completed before Sturgis Rally (August 1-10).
    Target: Black Hills done by July 22, at least 10 days before Sturgis.
    """
    simple_itinerary = [(stop, nights) for stop, nights, *_ in ITINERARY]
    result = check_sturgis(DEPARTURE, simple_itinerary)
    assert not result["conflict"], (
        f"Sturgis conflict detected: {result['conflicts']} — "
        "check Black Hills dates against rally start August 1"
    )


def test_black_hills_done_before_july_23():
    """Black Hills must be completed by July 22 at the latest."""
    schedule = build_schedule()
    black_hills_days = [e for e in schedule if e["stop"] == "Black Hills"]
    if black_hills_days:
        last_black_hills = max(e["date"] for e in black_hills_days)
        assert last_black_hills < date(2027, 7, 23), (
            f"Last Black Hills night is {last_black_hills}, must be before July 23"
        )


# ── SCHEDULE INTEGRITY ────────────────────────────────────────────────────────

def test_schedule_has_27_nights():
    """build_schedule() must return 27 overnight entries (28 days, home on day 28)."""
    schedule = build_schedule()
    assert len(schedule) == 27, f"Schedule has {len(schedule)} nights, expected 27"


def test_schedule_days_are_sequential():
    """Day numbers must be sequential with no gaps."""
    schedule = build_schedule()
    days = [e["day"] for e in schedule]
    assert days == list(range(1, 28)), f"Day numbers are not sequential: {days}"


def test_schedule_dates_are_sequential():
    """Each day's date must be exactly one day after the previous."""
    schedule = build_schedule()
    for i in range(1, len(schedule)):
        prev = schedule[i-1]["date"]
        curr = schedule[i]["date"]
        assert (curr - prev).days == 1, (
            f"Gap between Day {schedule[i-1]['day']} ({prev}) "
            f"and Day {schedule[i]['day']} ({curr})"
        )


def test_all_stops_in_destinations():
    """Every stop in the itinerary must have a corresponding destination record."""
    schedule = build_schedule()
    for entry in schedule:
        stop = entry["stop"]
        assert stop in DESTINATIONS, (
            f"Stop '{stop}' (Day {entry['day']}) not found in destinations.py"
        )


def test_glacier_is_7_nights_in_schedule():
    """Glacier must appear exactly 7 times in the schedule."""
    schedule = build_schedule()
    glacier_nights = [e for e in schedule if e["stop"] == "Glacier"]
    assert len(glacier_nights) == 7, (
        f"Glacier appears {len(glacier_nights)} times in schedule, expected 7"
    )


def test_glacier_starts_july_28():
    """First Glacier night must be July 28."""
    schedule = build_schedule()
    glacier_nights = [e for e in schedule if e["stop"] == "Glacier"]
    first = min(e["date"] for e in glacier_nights)
    assert first == date(2027, 7, 28), (
        f"First Glacier night is {first}, must be 2027-07-28"
    )


def test_no_more_than_3_consecutive_camp_nights_outside_glacier():
    """
    Outside of Glacier, never more than 3 consecutive pure camp nights.
    Hotel rhythm rule: every 4th night maximum is a hotel.
    'mixed' sleep type (e.g. camp then hotel) counts as a hotel reset.
    """
    schedule = build_schedule()
    consecutive = 0
    max_consecutive = 0
    for entry in schedule:
        if entry["stop"] == "Glacier":
            consecutive = 0  # Glacier is the intentional 7-night exception
            continue
        sleep = entry["sleep_type"].lower()
        if sleep == "camp":
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            # hotel, mixed, base (non-Glacier), home all reset the counter
            consecutive = 0
    assert max_consecutive <= 3, (
        f"Found {max_consecutive} consecutive pure camp nights outside Glacier "
        f"(max allowed: 3). Check hotel rhythm in itinerary.py."
    )


# ── GPS AND ROUTING ───────────────────────────────────────────────────────────

def test_houston_to_glacier_distance():
    """Houston to Glacier must be more than 1,500 straight-line miles."""
    houston = DESTINATIONS["Houston"]["gps"]
    glacier = DESTINATIONS["Glacier"]["gps"]
    dist = haversine(houston[0], houston[1], glacier[0], glacier[1])
    assert dist > 1500, f"Houston to Glacier is only {dist:.0f} miles"


def test_all_destinations_have_gps():
    """Every destination must have a valid GPS coordinate."""
    for name, dest in DESTINATIONS.items():
        gps = dest.get("gps")
        assert gps is not None, f"{name} missing GPS"
        lat, lon = gps
        assert -90 <= lat <= 90,   f"{name} latitude {lat} out of range"
        assert -180 <= lon <= 180, f"{name} longitude {lon} out of range"
        # All stops should be in the continental US or Canada
        assert 25 <= lat <= 55,    f"{name} latitude {lat} looks wrong for North America"
        assert -130 <= lon <= -65, f"{name} longitude {lon} looks wrong for North America"


# ── DOG RULES ─────────────────────────────────────────────────────────────────

def test_tango_is_ada():
    """Tango must be classified as ADA service animal."""
    assert DOGS["Tango"]["status"] == "ADA service animal"


def test_saki_is_esa():
    """Saki must be classified as ESA."""
    assert DOGS["Saki"]["status"] == "ESA — Emotional Support Animal"


def test_tango_has_broader_access_than_saki():
    """Tango's access description must be longer (more permissive) than Saki's."""
    assert len(DOGS["Tango"]["access"]) > len(DOGS["Saki"]["access"]) or \
           "full" in DOGS["Tango"]["access"].lower()
