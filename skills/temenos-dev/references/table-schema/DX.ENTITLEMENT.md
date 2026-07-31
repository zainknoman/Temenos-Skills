# DX.ENTITLEMENT — Table Schema

> Source: `INSERTS/I_F.DX.ENTITLEMENT` in `DX_CorporateActions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.ENT.CUSTOMER` | `DxEntitlement_Customer` | TField |  | This field shows the customer code of the corporate action No input field - Defaults from DX.DIARY |
| 2 | `DX.ENT.PORTFOLIO` | `DxEntitlement_Portfolio` | TField |  | This field displays the portfolio number No input field - Defaults from DX.DIARY |
| 3 | `DX.ENT.SECURITY.NO` | `DxEntitlement_SecurityNo` | TField |  | This field displays the security number. No input field - Defaults from DX.DIARY |
| 4 | `DX.ENT.CONTRACT.CODE` | `DxEntitlement_ContractCode` | TField |  | This field shows the contract code before the corporate action No input field - Defaults from DX.DIARY |
| 5 | `DX.ENT.CURRENCY` | `DxEntitlement_Currency` | TField |  | This field shows the currency code for the corporate action No input field - Defaults from DX.DIARY |
| 6 | `DX.ENT.DESCRIPTION` | `DxEntitlement_Description` | TField |  | This field displays a description for the corporate action No input field - Defaults from DX.DIARY |
| 7 | `DX.ENT.NEW.SEC.NO` | `DxEntitlement_NewSecNo` | TField |  | This field displays the security number after the corporate action No input field - Defaults from DX.DIARY. |
| 8 | `DX.ENT.NEW.CONT.CODE` | `DxEntitlement_NewContCode` | TField |  | This field displays the contract code after the corporate action No input field |
| 9 | `DX.ENT.NEW.CONT.SIZE` | `DxEntitlement_NewContSize` | TField |  | This field displays the size of the resulting contract after the corporate action No input field - Defaults from DX.DIARY |
| 10 | `DX.ENT.SIZE.RATIO` | `DxEntitlement_SizeRatio` | TField |  | This field displays the size ratio after the corporate action shown as a ratio of New Size : Old Size No input field - Defaults from DX.DIARY |
| 11 | `DX.ENT.OLD.SIZE` | `DxEntitlement_OldSize` | TField |  | This field displays the contract size before the corporate action No input field - Defaults from DX.DIARY |
| 12 | `DX.ENT.NEW.SIZE` | `DxEntitlement_NewSize` | TField |  | This field displays the contract size after the corporate action No input field |
| 13 | `DX.ENT.STR.RATIO` | `DxEntitlement_StrRatio` | TField |  | This field displays the strike price ratio after the corporate action shown as a ratio of New Str Pri : Old Str Pri No input field - Defaults from DX.DIARY |
| 14 | `DX.ENT.LOT.RATIO` | `DxEntitlement_LotRatio` | TField |  | This field displays the lots ratio after the corporate action shown as a ratio of New Lots : Old Lots No input field |
| 15 | `DX.ENT.PRICE.RATIO` | `DxEntitlement_PriceRatio` | TField |  | This field displays price ratio after corporate action shown as a ratio of New Price : Old Price No input field |
| 16 | `DX.ENT.ROUNDING` | `DxEntitlement_Rounding` | TField |  | This field specifies the type of rounding method to be applied, which can be one of the following: STANDARD - Round either upwards or downwards whichever is nearer, to the required number of decimal places UP - Round upwards to the required number of decimal places DOWN - Round downwards to the required number of decimal places No input field - Defaults from DX.DIARY |
| 17 | `DX.ENT.RND.FACTOR` | `DxEntitlement_RndFactor` | TField |  | Rounding factor has the following restrictions on the integer and fractional part : 1. The fraction is restricted to the Strike price scale i.e. &lt; scale factor 2. Unless the Price Scale factor is 100, integer part cannot be used No input field - Defaults from DX.DIARY |
| 18 | `DX.ENT.MAT.DATE` | `DxEntitlement_MatDate` |  |  |  |
| 19 | `DX.ENT.CALL.PUT` | `DxEntitlement_CallPut` |  |  |  |
| 20 | `DX.ENT.OLD.STR.PRI` | `DxEntitlement_OldStrPri` |  |  |  |
| 21 | `DX.ENT.NEW.STR.PRI` | `DxEntitlement_NewStrPri` |  |  |  |
| 22 | `DX.ENT.TRADES` | `DxEntitlement_Trades` |  |  |  |
| 23 | `DX.ENT.BUY.SELL` | `DxEntitlement_BuySell` |  |  |  |
| 24 | `DX.ENT.OLD.LOTS` | `DxEntitlement_OldLots` |  |  |  |
| 25 | `DX.ENT.NEW.LOTS` | `DxEntitlement_NewLots` |  |  |  |
| 26 | `DX.ENT.OLD.PRICE` | `DxEntitlement_OldPrice` |  |  |  |
| 27 | `DX.ENT.NEW.PRICE` | `DxEntitlement_NewPrice` |  |  |  |
| 28 | `DX.ENT.EXOTIC.FIELD.NAME` | `DxEntitlement_ExoticFieldName` |  |  |  |
| 29 | `DX.ENT.EXOTIC.OLD.VALUE` | `DxEntitlement_ExoticOldValue` |  |  |  |
| 30 | `DX.ENT.EXOTIC.NEW.VALUE` | `DxEntitlement_ExoticNewValue` |  |  |  |
| 31 | `DX.ENT.MARKET.PRICE.ID` | `DxEntitlement_MarketPriceId` |  |  |  |
| 32 | `DX.ENT.RESERVED13` | `DxEntitlement_Reserved13` |  |  |  |
| 33 | `DX.ENT.RESERVED12` | `DxEntitlement_Reserved12` |  |  |  |
| 34 | `DX.ENT.RESERVED11` | `DxEntitlement_Reserved11` |  |  |  |
| 35 | `DX.ENT.RESERVED10` | `DxEntitlement_Reserved10` |  |  |  |
| 36 | `DX.ENT.RESERVED09` | `DxEntitlement_Reserved09` | TField |  |  |
| 37 | `DX.ENT.RESERVED08` | `DxEntitlement_Reserved08` | TField |  |  |
| 38 | `DX.ENT.RESERVED07` | `DxEntitlement_Reserved07` | TField |  |  |
| 39 | `DX.ENT.RESERVED06` | `DxEntitlement_Reserved06` | TField |  |  |
| 40 | `DX.ENT.RESERVED05` | `DxEntitlement_Reserved05` | TField |  |  |
| 41 | `DX.ENT.RESERVED4` | `DxEntitlement_Reserved4` | TField |  |  |
| 42 | `DX.ENT.RESERVED3` | `DxEntitlement_Reserved3` | TField |  |  |
| 43 | `DX.ENT.RESERVED2` | `DxEntitlement_Reserved2` | TField |  |  |
| 44 | `DX.ENT.RESERVED1` | `DxEntitlement_Reserved1` | TField |  |  |
| 45 | `DX.ENT.LOCAL.REF` | `DxEntitlement_LocalRef` |  |  |  |
| 46 | `DX.ENT.OVERRIDE` | `DxEntitlement_Override` |  |  |  |
| 47 | `DX.ENT.RECORD.STATUS` | `DxEntitlement_RecordStatus` | String |  |  |
| 48 | `DX.ENT.CURR.NO` | `DxEntitlement_CurrNo` | String |  |  |
| 49 | `DX.ENT.INPUTTER` | `DxEntitlement_Inputter` |  |  |  |
| 50 | `DX.ENT.DATE.TIME` | `DxEntitlement_DateTime` |  |  |  |
| 51 | `DX.ENT.AUTHORISER` | `DxEntitlement_Authoriser` | String |  |  |
| 52 | `DX.ENT.CO.CODE` | `DxEntitlement_CoCode` | String |  |  |
| 53 | `DX.ENT.DEPT.CODE` | `DxEntitlement_DeptCode` | String |  |  |
| 54 | `DX.ENT.AUDITOR.CODE` | `DxEntitlement_AuditorCode` | String |  |  |
| 55 | `DX.ENT.AUDIT.DATE.TIME` | `DxEntitlement_AuditDateTime` | String |  |  |
