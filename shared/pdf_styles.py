"""
shared/pdf_styles.py
Carlito font registration and all paragraph styles used across
van spec and trip report PDFs.
"""

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── FONT REGISTRATION ─────────────────────────────────────────────────────────
# Carlito is metrically identical to Calibri (same character widths, same spacing).
# Installed at /usr/share/fonts/truetype/crosextra/ on Ubuntu.
# On macOS/Windows: download from Google Fonts and update paths.

FONT_PATHS = {
    "C":   "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf",
    "CB":  "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf",
    "CI":  "/usr/share/fonts/truetype/crosextra/Carlito-Italic.ttf",
    "CBI": "/usr/share/fonts/truetype/crosextra/Carlito-BoldItalic.ttf",
}


def register_fonts():
    """Register Carlito font family with ReportLab. Call once before building any PDF."""
    pdfmetrics.registerFont(TTFont("C",   FONT_PATHS["C"]))
    pdfmetrics.registerFont(TTFont("CB",  FONT_PATHS["CB"]))
    pdfmetrics.registerFont(TTFont("CI",  FONT_PATHS["CI"]))
    pdfmetrics.registerFont(TTFont("CBI", FONT_PATHS["CBI"]))
    pdfmetrics.registerFontFamily(
        "C", normal="C", bold="CB", italic="CI", boldItalic="CBI"
    )


# ── PALETTE — neutral only, no color coding ───────────────────────────────────
INK   = colors.HexColor("#1A1A1A")   # body text
MID   = colors.HexColor("#444444")   # secondary text
DIM   = colors.HexColor("#666666")   # tertiary / labels
RULE  = colors.HexColor("#CCCCCC")   # light rules
RULE2 = colors.HexColor("#E8E8E8")   # table inner grid
BG    = colors.HexColor("#F7F7F7")   # light background rows
GOLD  = colors.HexColor("#8B6914")   # star / anniversary accent
WHITE = colors.white
TBL_H = colors.HexColor("#2A2A2A")   # table header background


def S(name, **kwargs):
    """Shorthand for ParagraphStyle with Carlito as the default font."""
    kwargs.setdefault("fontName", "C")
    kwargs.setdefault("textColor", INK)
    return ParagraphStyle(name, **kwargs)


# ── STYLES ────────────────────────────────────────────────────────────────────

TITLE  = S("TITLE",  fontName="CB", fontSize=22, alignment=TA_CENTER, leading=28, spaceAfter=4)
SUB    = S("SUB",    fontName="CI", fontSize=11, alignment=TA_CENTER, leading=15, textColor=MID, spaceAfter=4)
H2     = S("H2",     fontName="CB", fontSize=13, leading=17, spaceBefore=10, spaceAfter=3)
H3     = S("H3",     fontName="CB", fontSize=11, leading=14, spaceBefore=8,  spaceAfter=2)
H4     = S("H4",     fontName="CB", fontSize=10, leading=13, spaceBefore=5,  spaceAfter=2)
BODY   = S("BODY",   fontSize=9.5,  leading=14, spaceAfter=4, alignment=TA_JUSTIFY)
BODYL  = S("BODYL",  fontSize=9.5,  leading=14, spaceAfter=4)
BUL    = S("BUL",    fontSize=9,    leading=13, leftIndent=14, spaceAfter=2)
LABEL  = S("LABEL",  fontName="CB", fontSize=8, textColor=DIM, leading=11, spaceAfter=1)
DETAIL = S("DETAIL", fontSize=8.5,  leading=12, textColor=MID, spaceAfter=2)
ITA    = S("ITA",    fontName="CI", fontSize=9, leading=12, textColor=MID, spaceAfter=3)
SMALL  = S("SMALL",  fontSize=8,    leading=12, textColor=DIM)
NOTE   = S("NOTE",   fontName="CI", fontSize=9, leading=13, textColor=MID)
WARN   = S("WARN",   fontName="CB", fontSize=9, leading=13, textColor=INK)
STAR   = S("STAR",   fontName="CBI",fontSize=9, leading=13, textColor=GOLD)
TH     = S("TH",     fontName="CB", fontSize=8.5, textColor=WHITE, leading=12)
TB     = S("TB",     fontSize=8.5,  leading=12)
