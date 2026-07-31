# ACH.FILE — Table Schema

> Source: `INSERTS/I_F.ACH.FILE` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.FIL.REC.TYPE.CODE` | `AchFile_RecTypeCode` | TField |  | ACH File header record type code always equal to 1. |
| 2 | `ACH.FIL.PRIORITY.CODE` | `AchFile_PriorityCode` | TField |  | ACH File header record priority code must contain a value of 01. |
| 3 | `ACH.FIL.IMMD.DESTINATION` | `AchFile_ImmdDestination` | TField |  | ACH File header record. Identifies the party to which the file is being delivered. |
| 4 | `ACH.FIL.IMMD.ORIGIN` | `AchFile_ImmdOrigin` | TField | Yes | 10 Positions and mandatory for all Files. ACH File header record. Identifies the sender of the file. This field contains the routing number of the ACH Operator or Sending Point that is Transmitting the File. The 10 characterfield begins with a blank in the first position, followed byt the four digit Federal Reserve Routing Symbol, the four digit ABA Institution Identifier, and the Check Digit. |
| 5 | `ACH.FIL.FILE.CREATION.DATE` | `AchFile_FileCreationDate` | TField |  | ACH File header record. Date on which the file was created. |
| 6 | `ACH.FIL.FILE.CREATION.TIME` | `AchFile_FileCreationTime` | TField |  | ACH File header record. Time in hours and minutes that the file creation or exchange took place. |
| 7 | `ACH.FIL.FILE.ID.MODIFIER` | `AchFile_FileIdModifier` | TField |  | ACH File header record. Unique 1 Alphanumeric code, upper case A-Z and numeric 0-9 accepted. The File ID Modifier, coupled with the File Creation Date and Time, can be used by the ODFI, along with other information, to trace the file. |
| 8 | `ACH.FIL.RECORD.SIZE` | `AchFile_RecordSize` | TField |  | ACH File header record. The Record Size indicates the number of characters in each record. The value "094" must be used. |
| 9 | `ACH.FIL.BLOCKING.FACTOR` | `AchFile_BlockingFactor` | TField | Yes | ACH file header record, mandatory for all files. The Blocking Factor defines the number of Records within a block (a block is 940 characters). For all files moving between a DFI and an ACH Operator (either way), the value "10" must be used. If the number of Records within the File is not a multiple of ten, the remainder of the block must be filled with "9's". |
| 10 | `ACH.FIL.FORMAT.CODE` | `AchFile_FormatCode` | TField | Yes | ACH file header record, mandatory for all files. This field must contain a value of "1". |
| 11 | `ACH.FIL.IMMD.DEST.NAME` | `AchFile_ImmdDestName` | TField | No | ACH file header record, optional for all files. This field contains the name of the ACH Operator or Receiving Point for which the File is destined. |
| 12 | `ACH.FIL.IMMD.ORIGIN.NAME` | `AchFile_ImmdOriginName` | TField | No | ACH file header record, optional for all files. This field contains the name of the ACH Operator or Sending Point that is Transmitting the file. |
| 13 | `ACH.FIL.REFERENCE.CODE` | `AchFile_ReferenceCode` | TField | No | ACH File Header Record, optional for all files. The field is reserved for information pertinent to the Originator. For the ADV this field must contain "ADV FILE". |
| 14 | `ACH.FIL.VALUE.DATE` | `AchFile_ValueDate` | TField |  | ACH Effective Entry Date. The date specified by the originator on which it intends a batch of entries to be settled. For ACH credits, the effective entry date must be one or two banking days following the processing date. |
| 15 | `ACH.FIL.DEBIT.COUNT` | `AchFile_DebitCount` | TField |  | Total count of all the debits in the file. |
| 16 | `ACH.FIL.CREDIT.COUNT` | `AchFile_CreditCount` | TField |  | Total count of all the credits in the file. |
| 17 | `ACH.FIL.LINES.PROCESSED` | `AchFile_LinesProcessed` | TField |  | System populated field. This field is used to store the number of lines processed during file loading. |
| 18 | `ACH.FIL.STATUS` | `AchFile_Status` | TField |  | Status of the file. Options are ACK, CANCELLED, CLEARED, DATA.ERROR, DEATH.NOTIFICATION, DELIVERED, EXCEPTION, LOADED, LOAD.ERROR, LOADING, NACK, PENDING, REJECTED, RETURNED, ReversalCompleted, VALIDATED, VALIDATION.ERROR, and VOIDED. |
| 19 | `ACH.FIL.TR.REC.TYPE.CODE` | `AchFile_TrRecTypeCode` | TField |  | File Control Record Type Code always "9". |
| 20 | `ACH.FIL.TR.BATCH.COUNT` | `AchFile_TrBatchCount` | TField |  | The value of the Batch Count field is equal to the number of Company/Batch Header Records in the file. |
| 21 | `ACH.FIL.TR.BLOCK.COUNT` | `AchFile_TrBlockCount` | TField | Yes | ACH File Control Record, mandatory for all files. The Block Count contains the number of blocks (a block is 940 characters) in the File, including both the File Header and File Control Records. |
| 22 | `ACH.FIL.TR.ADDENDA.COUNT` | `AchFile_TrAddendaCount` | TField | Yes | ACH File Control Record, mandatory for all files. The Entry/Addenda Count Field is a tally of each Entry Detail and Addenda Record processed within either the batch or File, as appropriate. |
| 23 | `ACH.FIL.TR.ENTRY.HASH` | `AchFile_TrEntryHash` | TField |  | The Entry Hash is the sum of the Entry Hash fields contained within the Company/Batch Control Records of the File. If the sum exceeds 10 characters, the field must be populated with the rightmost 10 characters. |
| 24 | `ACH.FIL.TR.TOT.DR.DLLR.AMT` | `AchFile_TrTotDrDllrAmt` | TField |  | The Total Debit Dollar Amount field contain accumulated Entry Detail debit totals within the file. |
| 25 | `ACH.FIL.TR.TOT.CR.DLLR.AMT` | `AchFile_TrTotCrDllrAmt` | TField |  | The Total Credit Dollar Amount field contain accumulated Entry Detail credit totals within the file. |
| 26 | `ACH.FIL.TR.RESERVED` | `AchFile_TrReserved` | TField |  | Reserved field |
| 27 | `ACH.FIL.REMARKS` | `AchFile_Remarks` |  |  |  |
| 28 | `ACH.FIL.LOAD.DATE` | `AchFile_LoadDate` | TField |  | Date the file was loaded into the ACH Warehouse. |
| 29 | `ACH.FIL.FILE.TYPE` | `AchFile_FileType` | TField |  | Valid types are None, Inward, or Outward. |
| 30 | `ACH.FIL.FILE.SOURCE` | `AchFile_FileSource` | TField |  | Valid types are None, Corporate, or Fed. |
| 31 | `ACH.FIL.SETTLEMENT.ACCT` | `AchFile_SettlementAcct` | TField |  | Account in which the ACH funds are settled. |
| 32 | `ACH.FIL.SETTLEMENT.DATE` | `AchFile_SettlementDate` |  |  |  |
| 33 | `ACH.FIL.SETTLE.DR.AMOUNT` | `AchFile_SettleDrAmount` |  |  |  |
| 34 | `ACH.FIL.SETTLE.CR.AMOUNT` | `AchFile_SettleCrAmount` |  |  |  |
| 35 | `ACH.FIL.RETURN.DR.AMOUNT` | `AchFile_ReturnDrAmount` |  |  |  |
| 36 | `ACH.FIL.RETURN.CR.AMOUNT` | `AchFile_ReturnCrAmount` |  |  |  |
| 37 | `ACH.FIL.SETTLEMENT.TXN.REF` | `AchFile_SettlementTxnRef` |  |  |  |
| 38 | `ACH.FIL.SETTLEMENT.COMPANY` | `AchFile_SettlementCompany` |  |  |  |
| 39 | `ACH.FIL.SETTLEMENT.TXN.STATUS` | `AchFile_SettlementTxnStatus` |  |  |  |
| 40 | `ACH.FIL.RESERVED.16` | `AchFile_Reserved16` |  |  |  |
| 41 | `ACH.FIL.ACH.BATCH` | `AchFile_AchBatch` |  |  |  |
| 42 | `ACH.FIL.ARC.BATCH.COUNT` | `AchFile_ArcBatchCount` | TField |  | Number of batches in the file. |
| 43 | `ACH.FIL.TAPE.REF` | `AchFile_TapeRef` | TField |  | Name of the file. |
| 44 | `ACH.FIL.FILE.RECORD` | `AchFile_FileRecord` | TField |  | System Populated field. This field stores entire File header record for an outward file |
| 45 | `ACH.FIL.FILE.TR.RECORD` | `AchFile_FileTrRecord` | TField |  | System Populated field. This field stores entire File control record for an outward file |
| 46 | `ACH.FIL.LAST.UPDATE.DATE` | `AchFile_LastUpdateDate` | TField |  | Date file was loaded. |
| 47 | `ACH.FIL.INTERNAL.BATCH.CNT` | `AchFile_InternalBatchCnt` | TField |  | Number of batches in the file. |
| 48 | `ACH.FIL.SAME.DAY` | `AchFile_SameDay` | TField |  | This field will be flagged with the value Y by the ACH.UPLOAD.WAHREHOUSE service if any of the batches in the file is a same day batch. |
| 49 | `ACH.FIL.RESERVED.10` | `AchFile_Reserved10` | TField |  | Reserved field |
| 50 | `ACH.FIL.RESERVED.9` | `AchFile_Reserved9` | TField |  | Reserved field |
| 51 | `ACH.FIL.RESERVED.8` | `AchFile_Reserved8` | TField |  | Reserved field |
| 52 | `ACH.FIL.RESERVED.7` | `AchFile_Reserved7` | TField |  | Reserved field |
| 53 | `ACH.FIL.RESERVED.6` | `AchFile_Reserved6` | TField |  | Reserved field |
| 54 | `ACH.FIL.RESERVED.5` | `AchFile_Reserved5` | TField |  | Reserved field |
| 55 | `ACH.FIL.RESERVED.4` | `AchFile_Reserved4` | TField |  | Reserved field |
| 56 | `ACH.FIL.RESERVED.3` | `AchFile_Reserved3` | TField |  | Reserved field |
| 57 | `ACH.FIL.RESERVED.2` | `AchFile_Reserved2` | TField |  | Reserved field |
| 58 | `ACH.FIL.RESERVED.1` | `AchFile_Reserved1` | TField |  | Reserved field |
| 59 | `ACH.FIL.LOCAL.REF` | `AchFile_LocalRef` |  |  |  |
| 60 | `ACH.FIL.OVERRIDE` | `AchFile_Override` |  |  |  |
| 61 | `ACH.FIL.RECORD.STATUS` | `AchFile_RecordStatus` | String |  |  |
| 62 | `ACH.FIL.CURR.NO` | `AchFile_CurrNo` | String |  |  |
| 63 | `ACH.FIL.INPUTTER` | `AchFile_Inputter` |  |  |  |
| 64 | `ACH.FIL.DATE.TIME` | `AchFile_DateTime` |  |  |  |
| 65 | `ACH.FIL.AUTHORISER` | `AchFile_Authoriser` | String |  |  |
| 66 | `ACH.FIL.CO.CODE` | `AchFile_CoCode` | String |  |  |
| 67 | `ACH.FIL.DEPT.CODE` | `AchFile_DeptCode` | String |  |  |
| 68 | `ACH.FIL.AUDITOR.CODE` | `AchFile_AuditorCode` | String |  |  |
| 69 | `ACH.FIL.AUDIT.DATE.TIME` | `AchFile_AuditDateTime` | String |  |  |
