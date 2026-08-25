"""
trip/data/meals.py
Complete 28-day meal plan for the 2027 Glacier NP road trip.

Rules:
- Hotel nights: breakfast provided, dinner out — zero cooking.
- Camp nights: full three meals on Coleman / cast iron / Instant Pot / Dutch oven.
- Lisa's favorites marked with star=True — distributed as surprises.

Cooking gear: Coleman 2-burner, cast iron skillet, cast iron waffle iron,
Dutch oven, Instant Pot Mini 3qt, Jetboil (backup).
"""

# ── LISA'S FAVORITES ─────────────────────────────────────────────────────────

LISAS_FAVORITES = [
    "Scrambled eggs with bacon and naan",
    "Crepes",
    "Hotdogs with relish",
    "Blueberry muffins",
    "Baked chicken shawarma with yellow rice and garbanzo beans",
    "Waffles with whipped butter and maple syrup",
    "Beef tenderloin",
    "Fried rice with pineapple and chicken",
    "Fresh Dutch oven bread",
    "Black bean soup",
]

# ── COOKING METHODS ───────────────────────────────────────────────────────────

COOKING_METHODS = [
    {
        "method": "Coleman 2-burner",
        "best_for": "Eggs, bacon, crepes, hotdogs, waffles, steak, stir fry",
        "notes": "Primary cooking. Works under any fire restriction.",
    },
    {
        "method": "Cast iron skillet",
        "best_for": "Eggs, bacon, steak, pork chops, crepes, fried rice, vegetables",
        "notes": "Ripping hot for searing and fried rice. Core tool.",
    },
    {
        "method": "Cast iron waffle iron",
        "best_for": "Waffles",
        "notes": "Lodge stovetop model on Coleman. Preheat 3 min per side. Butter generously between each waffle. Buy before departure (~$35).",
    },
    {
        "method": "Dutch oven",
        "best_for": "Baked chicken shawarma, blueberry muffins, fresh bread",
        "notes": "Parchment liner. Low flame under, foil or coals on lid for top heat. 20-35 min depending on recipe.",
    },
    {
        "method": "Instant Pot Mini 3qt",
        "best_for": "Spaghetti, black bean soup, rice, chicken",
        "notes": "Pressure cook pasta 8 min. Soup 15 min. One-pot camp meals.",
    },
    {
        "method": "No-knead bread (Dutch oven)",
        "best_for": "Fresh Dutch oven bread",
        "notes": "Mix flour + water + yeast + salt the night before (5 min). Rise 8-12 hrs. Bake in Dutch oven 35 min. Extraordinary results.",
    },
]

# ── RESUPPLY SCHEDULE ─────────────────────────────────────────────────────────

