# IS.COMMODITY — Table Schema

> Source: `INSERTS/I_F.IS.COMMODITY` in `IS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.COM.DESCRIPTION` | `IsCommodity_Description` |  |  |  |
| 2 | `IS.COM.STATUS` | `IsCommodity_Status` | TField | Yes | Defines the status of the commodity. The values to the field are defined in the EB.LOOKUP table with prefix &quot;IS.STATUS*&quot;. Validation Rules: 1. Valid values like Active, Inactive are defined in the EB.LOOKUP table with prefix &quot;IS.STATUS*&quot;. 2. Mandatory field. |
| 3 | `IS.COM.ASSET.TYPE` | `IsCommodity_AssetType` | TField | Yes | The type of the commodity defined. The named commodity are identical to Named Assets like Vehicle, etc. The quantified commodity are identical to commodities like tin, etc. Validation Rules: 1. Valid values are Named, Quantifiable. 2. Mandatory Input |
| 4 | `IS.COM.ASSET.TABLE` | `IsCommodity_AssetTable` | TField | Yes | The application in which the asset is defined. This application could be a regular or dynamic table. Validation rules: 1. Any valid application with PGM.TYPE &apos;H&apos; or &apos;D&apos;. 2. Mandatory input for Named Assets. |
| 5 | `IS.COM.ALLOWED.UNIT` | `IsCommodity_AllowedUnit` |  |  |  |
| 6 | `IS.COM.DECIMAL.QTY` | `IsCommodity_DecimalQty` |  |  |  |
| 7 | `IS.COM.CURRENCY` | `IsCommodity_Currency` | TField |  | The Currency in which the given commodity could be transacted in. This field is applicable only for Quantified Assets. Validation rules: 1. Must be a valid record from the table CURRENCY. |
| 8 | `IS.COM.BUY.BROKER` | `IsCommodity_BuyBroker` |  |  |  |
| 9 | `IS.COM.SELL.BROKER` | `IsCommodity_SellBroker` |  |  |  |
| 10 | `IS.COM.LOCATION` | `IsCommodity_Location` | TField |  | The location of the commodity. It could be the warehouse address or any other address where the commodity is present. Validation rules: 1. Standard T24 Alphanumeric field. 2. No-input field currently. Will be opened for user-input in future. |
| 11 | `IS.COM.COMMODITY.TYPE` | `IsCommodity_CommodityType` | TField |  | Denotes the commodity type if the commodity is transacted in local or international Validation rules: 1. Valid values are Local and International. 2. No-input field currently. Will be opened for user-input in future. |
| 12 | `IS.COM.MIN.THRESHOLD` | `IsCommodity_MinThreshold` | TField |  | The maximum quantity in unit(s) in which the commodity can be transacted. Validation rules: 1. Standard T24 numeric field. 2. No-input field currently. Will be opened for user-input in future. |
| 13 | `IS.COM.MAX.THRESHOLD` | `IsCommodity_MaxThreshold` | TField |  | The minimum quantity in unit(s) in which the commodity can be transacted. Validation rules: 1. Standard T24 numeric field 2. No-input field currently. Will be opened for user-input in future. |
| 14 | `IS.COM.TRACK.LIMIT` | `IsCommodity_TrackLimit` | TField |  | This is used to identify whether commodity/ broker limit tracking is required for the commodity or not. If check box is set then purchase application will track the commodity. Validation rules: 1. Values allowed are YES or NULL |
| 15 | `IS.COM.COM.DAILY.ALLWD.AMT` | `IsCommodity_ComDailyAllwdAmt` | TField |  | New field to define maximum daily allowed amount for commodity. |
| 16 | `IS.COM.MOV.TO.HIST.DAYS` | `IsCommodity_MovToHistDays` | TField |  | To define the number of calendar day�s application has to keep the data in LIVE file. Once number of calendar days is crossed, file data has to be removed from LIVE file or moved to archival file to keep file in optimal size. |
| 17 | `IS.COM.RESERVED.12` | `IsCommodity_Reserved12` | TField |  |  |
| 18 | `IS.COM.RESERVED.11` | `IsCommodity_Reserved11` | TField |  |  |
| 19 | `IS.COM.RESERVED.10` | `IsCommodity_Reserved10` | TField |  |  |
| 20 | `IS.COM.RESERVED.9` | `IsCommodity_Reserved9` | TField |  |  |
| 21 | `IS.COM.RESERVED.8` | `IsCommodity_Reserved8` | TField |  |  |
| 22 | `IS.COM.RESERVED.7` | `IsCommodity_Reserved7` | TField |  |  |
| 23 | `IS.COM.RESERVED.6` | `IsCommodity_Reserved6` | TField |  |  |
| 24 | `IS.COM.RESERVED.5` | `IsCommodity_Reserved5` | TField |  |  |
| 25 | `IS.COM.RESERVED.4` | `IsCommodity_Reserved4` | TField |  |  |
| 26 | `IS.COM.RESERVED.3` | `IsCommodity_Reserved3` | TField |  |  |
| 27 | `IS.COM.RESERVED.2` | `IsCommodity_Reserved2` | TField |  |  |
| 28 | `IS.COM.RESERVED.1` | `IsCommodity_Reserved1` | TField |  |  |
| 29 | `IS.COM.LOCAL.REF` | `IsCommodity_LocalRef` |  |  |  |
| 30 | `IS.COM.OVERRIDE` | `IsCommodity_Override` |  |  |  |
| 31 | `IS.COM.RECORD.STATUS` | `IsCommodity_RecordStatus` | String |  |  |
| 32 | `IS.COM.CURR.NO` | `IsCommodity_CurrNo` | String |  |  |
| 33 | `IS.COM.INPUTTER` | `IsCommodity_Inputter` |  |  |  |
| 34 | `IS.COM.DATE.TIME` | `IsCommodity_DateTime` |  |  |  |
| 35 | `IS.COM.AUTHORISER` | `IsCommodity_Authoriser` | String |  |  |
| 36 | `IS.COM.CO.CODE` | `IsCommodity_CoCode` | String |  |  |
| 37 | `IS.COM.DEPT.CODE` | `IsCommodity_DeptCode` | String |  |  |
| 38 | `IS.COM.AUDITOR.CODE` | `IsCommodity_AuditorCode` | String |  |  |
| 39 | `IS.COM.AUDIT.DATE.TIME` | `IsCommodity_AuditDateTime` | String |  |  |
| 40 | `IS.COM.UNIT.PRICE` | `IsCommodity_UnitPrice` |  |  |  |
| 41 | `IS.COM.DAILY.ALLWD.QTY` | `IsCommodity_DailyAllwdQty` |  |  |  |
| 42 | `IS.COM.DAILY.ALLWD.AMT` | `IsCommodity_DailyAllwdAmt` |  |  |  |
