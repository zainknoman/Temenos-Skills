# CAPL.PAYMENT.PRIORITY — Table Schema

> Source: `INSERTS/I_F.CAPL.PAYMENT.PRIORITY` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PP.DESCRIPTION` | `CaplPaymentPriority_Description` |  |  |  |
| 2 | `CAPL.PP.PRODUCT.TYPE` | `CaplPaymentPriority_ProductType` |  |  |  |
| 3 | `CAPL.PP.PROD.TYPE.PRIORITY` | `CaplPaymentPriority_ProdTypePriority` |  |  |  |
| 4 | `CAPL.PP.PROD.CATEGORY` | `CaplPaymentPriority_ProdCategory` |  |  |  |
| 5 | `CAPL.PP.PROD.APP` | `CaplPaymentPriority_ProdApp` |  |  |  |
| 6 | `CAPL.PP.PROD.AD` | `CaplPaymentPriority_ProdAd` |  |  |  |
| 7 | `CAPL.PP.CAT.APP.PRIORITY` | `CaplPaymentPriority_CatAppPriority` |  |  |  |
| 8 | `CAPL.PP.SUB.PRIORITY.1` | `CaplPaymentPriority_SubPriority1` |  |  |  |
| 9 | `CAPL.PP.SUB.PRIORITY.2` | `CaplPaymentPriority_SubPriority2` |  |  |  |
| 10 | `CAPL.PP.SUB.PRIORITY.3` | `CaplPaymentPriority_SubPriority3` |  |  |  |
| 11 | `CAPL.PP.RESERVED.15` | `CaplPaymentPriority_Reserved15` |  |  |  |
| 12 | `CAPL.PP.RESERVED.14` | `CaplPaymentPriority_Reserved14` |  |  |  |
| 13 | `CAPL.PP.RESERVED.13` | `CaplPaymentPriority_Reserved13` |  |  |  |
| 14 | `CAPL.PP.RESERVED.12` | `CaplPaymentPriority_Reserved12` |  |  |  |
| 15 | `CAPL.PP.HOLDS.SCREEN` | `CaplPaymentPriority_HoldsScreen` |  |  |  |
| 16 | `CAPL.PP.TRANSFER.SCREEN` | `CaplPaymentPriority_TransferScreen` |  |  |  |
| 17 | `CAPL.PP.CLOSURE.SCREEN` | `CaplPaymentPriority_ClosureScreen` |  |  |  |
| 18 | `CAPL.PP.RESERVED.11` | `CaplPaymentPriority_Reserved11` |  |  |  |
| 19 | `CAPL.PP.RESERVED.10` | `CaplPaymentPriority_Reserved10` |  |  |  |
| 20 | `CAPL.PP.REPORT.CATEGORY` | `CaplPaymentPriority_ReportCategory` |  |  |  |
| 21 | `CAPL.PP.REPORT.APP` | `CaplPaymentPriority_ReportApp` |  |  |  |
| 22 | `CAPL.PP.REPORT.AD` | `CaplPaymentPriority_ReportAd` |  |  |  |
| 23 | `CAPL.PP.EXCLUDE.CATEGORY` | `CaplPaymentPriority_ExcludeCategory` |  |  |  |
| 24 | `CAPL.PP.EXCLUDE.APP` | `CaplPaymentPriority_ExcludeApp` |  |  |  |
| 25 | `CAPL.PP.EXCLUDE.AD` | `CaplPaymentPriority_ExcludeAd` |  |  |  |
| 26 | `CAPL.PP.RESERVED.9` | `CaplPaymentPriority_Reserved9` |  |  |  |
| 27 | `CAPL.PP.RESERVED.8` | `CaplPaymentPriority_Reserved8` |  |  |  |
| 28 | `CAPL.PP.TERM.MIN.AMT` | `CaplPaymentPriority_TermMinAmt` |  |  |  |
| 29 | `CAPL.PP.RESERVED.7` | `CaplPaymentPriority_Reserved7` |  |  |  |
| 30 | `CAPL.PP.RESERVED.6` | `CaplPaymentPriority_Reserved6` |  |  |  |
| 31 | `CAPL.PP.RESERVED.5` | `CaplPaymentPriority_Reserved5` |  |  |  |
| 32 | `CAPL.PP.RESERVED.4` | `CaplPaymentPriority_Reserved4` |  |  |  |
| 33 | `CAPL.PP.RESERVED.3` | `CaplPaymentPriority_Reserved3` |  |  |  |
| 34 | `CAPL.PP.RESERVED.2` | `CaplPaymentPriority_Reserved2` |  |  |  |
| 35 | `CAPL.PP.RESERVED.1` | `CaplPaymentPriority_Reserved1` |  |  |  |
| 36 | `CAPL.PP.LOCAL.REF` | `CaplPaymentPriority_LocalRef` |  |  |  |
| 37 | `CAPL.PP.OVERRIDE` | `CaplPaymentPriority_Override` |  |  |  |
| 38 | `CAPL.PP.RECORD.STATUS` | `CaplPaymentPriority_RecordStatus` |  |  |  |
| 39 | `CAPL.PP.CURR.NO` | `CaplPaymentPriority_CurrNo` |  |  |  |
| 40 | `CAPL.PP.INPUTTER` | `CaplPaymentPriority_Inputter` |  |  |  |
| 41 | `CAPL.PP.DATE.TIME` | `CaplPaymentPriority_DateTime` |  |  |  |
| 42 | `CAPL.PP.AUTHORISER` | `CaplPaymentPriority_Authoriser` |  |  |  |
| 43 | `CAPL.PP.CO.CODE` | `CaplPaymentPriority_CoCode` |  |  |  |
| 44 | `CAPL.PP.DEPT.CODE` | `CaplPaymentPriority_DeptCode` |  |  |  |
| 45 | `CAPL.PP.AUDITOR.CODE` | `CaplPaymentPriority_AuditorCode` |  |  |  |
| 46 | `CAPL.PP.AUDIT.DATE.TIME` | `CaplPaymentPriority_AuditDateTime` |  |  |  |
