# FS.QUOTATION.PLACE.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.QUOTATION.PLACE.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.QUOTATION.PLACE.TYPE.DESCRIPTION` | `FsQuotationPlaceType_Description` |  |  |  |
| 2 | `FS.QUOTATION.PLACE.TYPE.FILTER.KEY` | `FsQuotationPlaceType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.QUOTATION.PLACE.TYPE.RECORD.ID` | `FsQuotationPlaceType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.QUOTATION.PLACE.TYPE.RESERVED10` | `FsQuotationPlaceType_Reserved10` | TField |  |  |
| 5 | `FS.QUOTATION.PLACE.TYPE.RESERVED9` | `FsQuotationPlaceType_Reserved9` | TField |  |  |
| 6 | `FS.QUOTATION.PLACE.TYPE.RESERVED8` | `FsQuotationPlaceType_Reserved8` | TField |  |  |
| 7 | `FS.QUOTATION.PLACE.TYPE.RESERVED7` | `FsQuotationPlaceType_Reserved7` | TField |  |  |
| 8 | `FS.QUOTATION.PLACE.TYPE.RESERVED6` | `FsQuotationPlaceType_Reserved6` | TField |  |  |
| 9 | `FS.QUOTATION.PLACE.TYPE.RESERVED5` | `FsQuotationPlaceType_Reserved5` | TField |  |  |
| 10 | `FS.QUOTATION.PLACE.TYPE.RESERVED4` | `FsQuotationPlaceType_Reserved4` | TField |  |  |
| 11 | `FS.QUOTATION.PLACE.TYPE.RESERVED3` | `FsQuotationPlaceType_Reserved3` | TField |  |  |
| 12 | `FS.QUOTATION.PLACE.TYPE.RESERVED2` | `FsQuotationPlaceType_Reserved2` | TField |  |  |
| 13 | `FS.QUOTATION.PLACE.TYPE.RESERVED1` | `FsQuotationPlaceType_Reserved1` | TField |  |  |
| 14 | `FS.QUOTATION.PLACE.TYPE.LOCAL.REF` | `FsQuotationPlaceType_LocalRef` |  |  |  |
| 15 | `FS.QUOTATION.PLACE.TYPE.OVERRIDE` | `FsQuotationPlaceType_Override` |  |  |  |
| 16 | `FS.QUOTATION.PLACE.TYPE.RECORD.STATUS` | `FsQuotationPlaceType_RecordStatus` | String |  |  |
| 17 | `FS.QUOTATION.PLACE.TYPE.CURR.NO` | `FsQuotationPlaceType_CurrNo` | String |  |  |
| 18 | `FS.QUOTATION.PLACE.TYPE.INPUTTER` | `FsQuotationPlaceType_Inputter` |  |  |  |
| 19 | `FS.QUOTATION.PLACE.TYPE.DATE.TIME` | `FsQuotationPlaceType_DateTime` |  |  |  |
| 20 | `FS.QUOTATION.PLACE.TYPE.AUTHORISER` | `FsQuotationPlaceType_Authoriser` | String |  |  |
| 21 | `FS.QUOTATION.PLACE.TYPE.CO.CODE` | `FsQuotationPlaceType_CoCode` | String |  |  |
| 22 | `FS.QUOTATION.PLACE.TYPE.DEPT.CODE` | `FsQuotationPlaceType_DeptCode` | String |  |  |
| 23 | `FS.QUOTATION.PLACE.TYPE.AUDITOR.CODE` | `FsQuotationPlaceType_AuditorCode` | String |  |  |
| 24 | `FS.QUOTATION.PLACE.TYPE.AUDIT.DATE.TIME` | `FsQuotationPlaceType_AuditDateTime` | String |  |  |
