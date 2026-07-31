# CAPL.H.AKCELERANT.SELECT.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.AKCELERANT.SELECT.PARAM` in `CAAKCL_AkcelerantInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AKCL.PARAM.EXTRACT.ALL` | `CaplHAkcelerantSelectParam_ExtractAll` | TField |  | Purpose of the field to indicate whether the extract to be done as part of COB process.Allowed inputs YES/NOYES - Extract process will be done as part of COB processNO - Extract process will not be done as part of COB process |
| 2 | `AKCL.PARAM.USE.FILE` | `CaplHAkcelerantSelectParam_UseFile` | TField |  | Field is used to validate the extract process to happen.Allowed Inputs: YES/NOValidation:If EXTRACT.ALL is YES, then USE.FILE to be NO. Else error is thrown to the user.Applcable only whe EXTRACT.ALL field is set to YES |
| 3 | `AKCL.PARAM.FILE.PATH` | `CaplHAkcelerantSelectParam_FilePath` | TField | Yes | Field to define the File name for account extractsValidation: Applcable only when USE.FILE is set to YES.When USE.FILE is set to YES, File name and file path is mandatory, else error will be thrown.Eg. .\ACCOUNT.OUT |
| 4 | `AKCL.PARAM.FILE.NAME` | `CaplHAkcelerantSelectParam_FileName` | TField | Yes | Field to define the File name for account extractsValidation: Applcable only when USE.FILE is set to YES.When USE.FILE is set to YES, File name and file path is mandatory, else error will be thrown.Eg. ACKLERANT.TXT |
| 5 | `AKCL.PARAM.EXC.INDUSTRY` | `CaplHAkcelerantSelectParam_ExcIndustry` |  |  |  |
| 6 | `AKCL.PARAM.AA.CLOSE.ACT` | `CaplHAkcelerantSelectParam_AaCloseAct` |  |  |  |
| 7 | `AKCL.PARAM.OFS.SOURCE` | `CaplHAkcelerantSelectParam_OfsSource` | TField |  | Field to store the OFS source data to be used for triggering account closure activity.Validation: record from OFS.SOURCE |
| 8 | `AKCL.PARAM.AAA.OFS.VERSION` | `CaplHAkcelerantSelectParam_AaaOfsVersion` | TField |  |  |
| 9 | `AKCL.PARAM.RESERVED.5` | `CaplHAkcelerantSelectParam_Reserved5` | TField |  |  |
| 10 | `AKCL.PARAM.LOCAL.REF` | `CaplHAkcelerantSelectParam_LocalRef` |  |  |  |
| 11 | `AKCL.PARAM.OVERRIDE` | `CaplHAkcelerantSelectParam_Override` |  |  |  |
| 12 | `AKCL.PARAM.RECORD.STATUS` | `CaplHAkcelerantSelectParam_RecordStatus` | String |  |  |
| 13 | `AKCL.PARAM.CURR.NO` | `CaplHAkcelerantSelectParam_CurrNo` | String |  |  |
| 14 | `AKCL.PARAM.INPUTTER` | `CaplHAkcelerantSelectParam_Inputter` |  |  |  |
| 15 | `AKCL.PARAM.DATE.TIME` | `CaplHAkcelerantSelectParam_DateTime` |  |  |  |
| 16 | `AKCL.PARAM.AUTHORISER` | `CaplHAkcelerantSelectParam_Authoriser` | String |  |  |
| 17 | `AKCL.PARAM.CO.CODE` | `CaplHAkcelerantSelectParam_CoCode` | String |  |  |
| 18 | `AKCL.PARAM.DEPT.CODE` | `CaplHAkcelerantSelectParam_DeptCode` | String |  |  |
| 19 | `AKCL.PARAM.AUDITOR.CODE` | `CaplHAkcelerantSelectParam_AuditorCode` | String |  |  |
| 20 | `AKCL.PARAM.AUDIT.DATE.TIME` | `CaplHAkcelerantSelectParam_AuditDateTime` | String |  |  |
