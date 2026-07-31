# FS.GA.NAV.SIMULATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.SIMULATION` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.SIMULATION.PARENT.REF.ID` | `FsGaNavSimulation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.SIMULATION.ORA.ROWID` | `FsGaNavSimulation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.SIMULATION.NAV.GROUP.CODE` | `FsGaNavSimulation_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 4 | `FS.GA.NAV.SIMULATION.FUND.ID` | `FsGaNavSimulation_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.NAV.SIMULATION.PROCESS.ID` | `FsGaNavSimulation_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 6 | `FS.GA.NAV.SIMULATION.OFFICIAL` | `FsGaNavSimulation_Official` | TField |  | Particular NAV type to be selected Multifonds DB Column is OFFICIAL. |
| 7 | `FS.GA.NAV.SIMULATION.UNOFFICIAL` | `FsGaNavSimulation_Unofficial` | TField |  | It contains the export type of the NAV, mainly while exporting to infocenter Multifonds DB Column is UNOFFICIAL. |
| 8 | `FS.GA.NAV.SIMULATION.DEALING.NAV.TYPE` | `FsGaNavSimulation_DealingNavType` | TField |  | Contains the dealing NAV type information Multifonds DB Column is FLG_DEALING_NAV. |
| 9 | `FS.GA.NAV.SIMULATION.NAV.TIME.STAMP` | `FsGaNavSimulation_NavTimeStamp` | TField |  | Indicates the time stamp of the NAV Multifonds DB Column is NAV_TIMESTAMP. |
| 10 | `FS.GA.NAV.SIMULATION.NAV.TIME.ZONE` | `FsGaNavSimulation_NavTimeZone` | TField |  | Indicates the time zone of the NAV Multifonds DB Column is NAV_TIMEZONE. |
| 11 | `FS.GA.NAV.SIMULATION.NAV.DATE` | `FsGaNavSimulation_NavDate` | TField |  | Displays NAV date of fund. Multifonds DB Column is NAV_DATE. |
| 12 | `FS.GA.NAV.SIMULATION.PRICE.DATE` | `FsGaNavSimulation_PriceDate` | TField |  | Date of the Price or Ex rate used in NAV Multifonds DB Column is DATE_COURS. |
| 13 | `FS.GA.NAV.SIMULATION.DATE.OF.NAV` | `FsGaNavSimulation_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 14 | `FS.GA.NAV.SIMULATION.NET.WORTH.ADJUSTMENT` | `FsGaNavSimulation_NetWorthAdjustment` | TField |  | Use this flag for applying the net worth adjustment on NAV. Related to Brazliian feature of NAV Multifonds DB Column is FLG_NET_WORTH_ADJ. |
| 15 | `FS.GA.NAV.SIMULATION.RESTATE.ELIGIBLE` | `FsGaNavSimulation_RestateEligible` | TField |  | Restate Eligible Multifonds DB Column is FLG_RST_ELIGIBLE. |
| 16 | `FS.GA.NAV.SIMULATION.REPORT.DATE` | `FsGaNavSimulation_ReportDate` | TField |  | Enter a date to be populated in the NAV reports as the NAV date Multifonds DB Column is REPORT_DATE. |
| 17 | `FS.GA.NAV.SIMULATION.RESERVED10` | `FsGaNavSimulation_Reserved10` | TField |  |  |
| 18 | `FS.GA.NAV.SIMULATION.RESERVED9` | `FsGaNavSimulation_Reserved9` | TField |  |  |
| 19 | `FS.GA.NAV.SIMULATION.RESERVED8` | `FsGaNavSimulation_Reserved8` | TField |  |  |
| 20 | `FS.GA.NAV.SIMULATION.RESERVED7` | `FsGaNavSimulation_Reserved7` | TField |  |  |
| 21 | `FS.GA.NAV.SIMULATION.RESERVED6` | `FsGaNavSimulation_Reserved6` | TField |  |  |
| 22 | `FS.GA.NAV.SIMULATION.RESERVED5` | `FsGaNavSimulation_Reserved5` | TField |  |  |
| 23 | `FS.GA.NAV.SIMULATION.RESERVED4` | `FsGaNavSimulation_Reserved4` | TField |  |  |
| 24 | `FS.GA.NAV.SIMULATION.RESERVED3` | `FsGaNavSimulation_Reserved3` | TField |  |  |
| 25 | `FS.GA.NAV.SIMULATION.RESERVED2` | `FsGaNavSimulation_Reserved2` | TField |  |  |
| 26 | `FS.GA.NAV.SIMULATION.RESERVED1` | `FsGaNavSimulation_Reserved1` | TField |  |  |
| 27 | `FS.GA.NAV.SIMULATION.LOCAL.REF` | `FsGaNavSimulation_LocalRef` |  |  |  |
| 28 | `FS.GA.NAV.SIMULATION.OVERRIDE` | `FsGaNavSimulation_Override` |  |  |  |
| 29 | `FS.GA.NAV.SIMULATION.RECORD.STATUS` | `FsGaNavSimulation_RecordStatus` | String |  |  |
| 30 | `FS.GA.NAV.SIMULATION.CURR.NO` | `FsGaNavSimulation_CurrNo` | String |  |  |
| 31 | `FS.GA.NAV.SIMULATION.INPUTTER` | `FsGaNavSimulation_Inputter` |  |  |  |
| 32 | `FS.GA.NAV.SIMULATION.DATE.TIME` | `FsGaNavSimulation_DateTime` |  |  |  |
| 33 | `FS.GA.NAV.SIMULATION.AUTHORISER` | `FsGaNavSimulation_Authoriser` | String |  |  |
| 34 | `FS.GA.NAV.SIMULATION.CO.CODE` | `FsGaNavSimulation_CoCode` | String |  |  |
| 35 | `FS.GA.NAV.SIMULATION.DEPT.CODE` | `FsGaNavSimulation_DeptCode` | String |  |  |
| 36 | `FS.GA.NAV.SIMULATION.AUDITOR.CODE` | `FsGaNavSimulation_AuditorCode` | String |  |  |
| 37 | `FS.GA.NAV.SIMULATION.AUDIT.DATE.TIME` | `FsGaNavSimulation_AuditDateTime` | String |  |  |
