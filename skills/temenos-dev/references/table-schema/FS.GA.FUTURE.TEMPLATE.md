# FS.GA.FUTURE.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUTURE.TEMPLATE` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUTURE.TEMPLATE.PARENT.REF.ID` | `FsGaFutureTemplate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUTURE.TEMPLATE.ORA.ROWID` | `FsGaFutureTemplate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUTURE.TEMPLATE.GTI.CODE` | `FsGaFutureTemplate_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 4 | `FS.GA.FUTURE.TEMPLATE.AMERICAN.OR.EUROPEAN.STYLE` | `FsGaFutureTemplate_AmericanOrEuropeanStyle` | TField |  | American Or European Style For Option Multifonds DB Column is STYLE. |
| 5 | `FS.GA.FUTURE.TEMPLATE.LOCALE.TYPE` | `FsGaFutureTemplate_LocaleType` | TField |  | Local Type of granular information to query in Chart Charesteric screen Multifonds DB Column is COTLOCALE. |
| 6 | `FS.GA.FUTURE.TEMPLATE.REPORTING.CODE` | `FsGaFutureTemplate_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 7 | `FS.GA.FUTURE.TEMPLATE.PRICING.FACTOR.CODE` | `FsGaFutureTemplate_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 8 | `FS.GA.FUTURE.TEMPLATE.MATURITY.DATE` | `FsGaFutureTemplate_MaturityDate` | TField |  | Maturity Date of an instrument, like for Bonds Multifonds DB Column is DATECH. |
| 9 | `FS.GA.FUTURE.TEMPLATE.GUARANTOR.OR.ISSUER` | `FsGaFutureTemplate_GuarantorOrIssuer` | TField |  | Guarantor Or Issuer Multifonds DB Column is NISSUER. |
| 10 | `FS.GA.FUTURE.TEMPLATE.QUOTATION.PLACE` | `FsGaFutureTemplate_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 11 | `FS.GA.FUTURE.TEMPLATE.TQUANT` | `FsGaFutureTemplate_Tquant` | TField |  | Tquant Multifonds DB Column is TQUANT. |
| 12 | `FS.GA.FUTURE.TEMPLATE.PRICE.PROVIDER` | `FsGaFutureTemplate_PriceProvider` | TField |  | Price Provider Multifonds DB Column is TQUOTA. |
| 13 | `FS.GA.FUTURE.TEMPLATE.QUANTITY` | `FsGaFutureTemplate_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 14 | `FS.GA.FUTURE.TEMPLATE.STATE.CODE` | `FsGaFutureTemplate_StateCode` | TField |  | Field is used to store the region type for Catastrophe bonds Multifonds DB Column is STATE_CODE. |
| 15 | `FS.GA.FUTURE.TEMPLATE.RISK.CODE` | `FsGaFutureTemplate_RiskCode` | TField |  | This field is used to store the risk type for the Catastrophe bonds. Multifonds DB Column is CGTI_RISK. |
| 16 | `FS.GA.FUTURE.TEMPLATE.INSTRUMENT.CODE` | `FsGaFutureTemplate_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 17 | `FS.GA.FUTURE.TEMPLATE.INSTRUMENT.CODE.2` | `FsGaFutureTemplate_InstrumentCode2` | TField |  | This field is used for compliance purpose. This field is an alternative to Instrument code 1 (MIG21). It is country of incorporation whenever applicable. Multifonds DB Column is CINSTRUMENT2. |
| 18 | `FS.GA.FUTURE.TEMPLATE.USER.DEFINABLE.FIELDS.GROUP` | `FsGaFutureTemplate_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 19 | `FS.GA.FUTURE.TEMPLATE.RESERVED10` | `FsGaFutureTemplate_Reserved10` | TField |  |  |
| 20 | `FS.GA.FUTURE.TEMPLATE.RESERVED9` | `FsGaFutureTemplate_Reserved9` | TField |  |  |
| 21 | `FS.GA.FUTURE.TEMPLATE.RESERVED8` | `FsGaFutureTemplate_Reserved8` | TField |  |  |
| 22 | `FS.GA.FUTURE.TEMPLATE.RESERVED7` | `FsGaFutureTemplate_Reserved7` | TField |  |  |
| 23 | `FS.GA.FUTURE.TEMPLATE.RESERVED6` | `FsGaFutureTemplate_Reserved6` | TField |  |  |
| 24 | `FS.GA.FUTURE.TEMPLATE.RESERVED5` | `FsGaFutureTemplate_Reserved5` | TField |  |  |
| 25 | `FS.GA.FUTURE.TEMPLATE.RESERVED4` | `FsGaFutureTemplate_Reserved4` | TField |  |  |
| 26 | `FS.GA.FUTURE.TEMPLATE.RESERVED3` | `FsGaFutureTemplate_Reserved3` | TField |  |  |
| 27 | `FS.GA.FUTURE.TEMPLATE.RESERVED2` | `FsGaFutureTemplate_Reserved2` | TField |  |  |
| 28 | `FS.GA.FUTURE.TEMPLATE.RESERVED1` | `FsGaFutureTemplate_Reserved1` | TField |  |  |
| 29 | `FS.GA.FUTURE.TEMPLATE.LOCAL.REF` | `FsGaFutureTemplate_LocalRef` |  |  |  |
| 30 | `FS.GA.FUTURE.TEMPLATE.OVERRIDE` | `FsGaFutureTemplate_Override` |  |  |  |
| 31 | `FS.GA.FUTURE.TEMPLATE.RECORD.STATUS` | `FsGaFutureTemplate_RecordStatus` | String |  |  |
| 32 | `FS.GA.FUTURE.TEMPLATE.CURR.NO` | `FsGaFutureTemplate_CurrNo` | String |  |  |
| 33 | `FS.GA.FUTURE.TEMPLATE.INPUTTER` | `FsGaFutureTemplate_Inputter` |  |  |  |
| 34 | `FS.GA.FUTURE.TEMPLATE.DATE.TIME` | `FsGaFutureTemplate_DateTime` |  |  |  |
| 35 | `FS.GA.FUTURE.TEMPLATE.AUTHORISER` | `FsGaFutureTemplate_Authoriser` | String |  |  |
| 36 | `FS.GA.FUTURE.TEMPLATE.CO.CODE` | `FsGaFutureTemplate_CoCode` | String |  |  |
| 37 | `FS.GA.FUTURE.TEMPLATE.DEPT.CODE` | `FsGaFutureTemplate_DeptCode` | String |  |  |
| 38 | `FS.GA.FUTURE.TEMPLATE.AUDITOR.CODE` | `FsGaFutureTemplate_AuditorCode` | String |  |  |
| 39 | `FS.GA.FUTURE.TEMPLATE.AUDIT.DATE.TIME` | `FsGaFutureTemplate_AuditDateTime` | String |  |  |
