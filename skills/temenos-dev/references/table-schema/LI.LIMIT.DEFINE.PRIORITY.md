# LI.LIMIT.DEFINE.PRIORITY — Table Schema

> Source: `INSERTS/I_F.LI.LIMIT.DEFINE.PRIORITY` in `LI_GroupLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.PR.PRIORITY` | `LiLimitDefinePriority_Priority` |  |  |  |
| 2 | `LI.PR.CUSTOMER.PRIORITY` | `LiLimitDefinePriority_CustomerPriority` | TField |  | Field to define the priority of the customer, Group Limits Utilisation will recalculate based on this Priority. When there is no priority denoted for the customer then default priority will be customers sorted in ascending order. Validations: Any numeric Value up to three digits. |
| 3 | `LI.PR.RESERVED.10` | `LiLimitDefinePriority_Reserved10` | TField |  |  |
| 4 | `LI.PR.RESERVED.9` | `LiLimitDefinePriority_Reserved9` | TField |  |  |
| 5 | `LI.PR.RESERVED.8` | `LiLimitDefinePriority_Reserved8` | TField |  |  |
| 6 | `LI.PR.RESERVED.7` | `LiLimitDefinePriority_Reserved7` | TField |  |  |
| 7 | `LI.PR.RESERVED.6` | `LiLimitDefinePriority_Reserved6` | TField |  |  |
| 8 | `LI.PR.RESERVED.5` | `LiLimitDefinePriority_Reserved5` | TField |  |  |
| 9 | `LI.PR.RESERVED.4` | `LiLimitDefinePriority_Reserved4` | TField |  |  |
| 10 | `LI.PR.RESERVED.3` | `LiLimitDefinePriority_Reserved3` | TField |  |  |
| 11 | `LI.PR.RESERVED.2` | `LiLimitDefinePriority_Reserved2` | TField |  |  |
| 12 | `LI.PR.RESERVED.1` | `LiLimitDefinePriority_Reserved1` | TField |  |  |
| 13 | `LI.PR.LOCAL.REF` | `LiLimitDefinePriority_LocalRef` |  |  |  |
| 14 | `LI.PR.RECORD.STATUS` | `LiLimitDefinePriority_RecordStatus` | String |  |  |
| 15 | `LI.PR.CURR.NO` | `LiLimitDefinePriority_CurrNo` | String |  |  |
| 16 | `LI.PR.INPUTTER` | `LiLimitDefinePriority_Inputter` |  |  |  |
| 17 | `LI.PR.DATE.TIME` | `LiLimitDefinePriority_DateTime` |  |  |  |
| 18 | `LI.PR.AUTHORISER` | `LiLimitDefinePriority_Authoriser` | String |  |  |
| 19 | `LI.PR.CO.CODE` | `LiLimitDefinePriority_CoCode` | String |  |  |
| 20 | `LI.PR.DEPT.CODE` | `LiLimitDefinePriority_DeptCode` | String |  |  |
| 21 | `LI.PR.AUDITOR.CODE` | `LiLimitDefinePriority_AuditorCode` | String |  |  |
| 22 | `LI.PR.AUDIT.DATE.TIME` | `LiLimitDefinePriority_AuditDateTime` | String |  |  |
