# FS.GA.NAV.PROCESS.LINKED — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.PROCESS.LINKED` in `FS_Processing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.PROCESS.LINKED.PARENT.REF.ID` | `FsGaNavProcessLinked_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.PROCESS.LINKED.ORA.ROWID` | `FsGaNavProcessLinked_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.PROCESS.LINKED.NAV.GROUP.CODE` | `FsGaNavProcessLinked_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 4 | `FS.GA.NAV.PROCESS.LINKED.PROCESS.GROUP` | `FsGaNavProcessLinked_ProcessGroup` | TField |  | Group of Processes ex. PGXX. Used for executing multiple process at a time. Multifonds DB Column is PROCESS_GRP. |
| 5 | `FS.GA.NAV.PROCESS.LINKED.PROCESS.ID` | `FsGaNavProcessLinked_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 6 | `FS.GA.NAV.PROCESS.LINKED.VALUATION.TYPE` | `FsGaNavProcessLinked_ValuationType` | TField |  | Type of NAV like O for Official, U for Unofficial, I for Intraday etc Multifonds DB Column is TYP_TRT. |
| 7 | `FS.GA.NAV.PROCESS.LINKED.VALUATION.METHOD` | `FsGaNavProcessLinked_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 8 | `FS.GA.NAV.PROCESS.LINKED.AUTO.NAV.TYPES` | `FsGaNavProcessLinked_AutoNavTypes` | TField |  | Type of automatic NAV like 0 for No auto NAV, 1 for Auto NAV etc Multifonds DB Column is TYP_AUTO_NAV. |
| 9 | `FS.GA.NAV.PROCESS.LINKED.INCLUDE.HOLIDAYS` | `FsGaNavProcessLinked_IncludeHolidays` | TField |  | Include holidays for the processes to be run Multifonds DB Column is FLG_HOLIDAY. |
| 10 | `FS.GA.NAV.PROCESS.LINKED.EXPORT.TO.IC` | `FsGaNavProcessLinked_ExportToIc` | TField |  | Export to Infocenter applicable for a NAV. NAV data is stored in infocenter when this is Y Multifonds DB Column is FLG_EXPORT. |
| 11 | `FS.GA.NAV.PROCESS.LINKED.EXPORT.TYPE` | `FsGaNavProcessLinked_ExportType` | TField |  | User Definable Export types like EOD for End of Day, SOD for Start of Day Multifonds DB Column is TYP_SIMEX. |
| 12 | `FS.GA.NAV.PROCESS.LINKED.CUT.OFF.TIME` | `FsGaNavProcessLinked_CutOffTime` | TField |  | Enter the time as of which IN-OUT movements should be stopped for a NAV calculation. Multifonds DB Column is CUT_OFF_TIME. |
| 13 | `FS.GA.NAV.PROCESS.LINKED.NAV.DATA` | `FsGaNavProcessLinked_NavData` | TField |  | This is just for reporting purpose and the exported data is for NAV Data related or not Multifonds DB Column is NAV_DATA. |
| 14 | `FS.GA.NAV.PROCESS.LINKED.BV.NAV.PRICE.TYPE` | `FsGaNavProcessLinked_BvNavPriceType` | TField |  | The price to be used in Back value NAV like Mid, Bid of Offer price Multifonds DB Column is BV_PRICE_TYPE. |
| 15 | `FS.GA.NAV.PROCESS.LINKED.NAV.PROCESS.GROUP.FOR.PRICE` | `FsGaNavProcessLinked_NavProcessGroupForPrice` | TField |  | Specify the NAV process group for pricing process Multifonds DB Column is PR_NAV_PROCESS. |
| 16 | `FS.GA.NAV.PROCESS.LINKED.CONFIRMED` | `FsGaNavProcessLinked_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 17 | `FS.GA.NAV.PROCESS.LINKED.INCLUDE.SOFT` | `FsGaNavProcessLinked_IncludeSoft` | TField |  | Set as Y for including Soft trades in NAV or NA process Multifonds DB Column is FLG_INCL_SOFT. |
| 18 | `FS.GA.NAV.PROCESS.LINKED.NUMBER.OF.PERIOD` | `FsGaNavProcessLinked_NumberOfPeriod` | TField |  | It allows user to define the number of days the NAV should be restated. Multifonds DB Column is NUM_PERIOD. |
| 19 | `FS.GA.NAV.PROCESS.LINKED.CALENDAR.FREQUENCY` | `FsGaNavProcessLinked_CalendarFrequency` | TField |  | Select the option for calendar frequency to run the process Multifonds DB Column is FLG_CALENDAR_FREQ. |
| 20 | `FS.GA.NAV.PROCESS.LINKED.CONTROL.ON.PROCESS` | `FsGaNavProcessLinked_ControlOnProcess` | TField |  | Control on Process Multifonds DB Column is FLG_TR_CONTROL. |
| 21 | `FS.GA.NAV.PROCESS.LINKED.EQUITY.AT.POSITION` | `FsGaNavProcessLinked_EquityAtPosition` | TField |  | Equity at Position Multifonds DB Column is FLG_POSITION. |
| 22 | `FS.GA.NAV.PROCESS.LINKED.LAST.PROCESS.OF.THE.DAY` | `FsGaNavProcessLinked_LastProcessOfTheDay` | TField |  | Indicates last process of the day Multifonds DB Column is LAST_NAV_PROCESS. |
| 23 | `FS.GA.NAV.PROCESS.LINKED.PV.NB.OF.DAYS.OR.LOOK.BACKDAYS` | `FsGaNavProcessLinked_PvNbOfDaysOrLookBackdays` | TField |  | The NAV date run is based on the FAD minus look back date. It can be choose either A a A 0A a A or A a A 1. A a A 0A a A : FAD equal to NAV date A a A 1A a A : NAV date equal to FAD minus 1 business day (T-1) Multifonds DB Column is PV_NB_DAYS. |
| 24 | `FS.GA.NAV.PROCESS.LINKED.WEM.UNCONFIRMED` | `FsGaNavProcessLinked_WemUnconfirmed` | TField |  | WEM Unconfirmed Multifonds DB Column is WEM_UNCONFIRM. |
| 25 | `FS.GA.NAV.PROCESS.LINKED.RESTATE.ELIGIBLE` | `FsGaNavProcessLinked_RestateEligible` | TField |  | Restate Eligible Multifonds DB Column is FLG_RST_ELIGIBLE. |
| 26 | `FS.GA.NAV.PROCESS.LINKED.BI.JOB.ID` | `FsGaNavProcessLinked_BiJobId` | TField |  | BI Job ID Multifonds DB Column is BI_JOB_ID. |
| 27 | `FS.GA.NAV.PROCESS.LINKED.AUTO.ACCOUNT.ON.CONFIRMATION` | `FsGaNavProcessLinked_AutoAccountOnConfirmation` | TField |  | Trigger the scheduler for certain type of funds like series fund, Friday forward &amp; Asset and managed funds. Multifonds DB Column is FLG_AUTO_ACC. |
| 28 | `FS.GA.NAV.PROCESS.LINKED.STATPRO.DATE.CONTROL` | `FsGaNavProcessLinked_StatproDateControl` | TField |  | Statpro reporting date control Multifonds DB Column is DATE_CNTRL. |
| 29 | `FS.GA.NAV.PROCESS.LINKED.TRANSACTION.OR.PRICING.SOURCE` | `FsGaNavProcessLinked_TransactionOrPricingSource` | TField |  | Transaction or Pricing Source Multifonds DB Column is TX_PR_SOURCE. |
| 30 | `FS.GA.NAV.PROCESS.LINKED.NET.WORTH.ADJUSTMENT` | `FsGaNavProcessLinked_NetWorthAdjustment` | TField |  | Use this flag for applying the net worth adjustment on NAV. Related to Brazliian feature of NAV Multifonds DB Column is FLG_NET_WORTH_ADJ. |
| 31 | `FS.GA.NAV.PROCESS.LINKED.FOR.V2.OR.V3.VALUATION` | `FsGaNavProcessLinked_ForV2OrV3Valuation` | TField |  | Flag for V2 or V3 Valuation Multifonds DB Column is FLG_NAV_VAL_V2V3. |
| 32 | `FS.GA.NAV.PROCESS.LINKED.BOND.TAX.OR.CGT` | `FsGaNavProcessLinked_BondTaxOrCgt` | TField |  | Bond Tax Or CGT Multifonds DB Column is FLG_CGT_BONDTAX. |
| 33 | `FS.GA.NAV.PROCESS.LINKED.SECURITY.CLOSING.FREQUENCY` | `FsGaNavProcessLinked_SecurityClosingFrequency` | TField |  | Security Closing Frequency Multifonds DB Column is FLG_SEC_CLOSE_FREQ. |
| 34 | `FS.GA.NAV.PROCESS.LINKED.RESERVED10` | `FsGaNavProcessLinked_Reserved10` | TField |  |  |
| 35 | `FS.GA.NAV.PROCESS.LINKED.RESERVED9` | `FsGaNavProcessLinked_Reserved9` | TField |  |  |
| 36 | `FS.GA.NAV.PROCESS.LINKED.RESERVED8` | `FsGaNavProcessLinked_Reserved8` | TField |  |  |
| 37 | `FS.GA.NAV.PROCESS.LINKED.RESERVED7` | `FsGaNavProcessLinked_Reserved7` | TField |  |  |
| 38 | `FS.GA.NAV.PROCESS.LINKED.RESERVED6` | `FsGaNavProcessLinked_Reserved6` | TField |  |  |
| 39 | `FS.GA.NAV.PROCESS.LINKED.RESERVED5` | `FsGaNavProcessLinked_Reserved5` | TField |  |  |
| 40 | `FS.GA.NAV.PROCESS.LINKED.RESERVED4` | `FsGaNavProcessLinked_Reserved4` | TField |  |  |
| 41 | `FS.GA.NAV.PROCESS.LINKED.RESERVED3` | `FsGaNavProcessLinked_Reserved3` | TField |  |  |
| 42 | `FS.GA.NAV.PROCESS.LINKED.RESERVED2` | `FsGaNavProcessLinked_Reserved2` | TField |  |  |
| 43 | `FS.GA.NAV.PROCESS.LINKED.RESERVED1` | `FsGaNavProcessLinked_Reserved1` | TField |  |  |
| 44 | `FS.GA.NAV.PROCESS.LINKED.LOCAL.REF` | `FsGaNavProcessLinked_LocalRef` |  |  |  |
| 45 | `FS.GA.NAV.PROCESS.LINKED.OVERRIDE` | `FsGaNavProcessLinked_Override` |  |  |  |
| 46 | `FS.GA.NAV.PROCESS.LINKED.RECORD.STATUS` | `FsGaNavProcessLinked_RecordStatus` | String |  |  |
| 47 | `FS.GA.NAV.PROCESS.LINKED.CURR.NO` | `FsGaNavProcessLinked_CurrNo` | String |  |  |
| 48 | `FS.GA.NAV.PROCESS.LINKED.INPUTTER` | `FsGaNavProcessLinked_Inputter` |  |  |  |
| 49 | `FS.GA.NAV.PROCESS.LINKED.DATE.TIME` | `FsGaNavProcessLinked_DateTime` |  |  |  |
| 50 | `FS.GA.NAV.PROCESS.LINKED.AUTHORISER` | `FsGaNavProcessLinked_Authoriser` | String |  |  |
| 51 | `FS.GA.NAV.PROCESS.LINKED.CO.CODE` | `FsGaNavProcessLinked_CoCode` | String |  |  |
| 52 | `FS.GA.NAV.PROCESS.LINKED.DEPT.CODE` | `FsGaNavProcessLinked_DeptCode` | String |  |  |
| 53 | `FS.GA.NAV.PROCESS.LINKED.AUDITOR.CODE` | `FsGaNavProcessLinked_AuditorCode` | String |  |  |
| 54 | `FS.GA.NAV.PROCESS.LINKED.AUDIT.DATE.TIME` | `FsGaNavProcessLinked_AuditDateTime` | String |  |  |
