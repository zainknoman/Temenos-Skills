# LI.MULTI.CUSTOMER.LIMIT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LI.MULTI.CUSTOMER.LIMIT.PARAMETER` in `LI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MCLP.DEF.JOINT.OR.MULTI` | `LiMultiCustomerLimitParameter_DefJointOrMulti` |  |  |  |
| 2 | `MCLP.DEF.RISK.GROUP.MAND` | `LiMultiCustomerLimitParameter_DefRiskGroupMand` |  |  |  |
| 3 | `MCLP.DEF.ALLOW.MULT.GROUP` | `LiMultiCustomerLimitParameter_DefAllowMultGroup` |  |  |  |
| 4 | `MCLP.RESERVED.10` | `LiMultiCustomerLimitParameter_Reserved10` | TField |  |  |
| 5 | `MCLP.RESERVED.9` | `LiMultiCustomerLimitParameter_Reserved9` | TField |  |  |
| 6 | `MCLP.RESERVED.8` | `LiMultiCustomerLimitParameter_Reserved8` | TField |  |  |
| 7 | `MCLP.RESERVED.7` | `LiMultiCustomerLimitParameter_Reserved7` | TField |  |  |
| 8 | `MCLP.RESERVED.6` | `LiMultiCustomerLimitParameter_Reserved6` | TField |  |  |
| 9 | `MCLP.SECTOR.START` | `LiMultiCustomerLimitParameter_SectorStart` |  |  |  |
| 10 | `MCLP.SECTOR.END` | `LiMultiCustomerLimitParameter_SectorEnd` |  |  |  |
| 11 | `MCLP.JOINT.OR.MULTI` | `LiMultiCustomerLimitParameter_JointOrMulti` |  |  |  |
| 12 | `MCLP.RISK.GROUP.MAND` | `LiMultiCustomerLimitParameter_RiskGroupMand` |  |  |  |
| 13 | `MCLP.ALLOW.MULT.GROUP` | `LiMultiCustomerLimitParameter_AllowMultGroup` |  |  |  |
| 14 | `MCLP.RESERVED.5` | `LiMultiCustomerLimitParameter_Reserved5` | TField |  |  |
| 15 | `MCLP.RESERVED.4` | `LiMultiCustomerLimitParameter_Reserved4` | TField |  |  |
| 16 | `MCLP.RESERVED.3` | `LiMultiCustomerLimitParameter_Reserved3` | TField |  |  |
| 17 | `MCLP.RESERVED.2` | `LiMultiCustomerLimitParameter_Reserved2` | TField |  |  |
| 18 | `MCLP.RESERVED.1` | `LiMultiCustomerLimitParameter_Reserved1` | TField |  |  |
| 19 | `MCLP.LOCAL.REF` | `LiMultiCustomerLimitParameter_LocalRef` |  |  |  |
| 20 | `MCLP.OVERRIDE` | `LiMultiCustomerLimitParameter_Override` |  |  |  |
| 21 | `MCLP.RECORD.STATUS` | `LiMultiCustomerLimitParameter_RecordStatus` | String |  |  |
| 22 | `MCLP.CURR.NO` | `LiMultiCustomerLimitParameter_CurrNo` | String |  |  |
| 23 | `MCLP.INPUTTER` | `LiMultiCustomerLimitParameter_Inputter` |  |  |  |
| 24 | `MCLP.DATE.TIME` | `LiMultiCustomerLimitParameter_DateTime` |  |  |  |
| 25 | `MCLP.AUTHORISER` | `LiMultiCustomerLimitParameter_Authoriser` | String |  |  |
| 26 | `MCLP.CO.CODE` | `LiMultiCustomerLimitParameter_CoCode` | String |  |  |
| 27 | `MCLP.DEPT.CODE` | `LiMultiCustomerLimitParameter_DeptCode` | String |  |  |
| 28 | `MCLP.AUDITOR.CODE` | `LiMultiCustomerLimitParameter_AuditorCode` | String |  |  |
| 29 | `MCLP.AUDIT.DATE.TIME` | `LiMultiCustomerLimitParameter_AuditDateTime` | String |  |  |
