# IS.PAYMENT.DECLARATION — Table Schema

> Source: `INSERTS/I_F.IS.PAYMENT.DECLARATION` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.IPD.DECL.LEVEL` | `IsPaymentDeclaration_DeclLevel` | TField |  | Contains the profit declaration types. The valid types are facility and drawing. |
| 2 | `IS.IPD.ARRANGEMENT` | `IsPaymentDeclaration_Arrangement` | TField |  | Displays the arrangement Reference. The aloowed values are either facility arrangement Id or Drawing arrangement Id. |
| 3 | `IS.IPD.ACCRUAL.START.DATE` | `IsPaymentDeclaration_AccrualStartDate` | TField |  | This field represents the start date of the current interest period. |
| 4 | `IS.IPD.ACCRUAL.END.DATE` | `IsPaymentDeclaration_AccrualEndDate` | TField |  | This field represents the end date of the current interest period. |
| 5 | `IS.IPD.PROFIT.SHARE.PERC` | `IsPaymentDeclaration_ProfitSharePerc` | TField |  | This field denotes the Profit Share percentage. The range must be from 0% to 100% |
| 6 | `IS.IPD.CUSTOMER` | `IsPaymentDeclaration_Customer` | TField |  | Customer id of the drawings / facility arrangement. NO-INPUT Field. |
| 7 | `IS.IPD.PRODUCT` | `IsPaymentDeclaration_Product` | TField |  | Displays the catalogue product id of the drawings / facility arrangement. NO-INPUT Field. |
| 8 | `IS.IPD.CONTRACT.CURRENCY` | `IsPaymentDeclaration_ContractCurrency` | TField |  | Displays the currency of the drawings / facility arrangement. NO-INPUT Field. |
| 9 | `IS.IPD.BOOKING.DATE` | `IsPaymentDeclaration_BookingDate` | TField |  | NO-INPUT Field. Date on which the declaration is recorded. Records TODAY date when creating. |
| 10 | `IS.IPD.VALUE.DATE` | `IsPaymentDeclaration_ValueDate` | TField |  | NO-INPUT Field. Start date of the declaration record. |
| 11 | `IS.IPD.MATURITY.DATE` | `IsPaymentDeclaration_MaturityDate` | TField |  | NO-INPUT Field. Maturity date of the declaration record. |
| 12 | `IS.IPD.AMOUNT` | `IsPaymentDeclaration_Amount` | TField |  | Declared Profit Amount of the drawings. |
| 13 | `IS.IPD.ARRANGEMENT.STATUS` | `IsPaymentDeclaration_ArrangementStatus` | TField |  | Displays the status of the drawings / facility arrangement. NO-INPUT Field. |
| 14 | `IS.IPD.DRAWING.ID` | `IsPaymentDeclaration_DrawingId` |  |  |  |
| 15 | `IS.IPD.DRAWING.ARR.CURRENCY` | `IsPaymentDeclaration_DrawingArrCurrency` |  |  |  |
| 16 | `IS.IPD.PROFIT.ACC.TYPE` | `IsPaymentDeclaration_ProfitAccType` |  |  |  |
| 17 | `IS.IPD.PROFIT.ACC.START.DATE` | `IsPaymentDeclaration_ProfitAccStartDate` |  |  |  |
| 18 | `IS.IPD.PROFIT.ACC.END.DATE` | `IsPaymentDeclaration_ProfitAccEndDate` |  |  |  |
| 19 | `IS.IPD.PROFIT.ACC.AMOUNT` | `IsPaymentDeclaration_ProfitAccAmount` |  |  |  |
| 20 | `IS.IPD.PROFIT.ACC.AMOUNT.FACILITY.CCY` | `IsPaymentDeclaration_ProfitAccAmountFacilityCcy` |  |  |  |
| 21 | `IS.IPD.TOTAL.ACCRUAL.PROFIT.AMT` | `IsPaymentDeclaration_TotalAccrualProfitAmt` | TField |  | This field represents the total accrued amount for the period |
| 22 | `IS.IPD.DECLARED.PROFIT.AMT` | `IsPaymentDeclaration_DeclaredProfitAmt` | TField |  | This field represents the profit amount calculated using the profit share percentage |
| 23 | `IS.IPD.ACC.DIFFERENCE.AMT` | `IsPaymentDeclaration_AccDifferenceAmt` | TField |  | The field denotes the difference between the accrued profit amount and the declared profit amount |
| 24 | `IS.IPD.PROFIT.SHARE.CALC.AMT` | `IsPaymentDeclaration_ProfitShareCalcAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 25 | `IS.IPD.PROFIT.SHARE.AMT` | `IsPaymentDeclaration_ProfitShareAmt` | TField |  | This field displays the profit share amount calculated based on the PROFIT.SHARE.PERC |
| 26 | `IS.IPD.SETTLEMENT.ACCOUNT` | `IsPaymentDeclaration_SettlementAccount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 27 | `IS.IPD.PROFIT.DEC.PL` | `IsPaymentDeclaration_ProfitDecPl` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 28 | `IS.IPD.STMT.NOS` | `IsPaymentDeclaration_StmtNos` |  |  |  |
| 29 | `IS.IPD.RESERVED.4` | `IsPaymentDeclaration_Reserved4` | TField |  |  |
| 30 | `IS.IPD.RESERVED.3` | `IsPaymentDeclaration_Reserved3` | TField |  |  |
| 31 | `IS.IPD.RESERVED.2` | `IsPaymentDeclaration_Reserved2` | TField |  |  |
| 32 | `IS.IPD.RESERVED.1` | `IsPaymentDeclaration_Reserved1` | TField |  |  |
| 33 | `IS.IPD.LOCAL.REF` | `IsPaymentDeclaration_LocalRef` |  |  |  |
| 34 | `IS.IPD.OVERRIDE` | `IsPaymentDeclaration_Override` |  |  |  |
| 35 | `IS.IPD.RECORD.STATUS` | `IsPaymentDeclaration_RecordStatus` | String |  |  |
| 36 | `IS.IPD.CURR.NO` | `IsPaymentDeclaration_CurrNo` | String |  |  |
| 37 | `IS.IPD.INPUTTER` | `IsPaymentDeclaration_Inputter` |  |  |  |
| 38 | `IS.IPD.DATE.TIME` | `IsPaymentDeclaration_DateTime` |  |  |  |
| 39 | `IS.IPD.AUTHORISER` | `IsPaymentDeclaration_Authoriser` | String |  |  |
| 40 | `IS.IPD.CO.CODE` | `IsPaymentDeclaration_CoCode` | String |  |  |
| 41 | `IS.IPD.DEPT.CODE` | `IsPaymentDeclaration_DeptCode` | String |  |  |
| 42 | `IS.IPD.AUDITOR.CODE` | `IsPaymentDeclaration_AuditorCode` | String |  |  |
| 43 | `IS.IPD.AUDIT.DATE.TIME` | `IsPaymentDeclaration_AuditDateTime` | String |  |  |
