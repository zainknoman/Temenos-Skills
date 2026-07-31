# BL.TXN.TYPE.CONDITION — Table Schema

> Source: `INSERTS/I_F.BL.TXN.TYPE.CONDITION` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.TXN.CHG.CODE` | `BlTxnTypeCondition_ChgCode` |  |  |  |
| 2 | `BL.TXN.CHARGE.LEVEL` | `BlTxnTypeCondition_ChargeLevel` |  |  |  |
| 3 | `BL.TXN.DISB.TXN.CODE` | `BlTxnTypeCondition_DisbTxnCode` | TField | No | The transaction code defined here is used for transaction processing during BL Disbursement which uses this BTTC Key. If it is not defined here, the code defined at the BL.PARAMETER level would be used. Validation Rules: Optional field. Must be valid record in TRANSACTION file. |
| 4 | `BL.TXN.GRACE.DAYS` | `BlTxnTypeCondition_GraceDays` | TField | No | This is an optional field with the Format nnC or nnW where nn is a number from 1 to 99. "C" stands for Calendar days and "W" for working days. An input of 0 is also allowed. If no value is entered, then the value would default as explained below which is a defaulting mechanism. If BGC value is defined (not null) then BGC value would be defaulted. If BTTC value is defined (not null) and BGC value is not defined (null), then BTTC value would be defaulted. If both BGC and BTTC values were not defined (null), then the Grace Days defined in the BL.PARAMETER file would be defaulted. Validation Rules: Value of 1-99 allowed suffixed with "C" or "W" |
| 5 | `BL.TXN.RETENTION.MARGIN` | `BlTxnTypeCondition_RetentionMargin` | TField |  | This field is to specify the default value for Retention margin for an invoice at transaction level Validation Rules: Standard T24 Rate field to specify retention margin percentage Accepts values in range 0 � 99 |
| 6 | `BL.TXN.CURRENCY` | `BlTxnTypeCondition_Currency` |  |  |  |
| 7 | `BL.TXN.INT.KEY` | `BlTxnTypeCondition_IntKey` |  |  |  |
| 8 | `BL.TXN.INT.SPREAD` | `BlTxnTypeCondition_IntSpread` |  |  |  |
| 9 | `BL.TXN.INT.RATE` | `BlTxnTypeCondition_IntRate` |  |  |  |
| 10 | `BL.TXN.MAX.INT.RATE` | `BlTxnTypeCondition_MaxIntRate` | TField | No | The value specified is used to check if the calculated Effective Rate of Interest is within permissible limits. The method of using these values for generating override messages is explained under "Defaulting Mechanism". If an interest rate is defined here, it implies that the Effective Interest Rate should not exceed the rate specified in this field during BL.BILL contract processing. Validation Rules: Optional Input |
| 11 | `BL.TXN.MIN.INT.RATE` | `BlTxnTypeCondition_MinIntRate` | TField | No | The value specified is used to check if the calculated Effective Rate of Interest is within permissible limits. The method of using these values for generating override messages is explained under "Defaulting Mechanism". If an interest rate is defined here, it implies that the Effective Interest Rate should not go below the rate specified in this field during BL.BILL Contract processing. Validation Rules: This is an optional input field. |
| 12 | `BL.TXN.RESERVED.10` | `BlTxnTypeCondition_Reserved10` | TField |  |  |
| 13 | `BL.TXN.RESERVED.9` | `BlTxnTypeCondition_Reserved9` | TField |  |  |
| 14 | `BL.TXN.RESERVED.8` | `BlTxnTypeCondition_Reserved8` | TField |  |  |
| 15 | `BL.TXN.RESERVED.7` | `BlTxnTypeCondition_Reserved7` | TField |  |  |
| 16 | `BL.TXN.RESERVED.6` | `BlTxnTypeCondition_Reserved6` | TField |  |  |
| 17 | `BL.TXN.RESERVED.5` | `BlTxnTypeCondition_Reserved5` | TField |  |  |
| 18 | `BL.TXN.RESERVED.4` | `BlTxnTypeCondition_Reserved4` | TField |  |  |
| 19 | `BL.TXN.RESERVED.3` | `BlTxnTypeCondition_Reserved3` | TField |  |  |
| 20 | `BL.TXN.RESERVED.2` | `BlTxnTypeCondition_Reserved2` | TField |  |  |
| 21 | `BL.TXN.RESERVED.1` | `BlTxnTypeCondition_Reserved1` | TField |  |  |
| 22 | `BL.TXN.LOCAL.REF` | `BlTxnTypeCondition_LocalRef` |  |  |  |
| 23 | `BL.TXN.OVERRIDE` | `BlTxnTypeCondition_Override` |  |  |  |
| 24 | `BL.TXN.RECORD.STATUS` | `BlTxnTypeCondition_RecordStatus` | String |  |  |
| 25 | `BL.TXN.CURR.NO` | `BlTxnTypeCondition_CurrNo` | String |  |  |
| 26 | `BL.TXN.INPUTTER` | `BlTxnTypeCondition_Inputter` |  |  |  |
| 27 | `BL.TXN.DATE.TIME` | `BlTxnTypeCondition_DateTime` |  |  |  |
| 28 | `BL.TXN.AUTHORISER` | `BlTxnTypeCondition_Authoriser` | String |  |  |
| 29 | `BL.TXN.CO.CODE` | `BlTxnTypeCondition_CoCode` | String |  |  |
| 30 | `BL.TXN.DEPT.CODE` | `BlTxnTypeCondition_DeptCode` | String |  |  |
| 31 | `BL.TXN.AUDITOR.CODE` | `BlTxnTypeCondition_AuditorCode` | String |  |  |
| 32 | `BL.TXN.AUDIT.DATE.TIME` | `BlTxnTypeCondition_AuditDateTime` | String |  |  |
