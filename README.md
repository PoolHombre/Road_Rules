# Road_Rules

Private repository — Kevin & Lisa McAuley

Two active projects, one repo:

- **Van** — GMC Savana 2500 expedition build specification, staged phases, electrical architecture, mechanical maintenance, exterior wrap
- **Trip** — 2027 Glacier NP road trip: routing, destinations, meals, faith, training, arts, history, camping, crowd optimization

---

## Structure

```
Road_Rules/
├── van/
│   ├── spec/         # Build stages, electrical, mechanical, systems, exterior
│   ├── data/         # Budget line items, vendor contacts
│   ├── changelog.py  # Every van build decision + reason
│   └── generate_spec.py
│
├── trip/
│   ├── data/         # Destinations, itinerary, meals, churches, gyms, arts, history, camping, routing
│   ├── rules/        # Route rules, crowd rules, dog access rules
│   ├── changelog.py  # Every trip decision + reason
│   └── generate_reports.py
│
├── shared/
│   ├── pdf_styles.py     # Carlito fonts, neutral palette, all styles
│   ├── pdf_components.py # Reusable PDF elements
│   └── utils.py          # Haversine, date math, crowd scoring model
│
└── build.py          # Regenerate all PDFs
```

## Requirements

```
pip install reportlab
```

Carlito font (metrically identical to Calibri) must be installed:
- Ubuntu/Debian: `sudo apt-get install fonts-crosextra-carlito`
- macOS: download from Google Fonts
- Windows: install from Google Fonts

## Usage

```bash
# Regenerate everything
python build.py

# Van spec only
python van/generate_spec.py

# Trip reports only
python trip/generate_reports.py
```

## Output

All PDFs written to `outputs/`.

---

*Built for a 2027 fifth anniversary trip. The van is the vehicle. The trip is the point.*
