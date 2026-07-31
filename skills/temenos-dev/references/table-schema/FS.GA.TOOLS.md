# FS.GA.TOOLS — Table Schema

> Source: `INSERTS/I_F.FS.GA.TOOLS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TOOLS.PARENT.REF.ID` | `FsGaTools_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.TOOLS.ORA.ROWID` | `FsGaTools_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.TOOLS.TOOL.PROCEDURE.NAME` | `FsGaTools_ToolProcedureName` | TField |  | Name of the procedure ex. Sup_deal, Init_Ptf Multifonds DB Column is TOOL. |
| 4 | `FS.GA.TOOLS.COMMITTED` | `FsGaTools_Committed` | TField |  | Commited Multifonds DB Column is COMMITED. |
| 5 | `FS.GA.TOOLS.NB.ERRORS` | `FsGaTools_NbErrors` | TField |  | NB Errors Multifonds DB Column is NB_ERRORS. |
| 6 | `FS.GA.TOOLS.PARAMETER.1` | `FsGaTools_Parameter1` | TField |  | First Parameter for tool procedure Multifonds DB Column is PRM_1. |
| 7 | `FS.GA.TOOLS.PARAMETER.2` | `FsGaTools_Parameter2` | TField |  | Second Parameter for tool procedure Multifonds DB Column is PRM_2. |
| 8 | `FS.GA.TOOLS.PARAMETER.3` | `FsGaTools_Parameter3` | TField |  | Third Parameter for tool procedure Multifonds DB Column is PRM_3. |
| 9 | `FS.GA.TOOLS.PARAMETER.4` | `FsGaTools_Parameter4` | TField |  | Fourth Parameter for tool procedure Multifonds DB Column is PRM_4. |
| 10 | `FS.GA.TOOLS.PARAMETER.5` | `FsGaTools_Parameter5` | TField |  | Fifth Parameter for tool procedure Multifonds DB Column is PRM_5. |
| 11 | `FS.GA.TOOLS.RESERVED10` | `FsGaTools_Reserved10` | TField |  |  |
| 12 | `FS.GA.TOOLS.RESERVED9` | `FsGaTools_Reserved9` | TField |  |  |
| 13 | `FS.GA.TOOLS.RESERVED8` | `FsGaTools_Reserved8` | TField |  |  |
| 14 | `FS.GA.TOOLS.RESERVED7` | `FsGaTools_Reserved7` | TField |  |  |
| 15 | `FS.GA.TOOLS.RESERVED6` | `FsGaTools_Reserved6` | TField |  |  |
| 16 | `FS.GA.TOOLS.RESERVED5` | `FsGaTools_Reserved5` | TField |  |  |
| 17 | `FS.GA.TOOLS.RESERVED4` | `FsGaTools_Reserved4` | TField |  |  |
| 18 | `FS.GA.TOOLS.RESERVED3` | `FsGaTools_Reserved3` | TField |  |  |
| 19 | `FS.GA.TOOLS.RESERVED2` | `FsGaTools_Reserved2` | TField |  |  |
| 20 | `FS.GA.TOOLS.RESERVED1` | `FsGaTools_Reserved1` | TField |  |  |
| 21 | `FS.GA.TOOLS.LOCAL.REF` | `FsGaTools_LocalRef` |  |  |  |
| 22 | `FS.GA.TOOLS.OVERRIDE` | `FsGaTools_Override` |  |  |  |
| 23 | `FS.GA.TOOLS.RECORD.STATUS` | `FsGaTools_RecordStatus` | String |  |  |
| 24 | `FS.GA.TOOLS.CURR.NO` | `FsGaTools_CurrNo` | String |  |  |
| 25 | `FS.GA.TOOLS.INPUTTER` | `FsGaTools_Inputter` |  |  |  |
| 26 | `FS.GA.TOOLS.DATE.TIME` | `FsGaTools_DateTime` |  |  |  |
| 27 | `FS.GA.TOOLS.AUTHORISER` | `FsGaTools_Authoriser` | String |  |  |
| 28 | `FS.GA.TOOLS.CO.CODE` | `FsGaTools_CoCode` | String |  |  |
| 29 | `FS.GA.TOOLS.DEPT.CODE` | `FsGaTools_DeptCode` | String |  |  |
| 30 | `FS.GA.TOOLS.AUDITOR.CODE` | `FsGaTools_AuditorCode` | String |  |  |
| 31 | `FS.GA.TOOLS.AUDIT.DATE.TIME` | `FsGaTools_AuditDateTime` | String |  |  |