RESUPPLY = [
    {
        "stop": "Home (pre-trip)",
        "day": 0,
        "covers": "Pre-trip prep",
        "items": (
            "Freeze ground beef, chicken thighs, pork portions flat in Dometic. "
            "Pre-mix 3 blueberry muffin dry-ingredient bags (labeled #1, #2, #3). "
            "Pre-mix shawarma spice blend (cumin, turmeric, coriander, paprika, garlic powder, cinnamon, black pepper). "
            "Pre-mix taco seasoning. Pre-mix black bean soup seasoning. "
            "Buy Lodge cast iron stovetop waffle iron (~$35). "
            "Buy 2 cans whipped cream. Buy real maple syrup. Buy parchment paper."
        ),
    },
    {
        "stop": "Sioux Falls, SD",
        "day": 2,
        "covers": "Days 3-6",
        "items": (
            "Eggs (farm/unwashed if possible — no refrigeration needed), bacon, naan, "
            "strawberries, blueberries, peaches, grapes, carrots, celery, "
            "chicken thighs (for shawarma Day 6), ground beef, garbanzo beans (canned x2), "
            "yellow rice, sausage (for black bean soup), tortillas, bread"
        ),
    },
    {
        "stop": "Rapid City, SD",
        "day": 4,
        "covers": "Days 5-8",
        "items": (
            "Apples, pears, cabbage, onions, Brussels sprouts, plums, "
            "chicken (for Day 6 shawarma if not bought in Sioux Falls), "
            "blueberries (for muffins Day 7), canned beans x2, pasta, jarred sauce x2, "
            "ground beef (tacos Day 7), tortillas, naan"
        ),
    },
    {
        "stop": "Dickinson or Medora, ND",
        "day": 8,
        "covers": "Days 9-13 (remote stretch)",
        "critical": True,
        "items": (
            "STOCK UP FOR REMOTE STRETCH. "
            "Extra shelf-stable: canned black beans x4, garbanzo beans x2, rice, pasta x2, jarred sauce x2, tuna x4. "
            "Fresh: carrots, cabbage, apples, pears, onions, celery. "
            "Eggs, chicken thighs, ground beef, pork sausage, bacon, naan, tortillas, bread"
        ),
    },
    {
        "stop": "Fort Benton or Great Falls, MT",
        "day": 13,
        "covers": "Days 14-17",
        "critical": True,
        "items": (
            "FULL STOCK BEFORE GLACIER. "
            "Beef tenderloin (buy and freeze immediately — this is the Day 18 anniversary dinner). "
            "Blueberries (muffins Day 17), strawberries, whipped cream x2, maple syrup. "
            "Bacon, eggs, butter, all proteins. Flour and yeast for no-knead bread. "
            "Beer from local brewery."
        ),
    },
    {
        "stop": "Columbia Falls or Whitefish, MT",
        "day": 15,
        "covers": "Days 15-20 (Glacier week)",
        "notes": "Best grocery town on the entire trip.",
        "items": (
            "Top up all Glacier week supplies. Confirm beef tenderloin is frozen. "
            "Fresh fruit for the week. Blueberries for Day 17 muffins. "
            "Maple syrup, whipped cream. Anything needed for the Day 18 anniversary dinner."
        ),
    },
    {
        "stop": "Helena, MT",
        "day": 21,
        "covers": "Days 22-25",
        "items": (
            "Chicken thighs (shawarma Day 22), pork chops, apples (for pork Day 24), "
            "Brussels sprouts, green beans, blueberries (final muffins Day 27), "
            "maple syrup, butter, eggs, bacon, naan, tortillas"
        ),
    },
    {
        "stop": "Cody, WY",
        "day": 25,
        "covers": "Days 26-28 (final stretch)",
        "items": (
            "Keep it light — going home. "
            "Eggs, bacon, naan, blueberries, almonds, apples, pears, cheese, tortillas, bread"
        ),
    },
]

# ── PANTRY — ALWAYS IN THE VAN ────────────────────────────────────────────────

PANTRY = [
    {"category": "Oils and fats",        "items": "Butter (Dometic fridge), olive oil, vegetable oil"},
    {"category": "Dry staples",           "items": "Rice, pasta, oats, flour, yeast, salt, sugar, baking powder"},
    {"category": "Canned goods",          "items": "Black beans x4, garbanzo beans x4, diced tomatoes x2, jarred pasta sauce x2"},
    {"category": "Sauces and condiments", "items": "Soy sauce, hot sauce, mustard, relish, maple syrup, honey, peanut butter"},
    {"category": "Spice blends",          "items": "Shawarma blend, taco seasoning, black bean soup seasoning, garlic powder, cumin, salt, pepper"},
    {"category": "Snacks",                "items": "Almonds, peanuts, protein bars, chocolate, dried fruit"},
    {"category": "Baking",                "items": "Pre-mixed muffin dry bags x3, parchment paper, whipped cream cans x2"},
    {"category": "Drinks",                "items": "Coffee grounds, tea, electrolyte packets, hot cocoa packets"},
    {"category": "Emergency meals",       "items": "Instant oats x6, ramen x4, tuna packets x4, peanut butter crackers"},
]

# ── PRODUCE LONGEVITY ─────────────────────────────────────────────────────────

PRODUCE_GUIDE = [
    {
        "days": "Days 1-3",
        "items": "Strawberries, blueberries, ripe bananas, peaches, fresh bread, broccoli",
        "storage": "Dometic fridge for berries. Eat first.",
    },
    {
        "days": "Days 1-5",
        "items": "Grapes, plums, tomatoes, green beans, fresh naan",
        "storage": "Fridge or cool spot. Buy and use early in each resupply cycle.",
    },
    {
        "days": "Days 1-7",
        "items": "Apples, pears, carrots, celery, cucumber, green beans",
        "storage": "Room temp fine. Fridge extends to 10 days.",
    },
    {
        "days": "10+ days",
        "items": "Cabbage, onions, Brussels sprouts, unwashed farm eggs, butter, hard cheese",
        "storage": "Room temp. Unwashed eggs need no refrigeration — buy from farm stands.",
    },
    {
        "days": "Indefinite",
        "items": "Almonds, peanuts, dried fruit, all canned goods",
        "storage": "Pantry stable. Always in the van.",
    },
]

