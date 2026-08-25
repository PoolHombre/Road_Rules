"""
tests/test_van.py
Validate the van build specification — budget math, stage integrity,
hard rules, and ordering constraints.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from van.spec.stages import (BUILD_STAGES, MECHANICAL_STAGES, EXTERIOR,
                               BUDGET, cumulative_budget)
from van.spec.electrical import DOMAINS, POWER_BUDGET
from van.changelog import CHANGELOG


# ── STAGES ────────────────────────────────────────────────────────────────────

def test_four_build_stages():
    """Must have exactly 4 build stages."""
    assert len(BUILD_STAGES) == 4, f"Found {len(BUILD_STAGES)} build stages, expected 4"


def test_five_mechanical_stages():
    """Must have exactly 5 mechanical stages (A through E)."""
    assert len(MECHANICAL_STAGES) == 5, \
        f"Found {len(MECHANICAL_STAGES)} mechanical stages, expected 5"
    assert set(MECHANICAL_STAGES.keys()) == {"A", "B", "C", "D", "E"}


def test_all_stages_have_required_fields():
    """Every build stage must have name, budget, and items."""
    for stage_num, stage in BUILD_STAGES.items():
        assert stage.get("name"),   f"Stage {stage_num} missing name"
        assert stage.get("budget"), f"Stage {stage_num} missing budget"
        assert stage.get("items"),  f"Stage {stage_num} missing items"


def test_all_mechanical_stages_have_required_fields():
    """Every mechanical stage must have name, timing, and items."""
    for stage_id, stage in MECHANICAL_STAGES.items():
        assert stage.get("name"),   f"Mechanical stage {stage_id} missing name"
        assert stage.get("timing"), f"Mechanical stage {stage_id} missing timing"
        assert stage.get("items"),  f"Mechanical stage {stage_id} missing items"


# ── BUDGET ────────────────────────────────────────────────────────────────────

def test_stage_1_budget():
    """Stage 1 budget must be $18,115."""
    assert BUILD_STAGES[1]["budget"] == 18115, \
        f"Stage 1 budget is {BUILD_STAGES[1]['budget']}, expected 18115"


def test_stage_2_budget():
    """Stage 2 budget must be $6,550."""
    assert BUILD_STAGES[2]["budget"] == 6550, \
        f"Stage 2 budget is {BUILD_STAGES[2]['budget']}, expected 6550"


def test_stage_3_budget():
    """Stage 3 budget must be $9,092."""
    assert BUILD_STAGES[3]["budget"] == 9092, \
        f"Stage 3 budget is {BUILD_STAGES[3]['budget']}, expected 9092"


def test_stage_4_budget():
    """Stage 4 budget must be $2,500."""
    assert BUILD_STAGES[4]["budget"] == 2500, \
        f"Stage 4 budget is {BUILD_STAGES[4]['budget']}, expected 2500"


def test_cumulative_budget_through_stage_1():
    """Budget through Stage 1 (with vehicle) must be ~$30,115."""
    total = cumulative_budget(1, include_vehicle=True)
    assert total == BUDGET["vehicle_purchase"] + BUDGET["stage_1"], \
        f"Cumulative budget through Stage 1 is {total}"


def test_cumulative_budget_through_stage_3():
    """Budget through Stage 3 (with vehicle) must be ~$45,757."""
    expected = (BUDGET["vehicle_purchase"] +
                BUDGET["stage_1"] +
                BUDGET["stage_2"] +
                BUDGET["stage_3"])
    actual = cumulative_budget(3, include_vehicle=True)
    assert actual == expected, f"Cumulative through Stage 3: {actual}, expected {expected}"


def test_cumulative_budget_increases_each_stage():
    """Each successive stage must add to the cumulative budget."""
    prev = 0
    for stage_num in range(1, 5):
        curr = cumulative_budget(stage_num, include_vehicle=False)
        assert curr > prev, \
            f"Stage {stage_num} cumulative ({curr}) not greater than previous ({prev})"
        prev = curr


# ── HARD RULES ────────────────────────────────────────────────────────────────

def test_no_induction_cooktop_in_any_stage():
    """
    Induction cooktop must NOT appear as a positive item in any build stage.
    It may appear in 'explicitly excluded' sections as a prohibition.
    Outdoor kitchen only — this rule is permanent and non-negotiable.
    """
    for stage_num, stage in BUILD_STAGES.items():
        for category, items in stage.get("items", {}).items():
            # Skip exclusion/prohibition sections — they exist to document the rule
            if any(word in category.lower() for word in ["excluded", "not included", "prohibited"]):
                continue
            for item in items:
                assert "induction" not in item.lower(), (
                    f"Stage {stage_num}, '{category}': '{item}' — "
                    "induction cooktop is permanently prohibited"
                )


def test_outdoor_kitchen_only_rule_exists():
    """Stage 3 must have an 'explicitly excluded' section prohibiting indoor cooking."""
    stage_3 = BUILD_STAGES[3]
    items = stage_3.get("items", {})
    excluded_key = next((k for k in items if "NOT" in k or "Excluded" in k or "excluded" in k), None)
    assert excluded_key is not None, \
        "Stage 3 must have an 'explicitly excluded' items section for indoor cooking"


def test_wind_turbine_order_note_exists():
    """
    Stage 3 must contain an order-first warning for the Primus wind turbine.
    Lead time is 4-6 weeks — ordering late gates the entire Stage 3.
    """
    stage_3 = BUILD_STAGES[3]
    items_text = str(stage_3.get("items", {})).lower()
    notes_text = stage_3.get("notes", "").lower()
    assert "order" in items_text or "order" in notes_text, \
        "Stage 3 must warn to ORDER THE PRIMUS TURBINE FIRST"


def test_wrap_is_applied_last():
    """Exterior wrap spec must specify it is applied LAST."""
    timing = EXTERIOR.get("wrap_timing", "").lower()
    assert "last" in timing, \
        f"Exterior wrap timing '{timing}' must specify LAST — wrap applied after all hardware"


def test_stage_c_requires_weight_data():
    """
    Stage C (Wilwood brakes) must reference waiting for Stage 1 weight.
    Brake spec cannot be finalized until loaded weight is known.
    """
    stage_c = MECHANICAL_STAGES["C"]
    notes = stage_c.get("notes", "").lower()
    assert "weight" in notes, \
        "Stage C must reference waiting for Stage 1 loaded weight before brake spec"


def test_stage_4_is_deferred():
    """Stage 4 (dual display) must be marked as deferred until after first expedition."""
    stage_4 = BUILD_STAGES[4]
    notes = stage_4.get("notes", "").lower()
    assert "defer" in notes or "after" in notes, \
        "Stage 4 must be marked as deferred until after the first expedition"


# ── ELECTRICAL ────────────────────────────────────────────────────────────────

def test_three_electrical_domains():
    """Must have exactly 3 electrical domains."""
    assert len(DOMAINS) == 3, f"Found {len(DOMAINS)} domains, expected 3"
    assert set(DOMAINS.keys()) == {1, 2, 3}


def test_domain_1_is_factory():
    """Domain 1 must be the factory vehicle electrical system."""
    assert "factory" in DOMAINS[1]["name"].lower() or "vehicle" in DOMAINS[1]["name"].lower()


def test_domain_2_has_12_circuits():
    """Domain 2 (aux 12V DC) must have exactly 12 circuits."""
    circuits = DOMAINS[2].get("circuits", [])
    assert len(circuits) == 12, f"Domain 2 has {len(circuits)} circuits, expected 12"


def test_domain_3_excludes_induction():
    """Domain 3 (120V AC) must explicitly exclude induction cooktop."""
    excluded = str(DOMAINS[3].get("explicitly_excluded", [])).lower()
    assert "induction" in excluded, \
        "Domain 3 must explicitly exclude induction cooktop"


def test_power_budget_has_required_fields():
    """Power budget must have total_with_ac_wh, usable_bank_wh, and solar_harvest_wh."""
    for field in ["total_with_ac_wh", "total_without_ac_wh",
                  "usable_bank_wh", "solar_harvest_wh", "alternator_wh_per_day"]:
        assert field in POWER_BUDGET, f"Power budget missing '{field}'"


def test_usable_bank_capacity():
    """400Ah × 12V × 80% DoD = 3,840Wh usable."""
    assert POWER_BUDGET["usable_bank_wh"] == 3840, \
        f"Usable bank is {POWER_BUDGET['usable_bank_wh']}Wh, expected 3840Wh"


def test_solar_harvest_is_positive():
    """Solar harvest must be a positive number."""
    assert POWER_BUDGET["solar_harvest_wh"] > 0


def test_bank_sufficient_for_one_night_without_ac():
    """Usable bank must cover at least 2 nights without AC."""
    two_nights_no_ac = POWER_BUDGET["total_without_ac_wh"] * 2
    assert POWER_BUDGET["usable_bank_wh"] >= two_nights_no_ac, (
        f"Bank ({POWER_BUDGET['usable_bank_wh']}Wh) insufficient for "
        f"2 nights without AC ({two_nights_no_ac}Wh)"
    )


# ── CHANGELOG ─────────────────────────────────────────────────────────────────

def test_changelog_has_entries():
    """Van changelog must have at least 10 entries."""
    assert len(CHANGELOG) >= 10, f"Van changelog has {len(CHANGELOG)} entries, expected ≥10"


def test_changelog_ids_are_sequential():
    """Changelog IDs must follow VAN-001, VAN-002, ... format without gaps."""
    ids = [entry["id"] for entry in CHANGELOG]
    for i, entry_id in enumerate(ids, start=1):
        expected = f"VAN-{i:03d}"
        assert entry_id == expected, \
            f"Changelog entry {i}: ID is '{entry_id}', expected '{expected}'"


def test_changelog_entries_have_required_fields():
    """Every changelog entry must have id, date, decision, and reason."""
    for entry in CHANGELOG:
        for field in ["id", "date", "decision", "reason"]:
            assert field in entry, \
                f"Changelog entry '{entry.get('id', '?')}' missing '{field}'"


def test_no_induction_in_changelog():
    """
    The changelog must not document adding an induction cooktop.
    Any entry approving indoor cooking would violate the hard rule.
    """
    for entry in CHANGELOG:
        decision = entry.get("decision", "").lower()
        reason = entry.get("reason", "").lower()
        assert "induction" not in decision or "no induction" in decision or "prohibit" in decision, (
            f"Changelog entry {entry['id']} appears to approve induction cooktop"
        )
