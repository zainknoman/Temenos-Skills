# FS.GI.PAYMENT.REPROCESS.PAY.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.PAYMENT.REPROCESS.PAY.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PAYMENT.REPROCESS.PAY.DET.UNIQUE.PAYMENT.REFERENCE` | `FsGiPaymentReprocessPayDetails_UniquePaymentReference` |  |  |  |
| 2 | `GI.PAYMENT.REPROCESS.PAY.DET.LINKED.BATCH.ID` | `FsGiPaymentReprocessPayDetails_LinkedBatchId` |  |  |  |
| 3 | `GI.PAYMENT.REPROCESS.PAY.DET.PAYMENT.EXTERNAL.REFERENCE` | `FsGiPaymentReprocessPayDetails_PaymentExternalReference` |  |  |  |
| 4 | `GI.PAYMENT.REPROCESS.PAY.DET.PAYMENT.REPROCESS.ID` | `FsGiPaymentReprocessPayDetails_PaymentReprocessId` |  |  |  |
| 5 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED10` | `FsGiPaymentReprocessPayDetails_Reserved10` |  |  |  |
| 6 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED9` | `FsGiPaymentReprocessPayDetails_Reserved9` |  |  |  |
| 7 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED8` | `FsGiPaymentReprocessPayDetails_Reserved8` |  |  |  |
| 8 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED7` | `FsGiPaymentReprocessPayDetails_Reserved7` |  |  |  |
| 9 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED6` | `FsGiPaymentReprocessPayDetails_Reserved6` |  |  |  |
| 10 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED5` | `FsGiPaymentReprocessPayDetails_Reserved5` |  |  |  |
| 11 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED4` | `FsGiPaymentReprocessPayDetails_Reserved4` |  |  |  |
| 12 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED3` | `FsGiPaymentReprocessPayDetails_Reserved3` |  |  |  |
| 13 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED2` | `FsGiPaymentReprocessPayDetails_Reserved2` |  |  |  |
| 14 | `GI.PAYMENT.REPROCESS.PAY.DET.RESERVED1` | `FsGiPaymentReprocessPayDetails_Reserved1` |  |  |  |
| 15 | `GI.PAYMENT.REPROCESS.PAY.DET.LOCAL.REF` | `FsGiPaymentReprocessPayDetails_LocalRef` |  |  |  |
| 16 | `GI.PAYMENT.REPROCESS.PAY.DET.OVERRIDE` | `FsGiPaymentReprocessPayDetails_Override` |  |  |  |
| 17 | `GI.PAYMENT.REPROCESS.PAY.DET.RECORD.STATUS` | `FsGiPaymentReprocessPayDetails_RecordStatus` |  |  |  |
| 18 | `GI.PAYMENT.REPROCESS.PAY.DET.CURR.NO` | `FsGiPaymentReprocessPayDetails_CurrNo` |  |  |  |
| 19 | `GI.PAYMENT.REPROCESS.PAY.DET.INPUTTER` | `FsGiPaymentReprocessPayDetails_Inputter` |  |  |  |
| 20 | `GI.PAYMENT.REPROCESS.PAY.DET.DATE.TIME` | `FsGiPaymentReprocessPayDetails_DateTime` |  |  |  |
| 21 | `GI.PAYMENT.REPROCESS.PAY.DET.AUTHORISER` | `FsGiPaymentReprocessPayDetails_Authoriser` |  |  |  |
| 22 | `GI.PAYMENT.REPROCESS.PAY.DET.CO.CODE` | `FsGiPaymentReprocessPayDetails_CoCode` |  |  |  |
| 23 | `GI.PAYMENT.REPROCESS.PAY.DET.DEPT.CODE` | `FsGiPaymentReprocessPayDetails_DeptCode` |  |  |  |
| 24 | `GI.PAYMENT.REPROCESS.PAY.DET.AUDITOR.CODE` | `FsGiPaymentReprocessPayDetails_AuditorCode` |  |  |  |
| 25 | `GI.PAYMENT.REPROCESS.PAY.DET.AUDIT.DATE.TIME` | `FsGiPaymentReprocessPayDetails_AuditDateTime` |  |  |  |