# ── 28-DAY MEAL PLAN ─────────────────────────────────────────────────────────
# Each entry keyed by day number (1-28).
# hotel=True means: breakfast provided, dinner out, no cooking.
# surprise: shown in gold if present — it's a Lisa favorite moment.

MEALS = {
    1: {
        "hotel": True,
        "lunch": "Wraps from home, fruit, almonds in the van",
        "notes": "Eat at home before departure.",
    },
    2: {
        "hotel": True,
        "lunch": "Deli stop en route — local sandwich shop",
        "notes": "Resupply in Sioux Falls tonight for Days 3-6.",
    },
    3: {
        "hotel": False,
        "breakfast": "Scrambled eggs with bacon and naan ★ — Coleman at hotel before checkout",
        "lunch": "Wall Drug stop (15 min). Carrots, almonds, peaches in the van.",
        "dinner": "Hotdogs with relish ★ — first campfire at Sage Creek. Strawberries for dessert.",
        "surprise": "Eggs + bacon + naan before the drive, hotdogs at the first campfire — two favorites in one day.",
    },
    4: {
        "hotel": True,
        "lunch": "Fried rice with pineapple and chicken — Instant Pot at the hotel or Coleman outside",
        "notes": "Hotel reset — July 4th weekend Badlands. Resupply in Rapid City.",
    },
    5: {
        "hotel": False,
        "breakfast": "Crepes ★ — cast iron on Coleman at the hotel before checkout. Butter, maple syrup, fresh grapes.",
        "lunch": "Apples, almonds, cheese and bread while exploring the Wildlife Loop Road",
        "dinner": "Black bean soup — Instant Pot (canned black beans, sausage, onion, cumin, lime). Crusty naan on the side.",
        "surprise": "Crepes breakfast — first surprise of the trip. Set up the Coleman while she sleeps.",
    },
    6: {
        "hotel": False,
        "breakfast": "Eggs any style, bacon, toast on cast iron. Coffee.",
        "lunch": "Cabbage wraps with leftover chicken, mustard",
        "dinner": "Baked chicken shawarma with yellow rice and garbanzo beans ★ — Dutch oven on Coleman. 45 min, one pot.",
        "surprise": "Baked chicken shawarma — the smell announces it. She will not believe this came from a camp stove.",
    },
    7: {
        "hotel": False,
        "breakfast": "Blueberry muffins ★ — Dutch oven, pre-mixed bag #1. Bake while she walks the dogs.",
        "lunch": "Hotdogs with relish ★ at a scenic overlook — Needles Highway or Sylvan Lake.",
        "dinner": "Ground beef tacos with fresh tomato, onion. Roasted Brussels sprouts in cast iron.",
        "surprise": "Blueberry muffins at breakfast — she returns from walking the dogs to find hot muffins waiting.",
    },
    8: {
        "hotel": True,
        "lunch": "Banana, peanuts, coffee in the van. Enchanted Highway detour — add 45 min.",
        "notes": "Resupply in Dickinson or Medora for Days 9-13. Critical remote stretch stock-up.",
    },
    9: {
        "hotel": False,
        "breakfast": "Scrambled eggs with bacon and naan ★ — Coleman at Cottonwood Campground. Morning light on the Little Missouri River.",
        "lunch": "Carrots, celery, pears, almonds — graze while exploring the South Unit loop",
        "dinner": "Spaghetti with meat sauce — Instant Pot. Sauté ground beef, add jarred sauce and pasta, pressure cook 8 min.",
        "surprise": "Eggs + bacon + naan at the Little Missouri River.",
    },
    10: {
        "hotel": False,
        "breakfast": "Oats with banana and peanut butter, coffee",
        "lunch": "PB and honey on naan, apple slices, almonds",
        "dinner": "Fried rice with pineapple and chicken ★ — cast iron on Coleman. Get the pan ripping hot.",
    },
    11: {
        "hotel": False,
        "breakfast": "Bacon, egg, cheese wrap in tortilla — eat in the van while driving",
        "lunch": "Leftover spaghetti cold from the fridge. Pear, almonds.",
        "dinner": "Cast iron steak — whatever cut Miles City grocery has. Butter, garlic, green beans in same pan. Stars over the Yellowstone.",
        "notes": "Stock up at IGA in Miles City before heading northwest.",
    },
    12: {
        "hotel": False,
        "breakfast": "Eggs and onion scramble, toast, coffee — eat before the long drive into the Breaks",
        "lunch": "Wraps with leftover steak slices, cabbage, mustard",
        "dinner": "Black bean soup — Instant Pot. Naan warmed in cast iron. The Missouri River 10 feet from camp.",
    },
    13: {
        "hotel": False,
        "breakfast": "Oats at camp — fast, breaking down early",
        "lunch": "Grand Union Hotel in Fort Benton — eat here. 1882 hotel on the levee. Do not skip.",
        "dinner": "Baked chicken shawarma with yellow rice and garbanzo beans ★ — Dutch oven at Choteau BLM. Rocky Mountain Front at sunset.",
        "surprise": "Shawarma at the base of the Rocky Mountain Front. Second appearance.",
        "notes": "Resupply in Fort Benton or Great Falls. Buy beef tenderloin and freeze immediately.",
    },
    14: {
        "hotel": False,
        "breakfast": "Crepes ★ — cast iron, celebrate Glacier arrival and family reunion. Butter, maple syrup, grapes, whipped cream.",
        "lunch": "Light — cheese, bread, fruit while setting up camp and doing the Columbia Falls grocery run",
        "dinner": "Hotdogs with relish ★ — Glacier Night 1 with family. Beer from Columbia Falls.",
        "surprise": "Crepes to celebrate arrival and the family reunion. Hotdogs at the first Glacier campfire.",
    },
    15: {
        "hotel": False,
        "breakfast": "Scrambled eggs with bacon and naan ★ — cast iron at base camp. Morning light on Montana mountains.",
        "lunch": "Pack out to Lake McDonald: apples, almonds, cheese, bread, carrots",
        "dinner": "Hotdogs with relish ★ — casual camp night with family.",
        "surprise": "Eggs + bacon + naan at Glacier base camp.",
    },
    16: {
        "hotel": False,
        "breakfast": "Waffles with whipped butter and maple syrup ★ — cast iron waffle iron on Coleman. Get up early, have it hot before she wakes. Fresh strawberries on the side.",
        "lunch": "Pack out for the hike — PB tortillas, peaches, almonds, chocolate",
        "dinner": "Ground beef tacos with fresh tomato, onion, avocado",
        "surprise": "Cast iron waffles — she wakes up to the smell of waffles at Glacier National Park.",
    },
    17: {
        "hotel": False,
        "breakfast": "Blueberry muffins ★ — Dutch oven, pre-mixed bag #2. Third surprise breakfast of the trip.",
        "lunch": "East Glacier deli or packed wraps and fruit",
        "dinner": "Spaghetti with meat sauce — Instant Pot. Easy after a long day.",
        "surprise": "Blueberry muffins — third surprise breakfast.",
    },
    18: {
        "hotel": False,
        "breakfast": "Oats, banana, coffee — easy morning",
        "lunch": "Apgar Village café or picnic at the lake",
        "dinner": "BEEF TENDERLOIN ★★★ — The anniversary dinner. Salt 1 hr before. Screaming hot cast iron, butter, garlic, rosemary. Sear all sides. Rest 10 min. Slice. Brussels sprouts and onion in same pan. Fresh Dutch oven bread (start dough last night). Two candles.",
        "surprise": "THE anniversary dinner. Beef tenderloin, fresh bread, candles at Glacier. This is the moment.",
        "notes": "Start no-knead bread dough on Day 17 evening — 5 min of work, rise overnight.",
    },
    19: {
        "hotel": False,
        "breakfast": "Scrambled eggs with bacon and naan ★ — recovery breakfast after the anniversary dinner",
        "lunch": "Flathead Lake picnic — peaches, grapes, cheese, bread, almonds",
        "dinner": "Fried rice with pineapple and pork — cast iron.",
        "surprise": "Eggs + bacon + naan — recovery morning after the anniversary dinner.",
    },
    20: {
        "hotel": False,
        "breakfast": "Banana, almonds, coffee — pre-dawn, eat fast, get to the shuttle by 6am",
        "lunch": "Pack out for Logan Pass — wraps, apples, almonds, chocolate, extra water",
        "dinner": "Crepes ★ — the GTSR victory dinner. Sweet crepes with whipped cream and fresh fruit. Third appearance.",
        "surprise": "Crepes for the GTSR victory dinner. The best day of the trip deserves a celebration.",
    },
    21: {
        "hotel": True,
        "lunch": "Gates of the Mountains area or scenic pullout — wraps, last of the Glacier groceries",
        "notes": "Resupply in Helena for Days 22-25.",
    },
    22: {
        "hotel": False,
        "breakfast": "Hotel provided",
        "lunch": "Drive day — wraps, pears, almonds, cheese in the van",
        "dinner": "Baked chicken shawarma with yellow rice and garbanzo beans ★ — Dutch oven at Shoshone NF camp. Wind River Range behind you. Fourth and final appearance.",
        "surprise": "Shawarma one more time at the Wind River Range — final appearance.",
    },
    23: {
        "hotel": False,
        "breakfast": "Oats at camp before the canyon drive",
        "lunch": "Eat in Thermopolis after the hot springs — Thermopolis Brewing or local diner",
        "dinner": "Black bean soup with fresh Dutch oven bread ★ — no-knead loaf started this morning. Bake at Boysen Reservoir camp.",
        "surprise": "Fresh Dutch oven bread at the reservoir camp. The smell is the announcement.",
        "notes": "Start no-knead bread dough before leaving camp in the morning — rise during the drive.",
    },
    24: {
        "hotel": False,
        "breakfast": "Scrambled eggs with bacon and naan ★ — Ten Sleep Canyon drive deserves a great start",
        "lunch": "Ten Sleep Brewing — eat in town, dog-friendly patio",
        "dinner": "Pork chops in cast iron with apples and onions. Green beans on the side. Camp at 8,000+ feet.",
        "surprise": "Eggs + bacon + naan before Ten Sleep Canyon.",
    },
    25: {
        "hotel": True,
        "lunch": "En route snack or stop in Ten Sleep or Greybull",
        "notes": "Irma Hotel restaurant for dinner — Buffalo Bill's, 1902, Queen Victoria's cherrywood bar. Order the steak. Resupply in Cody for Days 26-28.",
    },
    26: {
        "hotel": False,
        "breakfast": "Hotel provided",
        "lunch": "Drive day — almonds, pears, cheese, bread in the van",
        "dinner": "Hotdogs with relish ★ — final campfire of the trip at 10,000 feet in the Medicine Bow. Stars above the treeline.",
        "surprise": "Hotdogs at the final campfire. She'll know what this means by now.",
    },
    27: {
        "hotel": False,
        "breakfast": "Blueberry muffins ★ — Dutch oven at the Snowy Range camp before breaking down. Final muffin of the trip. Coffee. Alpine view. This is the goodbye breakfast.",
        "lunch": "Stop in Fort Collins CO or Pueblo CO, or drive-through if pushing hard",
        "dinner": "Dinner out in Oklahoma or Kansas — Cattlemen's Steakhouse OKC (open since 1910) if routing through",
        "surprise": "Final blueberry muffins at the Snowy Range. The goodbye breakfast.",
    },
    28: {
        "hotel": True,
        "lunch": "Turner Falls — 77-ft waterfall in the Arbuckle Mountains OK. Dogs on trails on leash. Last road lunch.",
        "dinner": "Home. Let Lisa cook whatever she wants in a real kitchen. Or order pizza. 28 days. You earned it.",
        "notes": "Home by evening.",
    },
}

