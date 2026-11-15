# -*- coding: utf-8 -*-
"""Render AGREEMENT_SHORT_EN.md (English translation of AGREEMENT_SHORT_HE.md)
as an A4, LTR, print-ready document in the same visual design as the Hebrew build."""
import io, re, html, base64, os
from fonts_embed import embedded_font_css

src = io.open("AGREEMENT_SHORT_EN.md", encoding="utf-8").read()
lines = src.split("\n")

# Brand assets (logo mark + official stamp), embedded as base64 so the HTML/PDF is self-contained.
_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
def _data_uri(fname):
    with open(os.path.join(_ASSETS, fname), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

LOGO_MARK = _data_uri("logo_mark_web.png")
LOGO_STAMP = _data_uri("logo_stamp_web.png")

def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t

out, i = [], 0
in_tbl = False

def close_tbl():
    global in_tbl
    if in_tbl:
        out.append("</tbody></table>")
        in_tbl = False

while i < len(lines):
    ln = lines[i].rstrip()
    s = ln.strip()

    if not s:
        close_tbl(); i += 1; continue

    # explicit keep-together group (heading/intro + the table it introduces,
    # so a table that doesn't fit the remaining page takes its heading with it
    # instead of stranding the heading/intro on the previous page)
    if s == "<!--group-start-->":
        out.append('<div class="keepgroup">'); i += 1; continue
    if s == "<!--group-end-->":
        out.append('</div>'); i += 1; continue

    # forced hard page break (distinct from "---", which is a cosmetic
    # divider only) — used where a section must start on its own page
    if s == "<!--newpage-->":
        out.append('<div class="hardbreak"></div>'); i += 1; continue

    # table
    if s.startswith("|") and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
        close_tbl()
        hdr = [c.strip() for c in s.strip("|").split("|")]
        aln = [c.strip() for c in lines[i+1].strip().strip("|").split("|")]
        def al(a): return "center" if a.startswith(":") and a.endswith(":") else "left"
        out.append("<table><thead><tr>" + "".join(
            f'<th style="text-align:{al(a)}">{inline(c)}</th>' for c, a in zip(hdr, aln)) + "</tr></thead><tbody>")
        in_tbl = True; i += 2
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            out.append("<tr>" + "".join(
                f'<td style="text-align:{al(aln[j]) if j<len(aln) else "left"}">{inline(c)}</td>'
                for j, c in enumerate(cells)) + "</tr>")
            i += 1
        close_tbl(); continue

    close_tbl()

    if s == "---":
        out.append('<div class="pagebreak"></div>'); i += 1; continue

    # a line of only underscores is a hand-fill blank — render as a
    # full-width ruled line rather than a <p>, whose justify/intrinsic-width
    # behavior shrinks an unbroken run of "_" to far less than the page width
    if re.fullmatch(r'_+', s):
        out.append('<div class="fillline"></div>'); i += 1; continue

    m = re.match(r'^(#{1,4})\s+(.*)$', s)
    if m:
        lvl, txt = len(m.group(1)), m.group(2)
        out.append(f'<h{lvl}>{inline(txt)}</h{lvl}>'); i += 1; continue

    if s.startswith("> "):
        blk = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            blk.append(lines[i].strip().lstrip(">").strip()); i += 1
        out.append('<div class="note">' + "<br>".join(inline(b) for b in blk if b) + "</div>")
        continue

    if re.match(r'^[-*]\s+', s) or re.match(r'^\d+\.\s+', s):
        ordered = bool(re.match(r'^\d+\.\s+', s))
        tag = "ol" if ordered else "ul"
        out.append(f"<{tag}>")
        while i < len(lines):
            c = lines[i].strip()
            if re.match(r'^[-*]\s+', c) or re.match(r'^\d+\.\s+', c):
                out.append("<li>" + inline(re.sub(r'^([-*]|\d+\.)\s+', '', c)) + "</li>"); i += 1
            else:
                break
        out.append(f"</{tag}>"); continue

    out.append("<p>" + inline(s) + "</p>"); i += 1

close_tbl()
body = "\n".join(out)

# the masthead already carries the wordmark: fold the leading title block into a title sheet
body = body.replace('<h1>LOS GARDIOS</h1>\n<h2>Client Engagement Agreement</h2>',
                    '<div class="doctitle">Client Engagement Agreement</div>', 1)

# annex cover pages — matching the original PDF's own divider-page design exactly:
# white background, a per-annex accent color (sampled from the source file), a small
# top masthead line with a colored circular letter badge, a colored "annex X" tag, the
# title and body in black/gray, and a giant, pale-tinted oversized letter bottom-left.
# Same 4-color categorical palette as the Guide's forecast-table section
# groups (gold/gold-deep/muted/purple) — not an independent color system.
ANNEX_COLORS = {
    "A": ("#A9824F", "#F4EEE4"),  # Genesis — gold
    "B": ("#8C6A3D", "#F2EAE0"),  # Commercial terms — gold-deep
    "C": ("#7D6F5C", "#F0EEE9"),  # Data & privacy — muted
    "D": ("#5B2986", "#F4F0F6"),  # Personal-data DPA — purple
}
_DEFAULT_AC_FOOT = "Forms an integral part of the Agreement (Section 15(a)) · enters into force upon signature at the end of this document"
for L, title, sub, foot in [
    ("A", "Genesis — Financial Terms",
     "The value of the Genesis Research and cost sharing, the Participation Fee, what happens if at the end of the research you decide not to proceed, and the purchase option (Buyout). A full description of the research process itself — in the Client Guide.",
     _DEFAULT_AC_FOOT),
    ("B", "Commercial Terms and Inputs",
     "The general principles for the monthly budget, scope boundaries and Tolerance level, and the Stop-Loss mechanism; the specific parameters for each engagement are set in its separate signed Proposal.",
     _DEFAULT_AC_FOOT),
    ("C", "Data, Privacy and Recorded Communication",
     "The three data layers and what is done in each layer, how the Client's privacy is protected, and how and when calls and meetings are recorded.",
     _DEFAULT_AC_FOOT),
    ("D", "Personal Data Protection (DPA)",
     "Purposes and manner of processing personal data, types of data and data subjects, sub-processors, international transfers, reporting of security incidents, and the right of audit.",
     "Applies to the engagement only if marked as such in the relevant signed Proposal (Section 15(a))"),
]:
    # compact per-annex banner — a colored tag + rule, no full divider page: the short
    # contract's whole point is length, and the full-page annex-cover (min-height:620px,
    # masthead, giant letter) costs nearly a full page per annex even sharing with content.
    accent, tint = ANNEX_COLORS[L]
    cover = (
        f'<div class="mini-divider" style="--ax:{accent};--ax-tint:{tint}">'
        f'<span class="mini-badge">{L}</span>'
        f'<span class="mini-sub">{sub}</span>'
        f'</div>'
    )
    body = body.replace(f"<h1>Appendix {L} — ", cover + f'<h1 class="annex-h" style="border-bottom-color:{accent}">Appendix {L} — ', 1)

# the framework agreement itself (Parts I-IV) gets the same divider treatment as the
# three annexes, so all four parts of the document open with a matching cover page —
# using the base brand purple (the framework's own identity, not a sub-annex hue) and a
# section-mark (§) in place of an annex letter, since this part isn't "annex X".
_fw_accent, _fw_tint = ANNEX_COLORS["A"]
_fw_cover = (
    f'<div class="mini-divider" style="--ax:{_fw_accent};--ax-tint:{_fw_tint}">'
    f'<span class="mini-badge">§</span>'
    f'<span class="mini-sub">Foundations of the engagement and the Parties\' obligations, protection of the Organization\'s Assets and intellectual property, liquidated damages and limitation of liability, term, termination and dispute resolution.</span>'
    f'</div>'
)
body = body.replace('<h1>Part I — Foundations of the Engagement</h1>',
                     _fw_cover + f'<h1 class="annex-h" style="border-bottom-color:{_fw_accent}">Part I — Foundations of the Engagement</h1>', 1)

# Signature blocks: the organization's column carries the official stamp — the authorized
# signatory signs across/beside it on the printed page, in addition to filling in their
# details in the rows above (name, title, ID) which remain plain fill-in lines.
_STAMP_CELL = (
    '<div class="stampcell"><img src="' + LOGO_STAMP + '" alt="Organization stamp" class="stampimg">'
    '<div class="stampline"></div><div class="stampcaption">Authorized signature — on and beside the stamp</div></div>'
)
body = body.replace(
    '<tr><td style="text-align:left">Signature and stamp</td><td style="text-align:left">______________________</td><td style="text-align:left">______________________</td></tr>',
    '<tr><td style="text-align:left">Signature and stamp</td><td style="text-align:left">______________________</td><td style="text-align:left">' + _STAMP_CELL + '</td></tr>',
    1,
)
body = body.replace(
    '<tr><td style="text-align:left">Signature</td><td style="text-align:left">______________________</td><td style="text-align:left">______________________</td></tr>',
    '<tr><td style="text-align:left">Signature</td><td style="text-align:left">______________________</td><td style="text-align:left">' + _STAMP_CELL + '</td></tr>',
    1,
)

# Clause cards — the original wraps each Section's body in a pale card sitting below the
# bold heading (the heading itself stays outside/above it, on the white page). Every
# <h2> here is either "Section N — ..." (gets the card) or a signature sub-heading like
# "Acknowledgments"/"Signatures" (left alone, matching the original's plain signature pages).
#
# Four clauses carry materially more weight for the signer than the rest of the
# document — the non-solicit/non-circumvent restriction, the liquidated-damages
# table, the liability cap, and the Buyout/independent-implementation restriction
# — and get a visually distinct card (purple accent instead of gold) so a reader
# skimming under signing pressure gets a cue that these are not routine clauses.
_KEY_CLAUSES = (
    "Section 8 — Protection of Professional",
    "Section 11 — Remedies, Recovery of Investment",
    "Section 12 — Limitation of Liability",
    "Section 3 — Purchase Option",
)
_parts = re.split(r'(<h[12][^>]*>.*?</h[12]>)', body)
_out2, _pending, _in_clause, _key_clause = [], [], False, False
def _flush():
    global _pending, _in_clause, _key_clause
    if _in_clause and _pending:
        _cls = "clausebox clausebox-key" if _key_clause else "clausebox"
        _out2.append(f'<div class="{_cls}">' + "".join(_pending) + '</div>')
    else:
        _out2.extend(_pending)
    _pending = []
for _tok in _parts:
    _m = re.match(r'<h([12])[^>]*>(.*?)</h\1>', _tok, re.S)
    if _m:
        _flush()
        _htxt = _m.group(2).strip()
        _in_clause = _m.group(1) == "2" and _htxt.startswith("Section ")
        _key_clause = any(_htxt.startswith(k) for k in _KEY_CLAUSES)
        _out2.append(_tok)
    else:
        _pending.append(_tok)
_flush()
body = "".join(_out2)
# keep forced page breaks outside the clause cards, so the preceding card does not
# split and leave an empty card sliver at the top of the new page
body = re.sub(r'\s*<div class="hardbreak"></div>\s*</div>', '</div>\n<div class="hardbreak"></div>', body)

CSS = """
/* Design language deliberately lighter than CLIENT_GUIDE_HE.md's build: the
   Guide is a physical, printed, editorial piece meant to impress on arrival;
   this Agreement is a digital document signed digitally — it borrows the
   Guide's palette tokens and Heebo/Frank Ruhl Libre font pairing so the two
   read as one brand family, but stays plain and functional (white page, no
   dark cover band, no photographic/editorial treatment) rather than matching
   the Guide's own level of production. The Agreement keeps its own flowing-
   document architecture (native @page pagination, not the Guide's per-page
   divs): this is a light re-theme, not a re-architecture. */
:root{
 --ink:#2A2118; --muted:#7D6F5C; --rule:#E3D8C3; --soft:#FAF7F1;
 --gold:#A9824F; --gold-deep:#8C6A3D;
 --purple:#5B2986; --accent:#5B2986
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#eeeae1;color:var(--ink);direction:ltr;
 font-family:"Heebo","Frank Ruhl Libre",Georgia,serif;
 font-size:10.4pt;line-height:1.78}
.sheet{max-width:820px;margin:0 auto;background:#fff;padding:34px 46px 46px}
.masthead{border-bottom:2px solid var(--gold);padding-bottom:14px;margin-bottom:26px;
 display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap}
.mh-brand{font-family:Helvetica,Arial,sans-serif;font-weight:700;font-size:17pt;
 letter-spacing:.28em;color:var(--ink);display:flex;align-items:center;gap:10px}
.mh-mark{height:30px;width:auto;flex:none}
.mh-meta{font-family:"Heebo",sans-serif;font-size:7.4pt;letter-spacing:.16em;
 color:var(--muted);text-align:right;line-height:1.9;direction:ltr}
.conf{display:inline-block;border:1px solid var(--purple);color:var(--purple);
 font-family:"Heebo",sans-serif;font-size:7pt;letter-spacing:.24em;
 padding:2px 9px;border-radius:2px}
h1{font-family:"Frank Ruhl Libre",serif;font-weight:600;font-size:17pt;margin:26px 0 12px;
 padding-bottom:8px;border-bottom:3px solid var(--gold);letter-spacing:.01em;color:var(--ink)}
h2{font-family:"Frank Ruhl Libre",serif;font-weight:600;font-size:12.8pt;margin:22px 0 8px;
 color:var(--ink);break-after:avoid;page-break-after:avoid}
.clausebox{background:var(--soft);border-inline-start:3px solid var(--gold);
 padding:14px 17px;margin:0 0 10px;break-inside:avoid;page-break-inside:avoid}
.clausebox-key{border-inline-start:5px solid var(--purple);position:relative;padding-top:28px}
.clausebox-key::before{content:"KEY PROTECTION MECHANISM — READ CAREFULLY";position:absolute;
 top:10px;inset-inline-start:17px;font-family:"Heebo",sans-serif;font-weight:700;
 font-size:7.4pt;letter-spacing:.14em;color:var(--purple)}
.keepgroup{break-inside:avoid;page-break-inside:avoid}
.clausebox>p:last-child,.clausebox>ul:last-child,.clausebox>ol:last-child,.clausebox>table:last-child{margin-bottom:0}
h3{font-family:"Frank Ruhl Libre",serif;font-size:11.2pt;margin:16px 0 6px;color:var(--gold-deep)}
h4{font-size:10pt;margin:13px 0 5px;color:var(--muted)}
p{margin:0 0 9px;text-align:justify;hyphens:auto;-webkit-hyphens:auto}
strong{font-weight:700;color:var(--ink)}
code{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:.87em;background:var(--soft);
 border:1px solid var(--rule);border-radius:3px;padding:.5px 4px;direction:ltr;
 display:inline-block;unicode-bidi:embed}
ul,ol{margin:0 0 10px;padding-inline-start:22px}
li{margin:0 0 4px;text-align:justify;hyphens:auto;-webkit-hyphens:auto}
table{width:100%;border-collapse:collapse;margin:12px 0 16px;font-size:9.2pt;
 display:block;overflow-x:auto}
thead th{background:transparent;color:var(--gold-deep);font-weight:700;padding:7px 9px;
 border-bottom:2px solid var(--gold);font-family:"Heebo",sans-serif;font-size:8.6pt;letter-spacing:.02em}
tbody td{border-bottom:1px solid var(--rule);padding:7px 9px;vertical-align:top}
.note{background:var(--soft);border-inline-start:3px solid var(--gold-deep);
 padding:11px 14px;margin:13px 0;font-size:9.6pt;color:#382c1f}
hr{border:0;border-top:1px solid var(--rule);margin:22px 0}
.pagebreak{border-top:1px solid var(--rule);margin:26px 0}
.hardbreak{break-before:page;page-break-before:always}
.fillline{border-bottom:1px solid var(--rule);height:26px;margin:0 0 4px}
/* Compact per-section banner — a colored badge letter and a one-line
   description above the heading, in the same eyebrow language as the
   Guide's chapter dividers, sized to cost no extra page per section. */
.mini-divider{display:flex;align-items:center;gap:12px;margin:30px 0 -4px;padding-top:16px;
 border-top:2px solid var(--ax)}
.mini-badge{width:26px;height:26px;border-radius:50%;background:var(--ax);color:#fff;
 font-family:"Frank Ruhl Libre",serif;font-weight:700;font-size:11pt;flex:none;
 display:flex;align-items:center;justify-content:center}
.mini-sub{font-family:"Heebo",sans-serif;font-size:8.8pt;color:var(--muted);line-height:1.6}
.stampcell{display:flex;flex-direction:column;align-items:center;gap:2px}
.stampimg{width:92px;height:92px;object-fit:contain;opacity:.9}
/* English text runs longer than the Hebrew: tighten the signature table so the
   whole signature block still fits on its own dedicated page */
table:has(.stampcell){margin:6px 0 0}
table:has(.stampcell) tbody td{padding:3px 9px}
table:has(.stampcell) thead th{padding:4px 9px}
table:has(.stampcell) .stampimg{width:64px;height:64px}
.hardbreak+h1{margin-top:0}
.stampline{width:100%;border-top:1px solid var(--ink);margin-top:2px}
.stampcaption{font-family:"Heebo",sans-serif;font-size:6.6pt;color:var(--muted);
 letter-spacing:.03em;text-align:center}
.doctitle{font-family:"Frank Ruhl Libre",serif;font-weight:600;font-size:23pt;margin:6px 0 4px;letter-spacing:.01em}
.docfoot{margin-top:34px;padding-top:12px;border-top:1px solid var(--rule);
 font-family:"Heebo",sans-serif;font-size:7.6pt;letter-spacing:.10em;
 color:var(--muted);display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
@page{size:A4;margin:22mm 15mm 17mm}
@media print{
 body{background:#fff}
 .sheet{max-width:none;padding:0}
 .masthead{margin:0 0 26px}
 thead th{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 .clausebox,.mini-badge{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 h1,h2{break-after:avoid}
 table,.note{break-inside:avoid}
}
"""

doc = f"""<!doctype html>
<html lang="en" dir="ltr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Los Gardios — Client Engagement Agreement</title>
{embedded_font_css()}
<style>{CSS}</style></head>
<body><div class="sheet">
<div class="masthead">
  <div><div class="mh-brand"><img src="{LOGO_MARK}" alt="Los Gardios" class="mh-mark">LOS GARDIOS HOLDINGS</div>
    <div style="margin-top:7px"><span class="conf">CONFIDENTIAL</span></div></div>
  <div class="mh-meta">Los Gardios Ltd.<br>516819257 · 15 HaSdera HaMerkazit, Modi'in<br>Template Version 2 · Unified Engagement Document Set</div>
</div>
{body}
<div class="docfoot"><span>Los Gardios — Client Engagement Agreement (Confidential)</span><span>Template Version 2</span></div>
</div></body></html>"""

io.open("AGREEMENT_SHORT_EN.html", "w", encoding="utf-8").write(doc)
print("wrote AGREEMENT_SHORT_EN.html", len(doc), "bytes")
