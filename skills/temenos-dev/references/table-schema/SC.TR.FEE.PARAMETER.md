# SC.TR.FEE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SC.TR.FEE.PARAMETER` in `SC_ScfTrailerFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TRAIL.DEFAULT.PRODUCT` | `ScTrFeeParameter_DefaultProduct` | TField | Yes | Specifies the default product under which the bank would like to report their PL earned on account of trailer fees. Validation Rules: 4 or 5 Numeric characters. Must exist as a valid CATEGORY code. This is a single value and mandatory field. |
| 2 | `SC.TRAIL.ACCRUAL.METHOD` | `ScTrFeeParameter_AccrualMethod` | TField | No | If this field is set to DAILY, then the trailer fee accrual entries will be raised on a daily basis for all issuers who have an arrangement with the respective customer company. Otherwise the accrual entries will be raised only on the calculation date as per the arrangement of the issuer. Validation Rules: This is a single value and optional field. Only valid value is DAILY. This field cannot be changed from DAILY to Null. |
| 3 | `SC.TRAIL.DAY.BASIS` | `ScTrFeeParameter_DayBasis` | TField | Conditional | This field needs to be set to indicate which day basis has to be used for daily accrual. Validation Rules: This is a single value and optional field. This field becomes mandatory if the field ACCRUAL.METHOD is set to DAILY and change is not allowed in this field once it is set. |
| 4 | `SC.TRAIL.TR.FEE.SUSP.CAT` | `ScTrFeeParameter_TrFeeSuspCat` | TField | Yes | Specifies the suspense category which is treated as a wash account for posting capitalization entry and apportioning of difference amount (if any). Validation Rules: This is a single value and mandatory field. Standard Category field. (Category code from 10000 � 19999) |
| 5 | `SC.TRAIL.TAX.CODE` | `ScTrFeeParameter_TaxCode` |  |  |  |
| 6 | `SC.TRAIL.TAX.PL` | `ScTrFeeParameter_TaxPl` |  |  |  |
| 7 | `SC.TRAIL.INCL.EXCL` | `ScTrFeeParameter_InclExcl` | TField |  | Field to hold values INCLUSIVE or EXCLUSIVE If this is INCLUSIVE, the service tax and other taxes if any, will be included in the trailer fees recovered from the fund house. If this is EXCLUSIVE, the amount received from issuer is only the fees, and no tax is received from issuer. Validation Rules: This field can accept two values INCLUSIVE or EXCLUSIVE |
| 8 | `SC.TRAIL.NO.ROUNDING.ACCRUAL` | `ScTrFeeParameter_NoRoundingAccrual` | TField |  | Options possible in the field are Yes Or Blank If this field is marked as YES, then the Accrued Interest in SC.TRAIL.FEES.EXTRACT and SC.TRAIL.FEES.ARRANGEMENT will be held up to 9 decimals else accruals will be rounded with respect to currency |
| 9 | `SC.TRAIL.AUTODEBIT.REC.ACC` | `ScTrFeeParameter_AutodebitRecAcc` | TField |  | This Field specifies whether to debit the receivable account automatically on the capitalization date or not If this field is set to NO On Capitalization date System will not debit receivable account and credit trailer fees suspense account On Payment when SETTLE.STATUS is �COMPLETE� in SC.TRAIL.FEES.HOLDING, system will debit the receivable account for the actual amount received and credit the trailer fee suspense Validation Rules: Options possible in the field are NO Or Blank Change allowed only when SETTLE.STATUS field is 'COMPLETE' for all existing SC.TRAIL.FEES.HOLDING records |
| 10 | `SC.TRAIL.REIMBURSE.ALLOWED` | `ScTrFeeParameter_ReimburseAllowed` | TField |  | This Field specifies whether Reimbursement of trailer fees is enabled or not If this field is marked as YES On Payment, when SETTLE.STATUS is �COMPLETE� in SC.TRAIL.FEES.HOLDING, then system will prompt to run SC.TRAIL.FEES.ADJUSTMENT service for reimbursement of trailer fees to eligible issuers Validation Rules: Options possible in the field are Yes Or Blank Change not allowed once set to YES |
| 11 | `SC.TRAIL.ACCR.PER.PORT` | `ScTrFeeParameter_AccrPerPort` | TField |  | This Field determines whether the accrual should be done per portfolio or per account officer If the field is set as Yes, system will post the accrual entries per security per portfolio. If this field is blank, the existing functionality of posting the accrual entries per security per account officer will continue Validation Rules: Options possible in the field are YES Or Blank Allowed to input only for New setup of SC.TR.FEE.PARAMETER |
| 12 | `SC.TRAIL.REIMBURSE.INT.CAT` | `ScTrFeeParameter_ReimburseIntCat` | TField |  | Specifies the internal category to which the reimbursement of Trailer fees should be credited. Validation Rules: Should be a valid CATEGORY between 10000...19999 Allowed to input only if REIMBURSE.ALLOWED flag is set to YES. |
| 13 | `SC.TRAIL.RESERVED.2` | `ScTrFeeParameter_Reserved2` | TField |  |  |
| 14 | `SC.TRAIL.RESERVED.1` | `ScTrFeeParameter_Reserved1` | TField |  |  |
| 15 | `SC.TRAIL.LOCAL.REF` | `ScTrFeeParameter_LocalRef` |  |  |  |
| 16 | `SC.TRAIL.RECORD.STATUS` | `ScTrFeeParameter_RecordStatus` | String |  |  |
| 17 | `SC.TRAIL.CURR.NO` | `ScTrFeeParameter_CurrNo` | String |  |  |
| 18 | `SC.TRAIL.INPUTTER` | `ScTrFeeParameter_Inputter` |  |  |  |
| 19 | `SC.TRAIL.DATE.TIME` | `ScTrFeeParameter_DateTime` |  |  |  |
| 20 | `SC.TRAIL.AUTHORISER` | `ScTrFeeParameter_Authoriser` | String |  |  |
| 21 | `SC.TRAIL.CO.CODE` | `ScTrFeeParameter_CoCode` | String |  |  |
| 22 | `SC.TRAIL.DEPT.CODE` | `ScTrFeeParameter_DeptCode` | String |  |  |
| 23 | `SC.TRAIL.AUDITOR.CODE` | `ScTrFeeParameter_AuditorCode` | String |  |  |
| 24 | `SC.TRAIL.AUDIT.DATE.TIME` | `ScTrFeeParameter_AuditDateTime` | String |  |  |
