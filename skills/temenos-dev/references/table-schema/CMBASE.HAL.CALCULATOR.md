# CMBASE.HAL.CALCULATOR — Table Schema

> Source: `INSERTS/I_F.CMBASE.HAL.CALCULATOR` in `CMBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMBASE.EXTERNAL.REF.NO` | `CmbaseHalCalculator_ExternalRefNo` | TField |  | This captures or records the reference number of the external application/system |
| 2 | `CMBASE.PURCHASE.PRICE` | `CmbaseHalCalculator_PurchasePrice` | TField |  | The purchase price of the primary collateral |
| 3 | `CMBASE.HOUSING.COMP.LN` | `CmbaseHalCalculator_HousingCompLn` | TField |  | Share of the housing company loan that the applicant is liable |
| 4 | `CMBASE.FAIR.VALUE` | `CmbaseHalCalculator_FairValue` | TField |  | Fair value recorded for the collateral |
| 5 | `CMBASE.PRODUCT.TYPE` | `CmbaseHalCalculator_ProductType` | TField |  | The loan product for which the HAL guarantee is calculated |
| 6 | `CMBASE.REQUESTED.LOAN.AMT` | `CmbaseHalCalculator_RequestedLoanAmt` | TField |  | The requested loan amount applicable. Currently the maximum percentage value applicable for Housing loan is 85% and for ASP Loan and Asp-additional Is 90%. |
| 7 | `CMBASE.COLLATERAL.VAL.PERCENT` | `CmbaseHalCalculator_CollateralValPercent` | TField |  | This is the applicable percentage for the primary collateral |
| 8 | `CMBASE.TRANSFERRED.LOAN` | `CmbaseHalCalculator_TransferredLoan` | TField |  | This field indicates if the loan is a transferred loan |
| 9 | `CMBASE.CALC.METHOD` | `CmbaseHalCalculator_CalcMethod` | TField |  | This field indicates the calculation method. Defaulted to Need based. If the loan is transferred loan, then the calculation method should be Percentage based. |
| 10 | `CMBASE.STATE.GUARANTEE.PERCENT` | `CmbaseHalCalculator_StateGuaranteePercent` | TField |  | This denotes the state guarantee percentage for a loan. |
| 11 | `CMBASE.ORIG.LN.ACC.NO` | `CmbaseHalCalculator_OrigLnAccNo` | TField |  | The field reflects the original loan account number from the bank where it is transferred from |
| 12 | `CMBASE.ORIG.DISB.DATE` | `CmbaseHalCalculator_OrigDisbDate` | TField |  | This field reflects the original disbursement date of the transferred loan. |
| 13 | `CMBASE.MAT.DATE` | `CmbaseHalCalculator_MatDate` | TField |  | This denotes the maturity date of the loan |
| 14 | `CMBASE.COLLATERAL.VALUE` | `CmbaseHalCalculator_CollateralValue` | TField |  | The field pertains to the collateral value vis-�-vis the requested loan amount |
| 15 | `CMBASE.HAL.LOAN.AMT` | `CmbaseHalCalculator_HalLoanAmt` | TField |  | This reflects the HAL loan amount and this is calculated by the system. |
| 16 | `CMBASE.HAL.GUARANTEE.AMT` | `CmbaseHalCalculator_HalGuaranteeAmt` | TField |  | This field derives the HAL guarantee amount |
| 17 | `CMBASE.HAL.GTEE.PORTION.PERCENT` | `CmbaseHalCalculator_HalGteePortionPercent` | TField |  | The field indicates the percentage of HAL guarantee against the HAL loan amount. |
| 18 | `CMBASE.HAL.GTEE.FEE` | `CmbaseHalCalculator_HalGteeFee` | TField |  | This field pertains to the HAL guarantee fee |
| 19 | `CMBASE.ADDL.COLLATERAL.REQD` | `CmbaseHalCalculator_AddlCollateralReqd` | TField |  | The field denotes if additional collateral is required for the loan. |
| 20 | `CMBASE.LOCAL.REF` | `CmbaseHalCalculator_LocalRef` |  |  |  |
| 21 | `CMBASE.RESERVED.1` | `CmbaseHalCalculator_Reserved1` | TField |  | Reserved for future use |
| 22 | `CMBASE.RESERVED.2` | `CmbaseHalCalculator_Reserved2` | TField |  | Reserved for future use |
| 23 | `CMBASE.RESERVED.3` | `CmbaseHalCalculator_Reserved3` | TField |  | Reserved for future use |
| 24 | `CMBASE.RESERVED.4` | `CmbaseHalCalculator_Reserved4` | TField |  | Reserved for future use |
| 25 | `CMBASE.RESERVED.5` | `CmbaseHalCalculator_Reserved5` | TField |  | Reserved for future use |
| 26 | `CMBASE.RESERVED.6` | `CmbaseHalCalculator_Reserved6` | TField |  | Reserved for future use |
| 27 | `CMBASE.RESERVED.7` | `CmbaseHalCalculator_Reserved7` | TField |  | Reserved for future use |
| 28 | `CMBASE.RESERVED.8` | `CmbaseHalCalculator_Reserved8` | TField |  | Reserved for future use |
| 29 | `CMBASE.OVERRIDE` | `CmbaseHalCalculator_Override` |  |  |  |
| 30 | `CMBASE.RECORD.STATUS` | `CmbaseHalCalculator_RecordStatus` | String |  |  |
| 31 | `CMBASE.CURR.NO` | `CmbaseHalCalculator_CurrNo` | String |  |  |
| 32 | `CMBASE.INPUTTER` | `CmbaseHalCalculator_Inputter` |  |  |  |
| 33 | `CMBASE.DATE.TIME` | `CmbaseHalCalculator_DateTime` |  |  |  |
| 34 | `CMBASE.AUTHORISER` | `CmbaseHalCalculator_Authoriser` | String |  |  |
| 35 | `CMBASE.CO.CODE` | `CmbaseHalCalculator_CoCode` | String |  |  |
| 36 | `CMBASE.DEPT.CODE` | `CmbaseHalCalculator_DeptCode` | String |  |  |
| 37 | `CMBASE.AUDITOR.CODE` | `CmbaseHalCalculator_AuditorCode` | String |  |  |
| 38 | `CMBASE.AUDIT.DATE.TIME` | `CmbaseHalCalculator_AuditDateTime` | String |  |  |
