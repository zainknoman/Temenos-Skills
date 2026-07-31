# FS.GI.RECEIPT.DEAL.MEMO — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.DEAL.MEMO` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.REC.DEAL.MEMO.DEAL.REFERENCE` | `FsGiReceiptDealMemo_DealReference` |  |  |  |
| 2 | `GI.REC.DEAL.MEMO.ORDER.ID` | `FsGiReceiptDealMemo_OrderId` |  |  |  |
| 3 | `GI.REC.DEAL.MEMO.PARTIAL.SETTLEMENT.ID` | `FsGiReceiptDealMemo_PartialSettlementId` |  |  |  |
| 4 | `GI.REC.DEAL.MEMO.MEMO` | `FsGiReceiptDealMemo_Memo` |  |  |  |
| 5 | `GI.REC.DEAL.MEMO.RESERVED10` | `FsGiReceiptDealMemo_Reserved10` |  |  |  |
| 6 | `GI.REC.DEAL.MEMO.RESERVED9` | `FsGiReceiptDealMemo_Reserved9` |  |  |  |
| 7 | `GI.REC.DEAL.MEMO.RESERVED8` | `FsGiReceiptDealMemo_Reserved8` |  |  |  |
| 8 | `GI.REC.DEAL.MEMO.RESERVED7` | `FsGiReceiptDealMemo_Reserved7` |  |  |  |
| 9 | `GI.REC.DEAL.MEMO.RESERVED6` | `FsGiReceiptDealMemo_Reserved6` |  |  |  |
| 10 | `GI.REC.DEAL.MEMO.RESERVED5` | `FsGiReceiptDealMemo_Reserved5` |  |  |  |
| 11 | `GI.REC.DEAL.MEMO.RESERVED4` | `FsGiReceiptDealMemo_Reserved4` |  |  |  |
| 12 | `GI.REC.DEAL.MEMO.RESERVED3` | `FsGiReceiptDealMemo_Reserved3` |  |  |  |
| 13 | `GI.REC.DEAL.MEMO.RESERVED2` | `FsGiReceiptDealMemo_Reserved2` |  |  |  |
| 14 | `GI.REC.DEAL.MEMO.RESERVED1` | `FsGiReceiptDealMemo_Reserved1` |  |  |  |
| 15 | `GI.REC.DEAL.MEMO.LOCAL.REF` | `FsGiReceiptDealMemo_LocalRef` |  |  |  |
| 16 | `GI.REC.DEAL.MEMO.OVERRIDE` | `FsGiReceiptDealMemo_Override` |  |  |  |
| 17 | `GI.REC.DEAL.MEMO.RECORD.STATUS` | `FsGiReceiptDealMemo_RecordStatus` |  |  |  |
| 18 | `GI.REC.DEAL.MEMO.CURR.NO` | `FsGiReceiptDealMemo_CurrNo` |  |  |  |
| 19 | `GI.REC.DEAL.MEMO.INPUTTER` | `FsGiReceiptDealMemo_Inputter` |  |  |  |
| 20 | `GI.REC.DEAL.MEMO.DATE.TIME` | `FsGiReceiptDealMemo_DateTime` |  |  |  |
| 21 | `GI.REC.DEAL.MEMO.AUTHORISER` | `FsGiReceiptDealMemo_Authoriser` |  |  |  |
| 22 | `GI.REC.DEAL.MEMO.CO.CODE` | `FsGiReceiptDealMemo_CoCode` |  |  |  |
| 23 | `GI.REC.DEAL.MEMO.DEPT.CODE` | `FsGiReceiptDealMemo_DeptCode` |  |  |  |
| 24 | `GI.REC.DEAL.MEMO.AUDITOR.CODE` | `FsGiReceiptDealMemo_AuditorCode` |  |  |  |
| 25 | `GI.REC.DEAL.MEMO.AUDIT.DATE.TIME` | `FsGiReceiptDealMemo_AuditDateTime` |  |  |  |
