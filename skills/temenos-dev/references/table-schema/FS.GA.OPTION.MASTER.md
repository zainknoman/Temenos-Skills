# FS.GA.OPTION.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.MASTER` in `FS_OptionMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.MASTER.PARENT.REF.ID` | `FsGaOptionMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.OPTION.MASTER.ORA.ROWID` | `FsGaOptionMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.OPTION.MASTER.OPTION.ID` | `FsGaOptionMaster_OptionId` | TField |  | Option Security ID Multifonds DB Column is NOPT. |
| 4 | `FS.GA.OPTION.MASTER.OPTION.TYPE` | `FsGaOptionMaster_OptionType` | TField |  | Option Type Call or Put Multifonds DB Column is TOPT. |
| 5 | `FS.GA.OPTION.MASTER.AMERICAN.OR.EUROPEAN.STYLE` | `FsGaOptionMaster_AmericanOrEuropeanStyle` | TField |  | American Or European Style For Option Multifonds DB Column is STYLE. |
| 6 | `FS.GA.OPTION.MASTER.UNDERLYING.RECEIVABLE` | `FsGaOptionMaster_UnderlyingReceivable` | TField |  | Underlying Recievable Multifonds DB Column is TUNDER. |
| 7 | `FS.GA.OPTION.MASTER.UNDERLYING.SECURITY` | `FsGaOptionMaster_UnderlyingSecurity` | TField |  | Underlying internal security number Multifonds DB Column is NUNDER. |
| 8 | `FS.GA.OPTION.MASTER.MATURITY.DATE` | `FsGaOptionMaster_MaturityDate` | TField |  | Maturity Date of an instrument, like for Bonds Multifonds DB Column is DATECH. |
| 9 | `FS.GA.OPTION.MASTER.OPTION.STRIKE.PRICE` | `FsGaOptionMaster_OptionStrikePrice` | TField |  | Option Strike Price Multifonds DB Column is STRIK. |
| 10 | `FS.GA.OPTION.MASTER.PRICE.PROVIDER` | `FsGaOptionMaster_PriceProvider` | TField |  | Price Provider Multifonds DB Column is TQUOTA. |
| 11 | `FS.GA.OPTION.MASTER.QUOTATION.PLACE` | `FsGaOptionMaster_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 12 | `FS.GA.OPTION.MASTER.GTI.CODE` | `FsGaOptionMaster_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 13 | `FS.GA.OPTION.MASTER.LOCAL.CURRENCY` | `FsGaOptionMaster_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 14 | `FS.GA.OPTION.MASTER.PRICING.FACTOR.CODE` | `FsGaOptionMaster_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 15 | `FS.GA.OPTION.MASTER.TQUANT` | `FsGaOptionMaster_Tquant` | TField |  | Tquant Multifonds DB Column is TQUANT. |
| 16 | `FS.GA.OPTION.MASTER.QUANTITY` | `FsGaOptionMaster_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 17 | `FS.GA.OPTION.MASTER.ORIGINAL.SYMBOL` | `FsGaOptionMaster_OriginalSymbol` | TField |  | Display the official ticker symbol or other useful information like contract size and maturity Multifonds DB Column is SYMB_ORI. |
| 18 | `FS.GA.OPTION.MASTER.CONTRACT.SIZE` | `FsGaOptionMaster_ContractSize` | TField |  | The contract size (if not zero) is used as a multiplier. Multifonds DB Column is FMULTI. |
| 19 | `FS.GA.OPTION.MASTER.OPTION.MARKET.VALUE` | `FsGaOptionMaster_OptionMarketValue` | TField |  | Option Market Value Multifonds DB Column is COURSOPS. |
| 20 | `FS.GA.OPTION.MASTER.DATE.OF.PRICE` | `FsGaOptionMaster_DateOfPrice` | TField |  | Value date of the securities prices Multifonds DB Column is DATECOURS. |
| 21 | `FS.GA.OPTION.MASTER.MIN.MARGIN.NAV.OPTIONS` | `FsGaOptionMaster_MinMarginNavOptions` | TField |  | Min Margin NAV for Options Multifonds DB Column is MARGIN. |
| 22 | `FS.GA.OPTION.MASTER.PERCENTAGE.VARIATION` | `FsGaOptionMaster_PercentageVariation` | TField |  | Variation of Price in Percentage Multifonds DB Column is PCTVAR. |
| 23 | `FS.GA.OPTION.MASTER.REPORTING.CODE` | `FsGaOptionMaster_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 24 | `FS.GA.OPTION.MASTER.OPTION.BID.MARKET.VALUE` | `FsGaOptionMaster_OptionBidMarketValue` | TField |  | Option Bid Market Value Multifonds DB Column is COURSOPS_BID. |
| 25 | `FS.GA.OPTION.MASTER.OPTION.OFFER.MARKET.VALUE` | `FsGaOptionMaster_OptionOfferMarketValue` | TField |  | Option Offer Market Value Multifonds DB Column is COURSOPS_OFFER. |
| 26 | `FS.GA.OPTION.MASTER.GUARANTOR.OR.ISSUER` | `FsGaOptionMaster_GuarantorOrIssuer` | TField |  | Guarantor Or Issuer Multifonds DB Column is NISSUER. |
| 27 | `FS.GA.OPTION.MASTER.NUMBER.OF.DAYS` | `FsGaOptionMaster_NumberOfDays` | TField |  | Compare variation D / Situation Date&apos; in the field &quot;Type&quot;. Then, it has to be completed with a number of days as of which the error message &quot;the difference is greater than X day&quot; will be prompted. Multifonds DB Column is NBJ_COURS. |
| 28 | `FS.GA.OPTION.MASTER.ISIN.CODE` | `FsGaOptionMaster_IsinCode` | TField |  | International security identification number (ISIN) Multifonds DB Column is CODISIN. |
| 29 | `FS.GA.OPTION.MASTER.ISIN.SEQUENCE` | `FsGaOptionMaster_IsinSequence` | TField |  | ISIN sequence of the security. Multifonds DB Column is SEQISIN. |
| 30 | `FS.GA.OPTION.MASTER.LOCALE.TYPE` | `FsGaOptionMaster_LocaleType` | TField |  | Local Type of granular information to query in Chart Charesteric screen Multifonds DB Column is COTLOCALE. |
| 31 | `FS.GA.OPTION.MASTER.COUNTERPARTY.CORRESPONDENT` | `FsGaOptionMaster_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 32 | `FS.GA.OPTION.MASTER.RATIO` | `FsGaOptionMaster_Ratio` | TField |  | Exercise Ratio between Option and underlying security. Also in futures it&apos;s used for French Year End Reporting Multifonds DB Column is RATIO. |
| 33 | `FS.GA.OPTION.MASTER.STATUS` | `FsGaOptionMaster_Status` | TField |  | It representing the status of the securiies if they are active are not,this field could corresponds to security,Future,options etc. Multifonds DB Column is ACTIF. |
| 34 | `FS.GA.OPTION.MASTER.DELTA.2` | `FsGaOptionMaster_Delta2` | TField |  | Delta-Difference 2 Multifonds DB Column is DELTA_2. |
| 35 | `FS.GA.OPTION.MASTER.DELTA` | `FsGaOptionMaster_Delta` | TField |  | Delta-Difference Multifonds DB Column is DELTA. |
| 36 | `FS.GA.OPTION.MASTER.SENSIBILITY` | `FsGaOptionMaster_Sensibility` | TField |  | Sensibility relates to security Multifonds DB Column is SENSIBILITY. |
| 37 | `FS.GA.OPTION.MASTER.BASKET.SECURITY.NUMBER` | `FsGaOptionMaster_BasketSecurityNumber` | TField |  | Basket Security Number Multifonds DB Column is NOVAL_BASKET. |
| 38 | `FS.GA.OPTION.MASTER.ARCHIVE` | `FsGaOptionMaster_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 39 | `FS.GA.OPTION.MASTER.REAL.EXPORT` | `FsGaOptionMaster_RealExport` | TField |  | Real Export Multifonds DB Column is REAL_EXPORT. |
| 40 | `FS.GA.OPTION.MASTER.STATE.CODE` | `FsGaOptionMaster_StateCode` | TField |  | Field is used to store the region type for Catastrophe bonds Multifonds DB Column is STATE_CODE. |
| 41 | `FS.GA.OPTION.MASTER.RISK.CODE` | `FsGaOptionMaster_RiskCode` | TField |  | This field is used to store the risk type for the Catastrophe bonds. Multifonds DB Column is CGTI_RISK. |
| 42 | `FS.GA.OPTION.MASTER.INSTRUMENT.CODE` | `FsGaOptionMaster_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 43 | `FS.GA.OPTION.MASTER.INSTRUMENT.CODE.2` | `FsGaOptionMaster_InstrumentCode2` | TField |  | This field is used for compliance purpose. This field is an alternative to Instrument code 1 (MIG21). It is country of incorporation whenever applicable. Multifonds DB Column is CINSTRUMENT2. |
| 44 | `FS.GA.OPTION.MASTER.NOTIF` | `FsGaOptionMaster_Notif` | TField |  | Notif Multifonds DB Column is FLG_NOTIF. |
| 45 | `FS.GA.OPTION.MASTER.USER.DEFINABLE.FIELDS.GROUP` | `FsGaOptionMaster_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 46 | `FS.GA.OPTION.MASTER.CURRENCY.CODE.OPTION` | `FsGaOptionMaster_CurrencyCodeOption` | TField |  | Currency code like EUR USD for Currency Options Multifonds DB Column is CMON_FX. |
| 47 | `FS.GA.OPTION.MASTER.REPORT.ASSET.TYPE` | `FsGaOptionMaster_ReportAssetType` | TField |  | Duplicate to Report Assest type (CODE_AT) Multifonds DB Column is REPORT_ASSET_TYPE. |
| 48 | `FS.GA.OPTION.MASTER.REPORT.ASSET.SUB.TYPE` | `FsGaOptionMaster_ReportAssetSubType` | TField |  | Duplicate to Report Assest type (CODE_AST) Multifonds DB Column is REPORT_ASSET_SUB_TYPE. |
| 49 | `FS.GA.OPTION.MASTER.PA.ASSET.CODE` | `FsGaOptionMaster_PaAssetCode` | TField |  | Pa Asset Code Multifonds DB Column is PA_ASSET_CODE. |
| 50 | `FS.GA.OPTION.MASTER.PA.ASSET.SUB.CODE` | `FsGaOptionMaster_PaAssetSubCode` | TField |  | Pa Asset Sub Code Multifonds DB Column is PA_ASSET_SUB_CODE. |
| 51 | `FS.GA.OPTION.MASTER.NA.ASSET.TYPE` | `FsGaOptionMaster_NaAssetType` | TField |  | Na Asset Type Multifonds DB Column is NA_ASSET_TYPE. |
| 52 | `FS.GA.OPTION.MASTER.NA.ASSET.SUB.TYPE` | `FsGaOptionMaster_NaAssetSubType` | TField |  | Na Asset Sub Type Multifonds DB Column is NA_ASSET_SUBTYPE. |
| 53 | `FS.GA.OPTION.MASTER.INSTRUMENT.GROUP` | `FsGaOptionMaster_InstrumentGroup` | TField |  | Instrument Group Multifonds DB Column is INSTRUMENT_GROUP. |
| 54 | `FS.GA.OPTION.MASTER.ASSET.TYPE.CODE` | `FsGaOptionMaster_AssetTypeCode` | TField |  | To enter Asset type for reporting. Multifonds DB Column is CODE_AT. |
| 55 | `FS.GA.OPTION.MASTER.ASSET.SUB.TYPE.CODE` | `FsGaOptionMaster_AssetSubTypeCode` | TField |  | To enter Asset sub type for reporting. Multifonds DB Column is CODE_AST. |
| 56 | `FS.GA.OPTION.MASTER.INSTRUMENT.TEMPLATE` | `FsGaOptionMaster_InstrumentTemplate` | TField |  | Instrument Template Multifonds DB Column is INST_TEMPLATE. |
| 57 | `FS.GA.OPTION.MASTER.RESERVED10` | `FsGaOptionMaster_Reserved10` | TField |  |  |
| 58 | `FS.GA.OPTION.MASTER.RESERVED9` | `FsGaOptionMaster_Reserved9` | TField |  |  |
| 59 | `FS.GA.OPTION.MASTER.RESERVED8` | `FsGaOptionMaster_Reserved8` | TField |  |  |
| 60 | `FS.GA.OPTION.MASTER.RESERVED7` | `FsGaOptionMaster_Reserved7` | TField |  |  |
| 61 | `FS.GA.OPTION.MASTER.RESERVED6` | `FsGaOptionMaster_Reserved6` | TField |  |  |
| 62 | `FS.GA.OPTION.MASTER.RESERVED5` | `FsGaOptionMaster_Reserved5` | TField |  |  |
| 63 | `FS.GA.OPTION.MASTER.RESERVED4` | `FsGaOptionMaster_Reserved4` | TField |  |  |
| 64 | `FS.GA.OPTION.MASTER.RESERVED3` | `FsGaOptionMaster_Reserved3` | TField |  |  |
| 65 | `FS.GA.OPTION.MASTER.RESERVED2` | `FsGaOptionMaster_Reserved2` | TField |  |  |
| 66 | `FS.GA.OPTION.MASTER.RESERVED1` | `FsGaOptionMaster_Reserved1` | TField |  |  |
| 67 | `FS.GA.OPTION.MASTER.LOCAL.REF` | `FsGaOptionMaster_LocalRef` |  |  |  |
| 68 | `FS.GA.OPTION.MASTER.OVERRIDE` | `FsGaOptionMaster_Override` |  |  |  |
| 69 | `FS.GA.OPTION.MASTER.RECORD.STATUS` | `FsGaOptionMaster_RecordStatus` | String |  |  |
| 70 | `FS.GA.OPTION.MASTER.CURR.NO` | `FsGaOptionMaster_CurrNo` | String |  |  |
| 71 | `FS.GA.OPTION.MASTER.INPUTTER` | `FsGaOptionMaster_Inputter` |  |  |  |
| 72 | `FS.GA.OPTION.MASTER.DATE.TIME` | `FsGaOptionMaster_DateTime` |  |  |  |
| 73 | `FS.GA.OPTION.MASTER.AUTHORISER` | `FsGaOptionMaster_Authoriser` | String |  |  |
| 74 | `FS.GA.OPTION.MASTER.CO.CODE` | `FsGaOptionMaster_CoCode` | String |  |  |
| 75 | `FS.GA.OPTION.MASTER.DEPT.CODE` | `FsGaOptionMaster_DeptCode` | String |  |  |
| 76 | `FS.GA.OPTION.MASTER.AUDITOR.CODE` | `FsGaOptionMaster_AuditorCode` | String |  |  |
| 77 | `FS.GA.OPTION.MASTER.AUDIT.DATE.TIME` | `FsGaOptionMaster_AuditDateTime` | String |  |  |
