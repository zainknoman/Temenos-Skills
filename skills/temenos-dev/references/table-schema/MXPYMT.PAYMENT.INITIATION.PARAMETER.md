# MXPYMT.PAYMENT.INITIATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.MXPYMT.PAYMENT.INITIATION.PARAMETER` in `MXPYMT_PaymentInitiationWaiting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MXPYMT.PAYMENT.ORDER.PRODUCT` | `MxpymtPaymentInitiationParameter_PaymentOrderProduct` |  |  |  |
| 2 | `MXPYMT.TXN.ORIGIN.CHANNEL` | `MxpymtPaymentInitiationParameter_TxnOriginChannel` |  |  |  |
| 3 | `MXPYMT.BENEFICIARY.CREATION.CHANNEL` | `MxpymtPaymentInitiationParameter_BeneficiaryCreationChannel` |  |  |  |
| 4 | `MXPYMT.CURRENCY` | `MxpymtPaymentInitiationParameter_Currency` |  |  |  |
| 5 | `MXPYMT.TXN.THRESHOLD.AMOUNT.BENEFIC` | `MxpymtPaymentInitiationParameter_TxnThresholdAmountBenefic` |  |  |  |
| 6 | `MXPYMT.TXN.THRESHOLD.AMOUNT.DELAY` | `MxpymtPaymentInitiationParameter_TxnThresholdAmountDelay` |  |  |  |
| 7 | `MXPYMT.DELAY.TIME` | `MxpymtPaymentInitiationParameter_DelayTime` |  |  |  |
| 8 | `MXPYMT.RESERVED.10` | `MxpymtPaymentInitiationParameter_Reserved10` |  |  |  |
| 9 | `MXPYMT.RESERVED.9` | `MxpymtPaymentInitiationParameter_Reserved9` |  |  |  |
| 10 | `MXPYMT.RESERVED.8` | `MxpymtPaymentInitiationParameter_Reserved8` |  |  |  |
| 11 | `MXPYMT.RESERVED.7` | `MxpymtPaymentInitiationParameter_Reserved7` |  |  |  |
| 12 | `MXPYMT.RESERVED.6` | `MxpymtPaymentInitiationParameter_Reserved6` | TField |  |  |
| 13 | `MXPYMT.RESERVED.5` | `MxpymtPaymentInitiationParameter_Reserved5` | TField |  |  |
| 14 | `MXPYMT.RESERVED.4` | `MxpymtPaymentInitiationParameter_Reserved4` | TField |  |  |
| 15 | `MXPYMT.RESERVED.3` | `MxpymtPaymentInitiationParameter_Reserved3` | TField |  |  |
| 16 | `MXPYMT.RESERVED.2` | `MxpymtPaymentInitiationParameter_Reserved2` | TField |  |  |
| 17 | `MXPYMT.RESERVED.1` | `MxpymtPaymentInitiationParameter_Reserved1` | TField |  |  |
| 18 | `MXPYMT.OVERRIDE` | `MxpymtPaymentInitiationParameter_Override` |  |  |  |
| 19 | `MXPYMT.RECORD.STATUS` | `MxpymtPaymentInitiationParameter_RecordStatus` | String |  |  |
| 20 | `MXPYMT.CURR.NO` | `MxpymtPaymentInitiationParameter_CurrNo` | String |  |  |
| 21 | `MXPYMT.INPUTTER` | `MxpymtPaymentInitiationParameter_Inputter` |  |  |  |
| 22 | `MXPYMT.DATE.TIME` | `MxpymtPaymentInitiationParameter_DateTime` |  |  |  |
| 23 | `MXPYMT.AUTHORISER` | `MxpymtPaymentInitiationParameter_Authoriser` | String |  |  |
| 24 | `MXPYMT.CO.CODE` | `MxpymtPaymentInitiationParameter_CoCode` | String |  |  |
| 25 | `MXPYMT.DEPT.CODE` | `MxpymtPaymentInitiationParameter_DeptCode` | String |  |  |
| 26 | `MXPYMT.AUDITOR.CODE` | `MxpymtPaymentInitiationParameter_AuditorCode` | String |  |  |
| 27 | `MXPYMT.AUDIT.DATE.TIME` | `MxpymtPaymentInitiationParameter_AuditDateTime` | String |  |  |
