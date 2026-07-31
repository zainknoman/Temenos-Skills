# MS.EVENT — Table Schema

> Source: `INSERTS/I_F.MS.EVENT` in `EB_MicroService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.SOE.DESCRIPTION` | `MsEvent_Description` |  |  |  |
| 2 | `MS.SOE.EVENT.CLASS` | `MsEvent_EventClass` | TField | Yes | EVENT Class present in MS.EVENT.CLASS application Validation: This is a mandatory field |
| 3 | `MS.SOE.EVENT.GROUP` | `MsEvent_EventGroup` | TField | Yes | Indicated to which Group this Event belongs to Validation: This is a mandatory field |
| 4 | `MS.SOE.SUBSCRIBED` | `MsEvent_Subscribed` | TField | Yes | Events will be emitted only if this field is set to Yes Validation: This is a mandatory field |
| 5 | `MS.SOE.TRANSACT.STAGE` | `MsEvent_TransactStage` | TField | Yes | Stage of the event This is a mandatory field and EB.LOOKUP on MS.TRANSACT.STAGE Validation: This is a mandatory field only if Event is Subscribed and not a Business Event(BUSINESS.EVENT will be set in MS.EVENT.CLASS) |
| 6 | `MS.SOE.COMPENSATORY.ACTION` | `MsEvent_CompensatoryAction` | TField |  | This field will be set as EMIT if event has be emitted for a compensatory request |
| 7 | `MS.SOE.ATTRIBUTE.TYPE` | `MsEvent_AttributeType` |  |  |  |
| 8 | `MS.SOE.ATTRIBUTE.VALUE` | `MsEvent_AttributeValue` |  |  |  |
| 9 | `MS.SOE.RESERVED.13` | `MsEvent_Reserved13` | TField |  | Reserved Field |
| 10 | `MS.SOE.RESERVED.12` | `MsEvent_Reserved12` | TField |  | Reserved Field |
| 11 | `MS.SOE.RESERVED.11` | `MsEvent_Reserved11` | TField |  | Reserved Field |
| 12 | `MS.SOE.RESERVED.10` | `MsEvent_Reserved10` | TField |  | Reserved Field |
| 13 | `MS.SOE.RESERVED.9` | `MsEvent_Reserved9` | TField |  | Reserved Field |
| 14 | `MS.SOE.RESERVED.8` | `MsEvent_Reserved8` | TField |  | Reserved Field |
| 15 | `MS.SOE.RESERVED.7` | `MsEvent_Reserved7` | TField |  | Reserved Field |
| 16 | `MS.SOE.RESERVED.6` | `MsEvent_Reserved6` | TField |  | Reserved Field |
| 17 | `MS.SOE.RESERVED.5` | `MsEvent_Reserved5` | TField |  | Reserved Field |
| 18 | `MS.SOE.RESERVED.4` | `MsEvent_Reserved4` | TField |  | Reserved Field |
| 19 | `MS.SOE.RESERVED.3` | `MsEvent_Reserved3` | TField |  | Reserved Field |
| 20 | `MS.SOE.RESERVED.2` | `MsEvent_Reserved2` | TField |  | Reserved Field |
| 21 | `MS.SOE.RESERVED.1` | `MsEvent_Reserved1` | TField |  | Reserved Field |
| 22 | `MS.SOE.LOCAL.REF` | `MsEvent_LocalRef` |  |  |  |
| 23 | `MS.SOE.OVERRIDE` | `MsEvent_Override` |  |  |  |
| 24 | `MS.SOE.RECORD.STATUS` | `MsEvent_RecordStatus` | String |  |  |
| 25 | `MS.SOE.CURR.NO` | `MsEvent_CurrNo` | String |  |  |
| 26 | `MS.SOE.INPUTTER` | `MsEvent_Inputter` |  |  |  |
| 27 | `MS.SOE.DATE.TIME` | `MsEvent_DateTime` |  |  |  |
| 28 | `MS.SOE.AUTHORISER` | `MsEvent_Authoriser` | String |  |  |
| 29 | `MS.SOE.CO.CODE` | `MsEvent_CoCode` | String |  |  |
| 30 | `MS.SOE.DEPT.CODE` | `MsEvent_DeptCode` | String |  |  |
| 31 | `MS.SOE.AUDITOR.CODE` | `MsEvent_AuditorCode` | String |  |  |
| 32 | `MS.SOE.AUDIT.DATE.TIME` | `MsEvent_AuditDateTime` | String |  |  |
