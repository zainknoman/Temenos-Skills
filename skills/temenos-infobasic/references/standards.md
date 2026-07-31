# Infobasic T24 Programming Standards

## File Header (ValidationCode Block)

Every .b source file MUST begin with this comment block:

```basic
* @ValidationCode : N/A
* @ValidationInfo : Timestamp         : DD MMM YYYY HH:MM:SS
* @ValidationInfo : Encoding          : Cp1252
* @ValidationInfo : User Name         : developer.name
* @ValidationInfo : Nb tests success  : N
* @ValidationInfo : Nb tests failure  : 0
* @ValidationInfo : Rating            : N/A
* @ValidationInfo : Coverage          : NNN/NNN (100.0%)
* @ValidationInfo : Strict flag       : true
* @ValidationInfo : Bypass GateKeeper : false
* @ValidationInfo : Compiler Version  : DEV_202109.20210814-0920
* @ValidationInfo : Copyright Temenos Headquarters SA 1993-2021. All rights reserved.
* <Rating>100</Rating>
```

Positive `<Rating>` means code passed validation. Negative = issues present.

---

## Modification History Format

Required in every routine, after the header:

```basic
*-----------------------------------------------------------------------------
* Modification History :
*
* DD/MM/YY - Task   : T-NNNNN
*             Defect : D-NNNNN      (or Enh : E-NNNNN)
*             Short description of the change made
*
* DD/MM/YY - Task   : T-NNNNN
*             Description of second change
*-----------------------------------------------------------------------------
```

---

## $PACKAGE and $USING vs $INSERT

### Modern DS Packager style (preferred for R20+):

```basic
$PACKAGE AA.PaymentSchedule           ;* declares this file's namespace
SUBROUTINE AA.MY.ROUTINE(param1, param2)
    $USING AA.Framework
    $USING AA.Interest
    $USING EB.API
    $USING EB.DataAccess
```

- `$PACKAGE` must be the first non-comment line
- `$USING` imports are inside the SUBROUTINE block, before any code
- Use dot-notation APIs, no CALL keyword

### Legacy classic style:

```basic
SUBROUTINE XX.MY.ROUTINE
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_F.MY.APPLICATION
```

- `$INSERT` inside SUBROUTINE block
- Use `CALL` for all T24 APIs

---

## GOSUB Region Structure

All code must be organized into named GOSUB regions with region markers:

```basic
*** <region name= Initialise>
*** <desc>Initialize variables and open files</desc>
Initialise:
    VAR = ""
RETURN
*** </region>
*-----------------------------------------------------------------------------
*** <region name= MainProcess>
*** <desc>Core business logic</desc>
MainProcess:
    ;* logic
RETURN
*** </region>
```

- Labels at column 0 (no indentation)
- Code inside: 4-space indentation
- RETURN at column 0 or 4-space indent (be consistent within a file)
- Separator lines: `*-----------------------------------------------------------------------------`

---

## Comment Standards

```basic
* Leading asterisk: file-level/block comments
;* Semicolon-asterisk: inline comments (preferred for inline)

*-----------------------------------------------------------------------------
* JavaDoc-style for subroutine docs
* @param  Input1    Description of input parameter
* @return Output1   Description of return value
* @author user@temenos.com
* @class  AA.PaymentSchedule
* @stereotype subroutine
*-----------------------------------------------------------------------------
```

**Do NOT** use multi-line comment blocks for trivial things. Comments explain WHY, not WHAT.

---

## Naming Conventions

### Module Prefixes

| Prefix | Module |
|--------|--------|
| `EB` | Core Enterprise Banking framework |
| `AA` | Arrangements Architecture (lending/deposits) |
| `AC` | Accounts / Soft Accounting |
| `AO` | AA Origination |
| `AF` | AA Framework (property templates) |
| `FT` | Funds Transfer |
| `SC` | Securities |
| `LD` | Loans and Deposits |
| `MM` | Money Market |
| `MG` | Mortgage |
| `SL` | Syndicated Loans |
| `DW` | Data Warehouse export |
| `DE` | Document Engine / SWIFT |
| `OR` | Order Management |
| `ST` | System Tables / Config |
| `CUS` | Customer |
| `XX` | Generic example / sample prefix |
| `BAB`, `VIR`, `VVR`, `VAR` | Custom bank prefix patterns |

### Routine Type Suffixes / Infixes

| Pattern | Meaning |
|---------|---------|
| `*.VVR.*` | Version Validate Record |
| `*.VIR.*` | Version Input Record |
| `*.VAR.*` | Version Authorise Record |
| `*.VCRR.*` | Version Create Record |
| `*.V.APPLICATION` | DS Packager field validation |
| `*.E.NOFILE.*` | NoFile Enquiry |
| `*.DE.CONV.*` | Display Engine conversion |
| `*.DE.MAP.*` | Display Engine mapping |
| `*.CALC.*` | Calculation subroutine |
| `*.GET.*` | Getter (read data) |
| `*.CHECK.*` | Check/validation subroutine |
| `*.LOCAL.*` | Local override / bank customization |
| `*.CUSTOM.*` | Custom business logic |
| `*.ARR.TC.*` | Arrangement Term Condition property template |
| `*.PRD.CAT.TC.*` | Product Catalogue Term Condition |
| `*.S.*` | Service routine |
| `*.C.*` | Called subroutine (utility) |
| `*.H.*` | Header / parameter table routine |
| `*.L.*` | Ledger / limit routine |

