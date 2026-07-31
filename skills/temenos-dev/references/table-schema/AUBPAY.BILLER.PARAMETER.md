# AUBPAY.BILLER.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AUBPAY.BILLER.PARAMETER` in `AUBPAY_BillerManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUBPAY.PARAM.PAYMENT.METHOD` | `AubpayBillerParameter_PaymentMethod` |  |  |  |
| 2 | `AUBPAY.PARAM.MIN.AMT.LOWER.LIMIT` | `AubpayBillerParameter_MinAmtLowerLimit` |  |  |  |
| 3 | `AUBPAY.PARAM.MIN.AMT.UPPER.LIMIT` | `AubpayBillerParameter_MinAmtUpperLimit` |  |  |  |
| 4 | `AUBPAY.PARAM.MAX.AMT.LOWER.LIMIT` | `AubpayBillerParameter_MaxAmtLowerLimit` |  |  |  |
| 5 | `AUBPAY.PARAM.MAX.AMT.UPPER.LIMIT` | `AubpayBillerParameter_MaxAmtUpperLimit` |  |  |  |
| 6 | `AUBPAY.PARAM.VAL.LENGTH.MIN.LIMIT` | `AubpayBillerParameter_ValLengthMinLimit` | TField |  | Minimum Limit of Valid Length |
| 7 | `AUBPAY.PARAM.VAL.LENGTH.MAX.LIMIT` | `AubpayBillerParameter_ValLengthMaxLimit` | TField |  | Maximum Limit of Valid Length |
| 8 | `AUBPAY.PARAM.LOCAL.REF` | `AubpayBillerParameter_LocalRef` |  |  |  |
| 9 | `AUBPAY.PARAM.OVERRIDE` | `AubpayBillerParameter_Override` |  |  |  |
| 10 | `AUBPAY.PARAM.RECORD.STATUS` | `AubpayBillerParameter_RecordStatus` | String |  |  |
| 11 | `AUBPAY.PARAM.CURR.NO` | `AubpayBillerParameter_CurrNo` | String |  |  |
| 12 | `AUBPAY.PARAM.INPUTTER` | `AubpayBillerParameter_Inputter` |  |  |  |
| 13 | `AUBPAY.PARAM.DATE.TIME` | `AubpayBillerParameter_DateTime` |  |  |  |
| 14 | `AUBPAY.PARAM.AUTHORISER` | `AubpayBillerParameter_Authoriser` | String |  |  |
| 15 | `AUBPAY.PARAM.CO.CODE` | `AubpayBillerParameter_CoCode` | String |  |  |
| 16 | `AUBPAY.PARAM.DEPT.CODE` | `AubpayBillerParameter_DeptCode` | String |  |  |
| 17 | `AUBPAY.PARAM.AUDITOR.CODE` | `AubpayBillerParameter_AuditorCode` | String |  |  |
| 18 | `AUBPAY.PARAM.AUDIT.DATE.TIME` | `AubpayBillerParameter_AuditDateTime` | String |  |  |
