# AUBPAY.BILLER — Table Schema

> Source: `INSERTS/I_F.AUBPAY.BILLER` in `AUBPAY_BillerManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUBPAY.BILLER.BILLER.SHORT.NAME` | `AubpayBiller_BillerShortName` | TField |  | The Short name for the Biller |
| 2 | `AUBPAY.BILLER.BILLER.LONG.NAME` | `AubpayBiller_BillerLongName` | TField |  | The Long name for the Biller |
| 3 | `AUBPAY.BILLER.MASTER.BILLER.CODE` | `AubpayBiller_MasterBillerCode` | TField |  |  |
| 4 | `AUBPAY.BILLER.MAST.BILLER.IND` | `AubpayBiller_MastBillerInd` | TField |  | Indicator of whether the Biller is a Master Biller (true) or not(false). |
| 5 | `AUBPAY.BILLER.BILLER.INST.CODE` | `AubpayBiller_BillerInstCode` | TField |  | Three character Institution Code (IC) of the Biller institution. |
| 6 | `AUBPAY.BILLER.LAST.CHANGE.DATE` | `AubpayBiller_LastChangeDate` | TField |  | Last modified date of the biller template |
| 7 | `AUBPAY.BILLER.PAYMENT.METHOD` | `AubpayBiller_PaymentMethod` |  |  |  |
| 8 | `AUBPAY.BILLER.MAX.AMOUNT` | `AubpayBiller_MaxAmount` |  |  |  |
| 9 | `AUBPAY.BILLER.MIN.AMOUNT` | `AubpayBiller_MinAmount` |  |  |  |
| 10 | `AUBPAY.BILLER.CUST.REF.NAME` | `AubpayBiller_CustRefName` | TField |  | This field will contain the value of TDS that is against the respective� Interest payment |
| 11 | `AUBPAY.BILLER.CUST.REF.LOCATION` | `AubpayBiller_CustRefLocation` | TField |  | This field will contains customer reference location |
| 12 | `AUBPAY.BILLER.VALID.LENGTH` | `AubpayBiller_ValidLength` |  |  |  |
| 13 | `AUBPAY.BILLER.CRN.POSITION` | `AubpayBiller_CrnPosition` |  |  |  |
| 14 | `AUBPAY.BILLER.FIXED.VALUE` | `AubpayBiller_FixedValue` |  |  |  |
| 15 | `AUBPAY.BILLER.VAR.CRN.IND` | `AubpayBiller_VarCrnInd` | TField |  | Name of the BPAY written validation rule indicator used to check the Customer Reference Number for this Biller. |
| 16 | `AUBPAY.BILLER.VAL.RULE.NAME` | `AubpayBiller_ValRuleName` | TField |  | Name of the BPAY written validation rule name used to check the Customer Reference Number for this Biller. |
| 17 | `AUBPAY.BILLER.CHK.DIGIT.RULE.NAME` | `AubpayBiller_ChkDigitRuleName` | TField |  | Name of the check digit rule to be applied to the CRN, where the rule is a pre-defined rule supported by BPAY. |
| 18 | `AUBPAY.BILLER.CUSTOM.CHK.DIGIT.RULE` | `AubpayBiller_CustomChkDigitRule` | TField |  | Check digit rule to be applied to the CRN, when it's a pre defined rule, but not one of the common ones covered by standardCheckDigitRule. |
| 19 | `AUBPAY.BILLER.CHK.DIGIT.LENGTH` | `AubpayBiller_ChkDigitLength` | TField |  | Number of digits used for the check digit. |
| 20 | `AUBPAY.BILLER.CUSTOM.CRN.POSITION` | `AubpayBiller_CustomCrnPosition` |  |  |  |
| 21 | `AUBPAY.BILLER.CUSTOM.CRN.WEIGHT` | `AubpayBiller_CustomCrnWeight` |  |  |  |
| 22 | `AUBPAY.BILLER.START.FROM` | `AubpayBiller_StartFrom` | TField |  | Side of the CRN from which the weights are to apply. (Left, Right) |
| 23 | `AUBPAY.BILLER.ADD.RESULT.DIGITS` | `AubpayBiller_AddResultDigits` | TField |  | Defines how the digits of each weight calculation should be added (added once, repeatedly, truncated to units or keep result) |
| 24 | `AUBPAY.BILLER.DIVIDE.RESULT.BY` | `AubpayBiller_DivideResultBy` | TField |  | Number by which to divide the result. Value must be 0 - 99. |
| 25 | `AUBPAY.BILLER.SUBTRACT.RESULT.FROM` | `AubpayBiller_SubtractResultFrom` | TField |  | Number from which to subtract the result. Value must be 0 - 99. |
| 26 | `AUBPAY.BILLER.KEEP.ZERO` | `AubpayBiller_KeepZero` | TField |  | Defines whether to keep a zero remainder as the check digit (true) or not (false). |
| 27 | `AUBPAY.BILLER.ACTIVATED.DATE` | `AubpayBiller_ActivatedDate` | TField |  |  |
| 28 | `AUBPAY.BILLER.ANZSIC.INDUSTRY.CODE` | `AubpayBiller_AnzsicIndustryCode` | TField |  | The ANZSIC (Industry) code of the Biller. |
| 29 | `AUBPAY.BILLER.CLOSURE.REASON` | `AubpayBiller_ClosureReason` | TField | Yes | Reason for closure of the Biller. Mandatory if the change is a closure. Else ignored. |
| 30 | `AUBPAY.BILLER.BILLER.STATUS` | `AubpayBiller_BillerStatus` | TField |  | Current Status of the Biller. Valid status are 'RESERVED', 'ACTIVE','CLOSED' |
| 31 | `AUBPAY.BILLER.LOCAL.REF` | `AubpayBiller_LocalRef` |  |  |  |
| 32 | `AUBPAY.BILLER.OVERRIDE` | `AubpayBiller_Override` |  |  |  |
| 33 | `AUBPAY.BILLER.RECORD.STATUS` | `AubpayBiller_RecordStatus` | String |  |  |
| 34 | `AUBPAY.BILLER.CURR.NO` | `AubpayBiller_CurrNo` | String |  |  |
| 35 | `AUBPAY.BILLER.INPUTTER` | `AubpayBiller_Inputter` |  |  |  |
| 36 | `AUBPAY.BILLER.DATE.TIME` | `AubpayBiller_DateTime` |  |  |  |
| 37 | `AUBPAY.BILLER.AUTHORISER` | `AubpayBiller_Authoriser` | String |  |  |
| 38 | `AUBPAY.BILLER.CO.CODE` | `AubpayBiller_CoCode` | String |  |  |
| 39 | `AUBPAY.BILLER.DEPT.CODE` | `AubpayBiller_DeptCode` | String |  |  |
| 40 | `AUBPAY.BILLER.AUDITOR.CODE` | `AubpayBiller_AuditorCode` | String |  |  |
| 41 | `AUBPAY.BILLER.AUDIT.DATE.TIME` | `AubpayBiller_AuditDateTime` | String |  |  |
