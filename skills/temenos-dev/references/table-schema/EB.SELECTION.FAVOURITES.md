# EB.SELECTION.FAVOURITES — Table Schema

> Source: `INSERTS/I_F.EB.SELECTION.FAVOURITES` in `EB_BrowserEnquiry.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.EF.NAME` | `EbSelectionFavourites_Name` |  |  |  |
| 2 | `EB.EF.FIELD.NAME` | `EbSelectionFavourites_FieldName` |  |  |  |
| 3 | `EB.EF.OPERAND` | `EbSelectionFavourites_Operand` |  |  |  |
| 4 | `EB.EF.DATA` | `EbSelectionFavourites_Data` |  |  |  |
| 5 | `EB.EF.SORT.BY` | `EbSelectionFavourites_SortBy` |  |  |  |
| 6 | `EB.EF.RESERVED.10` | `EbSelectionFavourites_Reserved10` | TField |  |  |
| 7 | `EB.EF.RESERVED.9` | `EbSelectionFavourites_Reserved9` | TField |  |  |
| 8 | `EB.EF.RESERVED.8` | `EbSelectionFavourites_Reserved8` | TField |  |  |
| 9 | `EB.EF.RESERVED.7` | `EbSelectionFavourites_Reserved7` | TField |  |  |
| 10 | `EB.EF.RESERVED.6` | `EbSelectionFavourites_Reserved6` | TField |  |  |
| 11 | `EB.EF.RESERVED.5` | `EbSelectionFavourites_Reserved5` | TField |  |  |
| 12 | `EB.EF.RESERVED.4` | `EbSelectionFavourites_Reserved4` | TField |  |  |
| 13 | `EB.EF.RESERVED.3` | `EbSelectionFavourites_Reserved3` | TField |  |  |
| 14 | `EB.EF.RESERVED.2` | `EbSelectionFavourites_Reserved2` | TField |  |  |
| 15 | `EB.EF.RESERVED.1` | `EbSelectionFavourites_Reserved1` | TField |  |  |
| 16 | `EB.EF.LOCAL.REF` | `EbSelectionFavourites_LocalRef` |  |  |  |
| 17 | `EB.EF.RECORD.STATUS` | `EbSelectionFavourites_RecordStatus` | String |  |  |
| 18 | `EB.EF.CURR.NO` | `EbSelectionFavourites_CurrNo` | String |  |  |
| 19 | `EB.EF.INPUTTER` | `EbSelectionFavourites_Inputter` |  |  |  |
| 20 | `EB.EF.DATE.TIME` | `EbSelectionFavourites_DateTime` |  |  |  |
| 21 | `EB.EF.AUTHORISER` | `EbSelectionFavourites_Authoriser` | String |  |  |
| 22 | `EB.EF.CO.CODE` | `EbSelectionFavourites_CoCode` | String |  |  |
| 23 | `EB.EF.DEPT.CODE` | `EbSelectionFavourites_DeptCode` | String |  |  |
| 24 | `EB.EF.AUDITOR.CODE` | `EbSelectionFavourites_AuditorCode` | String |  |  |
| 25 | `EB.EF.AUDIT.DATE.TIME` | `EbSelectionFavourites_AuditDateTime` | String |  |  |
