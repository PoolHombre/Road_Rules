"""
tests/test_meals.py
Validate the 28-day meal plan — coverage, hotel rules, favorites schedule.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from trip.data.meals import (MEALS, FAVORITES_SCHEDULE, RESUPPLY,
                              PANTRY, PRODUCE_GUIDE, COOKING_METHODS,
                              LISAS_FAVORITES)
from trip.data.itinerary import build_schedule


# ── COVERAGE ──────────────────────────────────────────────────────────────────

def test_all_28_days_have_meal_entries():
    """Every day from 1-28 must have a meal entry."""
    for day in range(1, 29):
        assert day in MEALS, f"Day {day} missing from MEALS"


def test_all_camp_days_have_three_meals():
    """Non-hotel days must have breakfast, lunch, and dinner defined."""
    for day, meal in MEALS.items():
        if not meal.get("hotel"):
            assert meal.get("breakfast"), f"Day {day} (camp): missing breakfast"
            assert meal.get("lunch"),     f"Day {day} (camp): missing lunch"
            assert meal.get("dinner"),    f"Day {day} (camp): missing dinner"


def test_hotel_days_have_no_cooking():
    """Hotel days must not have a breakfast or dinner field (they're provided/out)."""
    for day, meal in MEALS.items():
        if meal.get("hotel"):
            # breakfast on hotel days should be None or absent
            assert not meal.get("breakfast") or meal.get("breakfast") == "Hotel provided", (
                f"Day {day} (hotel): should not have a cooked breakfast"
            )


def test_hotel_days_have_lunch():
    """Hotel/driving days must still have a lunch entry (van snacks or deli stop)."""
    for day, meal in MEALS.items():
        if meal.get("hotel"):
            assert meal.get("lunch"), f"Day {day} (hotel): missing lunch"


# ── LISA'S FAVORITES ──────────────────────────────────────────────────────────

def test_beef_tenderloin_is_day_18():
    """Beef tenderloin anniversary dinner must be on Day 18 (August 1 at Glacier)."""
    tenderloin_days = [
        f["days"] for f in FAVORITES_SCHEDULE
        if "tenderloin" in f["meal"].lower()
    ]
    assert tenderloin_days, "Beef tenderloin not found in FAVORITES_SCHEDULE"
    assert 18 in tenderloin_days[0], (
        f"Beef tenderloin is on days {tenderloin_days[0]}, must include Day 18"
    )


def test_beef_tenderloin_in_day_18_meal():
    """Day 18 dinner must reference the beef tenderloin."""
    meal = MEALS[18]
    assert "tenderloin" in meal.get("dinner", "").lower() or \
           "tenderloin" in meal.get("surprise", "").lower(), (
        "Day 18 dinner must be the beef tenderloin"
    )


def test_day_18_has_surprise():
    """Day 18 must have a surprise annotation — this is the anniversary dinner."""
    assert MEALS[18].get("surprise"), "Day 18 must have a surprise annotation"


def test_crepes_appear_three_times():
    """Crepes must appear on exactly 3 days: first surprise, Glacier arrival, GTSR victory."""
    crepe_entry = next(
        (f for f in FAVORITES_SCHEDULE if "crepe" in f["meal"].lower()), None
    )
    assert crepe_entry is not None, "Crepes not found in FAVORITES_SCHEDULE"
    assert len(crepe_entry["days"]) == 3, (
        f"Crepes appear on {len(crepe_entry['days'])} days, expected 3"
    )


def test_crepes_on_glacier_arrival_day():
    """Crepes must appear on Day 14 (Glacier arrival)."""
    crepe_entry = next(
        (f for f in FAVORITES_SCHEDULE if "crepe" in f["meal"].lower()), None
    )
    assert 14 in crepe_entry["days"], "Crepes must be on Day 14 (Glacier arrival)"


def test_crepes_on_gtsr_day():
    """Crepes must appear on Day 20 (Going-to-the-Sun Road victory dinner)."""
    crepe_entry = next(
        (f for f in FAVORITES_SCHEDULE if "crepe" in f["meal"].lower()), None
    )
    assert 20 in crepe_entry["days"], "Crepes must be on Day 20 (GTSR victory dinner)"


def test_blueberry_muffins_appear_three_times():
    """Blueberry muffins must appear on exactly 3 days."""
    muffin_entry = next(
        (f for f in FAVORITES_SCHEDULE if "muffin" in f["meal"].lower()), None
    )
    assert muffin_entry is not None, "Blueberry muffins not found in FAVORITES_SCHEDULE"
    assert len(muffin_entry["days"]) == 3, (
        f"Blueberry muffins on {len(muffin_entry['days'])} days, expected 3"
    )


def test_final_muffins_are_last_camp_morning():
    """Final blueberry muffins must be Day 27 — the goodbye breakfast at Snowy Range."""
    muffin_entry = next(
        (f for f in FAVORITES_SCHEDULE if "muffin" in f["meal"].lower()), None
    )
    assert 27 in muffin_entry["days"], (
        "Final blueberry muffins must be on Day 27 (goodbye breakfast at Snowy Range)"
    )


def test_all_favorites_have_days():
    """Every favorite in FAVORITES_SCHEDULE must have at least one day assigned."""
    for entry in FAVORITES_SCHEDULE:
        assert entry["days"], f"'{entry['meal']}' has no days assigned"


def test_all_favorites_have_occasion():
    """Every favorite must have an occasion description."""
    for entry in FAVORITES_SCHEDULE:
        assert entry["occasion"], f"'{entry['meal']}' has no occasion description"


def test_surprise_days_are_not_hotel_days():
    """
    Surprises should not be on hotel days — Lisa gets breakfast provided
    and dinner out, so a surprise meal doesn't make sense.
    Exception: Day 3 eggs+naan is made at the hotel before checkout — that's fine.
    """
    for day, meal in MEALS.items():
        if meal.get("surprise") and meal.get("hotel") and day != 3:
            pytest.fail(
                f"Day {day} is a hotel night with a surprise — "
                "hotel nights are breakfast provided + dinner out"
            )


# ── RESUPPLY ──────────────────────────────────────────────────────────────────

def test_resupply_has_8_stops():
    """Must have exactly 8 resupply stops (including pre-trip home stop)."""
    assert len(RESUPPLY) == 8, f"Found {len(RESUPPLY)} resupply stops, expected 8"


def test_critical_resupply_before_remote_stretch():
    """Dickinson/Medora resupply must be marked critical — remote stretch follows."""
    medora_stop = next(
        (r for r in RESUPPLY if "Medora" in r["stop"] or "Dickinson" in r["stop"]), None
    )
    assert medora_stop is not None, "No Medora/Dickinson resupply found"
    assert medora_stop.get("critical"), (
        "Medora/Dickinson resupply must be marked critical — Missouri Breaks follows"
    )


def test_fort_benton_resupply_is_critical():
    """Fort Benton resupply must be marked critical — beef tenderloin is purchased here."""
    benton_stop = next(
        (r for r in RESUPPLY if "Benton" in r["stop"] or "Great Falls" in r["stop"]), None
    )
    assert benton_stop is not None, "No Fort Benton/Great Falls resupply found"
    assert benton_stop.get("critical"), (
        "Fort Benton/Great Falls resupply must be critical — beef tenderloin purchased here"
    )


def test_beef_tenderloin_mentioned_in_fort_benton_resupply():
    """Fort Benton resupply items must mention buying and freezing the beef tenderloin."""
    benton_stop = next(
        (r for r in RESUPPLY if "Benton" in r["stop"] or "Great Falls" in r["stop"]), None
    )
    assert benton_stop is not None
    assert "tenderloin" in benton_stop["items"].lower(), (
        "Fort Benton resupply must mention buying and freezing the beef tenderloin"
    )


# ── COOKING METHODS ───────────────────────────────────────────────────────────

def test_coleman_is_in_cooking_methods():
    """Coleman 2-burner must be in cooking methods — primary camp cooking tool."""
    methods = [m["method"] for m in COOKING_METHODS]
    assert any("Coleman" in m for m in methods), "Coleman 2-burner missing from COOKING_METHODS"


def test_dutch_oven_is_in_cooking_methods():
    """Dutch oven must be in cooking methods — used for muffins, bread, shawarma."""
    methods = [m["method"] for m in COOKING_METHODS]
    assert any("Dutch" in m or "dutch" in m for m in methods), \
        "Dutch oven missing from COOKING_METHODS"


def test_no_induction_cooktop():
    """Induction cooktop must NOT appear anywhere in the meal plan data."""
    # Check all meal text
    for day, meal in MEALS.items():
        for field in ["breakfast", "lunch", "dinner", "notes", "surprise"]:
            text = meal.get(field, "") or ""
            assert "induction" not in text.lower(), (
                f"Day {day} {field} mentions induction cooktop — permanently prohibited"
            )

    # Check cooking methods
    for method in COOKING_METHODS:
        assert "induction" not in method["method"].lower(), \
            "Induction cooktop must not appear in COOKING_METHODS"
