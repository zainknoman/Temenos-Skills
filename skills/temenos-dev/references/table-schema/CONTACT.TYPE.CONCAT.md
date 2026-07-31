# CONTACT.TYPE.CONCAT — Table Schema

> Source: `INSERTS/I_F.CONTACT.TYPE.CONCAT` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CTC.CONTACT.TYP.PARAM` | `ContactTypeConcat_ContactTypParam` | TField |  | Identifies the records created for the particular type (phone,mobile,email) in CONTACT.TYPE.PARAMETER. |
| 2 | `ST.CTC.RECORD.STATUS` | `ContactTypeConcat_RecordStatus` | String |  |  |
| 3 | `ST.CTC.CURR.NO` | `ContactTypeConcat_CurrNo` | String |  |  |
| 4 | `ST.CTC.INPUTTER` | `ContactTypeConcat_Inputter` |  |  |  |
| 5 | `ST.CTC.DATE.TIME` | `ContactTypeConcat_DateTime` |  |  |  |
| 6 | `ST.CTC.AUTHORISER` | `ContactTypeConcat_Authoriser` | String |  |  |
| 7 | `ST.CTC.CO.CODE` | `ContactTypeConcat_CoCode` | String |  |  |
| 8 | `ST.CTC.DEPT.CODE` | `ContactTypeConcat_DeptCode` | String |  |  |
| 9 | `ST.CTC.AUDITOR.CODE` | `ContactTypeConcat_AuditorCode` | String |  |  |
| 10 | `ST.CTC.AUDIT.DATE.TIME` | `ContactTypeConcat_AuditDateTime` | String |  |  |
