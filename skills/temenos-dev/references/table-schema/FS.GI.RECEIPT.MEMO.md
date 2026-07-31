# FS.GI.RECEIPT.MEMO — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.MEMO` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.RECEIPT.MEMO.RECEIPT.ID` | `FsGiReceiptMemo_ReceiptId` |  |  |  |
| 2 | `GI.RECEIPT.MEMO.MEMO` | `FsGiReceiptMemo_Memo` |  |  |  |
| 3 | `GI.RECEIPT.MEMO.RESERVED10` | `FsGiReceiptMemo_Reserved10` |  |  |  |
| 4 | `GI.RECEIPT.MEMO.RESERVED9` | `FsGiReceiptMemo_Reserved9` |  |  |  |
| 5 | `GI.RECEIPT.MEMO.RESERVED8` | `FsGiReceiptMemo_Reserved8` |  |  |  |
| 6 | `GI.RECEIPT.MEMO.RESERVED7` | `FsGiReceiptMemo_Reserved7` |  |  |  |
| 7 | `GI.RECEIPT.MEMO.RESERVED6` | `FsGiReceiptMemo_Reserved6` |  |  |  |
| 8 | `GI.RECEIPT.MEMO.RESERVED5` | `FsGiReceiptMemo_Reserved5` |  |  |  |
| 9 | `GI.RECEIPT.MEMO.RESERVED4` | `FsGiReceiptMemo_Reserved4` |  |  |  |
| 10 | `GI.RECEIPT.MEMO.RESERVED3` | `FsGiReceiptMemo_Reserved3` |  |  |  |
| 11 | `GI.RECEIPT.MEMO.RESERVED2` | `FsGiReceiptMemo_Reserved2` |  |  |  |
| 12 | `GI.RECEIPT.MEMO.RESERVED1` | `FsGiReceiptMemo_Reserved1` |  |  |  |
| 13 | `GI.RECEIPT.MEMO.LOCAL.REF` | `FsGiReceiptMemo_LocalRef` |  |  |  |
| 14 | `GI.RECEIPT.MEMO.OVERRIDE` | `FsGiReceiptMemo_Override` |  |  |  |
| 15 | `GI.RECEIPT.MEMO.RECORD.STATUS` | `FsGiReceiptMemo_RecordStatus` |  |  |  |
| 16 | `GI.RECEIPT.MEMO.CURR.NO` | `FsGiReceiptMemo_CurrNo` |  |  |  |
| 17 | `GI.RECEIPT.MEMO.INPUTTER` | `FsGiReceiptMemo_Inputter` |  |  |  |
| 18 | `GI.RECEIPT.MEMO.DATE.TIME` | `FsGiReceiptMemo_DateTime` |  |  |  |
| 19 | `GI.RECEIPT.MEMO.AUTHORISER` | `FsGiReceiptMemo_Authoriser` |  |  |  |
| 20 | `GI.RECEIPT.MEMO.CO.CODE` | `FsGiReceiptMemo_CoCode` |  |  |  |
| 21 | `GI.RECEIPT.MEMO.DEPT.CODE` | `FsGiReceiptMemo_DeptCode` |  |  |  |
| 22 | `GI.RECEIPT.MEMO.AUDITOR.CODE` | `FsGiReceiptMemo_AuditorCode` |  |  |  |
| 23 | `GI.RECEIPT.MEMO.AUDIT.DATE.TIME` | `FsGiReceiptMemo_AuditDateTime` |  |  |  |
