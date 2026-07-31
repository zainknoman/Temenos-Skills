# SEPA.INWARD.FILES — Table Schema

> Source: `INSERTS/I_F.SEPA.INWARD.FILES` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.ICF.FILE.NAME` | `SepaInwardFiles_FileName` | TField |  | This Field contains the Name of the file received in library. Validation Rules Value upto 50 type ANY(Any Character) |
| 2 | `SEP.ICF.PEACH.ID` | `SepaInwardFiles_PeachId` | TField |  | This field denotes the Issuing PE-ACH platform center Validation Rules Value upto 10 type ANY(Any Character) Value should exist in SEPA.PEACH Application |
| 3 | `SEP.ICF.CUSTOMER.ID` | `SepaInwardFiles_CustomerId` | TField |  | This field contains the ID of the Handing over customer Validation Rules Value upto 10 type ANY(Any Character) Value should exist in CUSTOMER Application |
| 4 | `SEP.ICF.PROCESS.DATE` | `SepaInwardFiles_ProcessDate` | D (DATE) |  | This field specifies the Treatment date of the inward file. Validation Rules Value upto 11 type D(DATE) |
| 5 | `SEP.ICF.PROCESS.TIME` | `SepaInwardFiles_ProcessTime` | TField |  | This field specifies the Treatment time of the inward file. Validation Rules Value upto 5 type TIME( Time Format) |
| 6 | `SEP.ICF.CREATION.DATE` | `SepaInwardFiles_CreationDate` | D (DATE) |  | This field specifies the Creation date of the inward file. Validation Rules Value upto 11 type D(DATE) |
| 7 | `SEP.ICF.CREATION.TIME` | `SepaInwardFiles_CreationTime` | TField |  | This field specifies the Creation time of the inward file. Validation Rules Value upto 5 type TIME( Time Format) |
| 8 | `SEP.ICF.FILE.HEADER` | `SepaInwardFiles_FileHeader` | A (Alphanumeric) |  | This field contains the File header sequence stored in such a way that it can be shown easily as it was in its original XML presentation by a delivered T24 drill down enquiry. Validation Rules Value upto 35 type A(Alphanumeric) |
| 9 | `SEP.ICF.MESSAGE.ID` | `SepaInwardFiles_MessageId` |  |  |  |
| 10 | `SEP.ICF.MESSAGE.TYPE` | `SepaInwardFiles_MessageType` |  |  |  |
| 11 | `SEP.ICF.GROUP.HEADER` | `SepaInwardFiles_GroupHeader` |  |  |  |
| 12 | `SEP.ICF.ORIGINAL.GROUP` | `SepaInwardFiles_OriginalGroup` |  |  |  |
| 13 | `SEP.ICF.SEPA.DETAIL.ID` | `SepaInwardFiles_SepaDetailId` |  |  |  |
| 14 | `SEP.ICF.TRANS.CODE` | `SepaInwardFiles_TransCode` |  |  |  |
| 15 | `SEP.ICF.TRANS.FIRST` | `SepaInwardFiles_TransFirst` |  |  |  |
| 16 | `SEP.ICF.TRANS.LAST` | `SepaInwardFiles_TransLast` |  |  |  |
| 17 | `SEP.ICF.TRANS.NUMBER` | `SepaInwardFiles_TransNumber` |  |  |  |
| 18 | `SEP.ICF.TOTAL.CHG` | `SepaInwardFiles_TotalChg` |  |  |  |
| 19 | `SEP.ICF.NET.AMOUNT` | `SepaInwardFiles_NetAmount` |  |  |  |
| 20 | `SEP.ICF.TOT.AMOUNT` | `SepaInwardFiles_TotAmount` |  |  |  |
| 21 | `SEP.ICF.STMT.NOS` | `SepaInwardFiles_StmtNos` |  |  |  |
| 22 | `SEP.ICF.LINKED.FT.ID` | `SepaInwardFiles_LinkedFtId` |  |  |  |
| 23 | `SEP.ICF.TXN.NETTING.ID` | `SepaInwardFiles_TxnNettingId` |  |  |  |
| 24 | `SEP.ICF.ON.US.TRANS` | `SepaInwardFiles_OnUsTrans` |  |  |  |
| 25 | `SEP.ICF.RESERVED.13` | `SepaInwardFiles_Reserved13` |  |  |  |
| 26 | `SEP.ICF.RESERVED.12` | `SepaInwardFiles_Reserved12` |  |  |  |
| 27 | `SEP.ICF.RESERVED.11` | `SepaInwardFiles_Reserved11` |  |  |  |
| 28 | `SEP.ICF.COMMENT` | `SepaInwardFiles_Comment` |  |  |  |
| 29 | `SEP.ICF.FILE.TRAILER` | `SepaInwardFiles_FileTrailer` | A (Alphanumeric) |  | This Field holds the Last Tag of the file �&lt;/SEPA.HEADER.ID&gt;� Validation Rules Value upto 35 type A(Alphanumeric) |
| 30 | `SEP.ICF.STATUS` | `SepaInwardFiles_Status` | TField |  | This field holds the Status of the transaction posted. ACP - Accepted CXL � Cancelled PND � Pending PRC � Processed RCV � Received RDY � Ready for transfer REJ � Rejected RET � Returned SND � Sent TRF - Transferred Validation Rules Value upto 3 type SEPA.TRANSFER.STS.LIST |
| 31 | `SEP.ICF.PRE.HEADER` | `SepaInwardFiles_PreHeader` |  |  |  |
| 32 | `SEP.ICF.LOCAL.REF` | `SepaInwardFiles_LocalRef` |  |  |  |
| 33 | `SEP.ICF.TOT.NO.OF.TXN.FILE` | `SepaInwardFiles_TotNoOfTxnFile` | TField |  | Total Number of Transactions in a file. Taken from the value in NbOfTxs tag in the XML file from Header part Validation Rules Value upto 18 type ANY(Any Character) |
| 34 | `SEP.ICF.TOT.AMOUNT.FILE` | `SepaInwardFiles_TotAmountFile` | TField |  | Total Transaction Amount in a file. Taken from the value in CtrlSum tag in the XML file from Header part Validation Rules Value upto 18 type ANY(Any Character) |
| 35 | `SEP.ICF.RESERVED.10` | `SepaInwardFiles_Reserved10` | TField |  |  |
| 36 | `SEP.ICF.RESERVED.9` | `SepaInwardFiles_Reserved9` | TField |  |  |
| 37 | `SEP.ICF.RESERVED.8` | `SepaInwardFiles_Reserved8` | TField |  |  |
| 38 | `SEP.ICF.RESERVED.7` | `SepaInwardFiles_Reserved7` | TField |  |  |
| 39 | `SEP.ICF.RESERVED.6` | `SepaInwardFiles_Reserved6` | TField |  |  |
| 40 | `SEP.ICF.RESERVED.5` | `SepaInwardFiles_Reserved5` | TField |  |  |
| 41 | `SEP.ICF.RESERVED.4` | `SepaInwardFiles_Reserved4` | TField |  |  |
| 42 | `SEP.ICF.RESERVED.3` | `SepaInwardFiles_Reserved3` | TField |  |  |
| 43 | `SEP.ICF.RESERVED.2` | `SepaInwardFiles_Reserved2` | TField |  |  |
| 44 | `SEP.ICF.RESERVED.1` | `SepaInwardFiles_Reserved1` | TField |  |  |