### Variable Naming (Legacy style)

| Prefix | Meaning |
|--------|---------|
| `FN.` | File Name string (e.g. `FN.ACCOUNT = 'F.ACCOUNT'`) |
| `F.` | File handle (e.g. `F.ACCOUNT = ''`) |
| `R.` | Record variable (e.g. `R.ACCOUNT`) |
| `E.` | Error from file operation (e.g. `E.ACCOUNT`) |
| `Y.` | Local working variable (e.g. `Y.TEMP.AMT`) |
| `V.` | Value extracted from record (e.g. `V.CUST`) |
| `FLD.` | Field position variable |
| `CNT.` | Counter variable |
| `TOT.` | Total variable |

Modern (CamelCase) style: `arrangementId`, `retError`, `rArrangement`, `weightedIntRate`.

---

## Error Handling Patterns

### In VVR (field-level validation)

```basic
ETEXT = 'ERROR.MESSAGE.KEY'   ;* message key from EB.ERROR, or literal text
AF = FIELD.POSITION.CONSTANT  ;* field number that has the error
AV = 1                        ;* multi-value position (default 1)
CALL STORE.END.ERROR          ;* posts error and stops field processing
```

### In VIR/VIR (record-level validation)

```basic
ETEXT = 'INVALID.ACCOUNT':FM:ACCOUNT.ID   ;* FM-separated params after message key
AF = MY.APP.CREDIT.ACCT                   ;* highlight specific field
CALL STORE.END.ERROR
```

### Override Warning (instead of hard error)

```basic
TEXT = 'AMOUNT.EXCEEDS.RECOMMENDED.LIMIT'
CALL STORE.OVERRIDE(CURR.NO)    ;* CURR.NO = DCOUNT(R.NEW(OVERRIDE.FIELD), @VM)
```

### In VAR (authorisation)

```basic
E = 'ERROR.MESSAGE'
MESSAGE = "ERROR"
V$ERROR = 1
```

### In DS Packager validation

```basic
EB.SystemTables.setE('Error message text')
```

### API error variable pattern

```basic
RET.ERR = ""
AA.Framework.GetArrangementConditions(ARR.ID, PROP.CLASS, PROP.ID, EFF.DATE, PROP.LIST, PROP.REC, RET.ERR)
IF RET.ERR THEN
    ;* handle error
END
```

### Guard-clause pattern (skip-flag)

```basic
CALC.ERR = ""
BEGIN CASE
    CASE NOT(ARRANGEMENT.ID)
        CALC.ERR = 1
    CASE NOT(INT.PROPERTY.ID)
        CALC.ERR = 1
END CASE
IF NOT(CALC.ERR) THEN
    GOSUB MAIN.PROCESS
END
```

---

## Code Review Checklist

### Structure
- [ ] File begins with `* @ValidationCode` header block
- [ ] `$PACKAGE` is first non-comment line (if DS Packager style)
- [ ] `$USING` / `$INSERT` declarations present and complete
- [ ] Modification history present and follows format
- [ ] Code organized into named GOSUB regions with `*** <region name= ...>` markers
- [ ] Main control flow calls GOSUB sections, no inline logic in the entry point
- [ ] Every GOSUB label at column 0 with colon; code indented 4 spaces
- [ ] `END` statement at bottom of file

### Naming
- [ ] Routine name follows module prefix conventions (EB/AA/FT/etc.)
- [ ] Variable names use correct prefix style (FN./F./R./E./Y. for legacy; CamelCase for modern)
- [ ] File handles opened before use with `CALL OPF` (legacy) or FRead (modern)

### Error Handling
- [ ] Error mechanism matches routine type (STORE.END.ERROR for VVR/VIR, V$ERROR for VAR, setE for DS Packager)
- [ ] File reads check error variable (`E.REC`, `READ.ERR`, or ELSE clause)
- [ ] Input parameters validated before use

### Dynamic Arrays
- [ ] `@FM` / `@VM` / `@SM` used (not hard-coded ASCII values)
- [ ] DCOUNT used for counting MV elements (not LEN)
- [ ] `<-1>` used for appending (not string concatenation)
- [ ] RAISE() called when reading AA condition records that store SM-delimited data as FM

### API Usage
- [ ] Correct API style for the project release ($INSERT legacy vs $USING modern)
- [ ] CALL parameter order matches subroutine signature
- [ ] AA.Framework getters used instead of direct COMMON variable access (modern style)
- [ ] EB.API.RoundAmount called after currency amount calculations

### Performance
- [ ] File handles opened once in Initialise, not inside loops
- [ ] CACHE.READ used for parameter/reference tables (not F.READ in loops)
- [ ] SELECT statements use indexed fields where possible

### Security
- [ ] No hard-coded user credentials in OFS message strings
- [ ] Amount comparisons use correct currency rounding before comparison
- [ ] Override not bypassed without proper authority check

---

## T24 Routine Lifecycle Summary

```
Input Stage:    VIR -> VVR (per field) -> display
Change Stage:   VIR -> VVR (per field) -> display
Auth Stage:     VAR -> display
After Commit:   VCRR
Enquiry:        E.NOFILE or direct file enquiry with DE.CONV conversions
AA Framework:   ArrangementActivity -> Property routines -> CALC/GET/CHECK
Service/Batch:  S. routines or PROGRAM blocks via EB.SERVICE scheduler
```
