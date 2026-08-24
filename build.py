"""
build.py
Master build script — regenerates all PDFs from source data.

Usage:
    python build.py           # Build everything
    python build.py --van     # Van spec only
    python build.py --trip    # Trip reports only
"""

import sys
import os

# Ensure the repo root is on the Python path
sys.path.insert(0, os.path.dirname(__file__))

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def build_van():
    print("Building van spec PDF...")
    from van.generate_spec import build
    build(output_dir=OUTPUT_DIR)
    print("  ✓ Van_Build_Master_Spec.pdf")


def build_trip():
    print("Building trip report PDFs...")
    from trip.generate_reports import build
    build(output_dir=OUTPUT_DIR)
    print("  ✓ 2027_McAuley_Glacier_NP_Road_Trip_Plan_B.pdf")
    print("  ✓ 2027_McAuley_Road_Trip_Meal_Plan.pdf")
    print("  ✓ 2027_McAuley_Glacier_Trip_Companion.pdf")


def main():
    ensure_output_dir()
    args = sys.argv[1:]

    if "--van" in args:
        build_van()
    elif "--trip" in args:
        build_trip()
    else:
        build_van()
        build_trip()

    print("\nDone. PDFs written to outputs/")


if __name__ == "__main__":
    main()
