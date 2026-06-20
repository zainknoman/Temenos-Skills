# Infobasic Claude Skill — Usage Guide

A Claude Code skill for writing, reviewing, and debugging Temenos T24/Transact
Infobasic (jBASE BASIC) routines. Built from 14 T24 reference PDFs and 3,323
real `.b` source files from this project directory.

---

## Skill Location

| Artifact | Path |
|----------|------|
| Skill folder | `C:\Users\Lenovo\.claude\skills\infobasic\` |
| Packaged file | `C:\Users\Lenovo\.claude\skills\infobasic\infobasic.skill` |

---

## Installation

The skill is already installed in your local Claude Code skills directory
(`C:\Users\Lenovo\.claude\skills\infobasic\`). No further setup is needed —
it activates automatically when you mention T24/Infobasic keywords.

To share the skill with another machine or team member, copy `infobasic.skill`
to their `~/.claude/skills/` directory (or `C:\Users\<name>\.claude\skills\`
on Windows) and extract it there.

---

## How It Auto-Triggers

The skill loads automatically when your prompt contains any of:

```
Infobasic   jBASE BASIC   T24 customization   VVR   VIR   VAR   VCRR
NoFile enquiry   DE conversion   AA calculation   SUBROUTINE   GOSUB
$INSERT I_COMMON   $USING   $PACKAGE   CALL OPF   CALL F.READ
STORE.END.ERROR   EB.SystemTables   AA.Framework   ETEXT   COMI
```

---

## Part 1 — Writing New Code

### Step 1: State what you need

Tell Claude the routine type, the T24 application/module, and the business requirement.

**Example prompts:**

```
Write a VVR routine for FUNDS.TRANSFER that checks the debit account currency
matches the transaction currency. Use $INSERT style.
```

```
Write a VIR routine for MY.APPLICATION that validates the credit account exists
and the amount does not exceed the customer's daily limit. Use DS Packager $USING style.
```

```
Write an AA calculation subroutine AA.CALC.PROFIT.SHARING that takes
ARRANGEMENT.ID and INT.PROPERTY.ID as inputs and returns TOTAL.PROFIT.
```

```
Write a NoFile enquiry subroutine AA.E.NOFILE.ACTIVE.ARRANGEMENTS that filters
by customerId and arrangementId selection criteria and returns arrangement status.
```

```
Write a DE conversion routine AA.DE.CONV.MATURITY.DATE that formats a raw
YYYYMMDD date field as DD/MM/YYYY for enquiry display.
```

```
Write a standalone batch PROGRAM that selects all records from F.MY.TABLE
and updates a status field, with error logging to a CSV file.
```

### Step 2: Specify the style if needed

If the project uses a specific T24 release style, say so:

- **Legacy style (pre-R20):** "Use `$INSERT I_COMMON` and `CALL` APIs"
- **Modern style (R20+ DS Packager):** "Use `$PACKAGE` and `$USING` APIs"

### Step 3: Review the generated code

Ask Claude to walk through the generated routine:

```
Explain what each GOSUB section does in the routine you just wrote.
```

```
What T24 COMMON variables does this routine rely on and where do they come from?
```

---

## Part 2 — Code Review

### Step 1: Paste the code

Copy the content of a `.b` file and paste it into the prompt:

```
Review this Infobasic routine for T24 standards compliance:

[paste code here]
```

### Step 2: Ask for a specific type of review

**Standards compliance:**
```
Review this .b file against T24 programming standards — check the ValidationCode
header, $PACKAGE/$USING declarations, GOSUB region markers, modification history
format, and naming conventions.
```

**Logic review:**
```
Review this VVR routine for correctness. Does it handle all V$FUNCTION stages
correctly? Is the error handling pattern right for a VVR?
```

**Security review:**
```
Review this routine for security issues — are amounts rounded before comparison,
are overrides implemented with proper authority checks, any hard-coded credentials?
```

**Performance review:**
```
Review this routine for performance — are file handles opened inside loops,
are CACHE.READ used for parameter tables, are SELECT statements using indexed fields?
```

**API usage review:**
```
Review the API calls in this routine. Are the parameter orders correct?
Is the right style used ($INSERT vs $USING)?
```

### Step 3: Get a fix for a specific issue

```
The VVR routine I pasted uses STORE.END.ERROR but the stage check is missing.
Fix it to skip processing when V$FUNCTION is "A" or "D".
```

---

## Part 3 — Debugging

### Step 1: Describe the symptom

```
This VVR routine is not firing when the CREDIT.ACCT.NO field changes.
What could be wrong?
```

```
This AA calculation subroutine returns CALC.ERR = 1 even when all inputs
are provided. How do I debug this?
```

### Step 2: Paste the failing code with the error

```
This routine throws a T24 compilation error. Here is the code:
[paste code]

