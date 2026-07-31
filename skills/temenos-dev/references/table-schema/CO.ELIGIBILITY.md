# CO.ELIGIBILITY — Table Schema

> Source: `INSERTS/I_F.CO.ELIGIBILITY` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.EL.DESCRIPTION` | `CoEligibility_Description` |  |  |  |
| 2 | `CO.EL.ELIGIBILITY.TYPE` | `CoEligibility_EligibilityType` | TField |  | A single value options field which specifies the eligibility rule type. Validation Rules: 1. Valid values are COLLATERAL.TYPE_ASSET.TYPE_SUB.ASSET.TYPE_SECURITY.NO |
| 3 | `CO.EL.ELIGIBILITY.VALUE` | `CoEligibility_EligibilityValue` |  |  |  |
| 4 | `CO.EL.RESERVED.15` | `CoEligibility_Reserved15` | TField |  |  |
| 5 | `CO.EL.RESERVED.14` | `CoEligibility_Reserved14` | TField |  |  |
| 6 | `CO.EL.RESERVED.13` | `CoEligibility_Reserved13` | TField |  |  |
| 7 | `CO.EL.RESERVED.12` | `CoEligibility_Reserved12` | TField |  |  |
| 8 | `CO.EL.RESERVED.11` | `CoEligibility_Reserved11` | TField |  |  |
| 9 | `CO.EL.RESERVED.10` | `CoEligibility_Reserved10` | TField |  |  |
| 10 | `CO.EL.RESERVED.9` | `CoEligibility_Reserved9` | TField |  |  |
| 11 | `CO.EL.RESERVED.8` | `CoEligibility_Reserved8` | TField |  |  |
| 12 | `CO.EL.RESERVED.7` | `CoEligibility_Reserved7` | TField |  |  |
| 13 | `CO.EL.RESERVED.6` | `CoEligibility_Reserved6` | TField |  |  |
| 14 | `CO.EL.RESERVED.5` | `CoEligibility_Reserved5` | TField |  |  |
| 15 | `CO.EL.RESERVED.4` | `CoEligibility_Reserved4` | TField |  |  |
| 16 | `CO.EL.RESERVED.3` | `CoEligibility_Reserved3` | TField |  |  |
| 17 | `CO.EL.RESERVED.2` | `CoEligibility_Reserved2` | TField |  |  |
| 18 | `CO.EL.RESERVED.1` | `CoEligibility_Reserved1` | TField |  |  |
| 19 | `CO.EL.LOCAL.REF` | `CoEligibility_LocalRef` |  |  |  |
| 20 | `CO.EL.OVERRIDE` | `CoEligibility_Override` |  |  |  |
| 21 | `CO.EL.RECORD.STATUS` | `CoEligibility_RecordStatus` | String |  |  |
| 22 | `CO.EL.CURR.NO` | `CoEligibility_CurrNo` | String |  |  |
| 23 | `CO.EL.INPUTTER` | `CoEligibility_Inputter` |  |  |  |
| 24 | `CO.EL.DATE.TIME` | `CoEligibility_DateTime` |  |  |  |
| 25 | `CO.EL.AUTHORISER` | `CoEligibility_Authoriser` | String |  |  |
| 26 | `CO.EL.CO.CODE` | `CoEligibility_CoCode` | String |  |  |
| 27 | `CO.EL.DEPT.CODE` | `CoEligibility_DeptCode` | String |  |  |
| 28 | `CO.EL.AUDITOR.CODE` | `CoEligibility_AuditorCode` | String |  |  |
| 29 | `CO.EL.AUDIT.DATE.TIME` | `CoEligibility_AuditDateTime` | String |  |  |
