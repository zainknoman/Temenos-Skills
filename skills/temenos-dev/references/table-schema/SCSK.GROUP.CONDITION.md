# SCSK.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.SCSK.GROUP.CONDITION` in `SC_ScfConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SK.SGC.CALC.METHOD` | `ScskGroupCondition_CalcMethod` | TField | Yes | Identifies the method for calculating the basis amount to calculate Safekeeping charges. This field will be used to determine the method for calculating the Safekeeping charges: i.e. If "TOTAL" then a total base amount for the portfolio's holdings will be used to calculate the charge. If "DETAIL" then for each "SEC.TYPE", individual charges will be calculated for each portfolio, based on the base amount for each security and then accumulated to determine the total charge. When set to "TOT.ADDON", system will calculate an add on fee in addition to the Total fees charged for the portfolio. Validation Rules: Input is Mandatory Enter "TOTAL" or "DETAIL" or "TOT.ADDON |
| 2 | `SK.SGC.SECURITY.TYPE` | `ScskGroupCondition_SecurityType` |  |  |  |
| 3 | `SK.SGC.DET.COMM.CODE` | `ScskGroupCondition_DetCommCode` |  |  |  |
| 4 | `SK.SGC.DET.PERCENTAGE` | `ScskGroupCondition_DetPercentage` |  |  |  |
| 5 | `SK.SGC.TOT.COMM.CODE` | `ScskGroupCondition_TotCommCode` | TField |  | Defines the Commission type to calculate the Safekeeping charges. This field relates to a record on the FT.COMMISSION.TYPE table which will be used to calculate the Safekeeping amount based on the total of the base amounts for each portfolio. Validation Rules: To be entered only if the calculation method is "TOTAL" or "TOT.ADDON". Upto 11 alphanumeric characters. |
| 6 | `SK.SGC.TOT.PERCENT` | `ScskGroupCondition_TotPercent` | TField | No | Percentage to be applied to the charge calculated. Defines a percentage to be applied to the total charge calculated using the commission type from the previous field. Validation Rules: Optional input unless the calculation method is "TOTAL" or "TOT.ADDON". Must be numeric |
| 7 | `SK.SGC.GLOBAL.CODE` | `ScskGroupCondition_GlobalCode` | TField | No | FT.COMMISSION.TYPE to be applied to the final total of calculated charge if a 'Foreign Fees' type charge is to be applied to the Safecustody Fees charged to the portfolio. Validation Rules: Optional input. Must exist on the FT.COMMISSION.TYPE file. |
| 8 | `SK.SGC.CALC.DEP.CHARGES` | `ScskGroupCondition_CalcDepCharges` | TField |  | Validation Rules: A maximum of 3 characters may be entered. The following values are permitted: NO |
| 9 | `SK.SGC.TAX.COMM.CODE` | `ScskGroupCondition_TaxCommCode` | TField | No | Identifies the the Charge Code or Group to determine the TAX code to be used for Safekeeping Charges. This field will be used to calculate the Tax Amount for resultant Safekeeping charge. Optional Input. |
| 10 | `SK.SGC.CALC.TYPE` | `ScskGroupCondition_CalcType` |  |  |  |
| 11 | `SK.SGC.PERIOD.START` | `ScskGroupCondition_PeriodStart` |  |  |  |
| 12 | `SK.SGC.PERIOD.END` | `ScskGroupCondition_PeriodEnd` |  |  |  |
| 13 | `SK.SGC.NO.OF.MONTHS` | `ScskGroupCondition_NoOfMonths` |  |  |  |
| 14 | `SK.SGC.DELIV.START` | `ScskGroupCondition_DelivStart` |  |  |  |
| 15 | `SK.SGC.DELIV.END` | `ScskGroupCondition_DelivEnd` |  |  |  |
| 16 | `SK.SGC.MIN.MAX.CCY` | `ScskGroupCondition_MinMaxCcy` |  |  |  |
| 17 | `SK.SGC.MIN.AMOUNT` | `ScskGroupCondition_MinAmount` |  |  |  |
| 18 | `SK.SGC.MAX.AMOUNT` | `ScskGroupCondition_MaxAmount` |  |  |  |
| 19 | `SK.SGC.DEF.MIN.MAX.CCY` | `ScskGroupCondition_DefMinMaxCcy` | TField | Yes | Specifies the currency code that will contain the default minimum / maximum values for safekeeping charges. If the system cannot find a definition in the currency in which the charges are calculated, the definitions for this currency will be taken and will be converted at mid-rate to the charge account currency. Validation Rules: Mandatory if MIN.MAX.CCY is specified Value must be defined in MIN.MAX.CCY |
| 20 | `SK.SGC.SECOND.FEE.CODE` | `ScskGroupCondition_SecondFeeCode` | TField |  | Identifies the Commission Type used to perform a secondary calculation on the result of the primary safekeeping fee calculation. This 'fee-on-fee' method is only supported for daily accrual, i.e. where SAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL for CHARGE.TYPE 'SC' is set to 'DAILY', and where SCSF.CHARGE.PARAMETER&gt;AVERAGE.CLOSING is set to 'PREV.MONTH.CLOSE' for all records. This field is ignored during the calculation of Depository Fees. Validation rules If used, must be entered in conjunction with a SECOND.FEE.PERC. |
| 21 | `SK.SGC.SECOND.FEE.PERC` | `ScskGroupCondition_SecondFeePerc` | TField |  | Defines the percentage to be applied when performing a secondary calculation on the result of the primary safekeeping fee calculation. This 'fee-on-fee' method is only supported for daily accrual, i.e. where SAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL for CHARGE.TYPE 'SC' is set to 'DAILY', and where SCSF.CHARGE.PARAMETER&gt;AVERAGE.CLOSING is set to 'PREV.MONTH.CLOSE' for all records. This field is ignored during the calculation of Depository Fees. Validation rules If used, must be entered in conjunction with a SECOND.FEE.CODE. |
| 22 | `SK.SGC.MINMAX.FEE.TYPE` | `ScskGroupCondition_MinmaxFeeType` |  |  |  |
| 23 | `SK.SGC.DET.MINMAX.CCY` | `ScskGroupCondition_DetMinmaxCcy` |  |  |  |
| 24 | `SK.SGC.DET.MIN.AMT` | `ScskGroupCondition_DetMinAmt` |  |  |  |
| 25 | `SK.SGC.DET.MAX.AMT` | `ScskGroupCondition_DetMaxAmt` |  |  |  |
| 26 | `SK.SGC.DET.DEF.CCY` | `ScskGroupCondition_DetDefCcy` | TField |  | This Field holds the Default Currency in which Min and Max amounts will be taken when MinMax amounts are not available in local currency. Validation Rules: Input allowed only when CALC.TYPE is 'DETAIL' Input allowed only when DET.MINMAX.CCY is inputted |
| 27 | `SK.SGC.RESERVED.8` | `ScskGroupCondition_Reserved8` | TField |  |  |
| 28 | `SK.SGC.RESERVED.7` | `ScskGroupCondition_Reserved7` | TField |  |  |
| 29 | `SK.SGC.RESERVED.6` | `ScskGroupCondition_Reserved6` | TField |  |  |
| 30 | `SK.SGC.RESERVED.5` | `ScskGroupCondition_Reserved5` | TField |  | Reserved for future use. Validation Rules: No input field. |
| 31 | `SK.SGC.RESERVED.4` | `ScskGroupCondition_Reserved4` | TField |  | Reserved for future use. Validation Rules: No input field. |
| 32 | `SK.SGC.RESERVED.3` | `ScskGroupCondition_Reserved3` | TField |  | Reserved for future use. Validation Rules: No input field. |
| 33 | `SK.SGC.RESERVED.2` | `ScskGroupCondition_Reserved2` | TField |  | Reserved for future use. Validation Rules: No input field. |
| 34 | `SK.SGC.RESERVED.1` | `ScskGroupCondition_Reserved1` | TField |  | Reserved for future use. Validation Rules: No input field. |
| 35 | `SK.SGC.LOCAL.REF` | `ScskGroupCondition_LocalRef` |  |  |  |
| 36 | `SK.SGC.RECORD.STATUS` | `ScskGroupCondition_RecordStatus` | String |  |  |
| 37 | `SK.SGC.CURR.NO` | `ScskGroupCondition_CurrNo` | String |  |  |
| 38 | `SK.SGC.INPUTTER` | `ScskGroupCondition_Inputter` |  |  |  |
| 39 | `SK.SGC.DATE.TIME` | `ScskGroupCondition_DateTime` |  |  |  |
| 40 | `SK.SGC.AUTHORISER` | `ScskGroupCondition_Authoriser` | String |  |  |
| 41 | `SK.SGC.CO.CODE` | `ScskGroupCondition_CoCode` | String |  |  |
| 42 | `SK.SGC.DEPT.CODE` | `ScskGroupCondition_DeptCode` | String |  |  |
| 43 | `SK.SGC.AUDITOR.CODE` | `ScskGroupCondition_AuditorCode` | String |  |  |
| 44 | `SK.SGC.AUDIT.DATE.TIME` | `ScskGroupCondition_AuditDateTime` | String |  |  |
