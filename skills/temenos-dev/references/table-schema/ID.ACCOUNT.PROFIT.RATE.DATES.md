# ID.ACCOUNT.PROFIT.RATE.DATES — Table Schema

> Source: `INSERTS/I_F.ID.ACCOUNT.PROFIT.RATE.DATES` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IAPRD.DATES` | `IdAccountProfitRateDates_Dates` |  |  |  |
| 2 | `ID.IAPRD.RESERVED.3` | `IdAccountProfitRateDates_Reserved3` | TField |  |  |
| 3 | `ID.IAPRD.RESERVED.2` | `IdAccountProfitRateDates_Reserved2` | TField |  |  |
| 4 | `ID.IAPRD.RESERVED.1` | `IdAccountProfitRateDates_Reserved1` | TField |  |  |
