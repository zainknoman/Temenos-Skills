# AA.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.AA.DESCRIPTION` in `AA_ProductManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DSC.DESCRIPTION` | `AaDescription_Description` |  |  |  |
| 2 | `AA.DSC.FULL.DESCRIPTION` | `AaDescription_FullDescription` |  |  |  |
| 3 | `AA.DSC.RECORD.STATUS` | `AaDescription_RecordStatus` | String |  |  |
| 4 | `AA.DSC.CURR.NO` | `AaDescription_CurrNo` | String |  |  |
| 5 | `AA.DSC.INPUTTER` | `AaDescription_Inputter` |  |  |  |
| 6 | `AA.DSC.DATE.TIME` | `AaDescription_DateTime` |  |  |  |
| 7 | `AA.DSC.AUTHORISER` | `AaDescription_Authoriser` | String |  |  |
| 8 | `AA.DSC.CO.CODE` | `AaDescription_CoCode` | String |  |  |
| 9 | `AA.DSC.DEPT.CODE` | `AaDescription_DeptCode` | String |  |  |
| 10 | `AA.DSC.AUDITOR.CODE` | `AaDescription_AuditorCode` | String |  |  |
| 11 | `AA.DSC.AUDIT.DATE.TIME` | `AaDescription_AuditDateTime` | String |  |  |
