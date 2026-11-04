# -*- coding: utf-8 -*-
"""Self-hosted, embedded Heebo/Frank Ruhl Libre @font-face CSS.

Both build_html_short.py and build_html_guide.py used to load these two
families from Google Fonts' CDN at render time (a `<link>` to
fonts.googleapis.com). That is fragile for a deterministic build pipeline —
and in this environment it silently produces WRONG output: Chromium's
PRINT-TO-PDF path (used by build_pdf_short.py/build_pdf_guide.py) fails to
embed the *variable* font files Google Fonts serves, falling back to
Liberation/DejaVu for the exported PDF specifically, even though the live
page (and a plain screenshot) renders with the correct webfont. Static,
single-weight instances embedded directly as data: URIs sidestep both
problems at once: no network dependency, and no variable-font PDF-embedding
bug. The six files in assets/fonts/ are static instances (via `fonttools
varLib.instancer`) of the official open-source variable fonts, at exactly
the weights this project's CSS uses (Heebo 300/400/600/700, Frank Ruhl Libre
600/700).
"""
import base64, os

_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "fonts")

_FACES = [
    ("Heebo", 300, "Heebo-300.ttf"),
    ("Heebo", 400, "Heebo-400.ttf"),
    ("Heebo", 600, "Heebo-600.ttf"),
    ("Heebo", 700, "Heebo-700.ttf"),
    ("Frank Ruhl Libre", 600, "FrankRuhlLibre-600.ttf"),
    ("Frank Ruhl Libre", 700, "FrankRuhlLibre-700.ttf"),
]


def embedded_font_css():
    """Returns a <style> block (including the tags) defining all six
    @font-face rules with base64-embedded font data — a drop-in replacement
    for the Google Fonts <link> tags."""
    rules = []
    for family, weight, fname in _FACES:
        with open(os.path.join(_ASSETS, fname), "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        rules.append(
            f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"src:url(data:font/ttf;base64,{b64}) format('truetype')}}"
        )
    return "<style>" + "".join(rules) + "</style>"
