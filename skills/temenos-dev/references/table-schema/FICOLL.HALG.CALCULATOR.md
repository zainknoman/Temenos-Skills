# FICOLL.HALG.CALCULATOR — Table Schema

> Source: `INSERTS/I_F.FICOLL.HALG.CALCULATOR` in `FICOLL_GuarantiaGuarantee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.HALGCALCULATOR.CUSTOMER.ID` | `FicollHalgCalculator_CustomerId` | TField |  | Customer Id or SSN Bussiness Id. |
| 2 | `FICOLL.HALGCALCULATOR.EXTERNAL.REFERENCE` | `FicollHalgCalculator_ExternalReference` | TField |  | OA Dossier number to be inputted. |
| 3 | `FICOLL.HALGCALCULATOR.CALCULATION.DATE` | `FicollHalgCalculator_CalculationDate` | TField |  | HALG calculation date. |
| 4 | `FICOLL.HALGCALCULATOR.HOUSE.PURPOSE` | `FicollHalgCalculator_HousePurpose` | TField |  | House Purpose options Living or Investment. |
| 5 | `FICOLL.HALGCALCULATOR.MUNICIPAL.NAME` | `FicollHalgCalculator_MunicipalName` | TField |  | Municipal Name and Code. |
| 6 | `FICOLL.HALGCALCULATOR.RISK.AREA.GROUP` | `FicollHalgCalculator_RiskAreaGroup` | TField |  | Based on parameterization in NORCUS.MUNICIPAL.CODE system auto populate the value. |
| 7 | `FICOLL.HALGCALCULATOR.MAX.GTEE.AMT` | `FicollHalgCalculator_MaxGteeAmt` | TField |  | Maximum guarantee amount for the property. Based on the purpose of housing property the amount will be defaulted. |
| 8 | `FICOLL.HALGCALCULATOR.PURCHASE.PRICE` | `FicollHalgCalculator_PurchasePrice` | TField |  | Purchase price of the house to be input. |
| 9 | `FICOLL.HALGCALCULATOR.MAX.LOAN.AMT` | `FicollHalgCalculator_MaxLoanAmt` | TField |  | Maximum Loan amount for the property. Based on the purpose of housing property the amount will be defaulted. |
| 10 | `FICOLL.HALGCALCULATOR.LOAN.AMT` | `FicollHalgCalculator_LoanAmt` | TField |  | Loan amount of the property to be input. |
| 11 | `FICOLL.HALGCALCULATOR.EXECUTION.VALUE` | `FicollHalgCalculator_ExecutionValue` | TField |  | Execution value for the purchasing property. |
| 12 | `FICOLL.HALGCALCULATOR.MAX.INT.GARANTIA.VALUE` | `FicollHalgCalculator_MaxIntGarantiaValue` | TField |  | Maximum Garantia amount for the property. |
| 13 | `FICOLL.HALGCALCULATOR.GARANTIA.VALUE` | `FicollHalgCalculator_GarantiaValue` | TField |  | Garantia amount provided for the purchasing property. |
| 14 | `FICOLL.HALGCALCULATOR.COLLATERAL.SHORTFALL` | `FicollHalgCalculator_CollateralShortfall` | TField |  | Any short fall in the Collateral. |
| 15 | `FICOLL.HALGCALCULATOR.GUARANTEED.PECT.LOAN` | `FicollHalgCalculator_GuaranteedPectLoan` | TField |  | Guaranteed percentage for the loan amount. |
| 16 | `FICOLL.HALGCALCULATOR.TOTAL.COST.GETE.PCT` | `FicollHalgCalculator_TotalCostGetePct` | TField |  | Garantia cost percentage value is fetched based on parameterization in FICOLL.GARANTIA.INTERNAL.PARAM table. |
| 17 | `FICOLL.HALGCALCULATOR.TOTAL.COST.GETE.AMT` | `FicollHalgCalculator_TotalCostGeteAmt` | TField |  | Garantia cost to be provided to guarantee. |
| 18 | `FICOLL.HALGCALCULATOR.GTEE.SHARE.COST.AMT` | `FicollHalgCalculator_GteeShareCostAmt` | TField |  | Garantia portion of charge on the Guarantee cost. |
| 19 | `FICOLL.HALGCALCULATOR.MAX.BANK.GTEE.COST.AMT` | `FicollHalgCalculator_MaxBankGteeCostAmt` | TField |  | Maximum bank portion on the Garantia cost. |
| 20 | `FICOLL.HALGCALCULATOR.BANK.GTEE.COST.AMT` | `FicollHalgCalculator_BankGteeCostAmt` | TField |  | Bank portion on the Garantia cost. |
| 21 | `FICOLL.HALGCALCULATOR.BANK.GTEE.COST.PCT` | `FicollHalgCalculator_BankGteeCostPct` | TField |  | Bank portion on the Garantia cost in percentage. |
| 22 | `FICOLL.HALGCALCULATOR.CALC.RISK.VALUE` | `FicollHalgCalculator_CalcRiskValue` | TField |  | The risk value of Garantia guarantee loan. |
| 23 | `FICOLL.HALGCALCULATOR.RISK.AREA.PCT` | `FicollHalgCalculator_RiskAreaPct` | TField |  | The risk area percentage parameterized in FICOLL.GARANTIA.INTERNAL.PARAM table. |
| 24 | `FICOLL.HALGCALCULATOR.RISK.AREA.CODE` | `FicollHalgCalculator_RiskAreaCode` | TField |  | The risk area code parameterized in FICOLL.GARANTIA.INTERNAL.PARAM table. |
| 25 | `FICOLL.HALGCALCULATOR.LOCAL.REF` | `FicollHalgCalculator_LocalRef` |  |  |  |
| 26 | `FICOLL.HALGCALCULATOR.OVERRIDE` | `FicollHalgCalculator_Override` |  |  |  |
| 27 | `FICOLL.HALGCALCULATOR.RECORD.STATUS` | `FicollHalgCalculator_RecordStatus` | String |  |  |
| 28 | `FICOLL.HALGCALCULATOR.CURR.NO` | `FicollHalgCalculator_CurrNo` | String |  |  |
| 29 | `FICOLL.HALGCALCULATOR.INPUTTER` | `FicollHalgCalculator_Inputter` |  |  |  |
| 30 | `FICOLL.HALGCALCULATOR.DATE.TIME` | `FicollHalgCalculator_DateTime` |  |  |  |
| 31 | `FICOLL.HALGCALCULATOR.AUTHORISER` | `FicollHalgCalculator_Authoriser` | String |  |  |
| 32 | `FICOLL.HALGCALCULATOR.CO.CODE` | `FicollHalgCalculator_CoCode` | String |  |  |
| 33 | `FICOLL.HALGCALCULATOR.DEPT.CODE` | `FicollHalgCalculator_DeptCode` | String |  |  |
| 34 | `FICOLL.HALGCALCULATOR.AUDITOR.CODE` | `FicollHalgCalculator_AuditorCode` | String |  |  |
| 35 | `FICOLL.HALGCALCULATOR.AUDIT.DATE.TIME` | `FicollHalgCalculator_AuditDateTime` | String |  |  |
