# ASSET.REG.PROPERTY — Table Schema

> Source: `INSERTS/I_F.ASSET.REG.PROPERTY` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.PROP.DESCRIPTION` | `AssetRegProperty_Description` |  |  |  |
| 2 | `CO.PROP.CONTRACT.OF.SALE` | `AssetRegProperty_ContractOfSale` | TField |  | Legal Agreement ID or the Sale Deed ID of the Property. |
| 3 | `CO.PROP.ASSET.TYPE` | `AssetRegProperty_AssetType` | TField |  | This field specifies the Type of the property. For example, Residential Property, Commercial Property, Vacant land. |
| 4 | `CO.PROP.ASSET.ID` | `AssetRegProperty_AssetId` | TField |  | Unique identification number allotted to each Property. This ID is usually generated when the Property is registered with the Municipal authority. |
| 5 | `CO.PROP.ASSET.OWNER` | `AssetRegProperty_AssetOwner` |  |  |  |
| 6 | `CO.PROP.OWING.PERC` | `AssetRegProperty_OwingPerc` |  |  |  |
| 7 | `CO.PROP.RESERVED20` | `AssetRegProperty_Reserved20` |  |  |  |
| 8 | `CO.PROP.RESERVED19` | `AssetRegProperty_Reserved19` |  |  |  |
| 9 | `CO.PROP.RESERVED18` | `AssetRegProperty_Reserved18` |  |  |  |
| 10 | `CO.PROP.RESERVED17` | `AssetRegProperty_Reserved17` |  |  |  |
| 11 | `CO.PROP.RESERVED16` | `AssetRegProperty_Reserved16` |  |  |  |
| 12 | `CO.PROP.LEASE.ID` | `AssetRegProperty_LeaseId` |  |  |  |
| 13 | `CO.PROP.ORIG.OWNER` | `AssetRegProperty_OrigOwner` |  |  |  |
| 14 | `CO.PROP.LEASE.START.DATE` | `AssetRegProperty_LeaseStartDate` |  |  |  |
| 15 | `CO.PROP.LEASE.EXPIRY.DATE` | `AssetRegProperty_LeaseExpiryDate` |  |  |  |
| 16 | `CO.PROP.LEASE.TENOR` | `AssetRegProperty_LeaseTenor` |  |  |  |
| 17 | `CO.PROP.RENEWAL.RIGHT` | `AssetRegProperty_RenewalRight` |  |  |  |
| 18 | `CO.PROP.RENEWAL.TENOR` | `AssetRegProperty_RenewalTenor` |  |  |  |
| 19 | `CO.PROP.RESERVED15` | `AssetRegProperty_Reserved15` |  |  |  |
| 20 | `CO.PROP.RESERVED14` | `AssetRegProperty_Reserved14` |  |  |  |
| 21 | `CO.PROP.RESERVED13` | `AssetRegProperty_Reserved13` |  |  |  |
| 22 | `CO.PROP.RESERVED12` | `AssetRegProperty_Reserved12` |  |  |  |
| 23 | `CO.PROP.RESERVED11` | `AssetRegProperty_Reserved11` |  |  |  |
| 24 | `CO.PROP.LAND.REGISTRY.NO` | `AssetRegProperty_LandRegistryNo` | TField |  | A unique Title Number is allocated by the Land Registry to each and every property that is registered. |
| 25 | `CO.PROP.REGISTRATION.DATE` | `AssetRegProperty_RegistrationDate` | TField |  | Date when the Property was registered. |
| 26 | `CO.PROP.PLOT.NO.` | `AssetRegProperty_PlotNo` | TField |  | Plot number is the number allotted to the plot when it is mutated in municipal records. |
| 27 | `CO.PROP.SIZE` | `AssetRegProperty_Size` | TField |  | Size or the dimensions of the Property. |
| 28 | `CO.PROP.COUNTRY` | `AssetRegProperty_Country` | TField |  | Country where the property is located. |
| 29 | `CO.PROP.VILLAGE` | `AssetRegProperty_Village` | TField |  | Village where the property is located. |
| 30 | `CO.PROP.LOCATION` | `AssetRegProperty_Location` | TField |  | Specifies the location or direction where the property resides. For example, northern, eastern, southern or western region of the Village or Town or Country. |
| 31 | `CO.PROP.DISTRICT` | `AssetRegProperty_District` | TField |  | Specifies the district where the property is located. |
| 32 | `CO.PROP.POSTAL.CODE` | `AssetRegProperty_PostalCode` | TField |  | Postal code of the property. |
| 33 | `CO.PROP.STREET` | `AssetRegProperty_Street` | TField |  | Street name or Street number of the Property. |
| 34 | `CO.PROP.ADDRESS` | `AssetRegProperty_Address` |  |  |  |
| 35 | `CO.PROP.TOWN` | `AssetRegProperty_Town` | TField |  | Specifies the Property town. |
| 36 | `CO.PROP.ASSET.CURRENCY` | `AssetRegProperty_AssetCurrency` | TField | Yes | Currency in which the Property is valuated. Validation Rules: Mandatory field. |
| 37 | `CO.PROP.MARKET.VALUE` | `AssetRegProperty_MarketValue` | TField | Yes | Estimated amount or true underlying value of the Property. When the Property is pledged as Collateral, Market Value would be considered as the Fed value of the Collateral. Validation Rules: Mandatory field. |
| 38 | `CO.PROP.OPEN.MARKET.VALUE.CUR` | `AssetRegProperty_OpenMarketValueCur` | TField |  | Open market value of the Property currently that is the estimated amount that the property would sell for between a willing buyer and willing seller on the date of valuation. |
| 39 | `CO.PROP.OPEN.MARKET.VALUE.COMP` | `AssetRegProperty_OpenMarketValueComp` | TField |  | Open market value of the Property currently that is the estimated amount that the property would sell for between a willing buyer and willing seller on the date of valuation after the any sort of construction at property is over. |
| 40 | `CO.PROP.FORCED.SALE.VALUE.CUR` | `AssetRegProperty_ForcedSaleValueCur` | TField |  | Forced Sale Value of the property that is the estimated amount of the property during an unforeseen or uncontrollable event. |
| 41 | `CO.PROP.FORCED.SALE.VALUE.COMP` | `AssetRegProperty_ForcedSaleValueComp` | TField |  | Forced Sale Value of the property that is the estimated amount of the property during an unforeseen or uncontrollable event after completion of any sort construction at the property site. |
| 42 | `CO.PROP.COEFFICIENT` | `AssetRegProperty_Coefficient` | TField | No | Specifies the percentage of the Property value to be used for Collateral valuations. Validation Rules: Optional field. When left as blank, system will consider the rate as 100%. |
| 43 | `CO.PROP.ADJ.MARKET.VALUE` | `AssetRegProperty_AdjMarketValue` | TField |  | Value of the asset calculated by applying Coefficient percentage on the Market value. Validation Rules: NOINPUT field. Maintained by System. |
| 44 | `CO.PROP.SUG.ADJ.MARKET.VALUE` | `AssetRegProperty_SugAdjMarketValue` | TField | No | Property value that will be considered as the Margin value for Collateral Valuations. When the field is left as blank, system will default the value from ADJ.MARKET.VALUE field. Validation Rules: Up to 19-digit numeric, inclusive decimal point (amount format). Optional input. |
| 45 | `CO.PROP.START.DATE` | `AssetRegProperty_StartDate` | TField |  | Date when the Property was purchased or possessed Validation Rules: 11 digit Date format field. Default value is today's date. |
| 46 | `CO.PROP.EXPIRY.DATE` | `AssetRegProperty_ExpiryDate` | TField |  | Date from which the Property will not be treated as an asset. After 1 month of Expiry, Property records will be archived which can be controlled by modifying the Retention period in ARCHIVE record. |
| 47 | `CO.PROP.ASSET.RANK` | `AssetRegProperty_AssetRank` | TField |  | Rank of the Property. |
| 48 | `CO.PROP.NOTES` | `AssetRegProperty_Notes` |  |  |  |
| 49 | `CO.PROP.COLLATERAL.ID` | `AssetRegProperty_CollateralId` | TField |  | This field refers to the ID of the Collateral to which the Asset is linked. Validation Rules: NOINPUT field. Maintained by System. |
| 50 | `CO.PROP.RESERVED10` | `AssetRegProperty_Reserved10` |  |  |  |
| 51 | `CO.PROP.RESERVED9` | `AssetRegProperty_Reserved9` |  |  |  |
| 52 | `CO.PROP.RESERVED8` | `AssetRegProperty_Reserved8` |  |  |  |
| 53 | `CO.PROP.RESERVED7` | `AssetRegProperty_Reserved7` |  |  |  |
| 54 | `CO.PROP.RESERVED6` | `AssetRegProperty_Reserved6` |  |  |  |
| 55 | `CO.PROP.RESERVED5` | `AssetRegProperty_Reserved5` |  |  |  |
| 56 | `CO.PROP.RESERVED4` | `AssetRegProperty_Reserved4` |  |  |  |
| 57 | `CO.PROP.RESERVED3` | `AssetRegProperty_Reserved3` |  |  |  |
| 58 | `CO.PROP.RESERVED2` | `AssetRegProperty_Reserved2` |  |  |  |
| 59 | `CO.PROP.RESERVED1` | `AssetRegProperty_Reserved1` |  |  |  |
| 60 | `CO.PROP.LOCAL.REF` | `AssetRegProperty_LocalRef` |  |  |  |
| 61 | `CO.PROP.OVERRIDE` | `AssetRegProperty_Override` |  |  |  |
| 62 | `CO.PROP.RECORD.STATUS` | `AssetRegProperty_RecordStatus` | String |  |  |
| 63 | `CO.PROP.CURR.NO` | `AssetRegProperty_CurrNo` | String |  |  |
| 64 | `CO.PROP.INPUTTER` | `AssetRegProperty_Inputter` |  |  |  |
| 65 | `CO.PROP.DATE.TIME` | `AssetRegProperty_DateTime` |  |  |  |
| 66 | `CO.PROP.AUTHORISER` | `AssetRegProperty_Authoriser` | String |  |  |
| 67 | `CO.PROP.CO.CODE` | `AssetRegProperty_CoCode` | String |  |  |
| 68 | `CO.PROP.DEPT.CODE` | `AssetRegProperty_DeptCode` | String |  |  |
| 69 | `CO.PROP.AUDITOR.CODE` | `AssetRegProperty_AuditorCode` | String |  |  |
| 70 | `CO.PROP.AUDIT.DATE.TIME` | `AssetRegProperty_AuditDateTime` | String |  |  |
