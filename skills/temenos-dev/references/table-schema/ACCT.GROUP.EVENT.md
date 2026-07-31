# ACCT.GROUP.EVENT — Table Schema

> Source: `INSERTS/I_F.ACCT.GROUP.EVENT` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.AGE.EVENT.TYPE` | `AcctGroupEvent_EventType` |  |  |  |
| 2 | `AC.AGE.EVENT` | `AcctGroupEvent_Event` |  |  |  |
| 3 | `AC.AGE.RESERVED.10` | `AcctGroupEvent_Reserved10` | TField |  |  |
| 4 | `AC.AGE.RESERVED.9` | `AcctGroupEvent_Reserved9` | TField |  |  |
| 5 | `AC.AGE.RESERVED.8` | `AcctGroupEvent_Reserved8` | TField |  |  |
| 6 | `AC.AGE.RESERVED.7` | `AcctGroupEvent_Reserved7` | TField |  |  |
| 7 | `AC.AGE.RESERVED.6` | `AcctGroupEvent_Reserved6` | TField |  |  |
| 8 | `AC.AGE.RESERVED.5` | `AcctGroupEvent_Reserved5` | TField |  |  |
| 9 | `AC.AGE.RESERVED.4` | `AcctGroupEvent_Reserved4` | TField |  |  |
| 10 | `AC.AGE.RESERVED.3` | `AcctGroupEvent_Reserved3` | TField |  |  |
| 11 | `AC.AGE.RESERVED.2` | `AcctGroupEvent_Reserved2` | TField |  |  |
| 12 | `AC.AGE.RESERVED.1` | `AcctGroupEvent_Reserved1` | TField |  |  |
| 13 | `AC.AGE.RECORD.STATUS` | `AcctGroupEvent_RecordStatus` | String |  |  |
| 14 | `AC.AGE.CURR.NO` | `AcctGroupEvent_CurrNo` | String |  |  |
| 15 | `AC.AGE.INPUTTER` | `AcctGroupEvent_Inputter` |  |  |  |
| 16 | `AC.AGE.DATE.TIME` | `AcctGroupEvent_DateTime` |  |  |  |
| 17 | `AC.AGE.AUTHORISER` | `AcctGroupEvent_Authoriser` | String |  |  |
| 18 | `AC.AGE.CO.CODE` | `AcctGroupEvent_CoCode` | String |  |  |
| 19 | `AC.AGE.DEPT.CODE` | `AcctGroupEvent_DeptCode` | String |  |  |
| 20 | `AC.AGE.AUDITOR.CODE` | `AcctGroupEvent_AuditorCode` | String |  |  |
| 21 | `AC.AGE.AUDIT.DATE.TIME` | `AcctGroupEvent_AuditDateTime` | String |  |  |
