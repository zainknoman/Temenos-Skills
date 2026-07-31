# CALEND.NPL.CUST.PROPG.WRK — Table Schema

> Source: `INSERTS/I_F.CALEND.NPL.CUST.PROPG.WRK` in `CALEND_NonPerformingLoan.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NPL.PG.ACTION` | `CalendNplCustPropgWrk_Action` |  |  |  |
| 2 | `NPL.PG.RESERVED.5` | `CalendNplCustPropgWrk_Reserved5` | TField |  |  |
| 3 | `NPL.PG.RESERVED.4` | `CalendNplCustPropgWrk_Reserved4` | TField |  |  |
| 4 | `NPL.PG.RESERVED.3` | `CalendNplCustPropgWrk_Reserved3` | TField |  |  |
| 5 | `NPL.PG.RESERVED.2` | `CalendNplCustPropgWrk_Reserved2` | TField |  |  |
| 6 | `NPL.PG.RESERVED.1` | `CalendNplCustPropgWrk_Reserved1` | TField |  |  |
