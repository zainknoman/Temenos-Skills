# CALEND.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CALEND.PARAMETER` in `CALEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CALEND.PRM.DESCRIPTION` | `CalendParameter_Description` |  |  |  |
| 2 | `CALEND.PRM.RSRV.ACCT.CATEG` | `CalendParameter_RsrvAcctCateg` |  |  |  |
| 3 | `CALEND.PRM.RSRV.ACCT.CHARGE` | `CalendParameter_RsrvAcctCharge` | TField |  | The charge property name used for reserve account to be parameterized here. When this charge property is attached to any loan and whenever there is a payment done to this charge property, the charge amount paid is moved to the reserve account during COB. It must be a valid record in AA.PROPERTY table. |
| 4 | `CALEND.PRM.NPL.PROPG.HOOK` | `CalendParameter_NplPropgHook` | TField |  | It should be a valid t24 routine which will have two arguments. This routine will be called from batch process CALEND.NPL.CUST.PROPG.PROCESS to process all loans of customer. First argument - It will have customer id and action as passing argument to hook routine. The hook routine has to process customer's loans for corresponding action. It will return the selected loans and corresponging indicator to mentioned whether NPL and NAB change or anyone of the status change and compant codes. E.g Passing arugument : customerid and action separated by @VM (value marker) Return value: Loan id, NPL and NAB Indicator and loan's company code separated by @VM (Value marker). More than one loans separated by @FM (Field Marker) SecondArgument - Return error if any for not processing the loans" This field will be input able only if record id is SYSTEM. |
| 5 | `CALEND.PRM.NPL.RESUME.HOOK` | `CalendParameter_NplResumeHook` | TField |  | It should be a valid t24 routine which will have two argument. This hook will be called from API CALEND.NPL.SUSPEND.ARRANGEMENT. First argument will be arrangement id. Hook routine will process the arrangement and validate whether the suspension is allowed. If so it will return value ""YES"" in second argument otherwise return ""NO""." This field will be input able only if record id is SYSTEM. |
| 6 | `CALEND.PRM.RESERVED.18` | `CalendParameter_Reserved18` | TField |  |  |
| 7 | `CALEND.PRM.RESERVED.17` | `CalendParameter_Reserved17` | TField |  |  |
| 8 | `CALEND.PRM.RESERVED.16` | `CalendParameter_Reserved16` | TField |  |  |
| 9 | `CALEND.PRM.RESERVED.15` | `CalendParameter_Reserved15` | TField |  |  |
| 10 | `CALEND.PRM.RESERVED.14` | `CalendParameter_Reserved14` | TField |  |  |
| 11 | `CALEND.PRM.RESERVED.13` | `CalendParameter_Reserved13` | TField |  |  |
| 12 | `CALEND.PRM.RESERVED.12` | `CalendParameter_Reserved12` | TField |  |  |
| 13 | `CALEND.PRM.RESERVED.11` | `CalendParameter_Reserved11` | TField |  |  |
| 14 | `CALEND.PRM.RESERVED.10` | `CalendParameter_Reserved10` | TField |  |  |
| 15 | `CALEND.PRM.RESERVED.9` | `CalendParameter_Reserved9` | TField |  |  |
| 16 | `CALEND.PRM.RESERVED.8` | `CalendParameter_Reserved8` | TField |  |  |
| 17 | `CALEND.PRM.RESERVED.7` | `CalendParameter_Reserved7` | TField |  |  |
| 18 | `CALEND.PRM.RESERVED.6` | `CalendParameter_Reserved6` | TField |  |  |
| 19 | `CALEND.PRM.RESERVED.5` | `CalendParameter_Reserved5` | TField |  |  |
| 20 | `CALEND.PRM.RESERVED.4` | `CalendParameter_Reserved4` | TField |  |  |
| 21 | `CALEND.PRM.RESERVED.3` | `CalendParameter_Reserved3` | TField |  |  |
| 22 | `CALEND.PRM.RESERVED.2` | `CalendParameter_Reserved2` | TField |  |  |
| 23 | `CALEND.PRM.RESERVED.1` | `CalendParameter_Reserved1` | TField |  |  |
| 24 | `CALEND.PRM.LOCAL.REF` | `CalendParameter_LocalRef` |  |  |  |
| 25 | `CALEND.PRM.OVERRIDE` | `CalendParameter_Override` |  |  |  |
| 26 | `CALEND.PRM.RECORD.STATUS` | `CalendParameter_RecordStatus` | String |  |  |
| 27 | `CALEND.PRM.CURR.NO` | `CalendParameter_CurrNo` | String |  |  |
| 28 | `CALEND.PRM.INPUTTER` | `CalendParameter_Inputter` |  |  |  |
| 29 | `CALEND.PRM.DATE.TIME` | `CalendParameter_DateTime` |  |  |  |
| 30 | `CALEND.PRM.AUTHORISER` | `CalendParameter_Authoriser` | String |  |  |
| 31 | `CALEND.PRM.CO.CODE` | `CalendParameter_CoCode` | String |  |  |
| 32 | `CALEND.PRM.DEPT.CODE` | `CalendParameter_DeptCode` | String |  |  |
| 33 | `CALEND.PRM.AUDITOR.CODE` | `CalendParameter_AuditorCode` | String |  |  |
| 34 | `CALEND.PRM.AUDIT.DATE.TIME` | `CalendParameter_AuditDateTime` | String |  |  |
