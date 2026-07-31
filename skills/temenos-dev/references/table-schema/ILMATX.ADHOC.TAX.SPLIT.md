# ILMATX.ADHOC.TAX.SPLIT — Table Schema

> Source: `INSERTS/I_F.ILMATX.ADHOC.TAX.SPLIT` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.DR.SEC.NO` | `IlmatxAdhocTaxSplit_DrSecNo` | TField |  | This Fields holds Security number of the security that the Diary record relates to |
| 2 | `ILMATX.OPTION.DESC` | `IlmatxAdhocTaxSplit_OptionDesc` |  |  |  |
| 3 | `ILMATX.PROCEED.TYPE` | `IlmatxAdhocTaxSplit_ProceedType` |  |  |  |
| 4 | `ILMATX.PRIORITY` | `IlmatxAdhocTaxSplit_Priority` |  |  |  |
| 5 | `ILMATX.TAX.ACTIVITY` | `IlmatxAdhocTaxSplit_TaxActivity` |  |  |  |
| 6 | `ILMATX.TAX.PROPERTY` | `IlmatxAdhocTaxSplit_TaxProperty` |  |  |  |
| 7 | `ILMATX.DR.SEC.PERC` | `IlmatxAdhocTaxSplit_DrSecPerc` |  |  |  |
| 8 | `ILMATX.STOCK.CR.SEC` | `IlmatxAdhocTaxSplit_StockCrSec` |  |  |  |
| 9 | `ILMATX.STOCK.VALUE.PERC` | `IlmatxAdhocTaxSplit_StockValuePerc` |  |  |  |
| 10 | `ILMATX.STOCK.TAX.PRICE` | `IlmatxAdhocTaxSplit_StockTaxPrice` |  |  |  |
| 11 | `ILMATX.BUNDLE.VALUE` | `IlmatxAdhocTaxSplit_BundleValue` |  |  |  |
| 12 | `ILMATX.RESERVED.5` | `IlmatxAdhocTaxSplit_Reserved5` | TField |  | Reserved for future use. |
| 13 | `ILMATX.RESERVED.4` | `IlmatxAdhocTaxSplit_Reserved4` | TField |  | Reserved for future use. |
| 14 | `ILMATX.RESERVED.3` | `IlmatxAdhocTaxSplit_Reserved3` | TField |  | Reserved for future use. |
| 15 | `ILMATX.RESERVED.2` | `IlmatxAdhocTaxSplit_Reserved2` | TField |  | Reserved for future use. |
| 16 | `ILMATX.RESERVED.1` | `IlmatxAdhocTaxSplit_Reserved1` | TField |  | Reserved for future use. |
| 17 | `ILMATX.LOCAL.REF` | `IlmatxAdhocTaxSplit_LocalRef` |  |  |  |
| 18 | `ILMATX.OVERRIDE` | `IlmatxAdhocTaxSplit_Override` |  |  |  |
| 19 | `ILMATX.RECORD.STATUS` | `IlmatxAdhocTaxSplit_RecordStatus` | String |  |  |
| 20 | `ILMATX.CURR.NO` | `IlmatxAdhocTaxSplit_CurrNo` | String |  |  |
| 21 | `ILMATX.INPUTTER` | `IlmatxAdhocTaxSplit_Inputter` |  |  |  |
| 22 | `ILMATX.DATE.TIME` | `IlmatxAdhocTaxSplit_DateTime` |  |  |  |
| 23 | `ILMATX.AUTHORISER` | `IlmatxAdhocTaxSplit_Authoriser` | String |  |  |
| 24 | `ILMATX.CO.CODE` | `IlmatxAdhocTaxSplit_CoCode` | String |  |  |
| 25 | `ILMATX.DEPT.CODE` | `IlmatxAdhocTaxSplit_DeptCode` | String |  |  |
| 26 | `ILMATX.AUDITOR.CODE` | `IlmatxAdhocTaxSplit_AuditorCode` | String |  |  |
| 27 | `ILMATX.AUDIT.DATE.TIME` | `IlmatxAdhocTaxSplit_AuditDateTime` | String |  |  |
