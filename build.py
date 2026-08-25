"""
build.py
Master build script — regenerates all PDFs from source data.

Usage:
    python build.py              # Build everything -> outputs/current/
    python build.py --van        # Van spec only
    python build.py --trip       # Trip reports only
    python build.py --archive    # Archive current, then rebuild
    python build.py --test       # Run tests before building
"""

import sys
import os
import shutil
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))

CURRENT_DIR = os.path.join(os.path.dirname(__file__), "outputs", "current")
ARCHIVE_DIR = os.path.join(os.path.dirname(__file__), "outputs", "archive")


def ensure_dirs():
    os.makedirs(CURRENT_DIR, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)


def archive_current():
    """Copy outputs/current/ to outputs/archive/YYYY-MM-DD/ before rebuilding."""
    pdfs = [f for f in os.listdir(CURRENT_DIR) if f.endswith(".pdf")]
    if not pdfs:
        print("  No current outputs to archive.")
        return
    archive_path = os.path.join(ARCHIVE_DIR, date.today().isoformat())
    os.makedirs(archive_path, exist_ok=True)
    for pdf in pdfs:
        shutil.copy2(os.path.join(CURRENT_DIR, pdf), archive_path)
    print(f"  Archived {len(pdfs)} PDFs to outputs/archive/{date.today().isoformat()}/")


def run_tests():
    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"],
        cwd=os.path.dirname(__file__)
    )
    if result.returncode != 0:
        print("\nTests failed — aborting build. Fix failures before generating PDFs.")
        sys.exit(1)
    print()


def build_van():
    print("Building van spec PDF...")
    from van.generate_spec import build
    build(output_dir=CURRENT_DIR)
    print("  ✓  Van_Build_Master_Spec.pdf")


def build_trip():
    print("Building trip PDFs...")
    from trip.generate_reports import build
    build(output_dir=CURRENT_DIR)


def main():
    ensure_dirs()
    args = sys.argv[1:]

    if "--test" in args:
        run_tests()

    if "--archive" in args:
        archive_current()

    if "--van" in args:
        build_van()
    elif "--trip" in args:
        build_trip()
    else:
        build_van()
        build_trip()

    print(f"\nOutputs written to outputs/current/")


if __name__ == "__main__":
    main()
