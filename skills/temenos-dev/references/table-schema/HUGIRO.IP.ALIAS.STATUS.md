# HUGIRO.IP.ALIAS.STATUS — Table Schema

> Source: `INSERTS/I_F.HUGIRO.IP.ALIAS.STATUS` in `HUGIRO_Lookup.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ALIAS.STATUS.PENDING.REGISTRATION` | `HugiroIpAliasStatus_PendingRegistration` | TField |  | Dropdown field. Valid values defined in ST.PROXY.STATUS table. |
| 2 | `ALIAS.STATUS.PENDING.DELETE` | `HugiroIpAliasStatus_PendingDelete` | TField |  | Dropdown field. Valid values defined in ST.PROXY.STATUS table. |
| 3 | `ALIAS.STATUS.PENDING.DEL.FOR.REGISTRATION` | `HugiroIpAliasStatus_PendingDelForRegistration` | TField |  |  |
| 4 | `ALIAS.STATUS.LOCAL.REF` | `HugiroIpAliasStatus_LocalRef` |  |  |  |
| 5 | `ALIAS.STATUS.RESERVED.5` | `HugiroIpAliasStatus_Reserved5` | TField |  |  |
| 6 | `ALIAS.STATUS.RESERVED.4` | `HugiroIpAliasStatus_Reserved4` | TField |  |  |
| 7 | `ALIAS.STATUS.RESERVED.3` | `HugiroIpAliasStatus_Reserved3` | TField |  |  |
| 8 | `ALIAS.STATUS.RESERVED.2` | `HugiroIpAliasStatus_Reserved2` | TField |  |  |
| 9 | `ALIAS.STATUS.RESERVED.1` | `HugiroIpAliasStatus_Reserved1` | TField |  |  |
| 10 | `ALIAS.STATUS.OVERRIDE` | `HugiroIpAliasStatus_Override` |  |  |  |
| 11 | `ALIAS.STATUS.RECORD.STATUS` | `HugiroIpAliasStatus_RecordStatus` | String |  |  |
| 12 | `ALIAS.STATUS.CURR.NO` | `HugiroIpAliasStatus_CurrNo` | String |  |  |
| 13 | `ALIAS.STATUS.INPUTTER` | `HugiroIpAliasStatus_Inputter` |  |  |  |
| 14 | `ALIAS.STATUS.DATE.TIME` | `HugiroIpAliasStatus_DateTime` |  |  |  |
| 15 | `ALIAS.STATUS.AUTHORISER` | `HugiroIpAliasStatus_Authoriser` | String |  |  |
| 16 | `ALIAS.STATUS.CO.CODE` | `HugiroIpAliasStatus_CoCode` | String |  |  |
| 17 | `ALIAS.STATUS.DEPT.CODE` | `HugiroIpAliasStatus_DeptCode` | String |  |  |
| 18 | `ALIAS.STATUS.AUDITOR.CODE` | `HugiroIpAliasStatus_AuditorCode` | String |  |  |
| 19 | `ALIAS.STATUS.AUDIT.DATE.TIME` | `HugiroIpAliasStatus_AuditDateTime` | String |  |  |
