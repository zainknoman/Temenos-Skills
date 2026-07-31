# ILSCPR.SECURITY.PRICES — Table Schema

> Source: `INSERTS/I_F.ILSCPR.SECURITY.PRICES` in `ILSCPR_PriceFeed.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEC.PRICES.SECURITY.CURRENCY` | `IlscprSecurityPrices_SecurityCurrency` | TField |  | The currency of the Security. Auto-defaulted from SECURITY.MASTER> SECURITY.CURRENCY. |
| 2 | `SEC.PRICES.PRICE` | `IlscprSecurityPrices_Price` |  |  |  |
| 3 | `SEC.PRICES.DATE` | `IlscprSecurityPrices_Date` |  |  |  |
| 4 | `SEC.PRICES.EFFECTIVE.DATE` | `IlscprSecurityPrices_EffectiveDate` |  |  |  |
| 5 | `SEC.PRICES.PRICE.FEED.SOURCE` | `IlscprSecurityPrices_PriceFeedSource` |  |  |  |
| 6 | `SEC.PRICES.LOCAL.REF` | `IlscprSecurityPrices_LocalRef` |  |  |  |
| 7 | `SEC.PRICES.RESERVED.1` | `IlscprSecurityPrices_Reserved1` | TField |  |  |
| 8 | `SEC.PRICES.RESERVED.2` | `IlscprSecurityPrices_Reserved2` | TField |  |  |
| 9 | `SEC.PRICES.RESERVED.3` | `IlscprSecurityPrices_Reserved3` | TField |  |  |
| 10 | `SEC.PRICES.RESERVED.4` | `IlscprSecurityPrices_Reserved4` | TField |  |  |
| 11 | `SEC.PRICES.RESERVED.5` | `IlscprSecurityPrices_Reserved5` | TField |  |  |
| 12 | `SEC.PRICES.RESERVED.6` | `IlscprSecurityPrices_Reserved6` | TField |  |  |
| 13 | `SEC.PRICES.RESERVED.7` | `IlscprSecurityPrices_Reserved7` | TField |  |  |
| 14 | `SEC.PRICES.RESERVED.8` | `IlscprSecurityPrices_Reserved8` | TField |  |  |
| 15 | `SEC.PRICES.RESERVED.9` | `IlscprSecurityPrices_Reserved9` | TField |  |  |
| 16 | `SEC.PRICES.RESERVED.10` | `IlscprSecurityPrices_Reserved10` | TField |  |  |
| 17 | `SEC.PRICES.OVERRIDE` | `IlscprSecurityPrices_Override` |  |  |  |
| 18 | `SEC.PRICES.RECORD.STATUS` | `IlscprSecurityPrices_RecordStatus` | String |  |  |
| 19 | `SEC.PRICES.CURR.NO` | `IlscprSecurityPrices_CurrNo` | String |  |  |
| 20 | `SEC.PRICES.INPUTTER` | `IlscprSecurityPrices_Inputter` |  |  |  |
| 21 | `SEC.PRICES.DATE.TIME` | `IlscprSecurityPrices_DateTime` |  |  |  |
| 22 | `SEC.PRICES.AUTHORISER` | `IlscprSecurityPrices_Authoriser` | String |  |  |
| 23 | `SEC.PRICES.CO.CODE` | `IlscprSecurityPrices_CoCode` | String |  |  |
| 24 | `SEC.PRICES.DEPT.CODE` | `IlscprSecurityPrices_DeptCode` | String |  |  |
| 25 | `SEC.PRICES.AUDITOR.CODE` | `IlscprSecurityPrices_AuditorCode` | String |  |  |
| 26 | `SEC.PRICES.AUDIT.DATE.TIME` | `IlscprSecurityPrices_AuditDateTime` | String |  |  |
