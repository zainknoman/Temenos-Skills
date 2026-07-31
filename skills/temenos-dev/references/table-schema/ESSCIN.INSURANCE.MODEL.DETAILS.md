# ESSCIN.INSURANCE.MODEL.DETAILS — Table Schema

> Source: `INSERTS/I_F.ESSCIN.INSURANCE.MODEL.DETAILS` in `ESSPIN_SocialInsurance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.MD.MODEL.TYPE` | `EsscinInsuranceModelDetails_ModelType` | TField |  | Refers to the insurance type |
| 2 | `ES.MD.MODEL` | `EsscinInsuranceModelDetails_Model` | TField |  | Referes to TC Code |
| 3 | `ES.MD.MODEL.CODE` | `EsscinInsuranceModelDetails_ModelCode` | TField |  | User configures Model Code corresponding to the MODEL |
| 4 | `ES.MD.MODEL.DESCRIPTION` | `EsscinInsuranceModelDetails_ModelDescription` |  |  |  |
| 5 | `ES.MD.SUFFIX` | `EsscinInsuranceModelDetails_Suffix` | TField |  | User configures ISSUER SUFFIX |
| 6 | `ES.MD.REGIME` | `EsscinInsuranceModelDetails_Regime` |  |  |  |
| 7 | `ES.MD.CODE.QUOTE.MODEL` | `EsscinInsuranceModelDetails_CodeQuoteModel` | TField |  | User configures CODE QUOTE MODEL corresponding to the MODEL |
| 8 | `ES.MD.LOCAL.REF` | `EsscinInsuranceModelDetails_LocalRef` |  |  |  |
| 9 | `ES.MD.SOCIAL.SECURITY.IDENTIFIER` | `EsscinInsuranceModelDetails_SocialSecurityIdentifier` |  |  |  |
| 10 | `ES.MD.RESERVED.2` | `EsscinInsuranceModelDetails_Reserved2` | TField |  |  |
| 11 | `ES.MD.RESERVED.3` | `EsscinInsuranceModelDetails_Reserved3` | TField |  |  |
| 12 | `ES.MD.RESERVED.4` | `EsscinInsuranceModelDetails_Reserved4` | TField |  |  |
| 13 | `ES.MD.RESERVED.5` | `EsscinInsuranceModelDetails_Reserved5` | TField |  |  |
| 14 | `ES.MD.RESERVED.6` | `EsscinInsuranceModelDetails_Reserved6` | TField |  |  |
| 15 | `ES.MD.RESERVED.7` | `EsscinInsuranceModelDetails_Reserved7` | TField |  |  |
| 16 | `ES.MD.RESERVED.8` | `EsscinInsuranceModelDetails_Reserved8` | TField |  |  |
| 17 | `ES.MD.RESERVED.9` | `EsscinInsuranceModelDetails_Reserved9` | TField |  |  |
| 18 | `ES.MD.RESERVED.10` | `EsscinInsuranceModelDetails_Reserved10` | TField |  |  |
| 19 | `ES.MD.RESERVED.11` | `EsscinInsuranceModelDetails_Reserved11` | TField |  |  |
| 20 | `ES.MD.RESERVED.12` | `EsscinInsuranceModelDetails_Reserved12` | TField |  |  |
| 21 | `ES.MD.RESERVED.13` | `EsscinInsuranceModelDetails_Reserved13` | TField |  |  |
| 22 | `ES.MD.RESERVED.14` | `EsscinInsuranceModelDetails_Reserved14` | TField |  |  |
| 23 | `ES.MD.RESERVED.15` | `EsscinInsuranceModelDetails_Reserved15` | TField |  |  |
| 24 | `ES.MD.OVERRIDE` | `EsscinInsuranceModelDetails_Override` |  |  |  |
| 25 | `ES.MD.RECORD.STATUS` | `EsscinInsuranceModelDetails_RecordStatus` | String |  |  |
| 26 | `ES.MD.CURR.NO` | `EsscinInsuranceModelDetails_CurrNo` | String |  |  |
| 27 | `ES.MD.INPUTTER` | `EsscinInsuranceModelDetails_Inputter` |  |  |  |
| 28 | `ES.MD.DATE.TIME` | `EsscinInsuranceModelDetails_DateTime` |  |  |  |
| 29 | `ES.MD.AUTHORISER` | `EsscinInsuranceModelDetails_Authoriser` | String |  |  |
| 30 | `ES.MD.CO.CODE` | `EsscinInsuranceModelDetails_CoCode` | String |  |  |
| 31 | `ES.MD.DEPT.CODE` | `EsscinInsuranceModelDetails_DeptCode` | String |  |  |
| 32 | `ES.MD.AUDITOR.CODE` | `EsscinInsuranceModelDetails_AuditorCode` | String |  |  |
| 33 | `ES.MD.AUDIT.DATE.TIME` | `EsscinInsuranceModelDetails_AuditDateTime` | String |  |  |
