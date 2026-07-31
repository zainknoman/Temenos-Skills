# TNBASE.FINANCIAL.DETAILS — Table Schema

> Source: `INSERTS/I_F.TNBASE.FINANCIAL.DETAILS` in `TNBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNBASE.FINANCIAL.DETAILS.FORM.TYPE` | `TnbaseFinancialDetails_FormType` | TField |  | Denotes the type of financial record |
| 2 | `TNBASE.FINANCIAL.DETAILS.CUSTOMER` | `TnbaseFinancialDetails_Customer` | TField |  | This is the T24 Customer ID |
| 3 | `TNBASE.FINANCIAL.DETAILS.TOTAL.RESERVED.AMT` | `TnbaseFinancialDetails_TotalReservedAmt` | TField |  | Total reserved amount |
| 4 | `TNBASE.FINANCIAL.DETAILS.RESERVE.TRANS.REF` | `TnbaseFinancialDetails_ReserveTransRef` |  |  |  |
| 5 | `TNBASE.FINANCIAL.DETAILS.SETT.TRANS.REF` | `TnbaseFinancialDetails_SettTransRef` |  |  |  |
| 6 | `TNBASE.FINANCIAL.DETAILS.ELIGIBLE.AMT` | `TnbaseFinancialDetails_EligibleAmt` | TField |  | Eligible amount for AVA record |
| 7 | `TNBASE.FINANCIAL.DETAILS.TOTAL.USED.AMT` | `TnbaseFinancialDetails_TotalUsedAmt` | TField |  | Total used amount |
| 8 | `TNBASE.FINANCIAL.DETAILS.AVAILABLE.AMT` | `TnbaseFinancialDetails_AvailableAmt` | TField |  | Available amount after Utilisation |
| 9 | `TNBASE.FINANCIAL.DETAILS.CARRY.AMT` | `TnbaseFinancialDetails_CarryAmt` | TField |  | Amount over respective Limit |
| 10 | `TNBASE.FINANCIAL.DETAILS.ALLOWED.AMT` | `TnbaseFinancialDetails_AllowedAmt` | TField |  | Allowed amount for AVA record |
| 11 | `TNBASE.FINANCIAL.DETAILS.ELIGIBLE.AMT.BFR.CO` | `TnbaseFinancialDetails_EligibleAmtBfrCo` | TField |  | Calculated Eligible amount before carry over |
| 12 | `TNBASE.FINANCIAL.DETAILS.CARRY.AMT.REQD` | `TnbaseFinancialDetails_CarryAmtReqd` | TField |  | Calculated required Carry amount |
| 13 | `TNBASE.FINANCIAL.DETAILS.CARRY.AMT.AMEND` | `TnbaseFinancialDetails_CarryAmtAmend` | TField |  | Calcuated Carry amount for amendment |
| 14 | `TNBASE.FINANCIAL.DETAILS.CARRY.AMT.UTL` | `TnbaseFinancialDetails_CarryAmtUtl` | TField |  | Calculated Carry amount utilised |
| 15 | `TNBASE.FINANCIAL.DETAILS.TAX.REFERENCE` | `TnbaseFinancialDetails_TaxReference` | TField |  | Reference number of Tax declaration. |
| 16 | `TNBASE.FINANCIAL.DETAILS.TAX.DECLARATION.DT` | `TnbaseFinancialDetails_TaxDeclarationDt` | TField |  | Year of Tax declaration. |
| 17 | `TNBASE.FINANCIAL.DETAILS.CONTRACT.AMOUNT.LCY` | `TnbaseFinancialDetails_ContractAmountLcy` | TField |  | Contract amount in local currency |
| 18 | `TNBASE.FINANCIAL.DETAILS.INC.DEC.AMT` | `TnbaseFinancialDetails_IncDecAmt` | TField |  | Amount of Usage/Supply |
| 19 | `TNBASE.FINANCIAL.DETAILS.INC.DEC.DATE` | `TnbaseFinancialDetails_IncDecDate` | TField |  | Date of Usage/Supply activity |
| 20 | `TNBASE.FINANCIAL.DETAILS.CLEARANCE.IND` | `TnbaseFinancialDetails_ClearanceInd` | TField |  | Clearance Indicator |
| 21 | `TNBASE.FINANCIAL.DETAILS.CBT.CLEARANCE.IND` | `TnbaseFinancialDetails_CbtClearanceInd` | TField |  | Central bank Clearance Indicator |
| 22 | `TNBASE.FINANCIAL.DETAILS.SETT.AMT.LCY` | `TnbaseFinancialDetails_SettAmtLcy` | TField |  | Settlement amount in local currency |
| 23 | `TNBASE.FINANCIAL.DETAILS.REC.STATUS` | `TnbaseFinancialDetails_RecStatus` | TField |  | Reflects the latest status of AVA record |
| 24 | `TNBASE.FINANCIAL.DETAILS.AUTH.AMT.CBT` | `TnbaseFinancialDetails_AuthAmtCbt` | TField |  | Reflects the Amount Authorized by CBT for any of the Business Types |
| 25 | `TNBASE.FINANCIAL.DETAILS.CUMULATIVE.USED.AMT` | `TnbaseFinancialDetails_CumulativeUsedAmt` | TField |  | This is the Amount which indicates the total used amount at any given point of time. It is applicable for all the Business Types. The amount is set to ZERO at the time of Renewal. |
| 26 | `TNBASE.FINANCIAL.DETAILS.EXPORT.REVENUE` | `TnbaseFinancialDetails_ExportRevenue` | TField |  | This field contains the Export Revenue on which EXPORT.PERCENT is applied. For manual supply of LIMIT this filed is auto-calculated based on the EXPORT.PERCENT. It is applicable only for Business Type EXPORTER. |
| 27 | `TNBASE.FINANCIAL.DETAILS.AVL.OTHER.EXPENSES` | `TnbaseFinancialDetails_AvlOtherExpenses` | TField |  | This field stores the Available other expense for the file |
| 28 | `TNBASE.FINANCIAL.DETAILS.USED.OTHER.EXPENSES` | `TnbaseFinancialDetails_UsedOtherExpenses` | TField |  | This field stores the other expensed used for the file. |
| 29 | `TNBASE.FINANCIAL.DETAILS.MON.EXP.MONTH` | `TnbaseFinancialDetails_MonExpMonth` |  |  |  |
| 30 | `TNBASE.FINANCIAL.DETAILS.MON.EXP.AMT` | `TnbaseFinancialDetails_MonExpAmt` |  |  |  |
| 31 | `TNBASE.FINANCIAL.DETAILS.MON.EXP.USED` | `TnbaseFinancialDetails_MonExpUsed` |  |  |  |
| 32 | `TNBASE.FINANCIAL.DETAILS.MON.EXP.BAL` | `TnbaseFinancialDetails_MonExpBal` |  |  |  |
| 33 | `TNBASE.FINANCIAL.DETAILS.TOTAL.MON.EXP.YEAR` | `TnbaseFinancialDetails_TotalMonExpYear` | TField |  |  |
| 34 | `TNBASE.FINANCIAL.DETAILS.LIV.EXP.BY.STUDENT` | `TnbaseFinancialDetails_LivExpByStudent` | TField |  | This field stores the living expenses amount which has to be paid by the student. |
| 35 | `TNBASE.FINANCIAL.DETAILS.TOTAL.FILE.TERM.AMT` | `TnbaseFinancialDetails_TotalFileTermAmt` | TField |  | This field stores the Total Registration Fees allowed for the Course |
| 36 | `TNBASE.FINANCIAL.DETAILS.USED.FILE.TERM.AMT` | `TnbaseFinancialDetails_UsedFileTermAmt` | TField |  | This field stores the Registration Fees used for the course |
| 37 | `TNBASE.FINANCIAL.DETAILS.UNAUTH.UTIL.AMT` | `TnbaseFinancialDetails_UnauthUtilAmt` | TField |  | This field identifies the USAGE balance which is not yet Authorized. |
| 38 | `TNBASE.FINANCIAL.DETAILS.CARRY.FWD.USED.AMT` | `TnbaseFinancialDetails_CarryFwdUsedAmt` |  |  |  |
| 39 | `TNBASE.FINANCIAL.DETAILS.RETROCEDED.AMT` | `TnbaseFinancialDetails_RetrocededAmt` |  |  |  |
| 40 | `TNBASE.FINANCIAL.DETAILS.UNAUTH.SCH.OTH.EXP` | `TnbaseFinancialDetails_UnauthSchOthExp` | TField |  | This Field holds the Unauthorized amount for Other Expense type for the respective schooling file. |
| 41 | `TNBASE.FINANCIAL.DETAILS.UNAUTH.SCH.REG.FEE` | `TnbaseFinancialDetails_UnauthSchRegFee` | TField |  | This Field holds the Unauthorized amount for Registration Fee Expense type for the respective schooling file. |
