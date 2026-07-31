# EB.QUERIES.ANSWERS — Table Schema

> Source: `INSERTS/I_F.EB.QUERIES.ANSWERS` in `QA_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.QA.ORG.DE.O.HEADER` | `EbQueriesAnswers_OrgDeOHeader` | TField | Yes | Specifies the ID of the Outward Message Header. This field is mandatory for cancellation messages (MTn92), but otherwise either this field or the ORG.DE.I.HEADER field can be input. This field defaults the ORIGINAL.MSG.TYPE, ORIGINAL.DATE, REL.REFERENCE and ORG.MSG.FIELD fields when input. Validation Rules: Must be a valid record on the F.DE.O.HEADER File. |
| 2 | `EB.QA.ORG.DE.I.HEADER` | `EbQueriesAnswers_OrgDeIHeader` | TField |  | Specifies the ID of the Inward Message Header. Either this field or the ORG.DE.O.HEADER field can be input. This field is invalid for cancellation messages (MTn92), but otherwise either this field or the ORG.DE.I.HEADER field can be input. This field defaults the ORIGINAL.MSG.TYPE, ORIGINAL.DATE, REL.REFERENCE and ORG.MSG.FIELD fields when input. Validation Rules: Must be a valid record on the F.DE.I.HEADER File. |
| 3 | `EB.QA.INWARD.DE.I.HEADER` | `EbQueriesAnswers_InwardDeIHeader` | TField |  | Specifies the ID of the Inward Message Header. This NOINPUT is populated automatically for Incoming messages only. This field defaults the ORIGINAL.MSG.TYPE, ORIGINAL.DATE, REL.REFERENCE and ORG.MSG.FIELD of the Incoming Message. Validation Rules: Must be a valid record on the F.DE.I.HEADER File. |
| 4 | `EB.QA.ORIGINAL.MSG.TYPE` | `EbQueriesAnswers_OriginalMsgType` | TField | Conditional | This field specifies the message type of the original message to which this cancellation, query or answer relates. Mandatory if MSG.CNTL.SUFFIX field is&amp;#145;92&amp;#146;, otherwise optional. SWIFT Category 3 &amp; 9 Messages are not Allowed, i.e. 300, 320, 900 etc. This field will be populated automatically and made no input when either the ORG.DE.O.HEADER or ORG.DE.I.HEADER field is input. Validation Rules: 1-4 numeric characters. Must be a valid record on the DE.MESSAGE file. |
| 5 | `EB.QA.ORIGINAL.DATE` | `EbQueriesAnswers_OriginalDate` | TField | Conditional | This field is used to retain the original date on which the original message was sent. Validation Rules: Up to 9 type D date characters (Date format in range 1950 to 2049). This field will be populated automatically and made no input when either the DE.O.HEADER.ID or DE.O.HEADER.ID field is input. Mandatory if MSG.CNTL.SUFFIX field is&amp;#145;92&amp;#146;, otherwise optional. |
| 6 | `EB.QA.REL.REFERENCE` | `EbQueriesAnswers_RelReference` | S (SWIFT) | Yes | This field contains the content of field 20 (Transaction Reference Number) of the original S.W.I.F.T Message to which the Cancellation, Query or Answer relates. It is automatically populated when ORG.DE.O.HEADER, ORG.DE.I.HEADER or INWARD.DE.I.HEADER is completed. Validation Rules: Mandatory Field Up to 16 type S (SWIFT) characters. This field must not start or end with a &amp;#145;/&amp;#146; and must not contain two consecutive slashes &amp;#145;//&amp;#146; (SWIFT Error Code T26) |
| 7 | `EB.QA.NARRATIVE` | `EbQueriesAnswers_Narrative` |  |  |  |
| 8 | `EB.QA.ORG.MSG.NARR` | `EbQueriesAnswers_OrgMsgNarr` |  |  |  |
| 9 | `EB.QA.ORG.MSG.FIELD` | `EbQueriesAnswers_OrgMsgField` |  |  |  |
| 10 | `EB.QA.CUSTOMER.NO` | `EbQueriesAnswers_CustomerNo` | TField |  | Input must be an existing CUSTOMER on the Customer File. The Customer&amp;#146;s SWIFT Address must be held on the DE.ADDRESS File. If this field is completed and a Swift BIC address is entered in the RECV.ADDR field, then the CUSTOMER.NO field takes precedent. Validation Rules: 3 -10 type MNE (0-9, or A-Z uppercase alpha) or '.' or 1-10 Numeric character Customer Code. |
| 11 | `EB.QA.RECV.ADDR` | `EbQueriesAnswers_RecvAddr` |  |  |  |
| 12 | `EB.QA.EB.ADVICE.NO` | `EbQueriesAnswers_EbAdviceNo` | TField | Yes | This field is the key to EB.ACTIVITY and EB.ADVICES numbers. It determines the message types to be sent and the mappings to be used. Mandatory Input for all Outward SWIFT Messages. MT MT Name Purpose n92 Request for Cancellation Request the receiver to consider cancellation of the message identified in the request. n95 Queries Request information relating to a previous message or amendment to a previous message. n96 Answers Responds to a MT n95 (Queries Message) or MT n92 (Request for Cancellation) or other messages where no specific message type has been provided for the response. Validation Rules: A valid record ID in EB.ADVICES. Valid inputs are SWIFT Message Types MTn92, MTn95 and MTn96 where n stands for Message Category 1,2,4,5,6,7 or 8. |
| 13 | `EB.QA.MSG.CNTL.SUFFIX` | `EbQueriesAnswers_MsgCntlSuffix` | TField |  | This noinput field will control whether the query or answer field will be allowed to input. Identifies the type of message to be raised, i.e. Cancellation, Queries or Answers. Valid input will be &amp;#145;92&amp;#146;, &amp;#145;95&amp;#146; or &amp;#145;96&amp;#146;. This field is driven from the Message type as held for the EB.ADVICE.NO . If 92 is present, QUERY and ANSWER fields should be disabled. If 95 is present, QUERY field should be enabled for input, otherwise disable. If 96 is present, ANSWER field should be enabled for input, otherwise disable. Validation Rules: Automatically generated field from the EB.ADVICE.NO field. No input possible. |
| 14 | `EB.QA.MSG.CNTL.CATEGORY` | `EbQueriesAnswers_MsgCntlCategory` | TField |  | This noinput field is driven from the Message type as held for the EB.ADVICE.NO. Valid input will be 1,2,3, 4,5,6,7, 8 or 9. Where Customer Transfers and Cheques Financial Institution Transfers Foreign Exchange, Money Market and Derivatives Collections and Cash Letters Securities Markets Precious Metals and Syndication Documentary Credits and Guarantees Travellers Cheques Cash Management &amp; Customer Status Validation Rules: Automatically generated field from the EB.ADVICE.NO field. No input possible. |
| 15 | `EB.QA.QUERY` | `EbQueriesAnswers_Query` |  |  |  |
| 16 | `EB.QA.ANSWER` | `EbQueriesAnswers_Answer` |  |  |  |
| 17 | `EB.QA.ASSIGNED.TO` | `EbQueriesAnswers_AssignedTo` |  |  |  |
| 18 | `EB.QA.DIRECTION` | `EbQueriesAnswers_Direction` | TField |  | Indicates the direction of the message. Validation Rules: Valid inputs are INWARD or OUTWARD. No input field. |
| 19 | `EB.QA.STATUS` | `EbQueriesAnswers_Status` | TField |  | Indicates the status of the message. Validation Rules: Valid will be listed as per EB.LOOKUP list. No input field |
| 20 | `EB.QA.SEND.NOTICE` | `EbQueriesAnswers_SendNotice` |  |  |  |
| 21 | `EB.QA.ACTIVITY.CODE` | `EbQueriesAnswers_ActivityCode` |  |  |  |
| 22 | `EB.QA.ACTIVITY.DATE` | `EbQueriesAnswers_ActivityDate` |  |  |  |
| 23 | `EB.QA.MAPPING.KEY` | `EbQueriesAnswers_MappingKey` |  |  |  |
| 24 | `EB.QA.DELIVERY.REF` | `EbQueriesAnswers_DeliveryRef` |  |  |  |
| 25 | `EB.QA.MSG.SENT.RECVD` | `EbQueriesAnswers_MsgSentRecvd` | TField |  | The common group messages can be used when querying or responding to messages Received or Messages Sent. The SWIFT messages themselves indicate the Message, Message Date and Message Direction (Sent or Received). This field is used to provide the correct tag for the SWIFT message and is based on the T24 message reference or the User input. For messages sent from T24 (ref such as D2002121274782374) this would default to S for Sent. For messages received by T24 (such as R20021212243242) it would default to R for Received. If the User is entering a free format query without using the T24 reference then the value needs to be set manually. Validation Rules: Acceptable values of S or R Defaults according to T24 delivery reference |
| 26 | `EB.QA.IN.TXN.REF` | `EbQueriesAnswers_InTxnRef` | TField |  | This field is used to hold the contents of Tag 20 while processing an inward n92, n95 or n96 message. |
| 27 | `EB.QA.ORIGINATOR.BIC` | `EbQueriesAnswers_OriginatorBic` | TField |  | Specifies the originator business identifier code of the cancellation message. Cannot be used if Originator Name is present (RECV.ADDR) Validation Rules: Should be valid 8 to 12 characters and should be valid BIC |
| 28 | `EB.QA.ISO.CANCEL.REASON.CODE` | `EbQueriesAnswers_IsoCancelReasonCode` | TField |  | Specifies the ISO reason code provided by the originating party of the cancellation request. Used to map tag 79 of n92 message along with Original message narrative. Validation Rules: 4 characters of alphatypenumeric Allowed codes as per ISO are DuplicatePayment[DUPL],IncorrectAgent[AGNT],IncorrectCurrency[CURR],RequestedByCustomer[CUST],UnduePayment[UPAY],CancelUponUnableToApply[CUTA],TechnicalProblem[TECH],FraudulentOrigin[FRAD],CoverCancelledOrReturned[COVR],WrongAmount[AM09] |
| 29 | `EB.QA.CANCEL.REASON.CODE` | `EbQueriesAnswers_CancelReasonCode` | TField |  | Specifies the ISO reason code provided by the originating party of the cancellation request. If Reason ISO code is provided then this proprietary reason field cannot be entered Validation Rules: 35 characters of alphatypenumeric |
| 30 | `EB.QA.CANCEL.ADDL.INFO` | `EbQueriesAnswers_CancelAddlInfo` |  |  |  |
| 31 | `EB.QA.ISO.REJ.REASON.CDE` | `EbQueriesAnswers_IsoRejReasonCde` | TField |  | Specifies the ISO reject reason code provided by the operator in case he is rejecting a cancellation request or if a reject message is received for an outward cancellation request. Validation Rules: 4 characters of alphatypenumeric Allowed codes as per ISO are CUST (Beneficiary's Refusal),LEGL (Legal reason, in relation with index 4.94),ARDT (The transaction has already been returned),AC04 (Account closed),AM04 (Insufficient funds on the account),NOAS (No response from beneficiary),NOOR (Original Credit Transfer never received) |
| 32 | `EB.QA.REJ.REASON.CDE` | `EbQueriesAnswers_RejReasonCde` | TField |  | Specifies the proprietary reason code for rejection cancellation request. If no Reason ISO code is provided then this proprietary reason must be filled. If Reason ISO code is provided then this proprietary reason field cannot be entered Validation Rules: 35 characters of alphatypenumeric |
| 33 | `EB.QA.REJECT.ADDL.INFO` | `EbQueriesAnswers_RejectAddlInfo` |  |  |  |
| 34 | `EB.QA.ISO.CLR.REASON.CODE` | `EbQueriesAnswers_IsoClrReasonCode` | TField |  | Specifies the ISO clearing reason code for a the cancellation request Validation Rules: 4 characters of alphatypenumeric |
| 35 | `EB.QA.CLR.REASON.CODE` | `EbQueriesAnswers_ClrReasonCode` | TField |  | Specifies the proprietary clearing reason code for the cancellation request Validation Rules: 35 characters of alphatypenumeric |
| 36 | `EB.QA.CLR.ADDL.INFO` | `EbQueriesAnswers_ClrAddlInfo` | TField |  | Specifies Additional information for the Clearing reason Validation Rules: 105 characters of alphatypenumeric |
| 37 | `EB.QA.ACCEPT.REJECT` | `EbQueriesAnswers_AcceptReject` | TField |  | This field represents the user action for a cancellation request. Possible values are - Accept, Reject, Pending, Partial Accept Accept - Accepting the Cancellation Request. On accepting the cancellation request, positive ROI (if configured for that clearing) and Return message will be triggered for the transaction. Reject - Rejecting the Cancellation Request. On rejecting, negative ROI message will be triggered. Pending - Sending interim response for the Cancellation Request. On selecting this option, Pending ROI message will be triggered (if configured for that clearing). Partial Accept - Partially accepting the Cancellation Request. User can select this option only if it is allowed for that clearing. On selecting this option, user must enter the return amount less than the original transaction amount. Validation: Pending Action is allowed by the system only when "Allowed ROI response" field of PP.CLEARING is configured to allow pending. 35 characters of alphatypenumeric |
| 38 | `EB.QA.ACPT.REASON.INFO` | `EbQueriesAnswers_AcptReasonInfo` |  |  |  |
| 39 | `EB.QA.AUTH.REJ.REASON` | `EbQueriesAnswers_AuthRejReason` | TField |  | Specifies reason for rejecting the authorisation of the cancellation request. This field is filled if the cancellation request has been rejected (not approved) as a result of authorization. Validation Rules: 140 characters of type alphatypenumeric |
| 40 | `EB.QA.ORIG.INTBK.SET.DTE` | `EbQueriesAnswers_OrigIntbkSetDte` | TField |  | Date, as provided in the original transaction, on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due. Validation Rules: Up to 8 type D date characters |
| 41 | `EB.QA.ISO.MSG.TYPE` | `EbQueriesAnswers_IsoMsgType` | TField |  | Specifies the message name identifier to which the message refers, eg, pacs.003.001.01 or MT103. Validation Rules: 35 characters of type alphatypenumeric |
| 42 | `EB.QA.REJ.MSG.TYPE` | `EbQueriesAnswers_RejMsgType` | TField |  | Specifies the message name identifier in case the cancellation request is rejected Validation Rules: 35 characters of type alphatypenumeric |
| 43 | `EB.QA.CLR.MSG.TYPE` | `EbQueriesAnswers_ClrMsgType` | TField |  |  |
| 44 | `EB.QA.ORIG.MSG.TYPE` | `EbQueriesAnswers_OrigMsgType` | TField |  | Specifies the original message name identifier to which the message refers, eg, pacs.003.001.01 or MT103. Validation Rules: 35 characters of type alphatypenumeric |
| 45 | `EB.QA.ORIG.TXN.TYPE` | `EbQueriesAnswers_OrigTxnType` | TField |  | Specifies the original transaction type for which the cancellation request was sent. For example CT for Credit Transfer, DD for Direct Debits Validation Rules: 4 characters of type alphatypenumeric |
| 46 | `EB.QA.CLEARING.ID` | `EbQueriesAnswers_ClearingId` | TField |  | Specifies the type of clearing from where the message has been received or to where the message has to be sent to Validation Rules: 35 characters of type alphatypenumeric |
| 47 | `EB.QA.REQ.EXEC.DATE` | `EbQueriesAnswers_ReqExecDate` | TField |  | Date for processing the cancellation payment (in case the request has been accepted by an operator, or is processed STP. Validation Rules: Up to 8 type D date characters |
| 48 | `EB.QA.APPLICATION.ID` | `EbQueriesAnswers_ApplicationId` | TField |  | The SYSTEM.ID from which the request was originated Validation Rules: 2 characters of type alphatypenumeric |
| 49 | `EB.QA.ERROR.REASON` | `EbQueriesAnswers_ErrorReason` | TField |  | The reason for rejection of this transaction to be specified here Validation Rules: 35 characters of type alphatypenumeric |
| 50 | `EB.QA.PROCESS.INDICATOR` | `EbQueriesAnswers_ProcessIndicator` | TField |  | This field will store the value if request can be processed manually or STP. Allowed values are STP, Manual and Blank Validation Rules: 35 characters of type alphatypenumeric |
| 51 | `EB.QA.LOCAL.REF` | `EbQueriesAnswers_LocalRef` |  |  |  |
| 52 | `EB.QA.ORIG.MSG.REFERENCE` | `EbQueriesAnswers_OrigMsgReference` | TField |  | Specifies the terms used to formally address a person. Validation Rules: 35 characters of type alphatypenumeric |
| 53 | `EB.QA.ORIG.INTBK.SET.AMT` | `EbQueriesAnswers_OrigIntbkSetAmt` | TField |  | Specifies the Original payment amount for cancellation. Validation Rules: 19 characters of type alphatypenumeric |
| 54 | `EB.QA.ORIG.INTBK.SET.AMT.CCY` | `EbQueriesAnswers_OrigIntbkSetAmtCcy` | TField |  | Specifies the Original payment amount currency. Validation Rules: 3 characters of type alphatypenumeric |
| 55 | `EB.QA.SENDER.INSTITUTION.BIC` | `EbQueriesAnswers_SenderInstitutionBic` | TField |  | Specifies the BIC of the DP originating this cancellation request. Validation Rules: 12 characters of type alphatypenumeric |
| 56 | `EB.QA.SENDER.INSTITUTION.OTHER.ID` | `EbQueriesAnswers_SenderInstitutionOtherId` | TField |  | Specifies the Other Identification of the DP originating this cancellation request. Validation Rules: 35 characters of type alphatypenumeric |
| 57 | `EB.QA.ORIG.DEBTOR.ACCOUNT` | `EbQueriesAnswers_OrigDebtorAccount` | TField |  | Specifies the Original debtor account of the transaction . Validation Rules: 35 characters of type alphatypenumeric |
| 58 | `EB.QA.ORIG.CREDITOR.ACCOUNT` | `EbQueriesAnswers_OrigCreditorAccount` | TField |  | Specifies the Original creditor account of the transaction. Validation Rules: 35 characters of type alphatypenumeric |
| 59 | `EB.QA.ORIG.DEBTOR.AGENT.BIC` | `EbQueriesAnswers_OrigDebtorAgentBic` | TField |  | Specifies the Original debtor agent BIC of the transaction. Validation Rules: 12 characters of type alphatypenumeric |
| 60 | `EB.QA.PAYMENT.METHOD` | `EbQueriesAnswers_PaymentMethod` | TField |  | Indicates if the original payment is an instant payment or not. (INST/NRINST= instant payment). Validation Rules: 6 characters of type alphatypenumeric |
| 61 | `EB.QA.ORIG.CREDITOR.AGENT.BIC` | `EbQueriesAnswers_OrigCreditorAgentBic` | TField |  | Specifies the Original creditor agent BIC. Validation Rules: 12 characters of type alphatypenumeric |
| 62 | `EB.QA.ORIG.CREDITOR.AGENT.OTHER.ID` | `EbQueriesAnswers_OrigCreditorAgentOtherId` | TField |  | Specifies the Original creditor agent other identification. Validation Rules: 35 characters of type alphatypenumeric |
| 63 | `EB.QA.ORIG.DEBTOR.AGENT.OTHER.ID` | `EbQueriesAnswers_OrigDebtorAgentOtherId` | TField |  | Specifies the Original debtor agent other identification. Validation Rules: 35 characters of type alphatypenumeric |
| 64 | `EB.QA.ORIGINATOR.OTHER.ID` | `EbQueriesAnswers_OriginatorOtherId` | TField |  | Specifies the Originator other identification. Validation Rules: 35 characters of type alphatypenumeric |
| 65 | `EB.QA.WAIVE.FEES` | `EbQueriesAnswers_WaiveFees` | TField |  | Specifies the detailing for EBQA record. Validation Rules: 3 characters of type alphatypenumeric |
| 66 | `EB.QA.CANCEL.REQ.ID` | `EbQueriesAnswers_CancelReqId` |  |  |  |
| 67 | `EB.QA.CANCEL.REQ.DATETIME` | `EbQueriesAnswers_CancelReqDatetime` |  |  |  |
| 68 | `EB.QA.ROI.ID` | `EbQueriesAnswers_RoiId` |  |  |  |
| 69 | `EB.QA.ROI.DATETIME` | `EbQueriesAnswers_RoiDatetime` |  |  |  |
| 70 | `EB.QA.INVESTIGATION.ID` | `EbQueriesAnswers_InvestigationId` |  |  |  |
| 71 | `EB.QA.INVESTIGATION.DATETIME` | `EbQueriesAnswers_InvestigationDatetime` |  |  |  |
| 72 | `EB.QA.END.TO.END.ID` | `EbQueriesAnswers_EndToEndId` | TField |  | This field is a Unique identification (reference), as assigned by the initiating party, to unambiguously identify the original transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. Validation Rules: A maximum of 35 Alphanumeric characters allowed. Input allowed only when PP module is installed. |
| 73 | `EB.QA.CREATION.DATE` | `EbQueriesAnswers_CreationDate` | TField |  | The field defines the date when EB.QUERIES.ANSWERS was first created. Amendments or response not record. Validation Rules: NOINPUT field. Auto populated by system. |
| 74 | `EB.QA.RECEIVED.REFERENCE` | `EbQueriesAnswers_ReceivedReference` |  |  |  |
| 75 | `EB.QA.SENT.REFERENCE` | `EbQueriesAnswers_SentReference` |  |  |  |
| 76 | `EB.QA.OVERRIDE` | `EbQueriesAnswers_Override` |  |  |  |
| 77 | `EB.QA.RECORD.STATUS` | `EbQueriesAnswers_RecordStatus` | String |  | Standard audit field |
| 78 | `EB.QA.CURR.NO` | `EbQueriesAnswers_CurrNo` | String |  | Standard audit field |
| 79 | `EB.QA.INPUTTER` | `EbQueriesAnswers_Inputter` |  |  |  |
| 80 | `EB.QA.DATE.TIME` | `EbQueriesAnswers_DateTime` |  |  |  |
| 81 | `EB.QA.AUTHORISER` | `EbQueriesAnswers_Authoriser` | String |  | Standard audit field |
| 82 | `EB.QA.CO.CODE` | `EbQueriesAnswers_CoCode` | String |  | Standard audit field |
| 83 | `EB.QA.DEPT.CODE` | `EbQueriesAnswers_DeptCode` | String |  | Standard audit field |
| 84 | `EB.QA.AUDITOR.CODE` | `EbQueriesAnswers_AuditorCode` | String |  | Standard audit field |
| 85 | `EB.QA.AUDIT.DATE.TIME` | `EbQueriesAnswers_AuditDateTime` | String |  | Standard audit field |
| 86 | `EB.QA.COMP.AMOUNT` | `EbQueriesAnswers_CompAmount` | TField |  | Compensation amount to be provided by the beneficiary bank while sending camt.029 response to incoming camt.087. Only allowed for ACVA/MODI status. |
| 87 | `EB.QA.COMP.REASON.CODE` | `EbQueriesAnswers_CompReasonCode` | TField |  | Compensation reason code will be VADA and to provided when compensation amount is provided. |
| 88 | `EB.QA.CHARGES.AMOUNT` | `EbQueriesAnswers_ChargesAmount` | TField | No | Charges amount is optional and provided in the camt.029 response to incoming camt.027 or camt.087. |
| 89 | `EB.QA.CHARGES.BIC` | `EbQueriesAnswers_ChargesBic` | TField |  | Beneficiary bank BIC requesting charges amount for processing the camt.027 or camt.087 |
| 90 | `EB.QA.CLAIM.PROC.DATE` | `EbQueriesAnswers_ClaimProcDate` | TField |  | The date on which the claim camt.027 was accepted and processed. Used only if status is ACNR |
| 91 | `EB.QA.CASE.STATUS` | `EbQueriesAnswers_CaseStatus` | TField |  | The Status of the CASE or investigation. The following values are allowed (schema error): ACNR (Accepted Claim Non-Receipt); RJNR (Rejected Claim Non-Receipt); ACVA (Accepted Value Date Adjustment); RJVA or CVAA (Rejected Value Date Adjustment); MODI (Modified As Per Request). |
| 92 | `EB.QA.MODIFICATION.STATUS.ID` | `EbQueriesAnswers_ModificationStatusId` | TField |  | Unique system generated id used when the status is ACNR,ACVA,RJVA,CVAA,MODI. Not allowed for RJNR. |
| 93 | `EB.QA.MOD.INTBK.SET.DTE` | `EbQueriesAnswers_ModIntbkSetDte` | TField |  | The field stores the modified interbank settlement date requested in the camt.087 message. |
| 94 | `EB.QA.INSTRCD.FOR.CREDITOR.AGENT` | `EbQueriesAnswers_InstrcdForCreditorAgent` | TField | Yes | If the modified interbank settlement date is same as the credit value date of pacs.008 then this field is mandatory. |
| 95 | `EB.QA.INSTRINF.FOR.CREDITOR.AGENT` | `EbQueriesAnswers_InstrinfForCreditorAgent` | TField | Yes | If the modified interbank settlement date is same as the credit value date of pacs.008 then this field is mandatory. |
| 96 | `EB.QA.CASE.TYPE` | `EbQueriesAnswers_CaseType` |  |  |  |
| 97 | `EB.QA.CASE.ID` | `EbQueriesAnswers_CaseId` |  |  |  |
| 98 | `EB.QA.CASE.DATETIME` | `EbQueriesAnswers_CaseDatetime` |  |  |  |
| 99 | `EB.QA.UETR.REF` | `EbQueriesAnswers_UetrRef` | TField |  |  |
| 100 | `EB.QA.SERVICE.TYPE.ID` | `EbQueriesAnswers_ServiceTypeId` | TField |  | This field stores the value of the ISO code which specifies Service Level. |
| 101 | `EB.QA.FORWARDED.TO.AGENT.BIC` | `EbQueriesAnswers_ForwardedToAgentBic` | TField |  |  |
| 102 | `EB.QA.ISO.REASON.CODE` | `EbQueriesAnswers_IsoReasonCode` | TField |  |  |
| 103 | `EB.QA.CHARGES.IBAN` | `EbQueriesAnswers_ChargesIban` | TField |  |  |
| 104 | `EB.QA.COMP.IBAN` | `EbQueriesAnswers_CompIban` | TField |  |  |
| 105 | `EB.QA.COMP.BIC` | `EbQueriesAnswers_CompBic` | TField |  |  |
| 106 | `EB.QA.REQ.ASSIGNMENT.ID` | `EbQueriesAnswers_ReqAssignmentId` |  |  |  |
| 107 | `EB.QA.RESP.ASSIGNMENT.ID` | `EbQueriesAnswers_RespAssignmentId` |  |  |  |
| 108 | `EB.QA.INVST.CASE.ID` | `EbQueriesAnswers_InvstCaseId` |  |  |  |
| 109 | `EB.QA.SENDER.CLRGSYSID` | `EbQueriesAnswers_SenderClrgsysid` | TField |  | Clearing system code of assigner of cancellation request Should be a valid clearing system id maintained in PI.ISO.EXTERNAL.CODE against id ClearingSysId |
| 110 | `EB.QA.SENDER.LEI` | `EbQueriesAnswers_SenderLei` | TField |  | Legal Entity Identifier (LEI) of assigner of cancellation request |
| 111 | `EB.QA.RECEIVER.BIC` | `EbQueriesAnswers_ReceiverBic` | TField |  | BIC of Assignee of cancellation request |
| 112 | `EB.QA.RECEIVER.CLRGSYSID` | `EbQueriesAnswers_ReceiverClrgsysid` | TField |  | Clearing system code of assignee of cancellation request Should be a valid clearing system id maintained in PI.ISO.EXTERNAL.CODE against id ClearingSysId |
| 113 | `EB.QA.RECEIVER.CLRGMEMID` | `EbQueriesAnswers_ReceiverClrgmemid` | TField |  | Clearing member identifciation of assignee of cancellation request |
| 114 | `EB.QA.RECEIVER.LEI` | `EbQueriesAnswers_ReceiverLei` | TField |  | Legal Entity Identifier (LEI) of assignee of cancellation request |
| 115 | `EB.QA.ORIG.CREATION.DATETIME` | `EbQueriesAnswers_OrigCreationDatetime` | TField |  | This field holds the creation date time details of underlying payment message |
| 116 | `EB.QA.ORIG.TXN.REFERENCE` | `EbQueriesAnswers_OrigTxnReference` | TField |  | This field holds the transaction identification of underlying payment message |
| 117 | `EB.QA.CNCL.INITIATED.BY` | `EbQueriesAnswers_CnclInitiatedBy` | TField |  | This field specifies if cancel request is initiated by customer or bank Allowed values are: C - indicates Cancel request is initiated by Customer B - indicates Cancel request is initiated by Bank |
| 118 | `EB.QA.CNCL.COVER` | `EbQueriesAnswers_CnclCover` | TField |  | This field specifies if cancel request is for the direct message or for the cover message (for customer and bank transfers which were settled using cover method) For a Customer transfer settled using cover method, pacs.008 is the direct/announcement message and pacs.009 COV is the cover message For a Bank transfer settled using cover method, pacs.009 ADV is the direct/announcement message and pacs.009 is the cover message Allowed values are: D - indicates cancel request is for the direct/announcement message C - indicates cancel request is for the cover message Blank - indicates cancel request is for a payment which is not settled using cover (means serial payment or payment sent directly through a clearing) |
| 119 | `EB.QA.CNCL.VIA.TRACKER` | `EbQueriesAnswers_CnclViaTracker` | TField |  | This field indicates if the cancellation request is sent/received via SWIFT tracker |
| 120 | `EB.QA.ORIG.CLEARING.SYS.REF` | `EbQueriesAnswers_OrigClearingSysRef` | TField |  | This field holds the clearing system reference of underlying payment message |
| 121 | `EB.QA.CREATOR.TYPE` | `EbQueriesAnswers_CreatorType` | TField |  | Specifies the type of Case creator Possible values are: P - Party A - Agent |
| 122 | `EB.QA.CREATOR.NAME` | `EbQueriesAnswers_CreatorName` | TField |  | Name of the case creator |
| 123 | `EB.QA.CREATOR.DEPT` | `EbQueriesAnswers_CreatorDept` | TField |  | Specifies the structured postal address - department of the case creator |
| 124 | `EB.QA.CREATOR.SUBDEPT` | `EbQueriesAnswers_CreatorSubdept` | TField |  | Specifies the structured postal address - sub department of the case creator |
| 125 | `EB.QA.CREATOR.STREET.NAME` | `EbQueriesAnswers_CreatorStreetName` | TField |  | Specifies the structured postal address - street name of case creator |
| 126 | `EB.QA.CREATOR.BLDG.NO` | `EbQueriesAnswers_CreatorBldgNo` | TField |  | Specifies the structured postal address - building number of the case creator |
| 127 | `EB.QA.CREATOR.BLDG.NAME` | `EbQueriesAnswers_CreatorBldgName` | TField |  | Specifies the structured postal address - building name of the case creator |
| 128 | `EB.QA.CREATOR.BLDG.FLOOR` | `EbQueriesAnswers_CreatorBldgFloor` | TField |  | Specifies the structured postal address - building floor of the case creator |
| 129 | `EB.QA.CREATOR.POST.BOX` | `EbQueriesAnswers_CreatorPostBox` | TField |  | Specifies the structured postal address - Postbox details of the case creator |
| 130 | `EB.QA.CREATOR.ROOM` | `EbQueriesAnswers_CreatorRoom` | TField |  | Specifies the structured postal address - room number of the case creator |
| 131 | `EB.QA.CREATOR.POST.CODE` | `EbQueriesAnswers_CreatorPostCode` | TField |  | Specifies the structured postal address - Post code of the case creator |
| 132 | `EB.QA.CREATOR.TOWN.NAME` | `EbQueriesAnswers_CreatorTownName` | TField |  | Specifies the structured postal address - Town name of the case creator |
| 133 | `EB.QA.CREATOR.TOWN.LOCATION` | `EbQueriesAnswers_CreatorTownLocation` | TField |  | Specifies the structured postal address - Town location of the case creator |
| 134 | `EB.QA.CREATOR.DISTRICT` | `EbQueriesAnswers_CreatorDistrict` | TField |  | Specifies the structured postal address - district of the case creator |
| 135 | `EB.QA.CREATOR.COUNTRY.SUB.DIV` | `EbQueriesAnswers_CreatorCountrySubDiv` | TField |  | Specifies the structured postal address - Country sub division of the case creator |
| 136 | `EB.QA.CREATOR.COUNTRY` | `EbQueriesAnswers_CreatorCountry` | TField |  | Specifies the structured postal address - country code of case creator |
| 137 | `EB.QA.CREATOR.ADDRESS.LINE` | `EbQueriesAnswers_CreatorAddressLine` |  |  |  |
| 138 | `EB.QA.CREATOR.BIC` | `EbQueriesAnswers_CreatorBic` | TField |  | BIC of the case creator |
| 139 | `EB.QA.CREATOR.CLRGSYSID` | `EbQueriesAnswers_CreatorClrgsysid` | TField |  | Clearing system identification code of case creator Should be a valid clearing system id maintained in PI.ISO.EXTERNAL.CODE against id ClearingSysId |
| 140 | `EB.QA.CREATOR.CLRGMEMID` | `EbQueriesAnswers_CreatorClrgmemid` | TField |  | Clearing member identification of case creator |
| 141 | `EB.QA.CREATOR.LEI` | `EbQueriesAnswers_CreatorLei` | TField |  | Legal Entity Identifier (LEI) of the case creator |
| 142 | `EB.QA.CREATOR.ORG.OTHER.ID` | `EbQueriesAnswers_CreatorOrgOtherId` |  |  |  |
| 143 | `EB.QA.CREATOR.ORG.OTHER.SCHCODE` | `EbQueriesAnswers_CreatorOrgOtherSchcode` |  |  |  |
| 144 | `EB.QA.CREATOR.ORG.OTHER.SCHPROP` | `EbQueriesAnswers_CreatorOrgOtherSchprop` |  |  |  |
| 145 | `EB.QA.CREATOR.ORG.OTHER.ISSUER` | `EbQueriesAnswers_CreatorOrgOtherIssuer` |  |  |  |
| 146 | `EB.QA.CREATOR.BIRTHDATE` | `EbQueriesAnswers_CreatorBirthdate` | TField |  | Specifies the Private Identification -> Date of Birth of the case creator |
| 147 | `EB.QA.CREATOR.PROVINCEOFBIRTH` | `EbQueriesAnswers_CreatorProvinceofbirth` | TField |  | Specifies the Private Identification -> Place of Birth of case creator |
| 148 | `EB.QA.CREATOR.CITYOFBIRTH` | `EbQueriesAnswers_CreatorCityofbirth` | TField |  | Specifies the Private Identification -> City of Birth of the case creator |
| 149 | `EB.QA.CREATOR.COUNTRYOFBIRTH` | `EbQueriesAnswers_CreatorCountryofbirth` | TField |  | Specifies the Private Identification -> Country code of birth of case creator |
| 150 | `EB.QA.CREATOR.PVT.OTHERID` | `EbQueriesAnswers_CreatorPvtOtherid` |  |  |  |
| 151 | `EB.QA.CREATOR.PVT.OTHSCHCODE` | `EbQueriesAnswers_CreatorPvtOthschcode` |  |  |  |
| 152 | `EB.QA.CREATOR.PVT.OTHSCHPROP` | `EbQueriesAnswers_CreatorPvtOthschprop` |  |  |  |
| 153 | `EB.QA.CREATOR.PVT.OTHISSUER` | `EbQueriesAnswers_CreatorPvtOthissuer` |  |  |  |
| 154 | `EB.QA.CREATOR.CNTRY.RESIDENCE` | `EbQueriesAnswers_CreatorCntryResidence` | TField |  | Specifies the country code of residence of case creator |
| 155 | `EB.QA.ORIGINATOR.DEPT` | `EbQueriesAnswers_OriginatorDept` | TField |  | Specifies the structured postal address - department of the case Originator |
| 156 | `EB.QA.ORIGINATOR.SUBDEPT` | `EbQueriesAnswers_OriginatorSubdept` | TField |  | Specifies the structured postal address - sub department of the Originator |
| 157 | `EB.QA.ORIGINATOR.STREET.NAME` | `EbQueriesAnswers_OriginatorStreetName` | TField |  | Specifies the structured postal address - street name of Originator |
| 158 | `EB.QA.ORIGINATOR.BLDG.NO` | `EbQueriesAnswers_OriginatorBldgNo` | TField |  | Specifies the structured postal address - building number of the Originator |
| 159 | `EB.QA.ORIGINATOR.BLDG.NAME` | `EbQueriesAnswers_OriginatorBldgName` | TField |  | Specifies the structured postal address - building name of the Originator |
| 160 | `EB.QA.ORIGINATOR.BLDG.FLOOR` | `EbQueriesAnswers_OriginatorBldgFloor` | TField |  | Specifies the structured postal address - building floor of the Originator |
| 161 | `EB.QA.ORIGINATOR.POST.BOX` | `EbQueriesAnswers_OriginatorPostBox` | TField |  | Specifies the structured postal address - Postbox details of the Originator |
| 162 | `EB.QA.ORIGINATOR.ROOM` | `EbQueriesAnswers_OriginatorRoom` | TField |  | Specifies the structured postal address - room number of the Originator |
| 163 | `EB.QA.ORIGINATOR.POST.CODE` | `EbQueriesAnswers_OriginatorPostCode` | TField |  | Specifies the structured postal address - Post code of the Originator |
| 164 | `EB.QA.ORIGINATOR.TOWN.NAME` | `EbQueriesAnswers_OriginatorTownName` | TField |  | Specifies the structured postal address - Town name of the Originator |
| 165 | `EB.QA.ORIGINATOR.TOWN.LOCATION` | `EbQueriesAnswers_OriginatorTownLocation` | TField |  | Specifies the structured postal address - Town location of the Originator |
| 166 | `EB.QA.ORIGINATOR.DISTRICT` | `EbQueriesAnswers_OriginatorDistrict` | TField |  | Specifies the structured postal address - district of the Originator |
| 167 | `EB.QA.ORIGINATOR.COUNTRY.SUB.DIV` | `EbQueriesAnswers_OriginatorCountrySubDiv` | TField |  | Specifies the structured postal address - Country sub division of the Originator |
| 168 | `EB.QA.ORIGINATOR.COUNTRY` | `EbQueriesAnswers_OriginatorCountry` | TField |  | Specifies the structured postal address - country code of the Originator |
| 169 | `EB.QA.ORIGINATOR.ADDRESS.LINE` | `EbQueriesAnswers_OriginatorAddressLine` |  |  |  |
| 170 | `EB.QA.ORIGINATOR.LEI` | `EbQueriesAnswers_OriginatorLei` | TField |  | Legal Entiry Identifier (LEI) of originator |
| 171 | `EB.QA.ORIGINATOR.ORG.OTHERID` | `EbQueriesAnswers_OriginatorOrgOtherid` |  |  |  |
| 172 | `EB.QA.ORIGINATOR.ORG.OTHSCHCODE` | `EbQueriesAnswers_OriginatorOrgOthschcode` |  |  |  |
| 173 | `EB.QA.ORIGINATOR.ORG.OTHSCHPROP` | `EbQueriesAnswers_OriginatorOrgOthschprop` |  |  |  |
| 174 | `EB.QA.ORIGINATOR.ORG.OTHISSUER` | `EbQueriesAnswers_OriginatorOrgOthissuer` |  |  |  |
| 175 | `EB.QA.ORIGINATOR.BIRTHDATE` | `EbQueriesAnswers_OriginatorBirthdate` | TField |  | Specifies the Private Identification -> Date of Birth of the originator |
| 176 | `EB.QA.ORIGINATOR.PROVINCEOFBIRTH` | `EbQueriesAnswers_OriginatorProvinceofbirth` | TField |  | Specifies the Private Identification -> Place of Birth of originator |
| 177 | `EB.QA.ORIGINATOR.CITYOFBIRTH` | `EbQueriesAnswers_OriginatorCityofbirth` | TField |  | Specifies the Private Identification -> City of Birth of the originator |
| 178 | `EB.QA.ORIGINATOR.COUNTRYOFBIRTH` | `EbQueriesAnswers_OriginatorCountryofbirth` | TField |  | Specifies the Private Identification -> Country code of birth of originator |
| 179 | `EB.QA.ORIGINATOR.PVT.OTHERID` | `EbQueriesAnswers_OriginatorPvtOtherid` |  |  |  |
| 180 | `EB.QA.ORIGINATOR.PVT.OTHSCHCODE` | `EbQueriesAnswers_OriginatorPvtOthschcode` |  |  |  |
| 181 | `EB.QA.ORIGINATOR.PVT.OTHSCHPROP` | `EbQueriesAnswers_OriginatorPvtOthschprop` |  |  |  |
| 182 | `EB.QA.ORIGINATOR.PVT.OTHISSUER` | `EbQueriesAnswers_OriginatorPvtOthissuer` |  |  |  |
| 183 | `EB.QA.ORIGINATOR.CNTRYOFRESIDENCE` | `EbQueriesAnswers_OriginatorCntryofresidence` | TField |  | Specifies the country code of residence of originator |
| 184 | `EB.QA.RETURN.REJECT.REF` | `EbQueriesAnswers_ReturnRejectRef` | TField |  | Specifies the return or reject reference generated or received for recall message |
| 185 | `EB.QA.ORIG.FT.NUMBER` | `EbQueriesAnswers_OrigFtNumber` | TField |  | Used to store the TPH FT number for incoming cancellation request |
| 186 | `EB.QA.PENDING.ADDL.INFO` | `EbQueriesAnswers_PendingAddlInfo` |  |  |  |
| 187 | `EB.QA.RETURN.AMOUNT` | `EbQueriesAnswers_ReturnAmount` | TField |  | Specifies the Return payment amount. |
| 188 | `EB.QA.REQUEST.CODE` | `EbQueriesAnswers_RequestCode` |  |  |  |
| 189 | `EB.QA.ADDITIONAL.REQUEST.INFORMATION` | `EbQueriesAnswers_AdditionalRequestInformation` |  |  |  |
| 190 | `EB.QA.CONTEXT.NAME` | `EbQueriesAnswers_ContextName` |  |  |  |
| 191 | `EB.QA.CONTEXT.VALUE` | `EbQueriesAnswers_ContextValue` |  |  |  |
| 192 | `EB.QA.CASE.MGMT.MSG.CONCAT` | `EbQueriesAnswers_CaseMgmtMsgConcat` |  |  |  |
