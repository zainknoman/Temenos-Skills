# ACH.BATCH — Table Schema

> Source: `INSERTS/I_F.ACH.BATCH` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.BAT.REC.TYPE.CODE` | `AchBatch_RecTypeCode` | TField |  | ACH company/batch header record type code always equal to 5. |
| 2 | `ACH.BAT.SVC.CLASS.CODE` | `AchBatch_SvcClassCode` | TField | Yes | 3 positions, mandatory for all batches. The Service Class Code (BAI Specifications) identifies the general classification of the dollar entries to be exchanged. ACH Entries are assigned Sercive Class Code series 200-299. Code values are: 200 ACH Entries Mixed Debits and Credits 220 ACH Credits Only 225 ACH Debits Only 280 ACH Automated Accounting Advices |
| 3 | `ACH.BAT.COMPANY.NAME` | `AchBatch_CompanyName` | TField | Yes | 16 Positions. Mandatory for all batches except IAT. This field identifies the source of the Entry and is used for descriptive purposes for the Receiver. See NACHA Guidelines for specific requirements. |
| 4 | `ACH.BAT.COMPANY.DATA` | `AchBatch_CompanyData` | TField |  | 20 Positions. This field allows Originators and/or ODFIs to include codes (one or more), of significance only to them, to enable specialized handling of all Entries in that batches.There is no standardized interpretation for the value of the field. This field must be returned intact on any Return Entry. |
| 5 | `ACH.BAT.COMPANY.ID` | `AchBatch_CompanyId` | TField | Yes | 10 Positons, mandatory for all batches except IAT. This is an alphameric code used to identify an Originator. See NACHA Guidelines for specific requirements. |
| 6 | `ACH.BAT.ENTRY.CLASS.CODE` | `AchBatch_EntryClassCode` | TField | Yes | 3 positions, mandatory for all batches. This field contains a three-character code used to identify various types of entries. See the NACHA Guidelines for a list of Standard Entry Class Codes. |
| 7 | `ACH.BAT.COMPANY.ENT.DESC` | `AchBatch_CompanyEntDesc` | TField | Yes | 10 Positions. Mandatory for all batches. The Originator establishes the value of this field to provide the Receiver with a description of the purpose of the Entry. See the NACHA Guidelines for specific requirements. |
| 8 | `ACH.BAT.COMPANY.DESC.DATE` | `AchBatch_CompanyDescDate` | TField | No | 6 Positions, optional field. The Originator establishes this field as the date it would like to see displayed to the Receiver for descriptive purposes. See the NACHA Guidelines for specific requirements. |
| 9 | `ACH.BAT.EFFECTIVE.DATE` | `AchBatch_EffectiveDate` | TField |  | 6 Positions and required for all batches. This date is specified by the Originator on which it entends a batch of Entries to be settled. See the NACHA Guidelines for specific requirements. |
| 10 | `ACH.BAT.SETTLE.JUL.DATE` | `AchBatch_SettleJulDate` | TField |  | 3 Positions. Inserted by Receiving ACH Operator (all batches). The Settlement Date (a 3-digit Julian date) for a batch of Entries is inserted by the Receiving ACH Operator. This is the date on which the Particiating DFI or its correspondent is scheduled to be debited or credited by the Federal Reserve. See the NACHA Guidelines for specific requirements. |
| 11 | `ACH.BAT.ORIG.STATUS.CODE` | `AchBatch_OrigStatusCode` | TField | Yes | 1 Position and mandatory for all batches. This code refers to the ODFI initiating the Entry. Code Values: 0 ADV File prepared by an ACH Operartor. 1 This code indentifies the Originator as a depository financial institution. 2 This code identifies the Originator as a Federal Government entity or agency. |
| 12 | `ACH.BAT.ORIG.DFI.ID` | `AchBatch_OrigDfiId` | TField |  | 10 Positions. The Originator Identification is an alphameric code used to uniquely identify an Originator. |
| 13 | `ACH.BAT.BATCH.NUMBER` | `AchBatch_BatchNumber` | TField | Yes | 7 Postions and mandatory for all batches. The ODFI or its Sending Point assigns this number in ascending sequence to each batch in a File of Entries. |
| 14 | `ACH.BAT.VALUE.DATE` | `AchBatch_ValueDate` | TField |  | ACH Effective Entry Date. The date specified by the originator on which it intends a batch of entries to be settled. For ACH credits, the effective entry date must be one or two banking days following the processing date. |
| 15 | `ACH.BAT.IMMEDIATE.ORIGIN` | `AchBatch_ImmediateOrigin` | TField | Yes | 10 Positions and mandatory for all Files. ACH File header record. Identifies the sender of the file. This field contains the routing number of the ACH Operator or Sending Point that is Transmitting the File. The 10 characterfield begins with a blank in the first position, followed byt the four digit Federal Reserve Routing Symbol, the four digit ABA Institution Identifier, and the Check Digit. |
| 16 | `ACH.BAT.DEBIT.COUNT` | `AchBatch_DebitCount` | TField |  | Total number of debit entries in the batch. |
| 17 | `ACH.BAT.CREDIT.COUNT` | `AchBatch_CreditCount` | TField |  | Total number of credit entries in the batch. |
| 18 | `ACH.BAT.IAT.INDICATOR` | `AchBatch_IatIndicator` | TField | Conditional | 16 Positions - Company/Batch Header Record - Optional (IAT, Returns); 16 Positions - Company/Batch Header Record - Mandatory (COR entries related to IAT)For forward IAT Entries, this field is left blank. For Notifications of Change related to IAT Entries, this field must contain the value "IATCOR" |
| 19 | `ACH.BAT.IAT.FX.INDICATOR` | `AchBatch_IatFxIndicator` | TField | Yes | 2 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR)This field contains a code used to indicate the foreign exchange conversion methodology applied to an IAT Entry. Use may be dependent on the particular exchange services offered by a Gateway Operator. See NACHA Guidelines for valid code values for this field. |
| 20 | `ACH.BAT.IAT.FX.REF.INDIC` | `AchBatch_IatFxRefIndic` | TField |  | 1 Position - Company/Batch Header Record - Required (IAT, Returns, COR)This field contains a code used to indicate the content of the Foreign Exchange Reference Field. See NACHA Guidelines for valid code values for this field. |
| 21 | `ACH.BAT.IAT.FX.REF` | `AchBatch_IatFxRef` | TField |  | 15 Positions - Company/Batch Header Record - Required (IAT, Returns, COR)This field contains either the foreign exchange rate used to execute the foreign exchange conversion of an IAT Entry or another reference to the foreign exchange transaction. Content is defined by the Foreign Exchange Reference Indicator Field.If the Foreign Exchange Indicator Field contains "FF", this field will always be space filled. |
| 22 | `ACH.BAT.ISO.DEST.CO.CODE` | `AchBatch_IsoDestCoCode` |  |  |  |
| 23 | `ACH.BAT.ORIGINATOR.ID` | `AchBatch_OriginatorId` | TField | Yes | Originator Identification: 10 Positions - Company/Batch Header Record - Mandatory (IAT, IAT Returns, IAT COR)The Originator Identification is an alphameric code used to uniquely identify an Originator. This is the ID that is set up in the ACH.CORPORATE.INFO table. |
| 24 | `ACH.BAT.ISO.ORIG.CCY.CODE` | `AchBatch_IsoOrigCcyCode` | TField | Yes | 3 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR).This field contains the three-character code, as approved by the International Organization for Standardization (ISO), to identify the currency denomination in which the Entry was first originated. |
| 25 | `ACH.BAT.ISO.DEST.CCY.CODE` | `AchBatch_IsoDestCcyCode` | TField | Yes | 3 Positions - Company/Batch Header Record - Mandatory (IAT, Returns, COR)This field contains the three-character code, as approved by the International Organization for Standardization (ISO), to identify the currency denomination in which the Entry is to be received. |
| 26 | `ACH.BAT.LOAD.DATE` | `AchBatch_LoadDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 27 | `ACH.BAT.TR.REC.TYPE.CODE` | `AchBatch_TrRecTypeCode` | TField |  | ACH company/batch control record type code always equal to 5. |
| 28 | `ACH.BAT.TR.SVC.CLASS.CODE` | `AchBatch_TrSvcClassCode` | TField | Yes | 3 positions, mandatory for all batch control records. The Service Class Code (BAI Specifications) identifies the general classification of the dollar entries to be exchanged. ACH Entries are assigned Sercive Class Code series 200-299. Code values are: 200 ACH Entries Mixed Debits and Credits 220 ACH Credits Only 225 ACH Debits Only 280 ACH Automated Accounting Advices |
| 29 | `ACH.BAT.TR.ADDENDA.COUNT` | `AchBatch_TrAddendaCount` | TField |  | Total number of addenda records in this batch. |
| 30 | `ACH.BAT.TR.ENTRY.HASH` | `AchBatch_TrEntryHash` | TField | Yes | 10 Positions - Company/Batch Control Record and File Control Record - Mandatory (all files)The Receiving DFI Identification in each Entry Detail Record is hashed to provide a check against inadvertent alteration of data contents due to hardware failure or program error. (NOTE: Addenda Records are not hashed.) |
| 31 | `ACH.BAT.TR.TOT.DR.DLLR.AMT` | `AchBatch_TrTotDrDllrAmt` | TField |  | Total Debit Dollar Amount of entries in the batch. |
| 32 | `ACH.BAT.TR.TOT.CR.DLLR.AMT` | `AchBatch_TrTotCrDllrAmt` | TField |  | Total Credit Dollar Amount of entires in the batch. |
| 33 | `ACH.BAT.TR.COMPANY.ID` | `AchBatch_TrCompanyId` | TField |  | 10 Positions - Company/Batch Control Record - Required (all batches)The Company Identification is an alphameric code used to identify an Originator. The Company Identification Field must be included on all Entries. |
| 34 | `ACH.BAT.TR.MSG.AUTH.CODE` | `AchBatch_TrMsgAuthCode` | TField | No | Message Authentication Code (MAC): 19 Positions - Company/Batch Control Record - Optional (all batches)The MAC is an-eight character code derived from a special key used in conjunction with the DES algorithm. The MAC is used to validate the authenticity of ACH Entries. The DES algorithm and key message standards must be in accordance with standards adopted by the American National Standards Institute. The remaining eleven characters of this field are blank. |
| 35 | `ACH.BAT.TR.RESERVED` | `AchBatch_TrReserved` | TField |  | Reserved field. |
| 36 | `ACH.BAT.TR.ORIG.DFI.ID` | `AchBatch_TrOrigDfiId` | TField |  | Company/Batch Control Record - 10 Positions. The Originator Identification is an alphameric code used to uniquely identify an Originator. |
| 37 | `ACH.BAT.TR.BATCH.NUMBER` | `AchBatch_TrBatchNumber` | TField | Yes | 7 Postions and mandatory for all Company/Batch Control record. The ODFI or its Sending Point assigns this number in ascending sequence to each batch in a File of Entries. |
| 38 | `ACH.BAT.STATUS` | `AchBatch_Status` | TField |  | Status of the batch. Valid values are ACK, Cancelled, Cleared, Data Error, Delivered, Exception, Loaded,Limit Breached, Nack, Pending, Prefunded, Processed, Rejected, Returned, ReversalInitiated, ReversalCompleted, Validated, Validation Error, or Voided. |
| 39 | `ACH.BAT.FILE.TYPE` | `AchBatch_FileType` | TField |  | File type valid values are, None, Inward, or Outward. |
| 40 | `ACH.BAT.FILE.SOURCE` | `AchBatch_FileSource` | TField |  | File source valid values are, None, Corporate, or Fed. |
| 41 | `ACH.BAT.REVERSAL.INDICATOR` | `AchBatch_ReversalIndicator` | TField |  | Future use |
| 42 | `ACH.BAT.SETTLEMENT.DATE` | `AchBatch_SettlementDate` | TField |  | 3 Positions. Inserted by Receiving ACH Operator (all batches). The Settlement Date (a 3-digit Julian date) for a batch of Entries is inserted by the Receiving ACH Operator. This is the date on which the Particiating DFI or its correspondent is scheduled to be debited or credited by the Federal Reserve. See the NACHA Guidelines for specific requirements. |
| 43 | `ACH.BAT.SETTLE.DR.AC` | `AchBatch_SettleDrAc` | TField |  | Debit Account in which the ACH funds are settled. |
| 44 | `ACH.BAT.SETTLE.CR.AC` | `AchBatch_SettleCrAc` | TField |  | Credit Account in which the ACH funds are settled. |
| 45 | `ACH.BAT.SETTLEMENT.TXN.REF` | `AchBatch_SettlementTxnRef` |  |  |  |
| 46 | `ACH.BAT.SETTLEMENT.COMPANY` | `AchBatch_SettlementCompany` | TField |  | Company defined in the ACH.CLEARING.PARAMETER in the Routing Company.1 field. |
| 47 | `ACH.BAT.RESERVED.17` | `AchBatch_Reserved17` | TField |  | Reserved field. |
| 48 | `ACH.BAT.RESERVED.16` | `AchBatch_Reserved16` | TField |  | Reserved field. |
| 49 | `ACH.BAT.FIN.ENTRY.COUNT` | `AchBatch_FinEntryCount` | TField |  | Number of Financial Entries in the Batch. |
| 50 | `ACH.BAT.NONFIN.ENTRY.COUNT` | `AchBatch_NonfinEntryCount` | TField |  | Number of Non-Financial Entires in the Batch. |
| 51 | `ACH.BAT.PRE.FUNDING` | `AchBatch_PreFunding` | TField |  | Future use |
| 52 | `ACH.BAT.ACH.FILE.ID` | `AchBatch_AchFileId` | TField |  | ID of the ACH file. |
| 53 | `ACH.BAT.TAPE.REF` | `AchBatch_TapeRef` | TField |  | Name of the file. |
| 54 | `ACH.BAT.AML.RESPONSE` | `AchBatch_AmlResponse` | TField |  | Response from AML system. Valid values are Null, 0, 1, Clean, or Hit. |
| 55 | `ACH.BAT.AML.REJ.REASON` | `AchBatch_AmlRejReason` | TField |  | Reason from the AML system that the batch was rejected. |
| 56 | `ACH.BAT.AML.VERIFICATION` | `AchBatch_AmlVerification` | TField |  | Field that determines if AML verification is used for this file |
| 57 | `ACH.BAT.AML.LEVELS` | `AchBatch_AmlLevels` | TField |  | Level set in ACH.AML.PARAMETER. Values are Null, 0, 1, or 2. |
| 58 | `ACH.BAT.AML.RESERVED.3` | `AchBatch_AmlReserved3` | TField |  | Reserved field. |
| 59 | `ACH.BAT.AML.RESERVED.2` | `AchBatch_AmlReserved2` | TField |  | Reserved field. |
| 60 | `ACH.BAT.AML.RESERVED.1` | `AchBatch_AmlReserved1` | TField |  | Reserved field. |
| 61 | `ACH.BAT.BATCH.XREF` | `AchBatch_BatchXref` | TField |  | Future use |
| 62 | `ACH.BAT.BATCH.RECORD` | `AchBatch_BatchRecord` | TField |  | System Populated field. This field stores entire batch header record for an outward file |
| 63 | `ACH.BAT.BATCH.TR.RECORD` | `AchBatch_BatchTrRecord` | TField |  | System Populated field. This field stores entire batch control record for an outward file |
| 64 | `ACH.BAT.RETURN.BATCH` | `AchBatch_ReturnBatch` | TField |  | Whether or not this is a return batch. Valid values are None, No, or Yes. |
| 65 | `ACH.BAT.REMARKS` | `AchBatch_Remarks` |  |  |  |
| 66 | `ACH.BAT.LAST.UPDATE.DATE` | `AchBatch_LastUpdateDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 67 | `ACH.BAT.ACH.OP.DATA` | `AchBatch_AchOpData` | TField |  |  |
| 68 | `ACH.BAT.SAME.DAY` | `AchBatch_SameDay` | TField |  | This field will be flagged with the value 'Y' by the ACH.UPLOAD.WAHREHOUSE and ACH.CAPTURE.UPDATE.WAREHOUSE service if the batch is a same day batch. |
| 69 | `ACH.BAT.DECISION.REASON` | `AchBatch_DecisionReason` | TField |  | This user will be able to capture the reason/information for the decision taken on the batch that had breached the limit. The decision can be either to process the batch if the status is 'loaded' or void the batch if the status is 'voided'. |
| 70 | `ACH.BAT.PROCESSING.DATE` | `AchBatch_ProcessingDate` | TField |  |  |
| 71 | `ACH.BAT.PREFUND.CODEWORD` | `AchBatch_PrefundCodeword` | TField |  |  |
| 72 | `ACH.BAT.OFFSET.DEFAULT` | `AchBatch_OffsetDefault` | TField |  | This field will be set to N if the ACH.CAPTURE record is input through one of the versions which are used to originate a same day DEBIT transaction. |
| 73 | `ACH.BAT.RESERVED.3` | `AchBatch_Reserved3` | TField |  | Reserved field. |
| 74 | `ACH.BAT.RESERVED.2` | `AchBatch_Reserved2` | TField |  | Reserved field. |
| 75 | `ACH.BAT.RESERVED.1` | `AchBatch_Reserved1` | TField |  | Reserved field. |
| 76 | `ACH.BAT.LOCAL.REF` | `AchBatch_LocalRef` |  |  |  |
| 77 | `ACH.BAT.OVERRIDE` | `AchBatch_Override` |  |  |  |
| 78 | `ACH.BAT.RECORD.STATUS` | `AchBatch_RecordStatus` | String |  |  |
| 79 | `ACH.BAT.CURR.NO` | `AchBatch_CurrNo` | String |  |  |
| 80 | `ACH.BAT.INPUTTER` | `AchBatch_Inputter` |  |  |  |
| 81 | `ACH.BAT.DATE.TIME` | `AchBatch_DateTime` |  |  |  |
| 82 | `ACH.BAT.AUTHORISER` | `AchBatch_Authoriser` | String |  |  |
| 83 | `ACH.BAT.CO.CODE` | `AchBatch_CoCode` | String |  |  |
| 84 | `ACH.BAT.DEPT.CODE` | `AchBatch_DeptCode` | String |  |  |
| 85 | `ACH.BAT.AUDITOR.CODE` | `AchBatch_AuditorCode` | String |  |  |
| 86 | `ACH.BAT.AUDIT.DATE.TIME` | `AchBatch_AuditDateTime` | String |  |  |
