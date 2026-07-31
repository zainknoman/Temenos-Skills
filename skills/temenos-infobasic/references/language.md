# Infobasic Language Reference

## Program Entry Points

```basic
PROGRAM MY.BATCH.PROGRAM          ;* standalone executable
SUBROUTINE MY.ROUTINE(P1, P2)     ;* called subroutine (no CALL keyword in modern style)
```

## Variables

- No declaration needed; dynamically typed (string/numeric context-sensitive)
- ALL.CAPS.WITH.DOTS = legacy T24 style; CamelCase = modern DS Packager/TAFJ style
- Special system variables (from I_COMMON): `TODAY` (YYYYMMDD), `LCCY`, `COMI`, `LNGG`, `COMI`, `AF`, `AV`, `V$FUNCTION`, `ETEXT`, `TEXT`, `MESSAGE`
- Record variables: `R.NEW`, `R.OLD`, `R.NEW.LAST` (active transaction record old/new values)

## Operators and Arithmetic

```basic
X = X + 1    ;* or X += 1  or  X++
X = X - 1    ;* or X -= 1  or  X--
X = X * 2    ;* or X *= 2
X = X / 2    ;* or X /= 2
VAR1 = "AB" : "CD"     ;* string concat -> "ABCD"
VAR1 := "EF"           ;* append -> "ABCDEF"
```

Comparison: `EQ NE LT LE GT GE` (same as `= <> < <= > >=`)  
Logic: `AND OR NOT()`  
Pattern match: `MATCHES "0N"` (N digits), `MATCHES "0A"` (N alpha), `MATCHES "..."` (literal)

## Control Flow

```basic
IF CONDITION THEN
    ;* statements
END ELSE
    ;* statements
END

BEGIN CASE
    CASE VAR EQ "A"
        ;* code
    CASE VAR EQ "B"
        ;* code
    CASE 1             ;* catch-all
        ;* default
END CASE

FOR I = 1 TO TOTAL
    IF DONE THEN BREAK
    IF SKIP.THIS THEN CONTINUE
NEXT I

LOOP
WHILE CONDITION      ;* pre-test (WHILE) or UNTIL (post-test)
    ;* body
REPEAT
```

## GOSUB (Internal Subroutines)

```basic
GOSUB INITIALISE
GOSUB MAIN.PROCESS
RETURN                 ;* ends main flow

INITIALISE:
    VAR = ""
RETURN

MAIN.PROCESS:
    ;* logic
RETURN
```

Labels are at column 0 with a colon. Code inside is indented 4 spaces.

## Dynamic Arrays and Delimiters

| Constant | ASCII | Meaning |
|----------|-------|---------|
| `@FM` / `@AM` | 254 | Field Mark - separates fields/attributes |
| `@VM` | 253 | Value Mark - separates multi-values |
| `@SM` | 252 | Sub-Value Mark |
| `@TM` | 251 | Text Mark |

```basic
;* Access syntax
ARRAY<field>               ;* field 1-based
ARRAY<field, multivalue>
ARRAY<field, multivalue, subvalue>
ARRAY<-1>                  ;* append new field
ARRAY<1,-1>                ;* append new MV in field 1

;* Count elements
DCOUNT(ARRAY, @FM)         ;* count FM-separated fields
DCOUNT(ARRAY, @VM)         ;* count MV within field 1
TOT = DCOUNT(LIST, @VM)

;* LOCATE - find value in a field
LOCATE VALUE IN ARRAY<FIELD, 1> SETTING POS THEN
    ;* found at POS
END ELSE
    ;* not found
END

;* LOCATE with sort order
LOCATE DATE IN ARRAY<FIELD, 1> BY 'AR' SETTING POS THEN ...

;* FIND - search all levels, returns FM/VM/SM position triplet
FIND "UNAUTH" IN activityStatus SETTING fmPos, vmPos, smPos THEN
    id = activityRef<fmPos, vmPos, smPos>
END

;* FINDSTR - substring search
FINDSTR MATCH.VALUE IN DATA SETTING Ap, Vp THEN ...

;* REMOVE - iterate dynamic list
LOOP
    REMOVE ITEM FROM LIST SETTING MARK   ;* MARK=1 more items, MARK=0 last
WHILE ITEM : MARK
    ;* process ITEM
REPEAT

;* RAISE / LOWER - change delimiter levels
R.TERM.AMOUNT = RAISE(PROPERTY.RECORD)  ;* @SM->@VM->@FM (expand)
LOWER.DATA    = LOWER(FULL.DATA)        ;* @FM->@VM->@SM (compress)

;* CONVERT
CONVERT @VM TO @SM IN linkedIds
CONVERT "," TO @FM IN RESULT
```

## String Functions

```basic
LEN(STR)                        ;* length
TRIM(STR)                       ;* trim whitespace
UPCASE(STR)                     ;* uppercase
DOWNCASE(STR)                   ;* lowercase
LEFT(STR, N)                    ;* left N chars
RIGHT(STR, N)                   ;* right N chars
STR[start, length]              ;* substring, 1-based
INDEX(STR, SUBSTR, OCC)         ;* position of Nth occurrence (0 = not found)
CHANGE(STR, OLD, NEW)           ;* replace all occurrences
FIELD(STR, DELIM, N)            ;* Nth token
FIELD(STR, DELIM, N, M)         ;* tokens N through M
FMT(VAR, "R%10")                ;* right-justify pad to 10 chars
FMT(VAR, "L%10")                ;* left-justify pad to 10 chars
SEQX(CHAR)                      ;* ASCII value of character
```

