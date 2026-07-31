# SEPA.OUTWARD.FILES — Table Schema

> Source: `INSERTS/I_F.SEPA.OUTWARD.FILES` in `EP_OutwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.OCF.FILE.NAME` | `SepaOutwardFiles_FileName` | TField |  | This field contains the Name of the file generated on library. Validation Rules Value upto 50 type ANY(Any Character) |
| 2 | `SEP.OCF.PEACH.ID` | `SepaOutwardFiles_PeachId` | TField |  | This field Issues the PE-ACH platform center Validation Rules Value upto 10 type ANY(Any Character) Value should exist in SEPA.PEACH Application |
| 3 | `SEP.OCF.CUSTOMER.ID` | `SepaOutwardFiles_CustomerId` | TField |  | This field specifies the ID of the Handing over customer Validation Rules Value upto 10 type ANY(Any Character) Value should exist in CUSTOMER Application |
| 4 | `SEP.OCF.PROCESS.DATE` | `SepaOutwardFiles_ProcessDate` | D (DATE) |  | This field specifies the Treatment date of the outward file. Validation Rules Value upto 11 type D(DATE) |
| 5 | `SEP.OCF.PROCESS.TIME` | `SepaOutwardFiles_ProcessTime` | TField |  | This field specifies the Treatment time of the outward file. Validation Rules Value upto 8 type TIME( Time Format) |
| 6 | `SEP.OCF.CREATION.DATE` | `SepaOutwardFiles_CreationDate` | D (DATE) |  | This field specifies the Creation date of the outward file. Validation Rules Value upto 11 type D(DATE) |
| 7 | `SEP.OCF.CREATION.TIME` | `SepaOutwardFiles_CreationTime` | TField |  | This field specifies the Creation time of the outward file. Validation Rules Value upto 8 type TIME( Time Format) |
| 8 | `SEP.OCF.FILE.HEADER` | `SepaOutwardFiles_FileHeader` | A (Alphanumeric) |  | This Field specifies the File header sequence stored in such a way that it can be shown easily as it was in its original XML presentation by a delivered T24 drill down enquiry. Validation Rules Value upto 255 type A(Alphanumeric) |
| 9 | `SEP.OCF.MESSAGE.ID` | `SepaOutwardFiles_MessageId` |  |  |  |
| 10 | `SEP.OCF.MESSAGE.TYPE` | `SepaOutwardFiles_MessageType` |  |  |  |
| 11 | `SEP.OCF.GROUP.HEADER` | `SepaOutwardFiles_GroupHeader` |  |  |  |
| 12 | `SEP.OCF.ORIGINAL.GROUP` | `SepaOutwardFiles_OriginalGroup` |  |  |  |
| 13 | `SEP.OCF.TRANS.CODE` | `SepaOutwardFiles_TransCode` |  |  |  |
| 14 | `SEP.OCF.TRANS.FIRST` | `SepaOutwardFiles_TransFirst` |  |  |  |
| 15 | `SEP.OCF.TRANS.LAST` | `SepaOutwardFiles_TransLast` |  |  |  |
| 16 | `SEP.OCF.TRANS.NUMBER` | `SepaOutwardFiles_TransNumber` |  |  |  |
| 17 | `SEP.OCF.TOT.AMOUNT` | `SepaOutwardFiles_TotAmount` |  |  |  |
| 18 | `SEP.OCF.STMT.NOS` | `SepaOutwardFiles_StmtNos` |  |  |  |
| 19 | `SEP.OCF.BULK.REJECT.CODE` | `SepaOutwardFiles_BulkRejectCode` |  |  |  |
| 20 | `SEP.OCF.BULK.REJECT.RSN` | `SepaOutwardFiles_BulkRejectRsn` |  |  |  |
| 21 | `SEP.OCF.COMMENT` | `SepaOutwardFiles_Comment` |  |  |  |
| 22 | `SEP.OCF.FILE.TRAILER` | `SepaOutwardFiles_FileTrailer` | A (Alphanumeric) |  | This field specifies the Last Tag of the file �&lt;/SEPA.HEADER.ID&gt;� Validation Rules Value upto 35 type A(Alphanumeric) |
| 23 | `SEP.OCF.STATUS` | `SepaOutwardFiles_Status` | TField |  | This field holds the Status of the transaction posted. ACP - Accepted CXL � Cancelled PND � Pending PRC � Processed RCV � Received RDY � Ready for transfer REJ � Rejected RET � Returned SND � Sent TRF - Transferred Validation Rules Value upto 3 type SEPA.TRANSFER.STS.LIST |
| 24 | `SEP.OCF.FILE.REJECT.CODE` | `SepaOutwardFiles_FileRejectCode` | A (Alphanumeric) |  | This field Specifies the reason code for file level rejection Must be valid code in SEPA.REASONS Validation Rules Value upto 4 type A(Alphanumeric) Value should exist in SEPA.REASONS |
| 25 | `SEP.OCF.PRE.HEADER` | `SepaOutwardFiles_PreHeader` |  |  |  |
| 26 | `SEP.OCF.ON.US.TRANS` | `SepaOutwardFiles_OnUsTrans` | A (Alphanumeric) |  | If this field is set to Y, then corresponding PACS message status will be updated accordingly for InHouse Transactions Validation rule Value upto 1 type A (Alphanumeric) and Value allowed 'Y' or null |
| 27 | `SEP.OCF.RESERVED.9` | `SepaOutwardFiles_Reserved9` | TField |  |  |
| 28 | `SEP.OCF.RESERVED.8` | `SepaOutwardFiles_Reserved8` | TField |  |  |
| 29 | `SEP.OCF.RESERVED.7` | `SepaOutwardFiles_Reserved7` | TField |  |  |
| 30 | `SEP.OCF.RESERVED.6` | `SepaOutwardFiles_Reserved6` | TField |  |  |
| 31 | `SEP.OCF.RESERVED.5` | `SepaOutwardFiles_Reserved5` | TField |  |  |
| 32 | `SEP.OCF.RESERVED.4` | `SepaOutwardFiles_Reserved4` | TField |  |  |
| 33 | `SEP.OCF.RESERVED.3` | `SepaOutwardFiles_Reserved3` | TField |  |  |
| 34 | `SEP.OCF.RESERVED.2` | `SepaOutwardFiles_Reserved2` | TField |  |  |
| 35 | `SEP.OCF.RESERVED.1` | `SepaOutwardFiles_Reserved1` | TField |  |  |
| 36 | `SEP.OCF.LOCAL.REF` | `SepaOutwardFiles_LocalRef` |  |  |  |
