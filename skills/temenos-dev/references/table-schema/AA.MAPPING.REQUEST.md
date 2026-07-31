# AA.MAPPING.REQUEST — Table Schema

> Source: `INSERTS/I_F.AA.MAPPING.REQUEST` in `AF_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.MAPR.APPLICATION` | `AaMappingRequest_Application` | TField | Yes | Reference of the OA.APPLICATION. Mandatory field |
| 2 | `AA.MAPR.PURPOSE` | `AaMappingRequest_Purpose` | TField | Yes | This field specifies the Purpose of the OA.APPLICATION. If the Application is running for multiple purposes, then this is mandatory. For single purpose,System would default the same. |
| 3 | `AA.MAPR.FULFILMENT.TYPE` | `AaMappingRequest_FulfilmentType` |  |  |  |
| 4 | `AA.MAPR.RESERVED.12` | `AaMappingRequest_Reserved12` |  |  |  |
| 5 | `AA.MAPR.RESERVED.11` | `AaMappingRequest_Reserved11` |  |  |  |
| 6 | `AA.MAPR.RESERVED.10` | `AaMappingRequest_Reserved10` |  |  |  |
| 7 | `AA.MAPR.RESERVED.9` | `AaMappingRequest_Reserved9` |  |  |  |
| 8 | `AA.MAPR.TARGET.APPLICATION` | `AaMappingRequest_TargetApplication` |  |  |  |
| 9 | `AA.MAPR.TARGET.REFERENCE` | `AaMappingRequest_TargetReference` |  |  |  |
| 10 | `AA.MAPR.TARGET.RESPONSE.STATUS` | `AaMappingRequest_TargetResponseStatus` |  |  |  |
| 11 | `AA.MAPR.RESERVED.8` | `AaMappingRequest_Reserved8` |  |  |  |
| 12 | `AA.MAPR.RESERVED.7` | `AaMappingRequest_Reserved7` |  |  |  |
| 13 | `AA.MAPR.RESERVED.6` | `AaMappingRequest_Reserved6` |  |  |  |
| 14 | `AA.MAPR.RESERVED.5` | `AaMappingRequest_Reserved5` |  |  |  |
| 15 | `AA.MAPR.TARGET.FAILURE` | `AaMappingRequest_TargetFailure` |  |  |  |
| 16 | `AA.MAPR.TARGET.FAILURE.DETS` | `AaMappingRequest_TargetFailureDets` |  |  |  |
| 17 | `AA.MAPR.RESERVED.4` | `AaMappingRequest_Reserved4` | TField |  |  |
| 18 | `AA.MAPR.RESERVED.3` | `AaMappingRequest_Reserved3` | TField |  |  |
| 19 | `AA.MAPR.RESERVED.2` | `AaMappingRequest_Reserved2` | TField |  |  |
| 20 | `AA.MAPR.RESERVED.1` | `AaMappingRequest_Reserved1` | TField |  |  |
| 21 | `AA.MAPR.LOCAL.REF` | `AaMappingRequest_LocalRef` |  |  |  |
| 22 | `AA.MAPR.OVERRIDE` | `AaMappingRequest_Override` |  |  |  |
| 23 | `AA.MAPR.RECORD.STATUS` | `AaMappingRequest_RecordStatus` | String |  |  |
| 24 | `AA.MAPR.CURR.NO` | `AaMappingRequest_CurrNo` | String |  |  |
| 25 | `AA.MAPR.INPUTTER` | `AaMappingRequest_Inputter` |  |  |  |
| 26 | `AA.MAPR.DATE.TIME` | `AaMappingRequest_DateTime` |  |  |  |
| 27 | `AA.MAPR.AUTHORISER` | `AaMappingRequest_Authoriser` | String |  |  |
| 28 | `AA.MAPR.CO.CODE` | `AaMappingRequest_CoCode` | String |  |  |
| 29 | `AA.MAPR.DEPT.CODE` | `AaMappingRequest_DeptCode` | String |  |  |
| 30 | `AA.MAPR.AUDITOR.CODE` | `AaMappingRequest_AuditorCode` | String |  |  |
| 31 | `AA.MAPR.AUDIT.DATE.TIME` | `AaMappingRequest_AuditDateTime` | String |  |  |
| 32 | `AA.MAPR.ACTIVITY` | `AaMappingRequest_Activity` | TField | Yes | This field defines the activity to be processed against Mapping Request. 1. Input in this field should be valid record under AA.CLASS.TYPE.ACTIVITY.CLASS application. 2. Input is mandatory in this field to commit the new mapping request. 3. System will defaults the RETRY.REQUEST activity when creating the new error log record under this application. |
