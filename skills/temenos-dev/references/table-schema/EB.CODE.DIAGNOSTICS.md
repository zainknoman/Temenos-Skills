# EB.CODE.DIAGNOSTICS — Table Schema

> Source: `INSERTS/I_F.EB.CODE.DIAGNOSTICS` in `EB_Seat.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.COD.DIAG.DESCRIPTION` | `EbCodeDiagnostics_Description` |  |  |  |
| 2 | `EB.COD.DIAG.SCRIPT.ID` | `EbCodeDiagnostics_ScriptId` |  |  |  |
| 3 | `EB.COD.DIAG.JOB.TXN.ID` | `EbCodeDiagnostics_JobTxnId` |  |  |  |
| 4 | `EB.COD.DIAG.APPLN.TXN.ID` | `EbCodeDiagnostics_ApplnTxnId` |  |  |  |
| 5 | `EB.COD.DIAG.CODE.COVERAGE` | `EbCodeDiagnostics_CodeCoverage` |  |  |  |
| 6 | `EB.COD.DIAG.CALL.DUMP` | `EbCodeDiagnostics_CallDump` |  |  |  |
| 7 | `EB.COD.DIAG.COMMON.DUMP` | `EbCodeDiagnostics_CommonDump` |  |  |  |
| 8 | `EB.COD.DIAG.RESERVED.5` | `EbCodeDiagnostics_Reserved5` |  |  |  |
| 9 | `EB.COD.DIAG.RESERVED.4` | `EbCodeDiagnostics_Reserved4` |  |  |  |
| 10 | `EB.COD.DIAG.RESERVED.3` | `EbCodeDiagnostics_Reserved3` |  |  |  |
| 11 | `EB.COD.DIAG.RESERVED.2` | `EbCodeDiagnostics_Reserved2` |  |  |  |
| 12 | `EB.COD.DIAG.RESERVED.1` | `EbCodeDiagnostics_Reserved1` |  |  |  |
| 13 | `EB.COD.DIAG.RESERVED.15` | `EbCodeDiagnostics_Reserved15` | TField |  |  |
| 14 | `EB.COD.DIAG.RESERVED.14` | `EbCodeDiagnostics_Reserved14` | TField |  |  |
| 15 | `EB.COD.DIAG.RESERVED.13` | `EbCodeDiagnostics_Reserved13` | TField |  |  |
| 16 | `EB.COD.DIAG.RESERVED.12` | `EbCodeDiagnostics_Reserved12` | TField |  |  |
| 17 | `EB.COD.DIAG.RESERVED.11` | `EbCodeDiagnostics_Reserved11` | TField |  |  |
| 18 | `EB.COD.DIAG.RESERVED.10` | `EbCodeDiagnostics_Reserved10` | TField |  |  |
| 19 | `EB.COD.DIAG.RESERVED.9` | `EbCodeDiagnostics_Reserved9` | TField |  |  |
| 20 | `EB.COD.DIAG.RESERVED.8` | `EbCodeDiagnostics_Reserved8` | TField |  |  |
| 21 | `EB.COD.DIAG.RESERVED.7` | `EbCodeDiagnostics_Reserved7` | TField |  |  |
| 22 | `EB.COD.DIAG.RESERVED.6` | `EbCodeDiagnostics_Reserved6` | TField |  |  |
| 23 | `EB.COD.DIAG.OVERRIDE` | `EbCodeDiagnostics_Override` |  |  |  |
| 24 | `EB.COD.DIAG.RECORD.STATUS` | `EbCodeDiagnostics_RecordStatus` | String |  |  |
| 25 | `EB.COD.DIAG.CURR.NO` | `EbCodeDiagnostics_CurrNo` | String |  |  |
| 26 | `EB.COD.DIAG.INPUTTER` | `EbCodeDiagnostics_Inputter` |  |  |  |
| 27 | `EB.COD.DIAG.DATE.TIME` | `EbCodeDiagnostics_DateTime` |  |  |  |
| 28 | `EB.COD.DIAG.AUTHORISER` | `EbCodeDiagnostics_Authoriser` | String |  |  |
| 29 | `EB.COD.DIAG.CO.CODE` | `EbCodeDiagnostics_CoCode` | String |  |  |
| 30 | `EB.COD.DIAG.DEPT.CODE` | `EbCodeDiagnostics_DeptCode` | String |  |  |
| 31 | `EB.COD.DIAG.AUDITOR.CODE` | `EbCodeDiagnostics_AuditorCode` | String |  |  |
| 32 | `EB.COD.DIAG.AUDIT.DATE.TIME` | `EbCodeDiagnostics_AuditDateTime` | String |  |  |
