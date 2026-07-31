# ILMATX.COST.DATA — Table Schema

> Source: `INSERTS/I_F.ILMATX.COST.DATA` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.COST.DATA.VALUE.DATE` | `IlmatxCostData_ValueDate` | TField |  | This field is Value date. |
| 2 | `ILMATX.COST.DATA.INV.CATEG` | `IlmatxCostData_InvCateg` | TField |  | This field is Investment category Main/Sub. |
| 3 | `ILMATX.COST.DATA.BANK.TRN.TYPE` | `IlmatxCostData_BankTrnType` | TField |  | This field is Bank Transaction type. |
| 4 | `ILMATX.COST.DATA.CR.DR` | `IlmatxCostData_CrDr` | TField |  | This field is Credit/Debit flag: 0: Not Applicable 1: Credit 2: Debit 3: Ex . |
| 5 | `ILMATX.COST.DATA.CLOSE.QTTY` | `IlmatxCostData_CloseQtty` | TField |  | This field is Close quantity. |
| 6 | `ILMATX.COST.DATA.RATE` | `IlmatxCostData_Rate` | TField |  | This field is Trade Rate (rate's currency). |
| 7 | `ILMATX.COST.DATA.CURRENCY` | `IlmatxCostData_Currency` | TField |  | This field is Rate Currency Code. |
| 8 | `ILMATX.COST.DATA.TRADE.CURRENCY` | `IlmatxCostData_TradeCurrency` | TField |  | This field is Trade Currency Code . |
| 9 | `ILMATX.COST.DATA.RATE.MULT` | `IlmatxCostData_RateMult` | TField |  | This field is Rate Multiplier. |
| 10 | `ILMATX.COST.DATA.CCY.GROSS.SUM` | `IlmatxCostData_CcyGrossSum` | TField |  | This field is Gross Sum in Trade Currency. |
| 11 | `ILMATX.COST.DATA.IND.COST.PAY` | `IlmatxCostData_IndCostPay` | TField |  | This field is Indirect Cost Pay. |
| 12 | `ILMATX.COST.DATA.CCY.COMM.SUM` | `IlmatxCostData_CcyCommSum` | TField |  | This field is Commission Fee. |
| 13 | `ILMATX.COST.DATA.CCY.INT.SUM` | `IlmatxCostData_CcyIntSum` | TField |  | This field is Interest summary . |
| 14 | `ILMATX.COST.DATA.CCY.KEEPCOMM.SUM` | `IlmatxCostData_CcyKeepcommSum` | TField |  | This field is Safe keeping Fee. |
| 15 | `ILMATX.COST.DATA.STORNO.TYPE` | `IlmatxCostData_StornoType` | TField |  | This field is Storno Type: 0: New 1: Retroactive 2: Canceled 3: Canceling. |
| 16 | `ILMATX.COST.DATA.STORNO.TRANS.REF` | `IlmatxCostData_StornoTransRef` | TField |  | This field is ID of the cancelled transaction by Storno |
| 17 | `ILMATX.COST.DATA.CAL.TAX.NIS` | `IlmatxCostData_CalTaxNis` | TField |  | This field is Calculated Tax Summary. |
| 18 | `ILMATX.COST.DATA.DEDUCT.REFUND.PL` | `IlmatxCostData_DeductRefundPl` | TField |  | This field is Deducted/Refunded Summary |
| 19 | `ILMATX.COST.DATA.CAL.TAX.NIS1` | `IlmatxCostData_CalTaxNis1` | TField |  | This field is Tax amount for payment. |
| 20 | `ILMATX.COST.DATA.TAX.RATE` | `IlmatxCostData_TaxRate` | TField |  | This field is Tax Rate. |
| 21 | `ILMATX.COST.DATA.ADJ.NIS.COST` | `IlmatxCostData_AdjNisCost` | TField |  | This field is Overall adjusted cost. |
| 22 | `ILMATX.COST.DATA.ERROR.CODE.IMP` | `IlmatxCostData_ErrorCodeImp` |  |  |  |
| 23 | `ILMATX.COST.DATA.ERROR.DESC.IMP` | `IlmatxCostData_ErrorDescImp` |  |  |  |
| 24 | `ILMATX.COST.DATA.CAL.TAX.IND` | `IlmatxCostData_CalTaxInd` | TField |  | This field Tax amount indication. |
| 25 | `ILMATX.COST.DATA.EXE.DATETIME` | `IlmatxCostData_ExeDatetime` | TField |  | This field is TaxServer execution time. |
| 26 | `ILMATX.COST.DATA.COMM.TYPE` | `IlmatxCostData_CommType` | TField |  | This field is Commission type Local/Foreign. |
| 27 | `ILMATX.COST.DATA.PL.SUM` | `IlmatxCostData_PlSum` | TField |  | This field is Gain/Loss summary. |
| 28 | `ILMATX.COST.DATA.PL.AFTER.DEDUCT` | `IlmatxCostData_PlAfterDeduct` | TField |  | This field is Gain/Loss summary after deduction. |
| 29 | `ILMATX.COST.DATA.PL.BAL.FOR.DEDUCT` | `IlmatxCostData_PlBalForDeduct` | TField |  | This field is Gain/Loss balance for deduction. |
| 30 | `ILMATX.COST.DATA.TAX.RATE.EX` | `IlmatxCostData_TaxRateEx` | TField |  | This field is to calculated tax rate is exempt for a new immigrant. |
| 31 | `ILMATX.COST.DATA.RESERVED.5` | `IlmatxCostData_Reserved5` | TField |  | Reserved for future use. |
| 32 | `ILMATX.COST.DATA.RESERVED.4` | `IlmatxCostData_Reserved4` | TField |  | Reserved for future use. |
| 33 | `ILMATX.COST.DATA.RESERVED.3` | `IlmatxCostData_Reserved3` | TField |  | Reserved for future use. |
| 34 | `ILMATX.COST.DATA.RESERVED.2` | `IlmatxCostData_Reserved2` | TField |  | Reserved for future use. |
| 35 | `ILMATX.COST.DATA.RESERVED.1` | `IlmatxCostData_Reserved1` | TField |  | Reserved for future use. |
| 36 | `ILMATX.COST.DATA.LOCAL.REF` | `IlmatxCostData_LocalRef` |  |  |  |
| 37 | `ILMATX.COST.DATA.OVERRIDE` | `IlmatxCostData_Override` |  |  |  |
| 38 | `ILMATX.COST.DATA.RECORD.STATUS` | `IlmatxCostData_RecordStatus` | String |  |  |
| 39 | `ILMATX.COST.DATA.CURR.NO` | `IlmatxCostData_CurrNo` | String |  |  |
| 40 | `ILMATX.COST.DATA.INPUTTER` | `IlmatxCostData_Inputter` |  |  |  |
| 41 | `ILMATX.COST.DATA.DATE.TIME` | `IlmatxCostData_DateTime` |  |  |  |
| 42 | `ILMATX.COST.DATA.AUTHORISER` | `IlmatxCostData_Authoriser` | String |  |  |
| 43 | `ILMATX.COST.DATA.CO.CODE` | `IlmatxCostData_CoCode` | String |  |  |
| 44 | `ILMATX.COST.DATA.DEPT.CODE` | `IlmatxCostData_DeptCode` | String |  |  |
| 45 | `ILMATX.COST.DATA.AUDITOR.CODE` | `IlmatxCostData_AuditorCode` | String |  |  |
| 46 | `ILMATX.COST.DATA.AUDIT.DATE.TIME` | `IlmatxCostData_AuditDateTime` | String |  |  |
