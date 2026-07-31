# HUGIRO.SENTANDROLLEDOVER.REPORT — Table Schema

> Source: `INSERTS/I_F.HUGIRO.SENTANDROLLEDOVER.REPORT` in `HUGIRO_IG2SettlementReports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.SRR.CREATION.DATE.TIME` | `HugiroSentandrolledoverReport_CreationDateTime` |  |  |  |
| 2 | `HU.SRR.SETTLEMENT.DATE` | `HugiroSentandrolledoverReport_SettlementDate` | TField |  | It is the settlement date for which IG2 is sending this report. |
| 3 | `HU.SRR.MESSAGE.SOURCE` | `HugiroSentandrolledoverReport_MessageSource` |  |  |  |
| 4 | `HU.SRR.SESSION.NUMBER` | `HugiroSentandrolledoverReport_SessionNumber` | TField |  | It is the session number for which IG2 is preparing the report. 1 is for the first session, 2 for the second etc. |
| 5 | `HU.SRR.SESSION.ID` | `HugiroSentandrolledoverReport_SessionId` | TField |  | It is the session ID. |
| 6 | `HU.SRR.RECEIVED.BIC` | `HugiroSentandrolledoverReport_ReceivedBic` | TField |  | It is the SWIFT BIC of the direct clearing member that receives this report. |
| 7 | `HU.SRR.RECEIVED.BANK.CODE` | `HugiroSentandrolledoverReport_ReceivedBankCode` | TField |  | It is the bank code of the direct. |
| 8 | `HU.SRR.ROLLEDOVER.NUMBER` | `HugiroSentandrolledoverReport_RolledoverNumber` | TField |  | CTs (Credit Transfers) and / or RCTs (RETURNs) Total number of rolled over transactions |
| 9 | `HU.SRR.ROLLEDOVER.AMOUNT` | `HugiroSentandrolledoverReport_RolledoverAmount` | TField |  | CTs and / or RCTs Total amount of rolled over transactions |
| 10 | `HU.SRR.ORIGINAL.MESSAGE.ID` | `HugiroSentandrolledoverReport_OriginalMessageId` | TField |  | Structure and contents of message and transaction identification depends on the transaction type. |
| 11 | `HU.SRR.ORIGINAL.TRANSACTION.ID` | `HugiroSentandrolledoverReport_OriginalTransactionId` | TField |  | Transaction ID of this transaction |
| 12 | `HU.SRR.ORIGINAL.SETTLEMENT.AMOUNT` | `HugiroSentandrolledoverReport_OriginalSettlementAmount` | TField |  | Interbank Settlement Amount of CT, Returned Interbank Settlement Amount of RCT |
| 13 | `HU.SRR.TRANSACTION.TYPE` | `HugiroSentandrolledoverReport_TransactionType` |  |  |  |
| 14 | `HU.SRR.TRANSACTION.STATUS` | `HugiroSentandrolledoverReport_TransactionStatus` |  |  |  |
| 15 | `HU.SRR.ORIGINAL.MESSAGE.ID.T.I` | `HugiroSentandrolledoverReport_OriginalMessageIdTI` |  |  |  |
| 16 | `HU.SRR.ORIGINAL.TRANSACTION.ID.T.I` | `HugiroSentandrolledoverReport_OriginalTransactionIdTI` |  |  |  |
| 17 | `HU.SRR.ORIGINAL.SETTLEMENT.AMOUNT.T.I` | `HugiroSentandrolledoverReport_OriginalSettlementAmountTI` |  |  |  |
| 18 | `HU.SRR.TRANSACTION.TYPE.T.I` | `HugiroSentandrolledoverReport_TransactionTypeTI` |  |  |  |
| 19 | `HU.SRR.TRANSACTION.STATUS.T.I` | `HugiroSentandrolledoverReport_TransactionStatusTI` |  |  |  |
