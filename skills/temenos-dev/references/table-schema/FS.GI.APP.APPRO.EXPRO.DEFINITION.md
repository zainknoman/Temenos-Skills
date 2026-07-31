# FS.GI.APP.APPRO.EXPRO.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.APPRO.EXPRO.DEFINITION` in `FS_FundLegalEntity.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.PARENT.REF.ID` | `FsGiAppApproExproDefinition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.ORA.ROWID` | `FsGiAppApproExproDefinition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.PARENT.ID.TYPE` | `FsGiAppApproExproDefinition_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Limited to two entity types 0003 TFC and 0008 Fund Promoter. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.PARENT.ID` | `FsGiAppApproExproDefinition_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.PAYMENT.TYPE` | `FsGiAppApproExproDefinition_PaymentType` | TField |  | Payment Type of the payment instruction. The available lookup details are Appro Payment Type (Internal Fund Movement) and Expro Payment Type (External Fund Movement). Multifonds DB Column is PAY_TYPE. |
| 6 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.OPERATION.CODE` | `FsGiAppApproExproDefinition_OperationCode` | TField |  | Operation code in scope of Appro and Expro payment type paramaterization. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.APPRO.EXPRO.ID` | `FsGiAppApproExproDefinition_ApproExproId` | TField |  | Unique internal identifier for appro expro payment type definition record. Multifonds DB Column is INTERNAL_ID. |
| 8 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED10` | `FsGiAppApproExproDefinition_Reserved10` | TField |  |  |
| 9 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED9` | `FsGiAppApproExproDefinition_Reserved9` | TField |  |  |
| 10 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED8` | `FsGiAppApproExproDefinition_Reserved8` | TField |  |  |
| 11 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED7` | `FsGiAppApproExproDefinition_Reserved7` | TField |  |  |
| 12 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED6` | `FsGiAppApproExproDefinition_Reserved6` | TField |  |  |
| 13 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED5` | `FsGiAppApproExproDefinition_Reserved5` | TField |  |  |
| 14 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED4` | `FsGiAppApproExproDefinition_Reserved4` | TField |  |  |
| 15 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED3` | `FsGiAppApproExproDefinition_Reserved3` | TField |  |  |
| 16 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED2` | `FsGiAppApproExproDefinition_Reserved2` | TField |  |  |
| 17 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RESERVED1` | `FsGiAppApproExproDefinition_Reserved1` | TField |  |  |
| 18 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.LOCAL.REF` | `FsGiAppApproExproDefinition_LocalRef` |  |  |  |
| 19 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.OVERRIDE` | `FsGiAppApproExproDefinition_Override` |  |  |  |
| 20 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.RECORD.STATUS` | `FsGiAppApproExproDefinition_RecordStatus` | String |  |  |
| 21 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.CURR.NO` | `FsGiAppApproExproDefinition_CurrNo` | String |  |  |
| 22 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.INPUTTER` | `FsGiAppApproExproDefinition_Inputter` |  |  |  |
| 23 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.DATE.TIME` | `FsGiAppApproExproDefinition_DateTime` |  |  |  |
| 24 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.AUTHORISER` | `FsGiAppApproExproDefinition_Authoriser` | String |  |  |
| 25 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.CO.CODE` | `FsGiAppApproExproDefinition_CoCode` | String |  |  |
| 26 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.DEPT.CODE` | `FsGiAppApproExproDefinition_DeptCode` | String |  |  |
| 27 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.AUDITOR.CODE` | `FsGiAppApproExproDefinition_AuditorCode` | String |  |  |
| 28 | `FS.GI.APP.APPRO.EXPRO.DEFINITION.AUDIT.DATE.TIME` | `FsGiAppApproExproDefinition_AuditDateTime` | String |  |  |
