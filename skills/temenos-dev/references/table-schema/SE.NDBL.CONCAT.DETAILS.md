# SE.NDBL.CONCAT.DETAILS — Table Schema

> Source: `INSERTS/I_F.SE.NDBL.CONCAT.DETAILS` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NDL.CAT.NDBL.APPL.DETAILS` | `SeNdblConcatDetails_NdblApplDetails` | TField |  |  |
| 2 | `NDL.CAT.RECORD.STATUS` | `SeNdblConcatDetails_RecordStatus` | String |  |  |
| 3 | `NDL.CAT.CURR.NO` | `SeNdblConcatDetails_CurrNo` | String |  |  |
| 4 | `NDL.CAT.INPUTTER` | `SeNdblConcatDetails_Inputter` |  |  |  |
| 5 | `NDL.CAT.DATE.TIME` | `SeNdblConcatDetails_DateTime` |  |  |  |
| 6 | `NDL.CAT.AUTHORISER` | `SeNdblConcatDetails_Authoriser` | String |  |  |
| 7 | `NDL.CAT.CO.CODE` | `SeNdblConcatDetails_CoCode` | String |  |  |
| 8 | `NDL.CAT.DEPT.CODE` | `SeNdblConcatDetails_DeptCode` | String |  |  |
| 9 | `NDL.CAT.AUDITOR.CODE` | `SeNdblConcatDetails_AuditorCode` | String |  |  |
| 10 | `NDL.CAT.AUDIT.DATE.TIME` | `SeNdblConcatDetails_AuditDateTime` | String |  |  |
