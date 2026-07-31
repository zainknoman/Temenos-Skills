# TCIB.CLOSURE.LOG — Table Schema

> Source: `INSERTS/I_F.TCIB.CLOSURE.LOG` in `CATCIB_TCIBOnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCIB.CLS.ACCOUNT` | `TcibClosureLog_Account` | TField |  | This field is used to store the valid account number for the exception to be captured.Valid record from ACCOUNT table. |
| 2 | `TCIB.CLS.REASON` | `TcibClosureLog_Reason` |  |  |  |
| 3 | `TCIB.CLS.RESERVED.1` | `TcibClosureLog_Reserved1` | TField |  |  |
| 4 | `TCIB.CLS.RESERVED.2` | `TcibClosureLog_Reserved2` | TField |  |  |
| 5 | `TCIB.CLS.RESERVED.3` | `TcibClosureLog_Reserved3` | TField |  |  |
| 6 | `TCIB.CLS.RESERVED.4` | `TcibClosureLog_Reserved4` | TField |  |  |
| 7 | `TCIB.CLS.RESERVED.5` | `TcibClosureLog_Reserved5` | TField |  |  |
| 8 | `TCIB.CLS.RECORD.STATUS` | `TcibClosureLog_RecordStatus` | String |  |  |
| 9 | `TCIB.CLS.CURR.NO` | `TcibClosureLog_CurrNo` | String |  |  |
| 10 | `TCIB.CLS.INPUTTER` | `TcibClosureLog_Inputter` |  |  |  |
| 11 | `TCIB.CLS.DATE.TIME` | `TcibClosureLog_DateTime` |  |  |  |
| 12 | `TCIB.CLS.AUTHORISER` | `TcibClosureLog_Authoriser` | String |  |  |
| 13 | `TCIB.CLS.CO.CODE` | `TcibClosureLog_CoCode` | String |  |  |
| 14 | `TCIB.CLS.DEPT.CODE` | `TcibClosureLog_DeptCode` | String |  |  |
| 15 | `TCIB.CLS.AUDITOR.CODE` | `TcibClosureLog_AuditorCode` | String |  |  |
| 16 | `TCIB.CLS.AUDIT.DATE.TIME` | `TcibClosureLog_AuditDateTime` | String |  |  |
