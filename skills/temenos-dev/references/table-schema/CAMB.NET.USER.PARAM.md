# CAMB.NET.USER.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.NET.USER.PARAM` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NET.USR.USER.NAME` | `CambNetUserParam_UserName` | TField |  | This field used to define SIGN.ON.NAME to be used for posting the ATM/POS transaction.Eg: ATM.USER |
| 2 | `NET.USR.PASSWORD` | `CambNetUserParam_Password` | TField |  | This field is absolute now |
| 3 | `NET.USR.RECORD.STATUS` | `CambNetUserParam_RecordStatus` | String |  |  |
| 4 | `NET.USR.CURR.NO` | `CambNetUserParam_CurrNo` | String |  |  |
| 5 | `NET.USR.INPUTTER` | `CambNetUserParam_Inputter` |  |  |  |
| 6 | `NET.USR.DATE.TIME` | `CambNetUserParam_DateTime` |  |  |  |
| 7 | `NET.USR.AUTHORISER` | `CambNetUserParam_Authoriser` | String |  |  |
| 8 | `NET.USR.CO.CODE` | `CambNetUserParam_CoCode` | String |  |  |
| 9 | `NET.USR.DEPT.CODE` | `CambNetUserParam_DeptCode` | String |  |  |
| 10 | `NET.USR.AUDITOR.CODE` | `CambNetUserParam_AuditorCode` | String |  |  |
| 11 | `NET.USR.AUDIT.DATE.TIME` | `CambNetUserParam_AuditDateTime` | String |  |  |
