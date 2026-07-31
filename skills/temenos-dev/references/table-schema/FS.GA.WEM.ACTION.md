# FS.GA.WEM.ACTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.ACTION` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.ACTION.PARENT.REF.ID` | `FsGaWemAction_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.ACTION.ORA.ROWID` | `FsGaWemAction_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.ACTION.ACTION.ID` | `FsGaWemAction_ActionId` | TField |  | Unique ID for an Action Multifonds DB Column is ACTION_ID. |
| 4 | `FS.GA.WEM.ACTION.NAME` | `FsGaWemAction_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 5 | `FS.GA.WEM.ACTION.DESCRIPTION` | `FsGaWemAction_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 6 | `FS.GA.WEM.ACTION.USER.GROUP.ACCESS.RIGHT` | `FsGaWemAction_UserGroupAccessRight` | TField |  | The user group which has rights to access the particular screen or function. Multifonds DB Column is ACCESS_ROLE. |
| 7 | `FS.GA.WEM.ACTION.RESET.ACCESS.GROUP.OR.ROLE` | `FsGaWemAction_ResetAccessGroupOrRole` | TField |  | Reset Access Group or Role Multifonds DB Column is RESET_ACCESS_ROLE. |
| 8 | `FS.GA.WEM.ACTION.RESERVED10` | `FsGaWemAction_Reserved10` | TField |  |  |
| 9 | `FS.GA.WEM.ACTION.RESERVED9` | `FsGaWemAction_Reserved9` | TField |  |  |
| 10 | `FS.GA.WEM.ACTION.RESERVED8` | `FsGaWemAction_Reserved8` | TField |  |  |
| 11 | `FS.GA.WEM.ACTION.RESERVED7` | `FsGaWemAction_Reserved7` | TField |  |  |
| 12 | `FS.GA.WEM.ACTION.RESERVED6` | `FsGaWemAction_Reserved6` | TField |  |  |
| 13 | `FS.GA.WEM.ACTION.RESERVED5` | `FsGaWemAction_Reserved5` | TField |  |  |
| 14 | `FS.GA.WEM.ACTION.RESERVED4` | `FsGaWemAction_Reserved4` | TField |  |  |
| 15 | `FS.GA.WEM.ACTION.RESERVED3` | `FsGaWemAction_Reserved3` | TField |  |  |
| 16 | `FS.GA.WEM.ACTION.RESERVED2` | `FsGaWemAction_Reserved2` | TField |  |  |
| 17 | `FS.GA.WEM.ACTION.RESERVED1` | `FsGaWemAction_Reserved1` | TField |  |  |
| 18 | `FS.GA.WEM.ACTION.LOCAL.REF` | `FsGaWemAction_LocalRef` |  |  |  |
| 19 | `FS.GA.WEM.ACTION.OVERRIDE` | `FsGaWemAction_Override` |  |  |  |
| 20 | `FS.GA.WEM.ACTION.RECORD.STATUS` | `FsGaWemAction_RecordStatus` | String |  |  |
| 21 | `FS.GA.WEM.ACTION.CURR.NO` | `FsGaWemAction_CurrNo` | String |  |  |
| 22 | `FS.GA.WEM.ACTION.INPUTTER` | `FsGaWemAction_Inputter` |  |  |  |
| 23 | `FS.GA.WEM.ACTION.DATE.TIME` | `FsGaWemAction_DateTime` |  |  |  |
| 24 | `FS.GA.WEM.ACTION.AUTHORISER` | `FsGaWemAction_Authoriser` | String |  |  |
| 25 | `FS.GA.WEM.ACTION.CO.CODE` | `FsGaWemAction_CoCode` | String |  |  |
| 26 | `FS.GA.WEM.ACTION.DEPT.CODE` | `FsGaWemAction_DeptCode` | String |  |  |
| 27 | `FS.GA.WEM.ACTION.AUDITOR.CODE` | `FsGaWemAction_AuditorCode` | String |  |  |
| 28 | `FS.GA.WEM.ACTION.AUDIT.DATE.TIME` | `FsGaWemAction_AuditDateTime` | String |  |  |
