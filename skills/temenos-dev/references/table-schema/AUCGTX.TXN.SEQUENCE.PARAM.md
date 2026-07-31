# AUCGTX.TXN.SEQUENCE.PARAM — Table Schema

> Source: `INSERTS/I_F.AUCGTX.TXN.SEQUENCE.PARAM` in `AUCGTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TXN.SEQ.TXN.NAME` | `AucgtxTxnSequenceParam_TxnName` |  |  |  |
| 2 | `TXN.SEQ.CG.TXN.TIME` | `AucgtxTxnSequenceParam_CgTxnTime` |  |  |  |
| 3 | `TXN.SEQ.DEFAULT.CR.TIME` | `AucgtxTxnSequenceParam_DefaultCrTime` | TField |  | This will hold the default time to be used for a Credit transaction, if the transaction type is not defined in TXN.NAME field. |
| 4 | `TXN.SEQ.DEFAULT.DR.TIME` | `AucgtxTxnSequenceParam_DefaultDrTime` | TField |  | This will hold the default time to be used for a Debit transaction, if the transaction type is not defined in TXN.NAME field. |
| 5 | `TXN.SEQ.TXN.SEQUENCE` | `AucgtxTxnSequenceParam_TxnSequence` | TField |  | This field should be set to Yes if the Sequencing should be performed. If this is set to No, the time fields will be populated based on the standard L1 processing. |
| 6 | `TXN.SEQ.LOCAL.REF` | `AucgtxTxnSequenceParam_LocalRef` |  |  |  |
| 7 | `TXN.SEQ.RESERVED.1` | `AucgtxTxnSequenceParam_Reserved1` | TField |  |  |
| 8 | `TXN.SEQ.RESERVED.2` | `AucgtxTxnSequenceParam_Reserved2` | TField |  |  |
| 9 | `TXN.SEQ.RESERVED.3` | `AucgtxTxnSequenceParam_Reserved3` | TField |  |  |
| 10 | `TXN.SEQ.RESERVED.4` | `AucgtxTxnSequenceParam_Reserved4` | TField |  |  |
| 11 | `TXN.SEQ.RESERVED.5` | `AucgtxTxnSequenceParam_Reserved5` | TField |  |  |
| 12 | `TXN.SEQ.RESERVED.6` | `AucgtxTxnSequenceParam_Reserved6` | TField |  |  |
| 13 | `TXN.SEQ.RESERVED.7` | `AucgtxTxnSequenceParam_Reserved7` | TField |  |  |
| 14 | `TXN.SEQ.RESERVED.8` | `AucgtxTxnSequenceParam_Reserved8` | TField |  |  |
| 15 | `TXN.SEQ.RESERVED.9` | `AucgtxTxnSequenceParam_Reserved9` | TField |  |  |
| 16 | `TXN.SEQ.RESERVED.10` | `AucgtxTxnSequenceParam_Reserved10` | TField |  |  |
| 17 | `TXN.SEQ.OVERRIDE` | `AucgtxTxnSequenceParam_Override` |  |  |  |
| 18 | `TXN.SEQ.RECORD.STATUS` | `AucgtxTxnSequenceParam_RecordStatus` | String |  |  |
| 19 | `TXN.SEQ.CURR.NO` | `AucgtxTxnSequenceParam_CurrNo` | String |  |  |
| 20 | `TXN.SEQ.INPUTTER` | `AucgtxTxnSequenceParam_Inputter` |  |  |  |
| 21 | `TXN.SEQ.DATE.TIME` | `AucgtxTxnSequenceParam_DateTime` |  |  |  |
| 22 | `TXN.SEQ.AUTHORISER` | `AucgtxTxnSequenceParam_Authoriser` | String |  |  |
| 23 | `TXN.SEQ.CO.CODE` | `AucgtxTxnSequenceParam_CoCode` | String |  |  |
| 24 | `TXN.SEQ.DEPT.CODE` | `AucgtxTxnSequenceParam_DeptCode` | String |  |  |
| 25 | `TXN.SEQ.AUDITOR.CODE` | `AucgtxTxnSequenceParam_AuditorCode` | String |  |  |
| 26 | `TXN.SEQ.AUDIT.DATE.TIME` | `AucgtxTxnSequenceParam_AuditDateTime` | String |  |  |
