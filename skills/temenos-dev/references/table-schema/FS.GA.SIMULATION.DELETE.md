# FS.GA.SIMULATION.DELETE — Table Schema

> Source: `INSERTS/I_F.FS.GA.SIMULATION.DELETE` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SIMULATION.DELETE.PARENT.REF.ID` | `FsGaSimulationDelete_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SIMULATION.DELETE.ORA.ROWID` | `FsGaSimulationDelete_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SIMULATION.DELETE.NAV.GROUP.CODE` | `FsGaSimulationDelete_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 4 | `FS.GA.SIMULATION.DELETE.PROCESS.ID` | `FsGaSimulationDelete_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 5 | `FS.GA.SIMULATION.DELETE.FUND.ID` | `FsGaSimulationDelete_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.SIMULATION.DELETE.OFFICIAL` | `FsGaSimulationDelete_Official` | TField |  | Particular NAV type to be selected Multifonds DB Column is OFFICIAL. |
| 7 | `FS.GA.SIMULATION.DELETE.DATE.OF.NAV` | `FsGaSimulationDelete_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 8 | `FS.GA.SIMULATION.DELETE.PROCESSING.DATE` | `FsGaSimulationDelete_ProcessingDate` | TField |  | Processing date of the simulated fund Multifonds DB Column is DATE_TRT. |
| 9 | `FS.GA.SIMULATION.DELETE.VALUATION.TYPE` | `FsGaSimulationDelete_ValuationType` | TField |  | Valuation type of the Fund Multifonds DB Column is TYP_TRT. |
| 10 | `FS.GA.SIMULATION.DELETE.USER.ID.NAME` | `FsGaSimulationDelete_UserIdName` | TField |  | User name who processed the fund simulation Multifonds DB Column is USER_ID. |
| 11 | `FS.GA.SIMULATION.DELETE.RESERVED10` | `FsGaSimulationDelete_Reserved10` | TField |  |  |
| 12 | `FS.GA.SIMULATION.DELETE.RESERVED9` | `FsGaSimulationDelete_Reserved9` | TField |  |  |
| 13 | `FS.GA.SIMULATION.DELETE.RESERVED8` | `FsGaSimulationDelete_Reserved8` | TField |  |  |
| 14 | `FS.GA.SIMULATION.DELETE.RESERVED7` | `FsGaSimulationDelete_Reserved7` | TField |  |  |
| 15 | `FS.GA.SIMULATION.DELETE.RESERVED6` | `FsGaSimulationDelete_Reserved6` | TField |  |  |
| 16 | `FS.GA.SIMULATION.DELETE.RESERVED5` | `FsGaSimulationDelete_Reserved5` | TField |  |  |
| 17 | `FS.GA.SIMULATION.DELETE.RESERVED4` | `FsGaSimulationDelete_Reserved4` | TField |  |  |
| 18 | `FS.GA.SIMULATION.DELETE.RESERVED3` | `FsGaSimulationDelete_Reserved3` | TField |  |  |
| 19 | `FS.GA.SIMULATION.DELETE.RESERVED2` | `FsGaSimulationDelete_Reserved2` | TField |  |  |
| 20 | `FS.GA.SIMULATION.DELETE.RESERVED1` | `FsGaSimulationDelete_Reserved1` | TField |  |  |
| 21 | `FS.GA.SIMULATION.DELETE.LOCAL.REF` | `FsGaSimulationDelete_LocalRef` |  |  |  |
| 22 | `FS.GA.SIMULATION.DELETE.OVERRIDE` | `FsGaSimulationDelete_Override` |  |  |  |
| 23 | `FS.GA.SIMULATION.DELETE.RECORD.STATUS` | `FsGaSimulationDelete_RecordStatus` | String |  |  |
| 24 | `FS.GA.SIMULATION.DELETE.CURR.NO` | `FsGaSimulationDelete_CurrNo` | String |  |  |
| 25 | `FS.GA.SIMULATION.DELETE.INPUTTER` | `FsGaSimulationDelete_Inputter` |  |  |  |
| 26 | `FS.GA.SIMULATION.DELETE.DATE.TIME` | `FsGaSimulationDelete_DateTime` |  |  |  |
| 27 | `FS.GA.SIMULATION.DELETE.AUTHORISER` | `FsGaSimulationDelete_Authoriser` | String |  |  |
| 28 | `FS.GA.SIMULATION.DELETE.CO.CODE` | `FsGaSimulationDelete_CoCode` | String |  |  |
| 29 | `FS.GA.SIMULATION.DELETE.DEPT.CODE` | `FsGaSimulationDelete_DeptCode` | String |  |  |
| 30 | `FS.GA.SIMULATION.DELETE.AUDITOR.CODE` | `FsGaSimulationDelete_AuditorCode` | String |  |  |
| 31 | `FS.GA.SIMULATION.DELETE.AUDIT.DATE.TIME` | `FsGaSimulationDelete_AuditDateTime` | String |  |  |
