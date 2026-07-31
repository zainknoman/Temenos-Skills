# DX.PRICE.SOURCE — Table Schema

> Source: `INSERTS/I_F.DX.PRICE.SOURCE` in `DX_Pricing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.PS.SHORT.DESC` | `DxPriceSource_ShortDesc` | TField | Yes | Please enter a short description that applies to this price source. This is used for enrichment, enquires and reporting purposes only. Validation Rules: 35 characters, alphanumeric Mandatory input. |
| 2 | `DX.PS.DESCRIPTION` | `DxPriceSource_Description` |  |  |  |
| 3 | `DX.PS.PROGRAM` | `DxPriceSource_Program` | TField |  | This field specifies the program (if any) that returns the price for a unique contract. In this context, the way the routine obtains the price is irrelevant whether it be an extraction from a datafile, a link to an external source or a price calculation routine. Input must be a valid program name in the PGM.FILE application Validation Rules: Up to 35 characters Input must be a valid record on the PGM.FILE Application Must exsist as a OBJECT.TYPE of "BLACK BOX" for application DX.PRICE.SOURCE. |
| 4 | `DX.PS.STOP.UPDATES` | `DxPriceSource_StopUpdates` | TField |  | This field is no longer used/required for processing in the derivatives module. Validation Rules: No Input |
| 5 | `DX.PS.CONS.DATA.NAME` | `DxPriceSource_ConsDataName` |  |  |  |
| 6 | `DX.PS.CONS.DATA.ITEM` | `DxPriceSource_ConsDataItem` |  |  |  |
| 7 | `DX.PS.RESERVED8` | `DxPriceSource_Reserved8` |  |  |  |
| 8 | `DX.PS.RESERVED7` | `DxPriceSource_Reserved7` |  |  |  |
| 9 | `DX.PS.UPDATE.AVAIL` | `DxPriceSource_UpdateAvail` | TField |  | Can this source provide an updated price on demand YES or NO Validation Rules: 3,2 Alpha YES/NO |
| 10 | `DX.PS.BUILD.PGM` | `DxPriceSource_BuildPgm` |  |  |  |
| 11 | `DX.PS.GARMAN.NODIV.RISK` | `DxPriceSource_GarmanNodivRisk` | TField |  | Field has been made obsolete. |
| 12 | `DX.PS.TIME.TO.EXPIRY` | `DxPriceSource_TimeToExpiry` | TField |  | This field is used to define the days to be considered, either Working (W) or Calendar (C) to arrive at the value in the field TIME.TO.EXPIRY of the table DX.MARKET.PRICE. Possible values are 'W' for working days and 'C' for calendar days. Default value is 'W'. |
| 13 | `DX.PS.RESERVED2` | `DxPriceSource_Reserved2` | TField |  | Reserved For Future Use Validation Rules: No Input Field |
| 14 | `DX.PS.RESERVED1` | `DxPriceSource_Reserved1` | TField |  | Reserved For Future Use Validation Rules: No Input Field |
| 15 | `DX.PS.RECORD.STATUS` | `DxPriceSource_RecordStatus` | String |  |  |
| 16 | `DX.PS.CURR.NO` | `DxPriceSource_CurrNo` | String |  |  |
| 17 | `DX.PS.INPUTTER` | `DxPriceSource_Inputter` |  |  |  |
| 18 | `DX.PS.DATE.TIME` | `DxPriceSource_DateTime` |  |  |  |
| 19 | `DX.PS.AUTHORISER` | `DxPriceSource_Authoriser` | String |  |  |
| 20 | `DX.PS.CO.CODE` | `DxPriceSource_CoCode` | String |  |  |
| 21 | `DX.PS.DEPT.CODE` | `DxPriceSource_DeptCode` | String |  |  |
| 22 | `DX.PS.AUDITOR.CODE` | `DxPriceSource_AuditorCode` | String |  |  |
| 23 | `DX.PS.AUDIT.DATE.TIME` | `DxPriceSource_AuditDateTime` | String |  |  |
