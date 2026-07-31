# EB.ACCESS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EB.ACCESS.PARAMETER` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.ACP.DEFAULT.ACCESS` | `EbAccessParameter_DefaultAccess` | TField |  | Default Access of the field. By Default it is set as LOCKED Valid input is 'LOCKED' or 'UNLOCKED' |
| 2 | `EB.ACP.CLASSIFICATION` | `EbAccessParameter_Classification` |  |  |  |
| 3 | `EB.ACP.FIELD.NAME` | `EbAccessParameter_FieldName` |  |  |  |
| 4 | `EB.ACP.FIELD.NO` | `EbAccessParameter_FieldNo` |  |  |  |
| 5 | `EB.ACP.FIELD.ACCESS` | `EbAccessParameter_FieldAccess` |  |  |  |
| 6 | `EB.ACP.RESERVED.1` | `EbAccessParameter_Reserved1` |  |  |  |
| 7 | `EB.ACP.RESERVED.2` | `EbAccessParameter_Reserved2` |  |  |  |
| 8 | `EB.ACP.RESERVED.3` | `EbAccessParameter_Reserved3` |  |  |  |
| 9 | `EB.ACP.RESERVED.4` | `EbAccessParameter_Reserved4` |  |  |  |
| 10 | `EB.ACP.RESERVED.5` | `EbAccessParameter_Reserved5` |  |  |  |
| 11 | `EB.ACP.RECORD.ID` | `EbAccessParameter_RecordId` |  |  |  |
| 12 | `EB.ACP.EXCLUDE.DATA.TYPE` | `EbAccessParameter_ExcludeDataType` |  |  |  |
| 13 | `EB.ACP.ID.PARAMETER` | `EbAccessParameter_IdParameter` | TField |  | Field to indicate if the application can allow Id specific lock down rules If ID.PARAMETER is enabled, record key specific lock down rules are applied to the transaction for which the record key matches with the record created in EB.ACCESS.PARAMETER of the format application-recordKey |
| 14 | `EB.ACP.DISABLE.NEW.RECORD` | `EbAccessParameter_DisableNewRecord` | TField |  | Enabling Disable New record field will stop the application mentioned in @ID from creating new records |
| 15 | `EB.ACP.LOCK.TEMENOS.RECORD` | `EbAccessParameter_LockTemenosRecord` | TField |  | When Lock Temenos Record field is enabled, records released from Temenos (entry in PGM.DATA.CONTROL) will have a default lockdown and cannot be amended |
| 16 | `EB.ACP.RESERVED.9` | `EbAccessParameter_Reserved9` | TField |  | Reserved Field |
| 17 | `EB.ACP.RESERVED.10` | `EbAccessParameter_Reserved10` | TField |  | Reserved Field |
| 18 | `EB.ACP.OVERRIDE` | `EbAccessParameter_Override` |  |  |  |
| 19 | `EB.ACP.RECORD.STATUS` | `EbAccessParameter_RecordStatus` | String |  |  |
| 20 | `EB.ACP.CURR.NO` | `EbAccessParameter_CurrNo` | String |  |  |
| 21 | `EB.ACP.INPUTTER` | `EbAccessParameter_Inputter` |  |  |  |
| 22 | `EB.ACP.DATE.TIME` | `EbAccessParameter_DateTime` |  |  |  |
| 23 | `EB.ACP.AUTHORISER` | `EbAccessParameter_Authoriser` | String |  |  |
| 24 | `EB.ACP.CO.CODE` | `EbAccessParameter_CoCode` | String |  |  |
| 25 | `EB.ACP.DEPT.CODE` | `EbAccessParameter_DeptCode` | String |  |  |
| 26 | `EB.ACP.AUDITOR.CODE` | `EbAccessParameter_AuditorCode` | String |  |  |
| 27 | `EB.ACP.AUDIT.DATE.TIME` | `EbAccessParameter_AuditDateTime` | String |  |  |
