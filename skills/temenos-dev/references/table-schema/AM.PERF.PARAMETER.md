# AM.PERF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AM.PERF.PARAMETER` in `AM_Performance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.SSP.PERF.TOLERANCE` | `AmPerfParameter_PerfTolerance` | TField |  | This field defines a threshold percentage for the change in a portfolios performance.It is used by the EOD batch job: PERFORMANCE.COMPARE.FLOWS. This job produces a report LIST OF PERFORMANCE VARIATIONS - DAILY LIST Validation Rules: : It should have a Numeric Value. |
| 2 | `AM.SSP.PERF.METHOD` | `AmPerfParameter_PerfMethod` | TField |  | This is the field which contains the default performance calculation formula. It is used within portfolio performance enquiries to display performance figures according to this defaulted methodology. The default methodology can be overridden when launching the enquiry. Validation Rules: : This field can have only either of the following values: 1.Daily 2.Modified Dietz |
| 3 | `AM.SSP.PERF.DECIMAL` | `AmPerfParameter_PerfDecimal` | TField |  | This field content specifies the number of decimals for displaying performance values. It is used within performance time series and list enquiries. If this parameter value is blank, the decimal number will be defaulted to 6 in performance enquiries. Validation Rules: : It can have any value from 0-6. |
| 4 | `AM.SSP.PERF.LIVE.DT` | `AmPerfParameter_PerfLiveDt` | TField |  | This is the date when the T24 system goes live and has to be inputted manually. This information is used by the Performance Take-on and Correction tool, SC.PERF.DETAIL.MAN.This application can be used for both: Capturing historical performance figures that were not calculated by the T24 system or correction of T24 calculated figures. This application checks the date in the ID recorded in SC.PERF.DETAIL.MAN, against the PERF.LIVE.DT field: if the ID date is lower than PERF.LIVE.DT, SC.PERF.DETAIL.MAN application assumes the application is being used to take on historic performance figures. If it is greater it is assumed that the application is being used to correct performances. Validation Rules: : Standard Date format. |
| 5 | `AM.SSP.LIMIT.PERF.DT` | `AmPerfParameter_LimitPerfDt` | TField |  | This date is used to control performance Take-on information, with SC.PERF.DETAIL.MAN application This is the performance date below which portfolio performance information cannot be introduced into the system. Validation Rules: : Standard Date format. |
| 6 | `AM.SSP.RESERVED18` | `AmPerfParameter_Reserved18` | TField |  |  |
| 7 | `AM.SSP.RESERVED17` | `AmPerfParameter_Reserved17` | TField |  |  |
| 8 | `AM.SSP.COMP.CALC.METHOD` | `AmPerfParameter_CompCalcMethod` | TField |  | This field defines the default composite calculation methodology used when displaying Composite time series and list enquiries. Validation Rules: : It can have one of the following values: 1. WD for Weighted Daily calculation methodology 2. EQWD for Equal Weighted Daily calculation methodology 3. WM for Weighted Modified Dietz calculation methodology 4. EQMD for Equal Weighted Modified Dietz calculation methodology |
| 9 | `AM.SSP.TAKE.ON.TYPE` | `AmPerfParameter_TakeOnType` | TField |  | This field allows the bank to choose its Take-on Type. This will be used for Portfolio Performance take-on and for Group of Portfolios Performance Take-on. The default is COMPLETE. AUTOMATIC. The four options available are: COMPLETE, MONTHLY RETURNS, QUARTERLY RETURNS and YEARLY RETURNS. COMPLETE - This value indicates that the performance migrated data are Complete. It includes date, indexes, portfolio values and flows, with atleast a record at the date of each flow. This Take-on Type will thus allow Daily as well as Modified Dietz calculation for migrated portfolios or Group of portfolios, from a performance start date prior to Perf.Live.Dt. MONTHLY RETURNS - This value indicates that the performance migrated data are minimal,ie, There would be a single consolidated index per month dated at the end of each month. QUARTERLY RETURNS - This value indicates that there would be a single consolidated index per quarter dated at the end of each quarter. YEARLY RETURNS - This value indicates that the performance migrated data are minimal,ie, There would be a single consolidated index per year dated at the end of each year. The options MONTHLY RETURNS, QUARTERLY RETURNS and YEARLY RETURNS will not include the flow details. The indexes provided may have been calculated according to Daily or Modified Dietz formula in the legacy system. Hence, this Take-on Type will allow only Daily calculation for migrated portfolios or Group of portfolios, from a performance start date prior to Perf.Live.Dt. Validation Rules: This is a NO CHANGE field. The default value is COMPLETE. |
| 10 | `AM.SSP.PERF.BREAK` | `AmPerfParameter_PerfBreak` | TField |  | This is the parameter field that enables or disables Performance Breakdown functionality. Validation Rules: Valid values are either YES/NO . |
| 11 | `AM.SSP.INFLOW.WEIGHT` | `AmPerfParameter_InflowWeight` | TField |  | This field specifies the inflow weightage. The two values are either 0 or 1 0 - Start of day 1 - End of day Validation Rules: Valid values are either 0 or 1. |
| 12 | `AM.SSP.OUTFLOW.WEIGHT` | `AmPerfParameter_OutflowWeight` | TField |  | This field specifies the outflow weightage. The values are either 0 or 1. 0 - Start of Day 1 - End of Day Validation Rules: Vaild values are either 0 or 1. |
| 13 | `AM.SSP.RESERVED16` | `AmPerfParameter_Reserved16` | TField |  |  |
| 14 | `AM.SSP.RESERVED15` | `AmPerfParameter_Reserved15` | TField |  |  |
| 15 | `AM.SSP.TRANS.MKT.PRICE` | `AmPerfParameter_TransMktPrice` |  |  |  |
| 16 | `AM.SSP.CROSS.EFFECT.PL` | `AmPerfParameter_CrossEffectPl` | TField |  | The field is used to specify the CROSS.EFFECT in PL. The two allowed values are ALL and FX. Validation Rules: Valid values are ALL and FX . |
| 17 | `AM.SSP.FEE.INCL.IN.CAP` | `AmPerfParameter_FeeInclInCap` | TField |  | The field is used to specify whether the Fees PL should be included in the Capital PL or not . The options are YES - The fee PL is booked into the capital PL and the fee PL is set to 0. NO - The fee PL is considered independent of the Capital PL and is not booked into the Capital PL. Validation Rules: Valid values are either YES or NO. |
| 18 | `AM.SSP.FX.SEGMENTATION` | `AmPerfParameter_FxSegmentation` | TField |  | This field specifies whether the BUY leg and the SELL leg of the FX transaction need to be considered as two seperate instruments or one instrument for performance calculation. The options are SEPERATE - The two legs of the forex transaction are considered as two seperate entities for performance calculation. CONSOLIDATE - The two legs of the forex transaction are consolidated into one instrument for performance calculation . Validation Rules: Valid values are SEPERATE and CONSOLIDATE . |
| 19 | `AM.SSP.RESERVED14` | `AmPerfParameter_Reserved14` | TField |  |  |
| 20 | `AM.SSP.EXT.FLOW.TXN.COSTS` | `AmPerfParameter_ExtFlowTxnCosts` | TField |  | This field is used to specify whether the external flows should be included in the transaction costs |
| 21 | `AM.SSP.PERF.TYPE` | `AmPerfParameter_PerfType` |  |  |  |
| 22 | `AM.SSP.PERF.ELEMENT` | `AmPerfParameter_PerfElement` |  |  |  |
| 23 | `AM.SSP.PERF.ROUTINE` | `AmPerfParameter_PerfRoutine` |  |  |  |
| 24 | `AM.SSP.PERF.ANN.MTHD` | `AmPerfParameter_PerfAnnMthd` | TField |  | The performance annualisation method to be be used. Valid values are Compound or Linear |
| 25 | `AM.SSP.PERF.ANN.GT1YR` | `AmPerfParameter_PerfAnnGt1yr` | TField |  | This field specifies whether to annualise performance greater than 1 year |
| 26 | `AM.SSP.REVALUE.FLOW` | `AmPerfParameter_RevalueFlow` | TField |  | Revalue the flow. Valid values are either YES/NO |
| 27 | `AM.SSP.VALUATION.SOURCE` | `AmPerfParameter_ValuationSource` | TField |  | Field specifies the valuation source for Portfolio performance calculation Value SC denotes standard portfolio valuation where the Value AM is used in scenarios where the calculation of total portfolio valuations require additional validations (Eg Certain nominal to be valued at agreed market Price / Rate) If the value is set as AM then valuation will be picked up from SC.VALUATION.EXTRACT. Validation Rules: Valid values as SC , AM or Null Values SC and Null are treated similarly |
| 28 | `AM.SSP.INCL.ACCR.FEES` | `AmPerfParameter_InclAccrFees` | TField |  | The value of this field determines whether the monthly fee accruals will be included in the cash flow, and hence, performance details for the associated portfolio. The field will only be effective if the setting in SAFECUSTODY.VALUES, field PERFROM.ACCRUAL, is set to MONTHLY, otherwise the field setting will be ignored. It can be set to include either safekeeping charges, advisory charges, both or none. Validation Rules: Valid values are ADVISORY, SAFEKEEP, BOTH or NONE |
| 29 | `AM.SSP.AIC.DAY.IND` | `AmPerfParameter_AicDayInd` | TField |  |  |
| 30 | `AM.SSP.LOCKING.ACCTS` | `AmPerfParameter_LockingAccts` |  |  |  |
| 31 | `AM.SSP.RESERVED11` | `AmPerfParameter_Reserved11` | TField |  |  |
| 32 | `AM.SSP.RESERVED10` | `AmPerfParameter_Reserved10` | TField |  |  |
| 33 | `AM.SSP.RESERVED09` | `AmPerfParameter_Reserved09` | TField |  |  |
| 34 | `AM.SSP.RESERVED08` | `AmPerfParameter_Reserved08` | TField |  |  |
| 35 | `AM.SSP.RESERVED07` | `AmPerfParameter_Reserved07` | TField |  |  |
| 36 | `AM.SSP.RESERVED06` | `AmPerfParameter_Reserved06` | TField |  |  |
| 37 | `AM.SSP.RESERVED05` | `AmPerfParameter_Reserved05` | TField |  |  |
| 38 | `AM.SSP.RESERVED04` | `AmPerfParameter_Reserved04` | TField |  |  |
| 39 | `AM.SSP.RECORD.STATUS` | `AmPerfParameter_RecordStatus` | String |  |  |
| 40 | `AM.SSP.CURR.NO` | `AmPerfParameter_CurrNo` | String |  |  |
| 41 | `AM.SSP.INPUTTER` | `AmPerfParameter_Inputter` |  |  |  |
| 42 | `AM.SSP.DATE.TIME` | `AmPerfParameter_DateTime` |  |  |  |
| 43 | `AM.SSP.AUTHORISER` | `AmPerfParameter_Authoriser` | String |  |  |
| 44 | `AM.SSP.CO.CODE` | `AmPerfParameter_CoCode` | String |  |  |
| 45 | `AM.SSP.DEPT.CODE` | `AmPerfParameter_DeptCode` | String |  |  |
| 46 | `AM.SSP.AUDITOR.CODE` | `AmPerfParameter_AuditorCode` | String |  |  |
| 47 | `AM.SSP.AUDIT.DATE.TIME` | `AmPerfParameter_AuditDateTime` | String |  |  |
