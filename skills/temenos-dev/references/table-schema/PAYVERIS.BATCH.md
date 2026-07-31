# PAYVERIS.BATCH — Table Schema

> Source: `INSERTS/I_F.PAYVERIS.BATCH` in `NAPVPT_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVB.BATCH.HEAD.IND` | `PayverisBatch_BatchHeadInd` | TField |  | The value would be "BH" |
| 2 | `PVB.FILE.ID` | `PayverisBatch_FileId` | TField |  | Payveris file identifier. Key to PAYVERIS.FILE |
| 3 | `PVB.BATCH.ID` | `PayverisBatch_BatchId` | TField |  | Id of the batch in the file |
| 4 | `PVB.STATUS` | `PayverisBatch_Status` | TField |  | LOADED � The file is processed and is loaded into Transact. |
| 5 | `PVB.BATCH.DESC` | `PayverisBatch_BatchDesc` | TField |  | Batch description sent form payveris |
| 6 | `PVB.FI.ID` | `PayverisBatch_FiId` | TField |  | Unique FI identifier assigned by payveris |
| 7 | `PVB.FI.NAME` | `PayverisBatch_FiName` | TField |  | Name of the FI |
| 8 | `PVB.ACCOUNT.NO` | `PayverisBatch_AccountNo` | TField |  | Holding account for the batch. |
| 9 | `PVB.ROUTING.NO` | `PayverisBatch_RoutingNo` | TField |  | Holding account Routing number. |
| 10 | `PVB.TOTAL.CR.TXNS` | `PayverisBatch_TotalCrTxns` | TField |  | Total credit transactions. |
| 11 | `PVB.TOTAL.CR.AMOUNT` | `PayverisBatch_TotalCrAmount` | TField |  | Total credit amount. |
| 12 | `PVB.TOTAL.DB.TXNS` | `PayverisBatch_TotalDbTxns` | TField |  | Total debit transactions. |
| 13 | `PVB.TOTAL.DB.AMOUNT` | `PayverisBatch_TotalDbAmount` | TField |  | Total debit amount. |
| 14 | `PVB.TOTAL.TXNS` | `PayverisBatch_TotalTxns` | TField |  | Total transactions. |
| 15 | `PVB.NET.AMOUNT` | `PayverisBatch_NetAmount` | TField |  | Total amount. |
| 16 | `PVB.CR.TXN.APPROVED` | `PayverisBatch_CrTxnApproved` | TField |  | Total number of credit transactions posted in the File |
| 17 | `PVB.CR.AMT.APPROVED` | `PayverisBatch_CrAmtApproved` | TField |  | Total amount of the credit transactions posted in the File |
| 18 | `PVB.CR.TXN.FAILED` | `PayverisBatch_CrTxnFailed` | TField |  | Total number of credit transactions rejected in the File. |
| 19 | `PVB.CR.AMT.FAILED` | `PayverisBatch_CrAmtFailed` | TField |  | Total amount of the credit transactions rejected in the File. |
| 20 | `PVB.DB.TXN.APPROVED` | `PayverisBatch_DbTxnApproved` | TField |  | Total number of debit transactions posted in the File |
| 21 | `PVB.DB.AMT.APPROVED` | `PayverisBatch_DbAmtApproved` | TField |  | Total amount of the debit transactions posted in the File |
| 22 | `PVB.DB.TXN.FAILED` | `PayverisBatch_DbTxnFailed` | TField |  | Total number of debit transactions rejected in the File. |
| 23 | `PVB.DB.AMT.FAILED` | `PayverisBatch_DbAmtFailed` | TField |  | Total amount of the debit transactions rejected in the File. |
| 24 | `PVB.NET.TXN.CODE` | `PayverisBatch_NetTxnCode` | TField |  | The indicator to specify if the net amount if a credit or debit . CR or DB |
| 25 | `PVB.ERROR.MESSAGE` | `PayverisBatch_ErrorMessage` | TField |  |  |
| 26 | `PVB.INWARD.ENTRY` | `PayverisBatch_InwardEntry` | TField |  |  |
| 27 | `PVB.RECORD.STATUS` | `PayverisBatch_RecordStatus` | String |  |  |
| 28 | `PVB.CURR.NO` | `PayverisBatch_CurrNo` | String |  |  |
| 29 | `PVB.INPUTTER` | `PayverisBatch_Inputter` |  |  |  |
| 30 | `PVB.DATE.TIME` | `PayverisBatch_DateTime` |  |  |  |
| 31 | `PVB.AUTHORISER` | `PayverisBatch_Authoriser` | String |  |  |
| 32 | `PVB.CO.CODE` | `PayverisBatch_CoCode` | String |  |  |
| 33 | `PVB.DEPT.CODE` | `PayverisBatch_DeptCode` | String |  |  |
| 34 | `PVB.AUDITOR.CODE` | `PayverisBatch_AuditorCode` | String |  |  |
| 35 | `PVB.AUDIT.DATE.TIME` | `PayverisBatch_AuditDateTime` | String |  |  |
