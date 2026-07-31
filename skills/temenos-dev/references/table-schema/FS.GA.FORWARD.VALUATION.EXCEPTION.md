# FS.GA.FORWARD.VALUATION.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.FORWARD.VALUATION.EXCEPTION` in `FS_PricesRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FORWARD.VALUATION.EXCEPTION.FUND.ID` | `FsGaForwardValuationException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.FORWARD.VALUATION.EXCEPTION.SERVICE.CODE` | `FsGaForwardValuationException_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 3 | `FS.GA.FORWARD.VALUATION.EXCEPTION.HEDGING.OR.TRADING.CATEGORY` | `FsGaForwardValuationException_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 4 | `FS.GA.FORWARD.VALUATION.EXCEPTION.FX.TYPE` | `FsGaForwardValuationException_FxType` | TField |  | FX Type For Spot And Forward Identification Multifonds DB Column is TYPE_FX. |
| 5 | `FS.GA.FORWARD.VALUATION.EXCEPTION.NUMBER.OF.DAYS.TO.SWITCH` | `FsGaForwardValuationException_NumberOfDaysToSwitch` | TField |  | Number of days to switch one valaution method to other. Multifonds DB Column is NB_SWITCH. |
| 6 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED10` | `FsGaForwardValuationException_Reserved10` | TField |  |  |
| 7 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED9` | `FsGaForwardValuationException_Reserved9` | TField |  |  |
| 8 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED8` | `FsGaForwardValuationException_Reserved8` | TField |  |  |
| 9 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED7` | `FsGaForwardValuationException_Reserved7` | TField |  |  |
| 10 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED6` | `FsGaForwardValuationException_Reserved6` | TField |  |  |
| 11 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED5` | `FsGaForwardValuationException_Reserved5` | TField |  |  |
| 12 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED4` | `FsGaForwardValuationException_Reserved4` | TField |  |  |
| 13 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED3` | `FsGaForwardValuationException_Reserved3` | TField |  |  |
| 14 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED2` | `FsGaForwardValuationException_Reserved2` | TField |  |  |
| 15 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RESERVED1` | `FsGaForwardValuationException_Reserved1` | TField |  |  |
| 16 | `FS.GA.FORWARD.VALUATION.EXCEPTION.RECORD.STATUS` | `FsGaForwardValuationException_RecordStatus` | String |  |  |
| 17 | `FS.GA.FORWARD.VALUATION.EXCEPTION.CURR.NO` | `FsGaForwardValuationException_CurrNo` | String |  |  |
| 18 | `FS.GA.FORWARD.VALUATION.EXCEPTION.INPUTTER` | `FsGaForwardValuationException_Inputter` |  |  |  |
| 19 | `FS.GA.FORWARD.VALUATION.EXCEPTION.DATE.TIME` | `FsGaForwardValuationException_DateTime` |  |  |  |
| 20 | `FS.GA.FORWARD.VALUATION.EXCEPTION.AUTHORISER` | `FsGaForwardValuationException_Authoriser` | String |  |  |
| 21 | `FS.GA.FORWARD.VALUATION.EXCEPTION.CO.CODE` | `FsGaForwardValuationException_CoCode` | String |  |  |
| 22 | `FS.GA.FORWARD.VALUATION.EXCEPTION.DEPT.CODE` | `FsGaForwardValuationException_DeptCode` | String |  |  |
| 23 | `FS.GA.FORWARD.VALUATION.EXCEPTION.AUDITOR.CODE` | `FsGaForwardValuationException_AuditorCode` | String |  |  |
| 24 | `FS.GA.FORWARD.VALUATION.EXCEPTION.AUDIT.DATE.TIME` | `FsGaForwardValuationException_AuditDateTime` | String |  |  |
