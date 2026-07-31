# ILMATX.ADHOC.TAX.DETS — Table Schema

> Source: `INSERTS/I_F.ILMATX.ADHOC.TAX.DETS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.DR.SEC.NO` | `IlmatxAdhocTaxDets_DrSecNo` | TField |  | This Fields holds Security number of the security that the Diary record relates to |
| 2 | `ILMATX.OPTION.DESC` | `IlmatxAdhocTaxDets_OptionDesc` |  |  |  |
| 3 | `ILMATX.PROCEED.TYPE` | `IlmatxAdhocTaxDets_ProceedType` |  |  |  |
| 4 | `ILMATX.PRIORITY` | `IlmatxAdhocTaxDets_Priority` |  |  |  |
| 5 | `ILMATX.TAX.ACTIVITY` | `IlmatxAdhocTaxDets_TaxActivity` |  |  |  |
| 6 | `ILMATX.TAX.PROPERTY` | `IlmatxAdhocTaxDets_TaxProperty` |  |  |  |
| 7 | `ILMATX.DR.SEC.NOM` | `IlmatxAdhocTaxDets_DrSecNom` |  |  |  |
| 8 | `ILMATX.STOCK.CR.SEC` | `IlmatxAdhocTaxDets_StockCrSec` |  |  |  |
| 9 | `ILMATX.CR.SEC.NOM` | `IlmatxAdhocTaxDets_CrSecNom` |  |  |  |
| 10 | `ILMATX.BUNDLE.VALUE` | `IlmatxAdhocTaxDets_BundleValue` |  |  |  |
| 11 | `ILMATX.STOCK.VALUE.AMT` | `IlmatxAdhocTaxDets_StockValueAmt` |  |  |  |
| 12 | `ILMATX.TOTAL.CASH.VALUE` | `IlmatxAdhocTaxDets_TotalCashValue` |  |  |  |
| 13 | `ILMATX.RESERVED.5` | `IlmatxAdhocTaxDets_Reserved5` | TField |  | Reserved for future use. |
| 14 | `ILMATX.RESERVED.4` | `IlmatxAdhocTaxDets_Reserved4` | TField |  | Reserved for future use. |
| 15 | `ILMATX.RESERVED.3` | `IlmatxAdhocTaxDets_Reserved3` | TField |  | Reserved for future use. |
| 16 | `ILMATX.RESERVED.2` | `IlmatxAdhocTaxDets_Reserved2` | TField |  | Reserved for future use. |
| 17 | `ILMATX.RESERVED.1` | `IlmatxAdhocTaxDets_Reserved1` | TField |  | Reserved for future use. |
| 18 | `ILMATX.LOCAL.REF` | `IlmatxAdhocTaxDets_LocalRef` |  |  |  |
| 19 | `ILMATX.OVERRIDE` | `IlmatxAdhocTaxDets_Override` |  |  |  |
| 20 | `ILMATX.RECORD.STATUS` | `IlmatxAdhocTaxDets_RecordStatus` | String |  |  |
| 21 | `ILMATX.CURR.NO` | `IlmatxAdhocTaxDets_CurrNo` | String |  |  |
| 22 | `ILMATX.INPUTTER` | `IlmatxAdhocTaxDets_Inputter` |  |  |  |
| 23 | `ILMATX.DATE.TIME` | `IlmatxAdhocTaxDets_DateTime` |  |  |  |
| 24 | `ILMATX.AUTHORISER` | `IlmatxAdhocTaxDets_Authoriser` | String |  |  |
| 25 | `ILMATX.CO.CODE` | `IlmatxAdhocTaxDets_CoCode` | String |  |  |
| 26 | `ILMATX.DEPT.CODE` | `IlmatxAdhocTaxDets_DeptCode` | String |  |  |
| 27 | `ILMATX.AUDITOR.CODE` | `IlmatxAdhocTaxDets_AuditorCode` | String |  |  |
| 28 | `ILMATX.AUDIT.DATE.TIME` | `IlmatxAdhocTaxDets_AuditDateTime` | String |  |  |
