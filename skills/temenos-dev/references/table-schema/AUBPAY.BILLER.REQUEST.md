# AUBPAY.BILLER.REQUEST — Table Schema

> Source: `INSERTS/I_F.AUBPAY.BILLER.REQUEST` in `AUBPAY_BillerManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BILLER.REQ.REQUEST.TYPE` | `AubpayBillerRequest_RequestType` | TField |  | Type of Request/Change Type. Possible values are ADD (action of interest), UPDATE, TRANSFER, CLOSE |
| 2 | `BILLER.REQ.BILLER.SHORT.NAME` | `AubpayBillerRequest_BillerShortName` | TField |  | The Short name for the Biller |
| 3 | `BILLER.REQ.BILLER.LONG.NAME` | `AubpayBillerRequest_BillerLongName` | TField |  | The Long name for the Biller |
| 4 | `BILLER.REQ.MAST.BILLER.IND` | `AubpayBillerRequest_MastBillerInd` | TField |  | Indicator of whether the Biller is a Master Biller (true) or not(false). |
| 5 | `BILLER.REQ.MAST.BILLER.CODE` | `AubpayBillerRequest_MastBillerCode` | TField |  | Biller Code of Cuscal client who is initiating this request. (to be only sent to BPAY while adding a MasterBiller) |
| 6 | `BILLER.REQ.BILLER.INST.CODE` | `AubpayBillerRequest_BillerInstCode` | TField |  | Three character Institution Code (IC) of the Biller institution. |
| 7 | `BILLER.REQ.PAYMENT.METHOD` | `AubpayBillerRequest_PaymentMethod` |  |  |  |
| 8 | `BILLER.REQ.MAX.AMOUNT` | `AubpayBillerRequest_MaxAmount` |  |  |  |
| 9 | `BILLER.REQ.MIN.AMOUNT` | `AubpayBillerRequest_MinAmount` |  |  |  |
| 10 | `BILLER.REQ.CUST.REF.NAME` | `AubpayBillerRequest_CustRefName` | TField |  | This field will contain the value of TDS that is against the respective� Interest payment |
| 11 | `BILLER.REQ.CUST.REF.LOCATION` | `AubpayBillerRequest_CustRefLocation` | TField |  | This field will contains customer reference location |
| 12 | `BILLER.REQ.VALID.LENGTH` | `AubpayBillerRequest_ValidLength` |  |  |  |
| 13 | `BILLER.REQ.CRN.POSITION` | `AubpayBillerRequest_CrnPosition` |  |  |  |
| 14 | `BILLER.REQ.FIXED.VALUE` | `AubpayBillerRequest_FixedValue` |  |  |  |
| 15 | `BILLER.REQ.VAR.CRN.IND` | `AubpayBillerRequest_VarCrnInd` | TField |  | Name of the BPAY written validation rule indicator used to check the Customer Reference Number for this Biller. |
| 16 | `BILLER.REQ.VAL.RULE.NAME` | `AubpayBillerRequest_ValRuleName` | TField |  | Name of the BPAY written validation rule name used to check the Customer Reference Number for this Biller. |
| 17 | `BILLER.REQ.CHK.DIGIT.RULE.NAME` | `AubpayBillerRequest_ChkDigitRuleName` | TField |  | Name of the check digit rule to be applied to the CRN, where the rule is a pre-defined rule supported by BPAY. |
| 18 | `BILLER.REQ.CUSTOM.CHK.DIGIT.RULE` | `AubpayBillerRequest_CustomChkDigitRule` | TField |  | Check digit rule to be applied to the CRN, when it's a pre defined rule, but not one of the common ones coveredby standardCheckDigitRule. |
| 19 | `BILLER.REQ.CHK.DIGIT.LENGTH` | `AubpayBillerRequest_ChkDigitLength` | TField |  | Number of digits used for the check digit. |
| 20 | `BILLER.REQ.CUSTOM.CRN.POSITION` | `AubpayBillerRequest_CustomCrnPosition` |  |  |  |
| 21 | `BILLER.REQ.CUSTOM.CRN.WEIGHT` | `AubpayBillerRequest_CustomCrnWeight` |  |  |  |
| 22 | `BILLER.REQ.START.FROM` | `AubpayBillerRequest_StartFrom` | TField |  | Side of the CRN from which the weights are to apply. (Left, Right) |
| 23 | `BILLER.REQ.ADD.RESULT.DIGITS` | `AubpayBillerRequest_AddResultDigits` | TField |  | Defines how the digits of each weight calculation should be added (added once, repeatedly, truncated to units orkeep result) |
| 24 | `BILLER.REQ.DIVIDE.RESULT.BY` | `AubpayBillerRequest_DivideResultBy` | TField |  | Number by which to divide the result. Value must be 0 - 99. |
| 25 | `BILLER.REQ.SUBTRACT.RESULT.FROM` | `AubpayBillerRequest_SubtractResultFrom` | TField |  | Number from which to subtract the result. Value must be 0 - 99. |
| 26 | `BILLER.REQ.KEEP.ZERO` | `AubpayBillerRequest_KeepZero` | TField |  | Defines whether to keep a zero remainder as the check digit (true) or not (false). |
| 27 | `BILLER.REQ.ACTIVATION.DATE` | `AubpayBillerRequest_ActivationDate` | TField |  | Date of when the new master/biller should be activated.Format YYYY-MM-DD |
| 28 | `BILLER.REQ.PUBLISH.BMF.IMMEDIATE` | `AubpayBillerRequest_PublishBmfImmediate` | TField |  | Indicates whether the new Biller/Biller Change is to be published to the Biller Master File immediately onapproval, or published on the activation date only. |
| 29 | `BILLER.REQ.ANZSIC.INDUSTRY.CODE` | `AubpayBillerRequest_AnzsicIndustryCode` | TField |  | The ANZSIC (Industry) code of the Biller. |
| 30 | `BILLER.REQ.CLIENT.ID` | `AubpayBillerRequest_ClientId` | TField |  | Client/Login ID who submitted the request |
| 31 | `BILLER.REQ.REQUEST.STATUS` | `AubpayBillerRequest_RequestStatus` | TField |  | Current Status of Change request |
| 32 | `BILLER.REQ.CLOSURE.REASON` | `AubpayBillerRequest_ClosureReason` | TField | Yes | Reason for closure of the Biller. Mandatory if the change is a closure. Else ignored. |
| 33 | `BILLER.REQ.BILLER.STATUS` | `AubpayBillerRequest_BillerStatus` | TField |  | Current Status of the Biller. Valid status are 'RESERVED', 'ACTIVE','CLOSED' |
| 34 | `BILLER.REQ.BPAY.ERROR.DESCRIPTION` | `AubpayBillerRequest_BpayErrorDescription` | TField |  | Error Description from BPAY |
| 35 | `BILLER.REQ.BPAY.ERR.CODE` | `AubpayBillerRequest_BpayErrCode` |  |  |  |
| 36 | `BILLER.REQ.BPAY.ERR.MSG` | `AubpayBillerRequest_BpayErrMsg` |  |  |  |
| 37 | `BILLER.REQ.BPAY.ERR.FIELD` | `AubpayBillerRequest_BpayErrField` |  |  |  |
| 38 | `BILLER.REQ.LOCAL.REF` | `AubpayBillerRequest_LocalRef` |  |  |  |
| 39 | `BILLER.REQ.OVERRIDE` | `AubpayBillerRequest_Override` |  |  |  |
| 40 | `BILLER.REQ.RECORD.STATUS` | `AubpayBillerRequest_RecordStatus` | String |  |  |
| 41 | `BILLER.REQ.CURR.NO` | `AubpayBillerRequest_CurrNo` | String |  |  |
| 42 | `BILLER.REQ.INPUTTER` | `AubpayBillerRequest_Inputter` |  |  |  |
| 43 | `BILLER.REQ.DATE.TIME` | `AubpayBillerRequest_DateTime` |  |  |  |
| 44 | `BILLER.REQ.AUTHORISER` | `AubpayBillerRequest_Authoriser` | String |  |  |
| 45 | `BILLER.REQ.CO.CODE` | `AubpayBillerRequest_CoCode` | String |  |  |
| 46 | `BILLER.REQ.DEPT.CODE` | `AubpayBillerRequest_DeptCode` | String |  |  |
| 47 | `BILLER.REQ.AUDITOR.CODE` | `AubpayBillerRequest_AuditorCode` | String |  |  |
| 48 | `BILLER.REQ.AUDIT.DATE.TIME` | `AubpayBillerRequest_AuditDateTime` | String |  |  |
