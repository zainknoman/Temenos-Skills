# INVESTMENT.PROGRAM — Table Schema

> Source: `INSERTS/I_F.INVESTMENT.PROGRAM` in `SC_ScoPortfolioMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.INV.DESCRIPTION` | `InvestmentProgram_Description` |  |  |  |
| 2 | `SC.INV.SHORT.DESCR` | `InvestmentProgram_ShortDescr` |  |  |  |
| 3 | `SC.INV.POLICY.PARAMETER` | `InvestmentProgram_PolicyParameter` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 11 characters may be entered. Must be the key to a valid entry on the POLICY.PARAMETER file. |
| 4 | `SC.INV.MATRIX` | `InvestmentProgram_Matrix` | TField |  | The matrix field links the investment program to an investment matrix. The matrix sets the market segment weightings of the strategy being followed by the investment program. This matrix is used by the portfolio modelling functionality to rebalance a portfolio in line with the objectives. The matrix should be specifically matched with the investment objectives of the strategy and accordingly will Standard T24 alphanumeric field. Validation Rules: Input only allowed if the Asset Management product is install. Must be the key to a valid entry on the AM.MATRIX file. |
| 5 | `SC.INV.INV.OBJECTIVE` | `InvestmentProgram_InvObjective` | TField |  | Standard T24 alphanumeric field. Validation Rules: Must be the key to a valid entry on the AM.INVESTMENT.OBJECTIVE file. Input only allowed if the Asset Management product is install. |
| 6 | `SC.INV.CURRENCY` | `InvestmentProgram_Currency` | TField |  | Standard T24 alphanumeric field. Validation Rules: Must be the key to a valid entry on the CURRENCY file. Input only allowed if the Asset Management product is install. |
| 7 | `SC.INV.SIZING` | `InvestmentProgram_Sizing` | TField |  | Standard T24 alphanumeric field. Validation Rules: Must be the key to a valid entry on the AM.SIZING file. Input only allowed if the Asset Management product is install. |
| 8 | `SC.INV.RIGHTS.TYPE` | `InvestmentProgram_RightsType` |  |  |  |
| 9 | `SC.INV.RIGHTS.DOMICILE` | `InvestmentProgram_RightsDomicile` |  |  |  |
| 10 | `SC.INV.RIGHTS.CCY` | `InvestmentProgram_RightsCcy` |  |  |  |
| 11 | `SC.INV.RIGHTS` | `InvestmentProgram_Rights` |  |  |  |
| 12 | `SC.INV.STOCK.CASH.TYPE` | `InvestmentProgram_StockCashType` |  |  |  |
| 13 | `SC.INV.STOCK.CASH.DOM` | `InvestmentProgram_StockCashDom` |  |  |  |
| 14 | `SC.INV.STOCK.CASH.CCY` | `InvestmentProgram_StockCashCcy` |  |  |  |
| 15 | `SC.INV.STOCK.CASH` | `InvestmentProgram_StockCash` |  |  |  |
| 16 | `SC.INV.REINVEST.TYPE` | `InvestmentProgram_ReinvestType` |  |  |  |
| 17 | `SC.INV.REINVEST.DOM` | `InvestmentProgram_ReinvestDom` |  |  |  |
| 18 | `SC.INV.REINVEST.CCY` | `InvestmentProgram_ReinvestCcy` |  |  |  |
| 19 | `SC.INV.REINVEST.INCOME` | `InvestmentProgram_ReinvestIncome` |  |  |  |
| 20 | `SC.INV.SELL.LOTS.TYPE` | `InvestmentProgram_SellLotsType` |  |  |  |
| 21 | `SC.INV.SELL.LOTS.DOM` | `InvestmentProgram_SellLotsDom` |  |  |  |
| 22 | `SC.INV.SELL.LOTS.CCY` | `InvestmentProgram_SellLotsCcy` |  |  |  |
| 23 | `SC.INV.SELL.ODD.LOTS` | `InvestmentProgram_SellOddLots` |  |  |  |
| 24 | `SC.INV.CCY.MATRIX` | `InvestmentProgram_CcyMatrix` | TField |  | This field defines the matrix in the AM.MATRIX application that will be used to rebalance the cash positions in an investment program. The currency re-balancing function will generate spot FX transactions switching cash from 1 account to another based on the absolute weightings defined in the matrix. Validation Rules: |
| 25 | `SC.INV.HDG.MATRIX` | `InvestmentProgram_HdgMatrix` | TField |  | This field defines the matrix in the AM.MATRIX application that will be used to hedge a currency position in a a portfolio linked to this investment program. The hedging re-balancing function will generate forward FX transactions based on a pivot currency and 1 other selected currency and re-balance the hedging position in line with the matrix objectives. Multiple FX transactions can be generated simply by running the re-balancing process but changing the alternate and/or pivot currency. Validation Rules: |
| 26 | `SC.INV.PF.FEES.TYPE` | `InvestmentProgram_PfFeesType` | TField |  | It should be a valid AM.PF.FEES.TYPE record. |
| 27 | `SC.INV.CALC.RISK.CLASS` | `InvestmentProgram_CalcRiskClass` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 28 | `SC.INV.COMMENTARY.SUMMARY` | `InvestmentProgram_CommentarySummary` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 29 | `SC.INV.COMMENTARY.DETAIL` | `InvestmentProgram_CommentaryDetail` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 30 | `SC.INV.RANKING` | `InvestmentProgram_Ranking` | TField |  | This Field Specifies allowed risk level for an investment program This Field is linked to EB.LOOKUP with ID as RISK.LEVEL* |
| 31 | `SC.INV.CREDIT.POLICY` | `InvestmentProgram_CreditPolicy` | TField |  |  |
| 32 | `SC.INV.LOCAL.REF` | `InvestmentProgram_LocalRef` |  |  |  |
| 33 | `SC.INV.RECORD.STATUS` | `InvestmentProgram_RecordStatus` | String |  |  |
| 34 | `SC.INV.CURR.NO` | `InvestmentProgram_CurrNo` | String |  |  |
| 35 | `SC.INV.INPUTTER` | `InvestmentProgram_Inputter` |  |  |  |
| 36 | `SC.INV.DATE.TIME` | `InvestmentProgram_DateTime` |  |  |  |
| 37 | `SC.INV.AUTHORISER` | `InvestmentProgram_Authoriser` | String |  |  |
| 38 | `SC.INV.CO.CODE` | `InvestmentProgram_CoCode` | String |  |  |
| 39 | `SC.INV.DEPT.CODE` | `InvestmentProgram_DeptCode` | String |  |  |
| 40 | `SC.INV.AUDITOR.CODE` | `InvestmentProgram_AuditorCode` | String |  |  |
| 41 | `SC.INV.AUDIT.DATE.TIME` | `InvestmentProgram_AuditDateTime` | String |  |  |
