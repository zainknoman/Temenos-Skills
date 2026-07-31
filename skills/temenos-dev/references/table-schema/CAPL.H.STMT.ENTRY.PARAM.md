# CAPL.H.STMT.ENTRY.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.STMT.ENTRY.PARAM` in `CABASE_LegacyFinancial.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.SEP.LEGACY.START.DATE` | `CaplHStmtEntryParam_LegacyStartDate` | TField |  | This field specifies the start date from which the legacy systemTransactions are uploaded into T24 and therefore available for querying.Valid date to be defined here. |
| 2 | `CAPL.SEP.T24.TXN.START.DATE` | `CaplHStmtEntryParam_T24TxnStartDate` | TField |  | This field specifies the start date of the transactions in T24.Valid date to be defined here. |
| 3 | `CAPL.SEP.T24.ORIG.LIVE.DATE` | `CaplHStmtEntryParam_T24OrigLiveDate` | TField |  |  |
| 4 | `CAPL.SEP.CORE.ARC.REQ` | `CaplHStmtEntryParam_CoreArcReq` | TField |  | This field is used to capture whether the system should consider the $ARC files while fetching the customer statement. It is a radio button field with valid values as Yes or No.If selected as Yes or None - then $ARC files will be considered for fetching customer statementIf selected as No - then $ARC files will not be considered for fetching customer statement |
| 5 | `CAPL.SEP.RESERVED.8` | `CaplHStmtEntryParam_Reserved8` | TField |  |  |
| 6 | `CAPL.SEP.RESERVED.7` | `CaplHStmtEntryParam_Reserved7` | TField |  |  |
| 7 | `CAPL.SEP.RESERVED.6` | `CaplHStmtEntryParam_Reserved6` | TField |  |  |
| 8 | `CAPL.SEP.RESERVED.5` | `CaplHStmtEntryParam_Reserved5` | TField |  |  |
| 9 | `CAPL.SEP.RESERVED.4` | `CaplHStmtEntryParam_Reserved4` | TField |  |  |
| 10 | `CAPL.SEP.RESERVED.3` | `CaplHStmtEntryParam_Reserved3` | TField |  |  |
| 11 | `CAPL.SEP.RESERVED.2` | `CaplHStmtEntryParam_Reserved2` | TField |  |  |
| 12 | `CAPL.SEP.RESERVED.1` | `CaplHStmtEntryParam_Reserved1` | TField |  |  |
| 13 | `CAPL.SEP.LOCAL.REF` | `CaplHStmtEntryParam_LocalRef` |  |  |  |
| 14 | `CAPL.SEP.OVERRIDE` | `CaplHStmtEntryParam_Override` |  |  |  |
| 15 | `CAPL.SEP.RECORD.STATUS` | `CaplHStmtEntryParam_RecordStatus` | String |  |  |
| 16 | `CAPL.SEP.CURR.NO` | `CaplHStmtEntryParam_CurrNo` | String |  |  |
| 17 | `CAPL.SEP.INPUTTER` | `CaplHStmtEntryParam_Inputter` |  |  |  |
| 18 | `CAPL.SEP.DATE.TIME` | `CaplHStmtEntryParam_DateTime` |  |  |  |
| 19 | `CAPL.SEP.AUTHORISER` | `CaplHStmtEntryParam_Authoriser` | String |  |  |
| 20 | `CAPL.SEP.CO.CODE` | `CaplHStmtEntryParam_CoCode` | String |  |  |
| 21 | `CAPL.SEP.DEPT.CODE` | `CaplHStmtEntryParam_DeptCode` | String |  |  |
| 22 | `CAPL.SEP.AUDITOR.CODE` | `CaplHStmtEntryParam_AuditorCode` | String |  |  |
| 23 | `CAPL.SEP.AUDIT.DATE.TIME` | `CaplHStmtEntryParam_AuditDateTime` | String |  |  |
