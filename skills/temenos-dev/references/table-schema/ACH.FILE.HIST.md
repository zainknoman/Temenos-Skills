# ACH.FILE.HIST — Table Schema

> Source: `INSERTS/I_F.ACH.FILE.HIST` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHFILE.HIST.REC.TYPE.CODE` | `AchFileHist_RecTypeCode` | TField |  | ACH File header record type code always equal to 1. |
| 2 | `ACHFILE.HIST.PRIORITY.CODE` | `AchFileHist_PriorityCode` | TField |  | ACH File header record priority code must contain a value of 01. |
| 3 | `ACHFILE.HIST.IMMD.DESTINATION` | `AchFileHist_ImmdDestination` | TField |  | ACH File header record. Identifies the party to which the file is being delivered. |
| 4 | `ACHFILE.HIST.IMMD.ORIGIN` | `AchFileHist_ImmdOrigin` | TField | Yes | 10 Positions and mandatory for all Files. ACH File header record. Identifies the sender of the file. This field contains the routing number of the ACH Operator or Sending Point that is Transmitting the File. The 10 characterfield begins with a blank in the first position, followed byt the four digit Federal Reserve Routing Symbol, the four digit ABA Institution Identifier, and the Check Digit. |
| 5 | `ACHFILE.HIST.FILE.CREATION.DATE` | `AchFileHist_FileCreationDate` | TField |  | ACH File header record. Date on which the file was created. |
| 6 | `ACHFILE.HIST.FILE.CREATION.TIME` | `AchFileHist_FileCreationTime` | TField |  | ACH File header record. Time in hours and minutes that the file creation or exchange took place. |
| 7 | `ACHFILE.HIST.FILE.ID.MODIFIER` | `AchFileHist_FileIdModifier` | TField |  | ACH File header record. Unique 1 Alphanumeric code, upper case A-Z and numeric 0-9 accepted. The File ID Modifier, coupled with the File Creation Date and Time, can be used by the ODFI, along with other information, to trace the file. |
| 8 | `ACHFILE.HIST.RECORD.SIZE` | `AchFileHist_RecordSize` | TField |  | ACH File header record. The Record Size indicates the number of characters in each record. The value "094" must be used. |
| 9 | `ACHFILE.HIST.BLOCKING.FACTOR` | `AchFileHist_BlockingFactor` | TField | Yes | ACH file header record, mandatory for all files. The Blocking Factor defines the number of Records within a block (a block is 940 characters). For all files moving between a DFI and an ACH Operator (either way), the value "10" must be used. If the number of Records within the File is not a multiple of ten, the remainder of the block must be filled with "9's". |
| 10 | `ACHFILE.HIST.FORMAT.CODE` | `AchFileHist_FormatCode` | TField | Yes | ACH file header record, mandatory for all files. This field must contain a value of "1". |
| 11 | `ACHFILE.HIST.IMMD.DEST.NAME` | `AchFileHist_ImmdDestName` | TField | No | ACH file header record, optional for all files. This field contains the name of the ACH Operator or Receiving Point for which the File is destined. |
| 12 | `ACHFILE.HIST.IMMD.ORIGIN.NAME` | `AchFileHist_ImmdOriginName` | TField | No | ACH file header record, optional for all files. This field contains the name of the ACH Operator or Sending Point that is Transmitting the file. |
| 13 | `ACHFILE.HIST.REFERENCE.CODE` | `AchFileHist_ReferenceCode` | TField | No | ACH File Header Record, optional for all files. The field is reserved for information pertinent to the Originator. For the ADV this field must contain "ADV FILE". |
| 14 | `ACHFILE.HIST.VALUE.DATE` | `AchFileHist_ValueDate` | TField |  | ACH Effective Entry Date. The date specified by the originator on which it intends a batch of entries to be settled. For ACH credits, the effective entry date must be one or two banking days following the processing date. |
| 15 | `ACHFILE.HIST.DEBIT.COUNT` | `AchFileHist_DebitCount` | TField |  | Total count of all the debits in the file. |
| 16 | `ACHFILE.HIST.CREDIT.COUNT` | `AchFileHist_CreditCount` | TField |  | Total count of all the credits in the file. |
| 17 | `ACHFILE.HIST.LINES.PROCESSED` | `AchFileHist_LinesProcessed` | TField |  | System populated field. This field is used to store the number of lines processed during file loading. |
| 18 | `ACHFILE.HIST.STATUS` | `AchFileHist_Status` | TField |  | Status of the file. Options are ACK, CANCELLED, CLEARED, DATA.ERROR, DEATH.NOTIFICATION, DELIVERED, EXCEPTION, LOADED, LOAD.ERROR, LOADING, NACK, PENDING, REJECTED, RETURNED, VALIDATED, VALIDATION.ERROR, and VOIDED. |
| 19 | `ACHFILE.HIST.TR.REC.TYPE.CODE` | `AchFileHist_TrRecTypeCode` | TField |  | File Control Record Type Code always "9". |
| 20 | `ACHFILE.HIST.TR.BATCH.COUNT` | `AchFileHist_TrBatchCount` | TField |  | The value of the Batch Count field is equal to the number of Company/Batch Header Records in the file. |
| 21 | `ACHFILE.HIST.TR.BLOCK.COUNT` | `AchFileHist_TrBlockCount` | TField | Yes | ACH File Control Record, mandatory for all files. The Block Count contains the number of blocks (a block is 940 characters) in the File, including both the File Header and File Control Records. |
| 22 | `ACHFILE.HIST.TR.ADDENDA.COUNT` | `AchFileHist_TrAddendaCount` | TField | Yes | ACH File Control Record, mandatory for all files. The Entry/Addenda Count Field is a tally of each Entry Detail and Addenda Record processed within either the batch or File, as appropriate. |
| 23 | `ACHFILE.HIST.TR.ENTRY.HASH` | `AchFileHist_TrEntryHash` | TField |  | The Entry Hash is the sum of the Entry Hash fields contained within the Company/Batch Control Records of the File. If the sum exceeds 10 characters, the field must be populated with the rightmost 10 characters. |
| 24 | `ACHFILE.HIST.TR.TOT.DR.DLLR.AMT` | `AchFileHist_TrTotDrDllrAmt` | TField |  | The Total Debit Dollar Amount field contain accumulated Entry Detail debit totals within the file. |
| 25 | `ACHFILE.HIST.TR.TOT.CR.DLLR.AMT` | `AchFileHist_TrTotCrDllrAmt` | TField |  | The Total Credit Dollar Amount field contain accumulated Entry Detail credit totals within the file. |
| 26 | `ACHFILE.HIST.TR.RESERVED` | `AchFileHist_TrReserved` | TField |  | Reserved field |
| 27 | `ACHFILE.HIST.REMARKS` | `AchFileHist_Remarks` |  |  |  |
| 28 | `ACHFILE.HIST.LOAD.DATE` | `AchFileHist_LoadDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 29 | `ACHFILE.HIST.FILE.TYPE` | `AchFileHist_FileType` | TField |  | Valid types are None, Inward, or Outward. |
| 30 | `ACHFILE.HIST.FILE.SOURCE` | `AchFileHist_FileSource` | TField |  | Valid types are None, Corporate, or Fed. |
| 31 | `ACHFILE.HIST.SETTLEMENT.ACCT` | `AchFileHist_SettlementAcct` | TField |  | Account in which the ACH funds are settled. |
| 32 | `ACHFILE.HIST.SETTLEMENT.DATE` | `AchFileHist_SettlementDate` |  |  |  |
| 33 | `ACHFILE.HIST.SETTLE.DR.AMOUNT` | `AchFileHist_SettleDrAmount` |  |  |  |
| 34 | `ACHFILE.HIST.SETTLE.CR.AMOUNT` | `AchFileHist_SettleCrAmount` |  |  |  |
| 35 | `ACHFILE.HIST.RETURN.DR.AMOUNT` | `AchFileHist_ReturnDrAmount` |  |  |  |
| 36 | `ACHFILE.HIST.RETURN.CR.AMOUNT` | `AchFileHist_ReturnCrAmount` |  |  |  |
| 37 | `ACHFILE.HIST.SETTLEMENT.TXN.REF` | `AchFileHist_SettlementTxnRef` |  |  |  |
| 38 | `ACHFILE.HIST.SETTLEMENT.COMPANY` | `AchFileHist_SettlementCompany` |  |  |  |
| 39 | `ACHFILE.HIST.SETTLEMENT.TXN.STATUS` | `AchFileHist_SettlementTxnStatus` |  |  |  |
| 40 | `ACHFILE.HIST.RESERVED.16` | `AchFileHist_Reserved16` |  |  |  |
| 41 | `ACHFILE.HIST.ACH.BATCH` | `AchFileHist_AchBatch` |  |  |  |
| 42 | `ACHFILE.HIST.ARC.BATCH.COUNT` | `AchFileHist_ArcBatchCount` | TField |  | Number of batches in the file. |
| 43 | `ACHFILE.HIST.TAPE.REF` | `AchFileHist_TapeRef` | TField |  | Name of the file. |
| 44 | `ACHFILE.HIST.FILE.RECORD` | `AchFileHist_FileRecord` | TField |  | System Populated field. This field stores entire File header record for an outward file |
| 45 | `ACHFILE.HIST.FILE.TR.RECORD` | `AchFileHist_FileTrRecord` | TField |  | System Populated field. This field stores entire File control record for an outward file |
| 46 | `ACHFILE.HIST.LAST.UPDATE.DATE` | `AchFileHist_LastUpdateDate` | TField |  | Date file was loaded. |
| 47 | `ACHFILE.HIST.INTERNAL.BATCH.CNT` | `AchFileHist_InternalBatchCnt` | TField |  | Number of batches in the file. |
| 48 | `ACHFILE.HIST.SAME.DAY` | `AchFileHist_SameDay` | TField |  | This field will be flagged with the value Y by the ACH.UPLOAD.WAHREHOUSE service if any of the batches in the file is a same day batch. |
| 49 | `ACHFILE.HIST.RESERVED.10` | `AchFileHist_Reserved10` | TField |  | Reserved field |
| 50 | `ACHFILE.HIST.RESERVED.9` | `AchFileHist_Reserved9` | TField |  | Reserved field |
| 51 | `ACHFILE.HIST.RESERVED.8` | `AchFileHist_Reserved8` | TField |  | Reserved field |
| 52 | `ACHFILE.HIST.RESERVED.7` | `AchFileHist_Reserved7` | TField |  | Reserved field |
| 53 | `ACHFILE.HIST.RESERVED.6` | `AchFileHist_Reserved6` | TField |  | Reserved field |
| 54 | `ACHFILE.HIST.RESERVED.5` | `AchFileHist_Reserved5` | TField |  | Reserved field |
| 55 | `ACHFILE.HIST.RESERVED.4` | `AchFileHist_Reserved4` | TField |  | Reserved field |
| 56 | `ACHFILE.HIST.RESERVED.3` | `AchFileHist_Reserved3` | TField |  | Reserved field |
| 57 | `ACHFILE.HIST.RESERVED.2` | `AchFileHist_Reserved2` | TField |  | Reserved field |
| 58 | `ACHFILE.HIST.RESERVED.1` | `AchFileHist_Reserved1` | TField |  | Reserved field |
| 59 | `ACHFILE.HIST.LOCAL.REF` | `AchFileHist_LocalRef` |  |  |  |
| 60 | `ACHFILE.HIST.OVERRIDE` | `AchFileHist_Override` |  |  |  |
