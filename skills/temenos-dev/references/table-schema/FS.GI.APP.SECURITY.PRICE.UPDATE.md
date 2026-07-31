# FS.GI.APP.SECURITY.PRICE.UPDATE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.SECURITY.PRICE.UPDATE` in `FS_TransactionProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.SECURITY.PRICE.UPDATE.PARENT.REF.ID` | `FsGiAppSecurityPriceUpdate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.SECURITY.PRICE.UPDATE.ORA.ROWID` | `FsGiAppSecurityPriceUpdate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.SECURITY.PRICE.UPDATE.SECURITY.ID` | `FsGiAppSecurityPriceUpdate_SecurityId` | TField |  | Security internal ID. Multifonds DB Column is NOVAL. |
| 4 | `FS.GI.APP.SECURITY.PRICE.UPDATE.EXCHANGE.GROUP` | `FsGiAppSecurityPriceUpdate_ExchangeGroup` | TField |  | Fund Exchange Group Multifonds DB Column is CGROUPE_COURS. |
| 5 | `FS.GI.APP.SECURITY.PRICE.UPDATE.LEGAL.ENTITY.ID` | `FsGiAppSecurityPriceUpdate_LegalEntityId` | TField |  | Legal Entity internal ID Multifonds DB Column is NTFC. |
| 6 | `FS.GI.APP.SECURITY.PRICE.UPDATE.FUND.ID` | `FsGiAppSecurityPriceUpdate_FundId` | TField |  | Fund internal ID Multifonds DB Column is NPTF. |
| 7 | `FS.GI.APP.SECURITY.PRICE.UPDATE.SHARE.CLASS.CURRENCY` | `FsGiAppSecurityPriceUpdate_ShareClassCurrency` | TField |  | TA Fund Currency (in 3 letter ISO code, Eg: EUR) for Switch-in fund. Multifonds DB Column is CMONCOTA. |
| 8 | `FS.GI.APP.SECURITY.PRICE.UPDATE.REPORTING.CODE` | `FsGiAppSecurityPriceUpdate_ReportingCode` | TField |  | The Reporting Code of the security. Multifonds DB Column is CODE_RAPPORT. |
| 9 | `FS.GI.APP.SECURITY.PRICE.UPDATE.QUOTATION.TYPE.CODE` | `FsGiAppSecurityPriceUpdate_QuotationTypeCode` | TField |  | Quotation type code. Multifonds DB Column is CORC. |
| 10 | `FS.GI.APP.SECURITY.PRICE.UPDATE.QUOTATION.PLACE.CODE` | `FsGiAppSecurityPriceUpdate_QuotationPlaceCode` | TField |  | The stock exchange from which a market price of the security is required. Multifonds DB Column is CPLACE. |
| 11 | `FS.GI.APP.SECURITY.PRICE.UPDATE.ACCOUNTING.DATE.MF` | `FsGiAppSecurityPriceUpdate_AccountingDateMf` | TField |  | Application date. Multifonds DB Column is DCTA. |
| 12 | `FS.GI.APP.SECURITY.PRICE.UPDATE.REFERENCE.NAV.VALUE` | `FsGiAppSecurityPriceUpdate_ReferenceNavValue` | TField |  | Reference net asset value. Multifonds DB Column is COURSVAL. |
| 13 | `FS.GI.APP.SECURITY.PRICE.UPDATE.HWM` | `FsGiAppSecurityPriceUpdate_Hwm` | TField |  | Highwatermark used for redemption or crysallization. Multifonds DB Column is COURSVAL_HWM. |
| 14 | `FS.GI.APP.SECURITY.PRICE.UPDATE.BMK` | `FsGiAppSecurityPriceUpdate_Bmk` | TField |  | Benchmark used for redemption or crystallization. Multifonds DB Column is COURSVAL_BMK. |
| 15 | `FS.GI.APP.SECURITY.PRICE.UPDATE.HURDLE.ADJUSTED.HWM` | `FsGiAppSecurityPriceUpdate_HurdleAdjustedHwm` | TField |  | Hurdle adjusted highwatermark used at redemption or crystallization. Multifonds DB Column is HURDLE_ADJ_HWM. |
| 16 | `FS.GI.APP.SECURITY.PRICE.UPDATE.HURDLE.RATE` | `FsGiAppSecurityPriceUpdate_HurdleRate` | TField |  | Hurdle rate used at redemption or crystallization. Multifonds DB Column is HURDLE_RATE. |
| 17 | `FS.GI.APP.SECURITY.PRICE.UPDATE.BID.MARKET.VALUE` | `FsGiAppSecurityPriceUpdate_BidMarketValue` | TField |  | Bid market value. Multifonds DB Column is COURSVAL_BID. |
| 18 | `FS.GI.APP.SECURITY.PRICE.UPDATE.OFFER.MARKET.VALUE` | `FsGiAppSecurityPriceUpdate_OfferMarketValue` | TField |  | Offer market value. Multifonds DB Column is COURSVAL_OFFER. |
| 19 | `FS.GI.APP.SECURITY.PRICE.UPDATE.TRUE.MARKET.VALUE` | `FsGiAppSecurityPriceUpdate_TrueMarketValue` | TField |  | Total market value. Multifonds DB Column is COURSVAL_TRUE. |
| 20 | `FS.GI.APP.SECURITY.PRICE.UPDATE.MIDDLE.MARKET.VALUE` | `FsGiAppSecurityPriceUpdate_MiddleMarketValue` | TField |  | Middle market value. Multifonds DB Column is COURSVAL_MIDDLE. |
| 21 | `FS.GI.APP.SECURITY.PRICE.UPDATE.SENSIBILITY` | `FsGiAppSecurityPriceUpdate_Sensibility` | TField |  | Sensibility. Multifonds DB Column is SENSIBILITY. |
| 22 | `FS.GI.APP.SECURITY.PRICE.UPDATE.DELTA` | `FsGiAppSecurityPriceUpdate_Delta` | TField |  | Delta. Multifonds DB Column is DELTA. |
| 23 | `FS.GI.APP.SECURITY.PRICE.UPDATE.GROSS.SHARE.PRICE` | `FsGiAppSecurityPriceUpdate_GrossSharePrice` | TField |  | Gross share price. Multifonds DB Column is G_SHARE_PRICE. |
| 24 | `FS.GI.APP.SECURITY.PRICE.UPDATE.FINAL.BENEFICIARY.TYPE` | `FsGiAppSecurityPriceUpdate_FinalBeneficiaryType` | TField |  | The final beneficiary type. Multifonds DB Column is CTYPE. |
| 25 | `FS.GI.APP.SECURITY.PRICE.UPDATE.PROVENANCE` | `FsGiAppSecurityPriceUpdate_Provenance` | TField |  | Provenance. Multifonds DB Column is PROVENANCE. |
| 26 | `FS.GI.APP.SECURITY.PRICE.UPDATE.REFERENCE.NAV.VALUE.TYPE` | `FsGiAppSecurityPriceUpdate_ReferenceNavValueType` | TField |  | Reference net asset value type. Multifonds DB Column is TYPE_COURSVAL. |
| 27 | `FS.GI.APP.SECURITY.PRICE.UPDATE.BID.MARKET.VALUE.TYPE` | `FsGiAppSecurityPriceUpdate_BidMarketValueType` | TField |  | Bid market value type. Multifonds DB Column is TYPE_COURSVAL_BID. |
| 28 | `FS.GI.APP.SECURITY.PRICE.UPDATE.OFFER.MARKET.VALUE.TYPE` | `FsGiAppSecurityPriceUpdate_OfferMarketValueType` | TField |  | Offer market value type. Multifonds DB Column is TYPE_COURSVAL_OFFER. |
| 29 | `FS.GI.APP.SECURITY.PRICE.UPDATE.PRICE.COD` | `FsGiAppSecurityPriceUpdate_PriceCod` | TField |  | Price code. Multifonds DB Column is COD_DPRICE. |
| 30 | `FS.GI.APP.SECURITY.PRICE.UPDATE.PRICING.DATE` | `FsGiAppSecurityPriceUpdate_PricingDate` | TField |  | Pricing date. Multifonds DB Column is DCTA_PRICING. |
| 31 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RNI.SHARE` | `FsGiAppSecurityPriceUpdate_RniShare` | TField |  | It specifies profit gain considered for German taxation when the Equalization code at the TA fund level is 000 - RNI part. Multifonds DB Column is RNI_PART. |
| 32 | `FS.GI.APP.SECURITY.PRICE.UPDATE.LEVERAGE` | `FsGiAppSecurityPriceUpdate_Leverage` | TField |  | Leverage. Multifonds DB Column is LEVERAGE. |
| 33 | `FS.GI.APP.SECURITY.PRICE.UPDATE.AKTIENGEWINN.D` | `FsGiAppSecurityPriceUpdate_AktiengewinnD` | TField |  | Aktiengewinn D. Multifonds DB Column is ACTIENGEWINN_PART. |
| 34 | `FS.GI.APP.SECURITY.PRICE.UPDATE.PERFORMANCE.FEE.PER.UNIT` | `FsGiAppSecurityPriceUpdate_PerformanceFeePerUnit` | TField |  | Performance fees per unit. Multifonds DB Column is PF_PART. |
| 35 | `FS.GI.APP.SECURITY.PRICE.UPDATE.REPORTING.CODE.FILTER` | `FsGiAppSecurityPriceUpdate_ReportingCodeFilter` | TField |  | Security Reporting Code filter. Multifonds DB Column is CODE. |
| 36 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED10` | `FsGiAppSecurityPriceUpdate_Reserved10` | TField |  |  |
| 37 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED9` | `FsGiAppSecurityPriceUpdate_Reserved9` | TField |  |  |
| 38 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED8` | `FsGiAppSecurityPriceUpdate_Reserved8` | TField |  |  |
| 39 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED7` | `FsGiAppSecurityPriceUpdate_Reserved7` | TField |  |  |
| 40 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED6` | `FsGiAppSecurityPriceUpdate_Reserved6` | TField |  |  |
| 41 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED5` | `FsGiAppSecurityPriceUpdate_Reserved5` | TField |  |  |
| 42 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED4` | `FsGiAppSecurityPriceUpdate_Reserved4` | TField |  |  |
| 43 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED3` | `FsGiAppSecurityPriceUpdate_Reserved3` | TField |  |  |
| 44 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED2` | `FsGiAppSecurityPriceUpdate_Reserved2` | TField |  |  |
| 45 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RESERVED1` | `FsGiAppSecurityPriceUpdate_Reserved1` | TField |  |  |
| 46 | `FS.GI.APP.SECURITY.PRICE.UPDATE.LOCAL.REF` | `FsGiAppSecurityPriceUpdate_LocalRef` |  |  |  |
| 47 | `FS.GI.APP.SECURITY.PRICE.UPDATE.OVERRIDE` | `FsGiAppSecurityPriceUpdate_Override` |  |  |  |
| 48 | `FS.GI.APP.SECURITY.PRICE.UPDATE.RECORD.STATUS` | `FsGiAppSecurityPriceUpdate_RecordStatus` | String |  |  |
| 49 | `FS.GI.APP.SECURITY.PRICE.UPDATE.CURR.NO` | `FsGiAppSecurityPriceUpdate_CurrNo` | String |  |  |
| 50 | `FS.GI.APP.SECURITY.PRICE.UPDATE.INPUTTER` | `FsGiAppSecurityPriceUpdate_Inputter` |  |  |  |
| 51 | `FS.GI.APP.SECURITY.PRICE.UPDATE.DATE.TIME` | `FsGiAppSecurityPriceUpdate_DateTime` |  |  |  |
| 52 | `FS.GI.APP.SECURITY.PRICE.UPDATE.AUTHORISER` | `FsGiAppSecurityPriceUpdate_Authoriser` | String |  |  |
| 53 | `FS.GI.APP.SECURITY.PRICE.UPDATE.CO.CODE` | `FsGiAppSecurityPriceUpdate_CoCode` | String |  |  |
| 54 | `FS.GI.APP.SECURITY.PRICE.UPDATE.DEPT.CODE` | `FsGiAppSecurityPriceUpdate_DeptCode` | String |  |  |
| 55 | `FS.GI.APP.SECURITY.PRICE.UPDATE.AUDITOR.CODE` | `FsGiAppSecurityPriceUpdate_AuditorCode` | String |  |  |
| 56 | `FS.GI.APP.SECURITY.PRICE.UPDATE.AUDIT.DATE.TIME` | `FsGiAppSecurityPriceUpdate_AuditDateTime` | String |  |  |
