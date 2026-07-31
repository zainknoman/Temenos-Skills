# FS.GA.WEM.EXCEPTION.CATEGORY — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.EXCEPTION.CATEGORY` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.EXCEPTION.CATEGORY.PARENT.REF.ID` | `FsGaWemExceptionCategory_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.EXCEPTION.CATEGORY.ORA.ROWID` | `FsGaWemExceptionCategory_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.EXCEPTION.CATEGORY.GROUP.ID` | `FsGaWemExceptionCategory_GroupId` | TField |  | ID of the group Multifonds DB Column is GROUP_ID. |
| 4 | `FS.GA.WEM.EXCEPTION.CATEGORY.GROUP.NAME` | `FsGaWemExceptionCategory_GroupName` | TField |  | Name of the group Multifonds DB Column is GROUP_NAME. |
| 5 | `FS.GA.WEM.EXCEPTION.CATEGORY.FAMILY.ID` | `FsGaWemExceptionCategory_FamilyId` | TField |  | ID of the Family Multifonds DB Column is FAMILY_ID. |
| 6 | `FS.GA.WEM.EXCEPTION.CATEGORY.FAMILY.NAME` | `FsGaWemExceptionCategory_FamilyName` | TField |  | Name of the Family Multifonds DB Column is FAMILY_NAME. |
| 7 | `FS.GA.WEM.EXCEPTION.CATEGORY.FUND.NAME` | `FsGaWemExceptionCategory_FundName` | TField |  | Fund Name Multifonds DB Column is FUND_ID. |
| 8 | `FS.GA.WEM.EXCEPTION.CATEGORY.CONTROL.NUMBER` | `FsGaWemExceptionCategory_ControlNumber` | TField |  | Control Number Multifonds DB Column is TYP_CONTROLE. |
| 9 | `FS.GA.WEM.EXCEPTION.CATEGORY.JUSTIFICATION.CATEGORY.CODE` | `FsGaWemExceptionCategory_JustificationCategoryCode` | TField |  | To assign the standard justification/exception category to an exception, while justifying and validating an exception Multifonds DB Column is CATEGORY. |
| 10 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED10` | `FsGaWemExceptionCategory_Reserved10` | TField |  |  |
| 11 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED9` | `FsGaWemExceptionCategory_Reserved9` | TField |  |  |
| 12 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED8` | `FsGaWemExceptionCategory_Reserved8` | TField |  |  |
| 13 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED7` | `FsGaWemExceptionCategory_Reserved7` | TField |  |  |
| 14 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED6` | `FsGaWemExceptionCategory_Reserved6` | TField |  |  |
| 15 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED5` | `FsGaWemExceptionCategory_Reserved5` | TField |  |  |
| 16 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED4` | `FsGaWemExceptionCategory_Reserved4` | TField |  |  |
| 17 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED3` | `FsGaWemExceptionCategory_Reserved3` | TField |  |  |
| 18 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED2` | `FsGaWemExceptionCategory_Reserved2` | TField |  |  |
| 19 | `FS.GA.WEM.EXCEPTION.CATEGORY.RESERVED1` | `FsGaWemExceptionCategory_Reserved1` | TField |  |  |
| 20 | `FS.GA.WEM.EXCEPTION.CATEGORY.LOCAL.REF` | `FsGaWemExceptionCategory_LocalRef` |  |  |  |
| 21 | `FS.GA.WEM.EXCEPTION.CATEGORY.OVERRIDE` | `FsGaWemExceptionCategory_Override` |  |  |  |
| 22 | `FS.GA.WEM.EXCEPTION.CATEGORY.RECORD.STATUS` | `FsGaWemExceptionCategory_RecordStatus` | String |  |  |
| 23 | `FS.GA.WEM.EXCEPTION.CATEGORY.CURR.NO` | `FsGaWemExceptionCategory_CurrNo` | String |  |  |
| 24 | `FS.GA.WEM.EXCEPTION.CATEGORY.INPUTTER` | `FsGaWemExceptionCategory_Inputter` |  |  |  |
| 25 | `FS.GA.WEM.EXCEPTION.CATEGORY.DATE.TIME` | `FsGaWemExceptionCategory_DateTime` |  |  |  |
| 26 | `FS.GA.WEM.EXCEPTION.CATEGORY.AUTHORISER` | `FsGaWemExceptionCategory_Authoriser` | String |  |  |
| 27 | `FS.GA.WEM.EXCEPTION.CATEGORY.CO.CODE` | `FsGaWemExceptionCategory_CoCode` | String |  |  |
| 28 | `FS.GA.WEM.EXCEPTION.CATEGORY.DEPT.CODE` | `FsGaWemExceptionCategory_DeptCode` | String |  |  |
| 29 | `FS.GA.WEM.EXCEPTION.CATEGORY.AUDITOR.CODE` | `FsGaWemExceptionCategory_AuditorCode` | String |  |  |
| 30 | `FS.GA.WEM.EXCEPTION.CATEGORY.AUDIT.DATE.TIME` | `FsGaWemExceptionCategory_AuditDateTime` | String |  |  |
