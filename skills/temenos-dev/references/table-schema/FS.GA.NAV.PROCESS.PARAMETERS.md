# FS.GA.NAV.PROCESS.PARAMETERS — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.PROCESS.PARAMETERS` in `FS_Processing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.PROCESS.PARAMETERS.PARENT.REF.ID` | `FsGaNavProcessParameters_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.PROCESS.PARAMETERS.ORA.ROWID` | `FsGaNavProcessParameters_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.PROCESS.PARAMETERS.NAV.GROUP.CODE` | `FsGaNavProcessParameters_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 4 | `FS.GA.NAV.PROCESS.PARAMETERS.PROCESS.ID` | `FsGaNavProcessParameters_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 5 | `FS.GA.NAV.PROCESS.PARAMETERS.VALUATION.TYPE` | `FsGaNavProcessParameters_ValuationType` | TField |  | Type of NAV like O for Official, U for Unofficial, I for Intraday etc Multifonds DB Column is TYP_TRT. |
| 6 | `FS.GA.NAV.PROCESS.PARAMETERS.VALUATION.METHOD` | `FsGaNavProcessParameters_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 7 | `FS.GA.NAV.PROCESS.PARAMETERS.AUTO.NAV.TYPES` | `FsGaNavProcessParameters_AutoNavTypes` | TField |  | Type of automatic NAV like 0 for No auto NAV, 1 for Auto NAV etc Multifonds DB Column is TYP_AUTO_NAV. |
| 8 | `FS.GA.NAV.PROCESS.PARAMETERS.EXPORT.TYPE` | `FsGaNavProcessParameters_ExportType` | TField |  | User Definable Export types like EOD for End of Day, SOD for Start of Day Multifonds DB Column is TYP_SIMEX. |
| 9 | `FS.GA.NAV.PROCESS.PARAMETERS.START.TIME` | `FsGaNavProcessParameters_StartTime` | TField |  | Start Time of the Process to be Run Multifonds DB Column is START_TIME. |
| 10 | `FS.GA.NAV.PROCESS.PARAMETERS.INCLUDE.HOLIDAYS` | `FsGaNavProcessParameters_IncludeHolidays` | TField |  | Include holidays for the processes to be run Multifonds DB Column is FLG_HOLIDAY. |
| 11 | `FS.GA.NAV.PROCESS.PARAMETERS.EXPORT.TO.IC` | `FsGaNavProcessParameters_ExportToIc` | TField |  | Export to Infocenter applicable for a NAV. NAV data is stored in infocenter when this is Y Multifonds DB Column is FLG_EXPORT. |
| 12 | `FS.GA.NAV.PROCESS.PARAMETERS.SUBMIT.DATE` | `FsGaNavProcessParameters_SubmitDate` | TField |  | Submit Date Multifonds DB Column is DATE_SUBMIT. |
| 13 | `FS.GA.NAV.PROCESS.PARAMETERS.CONFIRMED` | `FsGaNavProcessParameters_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 14 | `FS.GA.NAV.PROCESS.PARAMETERS.CUT.OFF.TIME` | `FsGaNavProcessParameters_CutOffTime` | TField |  | Enter the time as of which IN-OUT movements should be stopped for a NAV calculation. Multifonds DB Column is CUT_OFF_TIME. |
| 15 | `FS.GA.NAV.PROCESS.PARAMETERS.CALENDAR.FREQUENCY` | `FsGaNavProcessParameters_CalendarFrequency` | TField |  | Select the option for calendar frequency to run the process Multifonds DB Column is FLG_CALENDAR_FREQ. |
| 16 | `FS.GA.NAV.PROCESS.PARAMETERS.NAV.DATA` | `FsGaNavProcessParameters_NavData` | TField |  | This is just for reporting purpose and the exported data is for NAV Data related or not Multifonds DB Column is NAV_DATA. |
| 17 | `FS.GA.NAV.PROCESS.PARAMETERS.BV.NAV.PRICE.TYPE` | `FsGaNavProcessParameters_BvNavPriceType` | TField |  | The price to be used in Back value NAV like Mid, Bid of Offer price Multifonds DB Column is BV_PRICE_TYPE. |
| 18 | `FS.GA.NAV.PROCESS.PARAMETERS.NAV.PROCESS.GROUP.FOR.PRICE` | `FsGaNavProcessParameters_NavProcessGroupForPrice` | TField |  | Specify the NAV process group for pricing process Multifonds DB Column is PR_NAV_PROCESS. |
| 19 | `FS.GA.NAV.PROCESS.PARAMETERS.AUTO.ACCOUNT.ON.CONFIRMATION` | `FsGaNavProcessParameters_AutoAccountOnConfirmation` | TField |  | Trigger the scheduler for certain type of funds like series fund, Friday forward &amp; Asset and managed funds. Multifonds DB Column is FLG_AUTO_ACC. |
| 20 | `FS.GA.NAV.PROCESS.PARAMETERS.CONTROL.ON.PROCESS` | `FsGaNavProcessParameters_ControlOnProcess` | TField |  | Control on Process Multifonds DB Column is FLG_TR_CONTROL. |
| 21 | `FS.GA.NAV.PROCESS.PARAMETERS.BPEL.PROCESS.ID` | `FsGaNavProcessParameters_BpelProcessId` | TField |  | BPEL Process ID Multifonds DB Column is BPEL_PROCESS_ID. |
| 22 | `FS.GA.NAV.PROCESS.PARAMETERS.BPEL.FILE.NUMBER` | `FsGaNavProcessParameters_BpelFileNumber` | TField |  | BPEL File Number Multifonds DB Column is BPEL_FILE_NAME. |
| 23 | `FS.GA.NAV.PROCESS.PARAMETERS.STATPRO.DATE.CONTROL` | `FsGaNavProcessParameters_StatproDateControl` | TField |  | Statpro reporting date control Multifonds DB Column is DATE_CNTRL. |
| 24 | `FS.GA.NAV.PROCESS.PARAMETERS.NUMBER.OF.PERIOD` | `FsGaNavProcessParameters_NumberOfPeriod` | TField |  | It allows user to define the number of days the NAV should be restated. Multifonds DB Column is NUM_PERIOD. |
| 25 | `FS.GA.NAV.PROCESS.PARAMETERS.TRANSACTION.OR.PRICING.SOURCE` | `FsGaNavProcessParameters_TransactionOrPricingSource` | TField |  | Transaction or Pricing Source Multifonds DB Column is TX_PR_SOURCE. |
| 26 | `FS.GA.NAV.PROCESS.PARAMETERS.INCLUDE.SOFT` | `FsGaNavProcessParameters_IncludeSoft` | TField |  | Set as Y for including Soft trades in NAV or NA process Multifonds DB Column is FLG_INCL_SOFT. |
| 27 | `FS.GA.NAV.PROCESS.PARAMETERS.CASH.FLOW.ID` | `FsGaNavProcessParameters_CashFlowId` | TField |  | Cash Flow ID Multifonds DB Column is CASH_FLOW_ID. |
| 28 | `FS.GA.NAV.PROCESS.PARAMETERS.DATE.OF.NAV` | `FsGaNavProcessParameters_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 29 | `FS.GA.NAV.PROCESS.PARAMETERS.NUMBER.OF.TRIALS` | `FsGaNavProcessParameters_NumberOfTrials` | TField |  | The number of iterations finished. The value will be automatically reset to 0 when the process is rescheduled for the next day. Also have the option of resetting the value in case of any interruption. Multifonds DB Column is NG_NB_TRIAL. |
| 30 | `FS.GA.NAV.PROCESS.PARAMETERS.LAST.DATE` | `FsGaNavProcessParameters_LastDate` | TField |  | Last Date Multifonds DB Column is LAST_DATE. |
| 31 | `FS.GA.NAV.PROCESS.PARAMETERS.LOG.USER` | `FsGaNavProcessParameters_LogUser` | TField |  | Log User Multifonds DB Column is LOG_USER. |
| 32 | `FS.GA.NAV.PROCESS.PARAMETERS.EQUITY.AT.POSITION` | `FsGaNavProcessParameters_EquityAtPosition` | TField |  | Equity at Position Multifonds DB Column is FLG_POSITION. |
| 33 | `FS.GA.NAV.PROCESS.PARAMETERS.LAST.PROCESS.OF.THE.DAY` | `FsGaNavProcessParameters_LastProcessOfTheDay` | TField |  | Indicates last process of the day Multifonds DB Column is LAST_NAV_PROCESS. |
| 34 | `FS.GA.NAV.PROCESS.PARAMETERS.NET.WORTH.ADJUSTMENT` | `FsGaNavProcessParameters_NetWorthAdjustment` | TField |  | Use this flag for applying the net worth adjustment on NAV. Related to Brazliian feature of NAV Multifonds DB Column is FLG_NET_WORTH_ADJ. |
| 35 | `FS.GA.NAV.PROCESS.PARAMETERS.PV.NB.OF.DAYS.OR.LOOK.BACKDAYS` | `FsGaNavProcessParameters_PvNbOfDaysOrLookBackdays` | TField |  | The NAV date run is based on the FAD minus look back date. It can be choose either a 0a or a 1. a 0a : FAD equal to NAV date a 1a : NAV date equal to FAD minus 1 business day (T-1) Multifonds DB Column is PV_NB_DAYS. |
| 36 | `FS.GA.NAV.PROCESS.PARAMETERS.FOR.V2.OR.V3.VALUATION` | `FsGaNavProcessParameters_ForV2OrV3Valuation` | TField |  | Flag for V2 or V3 Valuation Multifonds DB Column is FLG_NAV_VAL_V2V3. |
| 37 | `FS.GA.NAV.PROCESS.PARAMETERS.RESTATE.ELIGIBLE` | `FsGaNavProcessParameters_RestateEligible` | TField |  | Restate Eligible Multifonds DB Column is FLG_RST_ELIGIBLE. |
| 38 | `FS.GA.NAV.PROCESS.PARAMETERS.JOB.NAME` | `FsGaNavProcessParameters_JobName` | TField |  | Assign job name to execute the specific task or Job Multifonds DB Column is JOB. |
| 39 | `FS.GA.NAV.PROCESS.PARAMETERS.BOND.TAX.OR.CGT` | `FsGaNavProcessParameters_BondTaxOrCgt` | TField |  | Bond Tax Or CGT Multifonds DB Column is FLG_CGT_BONDTAX. |
| 40 | `FS.GA.NAV.PROCESS.PARAMETERS.SECURITY.CLOSING.FREQUENCY` | `FsGaNavProcessParameters_SecurityClosingFrequency` | TField |  | Security Closing Frequency Multifonds DB Column is FLG_SEC_CLOSE_FREQ. |
| 41 | `FS.GA.NAV.PROCESS.PARAMETERS.OVERRIDE.IDENTIFIER` | `FsGaNavProcessParameters_OverrideIdentifier` | TField |  | Override Identifier Multifonds DB Column is FLG_OVERRIDE. |
| 42 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED10` | `FsGaNavProcessParameters_Reserved10` | TField |  |  |
| 43 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED9` | `FsGaNavProcessParameters_Reserved9` | TField |  |  |
| 44 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED8` | `FsGaNavProcessParameters_Reserved8` | TField |  |  |
| 45 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED7` | `FsGaNavProcessParameters_Reserved7` | TField |  |  |
| 46 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED6` | `FsGaNavProcessParameters_Reserved6` | TField |  |  |
| 47 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED5` | `FsGaNavProcessParameters_Reserved5` | TField |  |  |
| 48 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED4` | `FsGaNavProcessParameters_Reserved4` | TField |  |  |
| 49 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED3` | `FsGaNavProcessParameters_Reserved3` | TField |  |  |
| 50 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED2` | `FsGaNavProcessParameters_Reserved2` | TField |  |  |
| 51 | `FS.GA.NAV.PROCESS.PARAMETERS.RESERVED1` | `FsGaNavProcessParameters_Reserved1` | TField |  |  |
| 52 | `FS.GA.NAV.PROCESS.PARAMETERS.LOCAL.REF` | `FsGaNavProcessParameters_LocalRef` |  |  |  |
| 53 | `FS.GA.NAV.PROCESS.PARAMETERS.OVERRIDE` | `FsGaNavProcessParameters_Override` |  |  |  |
| 54 | `FS.GA.NAV.PROCESS.PARAMETERS.RECORD.STATUS` | `FsGaNavProcessParameters_RecordStatus` | String |  |  |
| 55 | `FS.GA.NAV.PROCESS.PARAMETERS.CURR.NO` | `FsGaNavProcessParameters_CurrNo` | String |  |  |
| 56 | `FS.GA.NAV.PROCESS.PARAMETERS.INPUTTER` | `FsGaNavProcessParameters_Inputter` |  |  |  |
| 57 | `FS.GA.NAV.PROCESS.PARAMETERS.DATE.TIME` | `FsGaNavProcessParameters_DateTime` |  |  |  |
| 58 | `FS.GA.NAV.PROCESS.PARAMETERS.AUTHORISER` | `FsGaNavProcessParameters_Authoriser` | String |  |  |
| 59 | `FS.GA.NAV.PROCESS.PARAMETERS.CO.CODE` | `FsGaNavProcessParameters_CoCode` | String |  |  |
| 60 | `FS.GA.NAV.PROCESS.PARAMETERS.DEPT.CODE` | `FsGaNavProcessParameters_DeptCode` | String |  |  |
| 61 | `FS.GA.NAV.PROCESS.PARAMETERS.AUDITOR.CODE` | `FsGaNavProcessParameters_AuditorCode` | String |  |  |
| 62 | `FS.GA.NAV.PROCESS.PARAMETERS.AUDIT.DATE.TIME` | `FsGaNavProcessParameters_AuditDateTime` | String |  |  |
