# FS.GI.DIST.AGENT.ADDRESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AGENT.ADDRESS` in `FS_Address.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AGENT.ADDRESS.PARENT.REF.ID` | `FsGiDistAgentAddress_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AGENT.ADDRESS.ORA.ROWID` | `FsGiDistAgentAddress_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AGENT.ADDRESS.AGENT.ID` | `FsGiDistAgentAddress_AgentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is NOUTLET. |
| 4 | `FS.GI.DIST.AGENT.ADDRESS.SELECTED.FLAG` | `FsGiDistAgentAddress_SelectedFlag` | TField |  | Selection of the main address for the entity. Multifonds DB Column is MAIN_ADR. |
| 5 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.NUMBER` | `FsGiDistAgentAddress_AddressNumber` | TField |  | Sequence number of the address. Multifonds DB Column is CADRESSE. |
| 6 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.LINE1` | `FsGiDistAgentAddress_AddressLine1` | TField |  | Address line 1. Multifonds DB Column is ADRESSE. |
| 7 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.LINE2` | `FsGiDistAgentAddress_AddressLine2` | TField |  | Address line 2. Multifonds DB Column is ADRESSE_LINE2. |
| 8 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.LINE3` | `FsGiDistAgentAddress_AddressLine3` | TField |  | Address line 3. Multifonds DB Column is ADRESSE_LINE3. |
| 9 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.LINE4` | `FsGiDistAgentAddress_AddressLine4` | TField |  | Address line 4. Multifonds DB Column is ADRESSE_LINE4. |
| 10 | `FS.GI.DIST.AGENT.ADDRESS.POSTCODE` | `FsGiDistAgentAddress_Postcode` | TField |  | Post code of the address. Multifonds DB Column is CODE. |
| 11 | `FS.GI.DIST.AGENT.ADDRESS.COUNTRY` | `FsGiDistAgentAddress_Country` | TField |  | Country code (in 2 letter format) of the address. Multifonds DB Column is PAYS. |
| 12 | `FS.GI.DIST.AGENT.ADDRESS.STATE` | `FsGiDistAgentAddress_State` | TField |  | State code of the address. Multifonds DB Column is STATE. |
| 13 | `FS.GI.DIST.AGENT.ADDRESS.PO.BOX` | `FsGiDistAgentAddress_PoBox` | TField |  | PO box number of the address. Multifonds DB Column is ADRESSE_LINE1. |
| 14 | `FS.GI.DIST.AGENT.ADDRESS.PRINT.FLAG` | `FsGiDistAgentAddress_PrintFlag` | TField |  | The address print status. Multifonds DB Column is FLAG_PRINT. |
| 15 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.TYPE` | `FsGiDistAgentAddress_AddressType` | TField |  | Address type code. Multifonds DB Column is ADR_TYPE. |
| 16 | `FS.GI.DIST.AGENT.ADDRESS.CONTACT.PERSON` | `FsGiDistAgentAddress_ContactPerson` | TField |  | Contact person of the address. Multifonds DB Column is CONTACT_PERSON. |
| 17 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.ID` | `FsGiDistAgentAddress_AddressId` | TField |  | Unique internal physical address identifier. Multifonds DB Column is INTERNAL_ID. |
| 18 | `FS.GI.DIST.AGENT.ADDRESS.CHANGE.REASON.CODE` | `FsGiDistAgentAddress_ChangeReasonCode` | TField |  | A code to track the reason why an Account field is updated by a user. Multifonds DB Column is CHG_REASON. |
| 19 | `FS.GI.DIST.AGENT.ADDRESS.CHANGE.REASON.COMMENT` | `FsGiDistAgentAddress_ChangeReasonComment` | TField | No | An optional user supplied description of the reason for the modification of the record. Multifonds DB Column is CHG_COMMENT. |
| 20 | `FS.GI.DIST.AGENT.ADDRESS.ADDRESS.EXTERNAL.REF` | `FsGiDistAgentAddress_AddressExternalRef` | TField |  | Address external reference. Multifonds DB Column is ADR_EXT_REF. |
| 21 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED10` | `FsGiDistAgentAddress_Reserved10` | TField |  |  |
| 22 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED9` | `FsGiDistAgentAddress_Reserved9` | TField |  |  |
| 23 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED8` | `FsGiDistAgentAddress_Reserved8` | TField |  |  |
| 24 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED7` | `FsGiDistAgentAddress_Reserved7` | TField |  |  |
| 25 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED6` | `FsGiDistAgentAddress_Reserved6` | TField |  |  |
| 26 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED5` | `FsGiDistAgentAddress_Reserved5` | TField |  |  |
| 27 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED4` | `FsGiDistAgentAddress_Reserved4` | TField |  |  |
| 28 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED3` | `FsGiDistAgentAddress_Reserved3` | TField |  |  |
| 29 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED2` | `FsGiDistAgentAddress_Reserved2` | TField |  |  |
| 30 | `FS.GI.DIST.AGENT.ADDRESS.RESERVED1` | `FsGiDistAgentAddress_Reserved1` | TField |  |  |
| 31 | `FS.GI.DIST.AGENT.ADDRESS.LOCAL.REF` | `FsGiDistAgentAddress_LocalRef` |  |  |  |
| 32 | `FS.GI.DIST.AGENT.ADDRESS.OVERRIDE` | `FsGiDistAgentAddress_Override` |  |  |  |
| 33 | `FS.GI.DIST.AGENT.ADDRESS.RECORD.STATUS` | `FsGiDistAgentAddress_RecordStatus` | String |  |  |
| 34 | `FS.GI.DIST.AGENT.ADDRESS.CURR.NO` | `FsGiDistAgentAddress_CurrNo` | String |  |  |
| 35 | `FS.GI.DIST.AGENT.ADDRESS.INPUTTER` | `FsGiDistAgentAddress_Inputter` |  |  |  |
| 36 | `FS.GI.DIST.AGENT.ADDRESS.DATE.TIME` | `FsGiDistAgentAddress_DateTime` |  |  |  |
| 37 | `FS.GI.DIST.AGENT.ADDRESS.AUTHORISER` | `FsGiDistAgentAddress_Authoriser` | String |  |  |
| 38 | `FS.GI.DIST.AGENT.ADDRESS.CO.CODE` | `FsGiDistAgentAddress_CoCode` | String |  |  |
| 39 | `FS.GI.DIST.AGENT.ADDRESS.DEPT.CODE` | `FsGiDistAgentAddress_DeptCode` | String |  |  |
| 40 | `FS.GI.DIST.AGENT.ADDRESS.AUDITOR.CODE` | `FsGiDistAgentAddress_AuditorCode` | String |  |  |
| 41 | `FS.GI.DIST.AGENT.ADDRESS.AUDIT.DATE.TIME` | `FsGiDistAgentAddress_AuditDateTime` | String |  |  |
