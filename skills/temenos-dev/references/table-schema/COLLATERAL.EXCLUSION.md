# COLLATERAL.EXCLUSION — Table Schema

> Source: `INSERTS/I_F.COLLATERAL.EXCLUSION` in `CO_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.EX.DESCRIPTION` | `CollateralExclusion_Description` |  |  |  |
| 2 | `CO.EX.COUNTRY` | `CollateralExclusion_Country` | TField | Yes | The country whose collateral's are to be excluded The country field in collateral specifies where the collateral is held. To exclude the collaterals belonging to a specific country, the country name can be defined in this field Validation Rules: Upto 5 alphabetic characters (country code) Mandatory input when other criteria fields are not defined Valid record in Country file |
| 3 | `CO.EX.CURRENCY` | `CollateralExclusion_Currency` | TField | No | The currency of the collateral which is to be excluded The currency in the collateral is that in which the collateral values are expressed. If the collaterals of a specific currency to be excluded, then the currency can be defined in this field Validation Rules: 3 alphabetic characters (currency format) Optional field Valid record in Currency file |
| 4 | `CO.EX.SECURITY.CODE` | `CollateralExclusion_SecurityCode` | TField | No | The Security code whose collateral's are to be excluded The collateral attached can be specific to a Security Master If those collaterals are to be excluded, then the Security Master id can be defined in this field The value "NULL" in this field is used to exclude the security collaterals without Security Master Validation Rules: 12 digit optional field Valid SECURITY.MASTER record or value NULL |
| 5 | `CO.EX.ISSUER` | `CollateralExclusion_Issuer` | TField | No | The field defines the Issuer of the security collateral to be excluded To mark the collaterals belonging to a specific issuer for exclusion, this field can be used The value "NULL" in this field is used to exclude the collaterals which does not have Issuer Validation Rules: 10 digit multi-value field Optional field |
| 6 | `CO.EX.INDUSTRY` | `CollateralExclusion_Industry` | TField | No | Industry of the security collateral which is to be excluded The Industry field in collateral indicates the industry to which the security belongs For excluding the security collaterals belonging to a specific industry, the value can be defined in this field The value "NULL" in this field is used to exclude the collaterals which does not have Industry Validation Rules: 1-4 characters Optional field Must be a valid record in SC.INDUSTRY file or the value "NULL" |
| 7 | `CO.EX.COUNTERPARTY` | `CollateralExclusion_Counterparty` | TField | No | Counterparty i.e. Customer of the collateral whose collaterals are to be marked for exclusion If a customer's collateral to be excluded, then customer id can be defined in this field Validation Rules: 10 digit optional field Valid customer record or the value "NULL" |
| 8 | `CO.EX.EXCLUDE.ALL` | `CollateralExclusion_ExcludeAll` | TField |  | This field is used to indicate whether all collaterals belonging to the criteria defined in other fields are to be excluded or not When the field is set to Yes, the service CO.EXCLUDE.SERVICE, will select all the collaterals falling under the criteria and will update the exclusion id When the field is set to No, then the collaterals can be excluded using the fast-path enquiry CO.EXCLUSION On verify the collateral exclusion record, the fast path enquiry CO.EXCLUSION will be launched with the list of collaterals based on the criteria The collaterals required to be excluded can be selected and committed Other fast path enquiry CO.EXCLUSION.AUTH can be used to authorized the collateral records from exception When this field is set to Yes, then the new collaterals if fall under the exclusion criteria, then exclusion id will be automatically defaulted in the EXCLUSION id field of collateral Validation Rules: Values allowed are Yes or No |
| 9 | `CO.EX.RESERVED.10` | `CollateralExclusion_Reserved10` | TField |  |  |
| 10 | `CO.EX.RESERVED.9` | `CollateralExclusion_Reserved9` | TField |  |  |
| 11 | `CO.EX.RESERVED.8` | `CollateralExclusion_Reserved8` | TField |  |  |
| 12 | `CO.EX.RESERVED.7` | `CollateralExclusion_Reserved7` | TField |  |  |
| 13 | `CO.EX.RESERVED.6` | `CollateralExclusion_Reserved6` | TField |  |  |
| 14 | `CO.EX.RESERVED.5` | `CollateralExclusion_Reserved5` | TField |  |  |
| 15 | `CO.EX.RESERVED.4` | `CollateralExclusion_Reserved4` | TField |  |  |
| 16 | `CO.EX.RESERVED.3` | `CollateralExclusion_Reserved3` | TField |  |  |
| 17 | `CO.EX.RESERVED.2` | `CollateralExclusion_Reserved2` | TField |  |  |
| 18 | `CO.EX.RESERVED.1` | `CollateralExclusion_Reserved1` | TField |  |  |
| 19 | `CO.EX.LOCAL.REF` | `CollateralExclusion_LocalRef` |  |  |  |
| 20 | `CO.EX.OVERRIDE` | `CollateralExclusion_Override` |  |  |  |
| 21 | `CO.EX.RECORD.STATUS` | `CollateralExclusion_RecordStatus` | String |  |  |
| 22 | `CO.EX.CURR.NO` | `CollateralExclusion_CurrNo` | String |  |  |
| 23 | `CO.EX.INPUTTER` | `CollateralExclusion_Inputter` |  |  |  |
| 24 | `CO.EX.DATE.TIME` | `CollateralExclusion_DateTime` |  |  |  |
| 25 | `CO.EX.AUTHORISER` | `CollateralExclusion_Authoriser` | String |  |  |
| 26 | `CO.EX.CO.CODE` | `CollateralExclusion_CoCode` | String |  |  |
| 27 | `CO.EX.DEPT.CODE` | `CollateralExclusion_DeptCode` | String |  |  |
| 28 | `CO.EX.AUDITOR.CODE` | `CollateralExclusion_AuditorCode` | String |  |  |
| 29 | `CO.EX.AUDIT.DATE.TIME` | `CollateralExclusion_AuditDateTime` | String |  |  |
