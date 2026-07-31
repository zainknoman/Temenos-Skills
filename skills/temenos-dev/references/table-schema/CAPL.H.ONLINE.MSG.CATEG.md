# CAPL.H.ONLINE.MSG.CATEG — Table Schema

> Source: `INSERTS/I_F.CAPL.H.ONLINE.MSG.CATEG` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.MDB.OMC.DESC` | `CaplHOnlineMsgCateg_Desc` |  |  |  |
| 2 | `CAPL.MDB.OMC.MSG.TYPE` | `CaplHOnlineMsgCateg_MsgType` | TField |  | Valid Message type at for MDIFINANCIALDELINQUENT. |
| 3 | `CAPL.MDB.OMC.RCL.MAP.ID` | `CaplHOnlineMsgCateg_RclMapId` |  |  |  |
| 4 | `CAPL.MDB.OMC.APPLICATION` | `CaplHOnlineMsgCateg_Application` |  |  |  |
| 5 | `CAPL.MDB.OMC.APPL.FLD` | `CaplHOnlineMsgCateg_ApplFld` |  |  |  |
| 6 | `CAPL.MDB.OMC.APPL.OPR` | `CaplHOnlineMsgCateg_ApplOpr` |  |  |  |
| 7 | `CAPL.MDB.OMC.APPL.VALUE` | `CaplHOnlineMsgCateg_ApplValue` |  |  |  |
| 8 | `CAPL.MDB.OMC.APPL.COND` | `CaplHOnlineMsgCateg_ApplCond` |  |  |  |
| 9 | `CAPL.MDB.OMC.RESERVED.11` | `CaplHOnlineMsgCateg_Reserved11` |  |  |  |
| 10 | `CAPL.MDB.OMC.RESERVED.12` | `CaplHOnlineMsgCateg_Reserved12` |  |  |  |
| 11 | `CAPL.MDB.OMC.EXT.RTN` | `CaplHOnlineMsgCateg_ExtRtn` | TField |  | Routine to be used for producing the messages. |
| 12 | `CAPL.MDB.OMC.RTN.RCL.MAP.ID` | `CaplHOnlineMsgCateg_RtnRclMapId` | TField |  | RCL mapping id to be used for forming the full message. |
| 13 | `CAPL.MDB.OMC.D.BFORE.MAT` | `CaplHOnlineMsgCateg_DBforeMat` | TField |  | No of Day's before Maturity |
| 14 | `CAPL.MDB.OMC.BY.CUS.ACC` | `CaplHOnlineMsgCateg_ByCusAcc` | TField |  | Application name to be used for fetching the data |
| 15 | `CAPL.MDB.OMC.FIXED.SELECTION` | `CaplHOnlineMsgCateg_FixedSelection` |  |  |  |
| 16 | `CAPL.MDB.OMC.RESERVED.1` | `CaplHOnlineMsgCateg_Reserved1` | TField |  |  |
| 17 | `CAPL.MDB.OMC.RESERVED.2` | `CaplHOnlineMsgCateg_Reserved2` | TField |  |  |
| 18 | `CAPL.MDB.OMC.RESERVED.3` | `CaplHOnlineMsgCateg_Reserved3` | TField |  |  |
| 19 | `CAPL.MDB.OMC.RESERVED.4` | `CaplHOnlineMsgCateg_Reserved4` | TField |  |  |
| 20 | `CAPL.MDB.OMC.RESERVED.5` | `CaplHOnlineMsgCateg_Reserved5` | TField |  |  |
| 21 | `CAPL.MDB.OMC.RESERVED.6` | `CaplHOnlineMsgCateg_Reserved6` | TField |  |  |
| 22 | `CAPL.MDB.OMC.RESERVED.7` | `CaplHOnlineMsgCateg_Reserved7` | TField |  |  |
| 23 | `CAPL.MDB.OMC.RESERVED.8` | `CaplHOnlineMsgCateg_Reserved8` | TField |  |  |
| 24 | `CAPL.MDB.OMC.RESERVED.9` | `CaplHOnlineMsgCateg_Reserved9` | TField |  |  |
| 25 | `CAPL.MDB.OMC.RESERVED.10` | `CaplHOnlineMsgCateg_Reserved10` | TField |  |  |
| 26 | `CAPL.MDB.OMC.LOCAL.REF` | `CaplHOnlineMsgCateg_LocalRef` |  |  |  |
| 27 | `CAPL.MDB.OMC.OVERRIDE` | `CaplHOnlineMsgCateg_Override` |  |  |  |
| 28 | `CAPL.MDB.OMC.RECORD.STATUS` | `CaplHOnlineMsgCateg_RecordStatus` | String |  |  |
| 29 | `CAPL.MDB.OMC.CURR.NO` | `CaplHOnlineMsgCateg_CurrNo` | String |  |  |
| 30 | `CAPL.MDB.OMC.INPUTTER` | `CaplHOnlineMsgCateg_Inputter` |  |  |  |
| 31 | `CAPL.MDB.OMC.DATE.TIME` | `CaplHOnlineMsgCateg_DateTime` |  |  |  |
| 32 | `CAPL.MDB.OMC.AUTHORISER` | `CaplHOnlineMsgCateg_Authoriser` | String |  |  |
| 33 | `CAPL.MDB.OMC.CO.CODE` | `CaplHOnlineMsgCateg_CoCode` | String |  |  |
| 34 | `CAPL.MDB.OMC.DEPT.CODE` | `CaplHOnlineMsgCateg_DeptCode` | String |  |  |
| 35 | `CAPL.MDB.OMC.AUDITOR.CODE` | `CaplHOnlineMsgCateg_AuditorCode` | String |  |  |
| 36 | `CAPL.MDB.OMC.AUDIT.DATE.TIME` | `CaplHOnlineMsgCateg_AuditDateTime` | String |  |  |
