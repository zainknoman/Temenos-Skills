# RD.PARAMETER — Table Schema

> Source: `INSERTS/I_F.RD.PARAMETER` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.PARM.VALIDATE.BIC` | `RdParameter_ValidateBic` | TField |  | The field will indicates if BICs should be validated against the directory or just its format should bevalidated. Yes - validate against the directory. No - it wont validate the BIC against the directory. Validation Rules: YES or NO field. Default value is NO. |
| 2 | `RD.PARM.REFERENCE.DATA` | `RdParameter_ReferenceData` | TField |  | Indicates if RD is the main reference data checked by the legacy BIC validation routine. Yes - the RD module will be used as the main reference data. Validation Rules: YES or NO field. Default value is YES. |
| 3 | `RD.PARM.RESERVED.5` | `RdParameter_Reserved5` |  |  |  |
| 4 | `RD.PARM.RESERVED.4` | `RdParameter_Reserved4` |  |  |  |
| 5 | `RD.PARM.RESERVED.3` | `RdParameter_Reserved3` |  |  |  |
| 6 | `RD.PARM.RESERVED.2` | `RdParameter_Reserved2` | TField |  |  |
| 7 | `RD.PARM.RESERVED.1` | `RdParameter_Reserved1` | TField |  |  |
| 8 | `RD.PARM.LOCAL.REF` | `RdParameter_LocalRef` |  |  |  |
| 9 | `RD.PARM.OVERRIDE` | `RdParameter_Override` |  |  |  |
| 10 | `RD.PARM.RECORD.STATUS` | `RdParameter_RecordStatus` | String |  |  |
| 11 | `RD.PARM.CURR.NO` | `RdParameter_CurrNo` | String |  |  |
| 12 | `RD.PARM.INPUTTER` | `RdParameter_Inputter` |  |  |  |
| 13 | `RD.PARM.DATE.TIME` | `RdParameter_DateTime` |  |  |  |
| 14 | `RD.PARM.AUTHORISER` | `RdParameter_Authoriser` | String |  |  |
| 15 | `RD.PARM.CO.CODE` | `RdParameter_CoCode` | String |  |  |
| 16 | `RD.PARM.DEPT.CODE` | `RdParameter_DeptCode` | String |  |  |
| 17 | `RD.PARM.AUDITOR.CODE` | `RdParameter_AuditorCode` | String |  |  |
| 18 | `RD.PARM.AUDIT.DATE.TIME` | `RdParameter_AuditDateTime` | String |  |  |
