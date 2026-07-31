# FS.GI.FUND.SIMULATION.CALENDAR — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.SIMULATION.CALENDAR` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.SIMULATION.CALENDAR.PARENT.REF.ID` | `FsGiFundSimulationCalendar_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.SIMULATION.CALENDAR.ORA.ROWID` | `FsGiFundSimulationCalendar_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.SIMULATION.CALENDAR.FUND.ID` | `FsGiFundSimulationCalendar_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.SIMULATION.CALENDAR.OPERATION.CODE` | `FsGiFundSimulationCalendar_OperationCode` | TField |  | Operation code which in scope of simulation process. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.SIMULATION.CALENDAR.SIMULATION.DATE` | `FsGiFundSimulationCalendar_SimulationDate` | TField |  | Date on which simulation process expected to happen. Multifonds DB Column is DATE_SIM. |
| 6 | `FS.GI.FUND.SIMULATION.CALENDAR.TRADE.DATE` | `FsGiFundSimulationCalendar_TradeDate` | TField |  | Trade date of the transaction. Multifonds DB Column is DOPER. |
| 7 | `FS.GI.FUND.SIMULATION.CALENDAR.INTERNAL.ID` | `FsGiFundSimulationCalendar_InternalId` | TField |  | Unique internal identifier of the simulation record. Multifonds DB Column is INTERNAL_ID. |
| 8 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED10` | `FsGiFundSimulationCalendar_Reserved10` | TField |  |  |
| 9 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED9` | `FsGiFundSimulationCalendar_Reserved9` | TField |  |  |
| 10 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED8` | `FsGiFundSimulationCalendar_Reserved8` | TField |  |  |
| 11 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED7` | `FsGiFundSimulationCalendar_Reserved7` | TField |  |  |
| 12 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED6` | `FsGiFundSimulationCalendar_Reserved6` | TField |  |  |
| 13 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED5` | `FsGiFundSimulationCalendar_Reserved5` | TField |  |  |
| 14 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED4` | `FsGiFundSimulationCalendar_Reserved4` | TField |  |  |
| 15 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED3` | `FsGiFundSimulationCalendar_Reserved3` | TField |  |  |
| 16 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED2` | `FsGiFundSimulationCalendar_Reserved2` | TField |  |  |
| 17 | `FS.GI.FUND.SIMULATION.CALENDAR.RESERVED1` | `FsGiFundSimulationCalendar_Reserved1` | TField |  |  |
| 18 | `FS.GI.FUND.SIMULATION.CALENDAR.LOCAL.REF` | `FsGiFundSimulationCalendar_LocalRef` |  |  |  |
| 19 | `FS.GI.FUND.SIMULATION.CALENDAR.OVERRIDE` | `FsGiFundSimulationCalendar_Override` |  |  |  |
| 20 | `FS.GI.FUND.SIMULATION.CALENDAR.RECORD.STATUS` | `FsGiFundSimulationCalendar_RecordStatus` | String |  |  |
| 21 | `FS.GI.FUND.SIMULATION.CALENDAR.CURR.NO` | `FsGiFundSimulationCalendar_CurrNo` | String |  |  |
| 22 | `FS.GI.FUND.SIMULATION.CALENDAR.INPUTTER` | `FsGiFundSimulationCalendar_Inputter` |  |  |  |
| 23 | `FS.GI.FUND.SIMULATION.CALENDAR.DATE.TIME` | `FsGiFundSimulationCalendar_DateTime` |  |  |  |
| 24 | `FS.GI.FUND.SIMULATION.CALENDAR.AUTHORISER` | `FsGiFundSimulationCalendar_Authoriser` | String |  |  |
| 25 | `FS.GI.FUND.SIMULATION.CALENDAR.CO.CODE` | `FsGiFundSimulationCalendar_CoCode` | String |  |  |
| 26 | `FS.GI.FUND.SIMULATION.CALENDAR.DEPT.CODE` | `FsGiFundSimulationCalendar_DeptCode` | String |  |  |
| 27 | `FS.GI.FUND.SIMULATION.CALENDAR.AUDITOR.CODE` | `FsGiFundSimulationCalendar_AuditorCode` | String |  |  |
| 28 | `FS.GI.FUND.SIMULATION.CALENDAR.AUDIT.DATE.TIME` | `FsGiFundSimulationCalendar_AuditDateTime` | String |  |  |
