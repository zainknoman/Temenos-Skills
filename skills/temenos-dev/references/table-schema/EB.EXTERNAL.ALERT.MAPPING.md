# EB.EXTERNAL.ALERT.MAPPING — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.ALERT.MAPPING` in `BE_AlertProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXT.ALT.DESCRIPTION` | `EbExternalAlertMapping_Description` |  |  |  |
| 2 | `EXT.ALT.APPLICATION.NAME` | `EbExternalAlertMapping_ApplicationName` | TField |  | This field is to specify the type of the application as defined in TEC.ITEMS to trigger an external alert. |
| 3 | `EXT.ALT.HEADER.MAPPING` | `EbExternalAlertMapping_HeaderMapping` | TField |  | Header values getting mapped from EB.EXTERNAL.REST.API.HEADER application to transmit alert to the external system. Validation Rules: Valid entry in EB.EXTERNAL.REST.API.HEADER application. |
| 4 | `EXT.ALT.BODY.TAG.START` | `EbExternalAlertMapping_BodyTagStart` |  |  |  |
| 5 | `EXT.ALT.DATA.FIELD.NAME` | `EbExternalAlertMapping_DataFieldName` |  |  |  |
| 6 | `EXT.ALT.DATA.FIELD.VALUE` | `EbExternalAlertMapping_DataFieldValue` |  |  |  |
| 7 | `EXT.ALT.FIELD.MAPPING.NUMBER` | `EbExternalAlertMapping_FieldMappingNumber` |  |  |  |
| 8 | `EXT.ALT.DATA.SINGLE.MULT` | `EbExternalAlertMapping_DataSingleMult` |  |  |  |
| 9 | `EXT.ALT.BODY.TAG.END` | `EbExternalAlertMapping_BodyTagEnd` |  |  |  |
| 10 | `EXT.ALT.SEPARATOR` | `EbExternalAlertMapping_Separator` |  |  |  |
| 11 | `EXT.ALT.RESERVEDFLD.6` | `EbExternalAlertMapping_Reservedfld6` |  |  |  |
| 12 | `EXT.ALT.RESERVEDFLD.5` | `EbExternalAlertMapping_Reservedfld5` |  |  |  |
| 13 | `EXT.ALT.RESERVEDFLD.4` | `EbExternalAlertMapping_Reservedfld4` |  |  |  |
| 14 | `EXT.ALT.RESERVEDFLD.3` | `EbExternalAlertMapping_Reservedfld3` |  |  |  |
| 15 | `EXT.ALT.RESERVEDFLD.2` | `EbExternalAlertMapping_Reservedfld2` |  |  |  |
| 16 | `EXT.ALT.RESERVEDFLD.1` | `EbExternalAlertMapping_Reservedfld1` |  |  |  |
| 17 | `EXT.ALT.RESERVED.10` | `EbExternalAlertMapping_Reserved10` | TField |  |  |
| 18 | `EXT.ALT.RESERVED.9` | `EbExternalAlertMapping_Reserved9` | TField |  |  |
| 19 | `EXT.ALT.RESERVED.8` | `EbExternalAlertMapping_Reserved8` | TField |  |  |
| 20 | `EXT.ALT.RESERVED.7` | `EbExternalAlertMapping_Reserved7` | TField |  |  |
| 21 | `EXT.ALT.RESERVED.6` | `EbExternalAlertMapping_Reserved6` | TField |  |  |
| 22 | `EXT.ALT.RESERVED.5` | `EbExternalAlertMapping_Reserved5` | TField |  |  |
| 23 | `EXT.ALT.RESERVED.4` | `EbExternalAlertMapping_Reserved4` | TField |  |  |
| 24 | `EXT.ALT.RESERVED.3` | `EbExternalAlertMapping_Reserved3` | TField |  |  |
| 25 | `EXT.ALT.RESERVED.2` | `EbExternalAlertMapping_Reserved2` | TField |  |  |
| 26 | `EXT.ALT.RESERVED.1` | `EbExternalAlertMapping_Reserved1` | TField |  |  |
| 27 | `EXT.ALT.LOCAL.REF` | `EbExternalAlertMapping_LocalRef` |  |  |  |
| 28 | `EXT.ALT.OVERRIDE` | `EbExternalAlertMapping_Override` |  |  |  |
| 29 | `EXT.ALT.RECORD.STATUS` | `EbExternalAlertMapping_RecordStatus` | String |  |  |
| 30 | `EXT.ALT.CURR.NO` | `EbExternalAlertMapping_CurrNo` | String |  |  |
| 31 | `EXT.ALT.INPUTTER` | `EbExternalAlertMapping_Inputter` |  |  |  |
| 32 | `EXT.ALT.DATE.TIME` | `EbExternalAlertMapping_DateTime` |  |  |  |
| 33 | `EXT.ALT.AUTHORISER` | `EbExternalAlertMapping_Authoriser` | String |  |  |
| 34 | `EXT.ALT.CO.CODE` | `EbExternalAlertMapping_CoCode` | String |  |  |
| 35 | `EXT.ALT.DEPT.CODE` | `EbExternalAlertMapping_DeptCode` | String |  |  |
| 36 | `EXT.ALT.AUDITOR.CODE` | `EbExternalAlertMapping_AuditorCode` | String |  |  |
| 37 | `EXT.ALT.AUDIT.DATE.TIME` | `EbExternalAlertMapping_AuditDateTime` | String |  |  |
| 38 | `EXT.ALT.DATA.FIELD.LABEL` | `EbExternalAlertMapping_DataFieldLabel` |  |  |  |
| 39 | `EXT.ALT.NON.NEGATIVE` | `EbExternalAlertMapping_NonNegative` |  |  |  |
