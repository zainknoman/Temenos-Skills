# LC.ADVICE.TEXT — Table Schema

> Source: `INSERTS/I_F.LC.ADVICE.TEXT` in `LC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TF.AD.DOCUMENT.CODE` | `LcAdviceText_DocumentCode1` |  |  |  |
| 2 | `TF.AD.SHORT.DESC` | `LcAdviceText_ShortDesc` |  |  |  |
| 3 | `TF.AD.NARRATIVE` | `LcAdviceText_Narrative` |  |  |  |
| 4 | `TF.AD.RECORD.STATUS` | `LcAdviceText_RecordStatus` | String |  |  |
| 5 | `TF.AD.CURR.NO` | `LcAdviceText_CurrNo` | String |  |  |
| 6 | `TF.AD.INPUTTER` | `LcAdviceText_Inputter` |  |  |  |
| 7 | `TF.AD.DATE.TIME` | `LcAdviceText_DateTime` |  |  |  |
| 8 | `TF.AD.AUTHORISER` | `LcAdviceText_Authoriser` | String |  |  |
| 9 | `TF.AD.CO.CODE` | `LcAdviceText_CoCode` | String |  |  |
| 10 | `TF.AD.DEPT.CODE` | `LcAdviceText_DeptCode` | String |  |  |
| 11 | `TF.AD.AUDITOR.CODE` | `LcAdviceText_AuditorCode` | String |  |  |
| 12 | `TF.AD.AUDIT.DATE.TIME` | `LcAdviceText_AuditDateTime` | String |  |  |
