# ACH.ENTRIES — Table Schema

> Source: `INSERTS/I_F.ACH.ENTRIES` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.ENT.STATUS` | `AchEntries_Status` | TField |  | Status of the Entry. Valid values are ACK, Cancelled, Cleared, Data Error, Death Notification, Delivered, Exception, Loaded, Nack, Pending, Rejected, Returned, ReversalInitiated, ReversalCompleted, Validated, Validation Error, or Voided. |
| 2 | `ACH.ENT.BATCH.ID` | `AchEntries_BatchId` | TField |  | Id of the batch that contains this entry. |
| 3 | `ACH.ENT.REC.TYPE.CODE` | `AchEntries_RecTypeCode` | TField |  | ACH Entry Detail record type code always equal to 6. |
| 4 | `ACH.ENT.TRANSACTION.CODE` | `AchEntries_TransactionCode` | TField |  | Identifies various types of debits and credit entries. See NACHA Guidelines for list of Transaction Codes. |
| 5 | `ACH.ENT.RECEIVING.DFI.ID` | `AchEntries_ReceivingDfiId` | TField | Yes | 8 Positions &#45; Entry Detail Record &#45; Mandatory. The standard routing number as assigned by Accuity (with Check Digit) is used to identify the DFI in which the Receiver maintains his account or a routing number assigned to a Federal Government agency by the Federal Reserve. For IAT Entries, this field contains the bank identification number of the DFI at which the Receiver maintains his account. |
| 6 | `ACH.ENT.CHECK.DIGIT` | `AchEntries_CheckDigit` | TField | Yes | 1 Position &#45; Entry Detail Record, Corporate Entry Detail Record &#45; Mandatory (all entries). See the NACHA Guidelines for additional details. |
| 7 | `ACH.ENT.DFI.ACCOUNT.NO` | `AchEntries_DfiAccountNo` | TField |  | 17 Positions &#45; Entry Detail Record &#45; Required. The DFI Account Number is the RDFI &#39; s customer&#39;s account number. It is usually obtained from: (1) the on-us field of the MICR line of a Check; (2) account statement; (3) passbook; or (4) other source document provided by the RDFI that specifically designates the account number to be used for ACH purposes. |
| 8 | `ACH.ENT.CUS.CLEAR.ACCT` | `AchEntries_CusClearAcct` | TField |  | Customer account where transaction is posted/cleared. |
| 9 | `ACH.ENT.AMOUNT` | `AchEntries_Amount` | TField |  | Amount of the entry to be posted to the customer account. |
| 10 | `ACH.ENT.INDIVIDUAL.ID.NO` | `AchEntries_IndividualIdNo` | TField |  | Customer's account number. |
| 11 | `ACH.ENT.INDIVIDUAL.NAME` | `AchEntries_IndividualName` | TField |  | Customer's name. |
| 12 | `ACH.ENT.DISCRETIONARY.DATA` | `AchEntries_DiscretionaryData` | TField | No | 2 Positions &#45; Entry Detail Record, Corporate Entry Detail Record &#45; Optional. This field in the Entry Detail Record allows ODFIs to include codes, of significance to them, to enable specialized handling of the Entry. |
| 13 | `ACH.ENT.ADDENDA.REC.ID` | `AchEntries_AddendaRecId` | TField | Yes | Indicator: 1 Position &#45; Entry Detail Record and Corporate Entry Detail - Mandatory. This field indicates the existence of an Addenda Record. |
| 14 | `ACH.ENT.TRACE.NUMBER` | `AchEntries_TraceNumber` | TField | Yes | 15 Positions &#45; Entry Detail Record, Corporate Entry Detail Record, and Addenda Records &#45; Mandatory. A Trace Number, assigned by the ODFI in ascending sequence, is included in each Entry Detail Record, Corporate Entry Detail Record, and Addenda Record. A Trace Number uniquely identifies each Entry Detail Record within a batch in an ACH input File. In association with the Batch Number, Transmission (File Creation) Date, and File ID Modifier, the Trace Number uniquely identifies an Entry within a specific File. For Addenda Records, the Trace Number is identical to the Trace Number in the associated Entry Detail Record. |
| 15 | `ACH.ENT.CHECK.SERIAL.NO` | `AchEntries_CheckSerialNo` | TField | No | 15 Positions &#45; Entry Detail Record &#45; Optional. This field contains the Check Serial Number of a Check. |
| 16 | `ACH.ENT.ROUTING.NO` | `AchEntries_RoutingNo` | TField | Yes | Routing Number of ACH Operator: 8 Positions &#45; Entry Detail Record &#45; Mandatory (ADV). This field contains the routing number of the ACH Operator that is Transmitting the File. |
| 17 | `ACH.ENT.FILE.ID` | `AchEntries_FileId` | TField |  | ID of the ACH file. |
| 18 | `ACH.ENT.ACH.OP.DATA` | `AchEntries_AchOpData` | TField | No | 1 Position &#45; Entry Detail Record &#45; Optional (ADV). This field is used as specified by the ACH Operator. |
| 19 | `ACH.ENT.ACH.OP.ROUTING` | `AchEntries_AchOpRouting` | TField | Yes | Operator: 8 Positions &#45; Entry Detail Record &#45; Mandatory (ADV). This field contains the routing number of the ACH Operator that is Transmitting the File. |
| 20 | `ACH.ENT.JULIAN.DATE` | `AchEntries_JulianDate` | TField | Yes | 3 positions &#45; Entry Detail Record &#45; Mandatory (ADV). This field contains the Julian date on which an Automated Accounting Advice is created. |
| 21 | `ACH.ENT.NO.ADD.REC` | `AchEntries_NoAddRec` | TField | Yes | 4 Positions &#45; Corporate Entry Detail Record/Entry Detail Record &#45; Mandatory (ATX, CTX, ENR, IAT, TRX, COR (IAT entries), refused ATX); 4 Positions &#45; Corporate Entry Detail Record &#45; Required (COR (except IAT), refused COR). CTX: This number represents the number of Addenda Records associated with the Corporate Entry Detail Record. This field will be zero filled if Field 12 (Addenda Record Indicator Value) of the related Corporate Entry Detail Record contains a value of &#39;0&#39; . ATX, ENR, IAT, TRX: This number represents the number of Addenda Records associated with the Entry Detail Record. |
| 22 | `ACH.ENT.TERMINAL.CITY` | `AchEntries_TerminalCity` | TField | Yes | 15 Positions &#45; Addenda Record &#45; Required (MTE, POS, SHR); 4 Positions &#45; Entry Detail Record &#45; Mandatory (POP). This field identifies the city, town, village, or township in which an Electronic terminal is located. |
| 23 | `ACH.ENT.TERMINAL.STATE` | `AchEntries_TerminalState` | TField | Yes | State: 2 Positions &#45; Addenda Record &#45; Required (MTE, POS, SHR); 2 Positions &#45; Entry Detail Record &#45; Mandatory (POP). This field identifies the state of the United States in which an Electronic terminal is located. |
| 24 | `ACH.ENT.LOAD.DATE` | `AchEntries_LoadDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 25 | `ACH.ENT.DEBIT.CREDIT.IND` | `AchEntries_DebitCreditInd` | TField |  | Valid values None, Credit, or Debit. |
| 26 | `ACH.ENT.BATCH.ORIGINATOR` | `AchEntries_BatchOriginator` | TField |  | Company ID from the Batch Record |
| 27 | `ACH.ENT.OFAC.INDICATOR` | `AchEntries_OfacIndicator` | TField | No | This field contains the Gateway operator OFAC screening indicator (optional field for IAT) |
| 28 | `ACH.ENT.SECONDARY.OFAC.IND` | `AchEntries_SecondaryOfacInd` | TField | No | This field contains the Secondary OFAC screening indicator (optional field for IAT) |
| 29 | `ACH.ENT.PAYMENT.TYPE.CODE` | `AchEntries_PaymentTypeCode` | TField | No | Code: 2 Positions &#45; Entry Detail Record &#45; Required (WEB, Returns, dishonored Returns, contested dishonored Returns); Optional. This field is used to indicate whether an Entry is a recurring or Single-Entry payment. |
| 30 | `ACH.ENT.RESERVED.21` | `AchEntries_Reserved21` | TField |  | Reserved Field |
| 31 | `ACH.ENT.IMMEDIATE.ORIGIN` | `AchEntries_ImmediateOrigin` | TField |  | This field contains the routing number of the ACH Operator or Sending Point that is Transmitting the File. The 10 character field begins with a blank in the first position, followed by the four digit Federal Reserve Routing Symbol, the four digit ABA Institution Identifier, and the Check Digit. |
| 32 | `ACH.ENT.T24.TXN.CODE` | `AchEntries_T24TxnCode` | TField |  | T24 Transaction code that corresponds with the ACH Transaction code of the entry. |
| 33 | `ACH.ENT.CURRENCY` | `AchEntries_Currency` | TField |  | Type of currency for this entry. |
| 34 | `ACH.ENT.VALUE.DATE` | `AchEntries_ValueDate` | TField |  | ACH Effective Entry Date. The date specified by the originator on which it intends a batch of entries to be settled. For ACH credits, the effective entry date must be one or two banking days following the processing date. |
| 35 | `ACH.ENT.ENTRY.TYPE` | `AchEntries_EntryType` | TField |  | Valid values None, Accounting, Death Notification,PreNotification or Notification |
| 36 | `ACH.ENT.NARRATIVE` | `AchEntries_Narrative` |  |  |  |
| 37 | `ACH.ENT.ACH.RET.CODE` | `AchEntries_AchRetCode` | TField | Yes | 3 Positions &#45; Addenda Record &#45; Mandatory (Returns); 2 Positions &#45; Addenda Record &#45; Mandatory (dishonored Returns, contested dishonored Returns). This field contains a standard code used by an ACH Operator or RDFI to describe the reason for returning an Entry. In a dishonored Return Entry and contested dishonored Return Entry, only the numeric portion of the code is used. See NACHA Guidelines for a complete listing of Return Reason Codes. |
| 38 | `ACH.ENT.ORIG.US.ACH.ENTRY` | `AchEntries_OrigUsAchEntry` | TField |  | Future use |
| 39 | `ACH.ENT.ORIG.TRACE.NO` | `AchEntries_OrigTraceNo` | TField | Yes | 15 Positions &#45; Addenda Record &#45; Mandatory (Returns, dishonored Returns, contested dishonored Returns, COR, refused COR, ACK, refused ACK, ATX, refused. This field contains the Trace Number as originally included on the forward Entry or Prenotification. The RDFI must include the Original Entry Trace Number in the Addenda Record of an Entry being returned to an ODFI, in the Addenda Record of an NOC, within an Acknowledgment Entry, or with an RDFI request for a copy of an authorization. |
| 40 | `ACH.ENT.ORIG.RECV.DFI.ID` | `AchEntries_OrigRecvDfiId` | TField |  | 8 Positions &#45; Addenda Record &#45; Required (Returns, dishonored Returns, contested dishonored Returns, COR, refused COR). This field contains the Receiving DFI identification as originally included on the forward Entry or Prenotification that the RDFI is returning or correcting. This field must be included in the Addenda Record for an Entry being returned to an ODFI, or within the Addenda Record accompanying a Notification of Change. |
| 41 | `ACH.ENT.T24.ENTRY.AC` | `AchEntries_T24EntryAc` | TField |  | Future use |
| 42 | `ACH.ENT.RETURN.DATE` | `AchEntries_ReturnDate` | TField |  | Date of the return entry. |
| 43 | `ACH.ENT.CARD.TXN.CODE` | `AchEntries_CardTxnCode` | TField | Yes | 2 Positions &#45; Entry Detail Record &#45; Mandatory (POS, SHR, Returns, dishonored Returns, contested dishonored Returns). See NACHA Guidelines for valid values. |
| 44 | `ACH.ENT.RECEIVING.CO.NAME` | `AchEntries_ReceivingCoName` | TField | No | 22 positions &#45; Entry Detail Record &#45; Required (ACK, CCD, refused ACK, Returns, dishonored Returns, contested dishonored Returns, COR, refused COR); 22 Positions &#45; Entry Detail Record &#45; Optional (ARC, BOC, POP). This field is entered by the Originator to provide additional identification of the Receiver and may be helpful in identifying Return Entries. |
| 45 | `ACH.ENT.AC.INWARD.ENTRY.ID` | `AchEntries_AcInwardEntryId` |  |  |  |
| 46 | `ACH.ENT.TAPE.REF` | `AchEntries_TapeRef` | TField |  | Name of the file. |
| 47 | `ACH.ENT.ZERO.DOLLAR.ENTRY` | `AchEntries_ZeroDollarEntry` | TField |  | Valid values are None, No, or Yes. |
| 48 | `ACH.ENT.CARD.EXPIRY.DATE` | `AchEntries_CardExpiryDate` | TField | No | 4 Positions &#45; Entry Detail Record &#45; Required (SHR); 6 Positions &#45; Addenda Record &#45; Optional (POS, SHR). POS, SHR: This code is used by cardholder processors and cardholder Financial Institutions to verify that the card remains valid and that certain security procedures required by various card authorization systems have been met. |
| 49 | `ACH.ENT.DOCUMENT.REF.NO` | `AchEntries_DocumentRefNo` | TField |  | 11 Positions &#45; Entry Detail Record &#45; Required (SHR). This field further defines the transaction in the event of a Receiver&#39;s inquiry. An example is an Electronic sequence number. |
| 50 | `ACH.ENT.INDV.CARD.ACCT.NO` | `AchEntries_IndvCardAcctNo` | TField |  | 22 Positions &#45; Entry Detail Record &#45; Required (SHR). The Individual Card Account Number is the number assigned by the card issuer and is obtained from the card itself. |
| 51 | `ACH.ENT.PROCESS.CTRL.FLD` | `AchEntries_ProcessCtrlFld` | TField | No | 6 Positions &#45; Entry Detail Record &#45; Required (TRC, XCK). This field contains an optional code, as obtained from a Check or sharedraft, which generally identifies the document type. The field is usually located to the right of the account number in the on-us field of the MICR line and is sometimes called a transaction code. |
| 52 | `ACH.ENT.ITEM.RESEARCH.NO` | `AchEntries_ItemResearchNo` | TField |  | 16 Positions &#45; Entry Detail Record &#45; Required (TRC, XCK). This field contains the MICR locator number for Check item research. |
| 53 | `ACH.ENT.ITEM.TYPE.INDI` | `AchEntries_ItemTypeIndi` | TField | No | 2 Positions &#45; Entry Detail Record &#45; Optional (TRC, TRX). This field indicates the type of items being truncated. See NACHA Guidelines for code values. |
| 54 | `ACH.ENT.MSG.TYPE` | `AchEntries_MsgType` | TField |  | Valid values are None, Inward, or Outward. |
| 55 | `ACH.ENT.ENTRY.CLASS.CODE` | `AchEntries_EntryClassCode` | TField | Yes | 3 positions, mandatory for all batches. This field contains a three-character code used to identify various types of entries. See the NACHA Guidelines for a list of Standard Entry Class Codes. |
| 56 | `ACH.ENT.ROUTING.CUSTOMER` | `AchEntries_RoutingCustomer` | TField |  | Name of customer receivng the file. |
| 57 | `ACH.ENT.CUSTOMER.FILE` | `AchEntries_CustomerFile` | TField |  | System populated file. This is updated as ""FED"" if the file is received from FED, otherwise this will be blank. |
| 58 | `ACH.ENT.REVERSAL.TRANSACTION` | `AchEntries_ReversalTransaction` | TField |  | System populated field. This field holds the Original AchEntries ID for a Reversal entry. |
| 59 | `ACH.ENT.SETTLEMENT.DATE` | `AchEntries_SettlementDate` | TField |  | The date specified by the originator on which it intends a batch of entries to be settled. For ACH credits, the effective entry date must be one or two banking days following the processing date. |
| 60 | `ACH.ENT.AML.RESPONSE` | `AchEntries_AmlResponse` | TField |  | Response from AML system. Valid values are Null, 0, 1, Clean, or Hit. |
| 61 | `ACH.ENT.AML.REJ.REASON` | `AchEntries_AmlRejReason` | TField |  | Reason from the AML system that the batch was rejected. |
| 62 | `ACH.ENT.AML.VERIFICATION` | `AchEntries_AmlVerification` | TField |  | Field that determines if AML verification is used for this file |
| 63 | `ACH.ENT.AML.LEVELS` | `AchEntries_AmlLevels` | TField |  | Level set in ACH.AML.PARAMETER. Values are Null, 0, 1, or 2. |
| 64 | `ACH.ENT.AML.RESERVED.3` | `AchEntries_AmlReserved3` | TField |  | Reserved Field |
| 65 | `ACH.ENT.AML.RESERVED.2` | `AchEntries_AmlReserved2` | TField |  | Reserved Field |
| 66 | `ACH.ENT.AML.RESERVED.1` | `AchEntries_AmlReserved1` | TField |  | Reserved Field |
| 67 | `ACH.ENT.ENTRIES.XREF` | `AchEntries_EntriesXref` | TField |  | System populated field. This field holds the inward AchEntries ID for a transit entry |
| 68 | `ACH.ENT.ENTRIES.RECORD` | `AchEntries_EntriesRecord` | TField |  | System Populated field. This field stores entire entry record for an outward file |
| 69 | `ACH.ENT.REMARKS` | `AchEntries_Remarks` |  |  |  |
| 70 | `ACH.ENT.RELEASE.DATE` | `AchEntries_ReleaseDate` | TField |  | Date the file was released from the ACH Warehouse. |
| 71 | `ACH.ENT.RETRY.ATTEMPTS` | `AchEntries_RetryAttempts` | TField |  | This field displays the number of times a retry payment has been attempted. One of the following three values will be displayed: a. Blank (null) indicates that the Retry Payment functionality is turned off. b. 1 indicates that a Retry Payments was attempted 1 time c. 2 indicates that a Retry Payments was attempted 2 times |
| 72 | `ACH.ENT.LAST.UPDATE.DATE` | `AchEntries_LastUpdateDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 73 | `ACH.ENT.RETURN.TYPE` | `AchEntries_ReturnType` | TField |  | Type of returns, valid values are None, Contested, Dishonored, or Return |
| 74 | `ACH.ENT.TXN.ADDL.INFO` | `AchEntries_TxnAddlInfo` | TField |  | System populated field. This will be updated as ""DUPRET"" when a duplicate return entry is received. |
| 75 | `ACH.ENT.ORIG.ACCOUNT` | `AchEntries_OrigAccount` | TField |  | System populated field. For each incoming return entry, this field will be updated with the account of the originator. |
| 76 | `ACH.ENT.ORIG.DD.ITEM.REF` | `AchEntries_OrigDdItemRef` | TField |  | This field will be used to store the original DD.ITEM record reference when a DD.ITEM is initiated as an outward ACH. This will be used by TPH to create DD.RETURN for originally created direct debit item. |
| 77 | `ACH.ENT.LARGE.DOLLAR` | `AchEntries_LargeDollar` | TField |  | The field will be set to "YES" in ACH.ENTRIES for any entry that is more than the amount defined in ACH.CLEARING.PARAMETER for any files that is originated by a corporate originator. |
| 78 | `ACH.ENT.EARLY.DEPOSIT` | `AchEntries_EarlyDeposit` | TField |  | The field would hold a value of "Y" if this entry qualifies for early deposit. |
| 79 | `ACH.ENT.REJECT.REASON` | `AchEntries_RejectReason` | TField |  | This field will record the reject reason when a pre note transaction is rejected. |
| 80 | `ACH.ENT.RESERVED.7` | `AchEntries_Reserved7` | TField |  | Reserved Field |
| 81 | `ACH.ENT.RESERVED.6` | `AchEntries_Reserved6` | TField |  | Reserved Field |
| 82 | `ACH.ENT.RESERVED.5` | `AchEntries_Reserved5` | TField |  | Reserved Field |
| 83 | `ACH.ENT.RESERVED.4` | `AchEntries_Reserved4` | TField |  | Reserved Field |
| 84 | `ACH.ENT.RESERVED.3` | `AchEntries_Reserved3` | TField |  | Reserved Field |
| 85 | `ACH.ENT.RESERVED.2` | `AchEntries_Reserved2` | TField |  | Reserved Field |
| 86 | `ACH.ENT.RESERVED.1` | `AchEntries_Reserved1` | TField |  | Reserved Field |
| 87 | `ACH.ENT.LOCAL.REF` | `AchEntries_LocalRef` |  |  |  |
| 88 | `ACH.ENT.OVERRIDE` | `AchEntries_Override` |  |  |  |
| 89 | `ACH.ENT.RECORD.STATUS` | `AchEntries_RecordStatus` | String |  |  |
| 90 | `ACH.ENT.CURR.NO` | `AchEntries_CurrNo` | String |  |  |
| 91 | `ACH.ENT.INPUTTER` | `AchEntries_Inputter` |  |  |  |
| 92 | `ACH.ENT.DATE.TIME` | `AchEntries_DateTime` |  |  |  |
| 93 | `ACH.ENT.AUTHORISER` | `AchEntries_Authoriser` | String |  |  |
| 94 | `ACH.ENT.CO.CODE` | `AchEntries_CoCode` | String |  |  |
| 95 | `ACH.ENT.DEPT.CODE` | `AchEntries_DeptCode` | String |  |  |
| 96 | `ACH.ENT.AUDITOR.CODE` | `AchEntries_AuditorCode` | String |  |  |
| 97 | `ACH.ENT.AUDIT.DATE.TIME` | `AchEntries_AuditDateTime` | String |  |  |
