# CAPL.H.ONLINE.MSG.TYPE — Table Schema

> Source: `INSERTS/I_F.CAPL.H.ONLINE.MSG.TYPE` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.MDB.OMT.DESC` | `CaplHOnlineMsgType_Desc` |  |  |  |
| 2 | `CAPL.MDB.OMT.CHANNEL` | `CaplHOnlineMsgType_Channel` |  |  |  |
| 3 | `CAPL.MDB.OMT.MSG.TYPE` | `CaplHOnlineMsgType_MsgType` | TField |  |  |
| 4 | `CAPL.MDB.OMT.RESERVED.1` | `CaplHOnlineMsgType_Reserved1` | TField |  |  |
| 5 | `CAPL.MDB.OMT.RESERVED.2` | `CaplHOnlineMsgType_Reserved2` | TField |  |  |
| 6 | `CAPL.MDB.OMT.RESERVED.3` | `CaplHOnlineMsgType_Reserved3` | TField |  |  |
| 7 | `CAPL.MDB.OMT.RESERVED.4` | `CaplHOnlineMsgType_Reserved4` | TField |  |  |
| 8 | `CAPL.MDB.OMT.RESERVED.5` | `CaplHOnlineMsgType_Reserved5` | TField |  |  |
| 9 | `CAPL.MDB.OMT.RESERVED.6` | `CaplHOnlineMsgType_Reserved6` | TField |  |  |
| 10 | `CAPL.MDB.OMT.RESERVED.7` | `CaplHOnlineMsgType_Reserved7` | TField |  |  |
| 11 | `CAPL.MDB.OMT.RESERVED.8` | `CaplHOnlineMsgType_Reserved8` | TField |  |  |
| 12 | `CAPL.MDB.OMT.RESERVED.9` | `CaplHOnlineMsgType_Reserved9` | TField |  |  |
| 13 | `CAPL.MDB.OMT.RESERVED.10` | `CaplHOnlineMsgType_Reserved10` | TField |  |  |
| 14 | `CAPL.MDB.OMT.LOCAL.REF` | `CaplHOnlineMsgType_LocalRef` |  |  |  |
| 15 | `CAPL.MDB.OMT.OVERRIDE` | `CaplHOnlineMsgType_Override` |  |  |  |
| 16 | `CAPL.MDB.OMT.RECORD.STATUS` | `CaplHOnlineMsgType_RecordStatus` | String |  |  |
| 17 | `CAPL.MDB.OMT.CURR.NO` | `CaplHOnlineMsgType_CurrNo` | String |  |  |
| 18 | `CAPL.MDB.OMT.INPUTTER` | `CaplHOnlineMsgType_Inputter` |  |  |  |
| 19 | `CAPL.MDB.OMT.DATE.TIME` | `CaplHOnlineMsgType_DateTime` |  |  |  |
| 20 | `CAPL.MDB.OMT.AUTHORISER` | `CaplHOnlineMsgType_Authoriser` | String |  |  |
| 21 | `CAPL.MDB.OMT.CO.CODE` | `CaplHOnlineMsgType_CoCode` | String |  |  |
| 22 | `CAPL.MDB.OMT.DEPT.CODE` | `CaplHOnlineMsgType_DeptCode` | String |  |  |
| 23 | `CAPL.MDB.OMT.AUDITOR.CODE` | `CaplHOnlineMsgType_AuditorCode` | String |  |  |
| 24 | `CAPL.MDB.OMT.AUDIT.DATE.TIME` | `CaplHOnlineMsgType_AuditDateTime` | String |  |  |
