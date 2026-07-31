# PAYVERIS.FILE — Table Schema

> Source: `INSERTS/I_F.PAYVERIS.FILE` in `NAPVPT_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVF.STATUS` | `PayverisFile_Status` | TField |  | The status would be the following LOADING - The file has been picked up for the processing and is getting de bluked. LOADED - The file is processed and is loaded into Transact. SETTLED - Once the entries are settled between the clearing account and settlement account. |
| 2 | `PVF.FILE.ID` | `PayverisFile_FileId` | TField |  | Store the id of the file from the payment file. The naming convention of the file id is Prod.(core name).good-funds_(bank_id)-(client code)_(unique batch identifier).out |
| 3 | `PVF.FILE.HEAD.IND` | `PayverisFile_FileHeadInd` | TField |  | The value would be "FH" |
| 4 | `PVF.ORIGINATOR.ID` | `PayverisFile_OriginatorId` | TField |  | File originator id. |
| 5 | `PVF.FILE.DESC` | `PayverisFile_FileDesc` | TField |  | File purpose description. |
| 6 | `PVF.DATE.SENT` | `PayverisFile_DateSent` | TField |  | The value sent in the file is in the format MMDDYYYY. This would be converted into Transact date format before storing. The date would be converted back into us format when it is sent back to paysafe. |
| 7 | `PVF.PROCESSOR.NAME` | `PayverisFile_ProcessorName` | TField |  | Core banking processor consuming the file. |
| 8 | `PVF.PROCESSOR.ID` | `PayverisFile_ProcessorId` | TField |  | Assigned by Payveris. |
| 9 | `PVF.NO.OF.BATCHES` | `PayverisFile_NoOfBatches` | TField |  | Batches in the File. |
| 10 | `PVF.TOTAL.CR.TXNS` | `PayverisFile_TotalCrTxns` | TField |  | Total credit transactions. |
| 11 | `PVF.TOTAL.CR.AMOUNT` | `PayverisFile_TotalCrAmount` | TField |  | Total credit amount. |
| 12 | `PVF.TOTAL.DB.TXNS` | `PayverisFile_TotalDbTxns` | TField |  | Total debit transactions. |
| 13 | `PVF.TOTAL.DB.AMOUNT` | `PayverisFile_TotalDbAmount` | TField |  | Total debit amount. |
| 14 | `PVF.TOTAL.TXNS` | `PayverisFile_TotalTxns` | TField |  | Total transactions. |
| 15 | `PVF.NET.AMOUNT` | `PayverisFile_NetAmount` | TField |  | Total amount. |
| 16 | `PVF.CR.TXN.APPROVED` | `PayverisFile_CrTxnApproved` | TField |  | Total number of credit transactions posted in the File |
| 17 | `PVF.CR.AMT.APPROVED` | `PayverisFile_CrAmtApproved` | TField |  | Total amount of the credit transactions posted in the File |
| 18 | `PVF.CR.TXN.FAILED` | `PayverisFile_CrTxnFailed` | TField |  | Total number of credit transactions rejected in the File. |
| 19 | `PVF.CR.AMT.FAILED` | `PayverisFile_CrAmtFailed` | TField |  | Total amount of the credit transactions rejected in the File. |
| 20 | `PVF.DB.TXN.APPROVED` | `PayverisFile_DbTxnApproved` | TField |  | Total number of debit transactions posted in the File |
| 21 | `PVF.DB.AMT.APPROVED` | `PayverisFile_DbAmtApproved` | TField |  | Total amount of the debit transactions posted in the File |
| 22 | `PVF.DB.TXN.FAILED` | `PayverisFile_DbTxnFailed` | TField |  | Total number of debit transactions rejected in the File. |
| 23 | `PVF.DB.AMT.FAILED` | `PayverisFile_DbAmtFailed` | TField |  | Total amount of the debit transactions rejected in the File. |
| 24 | `PVF.PROCESSING.DATE` | `PayverisFile_ProcessingDate` | TField |  | Transact Date when the file was loaded. |
| 25 | `PVF.LOADED.UPTO` | `PayverisFile_LoadedUpto` | TField |  | Number of records from files loaded. |
| 26 | `PVF.FILE.NAME` | `PayverisFile_FileName` | TField |  | Payveris File Name |
| 27 | `PVF.RECORD.STATUS` | `PayverisFile_RecordStatus` | String |  |  |
| 28 | `PVF.CURR.NO` | `PayverisFile_CurrNo` | String |  |  |
| 29 | `PVF.INPUTTER` | `PayverisFile_Inputter` |  |  |  |
| 30 | `PVF.DATE.TIME` | `PayverisFile_DateTime` |  |  |  |
| 31 | `PVF.AUTHORISER` | `PayverisFile_Authoriser` | String |  |  |
| 32 | `PVF.CO.CODE` | `PayverisFile_CoCode` | String |  |  |
| 33 | `PVF.DEPT.CODE` | `PayverisFile_DeptCode` | String |  |  |
| 34 | `PVF.AUDITOR.CODE` | `PayverisFile_AuditorCode` | String |  |  |
| 35 | `PVF.AUDIT.DATE.TIME` | `PayverisFile_AuditDateTime` | String |  |  |
