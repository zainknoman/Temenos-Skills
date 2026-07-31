# TC.SERVICES — Table Schema

> Source: `INSERTS/I_F.TC.SERVICES` in `AO_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TC.SVC.DESCRIPTION` | `TcServices_Description` |  |  |  |
| 2 | `TC.SVC.MANDATORY.SVC` | `TcServices_MandatorySvc` | TField | Yes | This field is used to define if the service is mandatory or not. Possible values: Null / Yes Validation rules: Throw error when Mandatory Service is set to Yes and all Mandatory Operations are set to No |
| 3 | `TC.SVC.OPERATION` | `TcServices_Operation` |  |  |  |
| 4 | `TC.SVC.OPERATION.DESC` | `TcServices_OperationDesc` |  |  |  |
| 5 | `TC.SVC.MANDATORY.OPS` | `TcServices_MandatoryOps` |  |  |  |
| 6 | `TC.SVC.RECORD.TYPE` | `TcServices_RecordType` |  |  |  |
| 7 | `TC.SVC.RECORD.NAME` | `TcServices_RecordName` |  |  |  |
| 8 | `TC.SVC.RESTRICTION` | `TcServices_Restriction` |  |  |  |
| 9 | `TC.SVC.DEPENDENT.SVC` | `TcServices_DependentSvc` |  |  |  |
| 10 | `TC.SVC.DEPENDENT.OPS` | `TcServices_DependentOps` |  |  |  |
| 11 | `TC.SVC.USER.SMS.GROUP` | `TcServices_UserSmsGroup` | TField |  | USER SMS Group restriction to be applied for this TC.SERVICES record. During runtime USER.SMS.GROUP is assigned to the external user request dynamically based on the Privilege Check configuration in CHANNEL.PARAMETER record. Validation rules: Valid record ID in USER.SMS.GROUP application Up to 35 alphanumeric characters |
| 12 | `TC.SVC.AUTO.GEN.SMS.GRP` | `TcServices_AutoGenSmsGrp` | TField |  |  |
| 13 | `TC.SVC.LOCAL.REF` | `TcServices_LocalRef` |  |  |  |
| 14 | `TC.SVC.OVERRIDE` | `TcServices_Override` |  |  |  |
| 15 | `TC.SVC.SV.RESERVED.5` | `TcServices_SvReserved5` |  |  |  |
| 16 | `TC.SVC.SV.RESERVED.4` | `TcServices_SvReserved4` |  |  |  |
| 17 | `TC.SVC.SV.RESERVED.3` | `TcServices_SvReserved3` |  |  |  |
| 18 | `TC.SVC.SV.RESERVED.2` | `TcServices_SvReserved2` |  |  |  |
| 19 | `TC.SVC.SV.RESERVED.1` | `TcServices_SvReserved1` |  |  |  |
| 20 | `TC.SVC.RESERVED.5` | `TcServices_Reserved5` | TField |  |  |
| 21 | `TC.SVC.RESERVED.4` | `TcServices_Reserved4` | TField |  |  |
| 22 | `TC.SVC.RESERVED.3` | `TcServices_Reserved3` | TField |  |  |
| 23 | `TC.SVC.RESERVED.2` | `TcServices_Reserved2` | TField |  |  |
| 24 | `TC.SVC.RESERVED.1` | `TcServices_Reserved1` | TField |  |  |
| 25 | `TC.SVC.RECORD.STATUS` | `TcServices_RecordStatus` | String |  |  |
| 26 | `TC.SVC.CURR.NO` | `TcServices_CurrNo` | String |  |  |
| 27 | `TC.SVC.INPUTTER` | `TcServices_Inputter` |  |  |  |
| 28 | `TC.SVC.DATE.TIME` | `TcServices_DateTime` |  |  |  |
| 29 | `TC.SVC.AUTHORISER` | `TcServices_Authoriser` | String |  |  |
| 30 | `TC.SVC.CO.CODE` | `TcServices_CoCode` | String |  |  |
| 31 | `TC.SVC.DEPT.CODE` | `TcServices_DeptCode` | String |  |  |
| 32 | `TC.SVC.AUDITOR.CODE` | `TcServices_AuditorCode` | String |  |  |
| 33 | `TC.SVC.AUDIT.DATE.TIME` | `TcServices_AuditDateTime` | String |  |  |
