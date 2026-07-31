# CURRENCY.GROUP — Table Schema

> Source: `INSERTS/I_F.CURRENCY.GROUP` in `ST_CurrencyConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CURGP.DESCRIPTION` | `CurrencyGroup_Description` |  |  |  |
| 2 | `ST.CURGP.CURRENCY` | `CurrencyGroup_Currency` |  |  |  |
| 3 | `ST.CURGP.RESERVED05` | `CurrencyGroup_Reserved05` | TField |  |  |
| 4 | `ST.CURGP.RESERVED04` | `CurrencyGroup_Reserved04` | TField |  |  |
| 5 | `ST.CURGP.RESERVED03` | `CurrencyGroup_Reserved03` | TField |  |  |
| 6 | `ST.CURGP.RESERVED02` | `CurrencyGroup_Reserved02` | TField |  |  |
| 7 | `ST.CURGP.RESERVED01` | `CurrencyGroup_Reserved01` | TField |  |  |
| 8 | `ST.CURGP.LOCAL.REF` | `CurrencyGroup_LocalRef` |  |  |  |
| 9 | `ST.CURGP.OVERRIDE` | `CurrencyGroup_Override` |  |  |  |
| 10 | `ST.CURGP.RECORD.STATUS` | `CurrencyGroup_RecordStatus` | String |  |  |
| 11 | `ST.CURGP.CURR.NO` | `CurrencyGroup_CurrNo` | String |  |  |
| 12 | `ST.CURGP.INPUTTER` | `CurrencyGroup_Inputter` |  |  |  |
| 13 | `ST.CURGP.DATE.TIME` | `CurrencyGroup_DateTime` |  |  |  |
| 14 | `ST.CURGP.AUTHORISER` | `CurrencyGroup_Authoriser` | String |  |  |
| 15 | `ST.CURGP.CO.CODE` | `CurrencyGroup_CoCode` | String |  |  |
| 16 | `ST.CURGP.DEPT.CODE` | `CurrencyGroup_DeptCode` | String |  |  |
| 17 | `ST.CURGP.AUDITOR.CODE` | `CurrencyGroup_AuditorCode` | String |  |  |
| 18 | `ST.CURGP.AUDIT.DATE.TIME` | `CurrencyGroup_AuditDateTime` | String |  |  |
