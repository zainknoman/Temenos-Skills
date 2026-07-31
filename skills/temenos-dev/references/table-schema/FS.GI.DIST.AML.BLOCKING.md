# FS.GI.DIST.AML.BLOCKING — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AML.BLOCKING` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AML.BLOCKING.PARENT.REF.ID` | `FsGiDistAmlBlocking_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AML.BLOCKING.ORA.ROWID` | `FsGiDistAmlBlocking_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AML.BLOCKING.PARENT.ID.TYPE` | `FsGiDistAmlBlocking_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.AML.BLOCKING.PARENT.ID` | `FsGiDistAmlBlocking_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.CODE` | `FsGiDistAmlBlocking_AmlBlockingCode` | TField |  | The AML blocking code applied on the entity for AML reason. Multifonds DB Column is BLOCK_CODE. |
| 6 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON1` | `FsGiDistAmlBlocking_AmlBlockingReason1` | TField |  | AML blocking reason code 1. Multifonds DB Column is REASON_CODE1. |
| 7 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON2` | `FsGiDistAmlBlocking_AmlBlockingReason2` | TField |  | AML blocking reason code 2. Multifonds DB Column is REASON_CODE2. |
| 8 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON3` | `FsGiDistAmlBlocking_AmlBlockingReason3` | TField |  | AML blocking reason code 3. Multifonds DB Column is REASON_CODE3. |
| 9 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON4` | `FsGiDistAmlBlocking_AmlBlockingReason4` | TField |  | AML blocking reason code 4. Multifonds DB Column is REASON_CODE4. |
| 10 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON5` | `FsGiDistAmlBlocking_AmlBlockingReason5` | TField |  | AML blocking reason code 5. Multifonds DB Column is REASON_CODE5. |
| 11 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON6` | `FsGiDistAmlBlocking_AmlBlockingReason6` | TField |  | AML blocking reason code 6. Multifonds DB Column is REASON_CODE6. |
| 12 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON7` | `FsGiDistAmlBlocking_AmlBlockingReason7` | TField |  | AML blocking reason code 7. Multifonds DB Column is REASON_CODE7. |
| 13 | `FS.GI.DIST.AML.BLOCKING.AML.BLOCKING.REASON8` | `FsGiDistAmlBlocking_AmlBlockingReason8` | TField |  | AML blocking reason code 8. Multifonds DB Column is REASON_CODE8. |
| 14 | `FS.GI.DIST.AML.BLOCKING.BLOCKING.INTERNAL.ID` | `FsGiDistAmlBlocking_BlockingInternalId` | TField |  | Unique internal AML Blocking identifier. Multifonds DB Column is INTERNAL_ID. |
| 15 | `FS.GI.DIST.AML.BLOCKING.RESERVED10` | `FsGiDistAmlBlocking_Reserved10` | TField |  |  |
| 16 | `FS.GI.DIST.AML.BLOCKING.RESERVED9` | `FsGiDistAmlBlocking_Reserved9` | TField |  |  |
| 17 | `FS.GI.DIST.AML.BLOCKING.RESERVED8` | `FsGiDistAmlBlocking_Reserved8` | TField |  |  |
| 18 | `FS.GI.DIST.AML.BLOCKING.RESERVED7` | `FsGiDistAmlBlocking_Reserved7` | TField |  |  |
| 19 | `FS.GI.DIST.AML.BLOCKING.RESERVED6` | `FsGiDistAmlBlocking_Reserved6` | TField |  |  |
| 20 | `FS.GI.DIST.AML.BLOCKING.RESERVED5` | `FsGiDistAmlBlocking_Reserved5` | TField |  |  |
| 21 | `FS.GI.DIST.AML.BLOCKING.RESERVED4` | `FsGiDistAmlBlocking_Reserved4` | TField |  |  |
| 22 | `FS.GI.DIST.AML.BLOCKING.RESERVED3` | `FsGiDistAmlBlocking_Reserved3` | TField |  |  |
| 23 | `FS.GI.DIST.AML.BLOCKING.RESERVED2` | `FsGiDistAmlBlocking_Reserved2` | TField |  |  |
| 24 | `FS.GI.DIST.AML.BLOCKING.RESERVED1` | `FsGiDistAmlBlocking_Reserved1` | TField |  |  |
| 25 | `FS.GI.DIST.AML.BLOCKING.LOCAL.REF` | `FsGiDistAmlBlocking_LocalRef` |  |  |  |
| 26 | `FS.GI.DIST.AML.BLOCKING.OVERRIDE` | `FsGiDistAmlBlocking_Override` |  |  |  |
| 27 | `FS.GI.DIST.AML.BLOCKING.RECORD.STATUS` | `FsGiDistAmlBlocking_RecordStatus` | String |  |  |
| 28 | `FS.GI.DIST.AML.BLOCKING.CURR.NO` | `FsGiDistAmlBlocking_CurrNo` | String |  |  |
| 29 | `FS.GI.DIST.AML.BLOCKING.INPUTTER` | `FsGiDistAmlBlocking_Inputter` |  |  |  |
| 30 | `FS.GI.DIST.AML.BLOCKING.DATE.TIME` | `FsGiDistAmlBlocking_DateTime` |  |  |  |
| 31 | `FS.GI.DIST.AML.BLOCKING.AUTHORISER` | `FsGiDistAmlBlocking_Authoriser` | String |  |  |
| 32 | `FS.GI.DIST.AML.BLOCKING.CO.CODE` | `FsGiDistAmlBlocking_CoCode` | String |  |  |
| 33 | `FS.GI.DIST.AML.BLOCKING.DEPT.CODE` | `FsGiDistAmlBlocking_DeptCode` | String |  |  |
| 34 | `FS.GI.DIST.AML.BLOCKING.AUDITOR.CODE` | `FsGiDistAmlBlocking_AuditorCode` | String |  |  |
| 35 | `FS.GI.DIST.AML.BLOCKING.AUDIT.DATE.TIME` | `FsGiDistAmlBlocking_AuditDateTime` | String |  |  |
