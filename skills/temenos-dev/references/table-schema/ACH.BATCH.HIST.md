# ACH.BATCH.HIST — Table Schema

> Source: `INSERTS/I_F.ACH.BATCH.HIST` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHBAT.HIST.REC.TYPE.CODE` | `AchBatchHist_RecTypeCode` | TField |  | ACH company/batch header record type code always equal to 5. |
| 2 | `ACHBAT.HIST.SVC.CLASS.CODE` | `AchBatchHist_SvcClassCode` | TField | Yes | 3 positions, mandatory for all batches. The Service Class Code (BAI Specifications) identifies the general classification of the dollar entries to be exchanged. ACH Entries are assigned Sercive Class Code series 200-299. Code values are: 200 ACH Entries Mixed Debits and Credits 220 ACH Credits Only 225 ACH Debits Only 280 ACH Automated Accounting Advices |
| 3 | `ACHBAT.HIST.COMPANY.NAME` | `AchBatchHist_CompanyName` | TField | Yes | 16 Positions. Mandatory for all batches except IAT. This field identifies the source of the Entry and is used for descriptive purposes for the Receiver. See NACHA Guidelines for specific requirements. |
| 4 | `ACHBAT.HIST.COMPANY.DATA` | `AchBatchHist_CompanyData` | TField |  | 20 Positions. This field allows Originators and/or ODFIs to include codes (one or more), of significance only to them, to enable specialized handling of all Entries in that batches.There is no standardized interpretation for the value of the field. This field must be returned intact on any Return Entry. |
| 5 | `ACHBAT.HIST.COMPANY.ID` | `AchBatchHist_CompanyId` | TField | Yes | 10 Positons, mandatory for all batches except IAT. This is an alphameric code used to identify an Originator. See NACHA Guidelines for specific requirements. |
| 6 | `ACHBAT.HIST.ENTRY.CLASS.CODE` | `AchBatchHist_EntryClassCode` | TField | Yes | 3 positions, mandatory for all batches. This field contains a three-character code used to identify various types of entries. See the NACHA Guidelines for a list of Standard Entry Class Codes. |
| 7 | `ACHBAT.HIST.COMPANY.ENT.DESC` | `AchBatchHist_CompanyEntDesc` | TField | Yes | 10 Positions. Mandatory for all batches. The Originator establishes the value of this field to provide the Receiver with a description of the purpose of the Entry. See the NACHA Guidelines for specific requirements. |
| 8 | `ACHBAT.HIST.COMPANY.DESC.DATE` | `AchBatchHist_CompanyDescDate` | TField | No | 6 Positions, optional field. The Originator establishes this field as the date it would like to see displayed to the Receiver for descriptive purposes. See the NACHA Guidelines for specific requirements. |
| 9 | `ACHBAT.HIST.EFFECTIVE.DATE` | `AchBatchHist_EffectiveDate` | TField |  | 6 Positions and required for all batches. This date is specified by the Originator on which it entends a batch of Entries to be settled. See the NACHA Guidelines for specific requirements. |
| 10 | `ACHBAT.HIST.SETTLE.JUL.DATE` | `AchBatchHist_SettleJulDate` | TField |  | 3 Positions. Inserted by Receiving ACH Operator (all batches). The Settlement Date (a 3-digit Julian date) for a batch of Entries is inserted by the Receiving ACH Operator. This is the date on which the Particiating DFI or its correspondent is scheduled to be debited or credited by the Federal Reserve. See the NACHA Guidelines for specific requirements. |
| 11 | `ACHBAT.HIST.ORIG.STATUS.CODE` | `AchBatchHist_OrigStatusCode` | TField | Yes | 1 Position and mandatory for all batches. This code refers to the ODFI initiating the Entry. Code Values: 0 ADV File prepared by an ACH Operartor. 1 This code indentifies the Originator as a depository financial institution. 2 This code identifies the Originator as a Federal Government entity or agency. |
| 12 | `ACHBAT.HIST.ORIG.DFI.ID` | `AchBatchHist_OrigDfiId` | TField |  | 10 Positions. The Originator Identification is an alphameric code used to uniquely identify an Originator. |
| 13 | `ACHBAT.HIST.BATCH.NUMBER` | `AchBatchHist_BatchNumber` | TField | Yes | 7 Postions and mandatory for all batches. The ODFI or its Sending Point assigns this number in ascending sequence to each batch in a File of Entries. |
| 14 | `ACHBAT.HIST.VALUE.DATE` | `AchBatchHist_ValueDate` | TField |  | ACH Effective Entry Date. The date specified by the originator on which it intends a batch of entries to be settled. For ACH credits, the effective entry date must be one or two banking days following the processing date. |
| 15 | `ACHBAT.HIST.IMMEDIATE.ORIGIN` | `AchBatchHist_ImmediateOrigin` | TField | Yes | 10 Positions and mandatory for all Files. ACH File header record. Identifies the sender of the file. This field contains the routing number of the ACH Operator or Sending Point that is Transmitting the File. The 10 characterfield begins with a blank in the first position, followed byt the four digit Federal Reserve Routing Symbol, the four digit ABA Institution Identifier, and the Check Digit. |
| 16 | `ACHBAT.HIST.DEBIT.COUNT` | `AchBatchHist_DebitCount` | TField |  | Total number of debit entries in the batch. |
| 17 | `ACHBAT.HIST.CREDIT.COUNT` | `AchBatchHist_CreditCount` | TField |  | Total number of credit entries in the batch. |
| 18 | `ACHBAT.HIST.IAT.INDICATOR` | `AchBatchHist_IatIndicator` | TField | Conditional | 16 Positions - Company/Batch Header Record - Optional (IAT, Returns); 16 Positions - Company/Batch Header Record - Mandatory (COR entries related to IAT)For forward IAT Entries, this field is left blank. For Notifications of Change related to IAT Entries, this field must contain the value "IATCOR" |
| 19 | `ACHBAT.HIST.IAT.FX.INDICATOR` | `AchBatchHist_IatFxIndicator` | TField | Yes | 2 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR)This field contains a code used to indicate the foreign exchange conversion methodology applied to an IAT Entry. Use may be dependent on the particular exchange services offered by a Gateway Operator. See NACHA Guidelines for valid code values for this field. |
| 20 | `ACHBAT.HIST.IAT.FX.REF.INDIC` | `AchBatchHist_IatFxRefIndic` | TField |  | 1 Position - Company/Batch Header Record - Required (IAT, Returns, COR)This field contains a code used to indicate the content of the Foreign Exchange Reference Field. See NACHA Guidelines for valid code values for this field. |
| 21 | `ACHBAT.HIST.IAT.FX.REF` | `AchBatchHist_IatFxRef` | TField |  | 15 Positions - Company/Batch Header Record - Required (IAT, Returns, COR)This field contains either the foreign exchange rate used to execute the foreign exchange conversion of an IAT Entry or another reference to the foreign exchange transaction. Content is defined by the Foreign Exchange Reference Indicator Field.If the Foreign Exchange Indicator Field contains "FF", this field will always be space filled. |
| 22 | `ACHBAT.HIST.ISO.DEST.CO.CODE` | `AchBatchHist_IsoDestCoCode` |  |  |  |
| 23 | `ACHBAT.HIST.ORIGINATOR.ID` | `AchBatchHist_OriginatorId` | TField | Yes | Originator Identification: 10 Positions - Company/Batch Header Record - Mandatory (IAT, IAT Returns, IAT COR)The Originator Identification is an alphameric code used to uniquely identify an Originator. This is the ID that is set up in the ACH.CORPORATE.INFO table. |
| 24 | `ACHBAT.HIST.ISO.ORIG.CCY.CODE` | `AchBatchHist_IsoOrigCcyCode` | TField | Yes | 3 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR).This field contains the three-character code, as approved by the International Organization for Standardization (ISO), to identify the currency denomination in which the Entry was first originated. |
| 25 | `ACHBAT.HIST.ISO.DEST.CCY.CODE` | `AchBatchHist_IsoDestCcyCode` | TField | Yes | 3 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR)This field contains the three-character code, as approved by the International Organization for Standardization (ISO), to identify the currency denomination in which the Entry is to be received. |
| 26 | `ACHBAT.HIST.LOAD.DATE` | `AchBatchHist_LoadDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 27 | `ACHBAT.HIST.TR.REC.TYPE.CODE` | `AchBatchHist_TrRecTypeCode` | TField |  | ACH company/batch control record type code always equal to 5. |
| 28 | `ACHBAT.HIST.TR.SVC.CLASS.CODE` | `AchBatchHist_TrSvcClassCode` | TField | Yes | 3 positions, mandatory for all batch control records. The Service Class Code (BAI Specifications) identifies the general classification of the dollar entries to be exchanged. ACH Entries are assigned Sercive Class Code series 200-299. Code values are: 200 ACH Entries Mixed Debits and Credits 220 ACH Credits Only 225 ACH Debits Only 280 ACH Automated Accounting Advices |
| 29 | `ACHBAT.HIST.TR.ADDENDA.COUNT` | `AchBatchHist_TrAddendaCount` | TField |  | Total number of addenda records in this batch. |
| 30 | `ACHBAT.HIST.TR.ENTRY.HASH` | `AchBatchHist_TrEntryHash` | TField | Yes | 10 Positions - Company/Batch Control Record and File Control Record - Mandatory (all files)The Receiving DFI Identification in each Entry Detail Record is hashed to provide a check against inadvertent alteration of data contents due to hardware failure or program error. (NOTE: Addenda Records are not hashed.) |
| 31 | `ACHBAT.HIST.TR.TOT.DR.DLLR.AMT` | `AchBatchHist_TrTotDrDllrAmt` | TField |  | Total Debit Dollar Amount of entries in the batch. |
| 32 | `ACHBAT.HIST.TR.TOT.CR.DLLR.AMT` | `AchBatchHist_TrTotCrDllrAmt` | TField |  | Total Credit Dollar Amount of entires in the batch. |
| 33 | `ACHBAT.HIST.TR.COMPANY.ID` | `AchBatchHist_TrCompanyId` | TField |  | 10 Positions - Company/Batch Control Record - Required (all batches)The Company Identification is an alphameric code used to identify an Originator. The Company Identification Field must be included on all Entries. |
| 34 | `ACHBAT.HIST.TR.MSG.AUTH.CODE` | `AchBatchHist_TrMsgAuthCode` | TField | No | Message Authentication Code (MAC): 19 Positions - Company/Batch Control Record - Optional (all batches)The MAC is an-eight character code derived from a special key used in conjunction with the DES algorithm. The MAC is used to validate the authenticity of ACH Entries. The DES algorithm and key message standards must be in accordance with standards adopted by the American National Standards Institute. The remaining eleven characters of this field are blank. |
| 35 | `ACHBAT.HIST.TR.RESERVED` | `AchBatchHist_TrReserved` | TField |  | Reserved field. |
| 36 | `ACHBAT.HIST.TR.ORIG.DFI.ID` | `AchBatchHist_TrOrigDfiId` | TField |  | Company/Batch Control Record - 10 Positions. The Originator Identification is an alphameric code used to uniquely identify an Originator. |
| 37 | `ACHBAT.HIST.TR.BATCH.NUMBER` | `AchBatchHist_TrBatchNumber` | TField | Yes | 7 Postions and mandatory for all Company/Batch Control record. The ODFI or its Sending Point assigns this number in ascending sequence to each batch in a File of Entries. |
| 38 | `ACHBAT.HIST.STATUS` | `AchBatchHist_Status` | TField |  | Status of the batch. Valid values are ACK, Cancelled, Cleared, Data Error, Delivered, Exception, Loaded,Limit Breached, Nack, Pending, Prefunded, Processed, Rejected, Returned, Validated, Validation Error, or Voided. |
| 39 | `ACHBAT.HIST.FILE.TYPE` | `AchBatchHist_FileType` | TField |  | File type valid values are, None, Inward, or Outward. |
| 40 | `ACHBAT.HIST.FILE.SOURCE` | `AchBatchHist_FileSource` | TField |  | File source valid values are, None, Corporate, or Fed. |
| 41 | `ACHBAT.HIST.REVERSAL.INDICATOR` | `AchBatchHist_ReversalIndicator` | TField |  | Future use |
| 42 | `ACHBAT.HIST.SETTLEMENT.DATE` | `AchBatchHist_SettlementDate` | TField |  | 3 Positions. Inserted by Receiving ACH Operator (all batches). The Settlement Date (a 3-digit Julian date) for a batch of Entries is inserted by the Receiving ACH Operator. This is the date on which the Particiating DFI or its correspondent is scheduled to be debited or credited by the Federal Reserve. See the NACHA Guidelines for specific requirements. |
| 43 | `ACHBAT.HIST.SETTLE.DR.AC` | `AchBatchHist_SettleDrAc` | TField |  | Debit Account in which the ACH funds are settled. |
| 44 | `ACHBAT.HIST.SETTLE.CR.AC` | `AchBatchHist_SettleCrAc` | TField |  | Credit Account in which the ACH funds are settled. |
| 45 | `ACHBAT.HIST.SETTLEMENT.TXN.REF` | `AchBatchHist_SettlementTxnRef` |  |  |  |
| 46 | `ACHBAT.HIST.SETTLEMENT.COMPANY` | `AchBatchHist_SettlementCompany` | TField |  | Company defined in the ACH.CLEARING.PARAMETER in the Routing Company.1 field. |
| 47 | `ACHBAT.HIST.RESERVED.17` | `AchBatchHist_Reserved17` | TField |  | Reserved field. |
| 48 | `ACHBAT.HIST.RESERVED.16` | `AchBatchHist_Reserved16` | TField |  | Reserved field. |
| 49 | `ACHBAT.HIST.FIN.ENTRY.COUNT` | `AchBatchHist_FinEntryCount` | TField |  | Number of Financial Entries in the Batch. |
| 50 | `ACHBAT.HIST.NONFIN.ENTRY.COUNT` | `AchBatchHist_NonfinEntryCount` | TField |  | Number of Non-Financial Entires in the Batch. |
| 51 | `ACHBAT.HIST.PRE.FUNDING` | `AchBatchHist_PreFunding` | TField |  | Future use |
| 52 | `ACHBAT.HIST.ACH.FILE.ID` | `AchBatchHist_AchFileId` | TField |  | ID of the ACH file. |
| 53 | `ACHBAT.HIST.TAPE.REF` | `AchBatchHist_TapeRef` | TField |  | Name of the file. |
| 54 | `ACHBAT.HIST.AML.RESPONSE` | `AchBatchHist_AmlResponse` | TField |  | Response from AML system. Valid values are Null, 0, 1, Clean, or Hit. |
| 55 | `ACHBAT.HIST.AML.REJ.REASON` | `AchBatchHist_AmlRejReason` | TField |  | Reason from the AML system that the batch was rejected. |
| 56 | `ACHBAT.HIST.AML.VERIFICATION` | `AchBatchHist_AmlVerification` | TField |  | Field that determines if AML verification is used for this file |
| 57 | `ACHBAT.HIST.AML.LEVELS` | `AchBatchHist_AmlLevels` | TField |  | Level set in ACH.AML.PARAMETER. Values are Null, 0, 1, or 2. |
| 58 | `ACHBAT.HIST.AML.RESERVED.3` | `AchBatchHist_AmlReserved3` | TField |  | Reserved field. |
| 59 | `ACHBAT.HIST.AML.RESERVED.2` | `AchBatchHist_AmlReserved2` | TField |  | Reserved field. |
| 60 | `ACHBAT.HIST.AML.RESERVED.1` | `AchBatchHist_AmlReserved1` | TField |  | Reserved field. |
| 61 | `ACHBAT.HIST.BATCH.XREF` | `AchBatchHist_BatchXref` | TField |  | Future use |
| 62 | `ACHBAT.HIST.BATCH.RECORD` | `AchBatchHist_BatchRecord` | TField |  | System Populated field. This field stores entire batch header record for an outward file |
| 63 | `ACHBAT.HIST.BATCH.TR.RECORD` | `AchBatchHist_BatchTrRecord` | TField |  | System Populated field. This field stores entire batch control record for an outward file |
| 64 | `ACHBAT.HIST.RETURN.BATCH` | `AchBatchHist_ReturnBatch` | TField |  | Whether or not this is a return batch. Valid values are None, No, or Yes. |
| 65 | `ACHBAT.HIST.REMARKS` | `AchBatchHist_Remarks` |  |  |  |
| 66 | `ACHBAT.HIST.LAST.UPDATE.DATE` | `AchBatchHist_LastUpdateDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 67 | `ACHBAT.HIST.ACH.OP.DATA` | `AchBatchHist_AchOpData` | TField |  |  |
| 68 | `ACHBAT.HIST.SAME.DAY` | `AchBatchHist_SameDay` | TField |  | This field will be flagged with the value 'Y' by the ACH.UPLOAD.WAHREHOUSE and ACH.CAPTURE.UPDATE.WAREHOUSE service if the batch is a same day batch. |
| 69 | `ACHBAT.HIST.DECISION.REASON` | `AchBatchHist_DecisionReason` | TField |  | This user will be able to capture the reason/information for the decision taken on the batch that had breached the limit. The decision can be either to process the batch if the status is 'loaded' or void the batch if the status is 'voided'. |
| 70 | `ACHBAT.HIST.PROCESSING.DATE` | `AchBatchHist_ProcessingDate` | TField |  |  |
| 71 | `ACHBAT.HIST.PREFUND.CODEWORD` | `AchBatchHist_PrefundCodeword` | TField |  |  |
| 72 | `ACHBAT.HIST.OFFSET.DEFAULT` | `AchBatchHist_OffsetDefault` | TField |  | This field will be set to N if the ACH.CAPTURE record is input through one of the versions which are used to originate a same day DEBIT transaction. |
| 73 | `ACHBAT.HIST.RESERVED.3` | `AchBatchHist_Reserved3` | TField |  | Reserved field. |
| 74 | `ACHBAT.HIST.RESERVED.2` | `AchBatchHist_Reserved2` | TField |  | Reserved field. |
| 75 | `ACHBAT.HIST.RESERVED.1` | `AchBatchHist_Reserved1` | TField |  | Reserved field. |
| 76 | `ACHBAT.HIST.LOCAL.REF` | `AchBatchHist_LocalRef` |  |  |  |
| 77 | `ACHBAT.HIST.OVERRIDE` | `AchBatchHist_Override` |  |  |  |
