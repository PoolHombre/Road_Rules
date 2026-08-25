"""
trip/data/churches.py
Catholic churches along the 2027 route with addresses and Mass schedule notes.

Always verify current Mass times at masstimes.org before each Sunday.
Schedules change seasonally and are not guaranteed.

The Cathedral of Saint Helena in Helena, MT is the spiritual highlight
of the route — visit regardless of Mass times.
"""

CHURCHES = {

    "Wichita": {
        "name":    "Cathedral of the Immaculate Conception",
        "address": "307 E Central Ave, Wichita, KS 67202",
        "phone":   "(316) 263-4295",
        "website": "catholicdioceseofwichita.org",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:00am", "10:00am", "12:00pm", "5:30pm"],
            "weekday":        "8:00am Mon-Fri, 9:00am Sat",
        },
        "notes":   "Diocese Cathedral for Wichita. Multiple Sunday Masses. Large parish.",
        "trip_day": 1,
    },

    "Sioux Falls": {
        "name":    "Cathedral of Saint Joseph",
        "address": "521 N Duluth Ave, Sioux Falls, SD 57104",
        "phone":   "(605) 336-7390",
        "website": "stjosephcathedral.net",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:00am", "10:30am"],
            "weekday":        "7:00am Mon-Fri",
        },
        "notes":   "Diocese of Sioux Falls cathedral. Confirm schedule — summer hours may vary.",
        "trip_day": 2,
    },

    "Rapid City": {
        "name":    "Cathedral of Our Lady of Perpetual Help",
        "address": "500 6th St, Rapid City, SD 57701",
        "phone":   "(605) 343-8541",
        "website": "olphcathedral.org",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:00am", "10:30am", "12:00pm"],
            "weekday":        "7:00am",
        },
        "notes":   "Diocese cathedral for western SD. Serves Days 3-4 (Badlands reset on Sunday).",
        "trip_day": 4,
    },

    "Custer": {
        "name":    "St. John the Baptist",
        "address": "Custer, SD — confirm address at masstimes.org",
        "phone":   "See parish website",
        "type":    "Parish",
        "masses":  {
            "saturday_vigil": "5:00pm (verify)",
            "sunday":         ["9:00am (verify)"],
            "weekday":        "Limited — check",
        },
        "notes":   "Small parish. Verify schedule before planning attendance. "
                   "Alternatively use Rapid City Cathedral (30 min).",
        "trip_day": "5-7",
    },

    "Dickinson": {
        "name":    "Cathedral of St. Patrick",
        "address": "228 E Villard St, Dickinson, ND 58601",
        "phone":   "(701) 225-3883",
        "website": "stpatrickdickinson.org",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:30am", "11:00am"],
            "weekday":        "7:30am",
        },
        "notes":   "Largest Catholic church in western ND. ~35 miles east of Medora. "
                   "Serves Days 8-10 (TRNP area). Saturday vigil on Day 8 is convenient.",
        "trip_day": 8,
    },

    "Miles City": {
        "name":    "Sacred Heart Catholic Church",
        "address": "814 Haynes Ave, Miles City, MT 59301",
        "phone":   "(406) 232-2870",
        "type":    "Parish",
        "masses":  {
            "saturday_vigil": "5:30pm (verify)",
            "sunday":         ["10:00am (verify)"],
            "weekday":        "8:00am (verify)",
        },
        "notes":   "Small parish. Call ahead or check masstimes.org. Day 11 is Sunday.",
        "trip_day": 11,
    },

    "Fort Benton": {
        "name":    "St. Paul's Catholic Church",
        "address": "1104 Front St, Fort Benton, MT 59442",
        "phone":   "(406) 622-3344",
        "type":    "Parish",
        "masses":  {
            "sunday":  ["10:00am (verify)"],
            "weekday": "Limited — check",
        },
        "notes":   "Historic levee parish. Small community. Day 13 is Tuesday — weekday Mass if available.",
        "trip_day": 13,
    },

    "Great Falls": {
        "name":    "St. Ann's Cathedral",
        "address": "2nd Ave N & 15th St, Great Falls, MT 59401",
        "phone":   "(406) 453-0620",
        "website": "diocesegfb.org",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:00pm",
            "sunday":         ["8:00am", "10:00am"],
            "weekday":        "7:00am or 12:10pm",
        },
        "notes":   "Diocese of Great Falls-Billings cathedral. Only if routing through Great Falls on Day 13.",
        "trip_day": "13 (optional)",
    },

    "Columbia Falls": {
        "name":    "St. Richard",
        "address": "250 5th Ave W, Columbia Falls, MT 59912",
        "phone":   "(406) 892-3666",
        "type":    "Parish",
        "masses":  {
            "sunday":  ["9:00am (verify)"],
            "weekday": "Limited — check",
        },
        "notes":   "Closest church to the Glacier west entrance. ~8 miles. Serves Glacier week.",
        "trip_day": "14-20",
    },

    "Kalispell": {
        "name":    "Holy Spirit Catholic Church",
        "address": "130 6th Ave E, Kalispell, MT 59901",
        "phone":   "(406) 752-5135",
        "website": "holyspiritksp.org",
        "type":    "Parish",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:30am", "10:30am"],
            "weekday":        "8:00am Mon-Fri",
        },
        "notes":   "~30 min from West Glacier. Solid option for Saturday vigil or Sunday during Glacier week.",
        "trip_day": "14-20",
    },

    "Whitefish": {
        "name":    "St. Matthew",
        "address": "600 E 2nd St, Whitefish, MT 59937",
        "phone":   "(406) 862-2613",
        "type":    "Parish",
        "masses":  {
            "saturday_vigil": "5:00pm",
            "sunday":         ["9:00am", "11:00am"],
            "weekday":        "8:00am",
        },
        "notes":   "~20 min from West Glacier. Good Saturday vigil option during Glacier week. "
                   "Whitefish has good restaurants for dinner after Mass.",
        "trip_day": "14-20",
    },

    "Helena": {
        "name":    "Cathedral of Saint Helena",
        "address": "530 N Ewing St, Helena, MT 59601",
        "phone":   "(406) 442-5825",
        "website": "sthelena.org",
        "type":    "Diocese Cathedral — National Register of Historic Places",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["9:00am", "11:00am"],
            "weekday":        "7:30am or 12:10pm",
        },
        "notes":   (
            "THE CATHEDRAL OF SAINT HELENA IS A DESTINATION VISIT. "
            "Gothic Revival construction began 1908, first Mass 1914. "
            "Modeled on the Votive Church in Vienna. Marble pillars, stunning stained glass. "
            "National Register of Historic Places. Helena Symphony performs here. "
            "Visit regardless of Mass times — a quiet hour in this space after three weeks "
            "on the road is worth planning around."
        ),
        "trip_day": 21,
    },

    "Thermopolis": {
        "name":    "Our Lady of the Mountains",
        "address": "420 Arapahoe St, Thermopolis, WY 82443",
        "phone":   "(307) 864-2517",
        "type":    "Parish",
        "masses":  {
            "sunday":  ["10:00am (verify)"],
            "weekday": "Limited — check masstimes.org",
        },
        "notes":   "Small parish. Day 23 is Friday — weekday Mass if available. Verify at masstimes.org.",
        "trip_day": 23,
    },

    "Worland": {
        "name":    "Confirm at masstimes.org",
        "address": "Worland, WY — nearest town to Bighorns with Catholic parish",
        "notes":   "~40 miles south of the Bighorn Plateau. Day 24 is Saturday — vigil option.",
        "trip_day": 24,
    },

    "Cody": {
        "name":    "Sacred Heart Catholic Church",
        "address": "1430 Beck Ave, Cody, WY 82414",
        "phone":   "(307) 587-4041",
        "type":    "Parish",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:00am", "10:30am"],
            "weekday":        "8:00am",
        },
        "notes":   "Day 25 is Sunday. Multiple Mass times — 10:30am is probably most convenient.",
        "trip_day": 25,
    },

    "Laramie": {
        "name":    "St. Laurence O'Toole",
        "address": "1026 Steele St, Laramie, WY 82070",
        "phone":   "(307) 742-3345",
        "type":    "Parish",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:30am", "11:00am"],
            "weekday":        "7:30am",
        },
        "notes":   "University town parish. Day 27 is Monday — weekday Mass if available.",
        "trip_day": 27,
    },

    "Tulsa": {
        "name":    "Holy Family Cathedral",
        "address": "8 W 5th St, Tulsa, OK 74103",
        "phone":   "(918) 582-6247",
        "website": "holyfamilycathedral.net",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:30pm",
            "sunday":         ["8:00am", "10:00am", "12:00pm"],
            "weekday":        "12:10pm",
        },
        "notes":   "Diocese of Tulsa cathedral. Only if routing through Tulsa on Day 27.",
        "trip_day": "27 (if routing through Tulsa)",
    },

    "Oklahoma City": {
        "name":    "Our Lady's Cathedral",
        "address": "307 NW 4th St, Oklahoma City, OK 73102",
        "phone":   "(405) 232-4406",
        "type":    "Diocese Cathedral",
        "masses":  {
            "saturday_vigil": "5:00pm",
            "sunday":         ["9:00am", "11:00am"],
            "weekday":        "12:05pm",
        },
        "notes":   "Diocese of Oklahoma City cathedral. Only if routing through OKC on Day 27.",
        "trip_day": "27 (if routing through OKC)",
    },
}


