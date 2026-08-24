"""
trip/data/destinations.py
All overnight destinations for the 2027 Glacier NP road trip.
Each entry is a complete research record — GPS, crowd data,
camping, restaurants, churches, BJJ, arts, history, dog notes.
"""

# ── DESTINATION RECORDS ───────────────────────────────────────────────────────
# Each key is the canonical stop name used throughout the codebase.
# GPS coordinates are (lat, lon) in decimal degrees.

DESTINATIONS = {

    "Houston": {
        "gps":    (29.760, -95.370),
        "type":   "origin",
        "state":  "TX",
        "notes":  "Departure and return point.",
    },

    "Wichita": {
        "gps":    (37.685, -97.330),
        "type":   "hotel",
        "state":  "KS",
        "crowd":  {"weekday": 2, "weekend": 3},
        "drive_from_prev": {"from": "Houston", "miles": 450, "hours": 6.0, "route": "I-35 N"},
        "restaurants": [
            {"name": "Georges French Bistro",  "address": "5 E Douglas Ave",     "notes": "James Beard semifinalist, finest dining in Wichita"},
            {"name": "Doo-Dah Diner",          "address": "206 E Kellogg St",    "notes": "Beloved local institution, breakfast all day"},
            {"name": "The Monarch",            "address": "579 E Douglas Ave",   "notes": "Craft cocktails, Douglas Design District"},
        ],
        "churches": [
            {"name": "Cathedral of the Immaculate Conception", "address": "307 E Central Ave",
             "notes": "Diocese Cathedral — Saturday vigil and multiple Sunday Masses"},
        ],
        "bjj": [
            {"name": "Check graciebarra.com", "address": "—", "notes": "Growing city — may have location by 2027"},
        ],
        "arts": [
            {"name": "Keeper of the Plains Ring of Fire", "details": "Nightly 9pm, free — 44-ft steel sculpture, fire pots lit at the river confluence. Do not skip."},
            {"name": "Wichita Art Museum",                "details": "1400 W Museum Blvd — largest American art collection in the region"},
            {"name": "Wichita Symphony",                  "details": "Century II Performing Arts Center — check summer 2027 schedule"},
            {"name": "First Friday Art Crawls",           "details": "Douglas Design District — monthly"},
        ],
        "poi": [
            {"name": "Keeper of the Plains",     "details": "44-ft steel sculpture at the confluence of the Arkansas rivers"},
            {"name": "Old Cowtown Museum",       "details": "1865 Museum Blvd — living history 1870s Wichita, dogs on leash outside"},
            {"name": "Mid-America All-Indian Museum", "details": "650 N Seneca St — Plains Indian heritage"},
            {"name": "Frank Lloyd Wright Allen House", "details": "255 N Roosevelt St — 1920 National Historic Landmark"},
        ],
        "history": (
            "Wichita sits at the confluence of the Arkansas and Little Arkansas rivers — "
            "a sacred Wichita and Lakota trading crossroads before European contact. "
            "Wyatt Earp served as assistant city marshal 1874-75. "
            "More than 50% of all general aviation aircraft ever built came from Wichita — "
            "Boeing, Cessna, and Beechcraft all have roots here."
        ),
        "dogs": "Keeper of the Plains river walk — dogs on leash. Riverside Park excellent for morning walks.",
        "lodging": [
            {"name": "Hotel at Old Town", "address": "830 E 1st St N", "pet_friendly": True, "notes": "Boutique, downtown Wichita"},
        ],
    },

    "Sioux Falls": {
        "gps":    (43.548, -96.731),
        "type":   "hotel",
        "state":  "SD",
        "crowd":  {"weekday": 2, "weekend": 3},
        "drive_from_prev": {"from": "Wichita", "miles": 460, "hours": 6.0, "route": "I-135 N → I-90 E"},
        "restaurants": [
            {"name": "Bread & Circus Sandwich Kitchen", "address": "510 N Phillips Ave",  "notes": "Local institution, excellent sandwiches"},
            {"name": "Sanaa's Gourmet Mediterranean",   "address": "300 S Phillips Ave",  "notes": "James Beard recognition, outstanding"},
            {"name": "Lost Arc Brewing",                "address": "500 E 69th St",       "notes": "Craft beer, dog-friendly patio"},
        ],
        "churches": [
            {"name": "Cathedral of Saint Joseph", "address": "521 N Duluth Ave",
             "notes": "Diocese of Sioux Falls — Saturday vigil and Sunday Masses"},
        ],
        "bjj": [
            {"name": "Check graciebarra.com", "address": "—", "notes": "Growing city — check before trip"},
        ],
        "arts": [
            {"name": "SculptureWalk",                     "details": "60+ international sculptures along Phillips Ave — free, self-guided"},
            {"name": "Washington Pavilion of Arts",       "details": "301 S Main Ave — visual arts, performing arts, science center"},
        ],
        "poi": [
            {"name": "Falls Park",      "details": "Sioux Quartzite waterfalls in the center of the city — dogs on leash"},
            {"name": "SculptureWalk",   "details": "Downtown river walk — 60+ sculptures"},
        ],
        "history": (
            "The falls of the Big Sioux River were a sacred Lakota meeting place. "
            "The pink Sioux Quartzite forming the falls is 1.7 billion years old. "
            "The city grew rapidly after the 1880s railroad arrival."
        ),
        "dogs": "Falls Park and SculptureWalk both dog-friendly on leash.",
        "notes": "Resupply here for Days 3-6. Hotel night — laundry, showers, rest before camping begins.",
    },

    "Badlands": {
        "gps":    (43.855, -102.337),
        "type":   "camp_then_hotel",
        "state":  "SD",
        "crowd":  {"weekday": 7, "weekend": 10},
        "drive_from_prev": {"from": "Sioux Falls", "miles": 350, "hours": 5.0, "route": "I-90 W"},
        "camping": [
            {"name": "Sage Creek Wilderness Campground", "type": "NPS free",
             "notes": "Inside the park. Free, no reservations, 22 sites, dark sky. Arrive by noon in summer. Dogs on leash in camp."},
            {"name": "Cedar Pass Campground",            "type": "NPS",
             "notes": "Reservation-based at recreation.gov. More developed, closer to visitor center."},
        ],
        "restaurants": [
            {"name": "Cedar Pass Lodge Restaurant", "address": "Inside the park",              "notes": "Basic but convenient"},
            {"name": "Wall Drug",                   "address": "510 Main St, Wall SD",        "notes": "Obligatory — 5-cent coffee and donuts"},
            {"name": "Firehouse Brewing Co",        "address": "610 Main St, Rapid City",     "notes": "Best craft beer in Rapid City"},
        ],
        "churches": [
            {"name": "Cathedral of Our Lady of Perpetual Help", "address": "500 6th St, Rapid City",
             "notes": "Diocese cathedral for western SD"},
        ],
        "bjj": [
            {"name": "Check graciebarra.com for Rapid City", "address": "—", "notes": "Network expanding — check before trip"},
        ],
        "arts": [
            {"name": "Prairie Edge Gallery", "details": "606 Main St, Rapid City — extraordinary Native American art, beadwork, jewelry. One of the best galleries on the entire trip."},
            {"name": "Dahl Arts Center",     "details": "713 7th St, Rapid City — local and regional contemporary art"},
        ],
        "poi": [
            {"name": "Badlands Loop Road (SD-240)", "details": "Bison, bighorn sheep, prairie dogs, fossils in the canyon walls"},
            {"name": "Sage Creek Rim Road",         "details": "Enters wilderness area — bison at dawn guaranteed"},
            {"name": "Roberts Prairie Dog Town",    "details": "Largest prairie dog colony in the park"},
            {"name": "Minuteman Missile NHS",       "details": "30 min east — Cold War ICBM launch facility, free, sobering and important"},
        ],
        "history": (
            "Mako Sica — bad lands — is the Lakota name. The White River Badlands expose "
            "fossils from 23-35 million years ago. Wounded Knee Massacre occurred 60 miles "
            "south in 1890 — last major armed conflict of the American Indian Wars. "
            "The land was transferred from the Lakota to NPS in a contested process beginning in 1939."
        ),
        "dogs": (
            "Dogs in campgrounds and parking areas on leash. NOT on trails. "
            "Tango (ADA service animal) on all trails. "
            "Bison wander through Sage Creek at dawn — keep dogs in van overnight."
        ),
        "crowd_strategy": (
            "July weekend = peak. Arrive Sage Creek by noon Saturday to secure a site. "
            "Hotel reset Sunday gives a shower and proper night before three more camp nights. "
            "Sunday morning: Badlands Loop before 8am — nearly empty."
        ),
    },

    "Black Hills": {
        "gps":    (43.855, -103.500),
        "type":   "camp",
        "state":  "SD",
        "crowd":  {"weekday": 6, "weekend": 9},
        "drive_from_prev": {"from": "Badlands", "miles": 100, "hours": 1.5, "route": "SD-44 W"},
        "camping": [
            {"name": "Sylvan Lake Campground, Custer SP", "type": "State Park",
             "notes": "Lakeside, stunning Black Hills setting. Reserve at custerresorts.com. Best campsite in the Black Hills."},
            {"name": "Black Hills NF Dispersed",          "type": "NF free",
             "notes": "353 miles of trails, free, dogs on leash. Endless options throughout the forest."},
            {"name": "Game Lodge Campground, Custer SP",  "type": "State Park",
             "notes": "Historic area, hookups available. custerresorts.com."},
        ],
        "restaurants": [
            {"name": "Laughing Water Restaurant, Crazy Horse", "address": "12151 Ave of the Chiefs", "notes": "Supports the memorial, surprisingly good"},
            {"name": "Custer Drug Store",                      "address": "545 Mt Rushmore Rd",      "notes": "Old soda fountain, local institution"},
            {"name": "Buglin' Bull Restaurant",                "address": "511 Mt Rushmore Rd",      "notes": "Local favorite, game meat"},
        ],
        "churches": [
            {"name": "Our Lady of Perpetual Help, Rapid City", "address": "500 6th St, Rapid City",
             "notes": "30 min from Custer — main Diocese cathedral for the region"},
        ],
        "bjj": [
            {"name": "Check graciebarra.com for Rapid City", "address": "—", "notes": "Check before trip"},
        ],
        "arts": [
            {"name": "Crazy Horse Memorial",  "details": "12 mi from Custer — the ongoing mountain carving is itself monumental art. Museum and cultural center extraordinary."},
            {"name": "Black Hills Playhouse", "details": "Custer SP — summer theater in the hills. blackhillsplayhouse.com."},
        ],
        "poi": [
            {"name": "Custer State Park Wildlife Loop", "details": "18-mile loop — bison, pronghorn, wild burros — go at dawn"},
            {"name": "Needles Highway",                 "details": "Narrow granite tunnels through spire formations — one of the great scenic drives"},
            {"name": "Crazy Horse Memorial",            "details": "17 mi from Custer — more powerful than Rushmore, ongoing since 1948"},
            {"name": "Sylvan Lake",                     "details": "Crystal clear granite lake, dogs on leash at the shore"},
            {"name": "Jewel Cave NM",                   "details": "Third longest cave in the world — book ranger-led tours at recreation.gov"},
            {"name": "Deadwood",                        "details": "Gold rush town, Wild Bill Hickok shot at Saloon No. 10 in 1876"},
            {"name": "Devils Tower NM",                 "details": "867-ft volcanic monolith — dogs on 1.3-mi base trail, prairie dog colony spectacular"},
        ],
        "history": (
            "Paha Sapa (the Black Hills) are the sacred center of Lakota cosmology. "
            "The 1868 Fort Laramie Treaty guaranteed the hills forever. Gold discovered "
            "in 1874 by Custer's expedition violated the treaty and triggered the Great Sioux War. "
            "The Supreme Court ruled in 1980 the land was taken illegally. "
            "The Lakota refused $106M in compensation. The trust fund now exceeds $1 billion, unclaimed."
        ),
        "dogs": (
            "Black Hills NF — dogs on leash on all 353 miles of trails. "
            "Custer State Park — dogs on leash in most areas including Wildlife Loop Road. "
            "Sylvan Lake shore — dogs on leash. Jewel Cave — dogs in picnic area only."
        ),
        "sturgis_warning": (
            "Sturgis Rally runs first week of August — 700,000+ motorcyclists. "
            "We finish Black Hills July 22, 10 days before Sturgis begins. Clear."
        ),
    },

    "Theodore Roosevelt": {
        "gps":    (46.979, -103.540),
        "type":   "hotel_then_camp",
        "state":  "ND",
        "crowd":  {"weekday": 4, "weekend": 6},
        "drive_from_prev": {"from": "Black Hills", "miles": 275, "hours": 4.5, "route": "I-90 W → I-94 W"},
        "camping": [
            {"name": "Cottonwood Campground, TRNP South Unit", "type": "NPS reservation",
             "notes": "Reservation-based since 2026. Book at recreation.gov. Riverside sites on the Little Missouri. Dogs on leash in camp."},
            {"name": "Juniper Campground, TRNP South Unit",    "type": "NPS reservation",
             "notes": "Alternative reservation campground. recreation.gov."},
            {"name": "Little Missouri National Grassland",     "type": "BLM free",
             "notes": "Surrounding the park. Dogs fully welcome, no restrictions. Free dispersed camping."},
        ],
        "restaurants": [
            {"name": "Theodore's Dining Room, Rough Riders Hotel", "address": "301 3rd Ave, Medora", "notes": "Solid food in a historic building"},
            {"name": "Pitchfork Fondue",                           "address": "Medora ND",           "notes": "Outdoor steak dinner, steaks cooked on pitchforks over fire — uniquely North Dakotan"},
            {"name": "Medora Fudge and Ice Cream Depot",          "address": "Medora ND",           "notes": "The Medora tradition"},
        ],
        "churches": [
            {"name": "Cathedral of St. Patrick, Dickinson", "address": "228 E Villard St, Dickinson ND",
             "notes": "Largest Catholic church in western ND — ~35 mi east of Medora"},
        ],
        "bjj": [
            {"name": "None near Medora", "address": "—", "notes": "Bismarck (~100 mi east) may have options. Check graciebarra.com."},
        ],
        "arts": [
            {"name": "Medora Musical",           "details": "Outdoor amphitheater, nightly summer performances. medora.com. Running since 1965."},
            {"name": "Pitchfork Fondue",         "details": "Outdoor dinner event before the Musical — reserve in advance at medora.com"},
            {"name": "Chateau de Mores",         "details": "Medora — 1883 French marquis chateau, guided tours, fascinating and strange"},
            {"name": "Enchanted Highway",        "details": "I-94 Exit 72 near Gladstone — 32 miles of giant scrap metal sculptures, Geese in Flight at 110 ft. Free."},
        ],
        "poi": [
            {"name": "South Unit Scenic Loop (36 mi)", "details": "Wild horses, bison, prairie dogs from the vehicle"},
            {"name": "Painted Canyon Visitor Center",  "details": "I-94 Exit 32 — free, panoramic view, dogs on sidewalk"},
            {"name": "North Unit day trip",            "details": "70 mi north on US-85 — quieter, cannonball concretions, Long X Trail (dogs on leash)"},
            {"name": "Little Missouri River",          "details": "Wade with dogs in the national grassland — dogs fully welcome"},
        ],
        "history": (
            "Theodore Roosevelt arrived in 1883 to hunt bison, two days after the deaths "
            "of his wife and mother on the same day — February 14, 1884. "
            "Three years of hard ranch work transformed him into the conservationist who "
            "created the National Park System, 150 national forests, and 18 national monuments. "
            "He said: 'I never would have been President if it had not been for my experiences in North Dakota.'"
        ),
        "dogs": (
            "Dogs in campgrounds and parking areas on leash. NOT on park trails. "
            "Tango (ADA) on all trails. "
            "Little Missouri National Grassland — dogs fully welcome, no restrictions."
        ),
        "pioneer_day_note": "Pioneer Day July 24 falls on Day 10 at TRNP. We are in North Dakota. ✅",
    },

    "Miles City": {
        "gps":    (46.408, -105.840),
        "type":   "camp",
        "state":  "MT",
        "crowd":  {"weekday": 1, "weekend": 1},
        "drive_from_prev": {"from": "Theodore Roosevelt", "miles": 200, "hours": 3.5, "route": "I-94 W"},
        "camping": [
            {"name": "BLM dispersed along the Yellowstone", "type": "BLM free",
             "notes": "Multiple sites east of Miles City along the river. Cottonwood groves, dog swimming. Free."},
            {"name": "Tongue River Reservoir SP",           "type": "State Park",
             "notes": "22 miles south, reservoir camping, some hookups. stateparks.mt.gov."},
        ],
        "restaurants": [
            {"name": "600 Bar and Grill",  "address": "600 Main St, Miles City", "notes": "Locals' choice, good food"},
            {"name": "Hole in the Wall",   "address": "602 Main St, Miles City", "notes": "Cold beer, genuine Montana atmosphere"},
        ],
        "churches": [
            {"name": "Sacred Heart Catholic Church", "address": "814 Haynes Ave, Miles City",
             "notes": "Confirm schedule before arrival"},
        ],
        "bjj": [
            {"name": "None", "address": "—", "notes": "Remote eastern Montana"},
        ],
        "arts": [
            {"name": "Range Rider Museum", "details": "435 LP Anderson Rd — genuine frontier history, one of the best small museums in Montana"},
        ],
        "poi": [
            {"name": "Range Rider Museum",    "details": "Frontier history, undervisited gem"},
            {"name": "Miles City Stockyards", "details": "Operating cattle auction — call (406) 232-5353 for schedule"},
            {"name": "Yellowstone River",     "details": "BLM land, cottonwood groves, dog swimming — Tango will love it"},
        ],
        "history": (
            "Miles City was founded in 1876 as a military camp following Little Bighorn (57 miles northwest). "
            "It became the center of the open-range cattle empire of the 1880s. "
            "The catastrophic winter of 1886-87 killed 60-90% of range cattle across eastern Montana "
            "and ended the era in a single season."
        ),
        "dogs": "Yellowstone River BLM land — dogs fully welcome. River swimming. Tongue River SP — dogs on leash.",
        "resupply_note": (
            "CRITICAL RESUPPLY: Stock up at the IGA in Miles City before heading northwest. "
            "This grocery carries you through the Missouri Breaks remote stretch to Fort Benton."
        ),
    },

    "Missouri Breaks": {
        "gps":    (47.500, -108.950),
        "type":   "camp",
        "state":  "MT",
        "crowd":  {"weekday": 2, "weekend": 2},
        "drive_from_prev": {"from": "Miles City", "miles": 250, "hours": 4.5, "route": "US-191 N"},
        "camping": [
            {"name": "James Kipp Recreation Area", "type": "BLM developed",
             "notes": "On the Missouri River at US-191. Basic facilities. Dogs welcome. Canoe launches."},
            {"name": "Coal Banks Landing",          "type": "BLM developed",
             "notes": "41 miles west on the river. More sites. Lewis & Clark campsites nearby."},
            {"name": "American Prairie Reserve",    "type": "BLM/private",
             "notes": "7 mi north of James Kipp on US-191. Prairie dog town, wetlands, some hookups."},
        ],
        "restaurants": [
            {"name": "No restaurants", "address": "—", "notes": "Self-sufficient. Cook at camp."},
        ],
        "churches": [
            {"name": "None on this segment", "address": "—", "notes": "St. Paul's in Fort Benton (next day)"},
        ],
        "bjj": [
            {"name": "None", "address": "—", "notes": "Remote north-central Montana"},
        ],
        "arts": [
            {"name": "Museum of the Upper Missouri (Fort Benton)", "details": "Visited next day — one of the finest small museums in Montana"},
        ],
        "poi": [
            {"name": "James Kipp Recreation Area",      "details": "Missouri River, BLM, camp on the river, canoe launches"},
            {"name": "Coal Banks Landing",              "details": "River access, Lewis & Clark campsites, white chalk cliffs visible"},
            {"name": "Upper Missouri River Breaks NM",  "details": "377,000 BLM acres — some of the most remote public land in Montana"},
        ],
        "history": (
            "Lewis and Clark traveled this exact stretch of the Missouri River in May-June 1805. "
            "Clark wrote: 'the hills and river cliffs which we passed today exhibit a most romantic appearance.' "
            "The white chalk cliffs and dark ponderosa pines looked like ruins of ancient architecture. "
            "Much of it looks the same today. The Breaks were also the hiding grounds of Butch Cassidy "
            "and the Sundance Kid."
        ),
        "dogs": (
            "James Kipp BLM — dogs fully welcome, no restrictions. Missouri River swimming for Tango. "
            "Watch for rattlesnakes on rocky areas in July."
        ),
        "connectivity": "No cell service. Download offline maps before leaving Miles City. Garmin inReach on.",
    },

    "Fort Benton": {
        "gps":    (47.820, -110.640),
        "type":   "camp",
        "state":  "MT",
        "crowd":  {"weekday": 2, "weekend": 2},
        "drive_from_prev": {"from": "Missouri Breaks", "miles": 120, "hours": 2.5, "route": "US-87 N"},
        "camping": [
            {"name": "BLM dispersed near Fort Benton", "type": "BLM free",
             "notes": "Along the Missouri River levee road. Free."},
            {"name": "Choteau BLM / Teton River area",  "type": "BLM free",
             "notes": "Northwest of Fort Benton toward Glacier. Base of the Rocky Mountain Front. Grizzly bear country."},
        ],
        "restaurants": [
            {"name": "Grand Union Hotel Restaurant", "address": "1 Grand Union Sq, Fort Benton",
             "notes": "1882 hotel on the levee — best food in north-central Montana. Eat lunch here."},
            {"name": "Missouri River Brewing, Great Falls", "address": "412 Central Ave, Great Falls",
             "notes": "Good local brewery if routing through Great Falls"},
        ],
        "churches": [
            {"name": "St. Paul's Catholic Church", "address": "1104 Front St, Fort Benton",
             "notes": "Historic levee parish — weekday Mass if available"},
            {"name": "St. Ann's Cathedral, Great Falls", "address": "2nd Ave N & 15th St, Great Falls",
             "notes": "Diocese of Great Falls-Billings — if routing through Great Falls"},
        ],
        "bjj": [
            {"name": "None", "address": "—", "notes": "Remote north-central Montana"},
        ],
        "arts": [
            {"name": "Museum of the Upper Missouri", "details": "Fort Benton — steamboat era, Lewis & Clark, Blackfeet and Assiniboine history. One of the finest small museums in Montana."},
            {"name": "Missouri Breaks Interpretive Center", "details": "Fort Benton — excellent orientation for the monument"},
        ],
        "poi": [
            {"name": "Fort Benton levee walk",           "details": "Grand Union Hotel, T.C. Powers Building, original adobe fort remains"},
            {"name": "Museum of the Upper Missouri",     "details": "Steamboat era, Lewis & Clark, tribal history"},
            {"name": "Rocky Mountain Front near Choteau","details": "Abrupt wall where the Rockies meet the plains — grizzly bear country, dramatic landscape transition"},
        ],
        "history": (
            "Fort Benton was the head of navigation on the Missouri River. "
            "At its peak in 1879, 45 steamboats docked in a single season. "
            "Lewis and Clark passed through in May 1805. "
            "'Birthplace of Montana' — the smallest National Historic Landmark."
        ),
        "dogs": (
            "Fort Benton levee walk — dogs on leash. BLM near Fort Benton — dogs fully welcome. "
            "Choteau/Rocky Mountain Front area — grizzly bear country, dogs must be under strict leash control."
        ),
        "resupply_note": (
            "RESUPPLY in Fort Benton or Great Falls for Days 14-17. "
            "Buy beef tenderloin now — freeze it. Blueberries, strawberries, whipped cream. "
            "Flour and yeast for Dutch oven bread. Full stock before Glacier."
        ),
    },

    "Glacier": {
        "gps":    (48.700, -113.800),
        "type":   "base_camp",
        "state":  "MT",
        "nights": 7,
        "crowd":  {"weekday": 7, "weekend": 10},
        "drive_from_prev": {"from": "Fort Benton", "miles": 150, "hours": 2.5, "route": "US-89 → MT-2"},
        "parents": {
            "arrive": "July 28, 2027",
            "depart": "~August 1, 2027",
            "notes":  "Coordinate rendezvous at Apgar Village or west entrance on arrival day",
        },
        "logan_pass": {
            "date":    "Tuesday, August 3, 2027",
            "shuttle": "Book at recreation.gov on June 3, 2027 at 7:00 PM MDT",
            "notes":   "60-day advance window. Sells out in minutes. Be logged in before 7pm.",
        },
        "camping": [
            {"name": "Flathead NF dispersed, near West Glacier or Columbia Falls", "type": "NF free",
             "notes": "2.4 million acres surrounding the park. Dogs on leash, all trails accessible. Free. PREFERRED."},
            {"name": "Apgar Campground, in-park", "type": "NPS reservation",
             "notes": "West entrance area. Dogs in campground. Some hookups. recreation.gov."},
        ],
        "restaurants": [
            {"name": "Belton Chalet Grill",   "address": "12575 US-2 E, West Glacier",    "notes": "Historic 1910 chalet, dog-friendly patio"},
            {"name": "Packer's Roost",        "address": "9 Nucleus Ave, Columbia Falls", "notes": "Locals' pub, cold beer"},
            {"name": "Park Cafe, St. Mary",   "address": "106 US-89, St. Mary",           "notes": "Legendary pie, seasonal, east entrance"},
            {"name": "Loula's Cafe, Whitefish","address": "300 2nd St E, Whitefish",       "notes": "Excellent breakfast, locals' favorite"},
        ],
        "churches": [
            {"name": "St. Richard",  "address": "250 5th Ave W, Columbia Falls", "notes": "Closest to the west entrance"},
            {"name": "Holy Spirit",  "address": "130 6th Ave E, Kalispell",      "notes": "~30 min from West Glacier"},
            {"name": "St. Matthew", "address": "600 E 2nd St, Whitefish",        "notes": "~20 min from West Glacier"},
        ],
        "bjj": [
            {"name": "None confirmed in area", "address": "—",
             "notes": "Gracie Barra Montana was in Bozeman (~2.5 hrs). Check graciebarra.com for any Kalispell/Whitefish location."},
        ],
        "arts": [
            {"name": "Glacier Symphony",         "details": "Whitefish Arts Center — glaciersymphony.org — summer concert schedule"},
            {"name": "Hockaday Museum of Art",   "details": "302 2nd Ave E, Kalispell — Montana and Northwest art, free admission"},
            {"name": "Bigfork Summer Playhouse", "details": "526 Electric Ave, Bigfork — professional Equity theater on Flathead Lake, Sunday matinees"},
            {"name": "Whitefish Arts Festival",  "details": "Typically first weekend of August — verify 2027 dates"},
        ],
        "poi": [
            {"name": "Going-to-the-Sun Road",     "details": "50 miles through the alpine heart — Logan Pass 6,646 ft. Book shuttle for Tuesday August 3."},
            {"name": "Many Glacier",              "details": "East side — Swiftcurrent Lake — least crowded major destination in the park"},
            {"name": "Flathead National Forest",  "details": "2.4 million acres — dogs on leash, all trails accessible"},
            {"name": "Lake McDonald",             "details": "Turquoise glacier-fed lake — boat rides (dogs allowed in boats)"},
            {"name": "Flathead Lake",             "details": "1 hr south — largest freshwater lake west of the Mississippi, dogs welcome"},
            {"name": "Whitefish Trails",          "details": "Dog-friendly mountain biking and hiking, 20 min from park"},
            {"name": "Waterton Lakes NP, Canada", "details": "30 min north across border — dogs more welcome than at Glacier"},
        ],
        "history": (
            "Going-to-the-Sun Road was built 1921-1932 by 1,000 workers cutting 50 miles of road "
            "into the Continental Divide by hand. Crown of the Continent designation recognizes "
            "the headwaters of three major river systems: the Columbia, the Missouri, and the Saskatchewan — "
            "water flowing to three oceans. Glacier had over 150 glaciers in 1850. Approximately 26 remain."
        ),
        "dogs": (
            "Inside the park: dogs on leash in developed areas, campgrounds, and parking only. "
            "NOT on backcountry trails. Tango (ADA service animal) allowed everywhere including all trails. "
            "Saki — developed areas and the van. "
            "Flathead NF outside the park: dogs on leash, all trails accessible."
        ),
        "van_size_warning": (
            "Vehicles over 21 feet long or 8 feet wide prohibited on Going-to-the-Sun Road "
            "between Avalanche Creek and Sun Point. "
            "Savana Extended (155 in wheelbase) is approximately 19-20 feet — should be fine. "
            "Confirm exact measurement with Aluminess bumper installed before the trip."
        ),
        "crowd_strategy": (
            "Weekend days (July 31, August 1): Apgar Village, Lake McDonald, family time. "
            "Weekdays (July 29-30, August 2): Flathead NF dog hiking, Many Glacier. "
            "Tuesday August 3: Going-to-the-Sun Road — book Logan Pass shuttle June 3."
        ),
    },

    "Helena": {
        "gps":    (46.596, -112.027),
        "type":   "hotel",
        "state":  "MT",
        "crowd":  {"weekday": 2, "weekend": 3},
        "drive_from_prev": {"from": "Glacier", "miles": 200, "hours": 4.5, "route": "US-2 → I-15 S"},
        "restaurants": [
            {"name": "On Broadway",          "address": "106 Broadway",         "notes": "Excellent local fine dining"},
            {"name": "Havre de Grace",       "address": "42 S Park Ave",        "notes": "Small, seasonal, outstanding"},
            {"name": "Blackfoot River Brewing","address": "66 S Park Ave",      "notes": "Local craft beer, good pub food"},
            {"name": "Cotton-Top Bakery",    "address": "38 N Last Chance Gulch","notes": "Pastry-school trained, worth a line"},
        ],
        "churches": [
            {"name": "Cathedral of Saint Helena", "address": "530 N Ewing St",
             "notes": "NATIONAL REGISTER OF HISTORIC PLACES. Gothic Revival 1908-1914. Marble pillars, stunning stained glass. Helena Symphony performs here. Visit regardless of Mass times."},
        ],
        "bjj": [
            {"name": "Check graciebarra.com for Helena", "address": "—", "notes": "State capital — possible location by 2027"},
        ],
        "arts": [
            {"name": "Holter Museum of Art",  "details": "12 E Lawrence St — contemporary Northwest art, rotating exhibitions, free"},
            {"name": "Helena Symphony",       "details": "Performs at Cathedral of Saint Helena — helenasymphony.org"},
            {"name": "Alive at Five",         "details": "Thursday summer evenings, downtown Helena, free outdoor music"},
            {"name": "Myrna Loy Center",      "details": "15 N Ewing St — independent film, small concerts in a former jail"},
        ],
        "poi": [
            {"name": "Cathedral of Saint Helena", "details": "530 N Ewing St — visit regardless of Mass. One of the great Catholic cathedrals of the West."},
            {"name": "Last Chance Gulch",          "details": "The original gold rush main street, now a walking mall"},
            {"name": "Montana State Capitol",      "details": "1301 6th Ave — tours available, art-filled interior"},
            {"name": "Gates of the Mountains",     "details": "30 min north — Missouri River canyon Lewis & Clark named in 1805"},
            {"name": "Garnet Ghost Town",          "details": "1 hr east on BLM land — 1870s gold mining ghost town"},
        ],
        "history": (
            "Gold discovered in Last Chance Gulch in 1864 — four prospectors' final attempt before "
            "giving up hit the richest placer deposit in Montana history. "
            "By 1888 Helena had more millionaires per capita than any other city in the United States. "
            "The Cathedral of Saint Helena was funded by these fortunes — construction 1908, first Mass 1914, "
            "modeled on the Votive Church in Vienna."
        ),
        "dogs": "Helena city parks — dogs on leash. Cathedral grounds — dogs on leash. Garnet Ghost Town BLM — dogs fully welcome.",
        "resupply_note": "Resupply in Helena for Days 22-25: chicken, pork chops, apples, Brussels sprouts, green beans, blueberries (Day 27 muffins), maple syrup, butter, eggs, bacon, naan.",
    },

    "Thermopolis": {
        "gps":    (43.647, -108.212),
        "type":   "camp",
        "state":  "WY",
        "crowd":  {"weekday": 2, "weekend": 4},
        "drive_from_prev": {"from": "Helena", "miles": 350, "hours": 5.5, "route": "I-15 S → US-287 → US-26 → WY-789 → US-20"},
        "camping": [
            {"name": "Boysen State Park", "type": "State Park",
             "notes": "17 mi south of Thermopolis. Reservoir camping, some hookups. Dogs on leash. wyoparks.wyo.gov."},
            {"name": "Shoshone NF dispersed near Dubois", "type": "NF free",
             "notes": "First national forest in America, established 1891. Near Dubois on the approach to Thermopolis."},
        ],
        "restaurants": [
            {"name": "Thermopolis Brewing Company", "address": "116 S 6th St, Thermopolis", "notes": "Craft beer, good food"},
            {"name": "Hot Springs County Museum café","address": "700 Broadway, Thermopolis", "notes": "Local institution"},
        ],
        "churches": [
            {"name": "Our Lady of the Mountains", "address": "420 Arapahoe St, Thermopolis",
             "notes": "Confirm schedule at masstime.us"},
        ],
        "bjj": [
            {"name": "None", "address": "—", "notes": "Remote Wyoming"},
        ],
        "arts": [
            {"name": "Wyoming Dinosaur Center", "details": "110 Carter Ranch Rd — one of the best dinosaur facilities in the country, on-site dig opportunities"},
            {"name": "Hot Springs County Museum","details": "700 Broadway — frontier history and dinosaur county context"},
        ],
        "poi": [
            {"name": "Hot Springs State Park — FREE bathhouse", "details": "104°F, Mon-Sat 8am-5:30pm, Sun noon-5:30pm. Both Kevin and Lisa soak. This is the genuine restorative stop."},
            {"name": "River Bend Bark Park",   "details": "Off-leash dog park adjacent to Hot Springs State Park entrance — Tango runs free"},
            {"name": "Wind River Canyon",      "details": "US-20 — 14 miles through a 2,400-ft deep canyon — one of Wyoming's great drives"},
            {"name": "Wyoming Dinosaur Center","details": "On-site dig opportunities, extraordinary collection"},
        ],
        "history": (
            "Thermopolis was ceded by the Shoshone and Arapaho tribes in 1896 with a specific legal "
            "stipulation: the hot springs must remain free to the public forever. Wyoming honors this "
            "treaty provision in the Hot Springs State Park free bathhouse today. "
            "Wind River Canyon cuts through 2.7 billion year old Precambrian granite — "
            "among the oldest exposed rock in North America."
        ),
        "dogs": "River Bend Bark Park — off-leash. Hot Springs State Park — dogs on leash. Boysen SP — dogs on leash. Shoshone NF — dogs on leash, all trails.",
    },

    "Bighorns": {
        "gps":    (44.500, -107.300),
        "type":   "camp",
        "state":  "WY",
        "crowd":  {"weekday": 2, "weekend": 3},
        "drive_from_prev": {"from": "Thermopolis", "miles": 120, "hours": 2.5, "route": "US-16 (Ten Sleep Canyon)"},
        "camping": [
            {"name": "Bighorn NF dispersed off US-16 or Route 20", "type": "NF free",
             "notes": "Free, established clearings, some alongside streams. 7,000-9,500 ft elevation. Dogs on leash."},
            {"name": "Shell Creek Campground", "type": "NF developed",
             "notes": "Near Shell Falls. recreation.gov."},
            {"name": "Sibley Lake Campground", "type": "NF developed",
             "notes": "Rare hookup-equipped NF campground. recreation.gov."},
        ],
        "restaurants": [
            {"name": "Ten Sleep Brewing", "address": "3 Craft Ln, Ten Sleep WY", "notes": "Excellent craft beer, dog-friendly patio in a beautiful canyon setting"},
            {"name": "Cowboy Bar, Ten Sleep","address": "Main St, Ten Sleep WY", "notes": "Local institution"},
        ],
        "churches": [
            {"name": "None on the plateau", "address": "—", "notes": "Nearest: Worland WY (~40 mi south) or Sheridan (~70 mi north)"},
        ],
        "bjj": [
            {"name": "None", "address": "—", "notes": "Remote"},
        ],
        "arts": [
            {"name": "Ten Sleep arts community", "details": "Small but real — galleries on the main street worth a look"},
        ],
        "poi": [
            {"name": "Ten Sleep Canyon",                  "details": "US-16 — canyon walls close to vertical before climbing to open highland"},
            {"name": "Shell Falls",                       "details": "US-14, right off the road — 3,600 gallons per second over 120 feet"},
            {"name": "Medicine Wheel National Historic Landmark", "details": "9,642 ft — sacred Native American site, short flat walk from parking"},
            {"name": "Cloud Peak Wilderness viewpoints",  "details": "Multiple overlooks accessible from Bighorn NF trails"},
        ],
        "history": (
            "Medicine Wheel is a 600-year-old stone structure of unknown origin at 9,642 feet. "
            "Its 28 spokes align with astronomical events including the summer solstice sunrise. "
            "Still used in ceremonies by Crow, Shoshone, and Arapaho peoples. "
            "The Bozeman Trail cut through the Bighorns in the 1860s, triggering Red Cloud's War — "
            "one of the few armed conflicts the US government definitively lost."
        ),
        "dogs": "Bighorn NF — dogs on leash on 1,200 miles of trails, no restrictions. Ten Sleep Canyon — dogs in van. Medicine Wheel — dogs on leash at parking area.",
        "van_routing_note": (
            "US-14A (Medicine Wheel Passage) has extreme hairpin turns — not recommended for large vehicles. "
            "Take US-14 through Shell Canyon instead. Equally spectacular, van-appropriate."
        ),
    },

    "Cody": {
        "gps":    (44.526, -109.057),
        "type":   "hotel",
        "state":  "WY",
        "crowd":  {"weekday": 3, "weekend": 5},
        "drive_from_prev": {"from": "Bighorns", "miles": 90, "hours": 3.0, "route": "US-14 or US-14A"},
        "restaurants": [
            {"name": "Irma Hotel Restaurant",       "address": "1192 Sheridan Ave, Cody", "notes": "Founded by Buffalo Bill 1902, cherrywood bar gifted by Queen Victoria"},
            {"name": "Wyoming's Rib and Chop House","address": "1367 Sheridan Ave, Cody", "notes": "Local steaks"},
        ],
        "churches": [
            {"name": "Sacred Heart Catholic", "address": "1430 Beck Ave, Cody",
             "notes": "Confirm schedule before arrival"},
        ],
        "bjj": [
            {"name": "None confirmed", "address": "—", "notes": "Remote"},
        ],
        "arts": [
            {"name": "Whitney Western Art Museum",  "details": "Inside Buffalo Bill Center — Remington, Russell, finest Western American art collection. Budget 2 hours."},
            {"name": "Buffalo Bill Center of the West", "details": "720 Sheridan Ave — 5 museums in one building, plan 4-5 hours"},
            {"name": "Cody Nite Rodeo",              "details": "519 W Yellowstone Ave — every night June-August, 8pm, ~$25. World's longest-running nightly rodeo."},
            {"name": "Cody Country Art League",      "details": "836 Sheridan Ave — local and regional artists"},
        ],
        "poi": [
            {"name": "Buffalo Bill Center of the West", "details": "5 museums — Buffalo Bill, Whitney Western Art, Draper Natural History, Plains Indian, Cody Firearms"},
            {"name": "Cody Nite Rodeo",                "details": "World's longest-running nightly rodeo — every night June-August"},
            {"name": "Heart Mountain Interpretive Center", "details": "1539 Heart Mountain Rd — Japanese American internment story, beautifully and honestly told"},
        ],
        "history": (
            "William F. 'Buffalo Bill' Cody founded the town in 1896. "
            "His Wild West shows introduced the concept of the 'American West' to the world. "
            "Heart Mountain Relocation Center interned 10,767 Japanese Americans from 1942-1945. "
            "Evacuees had an average of 6 days to liquidate their property before reporting."
        ),
        "dogs": "Buffalo Bill Center grounds — dogs on leash. Heart Mountain grounds — dogs on leash. Cody Nite Rodeo — dogs NOT in arena. Van with AC.",
        "lodging": [
            {"name": "Chamberlin Inn", "address": "1032 12th St, Cody WY", "pet_friendly": True, "notes": "Boutique, historic, pet-friendly"},
        ],
        "resupply_note": "Final resupply in Cody for Days 26-28: eggs, bacon, naan, blueberries, almonds, pears, cheese, tortillas.",
    },

    "Medicine Bow": {
        "gps":    (41.900, -106.200),
        "type":   "camp",
        "state":  "WY",
        "crowd":  {"weekday": 2, "weekend": 3},
        "drive_from_prev": {"from": "Cody", "miles": 250, "hours": 5.0, "route": "WY-120 → I-25 S → WY-130"},
        "camping": [
            {"name": "Medicine Bow NF dispersed, Snowy Range", "type": "NF free",
             "notes": "Above treeline at 10,000+ ft. Dogs on leash. Free. Last camp of the trip."},
            {"name": "Brooklyn Lake or Lewis Lake",             "type": "NF developed",
             "notes": "Developed campgrounds with some hookups. recreation.gov."},
            {"name": "Vedauwoo Recreation Area",               "type": "NF reservation",
             "notes": "Exit 329 off I-80. 1.4 billion year old granite hoodoos. reservation-based. recreation.gov."},
        ],
        "restaurants": [
            {"name": "Library Restaurant and Brewing", "address": "116 E Grand Ave, Laramie", "notes": "Best food in Laramie"},
            {"name": "The Alibi Bar and Frame",         "address": "Laramie WY",               "notes": "Historic bar, local institution"},
        ],
        "churches": [
            {"name": "St. Laurence O'Toole", "address": "1026 Steele St, Laramie WY",
             "notes": "Confirm schedule at masstime.us"},
        ],
        "bjj": [
            {"name": "UW clubs / check graciebarra.com", "address": "Laramie WY",
             "notes": "University of Wyoming — programs may have open mat sessions"},
        ],
        "arts": [
            {"name": "University of Wyoming Art Museum", "details": "2111 Willett Dr, Laramie — free, strong permanent collection"},
            {"name": "Vedauwoo rock formations",         "details": "Natural sculpture environment unlike anywhere in the US"},
        ],
        "poi": [
            {"name": "Vedauwoo Recreation Area",          "details": "Exit 329 off I-80 — 1.4 billion year old Sherman Granite hoodoos, climbing, dispersed camping"},
            {"name": "Snowy Range Scenic Byway (WY-130)","details": "29-mile alpine byway above treeline — typically open July-October"},
            {"name": "Wyoming Territorial Prison",        "details": "Laramie — where Butch Cassidy was imprisoned"},
        ],
        "history": (
            "Vedauwoo is an Arapaho word meaning 'earth born spirits' — the formations were sacred. "
            "The Sherman Granite is 1.4 billion years old. "
            "Medicine Bow-Routt National Forest was established in 1902 by Theodore Roosevelt — "
            "one of the first national forests under his administration."
        ),
        "dogs": "Medicine Bow NF — dogs on leash, all trails. Vedauwoo — dogs welcome at dispersed sites.",
    },

    "Oklahoma": {
        "gps":    (35.467, -97.517),
        "type":   "hotel_then_home",
        "state":  "OK",
        "crowd":  {"weekday": 2, "weekend": 3},
        "drive_from_prev": {"from": "Medicine Bow", "miles": 850, "hours": 12.0, "route": "I-25 S → I-40 or I-35 S"},
        "restaurants": [
            {"name": "Cattlemen's Steakhouse", "address": "1309 S Agnew Ave, OKC", "notes": "Open since 1910, breakfast until 2pm, most authentic western steakhouse in America"},
            {"name": "Tucker's Onion Burgers", "address": "Multiple OKC locations",  "notes": "Oklahoma's signature dish — the onion burger"},
        ],
        "churches": [
            {"name": "Holy Family Cathedral", "address": "8 W 5th St, Tulsa",      "notes": "Diocese cathedral if routing through Tulsa"},
            {"name": "Our Lady's Cathedral",   "address": "307 NW 4th St, OKC",    "notes": "Diocese cathedral in Oklahoma City"},
        ],
        "bjj": [
            {"name": "Gracie JJ Tulsa",          "address": "2911 E 91st St, Tulsa", "notes": "gracietulsa.com — Gracie Academy Certified. If routing through Tulsa."},
            {"name": "Lovato's School of BJJ",   "address": "4322 NW 39th St, OKC", "notes": "Rafael Lovato Jr. — world-class, not GB brand"},
        ],
        "arts": [
            {"name": "OKC National Memorial", "details": "620 N Harvey Ave — one of the most powerful memorials in America, dogs on grounds outside"},
            {"name": "Woody Guthrie Center",   "details": "102 E Reconciliation Way, Tulsa — if routing through"},
        ],
        "poi": [
            {"name": "Tallgrass Prairie National Preserve", "details": "K-177 near Strong City KS — bison visible from the road, free, last intact tallgrass prairie"},
            {"name": "OKC National Memorial",               "details": "168 empty chairs, reflecting pool, Survivor Tree — essential visit"},
            {"name": "Turner Falls",                        "details": "US-77 near Davis OK — 77-ft waterfall, dogs on trails, last road lunch"},
        ],
        "history": (
            "The Oklahoma Land Run on April 22, 1889 founded Oklahoma City in a single afternoon — "
            "50,000 settlers raced simultaneously for 2 million acres. "
            "The OKC bombing on April 19, 1995 killed 168 people — the deadliest domestic terrorism "
            "in US history until 9/11. "
            "Oklahoma was Indian Territory — the forced removal of the Five Civilized Tribes "
            "in the 1830s-40s is the Trail of Tears."
        ),
        "dogs": "Tallgrass Prairie — dogs in parking areas. OKC Memorial grounds — dogs on leash. Turner Falls — dogs on trails on leash.",
    },
}