# ── LISA'S FAVORITES SCHEDULE ─────────────────────────────────────────────────

FAVORITES_SCHEDULE = [
    {"meal": "Scrambled eggs + bacon + naan", "days": [3, 9, 15, 19, 24],
     "occasion": "Camp mornings — rotating surprise"},
    {"meal": "Crepes",                        "days": [5, 14, 20],
     "occasion": "Day 5: first surprise · Day 14: Glacier arrival · Day 20: GTSR victory dinner"},
    {"meal": "Hotdogs with relish",           "days": [3, 7, 14, 26],
     "occasion": "First camp · Black Hills · Glacier arrival · final campfire"},
    {"meal": "Blueberry muffins",             "days": [7, 17, 27],
     "occasion": "Black Hills · Many Glacier morning · final goodbye breakfast at Snowy Range"},
    {"meal": "Baked chicken shawarma",        "days": [6, 13, 22],
     "occasion": "Black Hills · Rocky Mountain Front · Wind River Range"},
    {"meal": "Waffles",                       "days": [16],
     "occasion": "Glacier dog hiking day — the cast iron waffle iron surprise"},
    {"meal": "Beef tenderloin",               "days": [18],
     "occasion": "The Glacier anniversary dinner — candles, fresh bread, the moment"},
    {"meal": "Fried rice with pineapple",     "days": [10, 19],
     "occasion": "TRNP and Glacier — cast iron, always excellent"},
    {"meal": "Fresh Dutch oven bread",        "days": [18, 23],
     "occasion": "Glacier anniversary · Boysen Reservoir camp"},
    {"meal": "Black bean soup",               "days": [5, 12, 23],
     "occasion": "Black Hills · Missouri River camp · Thermopolis"},
]
