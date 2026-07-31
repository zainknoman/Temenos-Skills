# CZ.CDP.PURPOSE — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.PURPOSE` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CDP.PURPOSE` | `CzCdpPurpose_Purpose` | TField |  | This field defines the purpose Allowed values initially are CONSENT,CONTRACTUAL,LEGAL,LEGITIMATE,TRANSACTION Additional values may be added using EB.LOOKUP e.g. Public Interest, Vital Interest |
| 2 | `CZ.CDP.ALLOW.IF.CUS.ERASED` | `CzCdpPurpose_AllowIfCusErased` | TField |  | NOINPUT field This field is not used currently |
| 3 | `CZ.CDP.RETENTION.PERIOD` | `CzCdpPurpose_RetentionPeriod` | TField |  | This field contains the standard period of retention assigned to each purpose. This standard or the default retention period would apply to all companies unless the company specific retention period (COMP.RET.PERIOD) is defined. Validations: Periods in day, month, or year e.g. 29D, 01M or 05Y. Should be in this format Either RETENTION.PERIOD or RET.PERIOD.RULE or RET.PERIOD.API is allowed if the PURPOSE is not TRANSACTION |
| 4 | `CZ.CDP.RET.PERIOD.RULE` | `CzCdpPurpose_RetPeriodRule` | TField |  | This will be a link to EB.RULE.GATEWAY where there will a rule define in the Rules Engine that will apply a rule and a retention period. Validations: Only allowed if RET.PERIOD.API and RETENTION.PERIOD not input and if the PURPOSE is not TRANSACTION |
| 5 | `CZ.CDP.RET.PERIOD.API` | `CzCdpPurpose_RetPeriodApi` | TField |  | An API to apply a logic and return a Retention period, it will be a valid record in EB.API Validations: Only allowed if RET.PERIOD.RULE and RETENTION.PERIOD not input and if the PURPOSE is not TRANSACTION |
| 6 | `CZ.CDP.COMP.RET.PERIOD` | `CzCdpPurpose_CompRetPeriod` |  |  |  |
| 7 | `CZ.CDP.ALLOW.ACTIVE.ERASURE` | `CzCdpPurpose_AllowActiveErasure` | TField |  | The field defines whether the purpose is allowed for erasure when the customer is still active. Validation Rules: Valid options are YES or NO. Default is NO. The field is enabled only when the field ALLOW.ACTIVE.ERASURE is set to YES in CZ.CDP.PARAMETER. |
| 8 | `CZ.CDP.RESERVED.19` | `CzCdpPurpose_Reserved19` | TField |  |  |
| 9 | `CZ.CDP.RESERVED.18` | `CzCdpPurpose_Reserved18` | TField |  |  |
| 10 | `CZ.CDP.RESERVED.17` | `CzCdpPurpose_Reserved17` | TField |  |  |
| 11 | `CZ.CDP.RESERVED.16` | `CzCdpPurpose_Reserved16` | TField |  |  |
| 12 | `CZ.CDP.RESERVED.15` | `CzCdpPurpose_Reserved15` | TField |  |  |
| 13 | `CZ.CDP.RESERVED.14` | `CzCdpPurpose_Reserved14` | TField |  |  |
| 14 | `CZ.CDP.RESERVED.13` | `CzCdpPurpose_Reserved13` | TField |  |  |
| 15 | `CZ.CDP.RESERVED.12` | `CzCdpPurpose_Reserved12` | TField |  |  |
| 16 | `CZ.CDP.RESERVED.11` | `CzCdpPurpose_Reserved11` | TField |  |  |
| 17 | `CZ.CDP.RESERVED.10` | `CzCdpPurpose_Reserved10` | TField |  |  |
| 18 | `CZ.CDP.RESERVED.09` | `CzCdpPurpose_Reserved09` | TField |  |  |
| 19 | `CZ.CDP.RESERVED.08` | `CzCdpPurpose_Reserved08` | TField |  |  |
| 20 | `CZ.CDP.RESERVED.07` | `CzCdpPurpose_Reserved07` | TField |  |  |
| 21 | `CZ.CDP.RESERVED.06` | `CzCdpPurpose_Reserved06` | TField |  |  |
| 22 | `CZ.CDP.RESERVED.05` | `CzCdpPurpose_Reserved05` | TField |  |  |
| 23 | `CZ.CDP.RESERVED.04` | `CzCdpPurpose_Reserved04` | TField |  |  |
| 24 | `CZ.CDP.RESERVED.03` | `CzCdpPurpose_Reserved03` | TField |  |  |
| 25 | `CZ.CDP.RESERVED.02` | `CzCdpPurpose_Reserved02` | TField |  |  |
| 26 | `CZ.CDP.LOCAL.REF` | `CzCdpPurpose_LocalRef` |  |  |  |
| 27 | `CZ.CDP.OVERRIDE` | `CzCdpPurpose_Override` |  |  |  |
| 28 | `CZ.CDP.RECORD.STATUS` | `CzCdpPurpose_RecordStatus` | String |  |  |
| 29 | `CZ.CDP.CURR.NO` | `CzCdpPurpose_CurrNo` | String |  |  |
| 30 | `CZ.CDP.INPUTTER` | `CzCdpPurpose_Inputter` |  |  |  |
| 31 | `CZ.CDP.DATE.TIME` | `CzCdpPurpose_DateTime` |  |  |  |
| 32 | `CZ.CDP.AUTHORISER` | `CzCdpPurpose_Authoriser` | String |  |  |
| 33 | `CZ.CDP.CO.CODE` | `CzCdpPurpose_CoCode` | String |  |  |
| 34 | `CZ.CDP.DEPT.CODE` | `CzCdpPurpose_DeptCode` | String |  |  |
| 35 | `CZ.CDP.AUDITOR.CODE` | `CzCdpPurpose_AuditorCode` | String |  |  |
| 36 | `CZ.CDP.AUDIT.DATE.TIME` | `CzCdpPurpose_AuditDateTime` | String |  |  |
