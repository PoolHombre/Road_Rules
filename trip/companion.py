"""
trip/companion.py
Builds the complete story (list of ReportLab flowables) for the Trip Companion PDF.

Called by trip/generate_reports.py:build_companion()

Structure:
  Part 1 — Summary & Quick Reference
  Part 2 — 28 Daily Pages
  Part 3 — Training & Exercise
  Part 4 — Faith
  Part 5 — Arts, Music & Culture
  Part 6 — History
  Part 7 — Meal Plan
  Part 8 — Camping Reference
  Part 9 — Change Log
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle,
                                 PageBreak, HRFlowable)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

from shared.pdf_styles import (S, INK, MID, DIM, RULE, BG, GOLD, WHITE, TBL_H)
from shared.pdf_components import (sp, hr, hr2, p, note_box, simple_table,
                                    label_value_row, section_break, day_header)
from shared.utils import trip_date, format_date

from trip.data.destinations import DESTINATIONS
from trip.data.itinerary import ITINERARY, KEY_DATES, build_schedule, DEPARTURE
from trip.data.meals import (MEALS, FAVORITES_SCHEDULE, RESUPPLY, PANTRY,
                              PRODUCE_GUIDE, COOKING_METHODS)
from trip.rules.route_rules import ROUTE_RULES, CAMP_PRIORITY, CAMPING_RESOURCES
from trip.rules.dog_rules import DOGS, ACCESS_BY_LAND_TYPE, STOP_SPECIFIC, VAN_AC_PROTOCOL
from trip.changelog import CHANGELOG

W = 6.8 * inch


def _title_styles():
    return {
        "TITLE": S("TT", fontName="CB", fontSize=22, alignment=TA_CENTER, leading=28, spaceAfter=4),
        "SUB":   S("SB", fontName="CI", fontSize=11, alignment=TA_CENTER, leading=15, textColor=MID, spaceAfter=4),
        "H2":    S("H2", fontName="CB", fontSize=13, leading=17, spaceBefore=10, spaceAfter=3),
        "H3":    S("H3", fontName="CB", fontSize=11, leading=14, spaceBefore=8,  spaceAfter=2),
        "H4":    S("H4", fontName="CB", fontSize=10, leading=13, spaceBefore=5,  spaceAfter=2),
        "BODY":  S("BO", fontSize=9.5, leading=14, spaceAfter=4, alignment=TA_JUSTIFY),
        "ITA":   S("IT", fontName="CI", fontSize=9, leading=12, textColor=MID, spaceAfter=3),
        "SMALL": S("SM", fontSize=8, leading=12, textColor=DIM),
        "STAR":  S("ST", fontName="CBI", fontSize=9, leading=13, textColor=GOLD),
    }


def _detail_rows(dest):
    """Build the label/value rows for a destination profile."""
    rows = []
    for r in dest.get("restaurants", []):
        rows.append(("🍽️  Eat",      f"{r['name']} — {r.get('address','')} — {r['notes']}"))
    for c in dest.get("churches", []):
        rows.append(("⛪  Faith",     f"{c['name']} — {c['address']} — {c['notes']}"))
    for b in dest.get("bjj", []):
        rows.append(("🥋  BJJ",      f"{b['name']} — {b['notes']}"))
    for a in dest.get("arts", []):
        rows.append(("🎨  Arts",     f"{a['name']} — {a['details']}"))
    for poi in dest.get("poi", []):
        rows.append(("📍  POI",      f"{poi['name']} — {poi['details']}"))
    for c in dest.get("camping", []):
        rows.append(("🏕️  Camp",     f"{c['name']} ({c['type']}) — {c['notes']}"))
    if dest.get("dogs"):
        rows.append(("🐾  Dogs",     dest["dogs"]))
    if dest.get("resupply_note"):
        rows.append(("🛒  Resupply", dest["resupply_note"]))
    if dest.get("crowd_strategy"):
        rows.append(("⏰  Crowds",   dest["crowd_strategy"]))
    if dest.get("van_size_warning"):
        rows.append(("⚠️  Van size", dest["van_size_warning"]))
    return rows


def _detail_table(rows):
    if not rows:
        return None
    t = Table(
        [[p(lbl, S("DL", fontName="CB", fontSize=8, textColor=DIM, leading=11)),
          p(val, S("DV", fontSize=8.5, leading=12))]
         for lbl, val in rows],
        colWidths=[1.1*inch, W - 1.1*inch]
    )
    t.setStyle(TableStyle([
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LINEBELOW",     (0,0), (-1,-1), 0.25, colors.HexColor("#E8E8E8")),
    ] + [("BACKGROUND", (0,i), (-1,i), BG if i%2==0 else WHITE)
         for i in range(len(rows))]))
    return t


def _day_page(story, st, day_num, schedule_entry, meal, dest_data):
    """Render one day page."""
    stop    = schedule_entry["stop"]
    date_str= schedule_entry["date_str"]
    drive   = schedule_entry["drive_note"]
    sleep   = schedule_entry["sleep_type"].title()

    story.append(PageBreak())
    story.append(day_header(day_num, date_str, stop, drive, sleep))

    # Surprise banner
    if meal.get("surprise"):
        t = Table([[p(f"★  Surprise for Lisa:  {meal['surprise']}", st["STAR"])]],
                  colWidths=[W])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#FDFAF3")),
            ("BOX",           (0,0), (-1,-1), 0.75, GOLD),
            ("TOPPADDING",    (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING",   (0,0), (-1,-1), 10),
            ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ]))
        story.append(t)

    story.append(sp(5))

    # Meals
    story.append(p("MEALS", S("MC", fontName="CB", fontSize=8, textColor=DIM, leading=11, spaceAfter=2)))
    is_hotel = meal.get("hotel", False)
    if is_hotel:
        meal_rows = [
            ("Breakfast", "Hotel provided"),
            ("Lunch",     meal.get("lunch", "—")),
            ("Dinner",    "Dinner out — see destination notes"),
        ]
    else:
        meal_rows = [
            ("Breakfast", meal.get("breakfast", "—")),
            ("Lunch",     meal.get("lunch", "—")),
            ("Dinner",    meal.get("dinner", "—")),
        ]

    for ml, mt in meal_rows:
        is_star = mt and "★" in mt
        t = Table([[
            p(ml, S("ML", fontName="CB", fontSize=7.5, textColor=DIM, leading=11)),
            p(mt or "—", st["STAR"] if is_star else S("MB", fontSize=8.5, leading=12)),
        ]], colWidths=[0.8*inch, W - 0.8*inch])
        t.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#FDFAF3") if is_star else WHITE),
            ("TOPPADDING",    (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("LEFTPADDING",   (0,0), (-1,-1), 5),
            ("RIGHTPADDING",  (0,0), (-1,-1), 5),
            ("VALIGN",        (0,0), (-1,-1), "TOP"),
            ("LINEBELOW",     (0,0), (-1,-1), 0.25, colors.HexColor("#EEEEEE")),
        ]))
        story.append(t)

    story.append(sp(6))

    # Destination detail rows
    if dest_data:
        rows = _detail_rows(dest_data)
        if dest_data.get("history"):
            rows.append(("📜  History", dest_data["history"]))
        if meal.get("notes"):
            rows.append(("📌  Notes", meal["notes"]))
        t = _detail_table(rows)
        if t:
            story.append(t)

    story.append(sp(4))


def build_story():
    st = _title_styles()
    story = []

    schedule = build_schedule()
    day_to_entry = {e["day"]: e for e in schedule}

    # Build a map from stop name to destinations data
    dest_map = DESTINATIONS

    # ── COVER ────────────────────────────────────────────────────────────────
    story += [
        sp(40),
        p("2027 McAuley Glacier Trip", st["TITLE"]),
        p("Complete Trip Companion",
          S("CT", fontName="CB", fontSize=14, alignment=TA_CENTER, leading=18, textColor=MID, spaceAfter=4)),
        sp(8), hr2(), sp(8),
        p("Kevin & Lisa McAuley  ·  Fifth Wedding Anniversary  ·  July 15 – August 11, 2027", st["SUB"]),
        p("Saki  ·  Tango",
          S("CP", fontName="CI", fontSize=9, alignment=TA_CENTER, textColor=DIM, leading=13, spaceAfter=4)),
        sp(10),
        p("Houston  →  Wichita  →  Sioux Falls  →  Badlands  →  Black Hills\n"
          "→  Theodore Roosevelt NP  →  Miles City  →  Missouri Breaks  →  Fort Benton\n"
          "→  Glacier National Park  (7 nights  ·  Parents July 28 – August 1)\n"
          "→  Helena  →  Wind River  →  Thermopolis  →  Bighorns  →  Cody\n"
          "→  Medicine Bow  →  Oklahoma  →  Houston",
          S("RT", fontName="CI", fontSize=9, alignment=TA_CENTER, textColor=DIM, leading=15)),
        sp(14), hr(), sp(8),
        p("28 days  ·  7 nights at Glacier  ·  Meals, training, faith, arts, history — every day",
          S("AN", fontName="CI", fontSize=11, alignment=TA_CENTER, textColor=MID, leading=16)),
        PageBreak(),
    ]

    # ── PART 1: SUMMARY ──────────────────────────────────────────────────────
    story += [
        p("Part 1  ·  Trip Summary & Quick Reference", st["SMALL"]),
        p("Complete Overview", st["H2"]),
        hr2(), sp(4),
    ]
    for label, val in [
        ("Departure",     f"{format_date(KEY_DATES['departure'])}, 2027"),
        ("Return",        f"{format_date(KEY_DATES['return'])}, 2027"),
        ("Total days",    "28"),
        ("Camp nights",   "~18 — Badlands, Black Hills, TRNP, Missouri Breaks, Glacier (7), Wind River, Bighorns, Medicine Bow"),
        ("Hotel nights",  "~9 — Wichita, Sioux Falls, Medora, Helena, Cody, Colorado/Oklahoma"),
        ("Glacier",       f"{format_date(KEY_DATES['glacier_arrive'])} – {format_date(KEY_DATES['glacier_depart'])}  ·  7 nights"),
        ("Parents",       f"Arrive {format_date(KEY_DATES['parents_arrive'])}, depart ~{format_date(KEY_DATES['parents_depart'])}"),
        ("Logan Pass",    f"Tuesday {format_date(KEY_DATES['logan_pass'])}  ·  Book {format_date(KEY_DATES['logan_pass_booking'])} at 7pm MDT"),
        ("Pioneer Day",   "July 24 = Day 10 at TRNP, North Dakota  ✅"),
        ("Sturgis",       "Black Hills done July 22 — 10 days before August 1 rally  ✅"),
        ("Tango",         "ADA service animal — full park trail access everywhere"),
        ("Saki",          "ESA — roads, campgrounds, parking only at NPS. Full access on NF/BLM on leash."),
        ("Hotel rule",    "Breakfast provided. Dinner out. Zero cooking on hotel nights."),
        ("Fire check",    "inciweb.nwcg.gov — every morning in July/August"),
    ]:
        story.append(label_value_row(label, val))

    story.append(sp(8))
    story.append(p("Critical Bookings", st["H3"]))
    story.append(hr())
    story.append(simple_table(
        ["Priority", "What", "Where", "When"],
        [
            ("1 — TODAY",    "TRNP Cottonwood Campground (Days 9-10)",      "recreation.gov",         "July fills fast"),
            ("2 — TODAY",    "Glacier Apgar/Flathead NF camp (Days 14-20)", "recreation.gov / ranger","7 nights — book now"),
            ("3 — WEEK",     "Sylvan Lake Camp, Custer SP (Days 5-7)",      "custerresorts.com",      "Popular summer"),
            ("4 — WEEK",     "Cody hotel (Day 25)",                         "BringFido",              "Chamberlin Inn"),
            ("5 — WEEK",     "Helena hotel (Day 21)",                       "BringFido",              "Pet-friendly required"),
            ("6 — 60 DAYS",  "Logan Pass Shuttle, Tue Aug 3",               "recreation.gov",         "June 3 at 7:00 PM MDT"),
            ("7 — BEFORE",   "America the Beautiful Pass",                  "Any NPS entrance",       "$80/yr"),
            ("8 — BEFORE",   "Planet Fitness Black Card",                   "planetfitness.com",      "$24.99/mo"),
            ("9 — JAN 2027", "Verify Glacier 2027 access policy",           "nps.gov/glac",           "NPS changes annually"),
            ("10 — DAILY",   "Fire restriction check",                      "inciweb.nwcg.gov",       "Every morning"),
        ],
        [0.9*inch, 2*inch, 1.7*inch, 1.7*inch]
    ))
    story.append(PageBreak())

    # ── PART 2: DAILY PAGES ───────────────────────────────────────────────────
    story += [
        p("Part 2  ·  Daily Pages", st["SMALL"]),
        p("28 Days  ·  July 15 – August 11, 2027", st["H2"]),
        hr2(), sp(4),
        p("Each page: meals, activities, training, faith, arts, history, dog notes, surprises.", st["ITA"]),
    ]

    for day_num in range(1, 29):
        entry = day_to_entry.get(day_num)
        if not entry:
            # Day 28 is home — synthetic entry
            entry = {
                "day": 28, "stop": "Houston",
                "date_str": format_date(trip_date(DEPARTURE, 28)),
                "sleep_type": "home", "drive_note": "~500 mi / ~6 hrs via I-35 S → I-45 S"
            }
        meal = MEALS.get(day_num, {})
        dest_data = dest_map.get(entry["stop"])
        _day_page(story, st, day_num, entry, meal, dest_data)

    # ── PART 3: TRAINING ──────────────────────────────────────────────────────
    story += section_break("Part 3", "Training & Exercise")
    story.append(p("Gracie Barra / BJJ Locations — Full Route", st["H3"]))
    story.append(hr())

    bjj_rows = []
    for stop_name, dest in dest_map.items():
        if dest.get("type") == "origin":
            continue
        for b in dest.get("bjj", []):
            bjj_rows.append((stop_name, b["name"], b.get("address","—"), b["notes"]))
    story.append(simple_table(
        ["Location", "School", "Contact", "Notes"],
        bjj_rows,
        [1.4*inch, 1.6*inch, 1.3*inch, 2.2*inch]
    ))
    story.append(sp(8))
    story.append(p("Training Alternatives When No Gym Is Available", st["H3"]))
    story.append(hr())
    for title, desc in [
        ("Hotel room circuit",   "Push-up pyramid (1-2-3-4-5-4-3-2-1), squat pyramid same, plank holds 1 min each, 3 rounds. 25 minutes total."),
        ("Trail running",        "Every NF/BLM camp has trail access. Morning run with Tango — he is the running partner."),
        ("Swimming",             "Flathead Lake, Yellowstone River, Missouri River, Boysen Reservoir — real training."),
        ("Bodyweight BJJ drilling","Guard retention hip escapes, technical stand-up, bridging — drill solo on a sleeping pad at camp. 20 min."),
        ("Hiking mileage",       "The trip averages 8-12 miles of walking on active days — real physical training."),
    ]:
        story.append(p(f"<b>{title}:</b>  {desc}", S("BO", fontSize=9.5, leading=14, spaceAfter=4)))

    # ── PART 4: FAITH ─────────────────────────────────────────────────────────
    story += section_break("Part 4", "Faith")
    story.append(p(
        "The Cathedral of Saint Helena in Helena, Montana is the spiritual highlight of the return "
        "journey — Gothic Revival, built 1908-1914, modeled on the Votive Church in Vienna, "
        "marble pillars, stunning stained glass, National Register of Historic Places. "
        "The Helena Symphony performs in it. Visit regardless of Mass times.",
        st["BODY"]))
    story.append(sp(6))

    church_rows = []
    for stop_name, dest in dest_map.items():
        if dest.get("type") == "origin":
            continue
        for c in dest.get("churches", []):
            church_rows.append((stop_name, c["name"], c["address"], c["notes"]))
    story.append(simple_table(
        ["Location", "Church", "Address", "Notes"],
        church_rows,
        [1.3*inch, 2*inch, 1.6*inch, 1.9*inch]
    ))

    # ── PART 5: ARTS ──────────────────────────────────────────────────────────
    story += section_break("Part 5", "Arts, Music & Culture")
    arts_rows = []
    for stop_name, dest in dest_map.items():
        if dest.get("type") == "origin":
            continue
        for a in dest.get("arts", []):
            arts_rows.append((stop_name, a["name"], a["details"]))
    story.append(simple_table(
        ["Location", "Venue / Event", "Details"],
        arts_rows,
        [1.2*inch, 2*inch, 3.6*inch]
    ))

    # ── PART 6: HISTORY ───────────────────────────────────────────────────────
    story += section_break("Part 6", "History")
    for stop_name, dest in dest_map.items():
        if dest.get("type") == "origin" or not dest.get("history"):
            continue
        story.append(p(stop_name, st["H3"]))
        story.append(p(dest["history"], st["BODY"]))
        story.append(sp(4))

    # ── PART 7: MEAL PLAN ─────────────────────────────────────────────────────
    story += section_break("Part 7", "Meal Plan")
    story.append(p(
        "Hotel nights: breakfast provided, dinner out — no cooking. "
        "Camp nights: full three meals. Lisa's favorites marked ★.",
        st["ITA"]))
    story.append(sp(6))
    story.append(simple_table(
        ["★ Favorite", "Days", "Occasion"],
        [(f["meal"], ", ".join(str(d) for d in f["days"]), f["occasion"])
         for f in FAVORITES_SCHEDULE],
        [2*inch, 1.3*inch, 3.5*inch]
    ))
    story.append(sp(8))
    story.append(simple_table(
        ["Method", "Best For", "Notes"],
        [(m["method"], m["best_for"], m["notes"]) for m in COOKING_METHODS],
        [1.5*inch, 2.2*inch, 3*inch]
    ))
    story.append(sp(8))
    story.append(simple_table(
        ["Stop", "Day", "Items (summary)"],
        [(r["stop"], str(r["day"]) if r["day"]>0 else "Pre",
          r["items"][:80]+"..." if len(r["items"])>80 else r["items"])
         for r in RESUPPLY],
        [1.5*inch, 0.4*inch, 4.8*inch]
    ))
    story.append(sp(8))
    story.append(simple_table(
        ["Category", "Items"],
        [(q["category"], q["items"]) for q in PANTRY],
        [1.5*inch, 5.3*inch]
    ))

    # ── PART 8: CAMPING ───────────────────────────────────────────────────────
    story += section_break("Part 8", "Camping Reference")
    for camp in CAMP_PRIORITY:
        story.append(p(f"<b>{camp['rank']}. {camp['type']} — {camp['cost']}</b>",
                       st["H4"] if "H4" in st else st["H3"]))
        story.append(p(camp["notes"], st["BODY"]))
    story.append(sp(6))
    story.append(simple_table(
        ["Resource", "Use", "Where"],
        [(r["name"], r["use"], r.get("where","—")) for r in CAMPING_RESOURCES],
        [1.4*inch, 3*inch, 2.4*inch]
    ))
    story.append(sp(6))
    story.append(note_box(
        "FIRE RESTRICTIONS: Check inciweb.nwcg.gov every morning in July and August. "
        "Many sites will be under Stage 1 or Stage 2 restrictions — no ground fires, "
        "sometimes no charcoal. The Coleman and Jetboil work regardless. "
        "Never assume a campfire is allowed without checking.",
        kind="warn"
    ))

    # ── PART 9: CHANGE LOG ────────────────────────────────────────────────────
    story += section_break("Part 9", "Change Log")
    story.append(p("Every major decision and why. Append new entries to trip/changelog.py.", st["ITA"]))
    story.append(sp(6))

    for entry in CHANGELOG:
        t = Table([[
            p(entry["id"], S("ID", fontName="CB", fontSize=9, textColor=DIM, leading=12)),
            Table([
                [p(entry["decision"], S("DEC", fontName="CB", fontSize=9, leading=13))],
                [p(entry["reason"],   S("REA", fontSize=8.5, leading=13))],
            ], colWidths=[W - 1.2*inch])
        ]], colWidths=[1.1*inch, W - 1.1*inch])
        t.setStyle(TableStyle([
            ("TOPPADDING",    (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING",   (0,0), (-1,-1), 0),
            ("RIGHTPADDING",  (0,0), (-1,-1), 0),
            ("VALIGN",        (0,0), (-1,-1), "TOP"),
            ("LINEBELOW",     (0,0), (-1,-1), 0.5, RULE),
        ]))
        story.append(t)
        story.append(sp(3))

    # ── FINAL ─────────────────────────────────────────────────────────────────
    story += [
        sp(20), hr(1), sp(10),
        p("28 days. Montana at the center. The Dakotas done right.\n"
          "Seven nights at the Crown of the Continent.\n"
          "The Missouri Breaks. Fort Benton. The Rocky Mountain Front.\n"
          "Thermopolis hot springs. The Snowy Range at 10,000 feet.\n"
          "The beef tenderloin at Glacier on August 1.\n\n"
          "Build the van. Book Glacier. Go north.",
          S("FN", fontName="CBI", fontSize=11, textColor=INK, alignment=TA_CENTER, leading=18)),
        sp(6),
        p(f"Kevin & Lisa McAuley  ·  {format_date(KEY_DATES['departure'])} – {format_date(KEY_DATES['return'])}, 2027",
          S("FC", fontName="CI", fontSize=9, textColor=DIM, alignment=TA_CENTER, leading=13)),
    ]

    return story
