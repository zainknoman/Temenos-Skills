# MDAL.PARTY — Table Schema

> Source: `INSERTS/I_F.MDAL.PARTY` in `SE_MDACustomer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDALP.FIELD.NAME` | `Mdar_FieldName` |  |  |  |
| 2 | `MDALP.FIELD.VALUE` | `MDALP_FieldValue` |  |  |  |
| 3 | `MDALP.RECORD.STATUS` | `MDALP_RecordStatus` |  |  |  |
| 4 | `MDALP.CURR.NO` | `MDALP_CurrNo` |  |  |  |
| 5 | `MDALP.INPUTTER` | `MDALP_Inputter` |  |  |  |
| 6 | `MDALP.DATE.TIME` | `MDALP_DateTime` |  |  |  |
| 7 | `MDALP.AUTHORISER` | `MDALP_Authoriser` |  |  |  |
| 8 | `MDALP.CO.CODE` | `MDALP_CoCode` |  |  |  |
| 9 | `MDALP.DEPT.CODE` | `MDALP_DeptCode` |  |  |  |
| 10 | `MDALP.AUDITOR.CODE` | `MDALP_AuditorCode` |  |  |  |
| 11 | `MDALP.AUDIT.DATE.TIME` | `MDALP_AuditDateTime` |  |  |  |
