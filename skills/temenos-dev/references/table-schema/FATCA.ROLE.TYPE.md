# FATCA.ROLE.TYPE — Table Schema

> Source: `INSERTS/I_F.FATCA.ROLE.TYPE` in `FA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.RT.JOINT.ROLES` | `FatcaRoleType_JointRoles` |  |  |  |
| 2 | `FA.RT.BENEFICIAL.ROLES` | `FatcaRoleType_BeneficialRoles` |  |  |  |
| 3 | `FA.RT.SUBSTANTIAL.ROLES` | `FatcaRoleType_SubstantialRoles` |  |  |  |
| 4 | `FA.RT.RESERVED.10` | `FatcaRoleType_Reserved10` | TField |  |  |
| 5 | `FA.RT.RESERVED.9` | `FatcaRoleType_Reserved9` | TField |  |  |
| 6 | `FA.RT.RESERVED.8` | `FatcaRoleType_Reserved8` | TField |  |  |
| 7 | `FA.RT.RESERVED.7` | `FatcaRoleType_Reserved7` | TField |  |  |
| 8 | `FA.RT.RESERVED.6` | `FatcaRoleType_Reserved6` | TField |  |  |
| 9 | `FA.RT.RESERVED.5` | `FatcaRoleType_Reserved5` | TField |  |  |
| 10 | `FA.RT.RESERVED.4` | `FatcaRoleType_Reserved4` | TField |  |  |
| 11 | `FA.RT.RESERVED.3` | `FatcaRoleType_Reserved3` | TField |  |  |
| 12 | `FA.RT.RESERVED.2` | `FatcaRoleType_Reserved2` | TField |  |  |
| 13 | `FA.RT.RESERVED.1` | `FatcaRoleType_Reserved1` | TField |  |  |
| 14 | `FA.RT.LOCAL.REF` | `FatcaRoleType_LocalRef` |  |  |  |
| 15 | `FA.RT.OVERRIDE` | `FatcaRoleType_Override` |  |  |  |
| 16 | `FA.RT.RECORD.STATUS` | `FatcaRoleType_RecordStatus` | String |  |  |
| 17 | `FA.RT.CURR.NO` | `FatcaRoleType_CurrNo` | String |  |  |
| 18 | `FA.RT.INPUTTER` | `FatcaRoleType_Inputter` |  |  |  |
| 19 | `FA.RT.DATE.TIME` | `FatcaRoleType_DateTime` |  |  |  |
| 20 | `FA.RT.AUTHORISER` | `FatcaRoleType_Authoriser` | String |  |  |
| 21 | `FA.RT.CO.CODE` | `FatcaRoleType_CoCode` | String |  |  |
| 22 | `FA.RT.DEPT.CODE` | `FatcaRoleType_DeptCode` | String |  |  |
| 23 | `FA.RT.AUDITOR.CODE` | `FatcaRoleType_AuditorCode` | String |  |  |
| 24 | `FA.RT.AUDIT.DATE.TIME` | `FatcaRoleType_AuditDateTime` | String |  |  |
