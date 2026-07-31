# DD.MANDATE.RECEIVED.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.RECEIVED.TRANSACTIONS` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MRT.COMPANY.ID` | `DdMandateReceivedTransactions_CompanyId` | TField |  | The Transact Company for which the file is received. |
| 2 | `DD.MRT.FILE.ID` | `DdMandateReceivedTransactions_FileId` | TField |  | The id of DD Mandate Received Files corresponding to the file in which the request has been received, allocated by Transact. |
| 3 | `DD.MRT.BULK.ID` | `DdMandateReceivedTransactions_BulkId` | TField |  | The id of DD Mandate Received Bulks corresponding to the file in which the request has been received, allocated by Transact. |
| 4 | `DD.MRT.FILE.REFERENCE` | `DdMandateReceivedTransactions_FileReference` | TField |  | File Reference of the sender. |
| 5 | `DD.MRT.BULK.REFERENCE` | `DdMandateReceivedTransactions_BulkReference` | TField |  | Bulk Reference of the sender. |
| 6 | `DD.MRT.CREATE.DATE.TIME` | `DdMandateReceivedTransactions_CreateDateTime` |  |  |  |
| 7 | `DD.MRT.RECEIVED.DATE` | `DdMandateReceivedTransactions_ReceivedDate` | TField |  | The business server date, which will populate when the file is received. It will be used in the archival process of the received files |
| 8 | `DD.MRT.DIRECTION` | `DdMandateReceivedTransactions_Direction` | TField |  | Indicates if the request is sent or received. |
| 9 | `DD.MRT.MESSAGE.TYPE` | `DdMandateReceivedTransactions_MessageType` | TField |  | The Bulk Type from DD.MANDATES.BULK.DETAILS pain.009, pain.010, pain.011, pain.012S. |
| 10 | `DD.MRT.REQUEST.ID` | `DdMandateReceivedTransactions_RequestId` | TField |  | The id of the New or Amend or Cancel Mandate request provided by the initiator. |
| 11 | `DD.MRT.PAYLOAD` | `DdMandateReceivedTransactions_Payload` | TField |  | The individual pain.009, pain.010, pain.011 message. |
| 12 | `DD.MRT.INSTRUCTING.AGENT` | `DdMandateReceivedTransactions_InstructingAgent` | TField |  | Sender of the bulk. |
| 13 | `DD.MRT.INSTRUCTED.AGENT` | `DdMandateReceivedTransactions_InstructedAgent` | TField |  | Receiver of the Bulk. |
| 14 | `DD.MRT.CREDITOR.AGENT` | `DdMandateReceivedTransactions_CreditorAgent` | TField |  | The Creditor Bank. |
| 15 | `DD.MRT.DEBTOR.AGENT` | `DdMandateReceivedTransactions_DebtorAgent` | TField |  | The Debtor Bank. |
| 16 | `DD.MRT.MANDATE.SERVICE` | `DdMandateReceivedTransactions_MandateService` | TField |  | Defaulted from Source. |
| 17 | `DD.MRT.PAYMENT.SERVICE` | `DdMandateReceivedTransactions_PaymentService` | TField |  | The Payment Service Level, which will be used while retrieving the DD Mandate when the DD collection is received. |
| 18 | `DD.MRT.LOCAL.INST` | `DdMandateReceivedTransactions_LocalInst` | TField |  | The Service Level, which will be used while retrieving the DD Mandate when the DD collection is received. |
| 19 | `DD.MRT.RESERVED.1` | `DdMandateReceivedTransactions_Reserved1` | TField |  | Reserved for future use. |
| 20 | `DD.MRT.ORIGINATED.BY` | `DdMandateReceivedTransactions_OriginatedBy` | TField |  | Capture who originated the DD mandate. Valid options are Debtor or Creditor. |
| 21 | `DD.MRT.MANDATE.TYPE` | `DdMandateReceivedTransactions_MandateType` | TField |  | The type of the mandate.Valid options are Paper or Electronic. |
| 22 | `DD.MRT.MANDATE.REF` | `DdMandateReceivedTransactions_MandateRef` | TField |  | The Unique Mandate Reference. |
| 23 | `DD.MRT.CREDITOR.ID` | `DdMandateReceivedTransactions_CreditorId` | TField |  | The Creditor ID. |
| 24 | `DD.MRT.DEBIT.ACCOUNT` | `DdMandateReceivedTransactions_DebitAccount` | TField |  | The Debtor account number. |
| 25 | `DD.MRT.DEBIT.IBAN` | `DdMandateReceivedTransactions_DebitIban` | TField |  | The Debtor IBAN. |
| 26 | `DD.MRT.ORIGINAL.MANDATE.REF` | `DdMandateReceivedTransactions_OriginalMandateRef` | TField |  | The Original Mandate Reference. |
| 27 | `DD.MRT.ORIGINAL.CREDITOR.ID` | `DdMandateReceivedTransactions_OriginalCreditorId` | TField |  | The Original Creditor Id. |
| 28 | `DD.MRT.ORIGINAL.DEBTOR.ACCOUNT` | `DdMandateReceivedTransactions_OriginalDebtorAccount` | TField |  | The Original debtor account. |
| 29 | `DD.MRT.DD.MANDATE.ID` | `DdMandateReceivedTransactions_DdMandateId` | TField |  | The Id of the DD.DDI. |
| 30 | `DD.MRT.STATUS` | `DdMandateReceivedTransactions_Status` | TField |  | The Status of the request: RECEIVED, PROCESSED, CONFIRMED, REJECTED. |
| 31 | `DD.MRT.ERROR.CODE` | `DdMandateReceivedTransactions_ErrorCode` | TField |  | Contains the ISO Reason Code corresponding to the T24 Error Id raised during validations. |
| 32 | `DD.MRT.ERROR.REASON` | `DdMandateReceivedTransactions_ErrorReason` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 33 | `DD.MRT.ACCEPTANCE.STATUS` | `DdMandateReceivedTransactions_AcceptanceStatus` | TField |  | Acceptance Status could be ACCEPTED or REJECTED based on inward Mandate Acceptance report(pain.012) from Creditor Bank. The Acceptance status is updated in the corresponding DD.MANDATE.REQUEST for further process flow of amending/cancelling DD Mandate Request. |
| 34 | `DD.MRT.ACCEPTANCE.RSN.CODE` | `DdMandateReceivedTransactions_AcceptanceRsnCode` | TField |  | The reason code updated based on the inward Mandate acceptance report(pain.012) from a Creditor Bank.Indicates Success or the reason code for the original amend/cancel request. |
| 35 | `DD.MRT.ORIG.FILE.REF` | `DdMandateReceivedTransactions_OrigFileRef` |  |  |  |
| 36 | `DD.MRT.ORIG.BULK.REF` | `DdMandateReceivedTransactions_OrigBulkRef` |  |  |  |
| 37 | `DD.MRT.ORIG.MSG.TYPE` | `DdMandateReceivedTransactions_OrigMsgType` |  |  |  |
