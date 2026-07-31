# HUGIRO.SENTANDSETTLED.REPORT — Table Schema

> Source: `INSERTS/I_F.HUGIRO.SENTANDSETTLED.REPORT` in `HUGIRO_IG2SettlementReports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.SSR.CREATION.DATE.TIME` | `HugiroSentandsettledReport_CreationDateTime` |  |  |  |
| 2 | `HU.SSR.SETTLEMENT.DATE` | `HugiroSentandsettledReport_SettlementDate` | TField |  | It is the settlement date for which IG2 is sending this report. |
| 3 | `HU.SSR.MESSAGE.SOURCE` | `HugiroSentandsettledReport_MessageSource` |  |  |  |
| 4 | `HU.SSR.SESSION.NUMBER` | `HugiroSentandsettledReport_SessionNumber` | TField |  | It is the session number for which IG2 is preparing the report. 1 is for the first session, 2 for the second etc. |
| 5 | `HU.SSR.SESSION.ID` | `HugiroSentandsettledReport_SessionId` | TField |  | It is the session ID. |
| 6 | `HU.SSR.RECEIVED.BIC` | `HugiroSentandsettledReport_ReceivedBic` | TField |  | It is the SWIFT BIC of the direct clearing member that receives this report. |
| 7 | `HU.SSR.RECEIVED.BANK.CODE` | `HugiroSentandsettledReport_ReceivedBankCode` | TField |  | It is the bank code of the direct. |
| 8 | `HU.SSR.SENT.CLEARED.TXN.NUMBER` | `HugiroSentandsettledReport_SentClearedTxnNumber` | TField |  | Total number of �sent and cleared� transactions |
| 9 | `HU.SSR.SENT.CLEARED.TXN.AMT` | `HugiroSentandsettledReport_SentClearedTxnAmt` | TField |  | Total amount of �sent and cleared� transactions |
| 10 | `HU.SSR.ORIGINAL.MESSAGE.ID` | `HugiroSentandsettledReport_OriginalMessageId` | TField |  | MsgId of the ICF containing this transaction |
| 11 | `HU.SSR.ORIGINAL.TRANSACTION.ID` | `HugiroSentandsettledReport_OriginalTransactionId` | TField |  | Transaction ID of this transaction |
| 12 | `HU.SSR.ORIGINAL.SETTLEMENT.AMOUNT` | `HugiroSentandsettledReport_OriginalSettlementAmount` | TField |  | Amount of this transaction |
| 13 | `HU.SSR.TRANSACTION.TYPE` | `HugiroSentandsettledReport_TransactionType` |  |  |  |
| 14 | `HU.SSR.TRANSACTION.STATUS` | `HugiroSentandsettledReport_TransactionStatus` |  |  |  |
| 15 | `HU.SSR.ORIGINAL.MESSAGE.ID.T.I` | `HugiroSentandsettledReport_OriginalMessageIdTI` |  |  |  |
| 16 | `HU.SSR.ORIGINAL.TRANSACTION.ID.T.I` | `HugiroSentandsettledReport_OriginalTransactionIdTI` |  |  |  |
| 17 | `HU.SSR.ORIGINAL.SETTLEMENT.AMOUNT.T.I` | `HugiroSentandsettledReport_OriginalSettlementAmountTI` |  |  |  |
| 18 | `HU.SSR.TRANSACTION.TYPE.T.I` | `HugiroSentandsettledReport_TransactionTypeTI` |  |  |  |
| 19 | `HU.SSR.TRANSACTION.STATUS.T.I` | `HugiroSentandsettledReport_TransactionStatusTI` |  |  |  |