Error: "Undefined variable R.ACCOUNT"
```

```
This NoFile enquiry returns no rows. The DAS selection logic is:
[paste code section]

The TABLE.NAME is AA.ARRANGEMENT.ACTIVITY and the filter is by masterArrangementId.
What is wrong?
```

### Step 3: Ask for specific debugging guidance

```
What $INSERT file provides the R.NEW() and R.OLD() variables for a classic-style
VVR routine?
```

```
In a VVR routine, what is the difference between R.OLD, R.NEW, and R.NEW.LAST?
```

```
Why does RAISE() need to be called after AA.Framework.GetArrangementConditions?
```

---

## Part 4 — Quick Reference Questions

Ask any Infobasic or T24 question directly:

```
What is the correct parameter order for CALL EXCHRATE?
```

```
How do I count multi-values in a dynamic array field?
```

```
What is the difference between LOCATE and FIND in jBASE BASIC?
```

```
How do I convert a YYYYMMDD date to DD/MM/YYYY display format in Infobasic?
```

```
What COMMON variables are available in a VVR routine and where do they come from?
```

```
How do I append a new multi-value to a field in a dynamic array?
```

```
What is the correct way to build and send an OFS message to authorise a transaction?
```

---

## Part 5 — Generating Code from a Development Requirement

Paste a business/technical requirement and ask Claude to generate the full routine:

```
Requirement:
- Application: FUNDS.TRANSFER
- Routine type: VIR (runs on Input and Change)
- Business rule: If the transaction amount exceeds USD 10,000 and the debit
  customer's sector is "RETAIL", the transaction must be referred for approval.
  This should post a T24 override, not a hard error.
- Style: $INSERT legacy style

Generate the complete Infobasic VIR routine.
```

---

## Skill File Structure

```
C:\Users\Lenovo\.claude\skills\infobasic\
├── SKILL.md                        Main skill definition and workflow
└── references\
    ├── language.md                 jBASE BASIC syntax, dynamic arrays, date/string functions
    ├── routine-types.md            Complete templates for every T24 routine type
    ├── apis.md                     Full API reference (legacy CALL + modern $USING)
    └── standards.md                Naming conventions, file header, review checklist
```

---

## Routine Type Cheat Sheet

| Routine Type | When it runs | Error mechanism |
|---|---|---|
| `VVR` | Every field change (per keystroke) | `ETEXT` + `CALL STORE.END.ERROR` |
| `VIR` | Once on Input or Change | `ETEXT` + `AF` + `CALL STORE.END.ERROR` |
| `VAR` | On Authorise | `E` + `V$ERROR = 1` |
| `VCRR` | After record committed | Side effects only |
| `V.APPLICATION` (DS Packager) | Field validation | `EB.SystemTables.setE('msg')` |
| `E.NOFILE.*` | Enquiry with no file | Populate `finalArray` |
| `DE.CONV.*` | Enquiry column display | Set `OutValue` |
| `AA.CALC.*` | AA framework calculation | Return error param |
| `AA.GET.*` | AA framework data read | Return error param |
| `*.S.*` | Background service | EB.Service APIs |
| `PROGRAM` | Standalone batch | `CRT` / log file |

---

## Common Variable Quick Reference (VVR/VIR context)

| Variable | Meaning |
|----------|---------|
| `AF` | Field number that triggered the routine |
| `AV` | Multi-value position within that field |
| `COMI` | New value being committed to the field |
| `V$FUNCTION` | `I`=Input `C`=Change `A`=Auth `D`=Delete `R`=Reverse |
| `TODAY` | Current date as YYYYMMDD |
| `LCCY` | Local currency code |
| `LNGG` | Current language number |
| `R.NEW(field)` | Current new value of a field |
| `R.OLD(field)` | Previous authorised value of a field |
| `PGM.VERSION` | Version suffix, e.g. `,CC` |
| `ETEXT` | Error message key/text for STORE.END.ERROR |
| `TEXT` | Override message text for STORE.OVERRIDE |

---

*Skill built 2026-06-18 from 14 T24 reference PDFs and 3,323 Infobasic .b source files.*
