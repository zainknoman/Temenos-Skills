# FICOLL.COLLATERAL.PARAM — Table Schema

> Source: `INSERTS/I_F.FICOLL.COLLATERAL.PARAM` in `FICOLL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FICOLL.PARAM.DEPRE.COLLATERAL.TYPE` | `FicollCollateralParam_DepreCollateralType` |  |  |  |
| 2 | `FICOLL.PARAM.LEASE.EXPIRY.TASK.PERIOD` | `FicollCollateralParam_LeaseExpiryTaskPeriod` | TField |  | Holds the period of lease expiry upto which the service should pick the collateral to create the task. Validation Rules: It can be given in days or months or years. Days format = xxxD , Months format = xxM Years format = xxY. Where x is a numeric value. |
| 3 | `FICOLL.PARAM.HL.TYPE` | `FicollCollateralParam_HlType` |  |  |  |
| 4 | `FICOLL.PARAM.GARANTIA.PROP.TYPE` | `FicollCollateralParam_GarantiaPropType` | TField |  |  |
| 5 | `FICOLL.PARAM.HL.COL.TYPE` | `FicollCollateralParam_HlColType` |  |  |  |
| 6 | `FICOLL.PARAM.CASH.COL.TYPE` | `FicollCollateralParam_CashColType` |  |  |  |
| 7 | `FICOLL.PARAM.HAL.COL.TYPE` | `FicollCollateralParam_HalColType` | TField |  | This field holds the Collateral Type HAL guarantee. |
| 8 | `FICOLL.PARAM.BREACH.PERCENTAGE` | `FicollCollateralParam_BreachPercentage` | TField |  | This field holds the percentage of LTC above which the warning message has to be raised to capture the breach reason. As of now we consider it as 85%. |
| 9 | `FICOLL.PARAM.BREACH.FIRST.HOUSE` | `FicollCollateralParam_BreachFirstHouse` | TField |  | This field holds the percentage of LTC allowed, when the breach reason is chosen as First House. If the LTC value is higher than this percentage for First House, then system should throw an error message. This percentage will be greater than FICOLL.PARAM.BREACH.PERCENTAGE. |
| 10 | `FICOLL.PARAM.LEASE.NOTES` | `FicollCollateralParam_LeaseNotes` | TField |  | This field holds the lease notes which specifies the action to be taken while creating a task in CR.CONTACT.LOG. |
| 11 | `FICOLL.PARAM.DEPRECIATION.METHOD` | `FicollCollateralParam_DepreciationMethod` |  |  |  |
| 12 | `FICOLL.PARAM.DEPRECIATION.API` | `FicollCollateralParam_DepreciationApi` |  |  |  |
| 13 | `FICOLL.PARAM.NV.LOWER.BREACH.CAP` | `FicollCollateralParam_NvLowerBreachCap` | TField |  | Holds the value of % difference between the existing and new Nominal value below which the override message has to be raised. |
| 14 | `FICOLL.PARAM.NV.UPPER.BREACH.CAP` | `FicollCollateralParam_NvUpperBreachCap` | TField |  | Holds the value of % difference between the existing and new Nominal value below which the override message has to be raised. |
| 15 | `FICOLL.PARAM.EXPIRY.GRANTEE.TYPE` | `FicollCollateralParam_ExpiryGranteeType` |  |  |  |
| 16 | `FICOLL.PARAM.GRANTEE.RENEWAL` | `FicollCollateralParam_GranteeRenewal` |  |  |  |
| 17 | `FICOLL.PARAM.ASSET.TYPE` | `FicollCollateralParam_AssetType` |  |  |  |
| 18 | `FICOLL.PARAM.BEARER.BOND.COL.TYPE` | `FicollCollateralParam_BearerBondColType` |  |  |  |
| 19 | `FICOLL.PARAM.INDEX.ID.CATEG` | `FicollCollateralParam_IndexIdCateg` |  |  |  |
| 20 | `FICOLL.PARAM.HOUSING.TYPE.CODE` | `FicollCollateralParam_HousingTypeCode` |  |  |  |
| 21 | `FICOLL.PARAM.SV.DIFF.PERCENTAGE` | `FicollCollateralParam_SvDiffPercentage` | TField |  | This field holds the percentage of difference in Statistical value and Nominal value. |
| 22 | `FICOLL.PARAM.HC.SERVICE.PROC.DATE` | `FicollCollateralParam_HcServiceProcDate` | TField |  | This field holds the last service run date of Dwelling house type index. |
| 23 | `FICOLL.PARAM.DC.SERVICE.PROC.DATE` | `FicollCollateralParam_DcServiceProcDate` | TField |  | This fields holds the last service run date of Detached house type index . |
| 24 | `FICOLL.PARAM.HOUSING.PROP.TYPE` | `FicollCollateralParam_HousingPropType` | TField |  | This field holds the collateral code of the Housing Property Type. |
| 25 | `FICOLL.PARAM.NLS.APPLICATION` | `FicollCollateralParam_NlsApplication` | TField |  | This field holds the T24 Application name, where the NLS details are stored. |
| 26 | `FICOLL.PARAM.NLS.FIELD` | `FicollCollateralParam_NlsField` | TField |  | This field holds the Field name in the above configured table, where housing company loan detail is defined. |
| 27 | `FICOLL.PARAM.GARANTIA.PERIOD` | `FicollCollateralParam_GarantiaPeriod` | TField |  | This field stores the garantia periods either in months or years. |
| 28 | `FICOLL.PARAM.HALG.CHARGE.ACTIVITY` | `FicollCollateralParam_HalgChargeActivity` |  |  |  |
| 29 | `FICOLL.PARAM.RESERVED.13` | `FicollCollateralParam_Reserved13` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 30 | `FICOLL.PARAM.RESERVED.12` | `FicollCollateralParam_Reserved12` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 31 | `FICOLL.PARAM.RESERVED.11` | `FicollCollateralParam_Reserved11` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 32 | `FICOLL.PARAM.RESERVED.10` | `FicollCollateralParam_Reserved10` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 33 | `FICOLL.PARAM.RESERVED.9` | `FicollCollateralParam_Reserved9` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 34 | `FICOLL.PARAM.RESERVED.8` | `FicollCollateralParam_Reserved8` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 35 | `FICOLL.PARAM.RESERVED.7` | `FicollCollateralParam_Reserved7` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 36 | `FICOLL.PARAM.RESERVED.6` | `FicollCollateralParam_Reserved6` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 37 | `FICOLL.PARAM.RESERVED.5` | `FicollCollateralParam_Reserved5` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 38 | `FICOLL.PARAM.RESERVED.4` | `FicollCollateralParam_Reserved4` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 39 | `FICOLL.PARAM.RESERVED.3` | `FicollCollateralParam_Reserved3` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 40 | `FICOLL.PARAM.RESERVED.2` | `FicollCollateralParam_Reserved2` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 41 | `FICOLL.PARAM.RESERVED.1` | `FicollCollateralParam_Reserved1` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 42 | `FICOLL.PARAM.LOCAL.REF` | `FicollCollateralParam_LocalRef` |  |  |  |
| 43 | `FICOLL.PARAM.OVERRIDE` | `FicollCollateralParam_Override` |  |  |  |
| 44 | `FICOLL.PARAM.RECORD.STATUS` | `FicollCollateralParam_RecordStatus` | String |  |  |
| 45 | `FICOLL.PARAM.CURR.NO` | `FicollCollateralParam_CurrNo` | String |  |  |
| 46 | `FICOLL.PARAM.INPUTTER` | `FicollCollateralParam_Inputter` |  |  |  |
| 47 | `FICOLL.PARAM.DATE.TIME` | `FicollCollateralParam_DateTime` |  |  |  |
| 48 | `FICOLL.PARAM.AUTHORISER` | `FicollCollateralParam_Authoriser` | String |  |  |
| 49 | `FICOLL.PARAM.CO.CODE` | `FicollCollateralParam_CoCode` | String |  |  |
| 50 | `FICOLL.PARAM.DEPT.CODE` | `FicollCollateralParam_DeptCode` | String |  |  |
| 51 | `FICOLL.PARAM.AUDITOR.CODE` | `FicollCollateralParam_AuditorCode` | String |  |  |
| 52 | `FICOLL.PARAM.AUDIT.DATE.TIME` | `FicollCollateralParam_AuditDateTime` | String |  |  |
