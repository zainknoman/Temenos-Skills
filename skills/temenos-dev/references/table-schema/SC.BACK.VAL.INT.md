# SC.BACK.VAL.INT — Table Schema

> Source: `INSERTS/I_F.SC.BACK.VAL.INT` in `EW_Integration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.BVI.CO.CODE` | `ScBackValInt_CoCode` | String |  | This field holds Company code to which the Account belongs |
| 2 | `SC.BVI.CURRENCY` | `ScBackValInt_Currency` | TField |  | This field holds the currency of the Account |
| 3 | `SC.BVI.DATE` | `ScBackValInt_Date` |  |  |  |
| 4 | `SC.BVI.FO.VALIDITY.DATE` | `ScBackValInt_FoValidityDate` |  |  |  |
| 5 | `SC.BVI.BALANCE` | `ScBackValInt_Balance` |  |  |  |
| 6 | `SC.BVI.ACCRUED.INTEREST` | `ScBackValInt_AccruedInterest` |  |  |  |
| 7 | `SC.BVI.HOLIDAY` | `ScBackValInt_Holiday` |  |  |  |
