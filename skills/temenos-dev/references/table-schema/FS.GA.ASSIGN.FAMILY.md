# FS.GA.ASSIGN.FAMILY — Table Schema

> Source: `INSERTS/I_F.FS.GA.ASSIGN.FAMILY` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.ASSIGN.FAMILY.FAMILY.ID` | `FsGaAssignFamily_FamilyId` | TField |  | Family ID Multifonds DB Column is P_FAMILY_ID. |
| 2 | `GA.ASSIGN.FAMILY.USER.ID` | `FsGaAssignFamily_UserId` | TField |  | User Multifonds DB Column is P_USER. |
| 3 | `GA.ASSIGN.FAMILY.RIGHTS.FLAG` | `FsGaAssignFamily_RightsFlag` | TField |  | Right Flag Multifonds DB Column is P_FLG_RIGHTS. |
| 4 | `GA.ASSIGN.FAMILY.RESERVED5` | `FsGaAssignFamily_Reserved5` | TField |  |  |
| 5 | `GA.ASSIGN.FAMILY.RESERVED4` | `FsGaAssignFamily_Reserved4` | TField |  |  |
| 6 | `GA.ASSIGN.FAMILY.RESERVED3` | `FsGaAssignFamily_Reserved3` | TField |  |  |
| 7 | `GA.ASSIGN.FAMILY.RESERVED2` | `FsGaAssignFamily_Reserved2` | TField |  |  |
| 8 | `GA.ASSIGN.FAMILY.RESERVED1` | `FsGaAssignFamily_Reserved1` | TField |  |  |
| 9 | `GA.ASSIGN.FAMILY.LOCAL.REF` | `FsGaAssignFamily_LocalRef` |  |  |  |
| 10 | `GA.ASSIGN.FAMILY.OVERRIDE` | `FsGaAssignFamily_Override` |  |  |  |
| 11 | `GA.ASSIGN.FAMILY.RECORD.STATUS` | `FsGaAssignFamily_RecordStatus` | String |  |  |
| 12 | `GA.ASSIGN.FAMILY.CURR.NO` | `FsGaAssignFamily_CurrNo` | String |  |  |
| 13 | `GA.ASSIGN.FAMILY.INPUTTER` | `FsGaAssignFamily_Inputter` |  |  |  |
| 14 | `GA.ASSIGN.FAMILY.DATE.TIME` | `FsGaAssignFamily_DateTime` |  |  |  |
| 15 | `GA.ASSIGN.FAMILY.AUTHORISER` | `FsGaAssignFamily_Authoriser` | String |  |  |
| 16 | `GA.ASSIGN.FAMILY.CO.CODE` | `FsGaAssignFamily_CoCode` | String |  |  |
| 17 | `GA.ASSIGN.FAMILY.DEPT.CODE` | `FsGaAssignFamily_DeptCode` | String |  |  |
| 18 | `GA.ASSIGN.FAMILY.AUDITOR.CODE` | `FsGaAssignFamily_AuditorCode` | String |  |  |
| 19 | `GA.ASSIGN.FAMILY.AUDIT.DATE.TIME` | `FsGaAssignFamily_AuditDateTime` | String |  |  |
