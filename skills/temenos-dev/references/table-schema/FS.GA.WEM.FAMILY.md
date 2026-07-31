# FS.GA.WEM.FAMILY — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.FAMILY` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.FAMILY.PARENT.REF.ID` | `FsGaWemFamily_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.FAMILY.ORA.ROWID` | `FsGaWemFamily_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.FAMILY.FAMILY.ID` | `FsGaWemFamily_FamilyId` | TField |  | ID of the Family Multifonds DB Column is FAMILY_ID. |
| 4 | `FS.GA.WEM.FAMILY.NAME` | `FsGaWemFamily_Name` | TField |  | Name Multifonds DB Column is NAME. |
| 5 | `FS.GA.WEM.FAMILY.DESCRIPTION` | `FsGaWemFamily_Description` | TField |  | Field Description Multifonds DB Column is DESCRIPTION. |
| 6 | `FS.GA.WEM.FAMILY.GROUP.ID` | `FsGaWemFamily_GroupId` | TField |  | ID of the group Multifonds DB Column is GROUP_ID. |
| 7 | `FS.GA.WEM.FAMILY.MODEL.ID` | `FsGaWemFamily_ModelId` | TField |  | ID of the Model Multifonds DB Column is MODEL_ID. |
| 8 | `FS.GA.WEM.FAMILY.FAMILY.TYPE` | `FsGaWemFamily_FamilyType` | TField |  | Based on the Funds available in the family, user can define the category Multifonds DB Column is FAMILY_TYPE. |
| 9 | `FS.GA.WEM.FAMILY.FAMILY.COMPLEXITY` | `FsGaWemFamily_FamilyComplexity` | TField |  | Complexity can be defined by user for each family in complexity adjustment screen Multifonds DB Column is FAMILY_COMPLEXITY. |
| 10 | `FS.GA.WEM.FAMILY.RESERVED10` | `FsGaWemFamily_Reserved10` | TField |  |  |
| 11 | `FS.GA.WEM.FAMILY.RESERVED9` | `FsGaWemFamily_Reserved9` | TField |  |  |
| 12 | `FS.GA.WEM.FAMILY.RESERVED8` | `FsGaWemFamily_Reserved8` | TField |  |  |
| 13 | `FS.GA.WEM.FAMILY.RESERVED7` | `FsGaWemFamily_Reserved7` | TField |  |  |
| 14 | `FS.GA.WEM.FAMILY.RESERVED6` | `FsGaWemFamily_Reserved6` | TField |  |  |
| 15 | `FS.GA.WEM.FAMILY.RESERVED5` | `FsGaWemFamily_Reserved5` | TField |  |  |
| 16 | `FS.GA.WEM.FAMILY.RESERVED4` | `FsGaWemFamily_Reserved4` | TField |  |  |
| 17 | `FS.GA.WEM.FAMILY.RESERVED3` | `FsGaWemFamily_Reserved3` | TField |  |  |
| 18 | `FS.GA.WEM.FAMILY.RESERVED2` | `FsGaWemFamily_Reserved2` | TField |  |  |
| 19 | `FS.GA.WEM.FAMILY.RESERVED1` | `FsGaWemFamily_Reserved1` | TField |  |  |
| 20 | `FS.GA.WEM.FAMILY.LOCAL.REF` | `FsGaWemFamily_LocalRef` |  |  |  |
| 21 | `FS.GA.WEM.FAMILY.OVERRIDE` | `FsGaWemFamily_Override` |  |  |  |
| 22 | `FS.GA.WEM.FAMILY.RECORD.STATUS` | `FsGaWemFamily_RecordStatus` | String |  |  |
| 23 | `FS.GA.WEM.FAMILY.CURR.NO` | `FsGaWemFamily_CurrNo` | String |  |  |
| 24 | `FS.GA.WEM.FAMILY.INPUTTER` | `FsGaWemFamily_Inputter` |  |  |  |
| 25 | `FS.GA.WEM.FAMILY.DATE.TIME` | `FsGaWemFamily_DateTime` |  |  |  |
| 26 | `FS.GA.WEM.FAMILY.AUTHORISER` | `FsGaWemFamily_Authoriser` | String |  |  |
| 27 | `FS.GA.WEM.FAMILY.CO.CODE` | `FsGaWemFamily_CoCode` | String |  |  |
| 28 | `FS.GA.WEM.FAMILY.DEPT.CODE` | `FsGaWemFamily_DeptCode` | String |  |  |
| 29 | `FS.GA.WEM.FAMILY.AUDITOR.CODE` | `FsGaWemFamily_AuditorCode` | String |  |  |
| 30 | `FS.GA.WEM.FAMILY.AUDIT.DATE.TIME` | `FsGaWemFamily_AuditDateTime` | String |  |  |
