# FS.GI.DIST.INVESTOR.ADDRESS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.INVESTOR.ADDRESS` in `FS_Address.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.INVESTOR.ADDRESS.PARENT.REF.ID` | `FsGiDistInvestorAddress_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.INVESTOR.ADDRESS.ORA.ROWID` | `FsGiDistInvestorAddress_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.INVESTOR.ADDRESS.INVESTOR.ID` | `FsGiDistInvestorAddress_InvestorId` | TField |  | Investor internal identification number. Multifonds DB Column is NCLIENT. |
| 4 | `FS.GI.DIST.INVESTOR.ADDRESS.SELECTED.FLAG` | `FsGiDistInvestorAddress_SelectedFlag` | TField |  | Selection of the main address for the entity. Multifonds DB Column is MAIN_ADR. |
| 5 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.NUMBER` | `FsGiDistInvestorAddress_AddressNumber` | TField |  | Sequence number of the address. Multifonds DB Column is CADRESSE. |
| 6 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.LINE1` | `FsGiDistInvestorAddress_AddressLine1` | TField |  | Address line 1. Multifonds DB Column is ADRESSE. |
| 7 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.LINE2` | `FsGiDistInvestorAddress_AddressLine2` | TField |  | Address line 2. Multifonds DB Column is ADRESSE_LINE2. |
| 8 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.LINE3` | `FsGiDistInvestorAddress_AddressLine3` | TField |  | Address line 3. Multifonds DB Column is ADRESSE_LINE3. |
| 9 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.LINE4` | `FsGiDistInvestorAddress_AddressLine4` | TField |  | Address line 4. Multifonds DB Column is ADRESSE_LINE4. |
| 10 | `FS.GI.DIST.INVESTOR.ADDRESS.POSTCODE` | `FsGiDistInvestorAddress_Postcode` | TField |  | Post code of the address. Multifonds DB Column is CODE. |
| 11 | `FS.GI.DIST.INVESTOR.ADDRESS.COUNTRY` | `FsGiDistInvestorAddress_Country` | TField |  | Country code (in 2 letter format) of the address. Multifonds DB Column is PAYS. |
| 12 | `FS.GI.DIST.INVESTOR.ADDRESS.STATE` | `FsGiDistInvestorAddress_State` | TField |  | State code of the address. Multifonds DB Column is STATE. |
| 13 | `FS.GI.DIST.INVESTOR.ADDRESS.PO.BOX` | `FsGiDistInvestorAddress_PoBox` | TField |  | PO box number of the address. Multifonds DB Column is ADRESSE_LINE1. |
| 14 | `FS.GI.DIST.INVESTOR.ADDRESS.PRINT.FLAG` | `FsGiDistInvestorAddress_PrintFlag` | TField |  | The address print status. Multifonds DB Column is FLAG_PRINT. |
| 15 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.TYPE` | `FsGiDistInvestorAddress_AddressType` | TField |  | Address type code. Multifonds DB Column is ADR_TYPE. |
| 16 | `FS.GI.DIST.INVESTOR.ADDRESS.CONTACT.PERSON` | `FsGiDistInvestorAddress_ContactPerson` | TField |  | Contact person of the address. Multifonds DB Column is CONTACT_PERSON. |
| 17 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.ID` | `FsGiDistInvestorAddress_AddressId` | TField |  | Unique internal physical address identifier. Multifonds DB Column is INTERNAL_ID. |
| 18 | `FS.GI.DIST.INVESTOR.ADDRESS.CHANGE.REASON.CODE` | `FsGiDistInvestorAddress_ChangeReasonCode` | TField |  | A code to track the reason why an Account field is updated by a user. Multifonds DB Column is CHG_REASON. |
| 19 | `FS.GI.DIST.INVESTOR.ADDRESS.CHANGE.REASON.COMMENT` | `FsGiDistInvestorAddress_ChangeReasonComment` | TField | No | An optional user supplied description of the reason for the modification of the record. Multifonds DB Column is CHG_COMMENT. |
| 20 | `FS.GI.DIST.INVESTOR.ADDRESS.ADDRESS.EXTERNAL.REF` | `FsGiDistInvestorAddress_AddressExternalRef` | TField |  | Address external reference. Multifonds DB Column is ADR_EXT_REF. |
| 21 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED10` | `FsGiDistInvestorAddress_Reserved10` | TField |  |  |
| 22 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED9` | `FsGiDistInvestorAddress_Reserved9` | TField |  |  |
| 23 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED8` | `FsGiDistInvestorAddress_Reserved8` | TField |  |  |
| 24 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED7` | `FsGiDistInvestorAddress_Reserved7` | TField |  |  |
| 25 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED6` | `FsGiDistInvestorAddress_Reserved6` | TField |  |  |
| 26 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED5` | `FsGiDistInvestorAddress_Reserved5` | TField |  |  |
| 27 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED4` | `FsGiDistInvestorAddress_Reserved4` | TField |  |  |
| 28 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED3` | `FsGiDistInvestorAddress_Reserved3` | TField |  |  |
| 29 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED2` | `FsGiDistInvestorAddress_Reserved2` | TField |  |  |
| 30 | `FS.GI.DIST.INVESTOR.ADDRESS.RESERVED1` | `FsGiDistInvestorAddress_Reserved1` | TField |  |  |
| 31 | `FS.GI.DIST.INVESTOR.ADDRESS.LOCAL.REF` | `FsGiDistInvestorAddress_LocalRef` |  |  |  |
| 32 | `FS.GI.DIST.INVESTOR.ADDRESS.OVERRIDE` | `FsGiDistInvestorAddress_Override` |  |  |  |
| 33 | `FS.GI.DIST.INVESTOR.ADDRESS.RECORD.STATUS` | `FsGiDistInvestorAddress_RecordStatus` | String |  |  |
| 34 | `FS.GI.DIST.INVESTOR.ADDRESS.CURR.NO` | `FsGiDistInvestorAddress_CurrNo` | String |  |  |
| 35 | `FS.GI.DIST.INVESTOR.ADDRESS.INPUTTER` | `FsGiDistInvestorAddress_Inputter` |  |  |  |
| 36 | `FS.GI.DIST.INVESTOR.ADDRESS.DATE.TIME` | `FsGiDistInvestorAddress_DateTime` |  |  |  |
| 37 | `FS.GI.DIST.INVESTOR.ADDRESS.AUTHORISER` | `FsGiDistInvestorAddress_Authoriser` | String |  |  |
| 38 | `FS.GI.DIST.INVESTOR.ADDRESS.CO.CODE` | `FsGiDistInvestorAddress_CoCode` | String |  |  |
| 39 | `FS.GI.DIST.INVESTOR.ADDRESS.DEPT.CODE` | `FsGiDistInvestorAddress_DeptCode` | String |  |  |
| 40 | `FS.GI.DIST.INVESTOR.ADDRESS.AUDITOR.CODE` | `FsGiDistInvestorAddress_AuditorCode` | String |  |  |
| 41 | `FS.GI.DIST.INVESTOR.ADDRESS.AUDIT.DATE.TIME` | `FsGiDistInvestorAddress_AuditDateTime` | String |  |  |
