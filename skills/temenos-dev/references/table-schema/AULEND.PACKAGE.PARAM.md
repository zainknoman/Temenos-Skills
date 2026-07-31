# AULEND.PACKAGE.PARAM — Table Schema

> Source: `INSERTS/I_F.AULEND.PACKAGE.PARAM` in `AULEND_AnnualPackageFee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PACKAGE.PARAM.PRODUCT.ID` | `AulendPackageParam_ProductId` |  |  |  |
| 2 | `PACKAGE.PARAM.CUSTOMER.ROLE` | `AulendPackageParam_CustomerRole` |  |  |  |
| 3 | `PACKAGE.PARAM.LOCAL.REF` | `AulendPackageParam_LocalRef` |  |  |  |
| 4 | `PACKAGE.PARAM.OVERRIDE` | `AulendPackageParam_Override` |  |  |  |
| 5 | `PACKAGE.PARAM.RECORD.STATUS` | `AulendPackageParam_RecordStatus` | String |  |  |
| 6 | `PACKAGE.PARAM.CURR.NO` | `AulendPackageParam_CurrNo` | String |  |  |
| 7 | `PACKAGE.PARAM.INPUTTER` | `AulendPackageParam_Inputter` |  |  |  |
| 8 | `PACKAGE.PARAM.DATE.TIME` | `AulendPackageParam_DateTime` |  |  |  |
| 9 | `PACKAGE.PARAM.AUTHORISER` | `AulendPackageParam_Authoriser` | String |  |  |
| 10 | `PACKAGE.PARAM.CO.CODE` | `AulendPackageParam_CoCode` | String |  |  |
| 11 | `PACKAGE.PARAM.DEPT.CODE` | `AulendPackageParam_DeptCode` | String |  |  |
| 12 | `PACKAGE.PARAM.AUDITOR.CODE` | `AulendPackageParam_AuditorCode` | String |  |  |
| 13 | `PACKAGE.PARAM.AUDIT.DATE.TIME` | `AulendPackageParam_AuditDateTime` | String |  |  |
| 14 | `PACKAGE.PARAM.PACKAGE.CHARGE.PROPERTY` | `AulendPackageParam_PackageChargeProperty` | TField |  | This field indicates the Charge property to be used for charging the package fee. This will be no input field and will have drop down field which will display the Charge properties from AA.PROPERTY. If this property is not available in the loan arrangement, the package will not be created. |
