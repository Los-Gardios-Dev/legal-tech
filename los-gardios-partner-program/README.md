# Los Gardios Partner Program — Restructured Documents

**⚠️ Confidential — not covered by this repository's root MIT license.** These
are Los Gardios Group's real, filled-in partner-program legal documents, not
a generic Skills IL example. They should not be redistributed, forked, or
installed the way the sibling `israeli-*` skill folders are.

## ⚠️ Hebrew is current; English is stale

This round's rebuild (see below) was Hebrew-only, per instruction —
**`Los_Gardios_Partner_Agreement_HE` and `Los_Gardios_Partner_Handbook_HE` are
current.** The `_EN` files are several structural rounds behind and no longer
match the Hebrew documents at all (different length, different section count,
old compensation clause). Since Hebrew is the governing language, don't send
the `_EN` files alongside the new `_HE` ones until they're rebuilt to match —
say so and that can be done next.

## What's here (current structure, as of the latest rebuild)

| File | What it is | Pages (PDF, measured) |
|---|---|---|
| `Los_Gardios_Partner_Agreement_HE.docx`/`.pdf` | The short, signed contract: party ID + minimal numbered enforcement clauses + Annexes C/D + signature page. | **6** (3 of them are the actual contract clauses — see breakdown below) |
| `Los_Gardios_Partner_Agreement_EN.docx`/`.pdf` | ⚠️ Stale — several rounds behind, do not use. | — |
| `Los_Gardios_Partner_Handbook_HE.docx`/`.pdf` | The full original 51-page document, kept essentially as-is, repurposed as the incorporated-by-reference Handbook. | **38** |
| `Los_Gardios_Partner_Handbook_EN.docx`/`.pdf` | ⚠️ Stale — several rounds behind, do not use. | — |

## The current architecture (corrected this round)

The prior round over-engineered this: it gave the Contract one short
paragraph per original topic (16 of them) and rebuilt the Handbook into new,
reorganized chapters. Both were more complicated than asked for. This round
follows the actual instruction instead:

**The Handbook is the original 51-page document, essentially unchanged** —
same numbering, same Table of Contents, same recitals, same section order,
nothing reworded or reorganized. The only edit anywhere in it: Section 9's
old compensation sub-clauses ((ו)/(ז) — the flat NIS 100,000 figure and its
blue-pencil clause) are replaced by the asset-category clause and table
already agreed on with you (see below), relettered to (ו)-(י) so the
section's own sequence stays intact. Every other section, including its many
internal "as stated in this Agreement" self-references, is left completely
untouched — that's intentional, not an oversight: the Contract's clause 2.2
incorporates the Handbook "as though fully set forth" in the Contract, which
is the standard legal mechanism that keeps those references correctly
binding without needing to hand-edit fifty pages of cross-references.

**The Contract is new and minimal** — party identification, then five
numbered sections of pure enforcement/incorporation machinery, decimally
numbered (1.1, 1.2, 1.3 / 2.1-2.4 / 3.1-3.2 / 4.1-4.2 / 5.1-5.3) as asked,
not one paragraph per original topic:

1. **מבוא ופרשנות** — governing language, nature of the relationship
   (profit-share only, not equity/employment), definitions-by-reference
2. **מדריך השותף — מיזוג והתחייבות** — the actual incorporation clauses:
   confirms the partner read the Handbook, binds them to every provision of
   it as though written into the Contract itself, sets the amendment
   procedure, and states which document prevails in a conflict
3. **תמורה ופיצוי** — the partner's sole compensation is the Handbook's
   profit-split; the malice-only compensation clause condensed to its
   operative terms (good-faith carve-out, the NIS 100,000 floor, pointer to
   the Handbook for the full asset-category table)
4. **סיום ויישוב סכסוכים** — pointers to the Handbook and Annex C (Section
   15's actual wording is still just a pointer here, not rewritten — see
   "Still open" below, that request was never specified)
5. **הוראות כלליות** — entire agreement, annexes, blue-pencil severability

