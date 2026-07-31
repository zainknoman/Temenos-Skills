# DX.CONTRACT.TERMS — Table Schema

> Source: `INSERTS/I_F.DX.CONTRACT.TERMS` in `DX_Configuration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.CT.MNEMONIC` | `DxContractTerms_Mnemonic` | TField |  | Contains a unique short code for each terms. It is used for easy reference, identification and quick informationretrieval. |
| 2 | `DX.CT.UNIQUE.IDENTIFIER` | `DxContractTerms_UniqueIdentifier` | TField |  | Alternative index to identify the basket. |
| 3 | `DX.CT.ULYING.ASSET.CLASS` | `DxContractTerms_UlyingAssetClass` | TField |  | Indicates whether the underlying is security or currency basket. |
| 4 | `DX.CT.STATIC.LEG` | `DxContractTerms_StaticLeg` | TField |  | Choose the type of option from the drop down menu 'CALL' or 'PUT' CALL: Call currency should be same in all multi-value pairs PUT: Put currency should be same in all multi-value pairs |
| 5 | `DX.CT.BASKET.TYPE` | `DxContractTerms_BasketType` | TField |  | Indicates the type of basket. EQUITY OR CURRENCY |
| 6 | `DX.CT.PRICE.SOURCE` | `DxContractTerms_PriceSource` | TField |  | Identifier of a price interface known to T24. |
| 7 | `DX.CT.CALL.PUT` | `DxContractTerms_CallPut` | TField |  | Choose the type of option from the drop down menu 'CALL' or 'PUT' CALL: Confers upon the holder the right, but not obligation, to BUY stock at a fixed price at a future date PUT: Confers upon the holder the right, but not obligation, to SELL stock at a fixed price at a future date Validation Rules: Up to 4 alpha characters No Input unless TRADE.TYPE = "OPTION" Input must be either CALL/PUT |
| 8 | `DX.CT.TRADE.CCY` | `DxContractTerms_TradeCcy` | TField | Yes | Indicates the trading currency in this field. Choose from the drop down menu list. The input may be one of the following: - the user-defined alpha currency code - the user-defined numeric currency code Validation Rules: Mandatory field. Alpha format - This code will then comprise three alpha characters as defined in the currency table. It isrecommended to use the standard SWIFT currency code. The following are examples of ISO/SWIFT codes: - USD = US Dollars - GBP = Pounds Sterling - DEM = Deutsche Marks - FRF = French Francs 3 characters (uppercase alpha) - type SSS The currency code entered must appear in the Currency table. Dealing between LU'X' and BE'X' currency codes isprohibited. |
| 9 | `DX.CT.MATURITY.DATE` | `DxContractTerms_MaturityDate` | TField |  | The delivery period or prompt date of the contract transacted. Validation Rules: Up to 11 characters in DATE format |
| 10 | `DX.CT.SETTLEMENT.METHOD` | `DxContractTerms_SettlementMethod` | TField |  | The settlement mode of the option contract is specified in this field. The option can be physically settled(Delivery/Receipt of the underlying takes place )or Cash settled (The cash difference is settled). Possible valuesare PHYSICAL or CASH. NULL value would by default use physical settlement |
| 11 | `DX.CT.ULYING.SECURITY` | `DxContractTerms_UlyingSecurity` |  |  |  |
| 12 | `DX.CT.CALL.CCY` | `DxContractTerms_CallCcy` |  |  |  |
| 13 | `DX.CT.PUT.CCY` | `DxContractTerms_PutCcy` |  |  |  |
| 14 | `DX.CT.WEIGHT` | `DxContractTerms_Weight` |  |  |  |
| 15 | `DX.CT.STRIKE.PERCENTAGE` | `DxContractTerms_StrikePercentage` |  |  |  |
| 16 | `DX.CT.ULYING.STRIKE.CCY` | `DxContractTerms_UlyingStrikeCcy` |  |  |  |
| 17 | `DX.CT.ULYING.STRIKE.PRICE` | `DxContractTerms_UlyingStrikePrice` |  |  |  |
| 18 | `DX.CT.RISK.LEVEL` | `DxContractTerms_RiskLevel` | TField |  |  |
| 19 | `DX.CT.SUB.ASSET.TYPE` | `DxContractTerms_SubAssetType` | TField |  | Identifies the group of like Contracts, which are reported together. Validation Rules: 1-5 Alphanumeric characters , Valid Sub Asset type |
| 20 | `DX.CT.RESERVED.8` | `DxContractTerms_Reserved8` | TField |  |  |
| 21 | `DX.CT.RESERVED.7` | `DxContractTerms_Reserved7` | TField |  |  |
| 22 | `DX.CT.RESERVED.6` | `DxContractTerms_Reserved6` | TField |  |  |
| 23 | `DX.CT.RESERVED.5` | `DxContractTerms_Reserved5` | TField |  |  |
| 24 | `DX.CT.RESERVED.4` | `DxContractTerms_Reserved4` | TField |  |  |
| 25 | `DX.CT.RESERVED.3` | `DxContractTerms_Reserved3` | TField |  |  |
| 26 | `DX.CT.RESERVED.2` | `DxContractTerms_Reserved2` | TField |  |  |
| 27 | `DX.CT.RESERVED.1` | `DxContractTerms_Reserved1` | TField |  |  |
| 28 | `DX.CT.LOCAL.REF` | `DxContractTerms_LocalRef` |  |  |  |
| 29 | `DX.CT.OVERRIDE` | `DxContractTerms_Override` |  |  |  |
| 30 | `DX.CT.RECORD.STATUS` | `DxContractTerms_RecordStatus` | String |  |  |
| 31 | `DX.CT.CURR.NO` | `DxContractTerms_CurrNo` | String |  |  |
| 32 | `DX.CT.INPUTTER` | `DxContractTerms_Inputter` |  |  |  |
| 33 | `DX.CT.DATE.TIME` | `DxContractTerms_DateTime` |  |  |  |
| 34 | `DX.CT.AUTHORISER` | `DxContractTerms_Authoriser` | String |  |  |
| 35 | `DX.CT.CO.CODE` | `DxContractTerms_CoCode` | String |  |  |
| 36 | `DX.CT.DEPT.CODE` | `DxContractTerms_DeptCode` | String |  |  |
| 37 | `DX.CT.AUDITOR.CODE` | `DxContractTerms_AuditorCode` | String |  |  |
| 38 | `DX.CT.AUDIT.DATE.TIME` | `DxContractTerms_AuditDateTime` | String |  |  |
