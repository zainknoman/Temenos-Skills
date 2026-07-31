# UKDDMP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.UKDDMP.PARAMETER` in `UKDDMP_Lodgements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UKDDMP.PARAMETER.ALLOWED.PAYMENT.TYPE` | `UkddmpParameter_AllowedPaymentType` |  |  |  |
| 2 | `UKDDMP.PARAMETER.RESERVED.8` | `UkddmpParameter_Reserved8` | TField |  | This field is reserved for future use |
| 3 | `UKDDMP.PARAMETER.RESERVED.7` | `UkddmpParameter_Reserved7` | TField |  | This field is reserved for future use |
| 4 | `UKDDMP.PARAMETER.RESERVED.6` | `UkddmpParameter_Reserved6` | TField |  | This field is reserved for future use |
| 5 | `UKDDMP.PARAMETER.RESERVED.5` | `UkddmpParameter_Reserved5` | TField |  | This field is reserved for future use |
| 6 | `UKDDMP.PARAMETER.RESERVED.4` | `UkddmpParameter_Reserved4` | TField |  | This field is reserved for future use |
| 7 | `UKDDMP.PARAMETER.RESERVED.3` | `UkddmpParameter_Reserved3` | TField |  | This field is reserved for future use |
| 8 | `UKDDMP.PARAMETER.RESERVED.2` | `UkddmpParameter_Reserved2` | TField |  | This field is reserved for future use |
| 9 | `UKDDMP.PARAMETER.RESERVED.1` | `UkddmpParameter_Reserved1` | TField |  | This field is reserved for future use |
| 10 | `UKDDMP.PARAMETER.LOCAL.REF` | `UkddmpParameter_LocalRef` |  |  |  |
| 11 | `UKDDMP.PARAMETER.OVERRIDE` | `UkddmpParameter_Override` |  |  |  |
| 12 | `UKDDMP.PARAMETER.RECORD.STATUS` | `UkddmpParameter_RecordStatus` | String |  |  |
| 13 | `UKDDMP.PARAMETER.CURR.NO` | `UkddmpParameter_CurrNo` | String |  |  |
| 14 | `UKDDMP.PARAMETER.INPUTTER` | `UkddmpParameter_Inputter` |  |  |  |
| 15 | `UKDDMP.PARAMETER.DATE.TIME` | `UkddmpParameter_DateTime` |  |  |  |
| 16 | `UKDDMP.PARAMETER.AUTHORISER` | `UkddmpParameter_Authoriser` | String |  |  |
| 17 | `UKDDMP.PARAMETER.CO.CODE` | `UkddmpParameter_CoCode` | String |  |  |
| 18 | `UKDDMP.PARAMETER.DEPT.CODE` | `UkddmpParameter_DeptCode` | String |  |  |
| 19 | `UKDDMP.PARAMETER.AUDITOR.CODE` | `UkddmpParameter_AuditorCode` | String |  |  |
| 20 | `UKDDMP.PARAMETER.AUDIT.DATE.TIME` | `UkddmpParameter_AuditDateTime` | String |  |  |
