# SAWATQ.AUTHORISED.USERS — Table Schema

> Source: `INSERTS/I_F.SAWATQ.AUTHORISED.USERS` in `SAWATQ_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUTH.USR.PRODUCT` | `SawatqAuthorisedUsers_Product` |  |  |  |
| 2 | `AUTH.USR.PRODUCT.REFERENCE` | `SawatqAuthorisedUsers_ProductReference` |  |  |  |
| 3 | `AUTH.USR.ROLE` | `SawatqAuthorisedUsers_Role` |  |  |  |
| 4 | `AUTH.USR.LOCAL.REF` | `SawatqAuthorisedUsers_LocalRef` |  |  |  |
| 5 | `AUTH.USR.OVERRIDE` | `SawatqAuthorisedUsers_Override` |  |  |  |
| 6 | `AUTH.USR.RESERVED.1` | `SawatqAuthorisedUsers_Reserved1` | TField |  | Reserved For Future Use |
| 7 | `AUTH.USR.RESERVED.2` | `SawatqAuthorisedUsers_Reserved2` | TField |  | Reserved For Future Use |
| 8 | `AUTH.USR.RESERVED.3` | `SawatqAuthorisedUsers_Reserved3` | TField |  | Reserved For Future Use |
| 9 | `AUTH.USR.RESERVED.4` | `SawatqAuthorisedUsers_Reserved4` | TField |  | Reserved For Future Use |
| 10 | `AUTH.USR.RESERVED.5` | `SawatqAuthorisedUsers_Reserved5` | TField |  | Reserved For Future Use |
| 11 | `AUTH.USR.RESERVED.6` | `SawatqAuthorisedUsers_Reserved6` | TField |  | Reserved For Future Use |
| 12 | `AUTH.USR.RESERVED.7` | `SawatqAuthorisedUsers_Reserved7` | TField |  | Reserved For Future Use |
| 13 | `AUTH.USR.RESERVED.8` | `SawatqAuthorisedUsers_Reserved8` | TField |  | Reserved For Future Use |
| 14 | `AUTH.USR.RESERVED.9` | `SawatqAuthorisedUsers_Reserved9` | TField |  | Reserved For Future Use |
| 15 | `AUTH.USR.RESERVED.10` | `SawatqAuthorisedUsers_Reserved10` | TField |  | Reserved For Future Use |
| 16 | `AUTH.USR.RECORD.STATUS` | `SawatqAuthorisedUsers_RecordStatus` | String |  |  |
| 17 | `AUTH.USR.CURR.NO` | `SawatqAuthorisedUsers_CurrNo` | String |  |  |
| 18 | `AUTH.USR.INPUTTER` | `SawatqAuthorisedUsers_Inputter` |  |  |  |
| 19 | `AUTH.USR.DATE.TIME` | `SawatqAuthorisedUsers_DateTime` |  |  |  |
| 20 | `AUTH.USR.AUTHORISER` | `SawatqAuthorisedUsers_Authoriser` | String |  |  |
| 21 | `AUTH.USR.CO.CODE` | `SawatqAuthorisedUsers_CoCode` | String |  |  |
| 22 | `AUTH.USR.DEPT.CODE` | `SawatqAuthorisedUsers_DeptCode` | String |  |  |
| 23 | `AUTH.USR.AUDITOR.CODE` | `SawatqAuthorisedUsers_AuditorCode` | String |  |  |
| 24 | `AUTH.USR.AUDIT.DATE.TIME` | `SawatqAuthorisedUsers_AuditDateTime` | String |  |  |
