"""
shared/pdf_components.py
Reusable ReportLab flowable components for van spec and trip report PDFs.
All components use the neutral palette from pdf_styles.py.
"""

from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, PageBreak)
from .pdf_styles import (S, INK, MID, DIM, RULE, RULE2, BG, GOLD, WHITE,
                         TBL_H, TITLE, SUB, H2, H3, BODY, ITA, SMALL,
                         NOTE, WARN, STAR, TH, TB, LABEL, DETAIL)

W = 6.8 * inch  # usable page width with 0.85" margins


# ── PRIMITIVES ────────────────────────────────────────────────────────────────

def sp(n=6):
    return Spacer(1, n)


def hr(thickness=0.5):
    return HRFlowable(width=W, thickness=thickness, color=RULE,
                      spaceAfter=3, spaceBefore=3)


def hr2():
    return HRFlowable(width=W, thickness=1, color=INK,
                      spaceAfter=6, spaceBefore=6)


def p(text, style=BODY):
    return Paragraph(text, style)


# ── BOXES ─────────────────────────────────────────────────────────────────────

def note_box(text, kind="note"):
    """
    Styled information box.
    kind: 'note' (soft), 'warn' (bold), 'star' (gold/anniversary)
    """
    styles = {
        "note": (NOTE, colors.HexColor("#F7F7F7"), RULE),
        "warn": (WARN, colors.HexColor("#F7F7F7"), INK),
        "star": (STAR, colors.HexColor("#FDFAF3"), GOLD),
    }
    sty, bg, border = styles.get(kind, styles["note"])
    t = Table([[p(text, sty)]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), bg),
        ("BOX",           (0, 0), (-1, -1), 0.75, border),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 11),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 11),
    ]))
    return t


# ── TABLES ───────────────────────────────────────────────────────────────────

def simple_table(headers, rows, widths):
    """
    Standard two-tone table with dark header.
    headers: list of strings
    rows: list of tuples/lists
    widths: list of column widths in inches (or reportlab units)
    """
    data = [[p(h, TH) for h in headers]]
    for row in rows:
        data.append([p(str(c), TB) for c in row])
    t = Table(data, colWidths=widths)
    cmds = [
        ("BACKGROUND",    (0, 0), (-1,  0), TBL_H),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("BOX",           (0, 0), (-1, -1), 0.5, RULE),
        ("INNERGRID",     (0, 0), (-1, -1), 0.25, RULE2),
    ]
    for i in range(len(rows)):
        bg = BG if i % 2 == 0 else WHITE
        cmds.append(("BACKGROUND", (0, i + 1), (-1, i + 1), bg))
    t.setStyle(TableStyle(cmds))
    return t


def label_value_row(label, value):
    """Single label: value row with a light bottom rule. Used for summary tables."""
    t = Table(
        [[p(label, LABEL), p(value, DETAIL)]],
        colWidths=[1.4 * inch, W - 1.4 * inch],
    )
    t.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW",     (0, 0), (-1, -1), 0.25, RULE2),
    ]))
    return t


def label_value_block(pairs):
    """Render a list of (label, value) pairs as stacked rows."""
    return [label_value_row(label, val) for label, val in pairs]


def detail_row(icon, label, text):
    """Icon + label: value row used in day pages."""
    if isinstance(text, list):
        text = "\n".join([f"·  {item}" for item in text])
    t = Table(
        [[p(f"{icon}  {label}", S("DL", fontName="CB", fontSize=8, textColor=DIM, leading=11)),
          p(text, S("DV", fontSize=8.5, leading=13))]],
        colWidths=[1.1 * inch, W - 1.1 * inch],
    )
    t.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW",     (0, 0), (-1, -1), 0.25, RULE2),
    ]))
    return t


# ── PAGE HEADERS ──────────────────────────────────────────────────────────────

def section_break(title, subtitle=""):
    """Full-page section divider — returns a list of flowables."""
    items = [
        PageBreak(),
        sp(20),
        p(title, TITLE),
    ]
    if subtitle:
        items.append(p(subtitle, SUB))
    items += [sp(6), hr2(), sp(8)]
    return items


def day_header(day_num, date_str, location, drive, sleep_type):
    """Day page header bar — dark background with day number, location, drive, sleep type."""
    hdr = Table([[
        Table([
            [p(f"Day {day_num}", S("DN", fontName="CB", fontSize=11, textColor=WHITE, leading=14))],
            [p(date_str,         S("DD", fontName="CI", fontSize=9,  textColor=colors.HexColor("#AAAAAA"), leading=12))],
        ], colWidths=[1.3 * inch]),
        Table([
            [p(location, S("DL", fontName="CB", fontSize=13, textColor=WHITE, leading=16))],
            [p(f"{drive}  ·  {sleep_type}",
               S("DR", fontName="CI", fontSize=8, textColor=colors.HexColor("#AAAAAA"), leading=11))],
        ], colWidths=[5.5 * inch]),
    ]], colWidths=[1.4 * inch, 5.4 * inch])
    hdr.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), colors.HexColor("#2A2A2A")),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("BOX",           (0, 0), (-1, -1), 0.5, colors.HexColor("#111111")),
        ("LINEAFTER",     (0, 0), (0,  -1), 0.5, colors.HexColor("#555555")),
    ]))
    return hdr
