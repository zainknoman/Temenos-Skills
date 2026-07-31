# LE.ELIGIBILITY.PARAM — Table Schema

> Source: `INSERTS/I_F.LE.ELIGIBILITY.PARAM` in `LE_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LE.LEP.EXCLUDE.COMP` | `LeEligibilityParam_ExcludeComp` |  |  |  |
| 2 | `LE.LEP.ELG.RULE` | `LeEligibilityParam_ElgRule` | TField | No | RULE to identify whether the business application is eligible for LEI check. The rule must be defined using EB.RULE.GATEWAY. The rule identifier must be configured in this field. Usage of ELG Rule and ELG API are mutually exclusive, if defined. Optional Field Validation Rules: Valid EB.RULE.GATEWAY Usage of ELG.RULE and ELG.API are mutually exclusive if defined |
| 3 | `LE.LEP.ELG.API` | `LeEligibilityParam_ElgApi` | TField | No | A local API which can help determine a business application as eligible for LEI check can be attached. The input arguments to this API are application Id, application record and the output arguments are the eligbility flag - YES or NO and errorMessages if any. All these are followed by a reserved argument at the end. Optional Field Validation Rules: Valid EB.API record If both this field and ELG.RULE field do not hold any value then all the transactions under this application areassumed eligible for LEI/NCI check |
| 4 | `LE.LEP.PARTY.FIELD` | `LeEligibilityParam_PartyField` |  |  |  |
| 5 | `LE.LEP.PARTY.ELG.RULE` | `LeEligibilityParam_PartyElgRule` |  |  |  |
| 6 | `LE.LEP.PARTY.ELG.API` | `LeEligibilityParam_PartyElgApi` |  |  |  |
| 7 | `LE.LEP.PARTY.RESERVED.5` | `LeEligibilityParam_PartyReserved5` |  |  |  |
| 8 | `LE.LEP.PARTY.RESERVED.4` | `LeEligibilityParam_PartyReserved4` |  |  |  |
| 9 | `LE.LEP.PARTY.RESERVED.3` | `LeEligibilityParam_PartyReserved3` |  |  |  |
| 10 | `LE.LEP.PARTY.RESERVED.2` | `LeEligibilityParam_PartyReserved2` |  |  |  |
| 11 | `LE.LEP.PARTY.RESERVED.1` | `LeEligibilityParam_PartyReserved1` |  |  |  |
| 12 | `LE.LEP.DERIVATIVE` | `LeEligibilityParam_Derivative` | TField | No | This field is used to mark all or a specfiic type of transaction under a business application as scoped under DERIVATIVE as per MIFID II definition. Optional field and allowed values are YES or NO. YES indicates derivative and Null or NO is considered a non-derivative |
| 13 | `LE.LEP.OVERRIDE.ERROR` | `LeEligibilityParam_OverrideError` | TField | Yes | Indicates whether Error should be thrown by the application or an override when LEI check fails Allowed value is ERROR or OVERRIDE Mandatory Field Validation Rules: Default will be set to OVERRIDE |
| 14 | `LE.LEP.TXN.DATE.FLD` | `LeEligibilityParam_TxnDateFld` | TField |  |  |
| 15 | `LE.LEP.LOCAL.REF` | `LeEligibilityParam_LocalRef` |  |  |  |
| 16 | `LE.LEP.THIRD.PARTY.FIELD` | `LeEligibilityParam_ThirdPartyField` |  |  |  |
| 17 | `LE.LEP.THIRD.PTY.ID.API` | `LeEligibilityParam_ThirdPartyIdApi` |  |  |  |
| 18 | `LE.LEP.RESERVED.08` | `LeEligibilityParam_Reserved08` | TField |  |  |
| 19 | `LE.LEP.RESERVED.07` | `LeEligibilityParam_Reserved07` | TField |  |  |
| 20 | `LE.LEP.RESERVED.06` | `LeEligibilityParam_Reserved06` | TField |  |  |
| 21 | `LE.LEP.RESERVED.05` | `LeEligibilityParam_Reserved05` | TField |  |  |
| 22 | `LE.LEP.RESERVED.04` | `LeEligibilityParam_Reserved04` | TField |  |  |
| 23 | `LE.LEP.RESERVED.03` | `LeEligibilityParam_Reserved03` | TField |  |  |
| 24 | `LE.LEP.RESERVED.02` | `LeEligibilityParam_Reserved02` | TField |  |  |
| 25 | `LE.LEP.RESERVED.01` | `LeEligibilityParam_Reserved01` | TField |  |  |
| 26 | `LE.LEP.RECORD.STATUS` | `LeEligibilityParam_RecordStatus` | String |  |  |
| 27 | `LE.LEP.CURR.NO` | `LeEligibilityParam_CurrNo` | String |  |  |
| 28 | `LE.LEP.INPUTTER` | `LeEligibilityParam_Inputter` |  |  |  |
| 29 | `LE.LEP.DATE.TIME` | `LeEligibilityParam_DateTime` |  |  |  |
| 30 | `LE.LEP.AUTHORISER` | `LeEligibilityParam_Authoriser` | String |  |  |
| 31 | `LE.LEP.CO.CODE` | `LeEligibilityParam_CoCode` | String |  |  |
| 32 | `LE.LEP.DEPT.CODE` | `LeEligibilityParam_DeptCode` | String |  |  |
| 33 | `LE.LEP.AUDITOR.CODE` | `LeEligibilityParam_AuditorCode` | String |  |  |
| 34 | `LE.LEP.AUDIT.DATE.TIME` | `LeEligibilityParam_AuditDateTime` | String |  |  |
