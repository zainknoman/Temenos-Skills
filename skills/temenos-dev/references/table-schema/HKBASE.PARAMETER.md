# HKBASE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.HKBASE.PARAMETER` in `HKBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HKBASE.PARAMETER.RELATION.ID` | `HkbaseParameter_RelationId` |  |  |  |
| 2 | `HKBASE.PARAMETER.LOCAL.REF` | `HkbaseParameter_LocalRef` |  |  |  |
| 3 | `HKBASE.PARAMETER.AEOI.ID` | `HkbaseParameter_AeoiId` | TField |  | Refers to AEOI id for the reporting entity. |
| 4 | `HKBASE.PARAMETER.USER.ROLE` | `HkbaseParameter_UserRole` |  |  |  |
| 5 | `HKBASE.PARAMETER.RESERVED.3` | `HkbaseParameter_Reserved3` |  |  |  |
| 6 | `HKBASE.PARAMETER.RESERVED.4` | `HkbaseParameter_Reserved4` | TField |  | Reserved for future purpose. |
| 7 | `HKBASE.PARAMETER.RESERVED.5` | `HkbaseParameter_Reserved5` | TField |  | Reserved for future purpose. |
| 8 | `HKBASE.PARAMETER.RESERVED.6` | `HkbaseParameter_Reserved6` | TField |  | Reserved for future purpose. |
| 9 | `HKBASE.PARAMETER.RESERVED.7` | `HkbaseParameter_Reserved7` | TField |  | Reserved for future purpose. |
| 10 | `HKBASE.PARAMETER.RESERVED.8` | `HkbaseParameter_Reserved8` | TField |  | Reserved for future purpose. |
| 11 | `HKBASE.PARAMETER.RESERVED.9` | `HkbaseParameter_Reserved9` | TField |  | Reserved for future purpose. |
| 12 | `HKBASE.PARAMETER.RESERVED.10` | `HkbaseParameter_Reserved10` | TField |  | Reserved for future purpose. |
| 13 | `HKBASE.PARAMETER.OVERRIDE` | `HkbaseParameter_Override` |  |  |  |
| 14 | `HKBASE.PARAMETER.RECORD.STATUS` | `HkbaseParameter_RecordStatus` | String |  |  |
| 15 | `HKBASE.PARAMETER.CURR.NO` | `HkbaseParameter_CurrNo` | String |  |  |
| 16 | `HKBASE.PARAMETER.INPUTTER` | `HkbaseParameter_Inputter` |  |  |  |
| 17 | `HKBASE.PARAMETER.DATE.TIME` | `HkbaseParameter_DateTime` |  |  |  |
| 18 | `HKBASE.PARAMETER.AUTHORISER` | `HkbaseParameter_Authoriser` | String |  |  |
| 19 | `HKBASE.PARAMETER.CO.CODE` | `HkbaseParameter_CoCode` | String |  |  |
| 20 | `HKBASE.PARAMETER.DEPT.CODE` | `HkbaseParameter_DeptCode` | String |  |  |
| 21 | `HKBASE.PARAMETER.AUDITOR.CODE` | `HkbaseParameter_AuditorCode` | String |  |  |
| 22 | `HKBASE.PARAMETER.AUDIT.DATE.TIME` | `HkbaseParameter_AuditDateTime` | String |  |  |
