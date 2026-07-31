# DD.MANDATE.SENT.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.SENT.TRANSACTIONS` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MST.COMPANY.ID` | `DdMandateSentTransactions_CompanyId` | TField |  | The Transact Company for which the file is sent. |
| 2 | `DD.MST.RECEIVED.FILE.ID` | `DdMandateSentTransactions_ReceivedFileId` | TField |  | The id of DD Mandate Received Files corresponding to the file in which the request has been received, allocated by Transact. |
| 3 | `DD.MST.RECEIVED.BULK.ID` | `DdMandateSentTransactions_ReceivedBulkId` | TField |  | The id of DD Mandate Received Bulks corresponding to the file in which the request has been received, allocated by Transact. |
| 4 | `DD.MST.ORIGINAL.TXN.ID` | `DdMandateSentTransactions_OriginalTxnId` | TField |  | Only for acceptance confirmations pain.012 - the id of the original request in DD Mandate Received Transactions. |
| 5 | `DD.MST.FILE.REFERENCE` | `DdMandateSentTransactions_FileReference` | TField |  | The reference of the outward bulk in which the message is sent to the central mandate service. |
| 6 | `DD.MST.BULK.REFERENCE` | `DdMandateSentTransactions_BulkReference` | TField |  | The reference of the outward file in which the message is sent to central mandate service. |
| 7 | `DD.MST.MESSAGE.TYPE` | `DdMandateSentTransactions_MessageType` | TField |  | Message Type. Currently only pain.012. |
| 8 | `DD.MST.ORIGINAL.MESSAGE.TYPE` | `DdMandateSentTransactions_OriginalMessageType` | TField |  | The Message Type of the received request. Only for pain.012. |
| 9 | `DD.MST.MANDATE.SERVICE` | `DdMandateSentTransactions_MandateService` | TField |  | The Mandate Service. |
| 10 | `DD.MST.REQUEST.ID` | `DdMandateSentTransactions_RequestId` | TField |  | The id of the New or Amend or Cancel Mandate request provided by the initiator. |
| 11 | `DD.MST.MANDATE.REF` | `DdMandateSentTransactions_MandateRef` | TField |  | The Unique Mandate Reference. |
| 12 | `DD.MST.CREDITOR.ID` | `DdMandateSentTransactions_CreditorId` | TField |  | The Creditor ID. |
| 13 | `DD.MST.CREATE.DATE.TIME` | `DdMandateSentTransactions_CreateDateTime` |  |  |  |
| 14 | `DD.MST.PROCESSED.DATE` | `DdMandateSentTransactions_ProcessedDate` | TField |  | The business server date, when the inward processing file is processed. It will be used in the archival process of the processed files |
| 15 | `DD.MST.PAYMENT.SERVICE` | `DdMandateSentTransactions_PaymentService` | TField |  | The Payment Service Level, which will be used while retrieving the DD Mandate when the DD collection is received. |
| 16 | `DD.MST.LOCAL.INST` | `DdMandateSentTransactions_LocalInst` | TField |  | The Service Level, which will be used while retrieving the DD Mandate when the DD collection is received. |
| 17 | `DD.MST.DEBIT.ACCOUNT` | `DdMandateSentTransactions_DebitAccount` | TField |  | The account number of the Debitor. |
| 18 | `DD.MST.DEBIT.IBAN` | `DdMandateSentTransactions_DebitIban` | TField |  | The Debtor IBAN. |
| 19 | `DD.MST.INSTG.AGENT.BIC` | `DdMandateSentTransactions_InstgAgentBic` | TField |  | Sender of the message. For acceptance confirmations, this will be the Instructing Agent of the original request. |
| 20 | `DD.MST.INSTD.AGENT.BIC` | `DdMandateSentTransactions_InstdAgentBic` | TField |  | Receiver of the Bulk. For acceptance cofirmations, this will be the Instructing Agent of the original request. |
| 21 | `DD.MST.CREDITOR.AGENT` | `DdMandateSentTransactions_CreditorAgent` | TField |  | The Creditor Bank. |
| 22 | `DD.MST.DEBTOR.AGENT` | `DdMandateSentTransactions_DebtorAgent` | TField |  | The Debtor Bank. |
| 23 | `DD.MST.DD.MANDATE.ID` | `DdMandateSentTransactions_DdMandateId` | TField |  | The Id of the DD.DDI. |
| 24 | `DD.MST.STATUS` | `DdMandateSentTransactions_Status` | TField |  | The Status of the request: NEW, PROCESSED, SENT, COMPLETED, ERROR, ACCREJ. |
| 25 | `DD.MST.ERROR.CODE` | `DdMandateSentTransactions_ErrorCode` | TField |  | Contains the ISO Reason Code corresponding to the T24 Error Id raised during validations. |
| 26 | `DD.MST.ERROR.REASON` | `DdMandateSentTransactions_ErrorReason` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 27 | `DD.MST.ACCEPTANCE.STATUS` | `DdMandateSentTransactions_AcceptanceStatus` | TField |  | Acceptance Status can be ACCEPTED or REJECTED. For outward acceptance confirmations only. |
| 28 | `DD.MST.ACCEPTANCE.RSN.CODE` | `DdMandateSentTransactions_AcceptanceRsnCode` | TField |  | For acceptance confirmations only. Indicates the success or reason code for the original request. |
| 29 | `DD.MST.FILE.NAME` | `DdMandateSentTransactions_FileName` | TField |  | The name of the sent file. |
| 30 | `DD.MST.MANDATE.REQUEST.ID` | `DdMandateSentTransactions_MndtReqId` |  |  |  |
| 31 | `DD.MST.AMEND.REASON.CODE` | `DdMandateSentTransactions_AmendRsnCode` |  |  |  |
| 32 | `DD.MST.AMEND.REASON.DESC` | `DdMandateSentTransactions_AmendRsnDesc` |  |  |  |
| 33 | `DD.MST.CANCEL.REASON.CODE` | `DdMandateSentTransactions_CancelRsnCode` |  |  |  |
| 34 | `DD.MST.CANCEL.REASON.DESC` | `DdMandateSentTransactions_CancelRsnDesc` |  |  |  |
| 35 | `DD.MST.ORIG.DEBIT.ACCOUNT` | `DdMandateSentTransactions_OrigDebitAccount` | TField |  | The Original Debtor Account for a Mandate Request, when request type is Amend. |
| 36 | `DD.MST.ORIG.DEBIT.IBAN` | `DdMandateSentTransactions_OrigDebitIban` | TField |  | The Original Debtor IBAN for a Mandate Request, when request type is Amend. |
| 37 | `DD.MST.RESUBMITTED.SENT.TXN` | `DdMandateSentTransactions_ResubmittedSentTxn` | TField |  | The field to store the Resubmitted Sent Transaction. During the Resubmission process, the rejected Sent Transaction will be marked as Resubmitted and will create the new Sent Transaction, in which the Resubmitted Sent Transaction will be tracked using this field. |
| 38 | `DD.MST.RESERVED.1` | `DdMandateSentTransactions_Reserved1` | TField |  |  |
| 39 | `DD.MST.LOCAL.REF` | `DdMandateSentTransactions_LocalRef` |  |  |  |
| 40 | `DD.MST.OVERRIDE` | `DdMandateSentTransactions_Override` |  |  |  |
| 41 | `DD.MST.RECORD.STATUS` | `DdMandateSentTransactions_RecordStatus` | String |  |  |
| 42 | `DD.MST.CURR.NO` | `DdMandateSentTransactions_CurrNo` | String |  |  |
| 43 | `DD.MST.INPUTTER` | `DdMandateSentTransactions_Inputter` |  |  |  |
| 44 | `DD.MST.DATE.TIME` | `DdMandateSentTransactions_DateTime` |  |  |  |
| 45 | `DD.MST.AUTHORISER` | `DdMandateSentTransactions_Authoriser` | String |  |  |
| 46 | `DD.MST.CO.CODE` | `DdMandateSentTransactions_CoCode` | String |  |  |
| 47 | `DD.MST.DEPT.CODE` | `DdMandateSentTransactions_DeptCode` | String |  |  |
| 48 | `DD.MST.AUDITOR.CODE` | `DdMandateSentTransactions_AuditorCode` | String |  |  |
| 49 | `DD.MST.AUDIT.DATE.TIME` | `DdMandateSentTransactions_AuditDateTime` | String |  |  |
