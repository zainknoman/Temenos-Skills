# FS.QUOTATION.PLACE — Table Schema

> Source: `INSERTS/I_F.FS.QUOTATION.PLACE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.QUOTATION.PLACE.DESCRIPTION` | `FsQuotationPlace_Description` |  |  |  |
| 2 | `FS.QUOTATION.PLACE.FILTER.KEY` | `FsQuotationPlace_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.QUOTATION.PLACE.RECORD.ID` | `FsQuotationPlace_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.QUOTATION.PLACE.RESERVED10` | `FsQuotationPlace_Reserved10` | TField |  |  |
| 5 | `FS.QUOTATION.PLACE.RESERVED9` | `FsQuotationPlace_Reserved9` | TField |  |  |
| 6 | `FS.QUOTATION.PLACE.RESERVED8` | `FsQuotationPlace_Reserved8` | TField |  |  |
| 7 | `FS.QUOTATION.PLACE.RESERVED7` | `FsQuotationPlace_Reserved7` | TField |  |  |
| 8 | `FS.QUOTATION.PLACE.RESERVED6` | `FsQuotationPlace_Reserved6` | TField |  |  |
| 9 | `FS.QUOTATION.PLACE.RESERVED5` | `FsQuotationPlace_Reserved5` | TField |  |  |
| 10 | `FS.QUOTATION.PLACE.RESERVED4` | `FsQuotationPlace_Reserved4` | TField |  |  |
| 11 | `FS.QUOTATION.PLACE.RESERVED3` | `FsQuotationPlace_Reserved3` | TField |  |  |
| 12 | `FS.QUOTATION.PLACE.RESERVED2` | `FsQuotationPlace_Reserved2` | TField |  |  |
| 13 | `FS.QUOTATION.PLACE.RESERVED1` | `FsQuotationPlace_Reserved1` | TField |  |  |
| 14 | `FS.QUOTATION.PLACE.LOCAL.REF` | `FsQuotationPlace_LocalRef` |  |  |  |
| 15 | `FS.QUOTATION.PLACE.OVERRIDE` | `FsQuotationPlace_Override` |  |  |  |
| 16 | `FS.QUOTATION.PLACE.RECORD.STATUS` | `FsQuotationPlace_RecordStatus` | String |  |  |
| 17 | `FS.QUOTATION.PLACE.CURR.NO` | `FsQuotationPlace_CurrNo` | String |  |  |
| 18 | `FS.QUOTATION.PLACE.INPUTTER` | `FsQuotationPlace_Inputter` |  |  |  |
| 19 | `FS.QUOTATION.PLACE.DATE.TIME` | `FsQuotationPlace_DateTime` |  |  |  |
| 20 | `FS.QUOTATION.PLACE.AUTHORISER` | `FsQuotationPlace_Authoriser` | String |  |  |
| 21 | `FS.QUOTATION.PLACE.CO.CODE` | `FsQuotationPlace_CoCode` | String |  |  |
| 22 | `FS.QUOTATION.PLACE.DEPT.CODE` | `FsQuotationPlace_DeptCode` | String |  |  |
| 23 | `FS.QUOTATION.PLACE.AUDITOR.CODE` | `FsQuotationPlace_AuditorCode` | String |  |  |
| 24 | `FS.QUOTATION.PLACE.AUDIT.DATE.TIME` | `FsQuotationPlace_AuditDateTime` | String |  |  |
