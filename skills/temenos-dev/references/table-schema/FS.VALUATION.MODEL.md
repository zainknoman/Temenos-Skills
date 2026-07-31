# FS.VALUATION.MODEL — Table Schema

> Source: `INSERTS/I_F.FS.VALUATION.MODEL` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.VALUATION.MODEL.DESCRIPTION` | `FsValuationModel_Description` |  |  |  |
| 2 | `FS.VALUATION.MODEL.FILTER.KEY` | `FsValuationModel_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.VALUATION.MODEL.RECORD.ID` | `FsValuationModel_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.VALUATION.MODEL.RESERVED10` | `FsValuationModel_Reserved10` | TField |  |  |
| 5 | `FS.VALUATION.MODEL.RESERVED9` | `FsValuationModel_Reserved9` | TField |  |  |
| 6 | `FS.VALUATION.MODEL.RESERVED8` | `FsValuationModel_Reserved8` | TField |  |  |
| 7 | `FS.VALUATION.MODEL.RESERVED7` | `FsValuationModel_Reserved7` | TField |  |  |
| 8 | `FS.VALUATION.MODEL.RESERVED6` | `FsValuationModel_Reserved6` | TField |  |  |
| 9 | `FS.VALUATION.MODEL.RESERVED5` | `FsValuationModel_Reserved5` | TField |  |  |
| 10 | `FS.VALUATION.MODEL.RESERVED4` | `FsValuationModel_Reserved4` | TField |  |  |
| 11 | `FS.VALUATION.MODEL.RESERVED3` | `FsValuationModel_Reserved3` | TField |  |  |
| 12 | `FS.VALUATION.MODEL.RESERVED2` | `FsValuationModel_Reserved2` | TField |  |  |
| 13 | `FS.VALUATION.MODEL.RESERVED1` | `FsValuationModel_Reserved1` | TField |  |  |
| 14 | `FS.VALUATION.MODEL.LOCAL.REF` | `FsValuationModel_LocalRef` |  |  |  |
| 15 | `FS.VALUATION.MODEL.OVERRIDE` | `FsValuationModel_Override` |  |  |  |
| 16 | `FS.VALUATION.MODEL.RECORD.STATUS` | `FsValuationModel_RecordStatus` | String |  |  |
| 17 | `FS.VALUATION.MODEL.CURR.NO` | `FsValuationModel_CurrNo` | String |  |  |
| 18 | `FS.VALUATION.MODEL.INPUTTER` | `FsValuationModel_Inputter` |  |  |  |
| 19 | `FS.VALUATION.MODEL.DATE.TIME` | `FsValuationModel_DateTime` |  |  |  |
| 20 | `FS.VALUATION.MODEL.AUTHORISER` | `FsValuationModel_Authoriser` | String |  |  |
| 21 | `FS.VALUATION.MODEL.CO.CODE` | `FsValuationModel_CoCode` | String |  |  |
| 22 | `FS.VALUATION.MODEL.DEPT.CODE` | `FsValuationModel_DeptCode` | String |  |  |
| 23 | `FS.VALUATION.MODEL.AUDITOR.CODE` | `FsValuationModel_AuditorCode` | String |  |  |
| 24 | `FS.VALUATION.MODEL.AUDIT.DATE.TIME` | `FsValuationModel_AuditDateTime` | String |  |  |
