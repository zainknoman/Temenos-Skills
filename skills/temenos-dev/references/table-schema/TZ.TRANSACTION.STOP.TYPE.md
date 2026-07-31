# TZ.TRANSACTION.STOP.TYPE — Table Schema

> Source: `INSERTS/I_F.TZ.TRANSACTION.STOP.TYPE` in `TZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TZ.TST.DESCRIPTION` | `TzTransactionStopType_Description` | TField | Yes | Description of the MatchType that can be defined. Validation Rule: Mandatory field. Value can be free-text. |
| 2 | `TZ.TST.MATCH.TYPE` | `TzTransactionStopType_MatchType` |  |  |  |
| 3 | `TZ.TST.MATCHING.ATTRIBUTE` | `TzTransactionStopType_MatchingAttribute` |  |  |  |
| 4 | `TZ.TST.MATCH.DEFAULT.DECISION` | `TzTransactionStopType_MatchDefaultDecision` |  |  |  |
| 5 | `TZ.TST.RESERVED.5` | `TzTransactionStopType_Reserved5` | TField |  |  |
| 6 | `TZ.TST.RESERVED.4` | `TzTransactionStopType_Reserved4` | TField |  |  |
| 7 | `TZ.TST.RESERVED.3` | `TzTransactionStopType_Reserved3` | TField |  |  |
| 8 | `TZ.TST.RESERVED.2` | `TzTransactionStopType_Reserved2` | TField |  |  |
| 9 | `TZ.TST.RESERVED.1` | `TzTransactionStopType_Reserved1` | TField |  |  |
| 10 | `TZ.TST.LOCAL.REF` | `TzTransactionStopType_LocalRef` |  |  |  |
| 11 | `TZ.TST.OVERRIDE` | `TzTransactionStopType_Override` |  |  |  |
| 12 | `TZ.TST.RECORD.STATUS` | `TzTransactionStopType_RecordStatus` | String |  |  |
| 13 | `TZ.TST.CURR.NO` | `TzTransactionStopType_CurrNo` | String |  |  |
| 14 | `TZ.TST.INPUTTER` | `TzTransactionStopType_Inputter` |  |  |  |
| 15 | `TZ.TST.DATE.TIME` | `TzTransactionStopType_DateTime` |  |  |  |
| 16 | `TZ.TST.AUTHORISER` | `TzTransactionStopType_Authoriser` | String |  |  |
| 17 | `TZ.TST.CO.CODE` | `TzTransactionStopType_CoCode` | String |  |  |
| 18 | `TZ.TST.DEPT.CODE` | `TzTransactionStopType_DeptCode` | String |  |  |
| 19 | `TZ.TST.AUDITOR.CODE` | `TzTransactionStopType_AuditorCode` | String |  |  |
| 20 | `TZ.TST.AUDIT.DATE.TIME` | `TzTransactionStopType_AuditDateTime` | String |  |  |
