# EB.EVENT.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.EVENT.TYPE` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.EVN.TYP.DESCRIPTION` | `EbEventType_Description` |  |  |  |
| 2 | `EB.EVN.TYP.TABLE` | `EbEventType_Table` | TField | No | It should be a valid T24 filename i.e Present on FILE.CONTROL.Optional Input. Type=Alphanumeric; Length=35Name of Source Table associated to this event type. Validation rules: |
| 3 | `EB.EVN.TYP.EB.ACTIVITY` | `EbEventType_EbActivity` | TField |  | Accepts input from EB.ACTIVITY application. Clients can set up records in EB.ACTIVITY and define individual message types in EB.ADVICES application to send alerts - taking up soft-delivery route |
| 4 | `EB.EVN.TYP.AC.FIELD.NAME` | `EbEventType_AcFieldName` |  |  |  |
| 5 | `EB.EVN.TYP.APPLICATION.API` | `EbEventType_ApplicationApi` | TField |  | For the processing of Inline events it may require application specific values like SERVICE.LINK, SERVICE.PRODUCT,SYSTEM.ID etc and it is the responsibility of user to pass the repetitive values. During the call of Inline processing an Hook API(&lt;Application Api\Event Type id's first component&gt;+'.EXTRACT.API', Example if the Application Api is specified as ACCOUNT.SWEEP then the extract API should be ACCOUNT.SWEEP.EXTRACT.API) will be invoked to pass the application specific values if its required. If this field is null then it will take the first component of id to form the API name. More information kindly refer the sample API's for the event type AC.ACCOUNT.LINK-SERVICE. Also it is possible to stop processing the TEC call for a particular context for example no tec invocation during Reverse and Replay of an activity. During the call of Inline processing another Hook API (&lt;Application Api\Event Type id's first component&gt;+'.EXIT.API', Example if the Application Api is specified as ACCOUNT.SWEEP then the extract API should be ACCOUNT.SWEEP.EXIT.API) will be invoked to exit from the current call. If this field is null then it will take the first component of id to form the API name. More information kindly refer the sample API's for the event type AC.ACCOUNT.LINK-SERVICE. Note : To invoke both API's it should have a valid entry in EB.API. |
| 6 | `EB.EVN.TYP.PAYLOAD.MAPPER` | `EbEventType_PayloadMapper` | TField |  |  |
| 7 | `EB.EVN.TYP.RESERVED.4` | `EbEventType_Reserved4` | TField |  |  |
| 8 | `EB.EVN.TYP.RESERVED.5` | `EbEventType_Reserved5` | TField |  |  |
| 9 | `EB.EVN.TYP.RESERVED.6` | `EbEventType_Reserved6` | TField |  |  |
| 10 | `EB.EVN.TYP.RESERVED.7` | `EbEventType_Reserved7` | TField |  |  |
| 11 | `EB.EVN.TYP.RESERVED.8` | `EbEventType_Reserved8` | TField |  |  |
| 12 | `EB.EVN.TYP.RESERVED.9` | `EbEventType_Reserved9` | TField |  |  |
| 13 | `EB.EVN.TYP.RESERVED.10` | `EbEventType_Reserved10` | TField |  |  |
| 14 | `EB.EVN.TYP.LOCAL.REF` | `EbEventType_LocalRef` |  |  |  |
| 15 | `EB.EVN.TYP.OVERRIDE` | `EbEventType_Override` |  |  |  |
| 16 | `EB.EVN.TYP.RECORD.STATUS` | `EbEventType_RecordStatus` | String |  |  |
| 17 | `EB.EVN.TYP.CURR.NO` | `EbEventType_CurrNo` | String |  |  |
| 18 | `EB.EVN.TYP.INPUTTER` | `EbEventType_Inputter` |  |  |  |
| 19 | `EB.EVN.TYP.DATE.TIME` | `EbEventType_DateTime` |  |  |  |
| 20 | `EB.EVN.TYP.AUTHORISER` | `EbEventType_Authoriser` | String |  |  |
| 21 | `EB.EVN.TYP.CO.CODE` | `EbEventType_CoCode` | String |  |  |
| 22 | `EB.EVN.TYP.DEPT.CODE` | `EbEventType_DeptCode` | String |  |  |
| 23 | `EB.EVN.TYP.AUDITOR.CODE` | `EbEventType_AuditorCode` | String |  |  |
| 24 | `EB.EVN.TYP.AUDIT.DATE.TIME` | `EbEventType_AuditDateTime` | String |  |  |
