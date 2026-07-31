# LKIFRS.STAGING.CRITERIA — Table Schema

> Source: `INSERTS/I_F.LKIFRS.STAGING.CRITERIA` in `LKIFRS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKIFRS.STAG.DESCRIPTION` | `LkifrsStagingCriteria_Description` | TField |  | Refers to the description of the product. |
| 2 | `LKIFRS.STAG.CRITERIA` | `LkifrsStagingCriteria_Criteria` |  |  |  |
| 3 | `LKIFRS.STAG.OPERAND` | `LkifrsStagingCriteria_Operand` |  |  |  |
| 4 | `LKIFRS.STAG.CRITERIA.VALUE.START` | `LkifrsStagingCriteria_CriteriaValueStart` |  |  |  |
| 5 | `LKIFRS.STAG.CRITERIA.VALUE.END` | `LkifrsStagingCriteria_CriteriaValueEnd` |  |  |  |
| 6 | `LKIFRS.STAG.RESERVED.1` | `LkifrsStagingCriteria_Reserved1` | TField |  | Reserved for future use. |
| 7 | `LKIFRS.STAG.RESERVED.2` | `LkifrsStagingCriteria_Reserved2` | TField |  | Reserved for future use. |
| 8 | `LKIFRS.STAG.RESERVED.3` | `LkifrsStagingCriteria_Reserved3` | TField |  | Reserved for future use. |
| 9 | `LKIFRS.STAG.RESERVED.4` | `LkifrsStagingCriteria_Reserved4` | TField |  | Reserved for future use. |
| 10 | `LKIFRS.STAG.RESERVED.5` | `LkifrsStagingCriteria_Reserved5` | TField |  | Reserved for future use. |
| 11 | `LKIFRS.STAG.RESERVED.6` | `LkifrsStagingCriteria_Reserved6` | TField |  | Reserved for future use. |
| 12 | `LKIFRS.STAG.RESERVED.7` | `LkifrsStagingCriteria_Reserved7` | TField |  | Reserved for future use. |
| 13 | `LKIFRS.STAG.RESERVED.8` | `LkifrsStagingCriteria_Reserved8` | TField |  | Reserved for future use. |
| 14 | `LKIFRS.STAG.LOCAL.REF` | `LkifrsStagingCriteria_LocalRef` |  |  |  |
| 15 | `LKIFRS.STAG.OVERRIDE` | `LkifrsStagingCriteria_Override` |  |  |  |
| 16 | `LKIFRS.STAG.RECORD.STATUS` | `LkifrsStagingCriteria_RecordStatus` | String |  |  |
| 17 | `LKIFRS.STAG.CURR.NO` | `LkifrsStagingCriteria_CurrNo` | String |  |  |
| 18 | `LKIFRS.STAG.INPUTTER` | `LkifrsStagingCriteria_Inputter` |  |  |  |
| 19 | `LKIFRS.STAG.DATE.TIME` | `LkifrsStagingCriteria_DateTime` |  |  |  |
| 20 | `LKIFRS.STAG.AUTHORISER` | `LkifrsStagingCriteria_Authoriser` | String |  |  |
| 21 | `LKIFRS.STAG.CO.CODE` | `LkifrsStagingCriteria_CoCode` | String |  |  |
| 22 | `LKIFRS.STAG.DEPT.CODE` | `LkifrsStagingCriteria_DeptCode` | String |  |  |
| 23 | `LKIFRS.STAG.AUDITOR.CODE` | `LkifrsStagingCriteria_AuditorCode` | String |  |  |
| 24 | `LKIFRS.STAG.AUDIT.DATE.TIME` | `LkifrsStagingCriteria_AuditDateTime` | String |  |  |
