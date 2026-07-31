# PI.GPI.TRACKER — Table Schema

> Source: `INSERTS/I_F.PI.GPI.TRACKER` in `PI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GPI.FT.NUMBER` | `PiGpiTracker_FtNumber` | TField |  | Unique id of the transaction in payments hub for which the confirmation is received/sent. |
| 2 | `GPI.FT.NUMBER.COVER` | `PiGpiTracker_FtNumberCover` | TField |  |  |
| 3 | `GPI.OVERALL.STATUS.CODE` | `PiGpiTracker_OverallStatusCode` | TField |  | Specifies the Overall status of the transaction in a coded form Values are:ACSC/ACCC - AcceptedSettlementCompleted ACSP - AcceptedSettlementInProcess RJCT - Rejected |
| 4 | `GPI.OVERALL.REASON.CODE` | `PiGpiTracker_OverallReasonCode` | TField |  | Provides more details on the status in process or rejection (like G000, G001, G002, G004, AC04) |
| 5 | `GPI.INITIATION.TIME` | `PiGpiTracker_InitiationTime` | TField |  | Date and Time at which the message enters the tracking system (e.g. gpi) Applicable only forgetTransactionDetailsAPI.To be stored in UTC format |
| 6 | `GPI.LAST.UPDATE.TIME` | `PiGpiTracker_LastUpdateTime` |  |  |  |
| 7 | `GPI.COMPLETION.TIME` | `PiGpiTracker_CompletionTime` | TField |  | Date and time based on the creation date of the status confirmation containing a final status ACSC.To be storedin UTC format |
| 8 | `GPI.MESSAGE.NAME.IDENTIFICATION` | `PiGpiTracker_MessageNameIdentification` |  |  |  |
| 9 | `GPI.DIRECTION` | `PiGpiTracker_Direction` |  |  |  |
| 10 | `GPI.RESERVED.15` | `PiGpiTracker_Reserved15` |  |  |  |
| 11 | `GPI.RESERVED.14` | `PiGpiTracker_Reserved14` |  |  |  |
| 12 | `GPI.RESERVED.13` | `PiGpiTracker_Reserved13` |  |  |  |
| 13 | `GPI.RESERVED.12` | `PiGpiTracker_Reserved12` |  |  |  |
| 14 | `GPI.RESERVED.11` | `PiGpiTracker_Reserved11` |  |  |  |
| 15 | `GPI.TRANSACTION.EVENT.TYPE` | `PiGpiTracker_TransactionEventType` |  |  |  |
| 16 | `GPI.NETWORK.REFERENCE` | `PiGpiTracker_NetworkReference` |  |  |  |
| 17 | `GPI.INSTRUCTION.IDENTIFICATION` | `PiGpiTracker_InstructionIdentification` |  |  |  |
| 18 | `GPI.RELATED.REFERENCE` | `PiGpiTracker_RelatedReference` |  |  |  |
| 19 | `GPI.STATUS.CODE` | `PiGpiTracker_StatusCode` |  |  |  |
| 20 | `GPI.REASON.CODE` | `PiGpiTracker_ReasonCode` |  |  |  |
| 21 | `GPI.SEVERITY` | `PiGpiTracker_Severity` |  |  |  |
| 22 | `GPI.INVALIDITY.REASON` | `PiGpiTracker_InvalidityReason` |  |  |  |
| 23 | `GPI.INVALIDITY.DESCRIPTION` | `PiGpiTracker_InvalidityDescription` |  |  |  |
| 24 | `GPI.ORIGINATOR.AGENT` | `PiGpiTracker_OriginatorAgent` |  |  |  |
| 25 | `GPI.FORWARDED.TO.AGENT` | `PiGpiTracker_ForwardedToAgent` |  |  |  |
| 26 | `GPI.SETTLEMENT.METHOD` | `PiGpiTracker_SettlementMethod` |  |  |  |
| 27 | `GPI.CLEARING.SYSTEM` | `PiGpiTracker_ClearingSystem` |  |  |  |
| 28 | `GPI.STATUS.UPDATE.TIME` | `PiGpiTracker_StatusUpdateTime` |  |  |  |
| 29 | `GPI.FUNDS.AVAILABLE.TIME` | `PiGpiTracker_FundsAvailableTime` |  |  |  |
| 30 | `GPI.CONFIRMED.AMOUNT` | `PiGpiTracker_ConfirmedAmount` |  |  |  |
| 31 | `GPI.CONFIRMED.AMOUNT.CURRENCY` | `PiGpiTracker_ConfirmedAmountCurrency` |  |  |  |
| 32 | `GPI.CHARGE.BEARER` | `PiGpiTracker_ChargeBearer` |  |  |  |
| 33 | `GPI.CHARGE.AMOUNT` | `PiGpiTracker_ChargeAmount` |  |  |  |
| 34 | `GPI.FOREIGN.EXCHANGE.RATE` | `PiGpiTracker_ForeignExchangeRate` |  |  |  |
| 35 | `GPI.DEBTOR` | `PiGpiTracker_Debtor` |  |  |  |
| 36 | `GPI.DEBTOR.AGENT` | `PiGpiTracker_DebtorAgent` |  |  |  |
| 37 | `GPI.INTERMEDIARY.AGENT1` | `PiGpiTracker_IntermediaryAgent1` |  |  |  |
| 38 | `GPI.INSTRUCTNG.REIMBURSEMENT.AGT` | `PiGpiTracker_InstructngReimbursementAgt` |  |  |  |
| 39 | `GPI.CREDITOR` | `PiGpiTracker_Creditor` |  |  |  |
| 40 | `GPI.CREDITOR.AGENT` | `PiGpiTracker_CreditorAgent` |  |  |  |
| 41 | `GPI.SENDER.ACK.RECEIPT` | `PiGpiTracker_SenderAckReceipt` |  |  |  |
| 42 | `GPI.RECEIVED.DATE` | `PiGpiTracker_ReceivedDate` |  |  |  |
| 43 | `GPI.INSTRUCTED.AMOUNT` | `PiGpiTracker_InstructedAmount` |  |  |  |
| 44 | `GPI.INSTRUCTED.AMOUNT.CURRENCY` | `PiGpiTracker_InstructedAmountCurrency` |  |  |  |
| 45 | `GPI.INTERBANK.SETTLEMENT.AMOUNT` | `PiGpiTracker_InterbankSettlementAmount` |  |  |  |
| 46 | `GPI.INTERBANK.SETTLEMENT.CURRENCY` | `PiGpiTracker_InterbankSettlementCurrency` |  |  |  |
| 47 | `GPI.INTERBANK.SETTLEMENT.DATE` | `PiGpiTracker_InterbankSettlementDate` |  |  |  |
| 48 | `GPI.FROM.AGENT` | `PiGpiTracker_FromAgent` |  |  |  |
| 49 | `GPI.EB.FREE.MESSAGE.ID` | `PiGpiTracker_EbFreeMessageId` |  |  |  |
| 50 | `GPI.END.TO.END.REF` | `PiGpiTracker_EndToEndRef` |  |  |  |
| 51 | `GPI.RESERVED.8` | `PiGpiTracker_Reserved8` |  |  |  |
| 52 | `GPI.RESERVED.7` | `PiGpiTracker_Reserved7` |  |  |  |
| 53 | `GPI.RESERVED.6` | `PiGpiTracker_Reserved6` |  |  |  |
| 54 | `GPI.CANCELLATION.STATUS` | `PiGpiTracker_CancellationStatus` | TField |  | This field indicates the status of a cancellation request sent or received for a payment Possible Values: CNCL, PDCR and RJCR CNCL CancelledAsPerRequest : Used when a requested cancellation is successful PDCR PendingCancellationRequest : Used when a requested cancellation is pending RJCR RejectedCancellationRequest : Used when a requested cancellation has been rejected |
| 55 | `GPI.RESERVED.4` | `PiGpiTracker_Reserved4` | TField |  |  |
| 56 | `GPI.RESERVED.3` | `PiGpiTracker_Reserved3` | TField |  |  |
| 57 | `GPI.RESERVED.2` | `PiGpiTracker_Reserved2` | TField |  |  |
| 58 | `GPI.RESERVED.1` | `PiGpiTracker_Reserved1` | TField |  |  |
| 59 | `GPI.LOCAL.REF` | `PiGpiTracker_LocalRef` |  |  |  |
| 60 | `GPI.OVERRIDE` | `PiGpiTracker_Override` |  |  |  |
