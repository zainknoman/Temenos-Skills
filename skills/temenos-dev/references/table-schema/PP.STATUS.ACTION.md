# PP.STATUS.ACTION — Table Schema

> Source: `INSERTS/I_F.PP.STATUS.ACTION` in `PP_TRIPService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SAC.CompanyID` | `PpStatusAction_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.SAC.ProgramName` | `PpStatusAction_Programname` |  |  |  |
| 3 | `PP.SAC.StatusActionDescription` | `PpStatusAction_Statusactiondescription` |  |  |  |
| 4 | `PP.SAC.StatusRouterExpectedErrorCode` | `PpStatusAction_Statusrouterexpectederrorcode` |  |  |  |
| 5 | `PP.SAC.StatusRouterExpectedStatus` | `PpStatusAction_Statusrouterexpectedstatus` |  |  |  |
| 6 | `PP.SAC.StatusEventType` | `PpStatusAction_Statuseventtype` |  |  |  |
| 7 | `PP.SAC.StatusExclusionAPI` | `PpStatusAction_Statusexclusionapi` | TField |  | Field used To configure the API whether Event trigger needs to be excluded or not. |
| 8 | `PP.SAC.RESERVED.3` | `PpStatusAction_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.SAC.RESERVED.2` | `PpStatusAction_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.SAC.RESERVED.1` | `PpStatusAction_Reserved1` |  |  |  |
| 11 | `PP.SAC.LOCAL.REF` | `PpStatusAction_LocalRef` |  |  |  |
| 12 | `PP.SAC.OVERRIDE` | `PpStatusAction_Override` |  |  |  |
| 13 | `PP.SAC.RECORD.STATUS` | `PpStatusAction_RecordStatus` | String |  |  |
| 14 | `PP.SAC.CURR.NO` | `PpStatusAction_CurrNo` | String |  |  |
| 15 | `PP.SAC.INPUTTER` | `PpStatusAction_Inputter` |  |  |  |
| 16 | `PP.SAC.DATE.TIME` | `PpStatusAction_DateTime` |  |  |  |
| 17 | `PP.SAC.AUTHORISER` | `PpStatusAction_Authoriser` | String |  |  |
| 18 | `PP.SAC.CO.CODE` | `PpStatusAction_CoCode` | String |  |  |
| 19 | `PP.SAC.DEPT.CODE` | `PpStatusAction_DeptCode` | String |  |  |
| 20 | `PP.SAC.AUDITOR.CODE` | `PpStatusAction_AuditorCode` | String |  |  |
| 21 | `PP.SAC.AUDIT.DATE.TIME` | `PpStatusAction_AuditDateTime` | String |  |  |
