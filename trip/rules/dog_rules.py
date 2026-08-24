"""
trip/rules/dog_rules.py
Dog access rules for Saki (ESA) and Tango (ADA service animal).

The ADA/ESA distinction is critical for trip planning and is respected
throughout all destination guidance.
"""

DOGS = {
    "Tango": {
        "breed":  "Husky",
        "status": "ADA service animal",
        "access": (
            "Full park trail access everywhere. ADA service animals are permitted "
            "in all areas open to the public including trails, lodges, shuttles, "
            "and below-the-rim areas at the Grand Canyon. "
            "No restrictions at any national park, national forest, or BLM land."
        ),
    },
    "Saki": {
        "breed":  "Schnauzer",
        "status": "ESA — Emotional Support Animal",
        "access": (
            "ESA status does NOT qualify as ADA at national parks. "
            "Saki is permitted in: roads, campgrounds, parking areas, and "
            "developed areas at NPS sites. "
            "Saki is NOT permitted on trails inside national parks. "
            "Saki has full access on all National Forest and BLM land on leash."
        ),
    },
}

# Access rules by land type
ACCESS_BY_LAND_TYPE = {
    "National Forest (NF)": {
        "Tango": "Full access on all trails on leash",
        "Saki":  "Full access on all trails on leash",
        "notes": "No restrictions. This is where both dogs get real trail access.",
    },
    "BLM Land": {
        "Tango": "Full access on all areas on leash",
        "Saki":  "Full access on all areas on leash",
        "notes": "No restrictions. Some areas allow off-leash in open terrain.",
    },
    "National Park": {
        "Tango": "Full access everywhere including trails and shuttles (ADA)",
        "Saki":  "Roads, campgrounds, parking areas, and developed areas ONLY",
        "notes": "Tango can hike all park trails. Saki stays in the van or developed areas.",
    },
    "State Park": {
        "Tango": "Full access on leash",
        "Saki":  "Most trails on leash — verify at each park",
        "notes": "State park rules vary. Generally more permissive than NPS for dogs.",
    },
}

# Stop-specific dog notes
STOP_SPECIFIC = {
    "Glacier": (
        "Inside the park: dogs on leash in developed areas, campgrounds, roads, and parking only. "
        "NOT on backcountry trails. "
        "Tango (ADA): full access everywhere including all trails. "
        "Saki: developed areas and the van with AC running. "
        "Flathead National Forest outside the park: both dogs on leash, all trails. "
        "Day 16 (Flathead NF hike) is specifically the dogs' best day of the entire trip."
    ),
    "Badlands": (
        "Dogs in campgrounds and parking areas on leash. NOT on trails. "
        "Tango (ADA): all trails. "
        "Saki: camp and parking areas. "
        "Sage Creek Campground: bison wander through at dawn — keep dogs in the van overnight."
    ),
    "Theodore Roosevelt": (
        "Dogs in campgrounds, parking areas, and roads on leash. NOT on park trails. "
        "Tango (ADA): all trails. "
        "Little Missouri National Grassland (adjacent, BLM): both dogs fully welcome, no restrictions."
    ),
    "Black Hills": (
        "Black Hills National Forest: dogs on leash on all 353 miles of trails. "
        "Custer State Park: dogs on leash in most areas including the Wildlife Loop Road. "
        "Sylvan Lake: dogs on leash at the shore. "
        "Jewel Cave NM: dogs in picnic area only — leave dogs in van with AC for cave tour."
    ),
    "Grand Tetons": (
        "Within Grand Teton NP: dogs restricted to roads, parking areas, and campgrounds. "
        "Tango (ADA): all trails. "
        "Bridger-Teton National Forest (surrounding the park): both dogs on leash, all trails — "
        "3.4 million acres of full dog access."
    ),
    "Hot Springs State Park": (
        "Dogs on leash on trails in the state park. "
        "River Bend Bark Park (off-leash) adjacent to the park entrance: Tango runs free. "
        "This is one of the few off-leash opportunities on the trip."
    ),
}

VAN_AC_PROTOCOL = (
    "When dogs are left in the van during trail time: "
    "the OutEquipPro Summit 2 AC must be running. "
    "The wired temperature sensor must be active with an alert set. "
    "Pre-cool the van before leaving the dogs. "
    "In July heat at low elevation, interior van temperature can reach dangerous levels "
    "within minutes without AC. This is the primary dog safety system on the trip."
)

HOT_SURFACE_PROTOCOL = (
    "Dog booties for Saki on hot surfaces: "
    "parking lots, paved areas in summer heat, sand at Bruneau Dunes. "
    "Musher's Secret wax on all paws before rocky terrain (Black Hills, Glacier approaches). "
    "Carry a collapsible water bowl — minimum 1 liter of dog water per active hour in summer heat."
)
