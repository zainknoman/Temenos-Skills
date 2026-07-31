# EB.PRODUCT.IMPORTER — Table Schema

> Source: `INSERTS/I_F.EB.PRODUCT.IMPORTER` in `AA_ProductAttribute.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.PRD.PRODUCT.TYPE` | `EbProductImporter_ProductType` | TField |  |  |
| 2 | `EB.PRD.PRODUCT.NAME` | `EbProductImporter_ProductName` | TField |  |  |
| 3 | `EB.PRD.PRODUCT.DESCRIPTION` | `EbProductImporter_ProductDescription` | TField |  |  |
| 4 | `EB.PRD.AVAILABLE.CURRENCY` | `EbProductImporter_AvailableCurrency` |  |  |  |
| 5 | `EB.PRD.EFFECTIVE.DATE` | `EbProductImporter_EffectiveDate` | TField |  |  |
| 6 | `EB.PRD.VERSION` | `EbProductImporter_Version` | TField |  |  |
| 7 | `EB.PRD.PRODUCT.ID` | `EbProductImporter_ProductId` | TField |  |  |
| 8 | `EB.PRD.RESERVED2` | `EbProductImporter_Reserved2` |  |  |  |
| 9 | `EB.PRD.PRODUCT.ATTRIBUTE` | `EbProductImporter_ProductAttribute` |  |  |  |
| 10 | `EB.PRD.FLD.NAME` | `EbProductImporter_FldName` |  |  |  |
| 11 | `EB.PRD.FLD.VALUE` | `EbProductImporter_FldValue` |  |  |  |
| 12 | `EB.PRD.RESERVED3` | `EbProductImporter_Reserved3` |  |  |  |
| 13 | `EB.PRD.RESERVED4` | `EbProductImporter_Reserved4` |  |  |  |
| 14 | `EB.PRD.RESERVED5` | `EbProductImporter_Reserved5` |  |  |  |
| 15 | `EB.PRD.RESERVED6` | `EbProductImporter_Reserved6` |  |  |  |
| 16 | `EB.PRD.PROPERTY.CONDITION` | `EbProductImporter_PropertyCondition` |  |  |  |
| 17 | `EB.PRD.ATTRIBUTE` | `EbProductImporter_Attribute` |  |  |  |
| 18 | `EB.PRD.FIELD.NAME` | `EbProductImporter_FieldName` |  |  |  |
| 19 | `EB.PRD.FIELD.VALUE` | `EbProductImporter_FieldValue` |  |  |  |
| 20 | `EB.PRD.ATTRIBUTE.PATH` | `EbProductImporter_AttributePath` |  |  |  |
| 21 | `EB.PRD.VARIATION` | `EbProductImporter_Variation` |  |  |  |
| 22 | `EB.PRD.RESERVED9` | `EbProductImporter_Reserved9` |  |  |  |
| 23 | `EB.PRD.RESERVED10` | `EbProductImporter_Reserved10` |  |  |  |
| 24 | `EB.PRD.IMPORT.STATUS` | `EbProductImporter_ImportStatus` | TField |  |  |
| 25 | `EB.PRD.IMPORT.HISTORY` | `EbProductImporter_ImportHistory` |  |  |  |
| 26 | `EB.PRD.IMPORT.DATE` | `EbProductImporter_ImportDate` |  |  |  |
| 27 | `EB.PRD.RETRY` | `EbProductImporter_Retry` | TField |  |  |
| 28 | `EB.PRD.IMPORT.TYPE` | `EbProductImporter_ImportType` | TField |  |  |
| 29 | `EB.PRD.IMPORT.ERROR.TYPE` | `EbProductImporter_ImportErrorType` |  |  |  |
| 30 | `EB.PRD.IMPORT.ERROR.SOURCE` | `EbProductImporter_ImportErrorSource` |  |  |  |
| 31 | `EB.PRD.IMPORT.ERROR` | `EbProductImporter_ImportError` |  |  |  |
| 32 | `EB.PRD.RESERVED11` | `EbProductImporter_Reserved11` |  |  |  |
| 33 | `EB.PRD.RESERVED12` | `EbProductImporter_Reserved12` |  |  |  |
| 34 | `EB.PRD.RESERVED13` | `EbProductImporter_Reserved13` |  |  |  |
| 35 | `EB.PRD.RESERVED14` | `EbProductImporter_Reserved14` | TField |  |  |
| 36 | `EB.PRD.RESERVED15` | `EbProductImporter_Reserved15` | TField |  |  |
| 37 | `EB.PRD.LOCAL.REF` | `EbProductImporter_LocalRef` |  |  |  |
| 38 | `EB.PRD.OVERRIDE` | `EbProductImporter_Override` |  |  |  |
| 39 | `EB.PRD.RECORD.STATUS` | `EbProductImporter_RecordStatus` | String |  |  |
| 40 | `EB.PRD.CURR.NO` | `EbProductImporter_CurrNo` | String |  |  |
| 41 | `EB.PRD.INPUTTER` | `EbProductImporter_Inputter` |  |  |  |
| 42 | `EB.PRD.DATE.TIME` | `EbProductImporter_DateTime` |  |  |  |
| 43 | `EB.PRD.AUTHORISER` | `EbProductImporter_Authoriser` | String |  |  |
| 44 | `EB.PRD.CO.CODE` | `EbProductImporter_CoCode` | String |  |  |
| 45 | `EB.PRD.DEPT.CODE` | `EbProductImporter_DeptCode` | String |  |  |
| 46 | `EB.PRD.AUDITOR.CODE` | `EbProductImporter_AuditorCode` | String |  |  |
| 47 | `EB.PRD.AUDIT.DATE.TIME` | `EbProductImporter_AuditDateTime` | String |  |  |
| 48 | `EB.PRD.EPP.PRODUCT.GROUP` | `EbProductImporter_EppProductGroup` | TField |  |  |
| 49 | `EB.PRD.EPP.PRODUCT.LINE` | `EbProductImporter_EppProductLine` | TField |  |  |
