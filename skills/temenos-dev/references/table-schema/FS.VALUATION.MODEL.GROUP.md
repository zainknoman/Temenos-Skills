# FS.VALUATION.MODEL.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.VALUATION.MODEL.GROUP` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.VALUATION.MODEL.GROUP.DESCRIPTION` | `FsValuationModelGroup_Description` |  |  |  |
| 2 | `FS.VALUATION.MODEL.GROUP.FILTER.KEY` | `FsValuationModelGroup_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.VALUATION.MODEL.GROUP.RECORD.ID` | `FsValuationModelGroup_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.VALUATION.MODEL.GROUP.RESERVED10` | `FsValuationModelGroup_Reserved10` | TField |  |  |
| 5 | `FS.VALUATION.MODEL.GROUP.RESERVED9` | `FsValuationModelGroup_Reserved9` | TField |  |  |
| 6 | `FS.VALUATION.MODEL.GROUP.RESERVED8` | `FsValuationModelGroup_Reserved8` | TField |  |  |
| 7 | `FS.VALUATION.MODEL.GROUP.RESERVED7` | `FsValuationModelGroup_Reserved7` | TField |  |  |
| 8 | `FS.VALUATION.MODEL.GROUP.RESERVED6` | `FsValuationModelGroup_Reserved6` | TField |  |  |
| 9 | `FS.VALUATION.MODEL.GROUP.RESERVED5` | `FsValuationModelGroup_Reserved5` | TField |  |  |
| 10 | `FS.VALUATION.MODEL.GROUP.RESERVED4` | `FsValuationModelGroup_Reserved4` | TField |  |  |
| 11 | `FS.VALUATION.MODEL.GROUP.RESERVED3` | `FsValuationModelGroup_Reserved3` | TField |  |  |
| 12 | `FS.VALUATION.MODEL.GROUP.RESERVED2` | `FsValuationModelGroup_Reserved2` | TField |  |  |
| 13 | `FS.VALUATION.MODEL.GROUP.RESERVED1` | `FsValuationModelGroup_Reserved1` | TField |  |  |
| 14 | `FS.VALUATION.MODEL.GROUP.LOCAL.REF` | `FsValuationModelGroup_LocalRef` |  |  |  |
| 15 | `FS.VALUATION.MODEL.GROUP.OVERRIDE` | `FsValuationModelGroup_Override` |  |  |  |
| 16 | `FS.VALUATION.MODEL.GROUP.RECORD.STATUS` | `FsValuationModelGroup_RecordStatus` | String |  |  |
| 17 | `FS.VALUATION.MODEL.GROUP.CURR.NO` | `FsValuationModelGroup_CurrNo` | String |  |  |
| 18 | `FS.VALUATION.MODEL.GROUP.INPUTTER` | `FsValuationModelGroup_Inputter` |  |  |  |
| 19 | `FS.VALUATION.MODEL.GROUP.DATE.TIME` | `FsValuationModelGroup_DateTime` |  |  |  |
| 20 | `FS.VALUATION.MODEL.GROUP.AUTHORISER` | `FsValuationModelGroup_Authoriser` | String |  |  |
| 21 | `FS.VALUATION.MODEL.GROUP.CO.CODE` | `FsValuationModelGroup_CoCode` | String |  |  |
| 22 | `FS.VALUATION.MODEL.GROUP.DEPT.CODE` | `FsValuationModelGroup_DeptCode` | String |  |  |
| 23 | `FS.VALUATION.MODEL.GROUP.AUDITOR.CODE` | `FsValuationModelGroup_AuditorCode` | String |  |  |
| 24 | `FS.VALUATION.MODEL.GROUP.AUDIT.DATE.TIME` | `FsValuationModelGroup_AuditDateTime` | String |  |  |
