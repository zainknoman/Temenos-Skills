# PASSWORD.RESET — Table Schema

> Source: `INSERTS/I_F.PASSWORD.RESET` in `EB_Security.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.PWR.USER.PW.ATTEMPT` | `PasswordReset_UserPwAttempt` |  |  |  |
| 2 | `EB.PWR.USER.ATTEMPT` | `PasswordReset_UserAttempt` |  |  |  |
| 3 | `EB.PWR.NO.OF.ATTEMPTS` | `PasswordReset_NoOfAttempts` |  |  |  |
| 4 | `EB.PWR.USER.DEACT.PERD` | `PasswordReset_UserDeactPerd` |  |  |  |
| 5 | `EB.PWR.DEACTIV.PERIOD` | `PasswordReset_DeactivPeriod` |  |  |  |
| 6 | `EB.PWR.USER.RESET` | `PasswordReset_UserReset` |  |  |  |
| 7 | `EB.PWR.USER.PASSWORD` | `PasswordReset_UserPassword` |  |  |  |
| 8 | `EB.PWR.USER.PWD` | `PasswordReset_UserPwd` |  |  |  |
| 9 | `EB.PWR.USER.TYPE` | `PasswordReset_UserType` | TField |  | Represents the type of user for whom the Security administrator wants to reset the Password. The possible types are Bank user (INT) or External user (EXT). |
| 10 | `EB.PWR.RECORD.STATUS` | `PasswordReset_RecordStatus` | String |  |  |
| 11 | `EB.PWR.CURR.NO` | `PasswordReset_CurrNo` | String |  |  |
| 12 | `EB.PWR.INPUTTER` | `PasswordReset_Inputter` |  |  |  |
| 13 | `EB.PWR.DATE.TIME` | `PasswordReset_DateTime` |  |  |  |
| 14 | `EB.PWR.AUTHORISER` | `PasswordReset_Authoriser` | String |  |  |
| 15 | `EB.PWR.CO.CODE` | `PasswordReset_CoCode` | String |  |  |
| 16 | `EB.PWR.DEPT.CODE` | `PasswordReset_DeptCode` | String |  |  |
| 17 | `EB.PWR.AUDITOR.CODE` | `PasswordReset_AuditorCode` | String |  |  |
| 18 | `EB.PWR.AUDIT.DATE.TIME` | `PasswordReset_AuditDateTime` | String |  |  |
| 19 | `EB.PWR.LOCAL.REF` | `PasswordReset_LocalRef` |  |  |  |
