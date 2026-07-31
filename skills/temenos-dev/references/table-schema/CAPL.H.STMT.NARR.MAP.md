# CAPL.H.STMT.NARR.MAP — Table Schema

> Source: `INSERTS/I_F.CAPL.H.STMT.NARR.MAP` in `CABASE_CustomerStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.STMT.NARR.TXN.DESC` | `CaplHStmtNarrMap_TxnDesc` | TField |  | Field is used to define the Transaction Description. |
| 2 | `CAPL.STMT.NARR.RESERVED.1` | `CaplHStmtNarrMap_Reserved1` | TField |  |  |
| 3 | `CAPL.STMT.NARR.STMT.DESC.1` | `CaplHStmtNarrMap_StmtDesc1` |  |  |  |
| 4 | `CAPL.STMT.NARR.STMT.DESC.2` | `CaplHStmtNarrMap_StmtDesc2` |  |  |  |
| 5 | `CAPL.STMT.NARR.STMT.DESC.3` | `CaplHStmtNarrMap_StmtDesc3` |  |  |  |
| 6 | `CAPL.STMT.NARR.NARR.LOC.CORE` | `CaplHStmtNarrMap_NarrLocCore` | TField |  | This field is to define whether the statement narrative needs to be defaulted based on Core functionality or current setup.Allowed values are LOCAL\CORE. |
| 7 | `CAPL.STMT.NARR.IVR.STMT.DESC` | `CaplHStmtNarrMap_IvrStmtDesc` | TField |  | Field to define the transaction description to be displayed in IVR. |
| 8 | `CAPL.STMT.NARR.RESERVED.3` | `CaplHStmtNarrMap_Reserved3` | TField |  |  |
| 9 | `CAPL.STMT.NARR.RESERVED.4` | `CaplHStmtNarrMap_Reserved4` | TField |  |  |
| 10 | `CAPL.STMT.NARR.LOCAL.REF` | `CaplHStmtNarrMap_LocalRef` |  |  |  |
| 11 | `CAPL.STMT.NARR.OVERRIDE` | `CaplHStmtNarrMap_Override` |  |  |  |
| 12 | `CAPL.STMT.NARR.RECORD.STATUS` | `CaplHStmtNarrMap_RecordStatus` | String |  |  |
| 13 | `CAPL.STMT.NARR.CURR.NO` | `CaplHStmtNarrMap_CurrNo` | String |  |  |
| 14 | `CAPL.STMT.NARR.INPUTTER` | `CaplHStmtNarrMap_Inputter` |  |  |  |
| 15 | `CAPL.STMT.NARR.DATE.TIME` | `CaplHStmtNarrMap_DateTime` |  |  |  |
| 16 | `CAPL.STMT.NARR.AUTHORISER` | `CaplHStmtNarrMap_Authoriser` | String |  |  |
| 17 | `CAPL.STMT.NARR.CO.CODE` | `CaplHStmtNarrMap_CoCode` | String |  |  |
| 18 | `CAPL.STMT.NARR.DEPT.CODE` | `CaplHStmtNarrMap_DeptCode` | String |  |  |
| 19 | `CAPL.STMT.NARR.AUDITOR.CODE` | `CaplHStmtNarrMap_AuditorCode` | String |  |  |
| 20 | `CAPL.STMT.NARR.AUDIT.DATE.TIME` | `CaplHStmtNarrMap_AuditDateTime` | String |  |  |
