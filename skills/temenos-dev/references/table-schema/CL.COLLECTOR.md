# CL.COLLECTOR — Table Schema

> Source: `INSERTS/I_F.CL.COLLECTOR` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.COLL.COLLECTOR.TYPE` | `ClCollector_CollectorType` | TField |  | Type of Collector (CL.COLLECTOR.TYPE). |
| 2 | `CL.COLL.COLLECTOR.USER` | `ClCollector_CollectorUser` | TField |  | System user to be linked to this collector ID. |
| 3 | `CL.COLL.INCENTIVE.STRATEGY` | `ClCollector_IncentiveStrategy` | TField |  | The strategy of incentive to be applied for this collector. (CL.INCENTIVE.STRATEGY). |
| 4 | `CL.COLL.ASSIGNED.QUEUES` | `ClCollector_AssignedQueues` |  |  |  |
| 5 | `CL.COLL.HOME.PHONE` | `ClCollector_HomePhone` | TField |  | Collector home phone number. |
| 6 | `CL.COLL.MOBILE.PHONE` | `ClCollector_MobilePhone` | TField |  |  |
| 7 | `CL.COLL.LOCAL.REF` | `ClCollector_LocalRef` |  |  |  |
| 8 | `CL.COLL.RESERVED.5` | `ClCollector_Reserved5` | TField |  |  |
| 9 | `CL.COLL.RESERVED.4` | `ClCollector_Reserved4` | TField |  |  |
| 10 | `CL.COLL.RESERVED.3` | `ClCollector_Reserved3` | TField |  |  |
| 11 | `CL.COLL.RESERVED.2` | `ClCollector_Reserved2` | TField |  |  |
| 12 | `CL.COLL.RESERVED.1` | `ClCollector_Reserved1` | TField |  |  |
| 13 | `CL.COLL.RECORD.STATUS` | `ClCollector_RecordStatus` | String |  |  |
| 14 | `CL.COLL.CURR.NO` | `ClCollector_CurrNo` | String |  |  |
| 15 | `CL.COLL.INPUTTER` | `ClCollector_Inputter` |  |  |  |
| 16 | `CL.COLL.DATE.TIME` | `ClCollector_DateTime` |  |  |  |
| 17 | `CL.COLL.AUTHORISER` | `ClCollector_Authoriser` | String |  |  |
| 18 | `CL.COLL.CO.CODE` | `ClCollector_CoCode` | String |  |  |
| 19 | `CL.COLL.DEPT.CODE` | `ClCollector_DeptCode` | String |  |  |
| 20 | `CL.COLL.AUDITOR.CODE` | `ClCollector_AuditorCode` | String |  |  |
| 21 | `CL.COLL.AUDIT.DATE.TIME` | `ClCollector_AuditDateTime` | String |  |  |
