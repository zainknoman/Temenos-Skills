# NA.PRODUCT.FIT.DEFINITION — Table Schema

> Source: `INSERTS/I_F.NA.PRODUCT.FIT.DEFINITION` in `NA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.PFD.MC.FIELD` | `NaProductFitDefinition_McField` |  |  |  |
| 2 | `NA.PFD.MC.FIELD.DEFAULT` | `NaProductFitDefinition_McFieldDefault` |  |  |  |
| 3 | `NA.PFD.PRODUCT.FIT.TYPE` | `NaProductFitDefinition_ProductFitType` |  |  |  |
| 4 | `NA.PFD.NEEDS.QUESTION` | `NaProductFitDefinition_NeedsQuestion` |  |  |  |
| 5 | `NA.PFD.STANDARDIZE` | `NaProductFitDefinition_Standardize` |  |  |  |
| 6 | `NA.PFD.METRIC.WEIGHT` | `NaProductFitDefinition_MetricWeight` |  |  |  |
| 7 | `NA.PFD.KNOCKOUT` | `NaProductFitDefinition_Knockout` |  |  |  |
| 8 | `NA.PFD.INT.ENQ.MC.FIELDS` | `NaProductFitDefinition_IntEnqMcFields` |  |  |  |
| 9 | `NA.PFD.INT.ENQ.REC.FIELDS` | `NaProductFitDefinition_IntEnqRecFields` |  |  |  |
| 10 | `NA.PFD.EXT.ENQ.MC.FIELDS` | `NaProductFitDefinition_ExtEnqMcFields` |  |  |  |
| 11 | `NA.PFD.EXT.ENQ.REC.FIELDS` | `NaProductFitDefinition_ExtEnqRecFields` |  |  |  |
| 12 | `NA.PFD.RESERVED.8` | `NaProductFitDefinition_Reserved8` | TField |  |  |
| 13 | `NA.PFD.ACTION` | `NaProductFitDefinition_Action` | TField | No | This field indicates which action will be performed after the record is authorised Optional Input Validation Rules a. Allowed values are Null of PUBLISH : If action is null the definition is simply being saved on file after authorization. If PUBLISH is specified, then the data will be written to catalog file - NA.PRODUCT.FIT.METHOD.CATALOG and updates application NA.PRODUCT.FIT.METHOD b.T24 string Input |
| 14 | `NA.PFD.EXPIRY.DATE` | `NaProductFitDefinition_ExpiryDate` | TField | No | Once defined , the product fit definition object can be PUBLISHED as many times as needed until it is expired. The product fit definition object can be set to expire by providing a future date in the EXPIRY.DATE field Optional Input Validation Rules a. Date provided should be in the future. b.T24 Date Input |
| 15 | `NA.PFD.PUBLISH.STATUS` | `NaProductFitDefinition_PublishStatus` | TField |  | PUBLISH.STATUS This field will contain the result of the publishing effort 1) Validation Rules a. No Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Errors |
| 16 | `NA.PFD.PUBLISH.STATUS.DATE` | `NaProductFitDefinition_PublishStatusDate` | TField |  | This field will indicate the date on which the product fit definition object was published. System maintained noinput field |
| 17 | `NA.PFD.AVAILABLE.DATE` | `NaProductFitDefinition_AvailableDate` | TField |  | This field will indicate from when the product fit definition object is available. Noinput field System Maintained |
| 18 | `NA.PFD.RESERVED.7` | `NaProductFitDefinition_Reserved7` |  |  |  |
| 19 | `NA.PFD.RESERVED.6` | `NaProductFitDefinition_Reserved6` |  |  |  |
| 20 | `NA.PFD.REFERENCE` | `NaProductFitDefinition_Reference` | TField |  | This field indicates the name of the product fit definition Object (valid purpose). System maintained noinput field |
| 21 | `NA.PFD.VERSION` | `NaProductFitDefinition_Version` | TField |  | This field specifies the version of the current product fit definition purpose. System maintained noinput field |
| 22 | `NA.PFD.VERSION.DATE` | `NaProductFitDefinition_VersionDate` | TField |  | This field specifies the effective date of the current product fit definition purpose. System maintained noinput field |
| 23 | `NA.PFD.MC.OUT.FIELD` | `NaProductFitDefinition_McOutField` |  |  |  |
| 24 | `NA.PFD.RESERVED.4` | `NaProductFitDefinition_Reserved4` | TField |  |  |
| 25 | `NA.PFD.RESERVED.3` | `NaProductFitDefinition_Reserved3` | TField |  |  |
| 26 | `NA.PFD.RESERVED.2` | `NaProductFitDefinition_Reserved2` | TField |  |  |
| 27 | `NA.PFD.RESERVED.1` | `NaProductFitDefinition_Reserved1` | TField |  |  |
| 28 | `NA.PFD.LOCAL.REF` | `NaProductFitDefinition_LocalRef` |  |  |  |
| 29 | `NA.PFD.OVERRIDE` | `NaProductFitDefinition_Override` |  |  |  |
| 30 | `NA.PFD.RECORD.STATUS` | `NaProductFitDefinition_RecordStatus` | String |  |  |
| 31 | `NA.PFD.CURR.NO` | `NaProductFitDefinition_CurrNo` | String |  |  |
| 32 | `NA.PFD.INPUTTER` | `NaProductFitDefinition_Inputter` |  |  |  |
| 33 | `NA.PFD.DATE.TIME` | `NaProductFitDefinition_DateTime` |  |  |  |
| 34 | `NA.PFD.AUTHORISER` | `NaProductFitDefinition_Authoriser` | String |  |  |
| 35 | `NA.PFD.CO.CODE` | `NaProductFitDefinition_CoCode` | String |  |  |
| 36 | `NA.PFD.DEPT.CODE` | `NaProductFitDefinition_DeptCode` | String |  |  |
| 37 | `NA.PFD.AUDITOR.CODE` | `NaProductFitDefinition_AuditorCode` | String |  |  |
| 38 | `NA.PFD.AUDIT.DATE.TIME` | `NaProductFitDefinition_AuditDateTime` | String |  |  |
