# FS.GA.OPTION.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.OPTION.TEMPLATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.OPTION.TEMPLATE.PARENT.REF.ID` | `FsGaOptionTemplate_ParentRefId` |  |  |  |
| 2 | `FS.GA.OPTION.TEMPLATE.ORA.ROWID` | `FsGaOptionTemplate_OraRowid` |  |  |  |
| 3 | `FS.GA.OPTION.TEMPLATE.GTI.CODE` | `FsGaOptionTemplate_GtiCode` |  |  |  |
| 4 | `FS.GA.OPTION.TEMPLATE.OPTION.TYPE` | `FsGaOptionTemplate_OptionType` |  |  |  |
| 5 | `FS.GA.OPTION.TEMPLATE.AMERICAN.OR.EUROPEAN.STYLE` | `FsGaOptionTemplate_AmericanOrEuropeanStyle` |  |  |  |
| 6 | `FS.GA.OPTION.TEMPLATE.UNDERLYING.RECEIVABLE` | `FsGaOptionTemplate_UnderlyingReceivable` |  |  |  |
| 7 | `FS.GA.OPTION.TEMPLATE.OPTION.STRIKE.PRICE` | `FsGaOptionTemplate_OptionStrikePrice` |  |  |  |
| 8 | `FS.GA.OPTION.TEMPLATE.MATURITY.DATE` | `FsGaOptionTemplate_MaturityDate` |  |  |  |
| 9 | `FS.GA.OPTION.TEMPLATE.LOCALE.TYPE` | `FsGaOptionTemplate_LocaleType` |  |  |  |
| 10 | `FS.GA.OPTION.TEMPLATE.PRICE.PROVIDER` | `FsGaOptionTemplate_PriceProvider` |  |  |  |
| 11 | `FS.GA.OPTION.TEMPLATE.QUOTATION.PLACE` | `FsGaOptionTemplate_QuotationPlace` |  |  |  |
| 12 | `FS.GA.OPTION.TEMPLATE.PRICING.FACTOR.CODE` | `FsGaOptionTemplate_PricingFactorCode` |  |  |  |
| 13 | `FS.GA.OPTION.TEMPLATE.CONTRACT.SIZE` | `FsGaOptionTemplate_ContractSize` |  |  |  |
| 14 | `FS.GA.OPTION.TEMPLATE.GUARANTOR.OR.ISSUER` | `FsGaOptionTemplate_GuarantorOrIssuer` |  |  |  |
| 15 | `FS.GA.OPTION.TEMPLATE.QUANTITY` | `FsGaOptionTemplate_Quantity` |  |  |  |
| 16 | `FS.GA.OPTION.TEMPLATE.TQUANT` | `FsGaOptionTemplate_Tquant` |  |  |  |
| 17 | `FS.GA.OPTION.TEMPLATE.REPORTING.CODE` | `FsGaOptionTemplate_ReportingCode` |  |  |  |
| 18 | `FS.GA.OPTION.TEMPLATE.STATE.CODE` | `FsGaOptionTemplate_StateCode` |  |  |  |
| 19 | `FS.GA.OPTION.TEMPLATE.RISK.CODE` | `FsGaOptionTemplate_RiskCode` |  |  |  |
| 20 | `FS.GA.OPTION.TEMPLATE.INSTRUMENT.CODE` | `FsGaOptionTemplate_InstrumentCode` |  |  |  |
| 21 | `FS.GA.OPTION.TEMPLATE.INSTRUMENT.CODE.2` | `FsGaOptionTemplate_InstrumentCode2` |  |  |  |
| 22 | `FS.GA.OPTION.TEMPLATE.USER.DEFINABLE.FIELDS.GROUP` | `FsGaOptionTemplate_UserDefinableFieldsGroup` |  |  |  |
| 23 | `FS.GA.OPTION.TEMPLATE.RESERVED10` | `FsGaOptionTemplate_Reserved10` |  |  |  |
| 24 | `FS.GA.OPTION.TEMPLATE.RESERVED9` | `FsGaOptionTemplate_Reserved9` |  |  |  |
| 25 | `FS.GA.OPTION.TEMPLATE.RESERVED8` | `FsGaOptionTemplate_Reserved8` |  |  |  |
| 26 | `FS.GA.OPTION.TEMPLATE.RESERVED7` | `FsGaOptionTemplate_Reserved7` |  |  |  |
| 27 | `FS.GA.OPTION.TEMPLATE.RESERVED6` | `FsGaOptionTemplate_Reserved6` |  |  |  |
| 28 | `FS.GA.OPTION.TEMPLATE.RESERVED5` | `FsGaOptionTemplate_Reserved5` |  |  |  |
| 29 | `FS.GA.OPTION.TEMPLATE.RESERVED4` | `FsGaOptionTemplate_Reserved4` |  |  |  |
| 30 | `FS.GA.OPTION.TEMPLATE.RESERVED3` | `FsGaOptionTemplate_Reserved3` |  |  |  |
| 31 | `FS.GA.OPTION.TEMPLATE.RESERVED2` | `FsGaOptionTemplate_Reserved2` |  |  |  |
| 32 | `FS.GA.OPTION.TEMPLATE.RESERVED1` | `FsGaOptionTemplate_Reserved1` |  |  |  |
| 33 | `FS.GA.OPTION.TEMPLATE.LOCAL.REF` | `FsGaOptionTemplate_LocalRef` |  |  |  |
| 34 | `FS.GA.OPTION.TEMPLATE.OVERRIDE` | `FsGaOptionTemplate_Override` |  |  |  |
| 35 | `FS.GA.OPTION.TEMPLATE.RECORD.STATUS` | `FsGaOptionTemplate_RecordStatus` |  |  |  |
| 36 | `FS.GA.OPTION.TEMPLATE.CURR.NO` | `FsGaOptionTemplate_CurrNo` |  |  |  |
| 37 | `FS.GA.OPTION.TEMPLATE.INPUTTER` | `FsGaOptionTemplate_Inputter` |  |  |  |
| 38 | `FS.GA.OPTION.TEMPLATE.DATE.TIME` | `FsGaOptionTemplate_DateTime` |  |  |  |
| 39 | `FS.GA.OPTION.TEMPLATE.AUTHORISER` | `FsGaOptionTemplate_Authoriser` |  |  |  |
| 40 | `FS.GA.OPTION.TEMPLATE.CO.CODE` | `FsGaOptionTemplate_CoCode` |  |  |  |
| 41 | `FS.GA.OPTION.TEMPLATE.DEPT.CODE` | `FsGaOptionTemplate_DeptCode` |  |  |  |
| 42 | `FS.GA.OPTION.TEMPLATE.AUDITOR.CODE` | `FsGaOptionTemplate_AuditorCode` |  |  |  |
| 43 | `FS.GA.OPTION.TEMPLATE.AUDIT.DATE.TIME` | `FsGaOptionTemplate_AuditDateTime` |  |  |  |
