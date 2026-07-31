# ILMATX.DIARY.TYPE.PARAM — Table Schema

> Source: `INSERTS/I_F.ILMATX.DIARY.TYPE.PARAM` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MATX.DIARY.MATRIX.TXN.TYPE` | `IlmatxDiaryTypeParam_MatrixTxnType` |  |  |  |
| 2 | `MATX.DIARY.QI.TAX.TYPE` | `IlmatxDiaryTypeParam_QiTaxType` | TField |  | It stores the QI tax type. |
| 3 | `MATX.DIARY.TAX.PRICE.APPLICABLE` | `IlmatxDiaryTypeParam_TaxPriceApplicable` | TField |  | yes or no field to check whether tax price is applicable. |
| 4 | `MATX.DIARY.NEW.SECURITY.PRICE.APPLICABLE` | `IlmatxDiaryTypeParam_NewSecurityPriceApplicable` | TField |  | yes or no field to check whether security price is applicable. |
| 5 | `MATX.DIARY.RESERVED.10` | `IlmatxDiaryTypeParam_Reserved10` | TField |  | Reserved for future use. |
| 6 | `MATX.DIARY.RESERVED.9` | `IlmatxDiaryTypeParam_Reserved9` | TField |  | Reserved for future use. |
| 7 | `MATX.DIARY.RESERVED.8` | `IlmatxDiaryTypeParam_Reserved8` | TField |  | Reserved for future use. |
| 8 | `MATX.DIARY.RESERVED.7` | `IlmatxDiaryTypeParam_Reserved7` | TField |  | Reserved for future use. |
| 9 | `MATX.DIARY.RESERVED.6` | `IlmatxDiaryTypeParam_Reserved6` | TField |  | Reserved for future use. |
| 10 | `MATX.DIARY.RESERVED.5` | `IlmatxDiaryTypeParam_Reserved5` | TField |  | Reserved for future use. |
| 11 | `MATX.DIARY.RESERVED.4` | `IlmatxDiaryTypeParam_Reserved4` | TField |  | Reserved for future use. |
| 12 | `MATX.DIARY.RESERVED.3` | `IlmatxDiaryTypeParam_Reserved3` | TField |  | Reserved for future use. |
| 13 | `MATX.DIARY.RESERVED.2` | `IlmatxDiaryTypeParam_Reserved2` | TField |  | Reserved for future use. |
| 14 | `MATX.DIARY.RESERVED.1` | `IlmatxDiaryTypeParam_Reserved1` | TField |  | Reserved for future use. |
| 15 | `MATX.DIARY.LOCAL.REF` | `IlmatxDiaryTypeParam_LocalRef` |  |  |  |
| 16 | `MATX.DIARY.OVERRIDE` | `IlmatxDiaryTypeParam_Override` |  |  |  |
| 17 | `MATX.DIARY.RECORD.STATUS` | `IlmatxDiaryTypeParam_RecordStatus` | String |  |  |
| 18 | `MATX.DIARY.CURR.NO` | `IlmatxDiaryTypeParam_CurrNo` | String |  |  |
| 19 | `MATX.DIARY.INPUTTER` | `IlmatxDiaryTypeParam_Inputter` |  |  |  |
| 20 | `MATX.DIARY.DATE.TIME` | `IlmatxDiaryTypeParam_DateTime` |  |  |  |
| 21 | `MATX.DIARY.AUTHORISER` | `IlmatxDiaryTypeParam_Authoriser` | String |  |  |
| 22 | `MATX.DIARY.CO.CODE` | `IlmatxDiaryTypeParam_CoCode` | String |  |  |
| 23 | `MATX.DIARY.DEPT.CODE` | `IlmatxDiaryTypeParam_DeptCode` | String |  |  |
| 24 | `MATX.DIARY.AUDITOR.CODE` | `IlmatxDiaryTypeParam_AuditorCode` | String |  |  |
| 25 | `MATX.DIARY.AUDIT.DATE.TIME` | `IlmatxDiaryTypeParam_AuditDateTime` | String |  |  |
