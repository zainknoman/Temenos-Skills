---
name: infobasic
description: >
  Write, review, and debug Temenos T24/Transact Infobasic (jBASE BASIC) routines.
  Covers: VVR/VIR/VAR/VCRR version routines, NoFile enquiry, DE conversion, AA
  calculation/getter/check subroutines, AA property templates, service routines,
  batch programs. Includes T24 standards, naming conventions, dynamic arrays
  (@AM/@VM/@SM), framework APIs (AA.Framework, AA.Interest, AA.PaymentSchedule,
  AC.Fees, EB.API, EB.DataAccess, EB.SystemTables, EB.Reports), legacy CALL APIs
  (OPF/F.READ/F.WRITE/EB.READLIST), error handling (STORE.END.ERROR, setE, V$ERROR),
  banking scenarios (FT, interest, dormancy, OFS, AA arrangements).
  Triggers: Infobasic, jBASE BASIC, T24 customization, VVR, VIR, VAR, NoFile enquiry,
  DE conversion, AA calculation, SUBROUTINE, GOSUB, $INSERT I_COMMON, $USING,
  $PACKAGE, CALL OPF, CALL F.READ, STORE.END.ERROR, EB.SystemTables, AA.Framework.
---

# Infobasic (jBASE BASIC) for Temenos T24/Transact

## Reference Files

Load the appropriate reference file(s) for the task at hand:

| File | When to load |
|------|-------------|
| [references/language.md](references/language.md) | Syntax, operators, dynamic arrays, file I/O, date functions, string functions |
| [references/routine-types.md](references/routine-types.md) | Complete templates for every routine type with real code patterns |
| [references/apis.md](references/apis.md) | Full API reference: AA.Framework, AA.Interest, AC.Fees, EB.*, legacy CALL APIs |
| [references/standards.md](references/standards.md) | Naming conventions, file header, modification history, comment style, review checklist |

**For writing new code**: load routine-types.md + apis.md  
**For reviewing existing code**: load standards.md + routine-types.md  
**For debugging**: load language.md + apis.md  
**For a quick question**: answer inline without loading files if the answer is clear

## Workflow

### Writing a New Routine

1. Identify the routine type (see table in routine-types.md)
2. Choose the right template from routine-types.md
3. Apply naming conventions from standards.md
4. Use the correct API style ($USING package APIs vs legacy $INSERT CALL APIs) - check which T24 release/style the project uses
5. Emit complete, compilable code with the ValidationCode header block

### Reviewing Existing Code

1. Check file header (ValidationCode block present)
2. Check $PACKAGE and $USING declarations
3. Verify GOSUB structure with region markers
4. Verify error-handling style is consistent
5. Check naming conventions (module prefix, variable prefixes)
6. Report violations using the checklist in standards.md

### Debugging

1. Identify the routine type to understand which framework variables are in scope
2. Check $INSERT / $USING imports - missing inserts cause "undefined variable" errors
3. Verify dynamic array addressing syntax (<FM,VM,SM>)
4. Verify CALL parameter order matches the called subroutine signature
5. Check ICONV/OCONV format codes for date conversion issues

---

## Multivalue Field Detection from JAR Structure

When `jar\com\temenos\t24\api\Record\<ApplicationName>\` contains **more than one** `.java` or `.class` file:

| Files in folder | Meaning |
|----------------|---------|
| `<AppNameCamelCase>Record.java` + `.class` only | Scalar record — all fields are single-value |
| Primary `<AppNameCamelCase>Record.java` **plus** other `*Class.java`/`.class` files | The extra `*Class` files are **multivalue group classes** — each maps to a multivalue T24 field |

**Example:** `AA.ARR.ACCOUNT` folder contains `AaArrAccountRecord.java`, `AltIdTypeClass.java`, `PostingRestrictClass.java`  
→ the fields corresponding to `AltIdTypeClass` and `PostingRestrictClass` are multivalue — code them with MV array syntax.

**Rule: every non-primary class in that folder = a multivalue field. Never read or write it as a scalar.**

### Separators

| Constant | CHAR | Level |
|----------|------|-------|
| `@FM` | 254 | Field (attribute) |
| `@VM` | 253 | Multivalue |
| `@SM` | 252 | Sub-value |

### Read MV field (FOR/NEXT + DCOUNT)

```
    lvMvCount = DCOUNT(lvRecord<FIELD.POS>, @VM)
    FOR lvI = 1 TO lvMvCount
        lvMvValue = lvRecord<FIELD.POS, lvI>
        * process lvMvValue
    NEXT lvI
```

### Guard empty MV field before loop

```
    IF lvRecord<FIELD.POS> NE '' THEN
        lvMvCount = DCOUNT(lvRecord<FIELD.POS>, @VM)
        FOR lvI = 1 TO lvMvCount
            lvMvValue = lvRecord<FIELD.POS, lvI>
        NEXT lvI
    END
```

### Write MV values

```
    FOR lvI = 1 TO lvItemCount
        lvRecord<FIELD.POS, lvI> = lvValues<lvI>
    NEXT lvI
```

### Read MV with sub-values (SV — inner class has multiple sub-fields)

```
    lvMvCount = DCOUNT(lvRecord<FIELD.POS>, @VM)
    FOR lvI = 1 TO lvMvCount
        lvSvCount = DCOUNT(lvRecord<FIELD.POS, lvI>, @SM)
        FOR lvJ = 1 TO lvSvCount
            lvSvValue = lvRecord<FIELD.POS, lvI, lvJ>
        NEXT lvJ
    NEXT lvI
```

### Add new MV occurrence

```
    lvRecord = INSERT(lvRecord, FIELD.POS, lvMvCount + 1, 0, lvNewValue)
```

### Delete MV occurrence

```
    DEL lvRecord<FIELD.POS, lvI>
```

### Naming conventions for MV loops

| Variable | Purpose |
|----------|---------|
| `lvMvCount` | total MV occurrences (`DCOUNT(..., @VM)`) |
| `lvI` | outer MV loop index (1-based) |
| `lvJ` | inner SV loop index (1-based) |
| `lvMvValue` | current MV value inside loop |
