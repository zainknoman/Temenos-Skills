# ITREGE.TRANSACTIONS.CODE — Table Schema

> Source: `INSERTS/I_F.ITREGE.TRANSACTIONS.CODE` in `ITREGE_PortfolioMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRANSCODE.SOURCE.TYPE` | `ItregeTransactionsCode_SourceType` |  |  |  |
| 2 | `TRANSCODE.TRANSACTION.CODE` | `ItregeTransactionsCode_TransactionCode` |  |  |  |
| 3 | `TRANSCODE.COLLECTION.TYPE.CR` | `ItregeTransactionsCode_CollectionTypeCr` |  |  |  |
| 4 | `TRANSCODE.COLLECTION.TYPE.DR` | `ItregeTransactionsCode_CollectionTypeDr` |  |  |  |
| 5 | `TRANSCODE.LOCAL.REF` | `ItregeTransactionsCode_LocalRef` |  |  |  |
| 6 | `TRANSCODE.OVERRIDE` | `ItregeTransactionsCode_Override` |  |  |  |
| 7 | `TRANSCODE.RECORD.STATUS` | `ItregeTransactionsCode_RecordStatus` | String |  |  |
| 8 | `TRANSCODE.CURR.NO` | `ItregeTransactionsCode_CurrNo` | String |  |  |
| 9 | `TRANSCODE.INPUTTER` | `ItregeTransactionsCode_Inputter` |  |  |  |
| 10 | `TRANSCODE.DATE.TIME` | `ItregeTransactionsCode_DateTime` |  |  |  |
| 11 | `TRANSCODE.AUTHORISER` | `ItregeTransactionsCode_Authoriser` | String |  |  |
| 12 | `TRANSCODE.CO.CODE` | `ItregeTransactionsCode_CoCode` | String |  |  |
| 13 | `TRANSCODE.DEPT.CODE` | `ItregeTransactionsCode_DeptCode` | String |  |  |
| 14 | `TRANSCODE.AUDITOR.CODE` | `ItregeTransactionsCode_AuditorCode` | String |  |  |
| 15 | `TRANSCODE.AUDIT.DATE.TIME` | `ItregeTransactionsCode_AuditDateTime` | String |  |  |
