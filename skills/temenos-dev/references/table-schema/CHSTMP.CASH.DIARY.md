# CHSTMP.CASH.DIARY — Table Schema

> Source: `INSERTS/I_F.CHSTMP.CASH.DIARY` in `CHSTMP_SwissTaxStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CASHDIARY.DATE` | `ChstmpCashDiary_Date` |  |  |  |
| 2 | `CASHDIARY.TXN.ID` | `ChstmpCashDiary_TxnId` |  |  |  |
| 3 | `CASHDIARY.LOCAL.REF` | `ChstmpCashDiary_LocalRef` |  |  |  |
| 4 | `CASHDIARY.RESERVED.5` | `ChstmpCashDiary_Reserved5` | TField |  | Reserved field for future use |
| 5 | `CASHDIARY.RESERVED.4` | `ChstmpCashDiary_Reserved4` | TField |  | Reserved field for future use |
| 6 | `CASHDIARY.RESERVED.3` | `ChstmpCashDiary_Reserved3` | TField |  | Reserved field for future use |
| 7 | `CASHDIARY.RESERVED.2` | `ChstmpCashDiary_Reserved2` | TField |  | Reserved field for future use |
| 8 | `CASHDIARY.RESERVED.1` | `ChstmpCashDiary_Reserved1` | TField |  | Reserved field for future use |
