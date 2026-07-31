# INLEND.SFMS.IN.MSG.PARAM — Table Schema

> Source: `INSERTS/I_F.INLEND.SFMS.IN.MSG.PARAM` in `INSFMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.SFMS.PARM.EXCL.APPLN.TYPE` | `InlendSfmsInMsgParam_ExclApplnType` |  |  |  |
| 2 | `INLEND.SFMS.PARM.IN.MSG.PATH` | `InlendSfmsInMsgParam_InMsgPath` | TField |  | File path for where the incoming SFMS messgages will be placed |
| 3 | `INLEND.SFMS.PARM.BKUP.IN.MSG.PATH` | `InlendSfmsInMsgParam_BkupInMsgPath` | TField |  | Backup file path where the incoming SFMS messages will be saved after it gets processed |
| 4 | `INLEND.SFMS.PARM.MSG.STATUS` | `InlendSfmsInMsgParam_MsgStatus` | TField |  | SFMS process will only be taken place if incoming msg status is equal to the configured msg status |
| 5 | `INLEND.SFMS.PARM.LOCAL.REF` | `InlendSfmsInMsgParam_LocalRef` |  |  |  |
| 6 | `INLEND.SFMS.PARM.OVERRIDE` | `InlendSfmsInMsgParam_Override` |  |  |  |
| 7 | `INLEND.SFMS.PARM.RECORD.STATUS` | `InlendSfmsInMsgParam_RecordStatus` | String |  |  |
| 8 | `INLEND.SFMS.PARM.CURR.NO` | `InlendSfmsInMsgParam_CurrNo` | String |  |  |
| 9 | `INLEND.SFMS.PARM.INPUTTER` | `InlendSfmsInMsgParam_Inputter` |  |  |  |
| 10 | `INLEND.SFMS.PARM.DATE.TIME` | `InlendSfmsInMsgParam_DateTime` |  |  |  |
| 11 | `INLEND.SFMS.PARM.AUTHORISER` | `InlendSfmsInMsgParam_Authoriser` | String |  |  |
| 12 | `INLEND.SFMS.PARM.CO.CODE` | `InlendSfmsInMsgParam_CoCode` | String |  |  |
| 13 | `INLEND.SFMS.PARM.DEPT.CODE` | `InlendSfmsInMsgParam_DeptCode` | String |  |  |
| 14 | `INLEND.SFMS.PARM.AUDITOR.CODE` | `InlendSfmsInMsgParam_AuditorCode` | String |  |  |
| 15 | `INLEND.SFMS.PARM.AUDIT.DATE.TIME` | `InlendSfmsInMsgParam_AuditDateTime` | String |  |  |
