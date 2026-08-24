"""
trip/changelog.py
Every significant trip planning decision, what was decided, and why.
Append new entries at the bottom. Never delete existing entries.
"""

CHANGELOG = [

    {
        "id":       "TRIP-001",
        "date":     "2026-08",
        "decision": "Routing direction — clockwise confirmed as optimal",
        "reason": (
            "Five routing circuits computed using haversine distances between all 17 GPS coordinates. "
            "Clockwise (southwest first, Dakotas on return) beats counterclockwise by 249 straight-line miles "
            "(~325 driving miles). Counterclockwise ends with the longest single leg (Sedona → Houston, "
            "~1,019 miles) on the final day when energy is lowest. Clockwise keeps that long diagonal on "
            "Day 2 outbound when fresh, and finishes with the gentle Oklahoma → Houston leg home."
        ),
        "alternatives_considered": [
            "Counterclockwise — rejected: final day too long",
            "Multiple intermediate options — all computed and ranked",
        ],
    },

    {
        "id":       "TRIP-002",
        "date":     "2026-08",
        "decision": "Plan A (Southwest focus) replaced by Plan B (Montana/Dakotas focus)",
        "reason": (
            "Kevin reoriented the trip from a Southwest-focused itinerary (Sedona, Grand Canyon North Rim, "
            "St. George, Bruneau Dunes, Grand Tetons) to a Montana and Dakotas-focused itinerary. "
            "What was gained: 7 nights at Glacier (vs 4), 7 Dakota nights (vs 3), Missouri Breaks routing, "
            "Thermopolis, Medicine Bow. "
            "What was lost: Sedona art scene, Grand Canyon North Rim/Kaibab Plateau, Bruneau Dunes, "
            "St. George, Grand Tetons. "
            "The Southwest destinations are recommended for a dedicated Arizona/Utah trip."
        ),
    },

    {
        "id":       "TRIP-003",
        "date":     "2026-08",
        "decision": "Moab dropped from Plan A",
        "reason": (
            "Moab is a 169 straight-line mile detour off the St. George → Salt Lake City corridor. "
            "Total detour cost: ~220 driving miles, approximately one full driving day. "
            "Saved time was redistributed to Sedona (3 nights vs 2), Grand Tetons (2 nights vs 1), "
            "and Black Hills (3 nights vs 1). "
            "Moab is recommended for a dedicated Utah canyon country trip."
        ),
    },

    {
        "id":       "TRIP-004",
        "date":     "2026-08",
        "decision": "Oklahoma City dropped from return route",
        "reason": (
            "OKC adds 2 hours of driving and one hotel night for two attractions "
            "(OKC National Memorial and Cattlemen's Steakhouse). "
            "Tulsa designated as the final rest stop with the direct push home from there. "
            "Both OKC attractions are genuine losses — if either matters more than an easy final day, "
            "adding OKC back adds only one day to the trip."
        ),
    },

    {
        "id":       "TRIP-005",
        "date":     "2026-08",
        "decision": "White Sands dropped from all plans",
        "reason": (
            "White Sands (Alamogordo NM) sits 200+ miles south and east of the northwestward trajectory "
            "from Palo Duro to Sedona. Adding it would require a 3-4 hour detour south and then "
            "backtracking northwest — effectively a full wasted driving day. "
            "White Sands is recommended for a dedicated southern New Mexico trip "
            "paired with Carlsbad Caverns and Big Bend."
        ),
    },

    {
        "id":       "TRIP-006",
        "date":     "2026-08",
        "decision": "Departure date — Thursday July 15, 2027",
        "reason": (
            "Date is driven by Kevin's parents' schedule. "
            "Parents arrive Salt Lake City July 24, Glacier July 28. "
            "Kevin and Lisa must arrive Glacier July 28 to overlap. "
            "Working back 13 travel days from July 28 gives July 15 departure. "
            "Confirmed benefits: "
            "Pioneer Day July 24 falls at Theodore Roosevelt NP (not Utah) ✅. "
            "Sturgis Rally (August 1-10) — Black Hills completed July 22, 10 days before Sturgis ✅. "
            "Logan Pass shuttle: Tuesday August 3, book recreation.gov June 3 at 7pm MDT."
        ),
        "alternatives_considered": [
            "July 1 departure — Glacier arrival July 14, Logan Pass July 20 (Monday). Badlands on July 4th weekend.",
            "July 8 departure — Glacier arrival July 21, Logan Pass July 27 (Monday). Better Badlands timing but later Glacier.",
            "July 15 departure — CONFIRMED. Driven by parents' schedule. All checks clear.",
        ],
    },

    {
        "id":       "TRIP-007",
        "date":     "2026-08",
        "decision": "Glacier dates — July 28 to August 4, 7 nights",
        "reason": (
            "Fixed by parents' schedule. Parents arrive Glacier July 28 and stay through approximately August 1. "
            "Kevin and Lisa depart August 4. "
            "Going-to-the-Sun Road day designated Tuesday August 3 — weekday, best possible crowd timing. "
            "Weekend days (July 31, August 1) assigned to lake, Apgar Village, and family time. "
            "Logan Pass shuttle for Tuesday August 3: book recreation.gov on June 3, 2027 at 7:00 PM MDT."
        ),
    },

    {
        "id":       "TRIP-008",
        "date":     "2026-08",
        "decision": "Hotel rule — every 4th night maximum outside Glacier",
        "reason": (
            "Never more than 3 consecutive camp nights outside of Glacier. "
            "Glacier 7-night camp is the intentional exception (fixed base, family nearby). "
            "Hotel nights are not a luxury — they are required maintenance for sustained camping. "
            "After 3 nights in a sleeping bag, a hot shower, proper bed, and laundry access "
            "meaningfully improve the quality of the subsequent camp nights."
        ),
        "hotel_schedule": [
            "Day 1 — Wichita",
            "Day 2 — Sioux Falls",
            "Day 4 — Badlands reset (July 4th weekend)",
            "Day 8 — Medora (last hotel before 3 TRNP camp nights)",
            "Day 21 — Helena",
            "Day 25 — Cody",
            "Day 27 — Colorado/Oklahoma",
        ],
    },

    {
        "id":       "TRIP-009",
        "date":     "2026-08",
        "decision": "Missouri Breaks routing selected over I-90/I-15 corridor",
        "reason": (
            "The drive from Miles City to Glacier via US-191 north through James Kipp and Fort Benton "
            "is fundamentally more interesting than I-90 west to I-15 north. "
            "The Upper Missouri River Breaks National Monument covers 377,000 BLM acres. "
            "Lewis and Clark traveled this exact river route in May-June 1805 — much of it unchanged today. "
            "Fort Benton is the birthplace of Montana and one of the finest small-town historical sites in the West. "
            "The Rocky Mountain Front near Choteau is one of the most dramatic landscape transitions in America."
        ),
    },

    {
        "id":       "TRIP-010",
        "date":     "2026-08",
        "decision": "Bonneville Salt Flats — en route stop only, not overnight",
        "reason": (
            "Bonneville (113.9°W) sits right on I-80 between Salt Lake City (111.9°W) and Bruneau Dunes (115.8°W) "
            "in Plan A. The detour cost is only 34 extra straight-line miles vs going direct. "
            "Treating it as a 2-hour mid-morning stop eliminates an unnecessary hotel night. "
            "Not relevant to Plan B — Utah is not on the Plan B route."
        ),
    },

    {
        "id":       "TRIP-011",
        "date":     "2026-08",
        "decision": "Grand Canyon — North Rim selected over South Rim (Plan A only)",
        "reason": (
            "North Rim sees approximately 10% of South Rim visitation. "
            "Kaibab National Forest (1.6 million acres) surrounds the North Rim — dogs fully welcome on all trails. "
            "Jacob Lake Inn (family-owned since 1923) is more characterful than Yavapai Lodge. "
            "8,770 ft elevation means meaningfully cooler July temperatures. "
            "The approach via US-89 through Marble Canyon and Vermilion Cliffs is extraordinary scenery. "
            "Jacob Lake to St. George is only 2h45m vs South Rim to St. George at 4h49m — "
            "a meaningful difference after a full canyon day. "
            "Moot in Plan B — Grand Canyon is not on the Plan B route."
        ),
    },

    {
        "id":       "TRIP-012",
        "date":     "2026-08",
        "decision": "Crowd optimization — start date and activity scheduling",
        "reason": (
            "A crowd scoring model was built assigning weekday (lower) and weekend (higher) scores "
            "to each destination based on NPS visitation data. All July start dates were scored. "
            "Key finding: Grand Canyon and Badlands are mathematically locked — they are 14 days apart "
            "on the itinerary and always fall on the same day of the week. "
            "Getting Grand Canyon on Monday automatically puts Badlands on Saturday. "
            "The July 15 departure (forced by parents' schedule) puts Badlands on Saturday July 17 "
            "with a hotel reset on Sunday and clean Monday departure to the Black Hills. "
            "Glacier weekend days (July 31, August 1) are designated for low-intensity activities "
            "(lake, Apgar, village). Weekdays (August 2-3) are reserved for GTSR and Many Glacier."
        ),
    },

    {
        "id":       "TRIP-013",
        "date":     "2026-08",
        "decision": "Meal plan — hotel nights are breakfast provided + dinner out, no cooking",
        "reason": (
            "Simplifies logistics, eliminates cooking equipment setup at hotels, "
            "and ensures Kevin and Lisa actually rest on hotel nights. "
            "Hotel nights are decompression nights — cooking defeats the purpose. "
            "The 28-day meal plan was built around this rule: camp nights get full three-meal plans, "
            "hotel nights get zero cooking."
        ),
    },

    {
        "id":       "TRIP-014",
        "date":     "2026-08",
        "decision": "Beef tenderloin anniversary dinner — Glacier, August 1",
        "reason": (
            "The fifth wedding anniversary falls during the Glacier week. "
            "The anniversary dinner is designated for August 1 (Sunday) — "
            "a family day with parents still present. "
            "The tenderloin is purchased in Fort Benton or Great Falls and frozen in the Dometic. "
            "Cast iron method: salt 1 hour before, screaming hot pan, butter and rosemary, "
            "sear all sides, rest 10 minutes, slice. "
            "Served with roasted Brussels sprouts from the same pan and fresh no-knead Dutch oven bread "
            "started the night before. Two candles."
        ),
    },

    {
        "id":       "TRIP-015",
        "date":     "2026-08",
        "decision": "Pioneer Day July 24 — confirmed clear of Utah",
        "reason": (
            "Pioneer Day (July 24) is Utah's largest state holiday — "
            "Days of '47 Parade, massive fireworks, road closures, full hotels statewide. "
            "On the July 15 departure schedule, Day 10 (July 24) is at Theodore Roosevelt NP "
            "in Medora, North Dakota. We are nowhere near Utah. ✅"
        ),
    },

    {
        "id":       "TRIP-016",
        "date":     "2026-08",
        "decision": "Sturgis Rally — confirmed 10 days clear",
        "reason": (
            "The Sturgis Motorcycle Rally runs the first full week of August each year — "
            "approximately 700,000+ motorcyclists fill the Black Hills and surrounding towns. "
            "On the July 15 departure schedule, the Black Hills are completed on July 22 — "
            "10 days before the rally begins on August 1. Completely clear. ✅"
        ),
    },

    # ── ADD NEW ENTRIES BELOW ──────────────────────────────────────────────────
]
