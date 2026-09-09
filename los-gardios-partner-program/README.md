# Los Gardios Partner Program — Restructured Documents

**⚠️ Confidential — not covered by this repository's root MIT license.** These
are Los Gardios Group's real, filled-in partner-program legal documents, not
a generic Skills IL example. They should not be redistributed, forked, or
installed the way the sibling `israeli-*` skill folders are.

## ⚠️ Hebrew is current; English is stale (Round 3/4 not yet applied to it)

Per explicit instruction, this round's rebuild (see below) was Hebrew-only —
**`Los_Gardios_Partner_Agreement_HE` and `Los_Gardios_Partner_Handbook_HE` are
current.** The `_EN` files are still the *previous* round's structure (the
"short-clause-per-obligation-cluster" version, 23/16 pages) and no longer
match the Hebrew documents' structure, section count, or the new compensation
clause at all. Since Hebrew is the governing language (see the Agreement's
own governing-language clause), this is a real mismatch, not just a stale
translation — **do not send the `_EN` files to anyone alongside the new `_HE`
files until they're rebuilt to match.** Say so and that can be done next.

## What's here

| File | What it is | Pages (PDF, measured) |
|---|---|---|
| `Los_Gardios_Partner_Agreement_HE.docx`/`.pdf` | The short, signed contract. Hebrew is the binding version per its own governing-language clause. | **11** |
| `Los_Gardios_Partner_Agreement_EN.docx`/`.pdf` | ⚠️ Stale — previous round's structure (23 pages), not this one. | 33 |
| `Los_Gardios_Partner_Handbook_HE.docx`/`.pdf` | The operations manual, incorporated by reference — not signed separately. | **28** |
| `Los_Gardios_Partner_Handbook_EN.docx`/`.pdf` | ⚠️ Stale — previous round's structure (16 pages), not this one. | 23 |

## This round: the actual 50+ pages relocated, not rewritten

Earlier rounds shortened *some* sections into commitment paragraphs but kept
much of the Agreement's own length (23 pages) — flagged at the time as not
matching the "1-3 pages of signing" target. This round follows through on
that instruction fully: **every section of the original contract is now
either (a) one short paragraph in the Agreement pointing to the Handbook, or
(b) relocated to the Handbook *verbatim* — copied from the original contract's
own XML, not paraphrased or rewritten into new prose.** Only section
headlines/framing were ever adapted for tone (the same treatment as the
existing "Our Investment" chapter); the operative legal text itself is moved,
not rewritten.

**The Agreement is 11 pages, not literally "1-3."** What keeps it above that:
party identification, Annexes C and D (the Country Annex and the Financial
Power-of-Attorney form — both explicitly requested to live in the signed
Agreement itself, not the Handbook), the individual-side-letter block with its
own blank lines and signature (Section 18(ז) in the original — this can't
move to a shared Handbook since it's a per-partner fillable exhibit with its
own signature line), the full compensation clause (see below), Section 15
(dispute resolution) and Section 19 (signatures/ID/payment) kept complete
rather than shortened, and the closing marking/signature clause. Everything
else is now a single short paragraph. The Table of Contents was dropped
entirely — it was sized for 55 pages and isn't needed at this length.

**Sections 15 and 19 were kept complete and verbatim, not shortened, on
purpose:** forum/governing-law terms are conventionally expected to stay
visible in the document a partner actually signs, and — separately — the
dispute-resolution/arbitration section's phrasing was flagged as wanting a
change that hasn't been specified yet. Verbatim preservation is the safe
default until that's clarified, rather than guessing at new wording.

## The compensation clause (Section 9) — redesigned this round

Modeled on the asset-value structure used in the client-engagement agreement
(the pattern shown for that document), Section 9's compensation clause now:

1. **Names the categories of investment** the Organization makes, as an actual
   table (asset type / description of the investment) — human capital
   (recruitment/screening/training), business relationships, confidential
   information/methodology, IP and technology, organizational/security
   infrastructure, and research/strategic assets for the partner's own work —
   instead of one undifferentiated "fine."
2. **Applies only to intentional, malicious harm.** This is now explicit and
   prominent: *"a partner who acted in good faith and made an honest mistake
   is not liable under this clause; a partner who deliberately and maliciously
   harmed one of these assets must compensate the Organization for it"* — in
   both directions, as requested.
3. **Ties the compensation to whichever specific asset was harmed**, not one
   flat number regardless of what happened — and if one course of conduct
   harms more than one category, only the single highest applicable amount is
   charged, not a stacked sum (anti-double-counting, mirroring the client-
   agreement pattern).
4. Keeps the **real, pre-existing figure** — NIS 100,000 per breach, as a
   floor, uncapped — since that's an actual agreed contractual term, not
   something to invent. **No per-category dollar figures were fabricated.**
   The client-engagement agreement's table has real internal cost figures
   (e.g. the $10,000 Genesis Audit); nothing equivalent exists for partner
   recruitment/training/etc. costs, and inventing numbers for a real contract
   would assert false facts. If you have real internal figures for any of the
   listed categories, they can be dropped in as a genuine value table instead
   of the category-description format used now.

