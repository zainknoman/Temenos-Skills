# ILSCPR.SECURITY.PRICE.CHANGE.HIST — Table Schema

> Source: `INSERTS/I_F.ILSCPR.SECURITY.PRICE.CHANGE.HIST` in `ILSCPR_PriceFeed.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEC.PRICE.HIST.SECURITY.NUMBER` | `IlscprSecurityPriceChangeHist_SecurityNumber` | TField |  | The security no of the associated security master. |
| 2 | `SEC.PRICE.HIST.DATE.CHANGE` | `IlscprSecurityPriceChangeHist_DateChange` | TField |  | The Date associated with the Price history being recorded. |
| 3 | `SEC.PRICE.HIST.TIME.CHANGE` | `IlscprSecurityPriceChangeHist_TimeChange` |  |  |  |
| 4 | `SEC.PRICE.HIST.NEW.PRICE` | `IlscprSecurityPriceChangeHist_NewPrice` |  |  |  |
| 5 | `SEC.PRICE.HIST.OLD.PRICE` | `IlscprSecurityPriceChangeHist_OldPrice` |  |  |  |
| 6 | `SEC.PRICE.HIST.LOCAL.REF` | `IlscprSecurityPriceChangeHist_LocalRef` |  |  |  |
| 7 | `SEC.PRICE.HIST.RESERVED.1` | `IlscprSecurityPriceChangeHist_Reserved1` | TField |  |  |
| 8 | `SEC.PRICE.HIST.RESERVED.2` | `IlscprSecurityPriceChangeHist_Reserved2` | TField |  |  |
| 9 | `SEC.PRICE.HIST.RESERVED.3` | `IlscprSecurityPriceChangeHist_Reserved3` | TField |  |  |
| 10 | `SEC.PRICE.HIST.RESERVED.4` | `IlscprSecurityPriceChangeHist_Reserved4` | TField |  |  |
| 11 | `SEC.PRICE.HIST.RESERVED.5` | `IlscprSecurityPriceChangeHist_Reserved5` | TField |  |  |
| 12 | `SEC.PRICE.HIST.RESERVED.6` | `IlscprSecurityPriceChangeHist_Reserved6` | TField |  |  |
| 13 | `SEC.PRICE.HIST.RESERVED.7` | `IlscprSecurityPriceChangeHist_Reserved7` | TField |  |  |
| 14 | `SEC.PRICE.HIST.RESERVED.8` | `IlscprSecurityPriceChangeHist_Reserved8` | TField |  |  |
| 15 | `SEC.PRICE.HIST.RESERVED.9` | `IlscprSecurityPriceChangeHist_Reserved9` | TField |  |  |
| 16 | `SEC.PRICE.HIST.RESERVED.10` | `IlscprSecurityPriceChangeHist_Reserved10` | TField |  |  |
| 17 | `SEC.PRICE.HIST.OVERRIDE` | `IlscprSecurityPriceChangeHist_Override` |  |  |  |
| 18 | `SEC.PRICE.HIST.RECORD.STATUS` | `IlscprSecurityPriceChangeHist_RecordStatus` | String |  |  |
| 19 | `SEC.PRICE.HIST.CURR.NO` | `IlscprSecurityPriceChangeHist_CurrNo` | String |  |  |
| 20 | `SEC.PRICE.HIST.INPUTTER` | `IlscprSecurityPriceChangeHist_Inputter` |  |  |  |
| 21 | `SEC.PRICE.HIST.DATE.TIME` | `IlscprSecurityPriceChangeHist_DateTime` |  |  |  |
| 22 | `SEC.PRICE.HIST.AUTHORISER` | `IlscprSecurityPriceChangeHist_Authoriser` | String |  |  |
| 23 | `SEC.PRICE.HIST.CO.CODE` | `IlscprSecurityPriceChangeHist_CoCode` | String |  |  |
| 24 | `SEC.PRICE.HIST.DEPT.CODE` | `IlscprSecurityPriceChangeHist_DeptCode` | String |  |  |
| 25 | `SEC.PRICE.HIST.AUDITOR.CODE` | `IlscprSecurityPriceChangeHist_AuditorCode` | String |  |  |
| 26 | `SEC.PRICE.HIST.AUDIT.DATE.TIME` | `IlscprSecurityPriceChangeHist_AuditDateTime` | String |  |  |
