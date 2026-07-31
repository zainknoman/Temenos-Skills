# INLEND.IMPORT.EXPORT.ATTRIBUTES — Table Schema

> Source: `INSERTS/I_F.INLEND.IMPORT.EXPORT.ATTRIBUTES` in `INBASE_CustomerValidations.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.IMPEXP.AD.CODE1` | `InlendImportExportAttributes_AdCode1` | TField |  | Authorised Dealer Code given by RBI |
| 2 | `INLEND.IMPEXP.AD.CODE2` | `InlendImportExportAttributes_AdCode2` | TField |  | Authorised Dealer Code given by RBI |
| 3 | `INLEND.IMPEXP.ADV.PAYMENT.PURPOSE.CODE` | `InlendImportExportAttributes_AdvPaymentPurposeCode` |  |  |  |
| 4 | `INLEND.IMPEXP.IMP.EXP.PURPOSE.CODE` | `InlendImportExportAttributes_ImpExpPurposeCode` |  |  |  |
| 5 | `INLEND.IMPEXP.ADV.PMT.CEILING.AMT.CURR` | `InlendImportExportAttributes_AdvPmtCeilingAmtCurr` |  |  |  |
| 6 | `INLEND.IMPEXP.ADV.PMT.CEILING.AMOUNT` | `InlendImportExportAttributes_AdvPmtCeilingAmount` |  |  |  |
| 7 | `INLEND.IMPEXP.BRANCH.IFSC.CODE` | `InlendImportExportAttributes_BranchIfscCode` | TField |  | IFSC Code of Branch |
| 8 | `INLEND.IMPEXP.ADV.PMT.CATEG.CODE` | `InlendImportExportAttributes_AdvPmtCategCode` |  |  |  |
| 9 | `INLEND.IMPEXP.PAYMENT.TERM` | `InlendImportExportAttributes_PaymentTerm` |  |  |  |
| 10 | `INLEND.IMPEXP.LC.TYPE.CATEG.CODE` | `InlendImportExportAttributes_LcTypeCategCode` |  |  |  |
| 11 | `INLEND.IMPEXP.DAYS.STALE.ADV.PMT` | `InlendImportExportAttributes_DaysStaleAdvPmt` | TField |  | No of days within which BOE should be available in case of remittance made as Advance Payment for non-capital goods |
| 12 | `INLEND.IMPEXP.DAYS.STALE.ADV.PMT.CAP.GOODS` | `InlendImportExportAttributes_DaysStaleAdvPmtCapGoods` | TField |  | No of days within which BOE should be available in case of remittance made as Advance Payment for capital goods |
| 13 | `INLEND.IMPEXP.GRACE.PERIOD.ORM` | `InlendImportExportAttributes_GracePeriodOrm` | TField |  | No of days up to which BOE settlement can be made, if ORM has become stale. |
| 14 | `INLEND.IMPEXP.DAYS.STALE.REMITTANCE` | `InlendImportExportAttributes_DaysStaleRemittance` | TField |  | No of days within which remittance should be made for BOE received. |
| 15 | `INLEND.IMPEXP.DEFAULT.BOE.EXTENSION.PERIOD` | `InlendImportExportAttributes_DefaultBoeExtensionPeriod` | TField |  | Default period for which a BOE can be extended |
| 16 | `INLEND.IMPEXP.MAX.BOE.EXTENSION.COUNT` | `InlendImportExportAttributes_MaxBoeExtensionCount` | TField |  | Default number of times a BOE can be extended |
| 17 | `INLEND.IMPEXP.BOE.ADJ.LIMIT.PERCENT` | `InlendImportExportAttributes_BoeAdjLimitPercent` | TField |  | Maximum percentage of invoice amount that can be adjusted for BOE to be closed. |
| 18 | `INLEND.IMPEXP.REMITTANCE.AMOUNT.GROSS.NET` | `InlendImportExportAttributes_RemittanceAmountGrossNet` | TField |  | If GROSS is chosen, remittance amount will include charges deducted, if any. If NETT is chosen, remittance amount will not include charges. |
| 19 | `INLEND.IMPEXP.EXPORTER.CATEGORY` | `InlendImportExportAttributes_ExporterCategory` |  |  |  |
| 20 | `INLEND.IMPEXP.PAYMENT.REALIZATION.EXPIRY` | `InlendImportExportAttributes_PaymentRealizationExpiry` |  |  |  |
| 21 | `INLEND.IMPEXP.DEFAULT.PRN.EXTENSION.PERIOD` | `InlendImportExportAttributes_DefaultPrnExtensionPeriod` | TField |  | Default period for which a Payment Realization can be extended |
| 22 | `INLEND.IMPEXP.MAX.PRN.EXTENSION.COUNT` | `InlendImportExportAttributes_MaxPrnExtensionCount` | TField |  | Default number of times a BOE can be extended |
| 23 | `INLEND.IMPEXP.GRACE.PERIOD.PRN` | `InlendImportExportAttributes_GracePeriodPrn` | TField |  | No of GRACE days up to which MAX PRN DATE can be made, after PRN has crossed MAX PRN Date. |
| 24 | `INLEND.IMPEXP.DEFAULT.IRM.SETTLE.PERIOD` | `InlendImportExportAttributes_DefaultIrmSettlePeriod` | TField |  | Default period for IRM settlement |
| 25 | `INLEND.IMPEXP.MTT.PERIOD` | `InlendImportExportAttributes_MttPeriod` | TField |  | To provide the maximum Merchant trading transaction period in months |
| 26 | `INLEND.IMPEXP.EXP.PROCEED.PRD` | `InlendImportExportAttributes_ExpProceedPrd` | TField |  | To provide the maximum period for the export proceeds to be realized in months |
| 27 | `INLEND.IMPEXP.MTT.IMP.PURPOSE.CODE` | `InlendImportExportAttributes_MttImpPurposeCode` | TField |  | To provide the purpose code for Import proceeds |
| 28 | `INLEND.IMPEXP.MTT.EXP.PURPOSE.CODE` | `InlendImportExportAttributes_MttExpPurposeCode` | TField |  | To provide the purpose code for Export proceeds |
| 29 | `INLEND.IMPEXP.DEFAULT.FIRC.VALID.PERIOD` | `InlendImportExportAttributes_DefaultFircValidPeriod` | TField |  | Default valid period of FIRC issues |
| 30 | `INLEND.IMPEXP.GENERATE.EBRC.AUTOMATICALLY` | `InlendImportExportAttributes_GenerateEbrcAutomatically` | TField |  | This field is of radio button type with YES or NO options. |
| 31 | `INLEND.IMPEXP.EBRC.CURRENCY` | `InlendImportExportAttributes_EbrcCurrency` |  |  |  |
| 32 | `INLEND.IMPEXP.EBRC.CONVERSION.RATE` | `InlendImportExportAttributes_EbrcConversionRate` | TField |  | Holds the conversion rate for calculation TOTAL.REALISED.AMT.INR |
| 33 | `INLEND.IMPEXP.PORT.CODE.INCLUSIVE` | `InlendImportExportAttributes_PortCodeInclusive` | TField |  | Options field. Allowed values are Yes/No. If Yes selected, Boe, Boe Settlement and Obb records should be created with port code as @id. |
| 34 | `INLEND.IMPEXP.RESERVED.1` | `InlendImportExportAttributes_Reserved1` | TField |  | Reserved for future purpose |
| 35 | `INLEND.IMPEXP.LOCAL.REF` | `InlendImportExportAttributes_LocalRef` |  |  |  |
| 36 | `INLEND.IMPEXP.OVERRIDE` | `InlendImportExportAttributes_Override` |  |  |  |
| 37 | `INLEND.IMPEXP.RECORD.STATUS` | `InlendImportExportAttributes_RecordStatus` | String |  |  |
| 38 | `INLEND.IMPEXP.CURR.NO` | `InlendImportExportAttributes_CurrNo` | String |  |  |
| 39 | `INLEND.IMPEXP.INPUTTER` | `InlendImportExportAttributes_Inputter` |  |  |  |
| 40 | `INLEND.IMPEXP.DATE.TIME` | `InlendImportExportAttributes_DateTime` |  |  |  |
| 41 | `INLEND.IMPEXP.AUTHORISER` | `InlendImportExportAttributes_Authoriser` | String |  |  |
| 42 | `INLEND.IMPEXP.CO.CODE` | `InlendImportExportAttributes_CoCode` | String |  |  |
| 43 | `INLEND.IMPEXP.DEPT.CODE` | `InlendImportExportAttributes_DeptCode` | String |  |  |
| 44 | `INLEND.IMPEXP.AUDITOR.CODE` | `InlendImportExportAttributes_AuditorCode` | String |  |  |
| 45 | `INLEND.IMPEXP.AUDIT.DATE.TIME` | `InlendImportExportAttributes_AuditDateTime` | String |  |  |
