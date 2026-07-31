# MDAL.MARKET — Table Schema

> Source: `INSERTS/I_F.MDAL.MARKET` in `SE_MDAMarketData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDALM.FIELD.NAME` | `MdalMarket_FieldName` |  |  |  |
| 2 | `MDALM.FIELD.VALUE` | `MdalMarket_FieldValue` |  |  |  |
| 3 | `MDALM.RECORD.STATUS` | `MdalMarket_RecordStatus` | String |  |  |
| 4 | `MDALM.CURR.NO` | `MdalMarket_CurrNo` | String |  |  |
| 5 | `MDALM.INPUTTER` | `MdalMarket_Inputter` |  |  |  |
| 6 | `MDALM.DATE.TIME` | `MdalMarket_DateTime` |  |  |  |
| 7 | `MDALM.AUTHORISER` | `MdalMarket_Authoriser` | String |  |  |
| 8 | `MDALM.CO.CODE` | `MdalMarket_CoCode` | String |  |  |
| 9 | `MDALM.DEPT.CODE` | `MdalMarket_DeptCode` | String |  |  |
| 10 | `MDALM.AUDITOR.CODE` | `MdalMarket_AuditorCode` | String |  |  |
| 11 | `MDALM.AUDIT.DATE.TIME` | `MdalMarket_AuditDateTime` | String |  |  |
