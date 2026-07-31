# AUBASE.ALT.ACCT.CURRENT.RANGE.INFO — Table Schema

> Source: `INSERTS/I_F.AUBASE.ALT.ACCT.CURRENT.RANGE.INFO` in `AUBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RANGE.INFO.RANGE.CONTENT` | `AubaseAltAcctCurrentRangeInfo_RangeContent` | TField |  | This is a system populated field. The number stored in this field would always fall within current range defined in the fields - AC.START.RANGE and AC.END.RANGE in the parameter table CMBASE.ALTERNATE.ID.PARAM The number in this field would begin or start with the number stored in AC.START.RANGE and gets incremented and updated by the system as and when a new arrangement gets created. The increment stops when the number reaches the number stored in AC.END.RANGE. Then the system moves to the start range of the next range that is defined in the parameter table CMBASE.ALTERNATE.ID.PARAM |
