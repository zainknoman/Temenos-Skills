# LENINS.INSURANCE.PARAM — Table Schema

> Source: `INSERTS/I_F.LENINS.INSURANCE.PARAM` in `LENINS_Insurance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INSPARAM.INSURANCE.OPTION` | `LeninsInsuranceParam_InsuranceOption` | TField |  | The field is to choose from the valid options given as radio buttons.Valid values: LOC INSURANCE, LIFE INSURANCE and DISABILITY INSURANCE. |
| 2 | `INSPARAM.AGE` | `LeninsInsuranceParam_Age` |  |  |  |
| 3 | `INSPARAM.RATE` | `LeninsInsuranceParam_Rate` |  |  |  |
| 4 | `INSPARAM.ADJUST.FACTOR` | `LeninsInsuranceParam_AdjustFactor` | TField |  | The Adjustment Factor for the year would be defined in this field. This is only for LOC Insurance premium calculation. |
| 5 | `INSPARAM.MIN.AGE` | `LeninsInsuranceParam_MinAge` | TField |  | This field is to specify the Minimum Age for availing the Insurance. |
| 6 | `INSPARAM.MAX.AGE` | `LeninsInsuranceParam_MaxAge` | TField |  | This field is to specify the Maximum Age until Insurance can be availed |
| 7 | `INSPARAM.ONLY.RENEW.AGE` | `LeninsInsuranceParam_OnlyRenewAge` | TField |  | This field is to mention the Age at which the insurance can be renewed |
| 8 | `INSPARAM.CONV.API` | `LeninsInsuranceParam_ConvApi` | TField |  | Specify: An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record LENINS.INSURANCE.PAR.CONV.API.HOOK. This field supports the Insurance.getCharge() method. The Insurance class is in the com.temenos.t24.api.hook.countrymodelbank.canada package which is in LENINS_InsuranceHook.jar shipped with T24. Field to store the local routine/api for Insurance charge calculation. |
| 9 | `INSPARAM.RESERVED.9` | `LeninsInsuranceParam_Reserved9` | TField |  |  |
| 10 | `INSPARAM.RESERVED.8` | `LeninsInsuranceParam_Reserved8` | TField |  | Future Use |
| 11 | `INSPARAM.RESERVED.7` | `LeninsInsuranceParam_Reserved7` | TField |  | Future Use |
| 12 | `INSPARAM.RESERVED.6` | `LeninsInsuranceParam_Reserved6` | TField |  | Future Use |
| 13 | `INSPARAM.RESERVED.5` | `LeninsInsuranceParam_Reserved5` | TField |  | Future Use |
| 14 | `INSPARAM.RESERVED.4` | `LeninsInsuranceParam_Reserved4` | TField |  | Future Use |
| 15 | `INSPARAM.RESERVED.3` | `LeninsInsuranceParam_Reserved3` | TField |  | Future Use |
| 16 | `INSPARAM.RESERVED.2` | `LeninsInsuranceParam_Reserved2` | TField |  | Future Use |
| 17 | `INSPARAM.RESERVED.1` | `LeninsInsuranceParam_Reserved1` | TField |  | Future Use |
| 18 | `INSPARAM.LOCAL.REF` | `LeninsInsuranceParam_LocalRef` |  |  |  |
| 19 | `INSPARAM.OVERRIDE` | `LeninsInsuranceParam_Override` |  |  |  |
| 20 | `INSPARAM.RECORD.STATUS` | `LeninsInsuranceParam_RecordStatus` | String |  |  |
| 21 | `INSPARAM.CURR.NO` | `LeninsInsuranceParam_CurrNo` | String |  |  |
| 22 | `INSPARAM.INPUTTER` | `LeninsInsuranceParam_Inputter` |  |  |  |
| 23 | `INSPARAM.DATE.TIME` | `LeninsInsuranceParam_DateTime` |  |  |  |
| 24 | `INSPARAM.AUTHORISER` | `LeninsInsuranceParam_Authoriser` | String |  |  |
| 25 | `INSPARAM.CO.CODE` | `LeninsInsuranceParam_CoCode` | String |  |  |
| 26 | `INSPARAM.DEPT.CODE` | `LeninsInsuranceParam_DeptCode` | String |  |  |
| 27 | `INSPARAM.AUDITOR.CODE` | `LeninsInsuranceParam_AuditorCode` | String |  |  |
| 28 | `INSPARAM.AUDIT.DATE.TIME` | `LeninsInsuranceParam_AuditDateTime` | String |  |  |
