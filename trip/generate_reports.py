"""
trip/generate_reports.py
Generates all three trip PDFs from structured data in trip/data/ and trip/rules/.

Outputs (written to output_dir, default 'outputs/'):
  - 2027_McAuley_Glacier_NP_Road_Trip_Plan_B.pdf
  - 2027_McAuley_Road_Trip_Meal_Plan.pdf
  - 2027_McAuley_Glacier_Trip_Companion.pdf

Usage:
    python trip/generate_reports.py
    # or via build.py:
    python build.py --trip
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

from shared.pdf_styles import (register_fonts, S, INK, MID, DIM,
                                RULE, BG, GOLD, WHITE, TBL_H)
from shared.pdf_components import (sp, hr, hr2, p, note_box, simple_table,
                                    label_value_row, section_break, day_header)
from shared.utils import trip_date, format_date

from trip.data.destinations import DESTINATIONS
from trip.data.itinerary import ITINERARY, KEY_DATES, build_schedule, DEPARTURE
from trip.data.meals import (MEALS, FAVORITES_SCHEDULE, RESUPPLY,
                              PRODUCE_GUIDE, COOKING_METHODS)
from trip.rules.route_rules import CAMP_PRIORITY
from trip.rules.dog_rules import DOGS
from trip.changelog import CHANGELOG

W = 6.8 * inch

def make_doc(filename, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)
    doc = SimpleDocTemplate(full_path, pagesize=letter,
        rightMargin=0.9*inch, leftMargin=0.9*inch,
        topMargin=0.8*inch, bottomMargin=0.8*inch)
    return doc, full_path


def std_styles():
    return {
        "TITLE": S("TT", fontName="CB", fontSize=20, alignment=TA_CENTER, leading=26, spaceAfter=4),
        "SUB":   S("SB", fontName="CI", fontSize=11, alignment=TA_CENTER, leading=15, textColor=MID, spaceAfter=4),
        "H2":    S("H2", fontName="CB", fontSize=13, leading=17, spaceBefore=10, spaceAfter=3),
        "H3":    S("H3", fontName="CB", fontSize=11, leading=14, spaceBefore=8,  spaceAfter=2),
        "BODY":  S("BO", fontSize=9.5, leading=14, spaceAfter=4, alignment=TA_JUSTIFY),
        "ITA":   S("IT", fontName="CI", fontSize=9, leading=12, textColor=MID, spaceAfter=3),
        "STAR":  S("ST", fontName="CBI", fontSize=9, leading=13, textColor=GOLD),
    }


# ── REPORT 1: PLAN B ─────────────────────────────────────────────────────────

def build_plan_b(output_dir="outputs"):
    register_fonts()
    doc, path = make_doc("2027_McAuley_Glacier_NP_Road_Trip_Plan_B.pdf", output_dir)
    st = std_styles()
    story = []

    # Cover
    story += [
        sp(40),
        p("2027 McAuley Glacier NP Road Trip", st["TITLE"]),
        p("Plan B  ·  Montana & Dakotas Edition",
          S("PB", fontName="CB", fontSize=14, alignment=TA_CENTER, leading=18, textColor=MID, spaceAfter=4)),
        sp(8), hr2(), sp(8),
        p("Kevin & Lisa McAuley  ·  Fifth Wedding Anniversary  ·  July–August 2027", st["SUB"]),
        p("Saki  ·  Tango",
          S("CP", fontName="CI", fontSize=9, alignment=TA_CENTER, textColor=DIM, leading=13, spaceAfter=4)),
        sp(12),
        p("Houston  →  Wichita  →  Sioux Falls  →  Badlands  →  Black Hills\n"
          "→  Theodore Roosevelt NP  →  Miles City  →  Missouri Breaks  →  Fort Benton\n"
          "→  Glacier National Park  (7 nights  ·  Parents July 28 – August 1)\n"
          "→  Helena  →  Wind River  →  Thermopolis  →  Bighorns  →  Cody\n"
          "→  Medicine Bow  →  Oklahoma  →  Houston",
          S("RT", fontName="CI", fontSize=9, alignment=TA_CENTER, textColor=DIM, leading=15)),
        sp(14), hr(), sp(8),
        p("28 days  ·  7 nights at Glacier  ·  Montana and the Dakotas at the center",
          S("AN", fontName="CI", fontSize=11, alignment=TA_CENTER, textColor=MID, leading=16)),
        PageBreak(),
    ]

    # Summary
    story += [
        p("Section 1 — Trip at a Glance", S("SM", fontSize=8, textColor=DIM)),
        p("Complete Overview", st["H2"]),
        hr2(), sp(4),
    ]
    for label, val in [
        ("Departure",     f"{format_date(KEY_DATES['departure'])}, 2027"),
        ("Return",        f"{format_date(KEY_DATES['return'])}, 2027"),
        ("Total days",    "28"),
        ("Glacier",       f"{format_date(KEY_DATES['glacier_arrive'])} – {format_date(KEY_DATES['glacier_depart'])}  ·  7 nights"),
        ("Parents",       f"Arrive {format_date(KEY_DATES['parents_arrive'])}, depart ~{format_date(KEY_DATES['parents_depart'])}"),
        ("Logan Pass",    f"Tuesday {format_date(KEY_DATES['logan_pass'])}  ·  Book {format_date(KEY_DATES['logan_pass_booking'])} at 7pm MDT"),
        ("Pioneer Day",   "July 24 = Day 10 at TRNP, North Dakota  ✅"),
        ("Sturgis",       "Black Hills done July 22 — 10 days before August 1 rally  ✅"),
        ("Hotel rule",    "Breakfast provided. Dinner out. Zero cooking on hotel nights."),
        ("Camp priority", "  ·  ".join([f"{c['rank']}. {c['type']}" for c in CAMP_PRIORITY])),
    ]:
        story.append(label_value_row(label, val))

    story.append(sp(8))
    story.append(p("Day-by-Day Itinerary", st["H3"]))
    story.append(hr())

    schedule = build_schedule()
    rows = [(str(e["day"]), e["date_str"], e["stop"],
             e["sleep_type"].title(),
             e["drive_note"][:48] if e["drive_note"] != "Local" else "Local")
            for e in schedule]
    rows.append(("28", format_date(trip_date(DEPARTURE, 28)),
                 "→ Houston (Home)", "Home", "~500 mi / ~6 hrs"))
    story.append(simple_table(
        ["Day", "Date", "Destination", "Sleep", "Drive"],
        rows,
        [0.35*inch, 0.9*inch, 2.1*inch, 0.7*inch, 2.65*inch]
    ))

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
            ("8 — BEFORE",   "Planet Fitness Black Card",                   "planetfitness.com",      "$24.99/mo — showers"),
            ("9 — JAN 2027", "Verify Glacier 2027 access policy",           "nps.gov/glac",           "NPS changes annually"),
            ("10 — DAILY",   "Fire restriction check",                      "inciweb.nwcg.gov",       "Every morning July/Aug"),
        ],
        [0.9*inch, 2*inch, 1.7*inch, 1.7*inch]
    ))
    story.append(PageBreak())

    # Destination profiles
    story += [
        p("Section 2 — Destination Profiles", S("SM", fontSize=8, textColor=DIM)),
        p("Every Stop", st["H2"]),
        hr2(), sp(4),
        p("Restaurants, churches, BJJ, arts, POI, history, dogs, camping — every stop.", st["ITA"]),
    ]

    for stop_name, dest in DESTINATIONS.items():
        if dest.get("type") == "origin":
            continue
        story.append(sp(6))
        story.append(p(stop_name, st["H2"]))
        drive = dest.get("drive_from_prev", {})
        story.append(p(f"{dest['state']}  ·  {drive.get('route','')}  ·  "
                       f"{drive.get('miles','')} mi  ·  {dest.get('type','').replace('_',' ').title()}",
                       st["ITA"]))
        story.append(hr())

        if dest.get("history"):
            story.append(p(dest["history"], st["BODY"]))
            story.append(sp(4))

        rows = []
        for r in dest.get("restaurants", []):
            rows.append(("🍽️  Eat",     f"{r['name']} — {r.get('address','')} — {r['notes']}"))
        for c in dest.get("churches", []):
            rows.append(("⛪  Faith",    f"{c['name']} — {c['address']} — {c['notes']}"))
        for b in dest.get("bjj", []):
            rows.append(("🥋  BJJ",     f"{b['name']} — {b['notes']}"))
        for a in dest.get("arts", []):
            rows.append(("🎨  Arts",    f"{a['name']} — {a['details']}"))
        for poi in dest.get("poi", []):
            rows.append(("📍  POI",     f"{poi['name']} — {poi['details']}"))
        for c in dest.get("camping", []):
            rows.append(("🏕️  Camp",    f"{c['name']} ({c['type']}) — {c['notes']}"))
        if dest.get("dogs"):
            rows.append(("🐾  Dogs",    dest["dogs"]))
        if dest.get("resupply_note"):
            rows.append(("🛒  Resupply",dest["resupply_note"]))
        if dest.get("crowd_strategy"):
            rows.append(("⏰  Crowds",  dest["crowd_strategy"]))
        if dest.get("van_size_warning"):
            rows.append(("⚠️  Van",     dest["van_size_warning"]))

        if rows:
            t = Table(
                [[p(lbl, S("DL",fontName="CB",fontSize=8,textColor=DIM,leading=11)),
                  p(val, S("DV",fontSize=8.5,leading=12))]
                 for lbl,val in rows],
                colWidths=[1.1*inch, W-1.1*inch])
            t.setStyle(TableStyle([
                ("TOPPADDING",    (0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                ("LEFTPADDING",   (0,0),(-1,-1),0),("RIGHTPADDING", (0,0),(-1,-1),0),
                ("VALIGN",        (0,0),(-1,-1),"TOP"),
                ("LINEBELOW",     (0,0),(-1,-1),0.25,colors.HexColor("#E8E8E8")),
            ]+[("BACKGROUND",(0,i),(-1,i),BG if i%2==0 else WHITE) for i in range(len(rows))]))
            story.append(t)
        story.append(sp(10))

    # Change log
    story += [PageBreak(),
              p("Section 3 — Change Log", S("SM",fontSize=8,textColor=DIM)),
              p("Every Decision & Reason", st["H2"]),
              hr2(), sp(4),
              p("Every significant planning decision, what was decided, and why. "
                "Append new entries to trip/changelog.py — never delete existing ones.", st["ITA"]),
              sp(6)]

    for entry in CHANGELOG:
        t = Table([[
            p(entry["id"], S("ID",fontName="CB",fontSize=9,textColor=DIM,leading=12)),
            Table([
                [p(entry["decision"], S("DEC",fontName="CB",fontSize=9,leading=13))],
                [p(entry["reason"],   S("REA",fontSize=8.5,leading=13))],
            ], colWidths=[W-1.2*inch])
        ]], colWidths=[1.1*inch, W-1.1*inch])
        t.setStyle(TableStyle([
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
            ("VALIGN",(0,0),(-1,-1),"TOP"),("LINEBELOW",(0,0),(-1,-1),0.5,RULE),
        ]))
        story.append(t)
        story.append(sp(3))

    story += [
        sp(16), hr(1), sp(8),
        p("28 days. Montana at the center. Build the van. Book Glacier. Go north.",
          S("FN",fontName="CBI",fontSize=11,textColor=INK,alignment=TA_CENTER,leading=18)),
        sp(4),
        p(f"Kevin & Lisa McAuley  ·  {format_date(KEY_DATES['departure'])} – {format_date(KEY_DATES['return'])}, 2027",
          S("FC",fontName="CI",fontSize=9,textColor=DIM,alignment=TA_CENTER,leading=13)),
    ]
    doc.build(story)
    return path


# ── REPORT 2: MEAL PLAN ───────────────────────────────────────────────────────

def build_meal_plan(output_dir="outputs"):
    register_fonts()
    doc, path = make_doc("2027_McAuley_Road_Trip_Meal_Plan.pdf", output_dir)
    st = std_styles()
    story = []

    story += [
        sp(50),
        p("2027 Road Trip Meal Plan", st["TITLE"]),
        p("Kevin & Lisa McAuley  ·  28 Days  ·  July–August 2027", st["SUB"]),
        sp(8), hr2(), sp(8),
        p("Hotel nights: breakfast provided, dinner out — no cooking. "
          "Camp nights: full three meals on Coleman / cast iron / Instant Pot / Dutch oven. "
          "Lisa's favorites marked ★.",
          S("IN",fontName="CI",fontSize=10.5,alignment=TA_CENTER,leading=16,textColor=MID)),
        sp(16),
    ]

    story.append(simple_table(
        ["Rule","Details"],
        [
            ("Hotel nights",    "Breakfast provided. Dinner out. Zero cooking."),
            ("Camp breakfasts", "Coleman + cast iron. Coffee always first."),
            ("Camp dinners",    "Coleman / Instant Pot / Dutch oven. One pot where possible."),
            ("Lisa's favorites ★","Eggs+naan · Crepes · Hotdogs · Muffins · Shawarma · Waffles · Beef tenderloin · Fresh bread"),
            ("Resupply",        "Every 3-4 days. Buy fresh, buy for what you'll eat before the next stop."),
            ("Pre-freeze",      "Portion and freeze: ground beef, chicken thighs, pork flat in Dometic."),
            ("Pre-mix at home", "Dry muffin mix ×3. Shawarma spice. Taco seasoning. Black bean soup seasoning."),
            ("Cast iron waffle iron","Lodge stovetop model (~$35). Buy before departure."),
            ("Dutch oven baking","Parchment liner. Low flame under, foil on lid. 20-35 min."),
            ("No-knead bread",  "Mix night before (5 min). Rise 8-12 hrs. Bake in Dutch oven 35 min."),
        ],
        [1.5*inch,5.2*inch]
    ))
    story.append(PageBreak())

    story.append(p("Day-by-Day Meal Plan", st["H2"]))
    story.append(hr2())

    schedule = build_schedule()
    day_to_stop = {e["day"]: e["stop"] for e in schedule}

    for day_num in range(1, 29):
        meal = MEALS.get(day_num, {})
        stop = day_to_stop.get(day_num, "Home")
        d = trip_date(DEPARTURE, day_num)

        hdr = day_header(day_num, format_date(d), stop, "",
                         "Hotel" if meal.get("hotel") else "Camp")
        story.append(hdr)

        if meal.get("surprise"):
            t = Table([[p(f"★  {meal['surprise']}", st["STAR"])]],colWidths=[W])
            t.setStyle(TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FDFAF3")),
                ("BOX",(0,0),(-1,-1),0.75,GOLD),
                ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
                ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
            ]))
            story.append(t)

        if meal.get("hotel"):
            meal_rows = [
                ("Breakfast","Hotel provided"),
                ("Lunch",    meal.get("lunch","—")),
                ("Dinner",   "Dinner out — see destination notes"),
            ]
        else:
            meal_rows = [
                ("Breakfast",meal.get("breakfast","—")),
                ("Lunch",    meal.get("lunch","—")),
                ("Dinner",   meal.get("dinner","—")),
            ]

        for ml, mt in meal_rows:
            is_star = mt and "★" in mt
            t = Table([[
                p(ml, S("ML",fontName="CB",fontSize=7.5,textColor=DIM,leading=11)),
                p(mt or "—", st["STAR"] if is_star else S("MB",fontSize=8.5,leading=12)),
            ]],colWidths=[0.8*inch, W-0.8*inch])
            t.setStyle(TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FDFAF3") if is_star else WHITE),
                ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                ("VALIGN",(0,0),(-1,-1),"TOP"),
                ("LINEBELOW",(0,0),(-1,-1),0.25,colors.HexColor("#EEEEEE")),
            ]))
            story.append(t)

        if meal.get("notes"):
            story.append(p(meal["notes"],
                           S("NT",fontName="CI",fontSize=8,textColor=DIM,leading=11)))
        story.append(sp(8))

    story.append(PageBreak())
    story.append(p("Lisa's Favorites — Master Schedule", st["H2"]))
    story.append(hr())
    story.append(simple_table(
        ["★ Favorite","Days","Occasion"],
        [(f["meal"],", ".join(str(d) for d in f["days"]),f["occasion"])
         for f in FAVORITES_SCHEDULE],
        [2*inch,1.3*inch,3.5*inch]
    ))
    story.append(sp(8))
    story.append(p("Resupply Schedule", st["H2"]))
    story.append(hr())
    story.append(simple_table(
        ["Stop","Day","Items (summary)"],
        [(r["stop"], str(r["day"]) if r["day"]>0 else "Pre",
          r["items"][:90]+"..." if len(r["items"])>90 else r["items"])
         for r in RESUPPLY],
        [1.5*inch,0.4*inch,4.8*inch]
    ))
    story.append(sp(8))
    story.append(p("Cooking Methods", st["H2"]))
    story.append(hr())
    story.append(simple_table(
        ["Method","Best For","Notes"],
        [(m["method"],m["best_for"],m["notes"]) for m in COOKING_METHODS],
        [1.5*inch,2.2*inch,3*inch]
    ))
    story.append(sp(8))
    story.append(p("Produce Longevity", st["H2"]))
    story.append(hr())
    story.append(simple_table(
        ["Days After Buying","Produce","Storage"],
        [(g["days"],g["items"],g["storage"]) for g in PRODUCE_GUIDE],
        [1.2*inch,3*inch,2.5*inch]
    ))
    story += [
        sp(12), hr(1), sp(8),
        p("The beef tenderloin at Glacier on August 1 is the meal.",
          S("FN",fontName="CBI",fontSize=11,textColor=INK,alignment=TA_CENTER,leading=18)),
        sp(4),
        p("Kevin & Lisa McAuley  ·  July–August 2027",
          S("FC",fontName="CI",fontSize=9,textColor=DIM,alignment=TA_CENTER,leading=13)),
    ]
    doc.build(story)
    return path


# ── REPORT 3: COMPANION ───────────────────────────────────────────────────────

def build_companion(output_dir="outputs"):
    register_fonts()
    doc, path = make_doc("2027_McAuley_Glacier_Trip_Companion.pdf", output_dir)
    from trip.companion import build_story
    story = build_story()
    doc.build(story)
    return path


# ── MAIN ─────────────────────────────────────────────────────────────────────

def build(output_dir="outputs"):
    print("  Building Plan B destination report...")
    build_plan_b(output_dir)
    print("    ✓  2027_McAuley_Glacier_NP_Road_Trip_Plan_B.pdf")

    print("  Building meal plan...")
    build_meal_plan(output_dir)
    print("    ✓  2027_McAuley_Road_Trip_Meal_Plan.pdf")

    print("  Building trip companion...")
    build_companion(output_dir)
    print("    ✓  2027_McAuley_Glacier_Trip_Companion.pdf")


if __name__ == "__main__":
    build("outputs")
    print("Done.")
