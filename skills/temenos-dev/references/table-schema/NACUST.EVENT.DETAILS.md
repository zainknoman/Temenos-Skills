# NACUST.EVENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.NACUST.EVENT.DETAILS` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NACUST.EVENT.DESCRIPTION` | `NacustEventDetails_Description` |  |  |  |
| 2 | `NACUST.EVENT.FULL.DESC` | `NacustEventDetails_FullDesc` |  |  |  |
| 3 | `NACUST.EVENT.EXECUTION.STAGE` | `NacustEventDetails_ExecutionStage` |  |  |  |
| 4 | `NACUST.EVENT.EXECUTION.SEQ` | `NacustEventDetails_ExecutionSeq` |  |  |  |
| 5 | `NACUST.EVENT.RESERVED.25` | `NacustEventDetails_Reserved25` |  |  |  |
| 6 | `NACUST.EVENT.RESERVED.24` | `NacustEventDetails_Reserved24` |  |  |  |
| 7 | `NACUST.EVENT.RESERVED.23` | `NacustEventDetails_Reserved23` |  |  |  |
| 8 | `NACUST.EVENT.RESERVED.22` | `NacustEventDetails_Reserved22` |  |  |  |
| 9 | `NACUST.EVENT.RESERVED.21` | `NacustEventDetails_Reserved21` |  |  |  |
| 10 | `NACUST.EVENT.EVENT.PROCESS.API` | `NacustEventDetails_EventProcessApi` | TField | Yes | Event api that will be triggered during the defined EXECUTION.STAGE of CoB. Validation Rules Mandatory Field. Routine should have an entry in the application EB.API. |
| 11 | `NACUST.EVENT.COMPONENT.NAME` | `NacustEventDetails_ComponentName` | TField | Yes | Component through which this event is triggered. Validation Rules Mandatory Field. Field value should be a valid record in the EB.COMPONENT application. |
| 12 | `NACUST.EVENT.ADVICE.NO` | `NacustEventDetails_AdviceNo` | TField | No | Field to capture the ADVICES ID. If this field is setup, then Delivery message will be generated. Validation Rules Optional Field. Field value should be a valid record in EB.ADVICES. |
| 13 | `NACUST.EVENT.RESERVED.20` | `NacustEventDetails_Reserved20` | TField |  |  |
| 14 | `NACUST.EVENT.RESERVED.19` | `NacustEventDetails_Reserved19` | TField |  |  |
| 15 | `NACUST.EVENT.RESERVED.18` | `NacustEventDetails_Reserved18` | TField |  |  |
| 16 | `NACUST.EVENT.RESERVED.17` | `NacustEventDetails_Reserved17` | TField |  |  |
| 17 | `NACUST.EVENT.RESERVED.16` | `NacustEventDetails_Reserved16` | TField |  |  |
| 18 | `NACUST.EVENT.RESERVED.15` | `NacustEventDetails_Reserved15` | TField |  |  |
| 19 | `NACUST.EVENT.RESERVED.14` | `NacustEventDetails_Reserved14` | TField |  |  |
| 20 | `NACUST.EVENT.RESERVED.13` | `NacustEventDetails_Reserved13` | TField |  |  |
| 21 | `NACUST.EVENT.RESERVED.12` | `NacustEventDetails_Reserved12` | TField |  |  |
| 22 | `NACUST.EVENT.RESERVED.11` | `NacustEventDetails_Reserved11` | TField |  |  |
| 23 | `NACUST.EVENT.RESERVED.10` | `NacustEventDetails_Reserved10` | TField |  |  |
| 24 | `NACUST.EVENT.RESERVED.9` | `NacustEventDetails_Reserved9` | TField |  |  |
| 25 | `NACUST.EVENT.RESERVED.8` | `NacustEventDetails_Reserved8` | TField |  |  |
| 26 | `NACUST.EVENT.RESERVED.7` | `NacustEventDetails_Reserved7` | TField |  |  |
| 27 | `NACUST.EVENT.RESERVED.6` | `NacustEventDetails_Reserved6` | TField |  |  |
| 28 | `NACUST.EVENT.RESERVED.5` | `NacustEventDetails_Reserved5` | TField |  |  |
| 29 | `NACUST.EVENT.RESERVED.4` | `NacustEventDetails_Reserved4` | TField |  |  |
| 30 | `NACUST.EVENT.RESERVED.3` | `NacustEventDetails_Reserved3` | TField |  |  |
| 31 | `NACUST.EVENT.RESERVED.2` | `NacustEventDetails_Reserved2` | TField |  |  |
| 32 | `NACUST.EVENT.RESERVED.1` | `NacustEventDetails_Reserved1` | TField |  |  |
| 33 | `NACUST.EVENT.LOCAL.REF` | `NacustEventDetails_LocalRef` |  |  |  |
| 34 | `NACUST.EVENT.OVERRIDE` | `NacustEventDetails_Override` |  |  |  |
| 35 | `NACUST.EVENT.RECORD.STATUS` | `NacustEventDetails_RecordStatus` | String |  |  |
| 36 | `NACUST.EVENT.CURR.NO` | `NacustEventDetails_CurrNo` | String |  |  |
| 37 | `NACUST.EVENT.INPUTTER` | `NacustEventDetails_Inputter` |  |  |  |
| 38 | `NACUST.EVENT.DATE.TIME` | `NacustEventDetails_DateTime` |  |  |  |
| 39 | `NACUST.EVENT.AUTHORISER` | `NacustEventDetails_Authoriser` | String |  |  |
| 40 | `NACUST.EVENT.CO.CODE` | `NacustEventDetails_CoCode` | String |  |  |
| 41 | `NACUST.EVENT.DEPT.CODE` | `NacustEventDetails_DeptCode` | String |  |  |
| 42 | `NACUST.EVENT.AUDITOR.CODE` | `NacustEventDetails_AuditorCode` | String |  |  |
| 43 | `NACUST.EVENT.AUDIT.DATE.TIME` | `NacustEventDetails_AuditDateTime` | String |  |  |