# ── SUNDAY MASS CALENDAR ──────────────────────────────────────────────────────
# Which church to attend on each Sunday of the trip.

SUNDAY_PLAN = [
    {"day": 2,  "date": "Fri Jul 16", "note": "Not a Sunday — Friday arrival in Sioux Falls"},
    {"day": 4,  "date": "Sun Jul 18", "church": "Rapid City",  "name": "Cathedral of Our Lady of Perpetual Help"},
    {"day": 11, "date": "Sun Jul 25", "church": "Miles City",   "name": "Sacred Heart — confirm schedule"},
    {"day": 18, "date": "Sun Aug 1",  "church": "Kalispell or Columbia Falls",
     "name": "Holy Spirit Kalispell or St. Richard Columbia Falls — parents may want to attend, coordinate"},
    {"day": 25, "date": "Sun Aug 8",  "church": "Cody",         "name": "Sacred Heart"},
]

SATURDAY_VIGIL_OPTIONS = [
    {"day": 1,  "date": "Thu Jul 15", "note": "No vigil — driving day, arrive Wichita late"},
    {"day": 8,  "date": "Thu Jul 22", "church": "Dickinson",    "name": "Cathedral of St. Patrick — Day 8 hotel night, 35 mi from Medora"},
    {"day": 17, "date": "Sat Jul 31", "church": "Kalispell or Whitefish",
     "name": "Holy Spirit or St. Matthew — Glacier weekend day, good evening option"},
    {"day": 24, "date": "Sat Aug 7",  "church": "Worland WY",   "name": "Verify at masstimes.org — ~40 mi south of Bighorns"},
]