Then the closing marking/signature clause, Annexes C and D (attached in
full — these are per-partner fillable forms, not general reference content,
so they can't move to the shared Handbook), and the signature page.

**Page breakdown, measured, not guessed:** the party-ID page + the five
numbered sections + the marking clause come to **3 pages** — matching what
you asked for. The remaining 4 pages are Annex C (Country Annex), Annex D
(Financial Power of Attorney), and the signature page — attachments, not
contract prose, per the earlier explicit instruction that C and D belong in
the signed package. If you'd rather those didn't count against the page
target at all — e.g. handed out as separate physical forms rather than part
of the same PDF — say so.

## The compensation clause — unchanged from last round, still in both places

Section 3.2 of the Contract has the operative terms (malice-only trigger,
good-faith carve-out, the real NIS 100,000/breach floor — no invented
numbers). The full version — the six-category investment table (human
capital, business relationships, confidential information/methodology,
IP/technology, security infrastructure, research/strategic assets) and the
complete anti-double-counting mechanism — lives in the Handbook's Section 9,
in place of the old flat clause. Nothing about the substance changed this
round, only where the short version sits.

## Layout fix — checkboxes were stacking instead of sitting on one line

Went through a careful side-by-side, page-by-page comparison against the
downloaded original PDF (not just spot checks) after being asked again to
match its layout. Found one real bug: the Discipline Group options and the
Annex D checkboxes (9 checkboxes total) are each their own `<w:p>` paragraph
in the source XML, immediately followed by a separate label paragraph —
the original visually places each pair on one line ("מסחר ☐"), but the
converter was rendering them as two stacked lines, taking roughly double
the vertical space and looking noticeably less organized. Fixed by merging
each checkbox with its following label onto one line; this alone brought
the Contract down from 7 to 6 pages. Checked the logo color too, since it
looked grayscale at a glance — sampled actual pixel values and it's
correctly the original's purple, so that one was a false alarm, not a bug.

## Design fidelity correction — I was wrong about one thing last round

Comparing pixel colors directly against the real original PDF (not just
eyeballing a thumbnail) turned up something I'd missed and stated
incorrectly before: **the original's rule lines — under the header, and
under every section heading — are a deep purple (`#4B2170`), not gray.**
I'd told you the design was "plainer, no purple" when flagging the uploaded
Client Engagement Agreement as a different document's brand skin — that
distinction still holds (that document's fuller card-style layout is a
different design system), but the purple accent itself turned out to be
part of the Partner Agreement's own real design after all, confirmed by
sampling actual pixel values from the downloaded original, not by looking.
Both documents' header/footer/heading rules now use the correct color.

## Completeness / audit trail from prior rounds (still holds)

Every original section (1-19) and both annexes are present — trivially true
now, since the Handbook is the original document itself. The two real gaps
found in the *original* contract's own drafting during the first audit
(the subcontracting procedure's full mechanics, referenced but never
actually written out anywhere in the original; the "not a substitute for
your own country's compliance" disclaimer) are **not** restored in this
version, since they were additions to the previous, more heavily-edited
Handbook draft, not part of the original document this round now uses
verbatim. Flagging this explicitly: if those two gap-fills should still be
added to the current Handbook, say so and it's a small, targeted addition
in Section 2 and Section 10 respectively, not a structural change.

## PDF generation — how, and one limitation to know about

This sandboxed environment's LibreOffice install is broken (confirmed via
strace — it fails even converting a plain `.txt` file), so the PDFs are
produced via a custom docx→HTML converter + WeasyPrint rather than Word's
own renderer — preserving real fonts, logo, RTL layout, bold formatting, the
running header/footer, and now the correct accent color, but rebuilding
page layout rather than using Word's own. **Recommendation: open the
`.docx` files in actual Word or Google Docs and re-export to PDF from there
for the version you actually send out** — the `.docx` files are built
directly from the original file's XML (fonts/logo/styles/theme inherited
verbatim, not recreated), so they're the higher-fidelity source; these PDFs
are a close approximation for review.

## Other things worth knowing

**Naming.** The Handbook is named the **Partner Handbook** (מדריך השותף),
not "Organization Protocols" — the original contract already uses a
different, capitalized, non-incorporated term ("the Source Protocol,"
Section 1) for HQ's internal compensation/tier framework, and reusing
"Protocols" would have collided with it.

**Pre-existing issue, not introduced here:** the *original* English
convenience translation has its own internal lettering drift in Section 8 —
harmless since Hebrew governs, worth a look if the English copy is ever
relied on directly.

## Still open

1. **Git push.** Commits are local only. Given the confidentiality notice
   above, pushing to the shared repo needs an explicit yes — asked
   repeatedly, still open.
2. **Dispute-resolution/arbitration phrasing (Section 15 / Contract 4.2).**
   Flagged early on as wanting a change; specifics never given, so it's
   still just a pointer rather than a guess at new wording.
3. **English rebuild.** Needs the same treatment as `_HE`.
4. **The two gap-fills** (subcontracting procedure, data-compliance
   disclaimer) — not in the current Handbook; say if you want them added
   back (see Completeness section above).

## Recommended next step

This was restructured by an AI agent, not a lawyer. Given real money
(₪100,000+ per breach), real international partners, and jurisdiction-
specific annexes are involved, **have an Israeli-licensed attorney review
both documents — especially the compensation clause and the Handbook
incorporation-by-reference mechanism — before circulating them for
signature.**
