# FS.GI.RECEIPT.REMITTER.CHECK — Table Schema

> Source: `INSERTS/I_F.FS.GI.RECEIPT.REMITTER.CHECK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.RECE.REMITTER.CHECK.REMITTER.CHECK.ID` | `FsGiReceiptRemitterCheck_RemitterCheckId` |  |  |  |
| 2 | `GI.RECE.REMITTER.CHECK.REMITTER.CHECK.DESCRIPTION` | `FsGiReceiptRemitterCheck_RemitterCheckDescription` |  |  |  |
| 3 | `GI.RECE.REMITTER.CHECK.STATUS` | `FsGiReceiptRemitterCheck_Status` |  |  |  |
| 4 | `GI.RECE.REMITTER.CHECK.PENDING.FLAG` | `FsGiReceiptRemitterCheck_PendingFlag` |  |  |  |
| 5 | `GI.RECE.REMITTER.CHECK.RESERVED10` | `FsGiReceiptRemitterCheck_Reserved10` |  |  |  |
| 6 | `GI.RECE.REMITTER.CHECK.RESERVED9` | `FsGiReceiptRemitterCheck_Reserved9` |  |  |  |
| 7 | `GI.RECE.REMITTER.CHECK.RESERVED8` | `FsGiReceiptRemitterCheck_Reserved8` |  |  |  |
| 8 | `GI.RECE.REMITTER.CHECK.RESERVED7` | `FsGiReceiptRemitterCheck_Reserved7` |  |  |  |
| 9 | `GI.RECE.REMITTER.CHECK.RESERVED6` | `FsGiReceiptRemitterCheck_Reserved6` |  |  |  |
| 10 | `GI.RECE.REMITTER.CHECK.RESERVED5` | `FsGiReceiptRemitterCheck_Reserved5` |  |  |  |
| 11 | `GI.RECE.REMITTER.CHECK.RESERVED4` | `FsGiReceiptRemitterCheck_Reserved4` |  |  |  |
| 12 | `GI.RECE.REMITTER.CHECK.RESERVED3` | `FsGiReceiptRemitterCheck_Reserved3` |  |  |  |
| 13 | `GI.RECE.REMITTER.CHECK.RESERVED2` | `FsGiReceiptRemitterCheck_Reserved2` |  |  |  |
| 14 | `GI.RECE.REMITTER.CHECK.RESERVED1` | `FsGiReceiptRemitterCheck_Reserved1` |  |  |  |
| 15 | `GI.RECE.REMITTER.CHECK.LOCAL.REF` | `FsGiReceiptRemitterCheck_LocalRef` |  |  |  |
| 16 | `GI.RECE.REMITTER.CHECK.OVERRIDE` | `FsGiReceiptRemitterCheck_Override` |  |  |  |
| 17 | `GI.RECE.REMITTER.CHECK.RECORD.STATUS` | `FsGiReceiptRemitterCheck_RecordStatus` |  |  |  |
| 18 | `GI.RECE.REMITTER.CHECK.CURR.NO` | `FsGiReceiptRemitterCheck_CurrNo` |  |  |  |
| 19 | `GI.RECE.REMITTER.CHECK.INPUTTER` | `FsGiReceiptRemitterCheck_Inputter` |  |  |  |
| 20 | `GI.RECE.REMITTER.CHECK.DATE.TIME` | `FsGiReceiptRemitterCheck_DateTime` |  |  |  |
| 21 | `GI.RECE.REMITTER.CHECK.AUTHORISER` | `FsGiReceiptRemitterCheck_Authoriser` |  |  |  |
| 22 | `GI.RECE.REMITTER.CHECK.CO.CODE` | `FsGiReceiptRemitterCheck_CoCode` |  |  |  |
| 23 | `GI.RECE.REMITTER.CHECK.DEPT.CODE` | `FsGiReceiptRemitterCheck_DeptCode` |  |  |  |
| 24 | `GI.RECE.REMITTER.CHECK.AUDITOR.CODE` | `FsGiReceiptRemitterCheck_AuditorCode` |  |  |  |
| 25 | `GI.RECE.REMITTER.CHECK.AUDIT.DATE.TIME` | `FsGiReceiptRemitterCheck_AuditDateTime` |  |  |  |
