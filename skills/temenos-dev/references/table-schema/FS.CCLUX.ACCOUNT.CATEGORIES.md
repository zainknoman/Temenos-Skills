# FS.CCLUX.ACCOUNT.CATEGORIES — Table Schema

> Source: `INSERTS/I_F.FS.CCLUX.ACCOUNT.CATEGORIES` in `FS_Common.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.CCLUX.ACCOUNT.CATEGORIES.DESCRIPTION` | `FsCcluxAccountCategories_Description` |  |  |  |
| 2 | `FS.CCLUX.ACCOUNT.CATEGORIES.FILTER.KEY` | `FsCcluxAccountCategories_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.CCLUX.ACCOUNT.CATEGORIES.RECORD.ID` | `FsCcluxAccountCategories_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED10` | `FsCcluxAccountCategories_Reserved10` | TField |  |  |
| 5 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED9` | `FsCcluxAccountCategories_Reserved9` | TField |  |  |
| 6 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED8` | `FsCcluxAccountCategories_Reserved8` | TField |  |  |
| 7 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED7` | `FsCcluxAccountCategories_Reserved7` | TField |  |  |
| 8 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED6` | `FsCcluxAccountCategories_Reserved6` | TField |  |  |
| 9 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED5` | `FsCcluxAccountCategories_Reserved5` | TField |  |  |
| 10 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED4` | `FsCcluxAccountCategories_Reserved4` | TField |  |  |
| 11 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED3` | `FsCcluxAccountCategories_Reserved3` | TField |  |  |
| 12 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED2` | `FsCcluxAccountCategories_Reserved2` | TField |  |  |
| 13 | `FS.CCLUX.ACCOUNT.CATEGORIES.RESERVED1` | `FsCcluxAccountCategories_Reserved1` | TField |  |  |
| 14 | `FS.CCLUX.ACCOUNT.CATEGORIES.LOCAL.REF` | `FsCcluxAccountCategories_LocalRef` |  |  |  |
| 15 | `FS.CCLUX.ACCOUNT.CATEGORIES.OVERRIDE` | `FsCcluxAccountCategories_Override` |  |  |  |
| 16 | `FS.CCLUX.ACCOUNT.CATEGORIES.RECORD.STATUS` | `FsCcluxAccountCategories_RecordStatus` | String |  |  |
| 17 | `FS.CCLUX.ACCOUNT.CATEGORIES.CURR.NO` | `FsCcluxAccountCategories_CurrNo` | String |  |  |
| 18 | `FS.CCLUX.ACCOUNT.CATEGORIES.INPUTTER` | `FsCcluxAccountCategories_Inputter` |  |  |  |
| 19 | `FS.CCLUX.ACCOUNT.CATEGORIES.DATE.TIME` | `FsCcluxAccountCategories_DateTime` |  |  |  |
| 20 | `FS.CCLUX.ACCOUNT.CATEGORIES.AUTHORISER` | `FsCcluxAccountCategories_Authoriser` | String |  |  |
| 21 | `FS.CCLUX.ACCOUNT.CATEGORIES.CO.CODE` | `FsCcluxAccountCategories_CoCode` | String |  |  |
| 22 | `FS.CCLUX.ACCOUNT.CATEGORIES.DEPT.CODE` | `FsCcluxAccountCategories_DeptCode` | String |  |  |
| 23 | `FS.CCLUX.ACCOUNT.CATEGORIES.AUDITOR.CODE` | `FsCcluxAccountCategories_AuditorCode` | String |  |  |
| 24 | `FS.CCLUX.ACCOUNT.CATEGORIES.AUDIT.DATE.TIME` | `FsCcluxAccountCategories_AuditDateTime` | String |  |  |
