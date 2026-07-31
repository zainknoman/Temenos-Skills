# FS.GI.DIST.FATCA.COND.INV — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.FATCA.COND.INV` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.FATCA.COND.INV.PARENT.REF.ID` | `FsGiDistFatcaCondInv_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.FATCA.COND.INV.ORA.ROWID` | `FsGiDistFatcaCondInv_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.FATCA.COND.INV.PARENT.ID.TYPE` | `FsGiDistFatcaCondInv_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.FATCA.COND.INV.PARENT.ID` | `FsGiDistFatcaCondInv_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.FATCA.COND.INV.RULE.CODE` | `FsGiDistFatcaCondInv_RuleCode` | TField |  | FATCA CRS Document definition rule code. Multifonds DB Column is RULE_CODE. |
| 6 | `FS.GI.DIST.FATCA.COND.INV.CONDITION.CODE` | `FsGiDistFatcaCondInv_ConditionCode` | TField |  | FATCA CRS Document definition condition set. Multifonds DB Column is CONDITION_CODE. |
| 7 | `FS.GI.DIST.FATCA.COND.INV.SET.ID1` | `FsGiDistFatcaCondInv_SetId1` | TField |  | First document set link to the rule. Multifonds DB Column is SET_ID1. |
| 8 | `FS.GI.DIST.FATCA.COND.INV.CONDITION1` | `FsGiDistFatcaCondInv_Condition1` | TField |  | FATCA CRS Document definition operation condition 1. Multifonds DB Column is CONDITION1. |
| 9 | `FS.GI.DIST.FATCA.COND.INV.SET.ID2` | `FsGiDistFatcaCondInv_SetId2` | TField |  | Second Document set link to the rule. Multifonds DB Column is SET_ID2. |
| 10 | `FS.GI.DIST.FATCA.COND.INV.CONDITION2` | `FsGiDistFatcaCondInv_Condition2` | TField |  | FATCA CRS Document definition operation condition 2. Multifonds DB Column is CONDITION2. |
| 11 | `FS.GI.DIST.FATCA.COND.INV.SET.ID3` | `FsGiDistFatcaCondInv_SetId3` | TField |  | Third Document set link to the rule. Multifonds DB Column is SET_ID3. |
| 12 | `FS.GI.DIST.FATCA.COND.INV.RESERVED10` | `FsGiDistFatcaCondInv_Reserved10` | TField |  |  |
| 13 | `FS.GI.DIST.FATCA.COND.INV.RESERVED9` | `FsGiDistFatcaCondInv_Reserved9` | TField |  |  |
| 14 | `FS.GI.DIST.FATCA.COND.INV.RESERVED8` | `FsGiDistFatcaCondInv_Reserved8` | TField |  |  |
| 15 | `FS.GI.DIST.FATCA.COND.INV.RESERVED7` | `FsGiDistFatcaCondInv_Reserved7` | TField |  |  |
| 16 | `FS.GI.DIST.FATCA.COND.INV.RESERVED6` | `FsGiDistFatcaCondInv_Reserved6` | TField |  |  |
| 17 | `FS.GI.DIST.FATCA.COND.INV.RESERVED5` | `FsGiDistFatcaCondInv_Reserved5` | TField |  |  |
| 18 | `FS.GI.DIST.FATCA.COND.INV.RESERVED4` | `FsGiDistFatcaCondInv_Reserved4` | TField |  |  |
| 19 | `FS.GI.DIST.FATCA.COND.INV.RESERVED3` | `FsGiDistFatcaCondInv_Reserved3` | TField |  |  |
| 20 | `FS.GI.DIST.FATCA.COND.INV.RESERVED2` | `FsGiDistFatcaCondInv_Reserved2` | TField |  |  |
| 21 | `FS.GI.DIST.FATCA.COND.INV.RESERVED1` | `FsGiDistFatcaCondInv_Reserved1` | TField |  |  |
| 22 | `FS.GI.DIST.FATCA.COND.INV.LOCAL.REF` | `FsGiDistFatcaCondInv_LocalRef` |  |  |  |
| 23 | `FS.GI.DIST.FATCA.COND.INV.OVERRIDE` | `FsGiDistFatcaCondInv_Override` |  |  |  |
| 24 | `FS.GI.DIST.FATCA.COND.INV.RECORD.STATUS` | `FsGiDistFatcaCondInv_RecordStatus` | String |  |  |
| 25 | `FS.GI.DIST.FATCA.COND.INV.CURR.NO` | `FsGiDistFatcaCondInv_CurrNo` | String |  |  |
| 26 | `FS.GI.DIST.FATCA.COND.INV.INPUTTER` | `FsGiDistFatcaCondInv_Inputter` |  |  |  |
| 27 | `FS.GI.DIST.FATCA.COND.INV.DATE.TIME` | `FsGiDistFatcaCondInv_DateTime` |  |  |  |
| 28 | `FS.GI.DIST.FATCA.COND.INV.AUTHORISER` | `FsGiDistFatcaCondInv_Authoriser` | String |  |  |
| 29 | `FS.GI.DIST.FATCA.COND.INV.CO.CODE` | `FsGiDistFatcaCondInv_CoCode` | String |  |  |
| 30 | `FS.GI.DIST.FATCA.COND.INV.DEPT.CODE` | `FsGiDistFatcaCondInv_DeptCode` | String |  |  |
| 31 | `FS.GI.DIST.FATCA.COND.INV.AUDITOR.CODE` | `FsGiDistFatcaCondInv_AuditorCode` | String |  |  |
| 32 | `FS.GI.DIST.FATCA.COND.INV.AUDIT.DATE.TIME` | `FsGiDistFatcaCondInv_AuditDateTime` | String |  |  |
