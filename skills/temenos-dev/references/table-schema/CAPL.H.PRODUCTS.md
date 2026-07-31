# CAPL.H.PRODUCTS — Table Schema

> Source: `INSERTS/I_F.CAPL.H.PRODUCTS` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.PROD.SHORT.DESCRP` | `CaplHProducts_ShortDescrp` | TField |  | This field is used to provide short description of the parameter record.Validation : It is a free text field.Eg: MDI param |
| 2 | `MDI.PROD.DESCRIPTION` | `CaplHProducts_Description` |  |  |  |
| 3 | `MDI.PROD.ALLOWED.TO.OPEN` | `CaplHProducts_AllowedToOpen` | TField |  | This field used define whether this product can be opened through member direct interface.Possible values are "Y" and "N". If this is set to "Y" indicates that this product canbe allowed to open fromMember direct interface.If this is set to "N" then theassociated product cannot beopened through Online Banking. then it |
| 4 | `MDI.PROD.AC.CATEGORY` | `CaplHProducts_AcCategory` |  |  |  |
| 5 | `MDI.PROD.ACCOUNT.PRODUCT` | `CaplHProducts_AccountProduct` |  |  |  |
| 6 | `MDI.PROD.TERM.PRODUCT` | `CaplHProducts_TermProduct` |  |  |  |
| 7 | `MDI.PROD.APP.FIELD` | `CaplHProducts_AppField` |  |  |  |
| 8 | `MDI.PROD.APP.VALUES` | `CaplHProducts_AppValues` |  |  |  |
| 9 | `MDI.PROD.PRODUCT.CURRENCY` | `CaplHProducts_ProductCurrency` | TField |  | This field used to provide currency which is going to be used for the account opening.Validation: The value in this field should be a valid record from NUMERIC.CURRENCYEg: 124 |
| 10 | `MDI.PROD.PROD.SUB.TYPE` | `CaplHProducts_ProdSubType` | TField |  | Type of product |
| 11 | `MDI.PROD.PROPERTY` | `CaplHProducts_Property` |  |  |  |
| 12 | `MDI.PROD.FIELD.NAME` | `CaplHProducts_FieldName` |  |  |  |
| 13 | `MDI.PROD.FIELD.VALUE` | `CaplHProducts_FieldValue` |  |  |  |
| 14 | `MDI.PROD.EFFECTIVE` | `CaplHProducts_Effective` |  |  |  |
| 15 | `MDI.PROD.IMT.ELIGIBLE` | `CaplHProducts_ImtEligible` | TField |  | Purpose of the field to define the ID product is eligible for Inter Member Transfer. Allowed inputs - Yes / NoYes - Product is eligible for Inter Member Transfer.No - Product is not eligible for Inter Member Transfer. |
| 16 | `MDI.PROD.RESERVED.2` | `CaplHProducts_Reserved2` | TField |  |  |
| 17 | `MDI.PROD.RESERVED.1` | `CaplHProducts_Reserved1` | TField |  |  |
| 18 | `MDI.PROD.LOCAL.REF` | `CaplHProducts_LocalRef` |  |  |  |
| 19 | `MDI.PROD.OVERRIDE` | `CaplHProducts_Override` |  |  |  |
| 20 | `MDI.PROD.RECORD.STATUS` | `CaplHProducts_RecordStatus` | String |  |  |
| 21 | `MDI.PROD.CURR.NO` | `CaplHProducts_CurrNo` | String |  |  |
| 22 | `MDI.PROD.INPUTTER` | `CaplHProducts_Inputter` |  |  |  |
| 23 | `MDI.PROD.DATE.TIME` | `CaplHProducts_DateTime` |  |  |  |
| 24 | `MDI.PROD.AUTHORISER` | `CaplHProducts_Authoriser` | String |  |  |
| 25 | `MDI.PROD.CO.CODE` | `CaplHProducts_CoCode` | String |  |  |
| 26 | `MDI.PROD.DEPT.CODE` | `CaplHProducts_DeptCode` | String |  |  |
| 27 | `MDI.PROD.AUDITOR.CODE` | `CaplHProducts_AuditorCode` | String |  |  |
| 28 | `MDI.PROD.AUDIT.DATE.TIME` | `CaplHProducts_AuditDateTime` | String |  |  |
