# CL.BUCKET.PARAM — Table Schema

> Source: `INSERTS/I_F.CL.BUCKET.PARAM` in `CL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.BUC.PARAM.DESCRIPTION` | `ClBucketParam_Description` |  |  |  |
| 2 | `CL.BUC.PARAM.NO.FROM` | `ClBucketParam_NoFrom` |  |  |  |
| 3 | `CL.BUC.PARAM.NO.TO` | `ClBucketParam_NoTo` |  |  |  |
| 4 | `CL.BUC.PARAM.BUCKET.NO` | `ClBucketParam_BucketNo` |  |  |  |
| 5 | `CL.BUC.PARAM.LOCAL.REF` | `ClBucketParam_LocalRef` |  |  |  |
| 6 | `CL.BUC.PARAM.RESERVED.5` | `ClBucketParam_Reserved5` | TField |  |  |
| 7 | `CL.BUC.PARAM.RESERVED.4` | `ClBucketParam_Reserved4` | TField |  |  |
| 8 | `CL.BUC.PARAM.RESERVED.3` | `ClBucketParam_Reserved3` | TField |  |  |
| 9 | `CL.BUC.PARAM.RESERVED.2` | `ClBucketParam_Reserved2` | TField |  |  |
| 10 | `CL.BUC.PARAM.RESERVED.1` | `ClBucketParam_Reserved1` | TField |  |  |
| 11 | `CL.BUC.PARAM.RECORD.STATUS` | `ClBucketParam_RecordStatus` | String |  |  |
| 12 | `CL.BUC.PARAM.CURR.NO` | `ClBucketParam_CurrNo` | String |  |  |
| 13 | `CL.BUC.PARAM.INPUTTER` | `ClBucketParam_Inputter` |  |  |  |
| 14 | `CL.BUC.PARAM.DATE.TIME` | `ClBucketParam_DateTime` |  |  |  |
| 15 | `CL.BUC.PARAM.AUTHORISER` | `ClBucketParam_Authoriser` | String |  |  |
| 16 | `CL.BUC.PARAM.CO.CODE` | `ClBucketParam_CoCode` | String |  |  |
| 17 | `CL.BUC.PARAM.DEPT.CODE` | `ClBucketParam_DeptCode` | String |  |  |
| 18 | `CL.BUC.PARAM.AUDITOR.CODE` | `ClBucketParam_AuditorCode` | String |  |  |
| 19 | `CL.BUC.PARAM.AUDIT.DATE.TIME` | `ClBucketParam_AuditDateTime` | String |  |  |
