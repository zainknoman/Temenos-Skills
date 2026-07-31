# FINCEN.EXEMPT.CONTROL.PARAM — Table Schema

> Source: `INSERTS/I_F.FINCEN.EXEMPT.CONTROL.PARAM` in `USREGS_FinCENBeneficialOwner.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FINCEN.PARAM.EXEMPTION.TYPE` | `FincenExemptControlParam_ExemptionType` | TField |  | Bank defined field with the reason that would exclude certain beneficial ownership information from being required at the customer level. Validation Rules: Free text field. 35 characters. |
| 2 | `FINCEN.PARAM.OWNERSHIP.PRONG` | `FincenExemptControlParam_OwnershipProng` | TField | Yes | Set YES if Ownership prong information is mandatory during customer creation. Validation Rules: Option YES or NO. |
| 3 | `FINCEN.PARAM.CONTROL.PRONG` | `FincenExemptControlParam_ControlProng` | TField | Yes | Set YES if Control prong information is mandatory during customer creation. Validation Rules: Option YES or NO. |
| 4 | `FINCEN.PARAM.CERTIFICATION.INFO` | `FincenExemptControlParam_CertificationInfo` | TField | Yes | Set YES if Certification information is mandatory during customer creation. Validation Rules: Option YES or NO. |
| 5 | `FINCEN.PARAM.RESERVED.9` | `FincenExemptControlParam_Reserved9` | TField |  |  |
| 6 | `FINCEN.PARAM.RESERVED.8` | `FincenExemptControlParam_Reserved8` | TField |  |  |
| 7 | `FINCEN.PARAM.RESERVED.7` | `FincenExemptControlParam_Reserved7` | TField |  |  |
| 8 | `FINCEN.PARAM.RESERVED.6` | `FincenExemptControlParam_Reserved6` | TField |  |  |
| 9 | `FINCEN.PARAM.RESERVED.5` | `FincenExemptControlParam_Reserved5` | TField |  |  |
| 10 | `FINCEN.PARAM.RESERVED.4` | `FincenExemptControlParam_Reserved4` | TField |  |  |
| 11 | `FINCEN.PARAM.RESERVED.3` | `FincenExemptControlParam_Reserved3` | TField |  |  |
| 12 | `FINCEN.PARAM.RESERVED.2` | `FincenExemptControlParam_Reserved2` | TField |  |  |
| 13 | `FINCEN.PARAM.RESERVED.1` | `FincenExemptControlParam_Reserved1` | TField |  |  |
| 14 | `FINCEN.PARAM.OVERRIDE` | `FincenExemptControlParam_Override` |  |  |  |
| 15 | `FINCEN.PARAM.RECORD.STATUS` | `FincenExemptControlParam_RecordStatus` | String |  |  |
| 16 | `FINCEN.PARAM.CURR.NO` | `FincenExemptControlParam_CurrNo` | String |  |  |
| 17 | `FINCEN.PARAM.INPUTTER` | `FincenExemptControlParam_Inputter` |  |  |  |
| 18 | `FINCEN.PARAM.DATE.TIME` | `FincenExemptControlParam_DateTime` |  |  |  |
| 19 | `FINCEN.PARAM.AUTHORISER` | `FincenExemptControlParam_Authoriser` | String |  |  |
| 20 | `FINCEN.PARAM.CO.CODE` | `FincenExemptControlParam_CoCode` | String |  |  |
| 21 | `FINCEN.PARAM.DEPT.CODE` | `FincenExemptControlParam_DeptCode` | String |  |  |
| 22 | `FINCEN.PARAM.AUDITOR.CODE` | `FincenExemptControlParam_AuditorCode` | String |  |  |
| 23 | `FINCEN.PARAM.AUDIT.DATE.TIME` | `FincenExemptControlParam_AuditDateTime` | String |  |  |
