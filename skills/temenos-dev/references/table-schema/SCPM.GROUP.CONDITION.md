# SCPM.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.SCPM.GROUP.CONDITION` in `SC_ScfConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PM.SGC.CALC.METHOD` | `ScpmGroupCondition_CalcMethod` | TField | Yes | Identifies the method for calculating the basis amount to calculate the management fees charges. This field will be used to determine the method for calculating the management fees charges: i.e. If "TOTAL" then a total base amount for the portfolio's holdings will be used to calculate the fees. If"DETAIL" then for each "SEC.TYPE", individual fees will be calculated for each portfolio, based on the base amountfor each security and then accumulated to determine the total charge. When set to "TOT.ADDON", system will calculate an add on fee in addition to the Total fees charged for the portfolio. Validation Rules: Input is Mandatory Enter "TOTAL" or "DETAIL" or "TOT.ADDON" |
| 2 | `PM.SGC.SECURITY.TYPE` | `ScpmGroupCondition_SecurityType` |  |  |  |
| 3 | `PM.SGC.DET.COMM.CODE` | `ScpmGroupCondition_DetCommCode` |  |  |  |
| 4 | `PM.SGC.DET.PERCENTAGE` | `ScpmGroupCondition_DetPercentage` |  |  |  |
| 5 | `PM.SGC.TOT.COMM.CODE` | `ScpmGroupCondition_TotCommCode` | TField |  | Defines the Commission type to calculate the management fees. This field relates to a record on the FT.COMMISSION.TYPE table which will be used to calculate the managementfees based on the total of the base amounts for each portfolio. Validation Rules: To be entered only if the calculation method is "TOTAL" or "TOT.ADDON". Upto 11 alphanumeric characters. |
| 6 | `PM.SGC.TOT.PERCENT` | `ScpmGroupCondition_TotPercent` | TField | No | Percentage to be applied to the charge calculated. Defines a percentage to be applied to the total fees calculated using the commission type from the previousfield. Validation Rules: Optional input unless the calculation method is "TOTAL" or "TOT.ADDON". Must be numeric |
| 7 | `PM.SGC.GLOBAL.CODE` | `ScpmGroupCondition_GlobalCode` | TField |  | Standard T24 alphanumeric field. Validation Rules: A maximum of 11 characters may be entered. Must be the key to a valid entry on the FT.COMMISSION.TYPE file. |
| 8 | `PM.SGC.TAX.COMM.CODE` | `ScpmGroupCondition_TaxCommCode` | TField | No | Identifies the the Charge Code or Group to determine the TAX code to be used for Advisory Charges. This field will be used to calculate the Tax Amount for resultant Advisory charge. Optional Input. |
| 9 | `PM.SGC.CALC.TYPE` | `ScpmGroupCondition_CalcType` |  |  |  |
| 10 | `PM.SGC.PERIOD.START` | `ScpmGroupCondition_PeriodStart` |  |  |  |
| 11 | `PM.SGC.PERIOD.END` | `ScpmGroupCondition_PeriodEnd` |  |  |  |
| 12 | `PM.SGC.NO.OF.MONTHS` | `ScpmGroupCondition_NoOfMonths` |  |  |  |
| 13 | `PM.SGC.DELIV.START` | `ScpmGroupCondition_DelivStart` |  |  |  |
| 14 | `PM.SGC.DELIV.END` | `ScpmGroupCondition_DelivEnd` |  |  |  |
| 15 | `PM.SGC.TOTAL.DETAILS` | `ScpmGroupCondition_TotalDetails` | TField | No | This field will only have an effect if the CALC.METHIOD is set to 'DETAIL'. YES / NO field to allow the user to calculate fees on the total value of the portfolio remaining after thepercentages entered in the DET.PERCENTAGE fields have been taken into account. If this field is set to 'NO' (or left blank) then the commission code used in the calculation of fees will bethose entered in the DET.COMM.CODE field. If this field is set to 'YES' then the commission code entered into the TOT.COMM.CODE field will be used on thetotal remaining value of the portfolio after the DET.PERCENTAGE fields have been taken into account. Validation Rules: Only input of YES or NO allowed. If this field is blank it will be treated as NO by the system. Optional Input. NOTE: For daily accruals this field is ignored and not supported. In this case it is always assumed to be NO. |
| 16 | `PM.SGC.MIN.MAX.CCY` | `ScpmGroupCondition_MinMaxCcy` |  |  |  |
| 17 | `PM.SGC.MIN.AMOUNT` | `ScpmGroupCondition_MinAmount` |  |  |  |
| 18 | `PM.SGC.MAX.AMOUNT` | `ScpmGroupCondition_MaxAmount` |  |  |  |
| 19 | `PM.SGC.DEF.MIN.MAX.CCY` | `ScpmGroupCondition_DefMinMaxCcy` | TField | Yes | Specifies the currency code that will contain the default minimum / maximum values for advisory charges. If the system cannot find a definition in the currency in which the charges are calculated, the definitions forthis currency will be taken and will be converted at mid-rate to the charge account currency. Validation Rules: Mandatory if MIN.MAX.CCY is specified Value must be defined in MIN.MAX.CCY |
| 20 | `PM.SGC.SECOND.FEE.CODE` | `ScpmGroupCondition_SecondFeeCode` | TField |  | Identifies the Commission Type used to perform a secondary calculation on the result of the primary managementfee calculation. This 'fee-on-fee' method is only supported for daily accrual, i.e. whereSAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL for CHARGE.TYPE 'IC' is set to 'DAILY', and whereSCPM.CHARGE.PARAMETER&gt;AVERAGE.CLOSING is set to 'PREV.MONTH.CLOSE' for all records. Validation rules If used, must be entered in conjunction with a SECOND.FEE.PERC. |
| 21 | `PM.SGC.SECOND.FEE.PERC` | `ScpmGroupCondition_SecondFeePerc` | TField |  | Defines the percentage to be applied when performing a secondary calculation on the result of the primarymanagement fee calculation. This 'fee-on-fee' method is only supported for daily accrual, i.e. whereSAFECUSTODY.VALUES&gt;PERFORM.ACCRUAL for CHARGE.TYPE 'IC' is set to 'DAILY', and whereSCPM.CHARGE.PARAMETER&gt;AVERAGE.CLOSING is set to 'PREV.MONTH.CLOSE' for all records. Validation rules If used, must be entered in conjunction with a SECOND.FEE.CODE. |
| 22 | `PM.SGC.TXN.FEE.CCY` | `ScpmGroupCondition_TxnFeeCcy` | TField | Yes | The field will hold the currency in which the associated transaction fee is defined. Validation Rules: A Valid record from CURRENCY Mandatory when TXNFEE field is input |
| 23 | `PM.SGC.TXN.FEE.START.TXN` | `ScpmGroupCondition_TxnFeeStartTxn` |  |  |  |
| 24 | `PM.SGC.TXN.FEE.END.TXN` | `ScpmGroupCondition_TxnFeeEndTxn` |  |  |  |
| 25 | `PM.SGC.TXN.FEE` | `ScpmGroupCondition_TxnFee` |  |  |  |
| 26 | `PM.SGC.TXN.FEE.COMM.TYPE` | `ScpmGroupCondition_TxnFeeCommType` |  |  |  |
| 27 | `PM.SGC.TXN.FEE.TRIGGER` | `ScpmGroupCondition_TxnFeeTrigger` | TField | No | The transaction based fee will be charged only if the portfolio value(AuM) falls below this amount,if threshold value is specified in this field Validation Rules: Optional input. Allowed when "OV" module is installed Not Allowed when AccrualType in SafeCustodyValues is "Daily" |
| 28 | `PM.SGC.RESERVED.7` | `ScpmGroupCondition_Reserved7` | TField |  |  |
| 29 | `PM.SGC.RESERVED.6` | `ScpmGroupCondition_Reserved6` | TField |  |  |
| 30 | `PM.SGC.RESERVED.5` | `ScpmGroupCondition_Reserved5` | TField |  |  |
| 31 | `PM.SGC.RESERVED.4` | `ScpmGroupCondition_Reserved4` | TField |  |  |
| 32 | `PM.SGC.RESERVED.3` | `ScpmGroupCondition_Reserved3` | TField |  |  |
| 33 | `PM.SGC.RESERVED.2` | `ScpmGroupCondition_Reserved2` | TField |  |  |
| 34 | `PM.SGC.RESERVED.1` | `ScpmGroupCondition_Reserved1` | TField |  |  |
| 35 | `PM.SGC.LOCAL.REF` | `ScpmGroupCondition_LocalRef` |  |  |  |
| 36 | `PM.SGC.RECORD.STATUS` | `ScpmGroupCondition_RecordStatus` | String |  |  |
| 37 | `PM.SGC.CURR.NO` | `ScpmGroupCondition_CurrNo` | String |  |  |
| 38 | `PM.SGC.INPUTTER` | `ScpmGroupCondition_Inputter` |  |  |  |
| 39 | `PM.SGC.DATE.TIME` | `ScpmGroupCondition_DateTime` |  |  |  |
| 40 | `PM.SGC.AUTHORISER` | `ScpmGroupCondition_Authoriser` | String |  |  |
| 41 | `PM.SGC.CO.CODE` | `ScpmGroupCondition_CoCode` | String |  |  |
| 42 | `PM.SGC.DEPT.CODE` | `ScpmGroupCondition_DeptCode` | String |  |  |
| 43 | `PM.SGC.AUDITOR.CODE` | `ScpmGroupCondition_AuditorCode` | String |  |  |
| 44 | `PM.SGC.AUDIT.DATE.TIME` | `ScpmGroupCondition_AuditDateTime` | String |  |  |
