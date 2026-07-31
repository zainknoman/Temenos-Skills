# AA.EXTERNAL.SYSTEM — Table Schema

> Source: `INSERTS/I_F.AA.EXTERNAL.SYSTEM` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.EX.DESCRIPTION` | `AaExternalSystem_Description` |  |  |  |
| 2 | `AA.EX.FULL.DESCRIPTION` | `AaExternalSystem_FullDescription` |  |  |  |
| 3 | `AA.EX.RECORD.STATUS` | `AaExternalSystem_RecordStatus` | String |  |  |
| 4 | `AA.EX.CURR.NO` | `AaExternalSystem_CurrNo` | String |  |  |
| 5 | `AA.EX.INPUTTER` | `AaExternalSystem_Inputter` |  |  |  |
| 6 | `AA.EX.DATE.TIME` | `AaExternalSystem_DateTime` |  |  |  |
| 7 | `AA.EX.AUTHORISER` | `AaExternalSystem_Authoriser` | String |  |  |
| 8 | `AA.EX.CO.CODE` | `AaExternalSystem_CoCode` | String |  |  |
| 9 | `AA.EX.DEPT.CODE` | `AaExternalSystem_DeptCode` | String |  |  |
| 10 | `AA.EX.AUDITOR.CODE` | `AaExternalSystem_AuditorCode` | String |  |  |
| 11 | `AA.EX.AUDIT.DATE.TIME` | `AaExternalSystem_AuditDateTime` | String |  |  |
