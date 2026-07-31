# FS.GA.HIGH.LOW.PRICE — Table Schema

> Source: `INSERTS/I_F.FS.GA.HIGH.LOW.PRICE` in `FS_Securities.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.HIGH.LOW.PRICE.PRICING.DT` | `FsGaHighLowPrice_PricingDt` | TField |  | This field displays the date of high and low prices available in the market Multifonds DB Column is PRICING_DATE. |
| 2 | `FS.GA.HIGH.LOW.PRICE.SECURITY.SERVICE.CODE` | `FsGaHighLowPrice_SecurityServiceCode` | TField |  | This field displays type of security for which the High and low prices/Exchange rates are defined Multifonds DB Column is SERVICE_CODE. |
| 3 | `FS.GA.HIGH.LOW.PRICE.PROVIDER.ID` | `FsGaHighLowPrice_ProviderId` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 4 | `FS.GA.HIGH.LOW.PRICE.SEC.ID.OR.CURRENCY` | `FsGaHighLowPrice_SecIdOrCurrency` | TField |  | This field displays external security id if ID Code field is defined for service codes BO, OP and FU and currency 1 for service code FS Multifonds DB Column is SEC_ID_CURR1. |
| 5 | `FS.GA.HIGH.LOW.PRICE.CURRENCY2` | `FsGaHighLowPrice_Currency2` | TField |  | This field displays currency 2 for service code FS Multifonds DB Column is CURR2. |
| 6 | `FS.GA.HIGH.LOW.PRICE.HIGH.PRICE` | `FsGaHighLowPrice_HighPrice` | TField |  | This field displays the high price or exchange rate for the price date defined Multifonds DB Column is HIGH_PRICE. |
| 7 | `FS.GA.HIGH.LOW.PRICE.LOW.PRICE` | `FsGaHighLowPrice_LowPrice` | TField |  | This field displays the low price or exchange rate for the price date defined Multifonds DB Column is LOW_PRICE. |
| 8 | `FS.GA.HIGH.LOW.PRICE.INTERNAL.ID` | `FsGaHighLowPrice_InternalId` | TField |  | Corresponds to the internal Id of the security for which high/low prices are defined. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GA.HIGH.LOW.PRICE.RESERVED10` | `FsGaHighLowPrice_Reserved10` | TField |  |  |
| 10 | `FS.GA.HIGH.LOW.PRICE.RESERVED9` | `FsGaHighLowPrice_Reserved9` | TField |  |  |
| 11 | `FS.GA.HIGH.LOW.PRICE.RESERVED8` | `FsGaHighLowPrice_Reserved8` | TField |  |  |
| 12 | `FS.GA.HIGH.LOW.PRICE.RESERVED7` | `FsGaHighLowPrice_Reserved7` | TField |  |  |
| 13 | `FS.GA.HIGH.LOW.PRICE.RESERVED6` | `FsGaHighLowPrice_Reserved6` | TField |  |  |
| 14 | `FS.GA.HIGH.LOW.PRICE.RESERVED5` | `FsGaHighLowPrice_Reserved5` | TField |  |  |
| 15 | `FS.GA.HIGH.LOW.PRICE.RESERVED4` | `FsGaHighLowPrice_Reserved4` | TField |  |  |
| 16 | `FS.GA.HIGH.LOW.PRICE.RESERVED3` | `FsGaHighLowPrice_Reserved3` | TField |  |  |
| 17 | `FS.GA.HIGH.LOW.PRICE.RESERVED2` | `FsGaHighLowPrice_Reserved2` | TField |  |  |
| 18 | `FS.GA.HIGH.LOW.PRICE.RESERVED1` | `FsGaHighLowPrice_Reserved1` | TField |  |  |
| 19 | `FS.GA.HIGH.LOW.PRICE.RECORD.STATUS` | `FsGaHighLowPrice_RecordStatus` | String |  |  |
| 20 | `FS.GA.HIGH.LOW.PRICE.CURR.NO` | `FsGaHighLowPrice_CurrNo` | String |  |  |
| 21 | `FS.GA.HIGH.LOW.PRICE.INPUTTER` | `FsGaHighLowPrice_Inputter` |  |  |  |
| 22 | `FS.GA.HIGH.LOW.PRICE.DATE.TIME` | `FsGaHighLowPrice_DateTime` |  |  |  |
| 23 | `FS.GA.HIGH.LOW.PRICE.AUTHORISER` | `FsGaHighLowPrice_Authoriser` | String |  |  |
| 24 | `FS.GA.HIGH.LOW.PRICE.CO.CODE` | `FsGaHighLowPrice_CoCode` | String |  |  |
| 25 | `FS.GA.HIGH.LOW.PRICE.DEPT.CODE` | `FsGaHighLowPrice_DeptCode` | String |  |  |
| 26 | `FS.GA.HIGH.LOW.PRICE.AUDITOR.CODE` | `FsGaHighLowPrice_AuditorCode` | String |  |  |
| 27 | `FS.GA.HIGH.LOW.PRICE.AUDIT.DATE.TIME` | `FsGaHighLowPrice_AuditDateTime` | String |  |  |
