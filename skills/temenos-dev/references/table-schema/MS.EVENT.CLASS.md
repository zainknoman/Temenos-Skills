# MS.EVENT.CLASS — Table Schema

> Source: `INSERTS/I_F.MS.EVENT.CLASS` in `EB_MicroService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.EC.DESCRIPTION` | `MsEventClass_Description` |  |  |  |
| 2 | `MS.EC.SYSTEM.IDENTIFIER` | `MsEventClass_SystemIdentifier` | TField | Yes | System Name to which Event has to be emitted from ServiceOrchestrator. Validation: This is a mandatory field |
| 3 | `MS.EC.SEQUENCE` | `MsEventClass_Sequence` | TField | Yes | Sequence order in which event will be emitted to SO Validation: This is a mandatory field |
| 4 | `MS.EC.POJO.CLASS` | `MsEventClass_PojoClass` | TField | Yes | Java class that will be triggered by FIELD.OBJECT.MAPPER API to build field object. Validation: This is a mandatory field |
| 5 | `MS.EC.FIELD.OBJECT.MAPPER` | `MsEventClass_FieldObjectMapper` | TField | Yes | JBC API wrapper , This routine will be called during PayloadHandoff to convert Payload to Json String Validation: This is a mandatory field Check.file on EB.API |
| 6 | `MS.EC.EXTENSION.DATA.MAPPER` | `MsEventClass_ExtensionDataMapper` | TField | Yes | JBC Wrapper will be called during PayloadHandoff , if any addition fieldName and Values to be sent before Json conversion Validation: This is a mandatory field Check.file on EB.API |
| 7 | `MS.EC.BUSINESS.EVENT` | `MsEvent_BusinessEvent` |  |  |  |
| 8 | `MS.EC.DISABLE.OBJ.MAPPER` | `MsEventClass_DisableObjMapper` | TField | Yes | This is Yes/No field to indicate whether ObjectMapper to be made as mandatory or not Validation: Yes - ObjectMapper and Pojo Class are not mandatory i.e., each business vertical will have their own logic to generate Json No - ObjectMapper and Pojo Class are mandatory |
| 9 | `MS.EC.ATTRIBUTE.TYPE` | `MsEventClass_AttributeType` |  |  |  |
| 10 | `MS.EC.ATTRIBUTE.VALUE` | `MsEventClass_AttributeValue` |  |  |  |
| 11 | `MS.EC.RESERVED.11` | `MsEventClass_Reserved11` | TField |  | Reserved Field |
| 12 | `MS.EC.RESERVED.10` | `MsEventClass_Reserved10` | TField |  | Reserved Field |
| 13 | `MS.EC.RESERVED.9` | `MsEventClass_Reserved9` | TField |  | Reserved Field |
| 14 | `MS.EC.RESERVED.8` | `MsEventClass_Reserved8` | TField |  | Reserved Field |
| 15 | `MS.EC.RESERVED.7` | `MsEventClass_Reserved7` | TField |  | Reserved Field |
| 16 | `MS.EC.RESERVED.6` | `MsEventClass_Reserved6` | TField |  | Reserved Field |
| 17 | `MS.EC.RESERVED.5` | `MsEventClass_Reserved5` | TField |  | Reserved Field |
| 18 | `MS.EC.RESERVED.4` | `MsEventClass_Reserved4` | TField |  | Reserved Field |
| 19 | `MS.EC.RESERVED.3` | `MsEventClass_Reserved3` | TField |  | Reserved Field |
| 20 | `MS.EC.RESERVED.2` | `MsEventClass_Reserved2` | TField |  | Reserved Field |
| 21 | `MS.EC.RESERVED.1` | `MsEventClass_Reserved1` | TField |  | Reserved Field |
| 22 | `MS.EC.LOCAL.REF` | `MsEventClass_LocalRef` |  |  |  |
| 23 | `MS.EC.OVERRIDE` | `MsEventClass_Override` |  |  |  |
| 24 | `MS.EC.RECORD.STATUS` | `MsEventClass_RecordStatus` | String |  |  |
| 25 | `MS.EC.CURR.NO` | `MsEventClass_CurrNo` | String |  |  |
| 26 | `MS.EC.INPUTTER` | `MsEventClass_Inputter` |  |  |  |
| 27 | `MS.EC.DATE.TIME` | `MsEventClass_DateTime` |  |  |  |
| 28 | `MS.EC.AUTHORISER` | `MsEventClass_Authoriser` | String |  |  |
| 29 | `MS.EC.CO.CODE` | `MsEventClass_CoCode` | String |  |  |
| 30 | `MS.EC.DEPT.CODE` | `MsEventClass_DeptCode` | String |  |  |
| 31 | `MS.EC.AUDITOR.CODE` | `MsEventClass_AuditorCode` | String |  |  |
| 32 | `MS.EC.AUDIT.DATE.TIME` | `MsEventClass_AuditDateTime` | String |  |  |
