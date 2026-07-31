# FS.GI.APP.KIID.COMPLIANCE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.KIID.COMPLIANCE` in `FS_Regulatory.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.KIID.COMPLIANCE.PARENT.REF.ID` | `FsGiAppKiidCompliance_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.KIID.COMPLIANCE.ORA.ROWID` | `FsGiAppKiidCompliance_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.KIID.COMPLIANCE.PARENT.ID.TYPE` | `FsGiAppKiidCompliance_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.APP.KIID.COMPLIANCE.LEGAL.ENTITY.ID` | `FsGiAppKiidCompliance_LegalEntityId` | TField |  | Legal Entity internal ID. Multifonds DB Column is NTFC. |
| 5 | `FS.GI.APP.KIID.COMPLIANCE.OPERATION.CODE` | `FsGiAppKiidCompliance_OperationCode` | TField |  | Operation code in scope for KIID compliance check. Multifonds DB Column is COPERATION. |
| 6 | `FS.GI.APP.KIID.COMPLIANCE.KIID.FLAG` | `FsGiAppKiidCompliance_KiidFlag` | TField |  | Flag to enable the operation code in scope of KIID check. Multifonds DB Column is FLG_KIID. |
| 7 | `FS.GI.APP.KIID.COMPLIANCE.KIID.FIRST.TXN.FLAG` | `FsGiAppKiidCompliance_KiidFirstTxnFlag` | TField |  | Flag to enable the operation code in scope of KIID check for first transaction only. Multifonds DB Column is FST_TRNS_FLG. |
| 8 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED10` | `FsGiAppKiidCompliance_Reserved10` | TField |  |  |
| 9 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED9` | `FsGiAppKiidCompliance_Reserved9` | TField |  |  |
| 10 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED8` | `FsGiAppKiidCompliance_Reserved8` | TField |  |  |
| 11 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED7` | `FsGiAppKiidCompliance_Reserved7` | TField |  |  |
| 12 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED6` | `FsGiAppKiidCompliance_Reserved6` | TField |  |  |
| 13 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED5` | `FsGiAppKiidCompliance_Reserved5` | TField |  |  |
| 14 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED4` | `FsGiAppKiidCompliance_Reserved4` | TField |  |  |
| 15 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED3` | `FsGiAppKiidCompliance_Reserved3` | TField |  |  |
| 16 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED2` | `FsGiAppKiidCompliance_Reserved2` | TField |  |  |
| 17 | `FS.GI.APP.KIID.COMPLIANCE.RESERVED1` | `FsGiAppKiidCompliance_Reserved1` | TField |  |  |
| 18 | `FS.GI.APP.KIID.COMPLIANCE.LOCAL.REF` | `FsGiAppKiidCompliance_LocalRef` |  |  |  |
| 19 | `FS.GI.APP.KIID.COMPLIANCE.OVERRIDE` | `FsGiAppKiidCompliance_Override` |  |  |  |
| 20 | `FS.GI.APP.KIID.COMPLIANCE.RECORD.STATUS` | `FsGiAppKiidCompliance_RecordStatus` | String |  |  |
| 21 | `FS.GI.APP.KIID.COMPLIANCE.CURR.NO` | `FsGiAppKiidCompliance_CurrNo` | String |  |  |
| 22 | `FS.GI.APP.KIID.COMPLIANCE.INPUTTER` | `FsGiAppKiidCompliance_Inputter` |  |  |  |
| 23 | `FS.GI.APP.KIID.COMPLIANCE.DATE.TIME` | `FsGiAppKiidCompliance_DateTime` |  |  |  |
| 24 | `FS.GI.APP.KIID.COMPLIANCE.AUTHORISER` | `FsGiAppKiidCompliance_Authoriser` | String |  |  |
| 25 | `FS.GI.APP.KIID.COMPLIANCE.CO.CODE` | `FsGiAppKiidCompliance_CoCode` | String |  |  |
| 26 | `FS.GI.APP.KIID.COMPLIANCE.DEPT.CODE` | `FsGiAppKiidCompliance_DeptCode` | String |  |  |
| 27 | `FS.GI.APP.KIID.COMPLIANCE.AUDITOR.CODE` | `FsGiAppKiidCompliance_AuditorCode` | String |  |  |
| 28 | `FS.GI.APP.KIID.COMPLIANCE.AUDIT.DATE.TIME` | `FsGiAppKiidCompliance_AuditDateTime` | String |  |  |