## Completeness audit (repeated for this round's rebuild)

Every original section (1-19) and both annexes were confirmed present in
either the Agreement or the Handbook by direct inspection of the rebuilt
files, the same way the first restructuring was audited. This round's rebuild
also re-confirmed the two real gaps the first audit found in the *original*
contract's own drafting are still correctly filled: the subcontracting
procedure's full mechanics (referenced by the Agreement, never actually
written out anywhere in the original) and the "this isn't a substitute for
your own country's data-protection compliance" disclaimer. Force majeure,
flagged previously as missing, turned out on a second, closer look to
actually be present in the original (Section 11(ז)) — it's carried over by
the plain verbatim relocation and needed no separate fix.

The old flat liquidated-damages clause and its blue-pencil sub-clause were
confirmed **absent** from both documents, as intended — they're superseded by
the new Section 9 compensation clause above, not merely relocated.

## Design fidelity fix (after feedback that the design wasn't preserved)

You were right — the PDF header/footer were wrong. I downloaded the actual
original PDF from the same Drive folder as the source `.docx` files and
compared it directly (rather than going by memory), which turned up two real
bugs in the PDF converter (not the `.docx` — see why below):

- **Footer**: the original has three parts — a blank per-party initials line
  on the left (for hand-initialing each page), "מסמך חסוי · Los Gardios
  Group" in the center, and a real "עמוד X מתוך Y" page count on the right.
  The PDFs sent earlier had one centered line with the wrong wording and no
  page numbers at all.
- **Header**: the original is a left-text / right-logo split with a rule
  underneath, not a centered bar.

Both are now fixed and match — see the header/footer on the PDFs above. One
thing I checked and it turned out **not** to be a problem: the font looked
different at a glance, but a side-by-side zoom of the same sentence in both
PDFs confirmed it's the same typeface (Frank Ruhl Libre, embedded in the
`.docx` and correctly picked up) — that was a false alarm on my part.

**Why this bug didn't affect the `.docx` files**: the `.docx` files are built
by literally copying the original's own header/footer/styles/theme XML parts
into the new file unchanged — they were never at risk here, since nothing
about them was regenerated. The bug was specifically in my separate, approximate
PDF converter (see below), which was hand-building its own simplified
header/footer instead of actually reading the original's real one. If you
want to sanity-check design fidelity again on anything else, the `.docx` is
the more reliable file to check — it opens with the original's real design
system, not an approximation.

## PDF generation — how, and one limitation to know about

This sandboxed environment's LibreOffice install is broken (confirmed via
strace — it fails even converting a plain `.txt` file, with and without
this session's own command-sandboxing disabled, so it's an environment
issue, not something to route around unsafely). There's no Word/LibreOffice
renderer available here, so the PDFs were produced via a custom docx→HTML
converter + WeasyPrint (a standalone Python PDF engine) — preserving the
real fonts, logo, RTL layout, bold formatting, and running header/footer,
but rebuilding the page layout rather than using Word's own renderer.
**Recommendation: open the `.docx` files in actual Word or Google Docs at
some point and re-export to PDF from there for the version you actually
send out** — the `.docx` files themselves are the ones built directly from
the original file's XML (fonts/logo/styles inherited, not recreated), so
they're the higher-fidelity source; these PDFs are a close approximation
for review purposes.

## Other things worth knowing

**Naming.** The Handbook is named the **Partner Handbook** (מדריך השותף), not
"Organization Protocols" — the original contract already uses a different,
capitalized, non-incorporated term ("the Source Protocol," Section 1) for
HQ's internal compensation/tier framework, and reusing "Protocols" for the
new document would have collided with it. The Agreement explicitly
distinguishes the two.

The Agreement incorporates the Handbook by reference (the "17." clause): the
Organization can update the Handbook's operational content with advance
written notice, but not the Agreement's core terms (pay, confidentiality, IP,
the compensation clause) without the partner's written consent, and the
Agreement prevails over the Handbook in the event of any conflict.

**Pre-existing issue found, not introduced here:** the *original* English
convenience translation has its own internal lettering drift in Section 8
(its English sub-clauses don't quite line up with the Hebrew ones a couple
of clauses in) — harmless since Hebrew governs, but worth a look if the
English copy is ever relied on directly.

## Still open

1. **Git push.** These commits are local only. Given the confidentiality
   notice above (real filled-in contracts, not a generic template), pushing
   to the shared repo needs an explicit yes — asked before, still open.
2. **Dispute-resolution/arbitration phrasing.** Flagged as wanting a change,
   specifics not yet given — Section 15 was left verbatim this round rather
   than guessed at (see above).
3. **English rebuild.** The `_EN` files need the same treatment as `_HE` to
   stop being stale (see the warning at the top).

## Recommended next step

This was restructured by an AI agent, not a lawyer. Given real money
(₪100,000+ per breach), real international partners, and jurisdiction-
specific annexes are involved, **have an Israeli-licensed attorney review
both documents — especially the compensation clause and the Handbook
incorporation-by-reference mechanism — before circulating them for
signature.**
