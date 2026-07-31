# FS.GA.WEM.CONTROL — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.CONTROL` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.WEM.CONTROL.NAME` | `FsGaWemControl_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 2 | `GA.WEM.CONTROL.DESCRIPTION` | `FsGaWemControl_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 3 | `GA.WEM.CONTROL.MANUAL` | `FsGaWemControl_Manual` | TField |  | Manual Multifonds DB Column is MANUAL. |
| 4 | `GA.WEM.CONTROL.USER.GROUP.ACCESS.RIGHT` | `FsGaWemControl_UserGroupAccessRight` | TField |  | The user group which has rights to access the particular screen or function. Multifonds DB Column is ACCESS_ROLE. |
| 5 | `GA.WEM.CONTROL.RESET.ACCESS.GROUP.OR.ROLE` | `FsGaWemControl_ResetAccessGroupOrRole` | TField |  | Reset Access Group or Role Multifonds DB Column is RESET_ACCESS_ROLE. |
| 6 | `GA.WEM.CONTROL.RESERVED5` | `FsGaWemControl_Reserved5` | TField |  |  |
| 7 | `GA.WEM.CONTROL.RESERVED4` | `FsGaWemControl_Reserved4` | TField |  |  |
| 8 | `GA.WEM.CONTROL.RESERVED3` | `FsGaWemControl_Reserved3` | TField |  |  |
| 9 | `GA.WEM.CONTROL.RESERVED2` | `FsGaWemControl_Reserved2` | TField |  |  |
| 10 | `GA.WEM.CONTROL.RESERVED1` | `FsGaWemControl_Reserved1` | TField |  |  |
| 11 | `GA.WEM.CONTROL.LOCAL.REF` | `FsGaWemControl_LocalRef` |  |  |  |
| 12 | `GA.WEM.CONTROL.OVERRIDE` | `FsGaWemControl_Override` |  |  |  |
| 13 | `GA.WEM.CONTROL.RECORD.STATUS` | `FsGaWemControl_RecordStatus` | String |  |  |
| 14 | `GA.WEM.CONTROL.CURR.NO` | `FsGaWemControl_CurrNo` | String |  |  |
| 15 | `GA.WEM.CONTROL.INPUTTER` | `FsGaWemControl_Inputter` |  |  |  |
| 16 | `GA.WEM.CONTROL.DATE.TIME` | `FsGaWemControl_DateTime` |  |  |  |
| 17 | `GA.WEM.CONTROL.AUTHORISER` | `FsGaWemControl_Authoriser` | String |  |  |
| 18 | `GA.WEM.CONTROL.CO.CODE` | `FsGaWemControl_CoCode` | String |  |  |
| 19 | `GA.WEM.CONTROL.DEPT.CODE` | `FsGaWemControl_DeptCode` | String |  |  |
| 20 | `GA.WEM.CONTROL.AUDITOR.CODE` | `FsGaWemControl_AuditorCode` | String |  |  |
| 21 | `GA.WEM.CONTROL.AUDIT.DATE.TIME` | `FsGaWemControl_AuditDateTime` | String |  |  |
