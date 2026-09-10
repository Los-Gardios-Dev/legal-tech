# Los Gardios Partner Program — Restructured Documents

**⚠️ Confidential — not covered by this repository's root MIT license.** These
are Los Gardios Group's real, filled-in partner-program legal documents, not
a generic Skills IL example. They should not be redistributed, forked, or
installed the way the sibling `israeli-*` skill folders are.

## Round 6 — design pass: spacing, real Table of Contents, first-person Contract, a completeness bugfix

Your last message bundled several distinct asks; here's what each one turned
into, plus one thing I found while implementing that wasn't on your list.

**1. Tier compensation split — verified against the actual text, you were
right.** You said you weren't sure the Handbook clearly covers "each layer
gets a fixed 20%, split equally among however many partners are actively
working that layer on that project." Section 6(ד) states exactly that:
*"הנתח המשוחרר לשכבה נתונה מתחלק שווה בשווה בין השותפים הפעילים המשובצים
לאותה שכבה באותה התקשרות"* — the share released to a given layer splits
equally among the partners actively assigned to that layer on that specific
engagement (2 people → 10% each; 5 → 4% each, exactly the self-balancing
dynamic you described). No change needed here — just confirming it's really
in there.

**2. Handbook still had a leftover fill-in block.** You were right again:
items after the org description were still the full party-ID block (name,
country, ID number, entity type, address, email, Discipline Group
checkboxes) — a straight duplicate of the Contract's own copy. Removed from
the Handbook; the Contract's copy is the only one left anywhere.

