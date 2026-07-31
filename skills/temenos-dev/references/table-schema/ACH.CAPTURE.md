# ACH.CAPTURE — Table Schema

> Source: `INSERTS/I_F.ACH.CAPTURE` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.CAP.ACCT.TYPE` | `AchCapture_AcctType` | TField |  | Type of Account, valid values are None, Checking Account, or Savings Account. |
| 2 | `ACH.CAP.SVC.CLASS.CODE` | `AchCapture_SvcClassCode` | TField | Yes | 3 positions, mandatory for all batches. The Service Class Code (BAI Specifications) identifies the general classification of the dollar entries to be exchanged. ACH Entries are assigned Sercive Class Code series 200-299. Code values are:200 ACH Entries Mixed Debits and Credits220 ACH Credits Only225 ACH Debits Only |
| 3 | `ACH.CAP.COMPANY.NAME` | `AchCapture_CompanyName` | TField | Yes | 16 Positions. Mandatory for all batches except IAT. This field identifies the source of the Entry and is used for descriptive purposes for the Receiver. See NACHA Guidelines for specific requirements. |
| 4 | `ACH.CAP.COMPANY.DISC.DATA` | `AchCapture_CompanyDiscData` | TField |  | 20 Positions. This field allows Originators and/or ODFIs to include codes (one or more), of significance only to them, to enable specialized handling of all Entries in that batches.There is no standardized interpretation for the value of the field. This field must be returned intact on any Return Entry. |
| 5 | `ACH.CAP.COMPANY.ID` | `AchCapture_CompanyId` | TField | Yes | 10 Positons, mandatory for all batches except IAT. This is an alphameric code used to identify an Originator. See NACHA Guidelines for specific requirements. |
| 6 | `ACH.CAP.SEC.CODE` | `AchCapture_SecCode` | TField | Yes | 3 positions, mandatory for all batches. This field contains a three-character code used to identify various types of entries. See the NACHA Guidelines for a list of Standard Entry Class Codes. |
| 7 | `ACH.CAP.COMPANY.ENT.DESC` | `AchCapture_CompanyEntDesc` | TField |  |  |
| 8 | `ACH.CAP.COMPANY.DESC.DATE` | `AchCapture_CompanyDescDate` | TField | No | 6 Positions, optional field. The Originator establishes this field as the date it would like to see displayed to the Receiver for descriptive purposes. See the NACHA Guidelines for specific requirements. |
| 9 | `ACH.CAP.EFFECTIVE.DATE` | `AchCapture_EffectiveDate` | TField |  | 6 Positions and required for all batches. This date is specified by the Originator on which it entends a batch of Entries to be settled. See the NACHA Guidelines for specific requirements. |
| 10 | `ACH.CAP.BATCHHDR.RESERVED.8` | `AchCapture_BatchhdrReserved8` | TField |  | Reserved Field |
| 11 | `ACH.CAP.ORIG.STATUS.CODE` | `AchCapture_OrigStatusCode` | TField | Yes | 1 Position and mandatory for all batches. This code refers to the ODFI initiating the Entry.Code Values:0 ADV File prepared by an ACH Operartor.1 This code indentifies the Originator as a depository financial institution.2 This code identifies the Originator as a Federal Government entity or agency. |
| 12 | `ACH.CAP.ORIG.DFI.ID` | `AchCapture_OrigDfiId` | TField |  | 10 Positions. The Originator Identification is an alphameric code used to uniquely identify an Originator. |
| 13 | `ACH.CAP.BATCH.NUMBER` | `AchCapture_BatchNumber` | TField | Yes | 7 Postions and mandatory for all batches. The ODFI or its Sending Point assigns this number in ascending sequence to each batch in a File of Entries. |
| 14 | `ACH.CAP.IMMEDIATE.ORIGIN` | `AchCapture_ImmediateOrigin` | TField | Yes | 10 Positions and mandatory for all Files. ACH File header record. Identifies the sender of the file. This field contains the routing number of the ACH Operator or Sending Point that is Transmitting the File. The 10 characterfield begins with a blank in the first position, followed byt the four digit Federal Reserve Routing Symbol, the four digit ABA Institution Identifier, and the Check Digit. |
| 15 | `ACH.CAP.DR.OFFSET.ACCOUNT` | `AchCapture_AchCapDrOffsetAccount` |  |  |  |
| 16 | `ACH.CAP.CR.OFFSET.ACCOUNT` | `AchCapture_AchCapCrOffsetAccount` |  |  |  |
| 17 | `ACH.CAP.BATCHHDR.RESERVED.7` | `AchCapture_BatchhdrReserved7` |  |  |  |
| 18 | `ACH.CAP.BATCHHDR.RESERVED.6` | `AchCapture_BatchhdrReserved6` |  |  |  |
| 19 | `ACH.CAP.BATCHHDR.RESERVED.5` | `AchCapture_BatchhdrReserved5` | TField |  | Reserved Field |
| 20 | `ACH.CAP.BATCHHDR.RESERVED.4` | `AchCapture_BatchhdrReserved4` | TField |  | Reserved Field |
| 21 | `ACH.CAP.BATCHHDR.RESERVED.3` | `AchCapture_BatchhdrReserved3` | TField |  | Reserved Field |
| 22 | `ACH.CAP.BATCHHDR.RESERVED.2` | `AchCapture_BatchhdrReserved2` | TField |  | Reserved Field |
| 23 | `ACH.CAP.BATCHHDR.RESERVED.1` | `AchCapture_BatchhdrReserved1` | TField |  | Reserved Field |
| 24 | `ACH.CAP.IAT.INDICATOR` | `AchCapture_IatIndicator` | TField | Conditional | 16 Positions - Company/Batch Header Record - Optional (IAT, Returns); 16 Positions - Company/Batch Header Record - Mandatory (COR entries related to IAT)For forward IAT Entries, this field is left blank. For Notifications of Change related to IAT Entries, this field must contain the value 'IATCOR' |
| 25 | `ACH.CAP.IAT.FX.INDICATOR` | `AchCapture_IatFxIndicator` | TField | Yes | 2 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR)This field contains a code used to indicate the foreign exchange conversion methodology applied to an IAT Entry. Use may be dependent on the particular exchange services offered by a Gateway Operator. See NACHA Guidelines for valid code values for this field. |
| 26 | `ACH.CAP.IAT.FX.REF.INDIC` | `AchCapture_IatFxRefIndic` | TField |  | 1 Position - Company/Batch Header Record - Required (IAT, Returns, COR)This field contains a code used to indicate the content of the Foreign Exchange Reference Field. See NACHA Guidelines for falid code values for this field. |
| 27 | `ACH.CAP.IAT.FX.REF` | `AchCapture_IatFxRef` | TField |  | 15 Positions - Company/Batch Header Record - Required (IAT, Returns, COR)This field contains either the foreign exchange rate used to execute the foreign exchange conversion of an IAT Entry or another reference to the foreign exchange transaction. Content is defined by the Foreign Exchange Reference Indicator Field.If the Foreign Exchange Indicator Field contains 'FF', this field will always be space filled. |
| 28 | `ACH.CAP.ISO.DEST.CO.CODE` | `AchCapture_IsoDestCoCode` |  |  |  |
| 29 | `ACH.CAP.ORIGINATOR.ID` | `AchCapture_OriginatorId` | TField | Yes | Originator Identification: 10 Positions - Company/Batch Header Record - Mandatory (IAT, IAT Returns, IAT COR)The Originator Identification is an alphameric code used to uniquely identify an Originator. This is the ID that is set up in the ACH.CORPORATE.INFO,ORIGINATOR table. |
| 30 | `ACH.CAP.ISO.ORIG.CCY.CODE` | `AchCapture_IsoOrigCcyCode` | TField | Yes | 3 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR).This field contains the three-character code, as approved by the International Organization for Standardization (ISO), to identify the currency denomination in which the Entry was first originated. |
| 31 | `ACH.CAP.ISO.DEST.CCY.CODE` | `AchCapture_IsoDestCcyCode` | TField | Yes | 3 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR)This field contains the three-character code, as approved by the International Organization for Standardization (ISO), to identify the currency denomination in which the Entry is to be received. |
| 32 | `ACH.CAP.OFFSET.DEFAULT` | `AchCapture_OffsetDefault` | TField |  | If the offset accounts need not to be defaulted then this field should be set to N. Currently, this field is set to N if the ACH.CAPTURE record is input through the below versions; ACH.CAPTURE,RETAIL.CIE ACH.CAPTURE,RETAIL.IAT ACH.CAPTURE,RETAIL.PPD ACH.CAPTURE,RETAIL.WEB These versions are used to originate a same day debit transaction. |
| 33 | `ACH.CAP.BATCHTR.RESERVED.9` | `AchCapture_BatchtrReserved9` | TField |  | Reserved Field |
| 34 | `ACH.CAP.BATCHTR.RESERVED.8` | `AchCapture_BatchtrReserved8` | TField |  | Reserved Field |
| 35 | `ACH.CAP.BATCHTR.RESERVED.7` | `AchCapture_BatchtrReserved7` | TField |  | Reserved Field |
| 36 | `ACH.CAP.BATCHTR.RESERVED.6` | `AchCapture_BatchtrReserved6` | TField |  | Reserved Field |
| 37 | `ACH.CAP.BATCHTR.RESERVED.5` | `AchCapture_BatchtrReserved5` | TField |  | Reserved Field |
| 38 | `ACH.CAP.BATCHTR.RESERVED.4` | `AchCapture_BatchtrReserved4` | TField |  | Reserved Field |
| 39 | `ACH.CAP.BATCHTR.RESERVED.3` | `AchCapture_BatchtrReserved3` | TField |  | Reserved Field |
| 40 | `ACH.CAP.BATCHTR.RESERVED.2` | `AchCapture_BatchtrReserved2` | TField |  | Reserved Field |
| 41 | `ACH.CAP.BATCHTR.RESERVED.1` | `AchCapture_BatchtrReserved1` | TField |  | Reserved Field |
| 42 | `ACH.CAP.TR.REC.TYPE.CODE` | `AchCapture_TrRecTypeCode` | TField |  | ACH company/batch control record type code always equal to 5. |
| 43 | `ACH.CAP.TR.SVC.CLASS.CODE` | `AchCapture_TrSvcClassCode` | TField | Yes | 3 positions, mandatory for all batch control records. The Service Class Code (BAI Specifications) identifies the general classification of the dollar entries to be exchanged. ACH Entries are assigned Sercive Class Code series 200-299. Code values are:200 ACH Entries Mixed Debits and Credits220 ACH Credits Only225 ACH Debits Only |
| 44 | `ACH.CAP.TR.ADDENDA.COUNT` | `AchCapture_TrAddendaCount` | TField |  | Total number of addenda records in this batch. |
| 45 | `ACH.CAP.TR.ENTRY.HASH` | `AchCapture_TrEntryHash` | TField | Yes | 10 Positions - Company/Batch Control Record and File Control Record - Mandatory (all files)The Receiving DFI Identification in each Entry Detail Record is hashed to provide a check against inadvertent alteration of data contents due to hardware failure or program error. (NOTE: Addenda Records are not hashed.) |
| 46 | `ACH.CAP.TR.TOT.DR.DLLR.AMT` | `AchCapture_TrTotDrDllrAmt` | TField |  | Total Debit Dollar Amount of entries in the batch. |
| 47 | `ACH.CAP.TR.TOT.CR.DLLR.AMT` | `AchCapture_TrTotCrDllrAmt` | TField |  | Total Credit Dollar Amount of entires in the batch. |
| 48 | `ACH.CAP.TR.COMPANY.ID` | `AchCapture_TrCompanyId` | TField |  | 10 Positions - Company/Batch Control Record - Required (all batches)The Company Identification is an alphameric code used to identify an Originator. The Company Identification Field must be included on all Entries. |
| 49 | `ACH.CAP.TR.MSG.AUTH.CODE` | `AchCapture_TrMsgAuthCode` | TField | No | Message Authentication Code (MAC): 19 Positions - Company/Batch Control Record - Optional (all batches)The MAC is an-eight character code derived from a special key used in conjunction with the DES algorithm. The MAC is used to validate the authenticity of ACH Entries. The DES algorithm and key message standards must be in accordance with standards adopted by the American National Standards Institute. The remaining eleven characters of this field are blank. |
| 50 | `ACH.CAP.TR.RESERVED` | `AchCapture_TrReserved` | TField |  | Reserved Field |
| 51 | `ACH.CAP.TR.ORIG.DFI.ID` | `AchCapture_TrOrigDfiId` | TField |  | Company/Batch Control Record - 10 Positions. The Originator Identification is an alphameric code used to uniquely identify an Originator. |
| 52 | `ACH.CAP.TR.BATCH.NUMBER` | `AchCapture_TrBatchNumber` | TField | Yes | 7 Postions and mandatory for all Company/Batch Control record. The ODFI or its Sending Point assigns this number in ascending sequence to each batch in a File of Entries. |
| 53 | `ACH.CAP.STATUS` | `AchCapture_Status` | TField |  | Status of the batch. Valid values are None, Completed, or Voided. |
| 54 | `ACH.CAP.FILE.TYPE` | `AchCapture_FileType` | TField |  | File type valid values are, None, Inward, or Outward. |
| 55 | `ACH.CAP.NO.OF.RECORDS` | `AchCapture_NoOfRecords` | TField |  | Future use |
| 56 | `ACH.CAP.PAY.OPTION` | `AchCapture_PayOption` | TField |  | Requied to be Single Payment or Recurring Payment. Field that defines this batch/entries as Single Payment or Recurring Payment. Valid values are None, Recurring Payment, or Single Payment. |
| 57 | `ACH.CAP.PAYMENT.FREQUENCY` | `AchCapture_PaymentFrequency` | TField |  | Frequency of the Recurring Payment. This field is not used with pay option of Single Payment. |
| 58 | `ACH.CAP.MATURITY.DATE` | `AchCapture_MaturityDate` | TField |  | This field is required if Pay Option is set to Recurring Payment. If the field is set ot Single Payment it defaults in current date. |
| 59 | `ACH.CAP.NEXT.PAYMENT.DATE` | `AchCapture_NextPaymentDate` | TField |  | Calculated using the Payment Frequency if the pay option is Recurring Payment. |
| 60 | `ACH.CAP.ENTRY.TYPE` | `AchCapture_EntryType` |  |  |  |
| 61 | `ACH.CAP.PROCESSING.DATE` | `AchCapture_ProcessingDate` |  |  |  |
| 62 | `ACH.CAP.TRANSACTION.CODE` | `AchCapture_TransactionCode` |  |  |  |
| 63 | `ACH.CAP.BENEFICIARY.ID` | `AchCapture_BeneficiaryId` |  |  |  |
| 64 | `ACH.CAP.RECEIVING.DFI.ID` | `AchCapture_ReceivingDfiId` |  |  |  |
| 65 | `ACH.CAP.CHECK.DIGIT` | `AchCapture_CheckDigit` |  |  |  |
| 66 | `ACH.CAP.DFI.ACCOUNT.NUMBER` | `AchCapture_DfiAccountNumber` |  |  |  |
| 67 | `ACH.CAP.AMOUNT` | `AchCapture_Amount` |  |  |  |
| 68 | `ACH.CAP.INDIVIDUAL.ID.NO` | `AchCapture_IndividualIdNo` |  |  |  |
| 69 | `ACH.CAP.INDIVIDUAL.NAME` | `AchCapture_IndividualName` |  |  |  |
| 70 | `ACH.CAP.DISCRETIONARY.DATA` | `AchCapture_DiscretionaryData` |  |  |  |
| 71 | `ACH.CAP.ADDENDA.REC.IND` | `AchCapture_AddendaRecInd` |  |  |  |
| 72 | `ACH.CAP.TRACE.NUMBER` | `AchCapture_TraceNumber` |  |  |  |
| 73 | `ACH.CAP.CHECK.SERIAL.NO` | `AchCapture_CheckSerialNo` |  |  |  |
| 74 | `ACH.CAP.ROUTING.NO` | `AchCapture_RoutingNo` |  |  |  |
| 75 | `ACH.CAP.ADV.FILE.ID` | `AchCapture_AdvFileId` |  |  |  |
| 76 | `ACH.CAP.ACH.OP.DATA` | `AchCapture_AchOpData` |  |  |  |
| 77 | `ACH.CAP.ACH.OP.ROUTING` | `AchCapture_AchOpRouting` |  |  |  |
| 78 | `ACH.CAP.JULIAN.DATE` | `AchCapture_JulianDate` |  |  |  |
| 79 | `ACH.CAP.NO.ADD.REC` | `AchCapture_NoAddRec` |  |  |  |
| 80 | `ACH.CAP.TERMINAL.CITY` | `AchCapture_TerminalCity` |  |  |  |
| 81 | `ACH.CAP.TERMINAL.STATE` | `AchCapture_TerminalState` |  |  |  |
| 82 | `ACH.CAP.OFAC.INDICATOR` | `AchCapture_OfacIndicator` |  |  |  |
| 83 | `ACH.CAP.SECONDARY.OFAC.IND` | `AchCapture_SecondaryOfacInd` |  |  |  |
| 84 | `ACH.CAP.PAYMENT.TYPE.CODE` | `AchCapture_PaymentTypeCode` |  |  |  |
| 85 | `ACH.CAP.NARRATIVE` | `AchCapture_Narrative` |  |  |  |
| 86 | `ACH.CAP.ACH.RET.CODE` | `AchCapture_AchRetCode` |  |  |  |
| 87 | `ACH.CAP.ORIG.US.ACH.ENTRY` | `AchCapture_OrigUsAchEntry` |  |  |  |
| 88 | `ACH.CAP.ORIG.TRACE.NO` | `AchCapture_OrigTraceNo` |  |  |  |
| 89 | `ACH.CAP.ORIG.RECV.DFI.ID` | `AchCapture_OrigRecvDfiId` |  |  |  |
| 90 | `ACH.CAP.CARD.TXN.CODE` | `AchCapture_CardTxnCode` |  |  |  |
| 91 | `ACH.CAP.RECEIVING.CO.NAME` | `AchCapture_ReceivingCoName` |  |  |  |
| 92 | `ACH.CAP.CARD.EXPIRY.DATE` | `AchCapture_CardExpiryDate` |  |  |  |
| 93 | `ACH.CAP.DOCUMENT.REF.NO` | `AchCapture_DocumentRefNo` |  |  |  |
| 94 | `ACH.CAP.INDV.CARD.ACCT.NO` | `AchCapture_IndvCardAcctNo` |  |  |  |
| 95 | `ACH.CAP.PROCESS.CTRL.FLD` | `AchCapture_ProcessCtrlFld` |  |  |  |
| 96 | `ACH.CAP.ITEM.RESEARCH.NO` | `AchCapture_ItemResearchNo` |  |  |  |
| 97 | `ACH.CAP.ITEM.TYPE.INDI` | `AchCapture_ItemTypeIndi` |  |  |  |
| 98 | `ACH.CAP.ROUTING.CUSTOMER` | `AchCapture_RoutingCustomer` |  |  |  |
| 99 | `ACH.CAP.ENTRY.RESERVED.15` | `AchCapture_EntryReserved15` |  |  |  |
| 100 | `ACH.CAP.ENTRY.RESERVED.14` | `AchCapture_EntryReserved14` |  |  |  |
| 101 | `ACH.CAP.ENTRY.RESERVED.13` | `AchCapture_EntryReserved13` |  |  |  |
| 102 | `ACH.CAP.ENTRY.RESERVED.12` | `AchCapture_EntryReserved12` |  |  |  |
| 103 | `ACH.CAP.ENTRY.RESERVED.11` | `AchCapture_EntryReserved11` |  |  |  |
| 104 | `ACH.CAP.ENTRY.RESERVED.10` | `AchCapture_EntryReserved10` |  |  |  |
| 105 | `ACH.CAP.ENTRY.RESERVED.9` | `AchCapture_EntryReserved9` |  |  |  |
| 106 | `ACH.CAP.ENTRY.RESERVED.8` | `AchCapture_EntryReserved8` |  |  |  |
| 107 | `ACH.CAP.ENTRY.RESERVED.7` | `AchCapture_EntryReserved7` |  |  |  |
| 108 | `ACH.CAP.ENTRY.RESERVED.6` | `AchCapture_EntryReserved6` |  |  |  |
| 109 | `ACH.CAP.ENTRY.RESERVED.5` | `AchCapture_EntryReserved5` |  |  |  |
| 110 | `ACH.CAP.ENTRY.RESERVED.4` | `AchCapture_EntryReserved4` |  |  |  |
| 111 | `ACH.CAP.ENTRY.RESERVED.3` | `AchCapture_EntryReserved3` |  |  |  |
| 112 | `ACH.CAP.ENTRY.RESERVED.2` | `AchCapture_EntryReserved2` |  |  |  |
| 113 | `ACH.CAP.ENTRY.RESERVED.1` | `AchCapture_EntryReserved1` |  |  |  |
| 114 | `ACH.CAP.ADDENDA.TYPE.CODE` | `AchCapture_AddendaTypeCode` |  |  |  |
| 115 | `ACH.CAP.PAYMENT.INFO` | `AchCapture_PaymentInfo` |  |  |  |
| 116 | `ACH.CAP.RET.REASON.CODE` | `AchCapture_RetReasonCode` |  |  |  |
| 117 | `ACH.CAP.DATE.OF.DEATH` | `AchCapture_DateOfDeath` |  |  |  |
| 118 | `ACH.CAP.ADDENDA.INFO` | `AchCapture_AddendaInfo` |  |  |  |
| 119 | `ACH.CAP.RET.RESERVED` | `AchCapture_RetReserved` |  |  |  |
| 120 | `ACH.CAP.ORIG.FWD.ENT.PAYAMT` | `AchCapture_OrigFwdEntPayamt` |  |  |  |
| 121 | `ACH.CAP.DISHON.RET.REASON` | `AchCapture_DishonRetReason` |  |  |  |
| 122 | `ACH.CAP.DISHON.RESERVED1` | `AchCapture_DishonReserved1` |  |  |  |
| 123 | `ACH.CAP.DISHON.RESERVED2` | `AchCapture_DishonReserved2` |  |  |  |
| 124 | `ACH.CAP.RET.TRACE.NO` | `AchCapture_RetTraceNo` |  |  |  |
| 125 | `ACH.CAP.RET.SETTLE.DATE` | `AchCapture_RetSettleDate` |  |  |  |
| 126 | `ACH.CAP.CONTEST.RET.REASON` | `AchCapture_ContestRetReason` |  |  |  |
| 127 | `ACH.CAP.CONTEST.ORIG.RET.DATE` | `AchCapture_ContestOrigRetDate` |  |  |  |
| 128 | `ACH.CAP.ORIG.SETTLEMENT.DATE` | `AchCapture_OrigSettlementDate` |  |  |  |
| 129 | `ACH.CAP.DISHON.RET.TRACE.NO` | `AchCapture_DishonRetTraceNo` |  |  |  |
| 130 | `ACH.CAP.DISHON.RET.SETTL.DATE` | `AchCapture_DishonRetSettlDate` |  |  |  |
| 131 | `ACH.CAP.CONTEST.RESERVED` | `AchCapture_ContestReserved` |  |  |  |
| 132 | `ACH.CAP.IAT.TRAN.TYPE.CODE` | `AchCapture_IatTranTypeCode` |  |  |  |
| 133 | `ACH.CAP.FOREIGN.PAYMENT.AMT` | `AchCapture_ForeignPaymentAmt` |  |  |  |
| 134 | `ACH.CAP.FOREIGN.TRACE.NO` | `AchCapture_ForeignTraceNo` |  |  |  |
| 135 | `ACH.CAP.RECEIVING.COMP.NAME` | `AchCapture_ReceivingCompName` |  |  |  |
| 136 | `ACH.CAP.IAT.RESERVED.1` | `AchCapture_IatReserved1` |  |  |  |
| 137 | `ACH.CAP.ORIGINATOR.NAME` | `AchCapture_OriginatorName` |  |  |  |
| 138 | `ACH.CAP.ORIGINATOR.ADDRS` | `AchCapture_OriginatorAddrs` |  |  |  |
| 139 | `ACH.CAP.IAT.RESERVED.2` | `AchCapture_IatReserved2` |  |  |  |
| 140 | `ACH.CAP.ORIGINATOR.CITY` | `AchCapture_OriginatorCity` |  |  |  |
| 141 | `ACH.CAP.ORIGINATOR.CO.POST` | `AchCapture_OriginatorCoPost` |  |  |  |
| 142 | `ACH.CAP.IAT.RESERVED.3` | `AchCapture_IatReserved3` |  |  |  |
| 143 | `ACH.CAP.ORIGINATOR.DFINAME` | `AchCapture_OriginatorDfiname` |  |  |  |
| 144 | `ACH.CAP.ODFI.ID.QUALIFIER` | `AchCapture_OdfiIdQualifier` |  |  |  |
| 145 | `ACH.CAP.ODFI.ID` | `AchCapture_OdfiId` |  |  |  |
| 146 | `ACH.CAP.ODFI.BRANCH.COCODE` | `AchCapture_OdfiBranchCocode` |  |  |  |
| 147 | `ACH.CAP.IAT.RESERVED.4` | `AchCapture_IatReserved4` |  |  |  |
| 148 | `ACH.CAP.RECEIVING.DFINAME` | `AchCapture_ReceivingDfiname` |  |  |  |
| 149 | `ACH.CAP.RDFI.ID.QUALIFIER` | `AchCapture_RdfiIdQualifier` |  |  |  |
| 150 | `ACH.CAP.RDFI.ID` | `AchCapture_RdfiId` |  |  |  |
| 151 | `ACH.CAP.RDFI.BRANCH.COCODE` | `AchCapture_RdfiBranchCocode` |  |  |  |
| 152 | `ACH.CAP.IAT.RESERVED.5` | `AchCapture_IatReserved5` |  |  |  |
| 153 | `ACH.CAP.RECEIVER.ID` | `AchCapture_ReceiverId` |  |  |  |
| 154 | `ACH.CAP.RECEIVER.ADDRESS` | `AchCapture_ReceiverAddress` |  |  |  |
| 155 | `ACH.CAP.IAT.RESERVED.6` | `AchCapture_IatReserved6` |  |  |  |
| 156 | `ACH.CAP.RECEIVER.CITY` | `AchCapture_ReceiverCity` |  |  |  |
| 157 | `ACH.CAP.RECEIVER.CO.POST` | `AchCapture_ReceiverCoPost` |  |  |  |
| 158 | `ACH.CAP.IAT.RESERVED.7` | `AchCapture_IatReserved7` |  |  |  |
| 159 | `ACH.CAP.IAT.PAYMENT.INFO.1` | `AchCapture_IatPaymentInfo1` |  |  |  |
| 160 | `ACH.CAP.IAT.PAYMENT.INFO.2` | `AchCapture_IatPaymentInfo2` |  |  |  |
| 161 | `ACH.CAP.FCB.NAME.1` | `AchCapture_FcbName1` |  |  |  |
| 162 | `ACH.CAP.FCB.ID.QUALIFIER.1` | `AchCapture_FcbIdQualifier1` |  |  |  |
| 163 | `ACH.CAP.FCB.ID.1` | `AchCapture_FcbId1` |  |  |  |
| 164 | `ACH.CAP.FCB.BRANCH.CODE.1` | `AchCapture_FcbBranchCode1` |  |  |  |
| 165 | `ACH.CAP.FCB.RESERVED.1` | `AchCapture_FcbReserved1` |  |  |  |
| 166 | `ACH.CAP.FCB.NAME.2` | `AchCapture_FcbName2` |  |  |  |
| 167 | `ACH.CAP.FCB.ID.QUALIFIER.2` | `AchCapture_FcbIdQualifier2` |  |  |  |
| 168 | `ACH.CAP.FCB.ID.2` | `AchCapture_FcbId2` |  |  |  |
| 169 | `ACH.CAP.FCB.BRANCH.CODE.2` | `AchCapture_FcbBranchCode2` |  |  |  |
| 170 | `ACH.CAP.FCB.RESERVED.2` | `AchCapture_FcbReserved2` |  |  |  |
| 171 | `ACH.CAP.FCB.NAME.3` | `AchCapture_FcbName3` |  |  |  |
| 172 | `ACH.CAP.FCB.ID.QUALIFIER.3` | `AchCapture_FcbIdQualifier3` |  |  |  |
| 173 | `ACH.CAP.FCB.ID.3` | `AchCapture_FcbId3` |  |  |  |
| 174 | `ACH.CAP.FCB.BRANCH.CODE.3` | `AchCapture_FcbBranchCode3` |  |  |  |
| 175 | `ACH.CAP.FCB.RESERVED.3` | `AchCapture_FcbReserved3` |  |  |  |
| 176 | `ACH.CAP.TXN.DESCRIPTION` | `AchCapture_TxnDescription` |  |  |  |
| 177 | `ACH.CAP.NETWORK.ID.CODE` | `AchCapture_NetworkIdCode` |  |  |  |
| 178 | `ACH.CAP.TERMINAL.ID.CODE` | `AchCapture_TerminalIdCode` |  |  |  |
| 179 | `ACH.CAP.TXN.SERIAL.NO` | `AchCapture_TxnSerialNo` |  |  |  |
| 180 | `ACH.CAP.TXN.DATE` | `AchCapture_TxnDate` |  |  |  |
| 181 | `ACH.CAP.TXN.TIME` | `AchCapture_TxnTime` |  |  |  |
| 182 | `ACH.CAP.TERMINAL.LOCATION` | `AchCapture_TerminalLocation` |  |  |  |
| 183 | `ACH.CAP.REF.INFO1` | `AchCapture_RefInfo1` |  |  |  |
| 184 | `ACH.CAP.REF.INFO2` | `AchCapture_RefInfo2` |  |  |  |
| 185 | `ACH.CAP.AUTHCODE.CARD.DATE` | `AchCapture_AuthcodeCardDate` |  |  |  |
| 186 | `ACH.CAP.CHANGE.CODE` | `AchCapture_ChangeCode` |  |  |  |
| 187 | `ACH.CAP.ADDENDA.SEQ.NO` | `AchCapture_AddendaSeqNo` |  |  |  |
| 188 | `ACH.CAP.ORIG.ENTRY.TRACENO` | `AchCapture_OrigEntryTraceno` |  |  |  |
| 189 | `ACH.CAP.CORRECTED.DATA` | `AchCapture_CorrectedData` |  |  |  |
| 190 | `ACH.CAP.ORIGINAL.RDFI.ID` | `AchCapture_OriginalRdfiId` |  |  |  |
| 191 | `ACH.CAP.REFUSED.COR.CODE` | `AchCapture_RefusedCorCode` |  |  |  |
| 192 | `ACH.CAP.COR.TRACE.SEQ.NO` | `AchCapture_CorTraceSeqNo` |  |  |  |
| 193 | `ACH.CAP.ACH.BEN.NAME` | `AchCapture_AchBenName` |  |  |  |
| 194 | `ACH.CAP.ADDENDA.RESERVED.10` | `AchCapture_AddendaReserved10` |  |  |  |
| 195 | `ACH.CAP.ADDENDA.RESERVED.9` | `AchCapture_AddendaReserved9` |  |  |  |
| 196 | `ACH.CAP.ADDENDA.RESERVED.8` | `AchCapture_AddendaReserved8` |  |  |  |
| 197 | `ACH.CAP.ADDENDA.RESERVED.7` | `AchCapture_AddendaReserved7` |  |  |  |
| 198 | `ACH.CAP.ADDENDA.RESERVED.6` | `AchCapture_AddendaReserved6` |  |  |  |
| 199 | `ACH.CAP.ADDENDA.RESERVED.5` | `AchCapture_AddendaReserved5` |  |  |  |
| 200 | `ACH.CAP.ADDENDA.RESERVED.4` | `AchCapture_AddendaReserved4` |  |  |  |
| 201 | `ACH.CAP.ADDENDA.RESERVED.3` | `AchCapture_AddendaReserved3` |  |  |  |
| 202 | `ACH.CAP.ADDENDA.RESERVED.2` | `AchCapture_AddendaReserved2` |  |  |  |
| 203 | `ACH.CAP.ADDENDA.RESERVED.1` | `AchCapture_AddendaReserved1` |  |  |  |
| 204 | `ACH.CAP.SAVE.TEMPLATE` | `AchCapture_SaveTemplate` | TField |  | Code to save this adhoc batch/entry as a template. Valid vaules is No or Yes. |
| 205 | `ACH.CAP.TEMPLATE.NAME` | `AchCapture_TemplateName` | TField |  | Description of Template. Field is required if Save Template equals Yes. |
| 206 | `ACH.CAP.RETURN.ENTRY.ID` | `AchCapture_ReturnEntryId` | TField |  | This field holds the ACH.ENTRIES record id which needs to be returned to FED |
| 207 | `ACH.CAP.CHANGE.ENTRY.ID` | `AchCapture_ChangeEntryId` | TField |  | This field holds the ACH.ENTRIES record id which needs to generated an outward NOC |
| 208 | `ACH.CAP.PROCESS.DATE` | `AchCapture_ProcessDate` | TField |  |  |
| 209 | `ACH.CAP.CAPTURE.RESERVED.8` | `AchCapture_CaptureReserved8` | TField |  | Reserved Field |
| 210 | `ACH.CAP.CAPTURE.RESERVED.7` | `AchCapture_CaptureReserved7` | TField |  | Reserved Field |
| 211 | `ACH.CAP.CAPTURE.RESERVED.6` | `AchCapture_CaptureReserved6` | TField |  | Reserved Field |
| 212 | `ACH.CAP.CAPTURE.RESERVED.5` | `AchCapture_CaptureReserved5` | TField |  | Reserved Field |
| 213 | `ACH.CAP.CAPTURE.RESERVED.4` | `AchCapture_CaptureReserved4` | TField |  | Reserved Field |
| 214 | `ACH.CAP.CAPTURE.RESERVED.3` | `AchCapture_CaptureReserved3` | TField |  | Reserved Field |
| 215 | `ACH.CAP.CAPTURE.RESERVED.2` | `AchCapture_CaptureReserved2` | TField |  | Reserved Field |
| 216 | `ACH.CAP.CAPTURE.RESERVED.1` | `AchCapture_CaptureReserved1` | TField |  | Reserved Field |
| 217 | `ACH.CAP.LOCAL.REF` | `AchCapture_LocalRef` |  |  |  |
| 218 | `ACH.CAP.STMT.NOS` | `AchCapture_StmtNos` |  |  |  |
| 219 | `ACH.CAP.OVERRIDE` | `AchCapture_Override` |  |  |  |
| 220 | `ACH.CAP.RECORD.STATUS` | `AchCapture_RecordStatus` | String |  |  |
| 221 | `ACH.CAP.CURR.NO` | `AchCapture_CurrNo` | String |  |  |
| 222 | `ACH.CAP.INPUTTER` | `AchCapture_Inputter` |  |  |  |
| 223 | `ACH.CAP.DATE.TIME` | `AchCapture_DateTime` |  |  |  |
| 224 | `ACH.CAP.AUTHORISER` | `AchCapture_Authoriser` | String |  |  |
| 225 | `ACH.CAP.CO.CODE` | `AchCapture_CoCode` | String |  |  |
| 226 | `ACH.CAP.DEPT.CODE` | `AchCapture_DeptCode` | String |  |  |
| 227 | `ACH.CAP.AUDITOR.CODE` | `AchCapture_AuditorCode` | String |  |  |
| 228 | `ACH.CAP.AUDIT.DATE.TIME` | `AchCapture_AuditDateTime` | String |  |  |
