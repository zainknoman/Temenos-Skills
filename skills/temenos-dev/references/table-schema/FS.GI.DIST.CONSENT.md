# FS.GI.DIST.CONSENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.CONSENT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.CONSENT.PARENT.REF.ID` | `FsGiDistConsent_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.CONSENT.ORA.ROWID` | `FsGiDistConsent_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.CONSENT.PARENT.ID.TYPE` | `FsGiDistConsent_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.CONSENT.PARENT.ID` | `FsGiDistConsent_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.CONSENT.CONSENT.FLAG` | `FsGiDistConsent_ConsentFlag` | TField |  | Consent Code of an entity for GDPR process action. Multifonds DB Column is CONSENT. |
| 6 | `FS.GI.DIST.CONSENT.RECEIVED.FLAG` | `FsGiDistConsent_ReceivedFlag` | TField |  | Flag indicates whether or not the investor consents to the GDPR process action. Multifonds DB Column is FLG_RECEIVED. |
| 7 | `FS.GI.DIST.CONSENT.RECEIVED.DATE` | `FsGiDistConsent_ReceivedDate` | TField |  | Date (in DD/MM/YYYY format) on which the consent has been received. Multifonds DB Column is RECEIVED_DATE. |
| 8 | `FS.GI.DIST.CONSENT.SEQUENCE.NUMBER` | `FsGiDistConsent_SequenceNumber` | TField |  | An internal sequence number. Multifonds DB Column is SEQ_NUM. |
| 9 | `FS.GI.DIST.CONSENT.RESERVED10` | `FsGiDistConsent_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.CONSENT.RESERVED9` | `FsGiDistConsent_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.CONSENT.RESERVED8` | `FsGiDistConsent_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.CONSENT.RESERVED7` | `FsGiDistConsent_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.CONSENT.RESERVED6` | `FsGiDistConsent_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.CONSENT.RESERVED5` | `FsGiDistConsent_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.CONSENT.RESERVED4` | `FsGiDistConsent_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.CONSENT.RESERVED3` | `FsGiDistConsent_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.CONSENT.RESERVED2` | `FsGiDistConsent_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.CONSENT.RESERVED1` | `FsGiDistConsent_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.CONSENT.LOCAL.REF` | `FsGiDistConsent_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.CONSENT.OVERRIDE` | `FsGiDistConsent_Override` |  |  |  |
| 21 | `FS.GI.DIST.CONSENT.RECORD.STATUS` | `FsGiDistConsent_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.CONSENT.CURR.NO` | `FsGiDistConsent_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.CONSENT.INPUTTER` | `FsGiDistConsent_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.CONSENT.DATE.TIME` | `FsGiDistConsent_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.CONSENT.AUTHORISER` | `FsGiDistConsent_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.CONSENT.CO.CODE` | `FsGiDistConsent_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.CONSENT.DEPT.CODE` | `FsGiDistConsent_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.CONSENT.AUDITOR.CODE` | `FsGiDistConsent_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.CONSENT.AUDIT.DATE.TIME` | `FsGiDistConsent_AuditDateTime` | String |  |  |
