# Local Template Tables (THE.TEMPLATE / `Table.*` framework)

**Sources (authoritative only):** Temenos *Core Banking Programming Templates T3PRGT – R19*
(`docs/.../Design Studio/`, pp. 50–100); R23 JAR `EB_Template.jar`: `INSERTS/I_Table`,
`INSERTS/I_DataTypes`, the `TEMPLATE*_cl` method classes and `component_EB_Template`.
Proven skeleton in this repo: `tests/golden/infobasic-local-table/` (template
`templates/infobasic/local-table`).

**R25:** both routines need `$PACKAGE <Pkg>` and a `private method` entry in `<Pkg>.component`, or tCompile fails with `No component defined. $PACKAGE is mandatory` (R25's own `T24_BP/TEMPLATE.b` has `$PACKAGE EB.Template` before `SUBROUTINE`). R25's shipped `TEMPLATE.b` writes `Table.trigger = ''`, and the golden case follows it. That line is harmless because it sets nothing. `I_Table` declares the common as `Table.triggerField` in both R23 and R25 (R25 checked 2026-10-07; see the note under §1), so to **actually set** a trigger field use `Table.triggerField` / `EB.Template.setTableTriggerfield`. Two styles compile on R25 and are both valid:
- **TAFJ Infobasic** (`$INSERT I_Table`, `Table.* = ...`, `CALL Table.defineId/addFieldDefinition/...`) - `tests/golden/infobasic-local-table/`.
- **Componentised jBC** (`$USING EB.Template`: `EB.Template.setTableName(...)` etc., then `EB.Template.TableDefineid/TableAddfielddefinition/TableAddfield/TableSetauditposition()` as in R25 `T24_BP/TEMPLATE.FIELDS.b`) - `tests/golden/jbc-local-table/` (template `templates/jbc/local-table`).

## Method routines (life cycle)

The application name `<APP>` is the main routine; each method is a separate subroutine
`<APP>.<METHOD>`. Only the main routine and `.FIELDS` are mandatory. (Method classes present in
R23 `EB_Template.jar`: `TEMPLATE`, `TEMPLATE.INITIALISE`, `.FIELDS`, `.FUNCTION`, `.ID`,
`.RECORD`, `.VALIDATE`, `.OVERRIDE`, `.PROCESS`, `.AUTHORISE`.)

| Order | Method | Runs | Use it to |
|-------|--------|------|-----------|
| 1 | `<APP>.INITIALISE` | once, when the application is invoked | Set up commons, open files |
| 2 | `<APP>.FIELDS` | page pre-load / `EB.DEV.HELPER` | Define the ID and every field (mandatory) |
| 3 | `<APP>.FUNCTION` | function check | React to `V$FUNCTION` (prefer `Table.blockedFunctions`) |
| 4 | `<APP>.ID` | after the key is entered | Validate/format the key. `COMI` and `ID.NEW` hold it; report through `E` (an `EB.ERROR` id) |
| 5 | `<APP>.RECORD` | after `RECORD.READ`, before display | Default values, make fields no-input. `R.NEW`, `R.NEW.LAST`, `R.OLD` are loaded |
| 6 | `<APP>.VALIDATE` | on Validate/Commit | Errors: `ETEXT` + `AF`/`AV`/`AS` + `STORE.END.ERROR` |
| 7 | `<APP>.OVERRIDE` | on Commit | Warnings: `TEXT` + `STORE.OVERRIDE(CURR.NO)` (the guide's prose calls it `.OVERRIDES`) |
| 8 | `<APP>.PROCESS` | on Commit | Accounting, charges, limits; record status decided |
| 9 | `<APP>.AUTHORISE` | on Authorise | Post-authorisation processing |

`RECORD.READ` searches `$NAU` → live → `$HIS`. `$DEL` is never searched.

**Older (pre-`Table.*`) template family** (*T24 Programming Standards* pp. 31–32). You will meet
it in legacy code; do not use it for new tables. A single `TEMPLATE` program calls
`<APP>.FIELD.DEFINITIONS`, `<APP>.CHECK.FIELDS` (per-field checks, called when the N array has
`C` as its third element), `<APP>.CROSSVAL` (commit, re-runs check fields), `<APP>.OVERRIDE` and
`<APP>.ACCOUNTING` (sets up the `EB.ACCOUNTING` call). Fields are defined with the `F`/`N`/`T`
arrays and `ID.F`/`ID.N`/`ID.T`, and the last two fields are `XX.LOCAL.REF` and `XX.OVERRIDE`.
`TEMPLATE.L` is the live-only variant with field definitions inline. The rule in both styles:
"never modify the template control code".

## 1. Main routine (`<APP>`)

Every property is a variable in `COMMON /OBJECT.TEMPLATE/` (`I_Table`):

```basic
    SUBROUTINE EB.INSURANCE
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_Table
*-----------------------------------------------------------------------------
    Table.name = 'EB.INSURANCE'         ;* Full application name incl. product prefix
    Table.title = 'Insurance'           ;* Screen title
    Table.stereotype = 'H'              ;* H, U, L, T or W — see below
    Table.product = 'EB'                ;* Must be on EB.PRODUCT
    Table.subProduct = ''               ;* Must be on EB.SUB.PRODUCT
    Table.classification = 'FIN'        ;* INT, FIN or CUS — see below
    Table.systemClearFile = 'Y'         ;* As per FILE.CONTROL
    Table.relatedFiles = ''             ;* As per FILE.CONTROL
    Table.isPostClosingFile = ''        ;* As per FILE.CONTROL
    Table.equatePrefix = 'EB.INS'       ;* Prefix of every EQU generated into I_F.EB.INSURANCE
    Table.idPrefix = ''                 ;* Used by EB.FORMAT.ID
    Table.blockedFunctions = ''         ;* Space-delimited, e.g. 'V R' blocks Verify and Reverse
    Table.triggerField = ''             ;* Trigger field for OPERATION-style fields
    RETURN
END
```

> The R19 guide's sample and R25's shipped `TEMPLATE.b` write `Table.trigger = ''`. `I_Table` (R23 and R25) declares **`Table.triggerField`**,
> not `Table.trigger`. The two compile the same way, but `Table.trigger` is just a local variable
> that has no effect. Use `Table.triggerField` when you need a trigger field.

Componentised form (`$USING EB.Template`): setter names verified in R23 `component_EB_Template`.
They are `setTableName`, `setTableTitle`, `setTableStereotype`, `setTableProduct`,
`setTableSubproduct`, `setTableClassification`, `setTableSystemclearfile`, `setTableRelatedfiles`,
`setTableIspostclosingfile`, `setTableEquateprefix`, `setTableIdprefix`,
`setTableBlockedfunctions` and `setTableTriggerfield`.
`setTableField`, `setTableId`, `setTableDescription` and `setTableSysId` **do not exist**.

**Stereotype** (R19 guide pp. 17–18):

| Type | Kind | Files |
|------|------|-------|
| `H` | Application | Live, `$NAU`, `$HIS` (+ `$DEL` if configured) |
| `U` | Application | Live, `$NAU`, `$DEL` — no history |
| `L` | Display | Live only, non-inputtable (system-updated) |
| `T` | Display | Live only — concat files |
| `W` | Utility | Live only — Input, See and Verify functions (work file; Verify starts a process) |

**Classification:** `FIN` financial, usually not shared (one file per company mnemonic);
`CUS` static data shareable between companies; `INT` installation, mostly shared.
`CST`, `FTD`, `FTF`, `CCY`, `NOS` are reserved for core.

## 2. `.FIELDS`

```basic
    SUBROUTINE EB.INSURANCE.FIELDS
    $INSERT I_COMMON
    $INSERT I_EQUATE
    $INSERT I_DataTypes
*-----------------------------------------------------------------------------
    CALL Table.defineId('POLICY.ID', T24_String)
*-----------------------------------------------------------------------------
    CALL Table.addField('CUSTOMER.NO', T24_Customer, Field_Mandatory, '')
    CALL Field.setCheckFile('CUSTOMER')                    ;* applies to the field just added
    CALL Table.addField('CURRENCY', T24_String, Field_Mandatory, '')
    CALL Field.setCheckFile('CURRENCY')
    CALL Table.addAmountField('SUM.ASSURED', 'CURRENCY', Field_Mandatory, '')
    CALL Table.addField('START.DATE', T24_Date, '', '')
    CALL Field.setDefault(TODAY)
    CALL Table.addOptionsField('PAY.MODE', 'MONTHLY_ANNUAL', '', '')
    CALL Table.addYesNoField('SANCTION', '', '')
    CALL Table.addFieldWithEbLookup('POLICY.TYPE', 'INS.POLICY.TYPE', '')
    CALL Table.addField('XX<NOMINEE.NAME', T24_String, '', '')     ;* associated MV group
    CALL Table.addField('XX>NOMINEE.SHARE', T24_Numeric, '', '')
*-----------------------------------------------------------------------------
    CALL Table.addReservedField('RESERVED.3')
    CALL Table.addReservedField('RESERVED.2')
    CALL Table.addReservedField('RESERVED.1')
    CALL Table.addLocalReferenceField('')                  ;* mandatory for every application
    CALL Table.addStatementNumbersField('')                ;* only if it raises accounting
    CALL Table.addOverrideField                            ;* must sit immediately before the audit fields
*-----------------------------------------------------------------------------
    CALL Table.setAuditPosition                            ;* last — appends the 9 audit fields
    RETURN
END
```

### API (R19 guide; componentised names verified in R23 `component_EB_Template`)

| Legacy `CALL` | `$USING EB.Template` | Arguments |
|---------------|----------------------|-----------|
| `Table.defineId` | `TableDefineid` | `(idName, dataType)` |
| `Table.addField` | `TableAddfield` | `(fieldName, dataType, args, neighbour)` |
| `Table.addFieldDefinition` | `TableAddfielddefinition` | `(fieldName, fieldLength, fieldType, neighbour)` † |
| `Table.addAmountField` | `TableAddamountfield` | `(fieldName, currencyFieldName, args, neighbour)` — currency field or `LCCY` |
| `Table.addOptionsField` | `TableAddoptionsfield` | `(fieldName, options separated by '_', args, neighbour)` |
| `Table.addYesNoField` | `TableAddyesnofield` | `(fieldName, args, neighbour)` — holds `YES` or blank |
| `Table.addFieldWithEbLookup` | `TableAddfieldwitheblookup` | `(fieldName, EB.LOOKUP virtual table, neighbour)` |
| `Table.addVirtualTableField` | `TableAddvirtualtablefield` | `(fieldName, virtual table, args, neighbour)` |
| `Table.addReservedField` | `TableAddreservedfield` | `(name)` — names `RESERVED.n` |
| `Table.addLocalReferenceField` | `TableAddlocalreferencefield` | `(neighbour)` — creates `LOCAL.REF` |
| `Table.addDeliveryReferenceField` | `TableAdddeliveryreferencefield` | `(neighbour)` — `DELIVERY.REF` |
| `Table.addStatementNumbersField` | `TableAddstatementnumbersfield` | `(neighbour)` — `STMT.NOS` |
| `Table.addOverrideField` | `TableAddoverridefield` | none |
| `Table.setAuditPosition` | `TableSetauditposition` | none |
| `Table.setAttributeOnFields` | `TableSetattributeonfields` | `(attribute, fieldNumbers FM-list)` |
| `Field.setCheckFile` | `FieldSetcheckfile` | `(application)` |
| `Field.setDefault` | `FieldSetdefault` | `(value)` |

† Not described in the R19 guide. The signature comes from the parameter names compiled into
R23 `Table_addFieldDefinition_20_cl` (`fieldName, fieldLength, fieldType, neighbour`). The
golden case uses `('DESCRIPTION', '35', 'A', '')`. The guide names `fieldType` codes by their
`IN2` validation routine (`A` text, `ANT` account, `CUS` customer, `D` date, `FQU` frequency).
Prefer `Table.addField` with a `T24_*` type when one fits.

**Data types** (`I_DataTypes`, R23): `T24_String`, `T24_BigString`, `T24_Text`,
`T24_TextWide`, `T24_Numeric`, `T24_Date`, `T24_Portfolio`, `T24_Account`,
`T24_InternalAccount`, `T24_Customer`, `T24_Frequency`. There is **no** `T24_Amount` and no
`T24_Company`; use `Table.addAmountField` for amounts.
**Args** (comma-joined): `Field_Mandatory`, `Field_NoInput`, `Field_NoChange`, `Field_Unique`,
`Field_NoNulls`, `Field_AllowNegative`, `Field_NoCopy`.

### Field naming

| Name form | Meaning |
|-----------|---------|
| `NAME` | Single value. Max 18 characters, no spaces, may not start with `XX` |
| `XX.NAME` | Stand-alone multi-value |
| `XX.LL.NAME` | Language multi-value |
| `XX<A` … `XX-B` … `XX>C` | Associated multi-value set (start / middle / end) |
| `XX<A` + `XX>XX.B` | Two-field associated set whose second field is sub-valued |
| `XX-XX<A` … `XX>XX>B` | Sub-valued group nested in an MV group (as used in core `DL.DEFINE`) |

### Mandatory structure (R19 guide)

- Every application **must** have `LOCAL.REF` and a set of `RESERVED.n` fields. Reserved fields
  let you add fields later without changing the data layout.
- `STMT.NOS` (if present) precedes `OVERRIDE`. `OVERRIDE` sits **immediately** before the
  audit fields, otherwise override text lands in whatever field is there.
- `Table.setAuditPosition` appends `RECORD.STATUS, CURR.NO, INPUTTER, DATE.TIME, AUTHORISER,
  CO.CODE, DEPT.CODE, AUDITOR.CODE, AUDIT.DATE.TIME`. `L` files have no audit fields.

## 3. Method examples

`.ID` — validate the key (`COMI` / `ID.NEW` hold it):

```basic
    SUBROUTINE EB.INSURANCE.ID
    $INSERT I_COMMON
    $INSERT I_EQUATE
    IF LEN(ID.NEW) GT 16 THEN
        E = 'EB-INVALID.ID'                 ;* an EB.ERROR id, not literal text
    END
    RETURN
END
```

For generated keys set `Table.idPrefix`. `EB.FORMAT.ID` then formats `I`-function IDs as
`<prefix>YYDDDNNNNN` (Julian date + serial) before `.ID` runs.

`.VALIDATE` — errors:

```basic
    IF R.NEW(EB.INS.START.DATE) GT R.NEW(EB.INS.END.DATE) THEN
        AF = EB.INS.START.DATE
        ETEXT = 'EB-START.AFTER.END'
        CALL STORE.END.ERROR                 ;* once per error
    END
```

`.OVERRIDE` — warnings; `&` placeholders in the OVERRIDE record take values in order:

```basic
    TEXT = 'INS.VALIDITY.EXCEEDED':FM:R.NEW(EB.INS.CUSTOMER.NO):VM:Y.YEARS
    CURR.NO = DCOUNT(R.NEW(EB.INS.OVERRIDE), VM) + 1
    CALL STORE.OVERRIDE(CURR.NO)
```

Generate the artefacts with `EB.DEV.HELPER I <APP>`. Verifying that record creates
`PGM.FILE`, `FILE.CONTROL`, `STANDARD.SELECTION`, the `I_F.<APP>` insert and the database files.

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Fields defined in the main routine | Main routine sets `Table.*` properties only; fields go in `.FIELDS` |
| `Table.setAuditPosition` not last / `OVERRIDE` not just before it | Fix the order — see "Mandatory structure" |
| No `LOCAL.REF` / no reserved fields | Both are mandatory for every application |
| Reordering or deleting fields after go-live | Positions are stored data — rename a `RESERVED.n` instead |
| `T24_Amount`, `T24_Company` | Not in `I_DataTypes`; use `addAmountField` / `Field.setCheckFile('COMPANY')` |
| `EB.Template.setTableField(...)` | Does not exist — use `Table.addField` / `EB.Template.TableAddfield` in `.FIELDS` |
| Hard-coded message text in `E`/`ETEXT` | Use an `EB.ERROR` id |
