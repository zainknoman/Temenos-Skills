# TC.OPERATIONS — Table Schema

> Source: `INSERTS/I_F.TC.OPERATIONS` in `T2_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TC.OPER.DESCRIPTION` | `TcOperations_Description` |  |  |  |
| 2 | `TC.OPER.ALLOWED.CHANNEL` | `TcOperations_AllowedChannel` |  |  |  |
| 3 | `TC.OPER.RESERVED.10` | `TcOperations_Reserved10` | TField |  |  |
| 4 | `TC.OPER.RESERVED.9` | `TcOperations_Reserved9` | TField |  |  |
| 5 | `TC.OPER.RESERVED.8` | `TcOperations_Reserved8` | TField |  |  |
| 6 | `TC.OPER.RESERVED.7` | `TcOperations_Reserved7` | TField |  |  |
| 7 | `TC.OPER.RESERVED.6` | `TcOperations_Reserved6` | TField |  |  |
| 8 | `TC.OPER.RESERVED.5` | `TcOperations_Reserved5` | TField |  |  |
| 9 | `TC.OPER.RESERVED.4` | `TcOperations_Reserved4` | TField |  |  |
| 10 | `TC.OPER.RESERVED.3` | `TcOperations_Reserved3` | TField |  |  |
| 11 | `TC.OPER.RESERVED.2` | `TcOperations_Reserved2` | TField |  |  |
| 12 | `TC.OPER.RESERVED.1` | `TcOperations_Reserved1` | TField |  |  |
| 13 | `TC.OPER.RECORD.STATUS` | `TcOperations_RecordStatus` | String |  |  |
| 14 | `TC.OPER.CURR.NO` | `TcOperations_CurrNo` | String |  |  |
| 15 | `TC.OPER.INPUTTER` | `TcOperations_Inputter` |  |  |  |
| 16 | `TC.OPER.DATE.TIME` | `TcOperations_DateTime` |  |  |  |
| 17 | `TC.OPER.AUTHORISER` | `TcOperations_Authoriser` | String |  |  |
| 18 | `TC.OPER.CO.CODE` | `TcOperations_CoCode` | String |  |  |
| 19 | `TC.OPER.DEPT.CODE` | `TcOperations_DeptCode` | String |  |  |
| 20 | `TC.OPER.AUDITOR.CODE` | `TcOperations_AuditorCode` | String |  |  |
| 21 | `TC.OPER.AUDIT.DATE.TIME` | `TcOperations_AuditDateTime` | String |  |  |