**3. Table of Contents — rebuilt, not patched.** What you were pointing at
("no design, something looks off about the positioning") is real: the
original document's own ToC has no page numbers and no dot leaders at all —
confirmed by inspecting its raw XML, there's no Word ToC field, just plain
text lines with two blank spacer paragraphs between every entry, which is
also most of what was reading as "excessive spacing." Rebuilt it from
scratch: real dot leaders, real page numbers (genuinely measured — rendered
the Handbook once, located the actual page each section lands on, then
rebaked those numbers into the final version, since this pipeline doesn't
have Word's own live-updating ToC field), one compact line per entry, and
the three stale entries for content that moved to the Contract (Annex D,
Annex C, Section 19) dropped.

**4. Handbook now reads like chapter dividers, not just headings.** Every
section heading is now a full-width purple banner in white text that starts
its own page — closer to the "partner-onboarding presentation" feel you
asked for than the previous thin rule-lines-above-and-below treatment.

**5. Contract: flat first-person clauses, light headers.** Rewrote every
operative clause in Sections 1-5 from third person ("השותף מתחייב...") to
first person ("הנני מתחייב...", "הנני מאשר...") per your three example
sentences — this is now genuinely "the partner's own commitments," not a
description of them. The five section headings stay (1./2./3./4./5., still
decimally numbered 1.1/1.2.../2.1/2.2... exactly like your dictation), but
they no longer get the Handbook's heavy banner treatment — just bold text
and a thin rule, no forced page break, so the Contract still reads as one
flat sequence rather than a multi-chapter document. That split (heavy
banners in the Handbook, light headers in the Contract) is my reading of
"don't need all the chapter headers/annexes/mess" — happy to adjust if you
meant something more literal, like dropping the section headers entirely
and running 1.1-5.3 as one unbroken numbered list.

**6. Stamp boxes enlarged; Annex D visually marked optional.** The
Organization/Partner stamp boxes at the signature page are now real boxes
(~2.7in × 0.85in) instead of a thin full-width strip. Annex D now renders
inside a distinct tan callout box with a gold border — your instinct was
right, and it turns out the original document's own Table of Contents
*already* labels it "(אופציונלי — למילוי רק במידת הצורך)" — I reused that
exact existing phrase rather than inventing new wording, just made it
visually impossible to miss.

**7. Marking clause polished.** Reworded to explicitly say "אני מודע/ת
במלואי להתחייבויותיי" (fully aware of my obligations) and commit "במלואן,
ללא יוצא מן הכלל ובאופן מוחלט" (fully, without exception, absolutely) —
closer to your suggested phrasing, still a first-person confirm-by-checkbox
clause right before the signature page.

**8. On "too many separate signature points":** looked at every signature
line in the Contract. Two are genuinely separate on purpose, not
redundancy — Annex C's banking-detail signoff and Annex D's power-of-attorney
signatures are different legal acts from the main signature (wrong banking
details or an unauthorized POA are real, distinct risks; keeping them as
their own explicit signoff is closer to standard practice, not less). I
didn't remove any signature line without checking what it actually covered
first — say if you want a specific one gone regardless.

**9. Bug I found while fixing the above, not on your list: Section
6(ט)/(י)/(יא) were missing from the Handbook entirely.** The original
document physically wedges Annex D *inside* Section 6, between sub-clauses
(ח) and (ט) — every earlier round's Annex D splice swept up those three real
Section 6 sub-clauses (expense/budget limits, tool costs, setoff and
recoupment) as if they were part of the POA annex. Net effect: they weren't
in the Handbook at all (even though this round's own new compensation
clause already cites "סעיף 6(יא)" — a dangling reference until now), and in
the Contract they sat, mislabeled, inside what's now a box saying "optional,
skip if not applicable" — which they are not. Fixed: 6(ט)-(יא) moved to the
Handbook (right after 6(ח), continuing the section's own lettering), and
Annex D in the Contract trimmed to the POA form itself.

## Final QA pass (4 parallel Haiku subagents, then critically reviewed)

Before calling this a final product, dispatched four independent review
agents in parallel (design/aesthetics, legal completeness/redundancy,
Hebrew phrasing, structural/psychological ordering) and then went through
every finding myself rather than applying them automatically — some were
solid, a few were mistaken, a couple would have contradicted your own
explicit instructions.

**Applied:**
- **Reordered Contract sections 3 and 4.** Compensation/damages now comes
  *after* termination & dispute resolution, not before — reading "here's
  how the relationship generally works and ends" before "here's the
  penalty for maliciously wrecking it" avoids the real ₪100,000 figure
  landing on the reader with no context first, which is exactly the
  "ambush" feeling you've asked this clause not to have since Round 4.
- **Moved the marking/acknowledgment clause** ("I have read and am bound by
  the Handbook") to *after* Annexes C and D, right before the signature
  page — it shouldn't ask a partner to attest they understood everything
  before the annexes even appear in front of them.
- A handful of small Hebrew wording fixes in the Handbook's new
  compensation clause and Contract 5.3 (grammatical number agreement,
  one genuinely ambiguous phrase, two redundant words) — none change
  meaning, all just clarity.

**Declined, with reasons:**
- Expanding Contract sections 3/4 (now termination and compensation) with
  more substantive detail — this is exactly what you asked to move *out*
  of the Contract and into the Handbook; adding it back would undo that.
- Several Hebrew "fixes" that turned out, on checking, to be wrong: e.g.
  one agent flagged "הימנו" as a typo for "ממנו" — it's actually correct,
  more formal Hebrew that matches the document's own register (and
  appears in verbatim original text elsewhere), not an error.
- A suggestion to reword one already-original, verbatim-preserved sentence
  in the Handbook — out of scope, since "maintain this exact document" is
  the standing instruction for anything that isn't newly drafted this
  round.

The completeness and design reviews came back clean (no missing content,
no contradictions between the Contract and Handbook, no visual defects
across all 7 Contract pages and 8 sampled Handbook pages) — reassuring,
but at this point expected given the extent of what's already been checked
in earlier rounds.

## Real bug the 4-agent review missed, caught by direct inspection instead

You spotted that the Handbook still had signature pages in it — worth being
upfront that the automated review above did **not** catch this; it took you
actually looking. Checked it directly and found three separate problems,
not just the one:

- **Section 19** (the main signature block — names, signature lines, date,
  organization/partner stamps) was in **both** the Handbook and the
  Contract. It only belongs in the Contract, since that's the document
  that's actually signed.
- **Annexes C and D** were also in both places, for the same reason —
  they're per-partner fillable forms (banking details, power of attorney),
  not shared reference material.
- **The individual side-letter block** (space for recording specific
  negotiated deviations, with its own two signature lines — originally
  Section 18(ז) in the source) was in the Handbook **only** — not in the
  Contract at all. That's arguably the more serious of the three: it's
  genuine signable content that had nowhere a partner could actually sign
  it.

Fixed: removed the first two from the Handbook entirely (they're already in
the Contract), and moved the side-letter block into the Contract, right
after Section 5, trimmed to 8 blank lines rather than the original's 25 for
the same page-density reason as the earlier pagination fix. The Handbook
now ends cleanly after Section 18's general provisions — no signature
content anywhere in it. Handbook dropped from 50 to 44 pages as a result;
Contract stayed at 7 (the added side-letter block was offset by removing
it being compact).

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
| `Los_Gardios_Partner_Agreement_HE.docx`/`.pdf` | The short, signed contract: party ID + flat first-person numbered clauses + Annexes C/D + signature page. | **8** (2 of them are the actual contract clauses — see breakdown below) |
| `Los_Gardios_Partner_Agreement_EN.docx`/`.pdf` | ⚠️ Stale — several rounds behind, do not use. | — |
| `Los_Gardios_Partner_Handbook_HE.docx`/`.pdf` | The original document minus its signing mechanics (Section 19, Annexes C/D, the side-letter block, the fill-in party-ID block — all Contract-only now) plus a real Table of Contents, repurposed as the incorporated-by-reference Handbook. | **45** (paginated like a book — see below) |
| `Los_Gardios_Partner_Handbook_EN.docx`/`.pdf` | ⚠️ Stale — several rounds behind, do not use. | — |

## Book-style formatting (this round)

Researched how contracts and handbooks are actually formatted professionally
before making these changes, per instruction, rather than guessing — see
Sources at the bottom. Three changes:

1. **Handbook: every major section now starts on its own fresh page**, with
   a bolder heading (a purple rule above and below, not just below) —
   matching the standard convention of clear chapter breaks in both
   contract and handbook design. This is why it grew from 38 to 50 pages:
   a section that only fills a third of a page still starts its neighbor on
   a clean new page rather than running straight into it, the same way a
   book's chapters do (this is a real design choice, not empty padding) —
   and it also lands within one page of the *original* 51-page document's
   own length, which is a good sign this matches its natural pagination
   rather than over-inflating it. The Table of Contents was already intact
   (this round's Handbook is the original document, ToC included).
2. **Contract: numbered sub-clauses (1.1, 1.2...) are now visibly indented**
   under their parent section, and each of the five sections has the same
   framed heading style as the Handbook's chapters — both are standard
   contract-drafting convention (decimal numbering plus indentation to show
   hierarchy).
3. **Removed repeated boilerplate.** The previous draft ended nearly half its
   sub-clauses with some variant of "as detailed in the Partner Handbook" —
   redundant, since clause 2.2 already establishes once that every Handbook
   provision binds the partner as if written into the Contract itself.
   Trimmed those down to a single specific cross-reference (by section
   number) only where it's genuinely useful for navigation, stated once
   per topic rather than tacked onto every sentence.

## The current architecture

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
numbered sections + the marking clause come to **2 pages** — tighter than
last time, since the boilerplate trim (above) actually shortened the text.
The remaining 5 pages are Annex C (Country Annex), Annex D (Financial Power
of Attorney), and the signature page — attachments, not contract prose, per
the earlier explicit instruction that C and D belong in the signed package.
If you'd rather those didn't count against the page target at all — e.g.
handed out as separate physical forms rather than part of the same PDF —
say so.

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
