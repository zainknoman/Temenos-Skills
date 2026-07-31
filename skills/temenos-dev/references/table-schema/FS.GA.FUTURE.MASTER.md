# FS.GA.FUTURE.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.MASTER` in `FS_FutureMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.MASTER.PARENT.REF.ID` | `FsGaFutureMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.MASTER.ORA.ROWID` | `FsGaFutureMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.MASTER.FUTURE.ID.CODE` | `FsGaFutureMaster_FutureIdCode` | TField |  | Future, Security,Swap,Derivative,CFD ID Code Multifonds DB Column is NFUT. |
| 4 | `FS.GA.FUTURE.MASTER.INTERNAL.SECURITY.ID` | `FsGaFutureMaster_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.FUTURE.MASTER.MATURITY.DATE` | `FsGaFutureMaster_MaturityDate` | TField |  | Maturity Date of an instrument, like for Bonds Multifonds DB Column is DATECH. |
| 6 | `FS.GA.FUTURE.MASTER.FIRST.NOTICED.DATE` | `FsGaFutureMaster_FirstNoticedDate` | TField |  | Date as of which the future will honor delivery Multifonds DB Column is DNOTICE. |
| 7 | `FS.GA.FUTURE.MASTER.PRICE.PROVIDER` | `FsGaFutureMaster_PriceProvider` | TField |  | Price Provider Multifonds DB Column is TQUOTA. |
| 8 | `FS.GA.FUTURE.MASTER.QUOTATION.PLACE` | `FsGaFutureMaster_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 9 | `FS.GA.FUTURE.MASTER.GTI.CODE` | `FsGaFutureMaster_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 10 | `FS.GA.FUTURE.MASTER.AMERICAN.OR.EUROPEAN.STYLE` | `FsGaFutureMaster_AmericanOrEuropeanStyle` | TField |  | American Or European Style For Option Multifonds DB Column is STYLE. |
| 11 | `FS.GA.FUTURE.MASTER.LOCAL.CURRENCY` | `FsGaFutureMaster_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 12 | `FS.GA.FUTURE.MASTER.TQUANT` | `FsGaFutureMaster_Tquant` | TField |  | Tquant Multifonds DB Column is TQUANT. |
| 13 | `FS.GA.FUTURE.MASTER.QUANTITY` | `FsGaFutureMaster_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 14 | `FS.GA.FUTURE.MASTER.ORIGINAL.SYMBOL` | `FsGaFutureMaster_OriginalSymbol` | TField |  | Display the official ticker symbol or other useful information like contract size and maturity Multifonds DB Column is SYMB_ORI. |
| 15 | `FS.GA.FUTURE.MASTER.CONTRACT.SIZE` | `FsGaFutureMaster_ContractSize` | TField |  | The contract size (if not zero) is used as a multiplier. Multifonds DB Column is FMULTI. |
| 16 | `FS.GA.FUTURE.MASTER.INITIAL.MARGIN` | `FsGaFutureMaster_InitialMargin` | TField |  | MultiFonds is able to compute the initial margin to be deposited with each opening or closing transaction. Enter the initial margin to be deposited per contract. Multifonds DB Column is MARG_INIT. |
| 17 | `FS.GA.FUTURE.MASTER.MINIMUM.MARGIN` | `FsGaFutureMaster_MinimumMargin` | TField |  | Minimum Margin Multifonds DB Column is MARG_MIN. |
| 18 | `FS.GA.FUTURE.MASTER.CREATE.DATE` | `FsGaFutureMaster_CreateDate` | TField |  | Create Date Multifonds DB Column is CREADATE. |
| 19 | `FS.GA.FUTURE.MASTER.REPORTING.CODE` | `FsGaFutureMaster_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 20 | `FS.GA.FUTURE.MASTER.GUARANTOR.OR.ISSUER` | `FsGaFutureMaster_GuarantorOrIssuer` | TField |  | Guarantor Or Issuer Multifonds DB Column is NISSUER. |
| 21 | `FS.GA.FUTURE.MASTER.ISIN.CODE` | `FsGaFutureMaster_IsinCode` | TField |  | International security identification number (ISIN) Multifonds DB Column is CODISIN. |
| 22 | `FS.GA.FUTURE.MASTER.ISIN.SEQUENCE` | `FsGaFutureMaster_IsinSequence` | TField |  | ISIN sequence of the security. Multifonds DB Column is SEQISIN. |
| 23 | `FS.GA.FUTURE.MASTER.FUTURE.MARKET.VALUE` | `FsGaFutureMaster_FutureMarketValue` | TField |  | Future Market Value Multifonds DB Column is COURSFUT. |
| 24 | `FS.GA.FUTURE.MASTER.DATE.OF.PRICE` | `FsGaFutureMaster_DateOfPrice` | TField |  | Value date of the securities prices Multifonds DB Column is DATECOURS. |
| 25 | `FS.GA.FUTURE.MASTER.FUTURE.BID.MARKET.VALUE` | `FsGaFutureMaster_FutureBidMarketValue` | TField |  | Future BID Market Value Multifonds DB Column is COURSFUT_BID. |
| 26 | `FS.GA.FUTURE.MASTER.FUTURE.OFFER.MARKET.VALUE` | `FsGaFutureMaster_FutureOfferMarketValue` | TField |  | Future Offer Market Value Multifonds DB Column is COURSFUT_OFFER. |
| 27 | `FS.GA.FUTURE.MASTER.PREVIOUS.COURS.DATE` | `FsGaFutureMaster_PreviousCoursDate` | TField |  | Previous Cours Date Multifonds DB Column is DATE_COURS_PREC. |
| 28 | `FS.GA.FUTURE.MASTER.ACTUAL.COURS.DATE` | `FsGaFutureMaster_ActualCoursDate` | TField |  | Actual Cours Date Multifonds DB Column is DATE_COURS_ACTUEL. |
| 29 | `FS.GA.FUTURE.MASTER.PERCENTAGE.VARIATION` | `FsGaFutureMaster_PercentageVariation` | TField |  | Variation of Price in Percentage Multifonds DB Column is PCTVAR. |
| 30 | `FS.GA.FUTURE.MASTER.CONVERSION.FACTOR` | `FsGaFutureMaster_ConversionFactor` | TField |  | Conversion Factor Multifonds DB Column is CONVERSION_FACTOR. |
| 31 | `FS.GA.FUTURE.MASTER.LOCALE.TYPE` | `FsGaFutureMaster_LocaleType` | TField |  | Local Type of granular information to query in Chart Charesteric screen Multifonds DB Column is COTLOCALE. |
| 32 | `FS.GA.FUTURE.MASTER.COUNTERPARTY.CORRESPONDENT` | `FsGaFutureMaster_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 33 | `FS.GA.FUTURE.MASTER.RATIO` | `FsGaFutureMaster_Ratio` | TField |  | Exercise Ratio between Option and underlying security. Also in futures it&apos;s used for French Year End Reporting Multifonds DB Column is RATIO. |
| 34 | `FS.GA.FUTURE.MASTER.BASKET.SECURITY.NUMBER` | `FsGaFutureMaster_BasketSecurityNumber` | TField |  | Basket Security Number Multifonds DB Column is NOVAL_BASKET. |
| 35 | `FS.GA.FUTURE.MASTER.STATUS` | `FsGaFutureMaster_Status` | TField |  | It representing the status of the securiies if they are active are not,this field could corresponds to security,Future,options etc. Multifonds DB Column is ACTIF. |
| 36 | `FS.GA.FUTURE.MASTER.SENSIBILITY` | `FsGaFutureMaster_Sensibility` | TField |  | Sensibility relates to security Multifonds DB Column is SENSIBILITY. |
| 37 | `FS.GA.FUTURE.MASTER.PRICING.FACTOR.CODE` | `FsGaFutureMaster_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 38 | `FS.GA.FUTURE.MASTER.INTEREST.RATE` | `FsGaFutureMaster_InterestRate` | TField |  | Interest rate applicable on the interest bearing instrument in the transaction Multifonds DB Column is TXINT. |
| 39 | `FS.GA.FUTURE.MASTER.CONTRACT.TERM` | `FsGaFutureMaster_ContractTerm` | TField |  | Contract Term Multifonds DB Column is CTERM. |
| 40 | `FS.GA.FUTURE.MASTER.AU.ROUNDING` | `FsGaFutureMaster_AuRounding` | TField |  | AU Rounding Multifonds DB Column is AU_ROUND. |
| 41 | `FS.GA.FUTURE.MASTER.ARCHIVE` | `FsGaFutureMaster_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 42 | `FS.GA.FUTURE.MASTER.REAL.EXPORT` | `FsGaFutureMaster_RealExport` | TField |  | Real Export Multifonds DB Column is REAL_EXPORT. |
| 43 | `FS.GA.FUTURE.MASTER.STATE.CODE` | `FsGaFutureMaster_StateCode` | TField |  | Field is used to store the region type for Catastrophe bonds Multifonds DB Column is STATE_CODE. |
| 44 | `FS.GA.FUTURE.MASTER.RISK.CODE` | `FsGaFutureMaster_RiskCode` | TField |  | This field is used to store the risk type for the Catastrophe bonds. Multifonds DB Column is CGTI_RISK. |
| 45 | `FS.GA.FUTURE.MASTER.INSTRUMENT.CODE` | `FsGaFutureMaster_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 46 | `FS.GA.FUTURE.MASTER.INSTRUMENT.CODE.2` | `FsGaFutureMaster_InstrumentCode2` | TField |  | This field is used for compliance purpose. This field is an alternative to Instrument code 1 (MIG21). It is country of incorporation whenever applicable. Multifonds DB Column is CINSTRUMENT2. |
| 47 | `FS.GA.FUTURE.MASTER.MARGIN.TYPE` | `FsGaFutureMaster_MarginType` | TField |  | Margin Type Multifonds DB Column is TYP_MARG. |
| 48 | `FS.GA.FUTURE.MASTER.UNDERLYING.SEC` | `FsGaFutureMaster_UnderlyingSec` | TField |  | Underlying Security Multifonds DB Column is UN_NOVAL. |
| 49 | `FS.GA.FUTURE.MASTER.UNDERLYING.RECEIVABLE` | `FsGaFutureMaster_UnderlyingReceivable` | TField |  | Underlying Recievable Multifonds DB Column is TUNDER. |
| 50 | `FS.GA.FUTURE.MASTER.EXPIRY.DATE.OF.INSTRUMENT` | `FsGaFutureMaster_ExpiryDateOfInstrument` | TField |  | Expiry Date Of Instrument Multifonds DB Column is DATECH_SEC_FWD. |
| 51 | `FS.GA.FUTURE.MASTER.NOTIF` | `FsGaFutureMaster_Notif` | TField |  | Notif Multifonds DB Column is FLG_NOTIF. |
| 52 | `FS.GA.FUTURE.MASTER.USER.DEFINABLE.FIELDS.GROUP` | `FsGaFutureMaster_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 53 | `FS.GA.FUTURE.MASTER.REPORT.ASSET.TYPE` | `FsGaFutureMaster_ReportAssetType` | TField |  | Duplicate to Report Assest type (CODE_AT) Multifonds DB Column is REPORT_ASSET_TYPE. |
| 54 | `FS.GA.FUTURE.MASTER.REPORT.ASSET.SUB.TYPE` | `FsGaFutureMaster_ReportAssetSubType` | TField |  | Duplicate to Report Assest type (CODE_AST) Multifonds DB Column is REPORT_ASSET_SUB_TYPE. |
| 55 | `FS.GA.FUTURE.MASTER.PA.ASSET.CODE` | `FsGaFutureMaster_PaAssetCode` | TField |  | Pa Asset Code Multifonds DB Column is PA_ASSET_CODE. |
| 56 | `FS.GA.FUTURE.MASTER.PA.ASSET.SUB.CODE` | `FsGaFutureMaster_PaAssetSubCode` | TField |  | Pa Asset Sub Code Multifonds DB Column is PA_ASSET_SUB_CODE. |
| 57 | `FS.GA.FUTURE.MASTER.NA.ASSET.TYPE` | `FsGaFutureMaster_NaAssetType` | TField |  | Na Asset Type Multifonds DB Column is NA_ASSET_TYPE. |
| 58 | `FS.GA.FUTURE.MASTER.NA.ASSET.SUB.TYPE` | `FsGaFutureMaster_NaAssetSubType` | TField |  | Na Asset Sub Type Multifonds DB Column is NA_ASSET_SUBTYPE. |
| 59 | `FS.GA.FUTURE.MASTER.INSTRUMENT.GROUP` | `FsGaFutureMaster_InstrumentGroup` | TField |  | Instrument Group Multifonds DB Column is INSTRUMENT_GROUP. |
| 60 | `FS.GA.FUTURE.MASTER.ASSET.TYPE.CODE` | `FsGaFutureMaster_AssetTypeCode` | TField |  | To enter Asset type for reporting. Multifonds DB Column is CODE_AT. |
| 61 | `FS.GA.FUTURE.MASTER.ASSET.SUB.TYPE.CODE` | `FsGaFutureMaster_AssetSubTypeCode` | TField |  | To enter Asset sub type for reporting. Multifonds DB Column is CODE_AST. |
| 62 | `FS.GA.FUTURE.MASTER.INSTRUMENT.TEMPLATE` | `FsGaFutureMaster_InstrumentTemplate` | TField |  | Instrument Template Multifonds DB Column is INST_TEMPLATE. |
| 63 | `FS.GA.FUTURE.MASTER.ADJUSTMENT.MARGIN` | `FsGaFutureMaster_AdjustmentMargin` | TField |  | Adjustment Margin Multifonds DB Column is FLG_ADJ_MARGIN. |
| 64 | `FS.GA.FUTURE.MASTER.EFFECT.DATE` | `FsGaFutureMaster_EffectDate` | TField |  | Effective Date Multifonds DB Column is EFFECTIVE_DATE. |
| 65 | `FS.GA.FUTURE.MASTER.RESERVED10` | `FsGaFutureMaster_Reserved10` | TField |  |  |
| 66 | `FS.GA.FUTURE.MASTER.RESERVED9` | `FsGaFutureMaster_Reserved9` | TField |  |  |
| 67 | `FS.GA.FUTURE.MASTER.RESERVED8` | `FsGaFutureMaster_Reserved8` | TField |  |  |
| 68 | `FS.GA.FUTURE.MASTER.RESERVED7` | `FsGaFutureMaster_Reserved7` | TField |  |  |
| 69 | `FS.GA.FUTURE.MASTER.RESERVED6` | `FsGaFutureMaster_Reserved6` | TField |  |  |
| 70 | `FS.GA.FUTURE.MASTER.RESERVED5` | `FsGaFutureMaster_Reserved5` | TField |  |  |
| 71 | `FS.GA.FUTURE.MASTER.RESERVED4` | `FsGaFutureMaster_Reserved4` | TField |  |  |
| 72 | `FS.GA.FUTURE.MASTER.RESERVED3` | `FsGaFutureMaster_Reserved3` | TField |  |  |
| 73 | `FS.GA.FUTURE.MASTER.RESERVED2` | `FsGaFutureMaster_Reserved2` | TField |  |  |
| 74 | `FS.GA.FUTURE.MASTER.RESERVED1` | `FsGaFutureMaster_Reserved1` | TField |  |  |
| 75 | `FS.GA.FUTURE.MASTER.LOCAL.REF` | `FsGaFutureMaster_LocalRef` |  |  |  |
| 76 | `FS.GA.FUTURE.MASTER.OVERRIDE` | `FsGaFutureMaster_Override` |  |  |  |
| 77 | `FS.GA.FUTURE.MASTER.RECORD.STATUS` | `FsGaFutureMaster_RecordStatus` | String |  |  |
| 78 | `FS.GA.FUTURE.MASTER.CURR.NO` | `FsGaFutureMaster_CurrNo` | String |  |  |
| 79 | `FS.GA.FUTURE.MASTER.INPUTTER` | `FsGaFutureMaster_Inputter` |  |  |  |
| 80 | `FS.GA.FUTURE.MASTER.DATE.TIME` | `FsGaFutureMaster_DateTime` |  |  |  |
| 81 | `FS.GA.FUTURE.MASTER.AUTHORISER` | `FsGaFutureMaster_Authoriser` | String |  |  |
| 82 | `FS.GA.FUTURE.MASTER.CO.CODE` | `FsGaFutureMaster_CoCode` | String |  |  |
| 83 | `FS.GA.FUTURE.MASTER.DEPT.CODE` | `FsGaFutureMaster_DeptCode` | String |  |  |
| 84 | `FS.GA.FUTURE.MASTER.AUDITOR.CODE` | `FsGaFutureMaster_AuditorCode` | String |  |  |
| 85 | `FS.GA.FUTURE.MASTER.AUDIT.DATE.TIME` | `FsGaFutureMaster_AuditDateTime` | String |  |  |
