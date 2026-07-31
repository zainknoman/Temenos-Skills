# ESBASE.CLIENT.CUTOFF — Table Schema

> Source: `INSERTS/I_F.ESBASE.CLIENT.CUTOFF` in `ESBASE_NonPayableFile.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESBASE.CLNT.CLEARING.TRANSACTION.TYPE` | `EsbaseClientCutoff_ClearingTransactionType` | TField |  | This will hold the type of the transaction |
| 2 | `ESBASE.CLNT.CUTOFF.TIME` | `EsbaseClientCutoff_CutoffTime` | TField |  | This will hold the cut off time |
| 3 | `ESBASE.CLNT.STATUS` | `EsbaseClientCutoff_Status` | TField |  | This will hold the status |
| 4 | `ESBASE.CLNT.LOCAL.REF` | `EsbaseClientCutoff_LocalRef` |  |  |  |
| 5 | `ESBASE.CLNT.OVERRIDE` | `EsbaseClientCutoff_Override` |  |  |  |
| 6 | `ESBASE.CLNT.RECORD.STATUS` | `EsbaseClientCutoff_RecordStatus` | String |  |  |
| 7 | `ESBASE.CLNT.CURR.NO` | `EsbaseClientCutoff_CurrNo` | String |  |  |
| 8 | `ESBASE.CLNT.INPUTTER` | `EsbaseClientCutoff_Inputter` |  |  |  |
| 9 | `ESBASE.CLNT.DATE.TIME` | `EsbaseClientCutoff_DateTime` |  |  |  |
| 10 | `ESBASE.CLNT.AUTHORISER` | `EsbaseClientCutoff_Authoriser` | String |  |  |
| 11 | `ESBASE.CLNT.CO.CODE` | `EsbaseClientCutoff_CoCode` | String |  |  |
| 12 | `ESBASE.CLNT.DEPT.CODE` | `EsbaseClientCutoff_DeptCode` | String |  |  |
| 13 | `ESBASE.CLNT.AUDITOR.CODE` | `EsbaseClientCutoff_AuditorCode` | String |  |  |
| 14 | `ESBASE.CLNT.AUDIT.DATE.TIME` | `EsbaseClientCutoff_AuditDateTime` | String |  |  |
