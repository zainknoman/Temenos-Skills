# FS.GI.DIST.REGISTER.ADDRESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.REGISTER.ADDRESS` in `FS_Address.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.REGISTER.ADDRESS.PARENT.REF.ID` | `FsGiDistRegisterAddress_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.REGISTER.ADDRESS.ORA.ROWID` | `FsGiDistRegisterAddress_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.REGISTER.ADDRESS.REGISTER.ID` | `FsGiDistRegisterAddress_RegisterId` | TField |  | Register Internal Identification number. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.REGISTER.ADDRESS.SELECTED.FLAG` | `FsGiDistRegisterAddress_SelectedFlag` | TField |  | Selection of the main address for the entity. Multifonds DB Column is MAIN_ADR. |
| 5 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.NUMBER` | `FsGiDistRegisterAddress_AddressNumber` | TField |  | Sequence number of the address. Multifonds DB Column is CADRESSE. |
| 6 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.LINE1` | `FsGiDistRegisterAddress_AddressLine1` | TField |  | Address line 1. Multifonds DB Column is ADRESSE. |
| 7 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.LINE2` | `FsGiDistRegisterAddress_AddressLine2` | TField |  | Address line 2. Multifonds DB Column is ADRESSE_LINE2. |
| 8 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.LINE3` | `FsGiDistRegisterAddress_AddressLine3` | TField |  | Address line 3. Multifonds DB Column is ADRESSE_LINE3. |
| 9 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.LINE4` | `FsGiDistRegisterAddress_AddressLine4` | TField |  | Address line 4. Multifonds DB Column is ADRESSE_LINE4. |
| 10 | `FS.GI.DIST.REGISTER.ADDRESS.POSTCODE` | `FsGiDistRegisterAddress_Postcode` | TField |  | Post code of the address. Multifonds DB Column is CODE. |
| 11 | `FS.GI.DIST.REGISTER.ADDRESS.COUNTRY` | `FsGiDistRegisterAddress_Country` | TField |  | Country code (in 2 letter format) of the address. Multifonds DB Column is PAYS. |
| 12 | `FS.GI.DIST.REGISTER.ADDRESS.STATE` | `FsGiDistRegisterAddress_State` | TField |  | State code of the address. Multifonds DB Column is STATE. |
| 13 | `FS.GI.DIST.REGISTER.ADDRESS.PO.BOX` | `FsGiDistRegisterAddress_PoBox` | TField |  | PO box number of the address. Multifonds DB Column is ADRESSE_LINE1. |
| 14 | `FS.GI.DIST.REGISTER.ADDRESS.PRINT.FLAG` | `FsGiDistRegisterAddress_PrintFlag` | TField |  | The address print status. Multifonds DB Column is FLAG_PRINT. |
| 15 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.TYPE` | `FsGiDistRegisterAddress_AddressType` | TField |  | Address type code. Multifonds DB Column is ADR_TYPE. |
| 16 | `FS.GI.DIST.REGISTER.ADDRESS.CONTACT.PERSON` | `FsGiDistRegisterAddress_ContactPerson` | TField |  | Contact person of the address. Multifonds DB Column is CONTACT_PERSON. |
| 17 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.ID` | `FsGiDistRegisterAddress_AddressId` | TField |  | Unique internal physical address identifier. Multifonds DB Column is INTERNAL_ID. |
| 18 | `FS.GI.DIST.REGISTER.ADDRESS.CHANGE.REASON.CODE` | `FsGiDistRegisterAddress_ChangeReasonCode` | TField |  | A code to track the reason why an Account field is updated by a user. Multifonds DB Column is CHG_REASON. |
| 19 | `FS.GI.DIST.REGISTER.ADDRESS.CHANGE.REASON.COMMENT` | `FsGiDistRegisterAddress_ChangeReasonComment` | TField | No | An optional user supplied description of the reason for the modification of the record. Multifonds DB Column is CHG_COMMENT. |
| 20 | `FS.GI.DIST.REGISTER.ADDRESS.ADDRESS.EXTERNAL.REF` | `FsGiDistRegisterAddress_AddressExternalRef` | TField |  | Address external reference. Multifonds DB Column is ADR_EXT_REF. |
| 21 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED10` | `FsGiDistRegisterAddress_Reserved10` | TField |  |  |
| 22 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED9` | `FsGiDistRegisterAddress_Reserved9` | TField |  |  |
| 23 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED8` | `FsGiDistRegisterAddress_Reserved8` | TField |  |  |
| 24 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED7` | `FsGiDistRegisterAddress_Reserved7` | TField |  |  |
| 25 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED6` | `FsGiDistRegisterAddress_Reserved6` | TField |  |  |
| 26 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED5` | `FsGiDistRegisterAddress_Reserved5` | TField |  |  |
| 27 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED4` | `FsGiDistRegisterAddress_Reserved4` | TField |  |  |
| 28 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED3` | `FsGiDistRegisterAddress_Reserved3` | TField |  |  |
| 29 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED2` | `FsGiDistRegisterAddress_Reserved2` | TField |  |  |
| 30 | `FS.GI.DIST.REGISTER.ADDRESS.RESERVED1` | `FsGiDistRegisterAddress_Reserved1` | TField |  |  |
| 31 | `FS.GI.DIST.REGISTER.ADDRESS.LOCAL.REF` | `FsGiDistRegisterAddress_LocalRef` |  |  |  |
| 32 | `FS.GI.DIST.REGISTER.ADDRESS.OVERRIDE` | `FsGiDistRegisterAddress_Override` |  |  |  |
| 33 | `FS.GI.DIST.REGISTER.ADDRESS.RECORD.STATUS` | `FsGiDistRegisterAddress_RecordStatus` | String |  |  |
| 34 | `FS.GI.DIST.REGISTER.ADDRESS.CURR.NO` | `FsGiDistRegisterAddress_CurrNo` | String |  |  |
| 35 | `FS.GI.DIST.REGISTER.ADDRESS.INPUTTER` | `FsGiDistRegisterAddress_Inputter` |  |  |  |
| 36 | `FS.GI.DIST.REGISTER.ADDRESS.DATE.TIME` | `FsGiDistRegisterAddress_DateTime` |  |  |  |
| 37 | `FS.GI.DIST.REGISTER.ADDRESS.AUTHORISER` | `FsGiDistRegisterAddress_Authoriser` | String |  |  |
| 38 | `FS.GI.DIST.REGISTER.ADDRESS.CO.CODE` | `FsGiDistRegisterAddress_CoCode` | String |  |  |
| 39 | `FS.GI.DIST.REGISTER.ADDRESS.DEPT.CODE` | `FsGiDistRegisterAddress_DeptCode` | String |  |  |
| 40 | `FS.GI.DIST.REGISTER.ADDRESS.AUDITOR.CODE` | `FsGiDistRegisterAddress_AuditorCode` | String |  |  |
| 41 | `FS.GI.DIST.REGISTER.ADDRESS.AUDIT.DATE.TIME` | `FsGiDistRegisterAddress_AuditDateTime` | String |  |  |
