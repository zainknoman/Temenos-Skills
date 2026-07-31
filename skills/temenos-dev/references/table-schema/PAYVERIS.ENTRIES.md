# PAYVERIS.ENTRIES — Table Schema

> Source: `INSERTS/I_F.PAYVERIS.ENTRIES` in `NAPVPT_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVE.ENTRY.IND` | `PayverisEntries_EntryInd` | TField |  | Entry indicator the value would be "DE" |
| 2 | `PVE.FILE.ID` | `PayverisEntries_FileId` | TField |  | Payveris file identifier. Key to PAYVERIS.FILE |
| 3 | `PVE.BATCH.ID` | `PayverisEntries_BatchId` | TField |  | Id of the batch in the file |
| 4 | `PVE.STATUS` | `PayverisEntries_Status` | TField |  | LOADED � The file is processed and is loaded into Transact. |
| 5 | `PVE.TRANSACTION.TYPE` | `PayverisEntries_TransactionType` | TField |  | The values that are sent in the interface are listed beow values BP PIN � Online bill payments RETURN BILL PAY � Returned payment EXT Transfer � External Transfer Return Transfer � Returned Transfer PIN � Pin transfer |
| 6 | `PVE.TRANSACTION.CODE` | `PayverisEntries_TransactionCode` | TField |  | Values for the field DB for debit transaction CR for credit transaction |
| 7 | `PVE.ROUTING.NO` | `PayverisEntries_RoutingNo` | TField |  | Routing number of the bank |
| 8 | `PVE.ACCOUNT.NO` | `PayverisEntries_AccountNo` | TField |  | Holding account for the batch. |
| 9 | `PVE.AMOUNT` | `PayverisEntries_Amount` | TField |  |  |
| 10 | `PVE.CONFIRMATION.NO` | `PayverisEntries_ConfirmationNo` | TField |  | Confirmation Number |
| 11 | `PVE.CONSUMER.NAME` | `PayverisEntries_ConsumerName` | TField |  | Consumer name |
| 12 | `PVE.TRACE.NO` | `PayverisEntries_TraceNo` | TField |  | Trace Number |
| 13 | `PVE.TXN.DESCRIPTION` | `PayverisEntries_TxnDescription` | TField |  | Transaction Description |
| 14 | `PVE.PAYEE.NAME` | `PayverisEntries_PayeeName` | TField |  | Payee name |
| 15 | `PVE.PAYEE.ACCOUNT.NO` | `PayverisEntries_PayeeAccountNo` | TField |  | Payee account number |
| 16 | `PVE.APPROVAL.IND` | `PayverisEntries_ApprovalInd` | TField |  | Either "Y" or "N" |
| 17 | `PVE.ERROR.CODE` | `PayverisEntries_ErrorCode` | TField |  | 01 to 05 |
| 18 | `PVE.ERROR.MESSAGE` | `PayverisEntries_ErrorMessage` | TField |  | Error Message on posting entry to account |
| 19 | `PVE.INWARD.ENTRY` | `PayverisEntries_InwardEntry` | TField |  |  |
| 20 | `PVE.RECORD.STATUS` | `PayverisEntries_RecordStatus` | String |  |  |
| 21 | `PVE.CURR.NO` | `PayverisEntries_CurrNo` | String |  |  |
| 22 | `PVE.INPUTTER` | `PayverisEntries_Inputter` |  |  |  |
| 23 | `PVE.DATE.TIME` | `PayverisEntries_DateTime` |  |  |  |
| 24 | `PVE.AUTHORISER` | `PayverisEntries_Authoriser` | String |  |  |
| 25 | `PVE.CO.CODE` | `PayverisEntries_CoCode` | String |  |  |
| 26 | `PVE.DEPT.CODE` | `PayverisEntries_DeptCode` | String |  |  |
| 27 | `PVE.AUDITOR.CODE` | `PayverisEntries_AuditorCode` | String |  |  |
| 28 | `PVE.AUDIT.DATE.TIME` | `PayverisEntries_AuditDateTime` | String |  |  |
