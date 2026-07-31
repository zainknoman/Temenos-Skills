# CAPL.H.CLR.REDIRECT.ACCT — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CLR.REDIRECT.ACCT` in `CABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CLR.RED.AC.VAL.ACCT.NO` | `CaplHClrRedirectAcct_ValAcctNo` | TField |  | Valid T24 Account number. |
| 2 | `CLR.RED.AC.START.DATE` | `CaplHClrRedirectAcct_StartDate` | TField |  | This field is used to capture the date from which the Redirection is valid for clearing. |
| 3 | `CLR.RED.AC.END.DATE` | `CaplHClrRedirectAcct_EndDate` | TField |  | This field is to capture the end date when the Redirection expires in the system.. |
| 4 | `CLR.RED.AC.CLOSED.ACCT` | `CaplHClrRedirectAcct_ClosedAcct` | TField |  |  |
| 5 | `CLR.RED.AC.RESERVED.1` | `CaplHClrRedirectAcct_Reserved1` | TField |  |  |
| 6 | `CLR.RED.AC.RESERVED.2` | `CaplHClrRedirectAcct_Reserved2` | TField |  |  |
| 7 | `CLR.RED.AC.RESERVED.3` | `CaplHClrRedirectAcct_Reserved3` | TField |  |  |
| 8 | `CLR.RED.AC.RESERVED.4` | `CaplHClrRedirectAcct_Reserved4` | TField |  |  |
| 9 | `CLR.RED.AC.RESERVED.5` | `CaplHClrRedirectAcct_Reserved5` | TField |  |  |
| 10 | `CLR.RED.AC.RESERVED.6` | `CaplHClrRedirectAcct_Reserved6` | TField |  |  |
| 11 | `CLR.RED.AC.RESERVED.7` | `CaplHClrRedirectAcct_Reserved7` | TField |  |  |
| 12 | `CLR.RED.AC.RESERVED.8` | `CaplHClrRedirectAcct_Reserved8` | TField |  |  |
| 13 | `CLR.RED.AC.RESERVED.9` | `CaplHClrRedirectAcct_Reserved9` | TField |  |  |
| 14 | `CLR.RED.AC.LOCAL.REF` | `CaplHClrRedirectAcct_LocalRef` |  |  |  |
| 15 | `CLR.RED.AC.OVERRIDE` | `CaplHClrRedirectAcct_Override` |  |  |  |
| 16 | `CLR.RED.AC.RECORD.STATUS` | `CaplHClrRedirectAcct_RecordStatus` | String |  |  |
| 17 | `CLR.RED.AC.CURR.NO` | `CaplHClrRedirectAcct_CurrNo` | String |  |  |
| 18 | `CLR.RED.AC.INPUTTER` | `CaplHClrRedirectAcct_Inputter` |  |  |  |
| 19 | `CLR.RED.AC.DATE.TIME` | `CaplHClrRedirectAcct_DateTime` |  |  |  |
| 20 | `CLR.RED.AC.AUTHORISER` | `CaplHClrRedirectAcct_Authoriser` | String |  |  |
| 21 | `CLR.RED.AC.CO.CODE` | `CaplHClrRedirectAcct_CoCode` | String |  |  |
| 22 | `CLR.RED.AC.DEPT.CODE` | `CaplHClrRedirectAcct_DeptCode` | String |  |  |
| 23 | `CLR.RED.AC.AUDITOR.CODE` | `CaplHClrRedirectAcct_AuditorCode` | String |  |  |
| 24 | `CLR.RED.AC.AUDIT.DATE.TIME` | `CaplHClrRedirectAcct_AuditDateTime` | String |  |  |
