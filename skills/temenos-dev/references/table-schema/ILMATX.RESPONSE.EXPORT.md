# ILMATX.RESPONSE.EXPORT — Table Schema

> Source: `INSERTS/I_F.ILMATX.RESPONSE.EXPORT` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.RESPONSE.EXPORT.BANK.TRN.TYPE` | `IlmatxResponseExport_BankTrnType` | TField |  | This field is Transaction Type. |
| 2 | `ILMATX.RESPONSE.EXPORT.VALUE.DATE` | `IlmatxResponseExport_ValueDate` | TField |  | This field is Value Date. |
| 3 | `ILMATX.RESPONSE.EXPORT.OPEN.QTTY` | `IlmatxResponseExport_OpenQtty` | TField |  | This field is Quantity on the opening transaction quantity on the original cost Lot. |
| 4 | `ILMATX.RESPONSE.EXPORT.OPEN.QTTY.RATIO` | `IlmatxResponseExport_OpenQttyRatio` | TField |  | This field is Open quantities Ratio . |
| 5 | `ILMATX.RESPONSE.EXPORT.CLOSE.QTTY.RATIO` | `IlmatxResponseExport_CloseQttyRatio` | TField |  | This field is Close quantities Ratio . |
| 6 | `ILMATX.RESPONSE.EXPORT.CLOSE.QTTY` | `IlmatxResponseExport_CloseQtty` | TField |  | This field is Close quantity . |
| 7 | `ILMATX.RESPONSE.EXPORT.RATE` | `IlmatxResponseExport_Rate` | TField |  | This field is Cost Rate. |
| 8 | `ILMATX.RESPONSE.EXPORT.CCY.GROSS.SUM` | `IlmatxResponseExport_CcyGrossSum` | TField |  | This field is Gross summary in currency . |
| 9 | `ILMATX.RESPONSE.EXPORT.CCY.COMM.SUM` | `IlmatxResponseExport_CcyCommSum` | TField |  | This field is Commission summary in currency. |
| 10 | `ILMATX.RESPONSE.EXPORT.CCY.INT.SUM` | `IlmatxResponseExport_CcyIntSum` | TField |  | This field is Interest summary in currency. |
| 11 | `ILMATX.RESPONSE.EXPORT.CCY.KEEPCOMM.SUM` | `IlmatxResponseExport_CcyKeepcommSum` | TField |  | This field is Safekeeping summary in currency. |
| 12 | `ILMATX.RESPONSE.EXPORT.CAL.TAX.DATE` | `IlmatxResponseExport_CalTaxDate` | TField |  | This field is Effective date for tax calculation. |
| 13 | `ILMATX.RESPONSE.EXPORT.CCY.RATE.TAX.DATE` | `IlmatxResponseExport_CcyRateTaxDate` | TField |  | This field is Currency Rate (on the effective date for tax calculation) . |
| 14 | `ILMATX.RESPONSE.EXPORT.CCY.RATE.VAL.DATE` | `IlmatxResponseExport_CcyRateValDate` | TField |  | This field is Currency Rate, on value (realisation) date. |
| 15 | `ILMATX.RESPONSE.EXPORT.BASE.INDEX` | `IlmatxResponseExport_BaseIndex` | TField |  | This field is Base Index. |
| 16 | `ILMATX.RESPONSE.EXPORT.CURRENT.INDEX` | `IlmatxResponseExport_CurrentIndex` | TField |  | This field is Current Index |
| 17 | `ILMATX.RESPONSE.EXPORT.NIS.PAY.VAL` | `IlmatxResponseExport_NisPayVal` | TField |  | This field is Net pay value in ILS. |
| 18 | `ILMATX.RESPONSE.EXPORT.NIS.TOTAL.VAL` | `IlmatxResponseExport_NisTotalVal` | TField |  | This field is Net Cost value in ILS. |
| 19 | `ILMATX.RESPONSE.EXPORT.ADJ.NIS.COST` | `IlmatxResponseExport_AdjNisCost` | TField |  | This field is Adjusted Net Cost value in ILS. |
| 20 | `ILMATX.RESPONSE.EXPORT.NOM.NIS.PROF` | `IlmatxResponseExport_NomNisProf` | TField |  | This field is Nominal Gain/Loss. |
| 21 | `ILMATX.RESPONSE.EXPORT.NIS.REAL.PROF` | `IlmatxResponseExport_NisRealProf` | TField |  | This field is Real Gain/Loss. |
| 22 | `ILMATX.RESPONSE.EXPORT.TAX.RATE` | `IlmatxResponseExport_TaxRate` | TField |  | This field is Tax Rate. |
| 23 | `ILMATX.RESPONSE.EXPORT.CAL.TAX.TYPE` | `IlmatxResponseExport_CalTaxType` | TField |  | This field is Type of tax calculation:1: Real 2: Nominal 3: Exempted (ccustomer / security) 7: Calculation exemption (no need to calculate). |
| 24 | `ILMATX.RESPONSE.EXPORT.CAL.TAX.NIS` | `IlmatxResponseExport_CalTaxNis` | TField |  | This field Calculated Tax in ILS . |
| 25 | `ILMATX.RESPONSE.EXPORT.DEDUCT.REFUND.PL` | `IlmatxResponseExport_DeductRefundPl` | TField |  | This field is Deducted/Refunded amount. |
| 26 | `ILMATX.RESPONSE.EXPORT.CAL.TAX.NIS1` | `IlmatxResponseExport_CalTaxNis1` | TField |  | This field is Calculated Tax in ILS. |
| 27 | `ILMATX.RESPONSE.EXPORT.CAL.COST.VALUE` | `IlmatxResponseExport_CalCostValue` | TField |  | This field is Effective Cost for tax calculation. |
| 28 | `ILMATX.RESPONSE.EXPORT.CAL.TAX.TYPE.NUM` | `IlmatxResponseExport_CalTaxTypeNum` | TField |  | This field is . |
| 29 | `ILMATX.RESPONSE.EXPORT.START.DATE.TAX.CAL` | `IlmatxResponseExport_StartDateTaxCal` | TField |  | This field is Effective date for tax calculation. |
| 30 | `ILMATX.RESPONSE.EXPORT.START.DATE.INDEX` | `IlmatxResponseExport_StartDateIndex` | TField |  | This field is CPI on Effective date. |
| 31 | `ILMATX.RESPONSE.EXPORT.START.DATE.RATE` | `IlmatxResponseExport_StartDateRate` | TField |  | This field is Rate on Effective date. |
| 32 | `ILMATX.RESPONSE.EXPORT.START.DATE.CCY.RATE` | `IlmatxResponseExport_StartDateCcyRate` | TField |  | This field is Currency Rate on Effective date. |
| 33 | `ILMATX.RESPONSE.EXPORT.START.DATE.VAL.NOM` | `IlmatxResponseExport_StartDateValNom` | TField |  | This field is Nominal Cost on Effective date. |
| 34 | `ILMATX.RESPONSE.EXPORT.START.DATE.VAL.REAL` | `IlmatxResponseExport_StartDateValReal` | TField |  | This field is Actual Cost on Effective date. |
| 35 | `ILMATX.RESPONSE.EXPORT.PL.B.START.DATE.NO` | `IlmatxResponseExport_PlBStartDateNo` | TField |  | This field is Nominal Gain/Loss, before the effective date. |
| 36 | `ILMATX.RESPONSE.EXPORT.PL.B.START.DATE.RATE` | `IlmatxResponseExport_PlBStartDateRate` | TField |  | This field is Real Gain/Loss, before effective date. |
| 37 | `ILMATX.RESPONSE.EXPORT.Pl.A.START.DATE.NO` | `IlmatxResponseExport_PlAStartDateNo` | TField |  | This field is Nominal Gain/Loss, after the effective date. |
| 38 | `ILMATX.RESPONSE.EXPORT.PL.A.START.DATE.RATE` | `IlmatxResponseExport_PlAStartDateRate` | TField |  | This field is Real Gain/Loss, after the effective date. |
| 39 | `ILMATX.RESPONSE.EXPORT.EXE.DATETIME` | `IlmatxResponseExport_ExeDatetime` | TField |  | This field is TaxServer execution time. |
| 40 | `ILMATX.RESPONSE.EXPORT.COMM.TYPE` | `IlmatxResponseExport_CommType` | TField |  | This field is Commision Type. |
| 41 | `ILMATX.RESPONSE.EXPORT.ERROR.CODE.CALC` | `IlmatxResponseExport_ErrorCodeCalc` |  |  |  |
| 42 | `ILMATX.RESPONSE.EXPORT.ERROR.DESC.CALC` | `IlmatxResponseExport_ErrorDescCalc` |  |  |  |
| 43 | `ILMATX.RESPONSE.EXPORT.PL.A.DEDUCT` | `IlmatxResponseExport_PlADeduct` | TField |  | This field is Gain/Loss after deduction. |
| 44 | `ILMATX.RESPONSE.EXPORT.RESERVED.5` | `IlmatxResponseExport_Reserved5` | TField |  | Reserved for future use. |
| 45 | `ILMATX.RESPONSE.EXPORT.RESERVED.4` | `IlmatxResponseExport_Reserved4` | TField |  | Reserved for future use. |
| 46 | `ILMATX.RESPONSE.EXPORT.RESERVED.3` | `IlmatxResponseExport_Reserved3` | TField |  | Reserved for future use. |
| 47 | `ILMATX.RESPONSE.EXPORT.RESERVED.2` | `IlmatxResponseExport_Reserved2` | TField |  | Reserved for future use. |
| 48 | `ILMATX.RESPONSE.EXPORT.RESERVED.1` | `IlmatxResponseExport_Reserved1` | TField |  | Reserved for future use. |
| 49 | `ILMATX.RESPONSE.EXPORT.LOCAL.REF` | `IlmatxResponseExport_LocalRef` |  |  |  |
| 50 | `ILMATX.RESPONSE.EXPORT.OVERRIDE` | `IlmatxResponseExport_Override` |  |  |  |
| 51 | `ILMATX.RESPONSE.EXPORT.RECORD.STATUS` | `IlmatxResponseExport_RecordStatus` | String |  |  |
| 52 | `ILMATX.RESPONSE.EXPORT.CURR.NO` | `IlmatxResponseExport_CurrNo` | String |  |  |
| 53 | `ILMATX.RESPONSE.EXPORT.INPUTTER` | `IlmatxResponseExport_Inputter` |  |  |  |
| 54 | `ILMATX.RESPONSE.EXPORT.DATE.TIME` | `IlmatxResponseExport_DateTime` |  |  |  |
| 55 | `ILMATX.RESPONSE.EXPORT.AUTHORISER` | `IlmatxResponseExport_Authoriser` | String |  |  |
| 56 | `ILMATX.RESPONSE.EXPORT.CO.CODE` | `IlmatxResponseExport_CoCode` | String |  |  |
| 57 | `ILMATX.RESPONSE.EXPORT.DEPT.CODE` | `IlmatxResponseExport_DeptCode` | String |  |  |
| 58 | `ILMATX.RESPONSE.EXPORT.AUDITOR.CODE` | `IlmatxResponseExport_AuditorCode` | String |  |  |
| 59 | `ILMATX.RESPONSE.EXPORT.AUDIT.DATE.TIME` | `IlmatxResponseExport_AuditDateTime` | String |  |  |
