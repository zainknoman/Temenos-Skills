# FS.GI.PAYMENT.INST.INDIVIDUAL.MEMO — Table Schema

> Source: `INSERTS/I_F.FS.GI.PAYMENT.INST.INDIVIDUAL.MEMO` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.INDIVIDUAL.PAYMENT.ID` | `FsGiPaymentInstIndividualMemo_IndividualPaymentId` |  |  |  |
| 2 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.BATCH.ID` | `FsGiPaymentInstIndividualMemo_BatchId` |  |  |  |
| 3 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.MEMO` | `FsGiPaymentInstIndividualMemo_Memo` |  |  |  |
| 4 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED10` | `FsGiPaymentInstIndividualMemo_Reserved10` |  |  |  |
| 5 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED9` | `FsGiPaymentInstIndividualMemo_Reserved9` |  |  |  |
| 6 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED8` | `FsGiPaymentInstIndividualMemo_Reserved8` |  |  |  |
| 7 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED7` | `FsGiPaymentInstIndividualMemo_Reserved7` |  |  |  |
| 8 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED6` | `FsGiPaymentInstIndividualMemo_Reserved6` |  |  |  |
| 9 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED5` | `FsGiPaymentInstIndividualMemo_Reserved5` |  |  |  |
| 10 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED4` | `FsGiPaymentInstIndividualMemo_Reserved4` |  |  |  |
| 11 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED3` | `FsGiPaymentInstIndividualMemo_Reserved3` |  |  |  |
| 12 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED2` | `FsGiPaymentInstIndividualMemo_Reserved2` |  |  |  |
| 13 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RESERVED1` | `FsGiPaymentInstIndividualMemo_Reserved1` |  |  |  |
| 14 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.LOCAL.REF` | `FsGiPaymentInstIndividualMemo_LocalRef` |  |  |  |
| 15 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.OVERRIDE` | `FsGiPaymentInstIndividualMemo_Override` |  |  |  |
| 16 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.RECORD.STATUS` | `FsGiPaymentInstIndividualMemo_RecordStatus` |  |  |  |
| 17 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.CURR.NO` | `FsGiPaymentInstIndividualMemo_CurrNo` |  |  |  |
| 18 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.INPUTTER` | `FsGiPaymentInstIndividualMemo_Inputter` |  |  |  |
| 19 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.DATE.TIME` | `FsGiPaymentInstIndividualMemo_DateTime` |  |  |  |
| 20 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.AUTHORISER` | `FsGiPaymentInstIndividualMemo_Authoriser` |  |  |  |
| 21 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.CO.CODE` | `FsGiPaymentInstIndividualMemo_CoCode` |  |  |  |
| 22 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.DEPT.CODE` | `FsGiPaymentInstIndividualMemo_DeptCode` |  |  |  |
| 23 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.AUDITOR.CODE` | `FsGiPaymentInstIndividualMemo_AuditorCode` |  |  |  |
| 24 | `GI.PAYMENT.INST.INDIVIDUAL.MEMO.AUDIT.DATE.TIME` | `FsGiPaymentInstIndividualMemo_AuditDateTime` |  |  |  |
