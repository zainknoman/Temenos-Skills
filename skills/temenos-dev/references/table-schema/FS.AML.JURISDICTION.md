# FS.AML.JURISDICTION — Table Schema

> Source: `INSERTS/I_F.FS.AML.JURISDICTION` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.AML.JURISDICTION.DESCRIPTION` | `FsAmlJurisdiction_Description` |  |  |  |
| 2 | `FS.AML.JURISDICTION.FILTER.KEY` | `FsAmlJurisdiction_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.AML.JURISDICTION.RECORD.ID` | `FsAmlJurisdiction_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.AML.JURISDICTION.RESERVED10` | `FsAmlJurisdiction_Reserved10` | TField |  |  |
| 5 | `FS.AML.JURISDICTION.RESERVED9` | `FsAmlJurisdiction_Reserved9` | TField |  |  |
| 6 | `FS.AML.JURISDICTION.RESERVED8` | `FsAmlJurisdiction_Reserved8` | TField |  |  |
| 7 | `FS.AML.JURISDICTION.RESERVED7` | `FsAmlJurisdiction_Reserved7` | TField |  |  |
| 8 | `FS.AML.JURISDICTION.RESERVED6` | `FsAmlJurisdiction_Reserved6` | TField |  |  |
| 9 | `FS.AML.JURISDICTION.RESERVED5` | `FsAmlJurisdiction_Reserved5` | TField |  |  |
| 10 | `FS.AML.JURISDICTION.RESERVED4` | `FsAmlJurisdiction_Reserved4` | TField |  |  |
| 11 | `FS.AML.JURISDICTION.RESERVED3` | `FsAmlJurisdiction_Reserved3` | TField |  |  |
| 12 | `FS.AML.JURISDICTION.RESERVED2` | `FsAmlJurisdiction_Reserved2` | TField |  |  |
| 13 | `FS.AML.JURISDICTION.RESERVED1` | `FsAmlJurisdiction_Reserved1` | TField |  |  |
| 14 | `FS.AML.JURISDICTION.LOCAL.REF` | `FsAmlJurisdiction_LocalRef` |  |  |  |
| 15 | `FS.AML.JURISDICTION.OVERRIDE` | `FsAmlJurisdiction_Override` |  |  |  |
| 16 | `FS.AML.JURISDICTION.RECORD.STATUS` | `FsAmlJurisdiction_RecordStatus` | String |  |  |
| 17 | `FS.AML.JURISDICTION.CURR.NO` | `FsAmlJurisdiction_CurrNo` | String |  |  |
| 18 | `FS.AML.JURISDICTION.INPUTTER` | `FsAmlJurisdiction_Inputter` |  |  |  |
| 19 | `FS.AML.JURISDICTION.DATE.TIME` | `FsAmlJurisdiction_DateTime` |  |  |  |
| 20 | `FS.AML.JURISDICTION.AUTHORISER` | `FsAmlJurisdiction_Authoriser` | String |  |  |
| 21 | `FS.AML.JURISDICTION.CO.CODE` | `FsAmlJurisdiction_CoCode` | String |  |  |
| 22 | `FS.AML.JURISDICTION.DEPT.CODE` | `FsAmlJurisdiction_DeptCode` | String |  |  |
| 23 | `FS.AML.JURISDICTION.AUDITOR.CODE` | `FsAmlJurisdiction_AuditorCode` | String |  |  |
| 24 | `FS.AML.JURISDICTION.AUDIT.DATE.TIME` | `FsAmlJurisdiction_AuditDateTime` | String |  |  |
