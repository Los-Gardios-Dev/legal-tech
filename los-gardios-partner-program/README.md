# Los Gardios Partner Program — Restructured Documents

**⚠️ Confidential — not covered by this repository's root MIT license.** These
are Los Gardios Group's real, filled-in partner-program legal documents, not
a generic Skills IL example. They should not be redistributed, forked, or
installed the way the sibling `israeli-*` skill folders are.

## What's here

The original 55-page `Los Gardios Partner Agreement` (source: the org's
Google Drive, both `.docx` and `.pdf`, Hebrew-authoritative + English
convenience translation) has been split into two documents, each provided
as both `.docx` (editable, original fonts/logo/header-footer preserved) and
`.pdf` (see *PDF generation* below for how these were produced and their
one known limitation):

| File | What it is | Pages (PDF) |
|---|---|---|
| `Los_Gardios_Partner_Agreement_HE.docx`/`.pdf` | The short, signed contract. Hebrew is the binding version per its own governing-language clause. | **23** |
| `Los_Gardios_Partner_Agreement_EN.docx`/`.pdf` | Convenience translation of the above. | 33 (see note below) |
| `Los_Gardios_Partner_Handbook_HE.docx`/`.pdf` | The operations manual, incorporated by reference — not signed separately. | 16 |
| `Los_Gardios_Partner_Handbook_EN.docx`/`.pdf` | Convenience translation of the above. | 23 |

**The Agreement is 23 pages, not the "3-5 pages" originally asked for.**
Every "compliance obligation" cluster (confidentiality, IP, data security,
authority/voice) is now a single commitment paragraph pointing to the
Handbook — see below — matching the pattern requested. What's left and
keeps it at 23 pages is: the full Definitions (kept for cross-reference
safety), the actual compensation Waterfall percentages and liability-cap
figures (deal terms, not obligations), and Sections 12-19 (termination,
tax, dispute resolution, international applicability, amendments, general
provisions, signatures) plus the two banking/POA annexes — kept close to
their original length because they're procedural/rights machinery, not
"things the partner promises to comply with." **If you want those
shortened the same way — a short paragraph per topic, full mechanics
moved to the Handbook — say so and it can be done**, but flagging first
because compressing e.g. the actual arbitration/jurisdiction clause or
the termination notice periods into a Handbook cross-reference is a
different kind of change than compressing a confidentiality clause: courts
generally expect dispute-resolution and governing-law terms to live in the
signed instrument itself, and a partner arguably needs their own notice-
period rights visible in what they sign, not only in an appendix the
Organization can amend with notice.

## The pattern applied, cluster by cluster

Per your instruction, every obligation-type section in the Agreement is
now one short paragraph — "by signing this Agreement, the Partner
undertakes to X, as detailed in the Partner Handbook" — with the full
substantive rules moved into the Handbook (new Chapter 10, plus existing
chapters):

| Cluster | Agreement now says (in short) | Full detail lives in |
|---|---|---|
| Confidentiality / non-solicitation / non-disclosure of methodology | One commitment paragraph (Section 9(a)) | Handbook Ch.10 |
| Data protection & security | One commitment paragraph, keeping the concrete numbers ($150k insurance, 48h notice) visible | Handbook Ch.10 (general duty) + Ch.8 (AI/tool policy, already there) |
| IP — the *exception* mechanism, hermetic rule, assignment, moral rights | One commitment paragraph (Section 8(b)); the default-ownership rule itself (8(a)) stays, since that's the actual deal term of who owns what | Handbook Ch.10 (hermetic rule/assignment) + Ch.7 (classification/monetization, already there) |
| Authority — voice & signature limits | One paragraph (Section 11(a)) | Handbook Ch.10 |
| Subcontracting | Already short (Section 2(b)) — unchanged | Handbook Ch.10 (full procedure — **this was missing entirely before**, see audit below) |

**Kept at full/near-full length, deliberately:** the compensation Waterfall
and its percentages, the liquidated-damages figure and mechanism, the
liability cap and its four uncapped exceptions, indemnification, and
Sections 12-19 — see the length note above for why.

## Completeness audit (what you asked me to verify before generating the PDF)

I went through every original section and sub-clause and confirmed each
one is either in the Agreement (short or full) or in the Handbook. This
audit caught two real gaps that predate today's changes — neither was a
consequence of shortening the Agreement, both were things the original
restructuring simply missed:

1. **Force majeure (original Section 11(g)) was missing entirely** from
   both documents. Added back to the Agreement (Section 11) in both
   languages — it's mutual boilerplate protecting both sides, not an
   obligation cluster, so it stays in the signed contract rather than
   moving to the Handbook.
2. **The subcontracting procedure's full mechanics were never written
   into the Handbook** — the Agreement pointed to it, but the Handbook
   only had the short pointer's target promised, not the actual content.
   Written into the new Handbook Chapter 10.

One more minor gap closed: Section 10(e)'s "this isn't a substitute for
your own country's data-protection compliance" disclaimer, added as a
closing note to Handbook Chapter 8.

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
for review purposes. This is also very likely why the English PDF page
counts (33 / 23) run proportionally higher than Hebrew's (23 / 16) — the
converter doesn't have the original's exact English body-text font
metrics to match against.

## Other things worth knowing

**Naming fix.** The original contract already has a *different*,
capitalized, non-incorporated term — "the Source Protocol" (פרוטוקול
המקור, Section 1) — for HQ's internal compensation/tier framework. Calling
the new document "Organization Protocols" would have collided with it, so
it's named the **Partner Handbook** instead, with an explicit clause
distinguishing the two.

**Fines reframed as investment + consequence, not weakened.** The original
liquidated-damages clause (₪100,000 minimum per breach, no cap) is
unchanged in legal substance — same figure, same floor/uncapped structure,
same blue-pencil severability — but now opens with what the Organization
invests before stating the compensation consequence for malicious harm.
**If the intent was also to change the amount, or narrow the trigger to
intentional conduct only (the original already reaches certain negligence
too), that's a substantive legal change, not a framing one — say so and
it can be adjusted.**

**Pre-existing issue found, not introduced here:** the *original* English
convenience translation has its own internal lettering drift in Section 8
(its English sub-clauses don't quite line up with the Hebrew ones a couple
of clauses in) — harmless since Hebrew governs, but worth a look if the
English copy is ever relied on directly.

The Agreement now incorporates the Handbook by reference (Section 17): the
Organization can update the Handbook's operational content with advance
written notice, but not the Agreement's core terms (pay, confidentiality,
IP, the compensation figure) without the partner's written consent.

## Recommended next step

This was restructured by an AI agent, not a lawyer. Given real money
(₪100,000+ per breach), real international partners, and jurisdiction-
specific annexes are involved, **have an Israeli-licensed attorney review
both documents — especially the compensation clause and the Handbook
incorporation-by-reference mechanism — before circulating them for
signature.**