## Numeric Functions

```basic
ABS(X)
INT(X)                   ;* truncate to integer
MOD(X, Y)                ;* modulus
MAXIMUM(DYNARRAY)        ;* max across VM-separated values
MINIMUM(DYNARRAY)        ;* min across VM-separated values
```

## Date and Time

```basic
TODAY        ;* YYYYMMDD from I_COMMON (e.g. 20240115)
DATE()       ;* Julian day number
TIME()       ;* seconds since midnight
TIMEDATE()   ;* "HH:MM:SS DD MMM YYYY"

;* ICONV - external -> internal
ICONV("20240115", "D")     ;* YYYYMMDD -> Julian
ICONV(TODAY, 'DJ')         ;* YYYYMMDD -> days from T24 epoch (1967-12-31)

;* OCONV - internal -> external
OCONV(DATE(), 'D.E')       ;* Julian -> DD/MM/YYYY
OCONV(DATE(), 'D4E-')      ;* Julian -> DD/MM/YYYY with dashes
OCONV(TIME(), 'MTS')       ;* seconds -> HH:MM:SS

;* Date arithmetic
CALL CDT('PK', MY.DATE, '+30')           ;* add 30 calendar days (modifies MY.DATE)
CALL CDD('PK', START.DATE, END.DATE, CDAYS)   ;* CDAYS = count of days (type 'C')
EB.API.Cdt("", CHECK.DATE, "-1C")        ;* subtract 1 calendar day (modern API)

;* Julian arithmetic
J1 = ICONV(DATE1, 'DJ')
J2 = ICONV(DATE2, 'DJ')
DIFF = J2 - J1
```

## File I/O

```basic
;* Open file (legacy)
FN.ACCOUNT = 'F.ACCOUNT'
F.ACCOUNT = ''
CALL OPF(FN.ACCOUNT, F.ACCOUNT)

;* Read (legacy)
CALL F.READ(FN.ACCOUNT, ACCOUNT.ID, R.ACCOUNT, F.ACCOUNT, E.ACCOUNT)
IF E.ACCOUNT THEN RETURN   ;* not found or error

;* Read with CACHE (for reference/parameter tables)
CALL CACHE.READ('F.ASCII.VAL.TABLE', TABLE.ID, R.TABLE, READ.FAILED)

;* Write (legacy)
CALL F.WRITE(FN.FILE, RECORD.ID, R.RECORD)

;* Direct jBASE READ/WRITE
READ R.REC FROM F.FILE, KEY THEN
    ;* found
END ELSE
    ;* not found or: ELSE NULL
END
WRITE R.REC TO F.FILE, KEY

;* Modern DataAccess API
EB.DataAccess.FRead("F.AA.ARRANGEMENT", ARR.ID, R.REC, "", READ.ERR)

;* Select/list processing
SELECT.STMT = 'SELECT ' : FN.FILE : ' WITH CUSTOMER EQ ' : CUST.ID
LIST = ''
CALL EB.READLIST(SELECT.STMT, LIST, '', TOTAL, ERR)
FOR I = 1 TO TOTAL
    RECORD.ID = LIST<I>
    CALL F.READ(FN.FILE, RECORD.ID, R.REC, F.FILE, E.REC)
NEXT I

;* DAS selection (modern)
TABLE.NAME = "AA.ARRANGEMENT.ACTIVITY"
THE.LIST = DAS$STATUS.NAU
THE.ARGS<1> = masterArrangementId
EB.DataAccess.Das(TABLE.NAME, THE.LIST, THE.ARGS, '$NAU')

;* Sequential file write
OPENSEQ '&SAVEDLISTS&', 'MY.LOG.csv' TO LOG.PATH THEN
    CREATE LOG.PATH ELSE NULL
END
WRITESEQ FAIL.DATA TO LOG.PATH ELSE NULL

;* Dimensioned arrays
DIM RDetail(500)
MAT RDetail = ''
MATREAD RDetail FROM F.FILE, KEY ELSE RETURN
```

## OFS (Open Financial Services) Messaging

```basic
;* Build OFS message
APP.NAME = 'FUNDS.TRANSFER'
FUNC = 'A'                        ;* A=Authorise, I=Input, R=Reverse, D=Delete
OFS.HEADER = APP.NAME : ",/" : FUNC : "/PROCESS//0," : USER : "/" : PASS : "/" : COMP : ","
IF INDEX(TXN.ID, "/,", 1) THEN CONVERT "/," TO "^?" IN TXN.ID
OFS.MSG = OFS.HEADER : TXN.ID : ",FIELD:1:1=VALUE"

CALL OFS.CALL.BULK.MANAGER('GCS', OFS.MSG, RESPONSE, txnCommitted)

;* Parse response
PASS.FAIL = FIELD(FIELD(RESPONSE, ",", 1, 3), "/", 3)
IF PASS.FAIL[1,2] EQ "-1" THEN ;* failure
```

## Misc

```basic
NULL              ;* no-op (use in ELSE NULL pattern)
DEBUG             ;* breakpoint
CRT "Message"    ;* console output (development only)
ENCRYPT(VAL, "9", 2)
DECRYPT(VAL, "9", 2)
```
