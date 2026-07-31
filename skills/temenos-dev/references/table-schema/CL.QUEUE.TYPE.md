# CL.QUEUE.TYPE — Table Schema

> Source: `INSERTS/I_F.CL.QUEUE.TYPE` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.QT.DESCRIPTION` | `ClQueueType_Description` |  |  |  |
| 2 | `CL.QT.EXTNL.INTL` | `ClQueueType_ExtnlIntl` | TField |  | To indicate whether the queue type is handled by external or internal collectors. |
| 3 | `CL.QT.LOCAL.REF` | `ClQueueType_LocalRef` |  |  |  |
| 4 | `CL.QT.RESERVED.5` | `ClQueueType_Reserved5` | TField |  |  |
| 5 | `CL.QT.RESERVED.4` | `ClQueueType_Reserved4` | TField |  |  |
| 6 | `CL.QT.RESERVED.3` | `ClQueueType_Reserved3` | TField |  |  |
| 7 | `CL.QT.RESERVED.2` | `ClQueueType_Reserved2` | TField |  |  |
| 8 | `CL.QT.RESERVED.1` | `ClQueueType_Reserved1` | TField |  |  |
| 9 | `CL.QT.RECORD.STATUS` | `ClQueueType_RecordStatus` | String |  |  |
| 10 | `CL.QT.CURR.NO` | `ClQueueType_CurrNo` | String |  |  |
| 11 | `CL.QT.INPUTTER` | `ClQueueType_Inputter` |  |  |  |
| 12 | `CL.QT.DATE.TIME` | `ClQueueType_DateTime` |  |  |  |
| 13 | `CL.QT.AUTHORISER` | `ClQueueType_Authoriser` | String |  |  |
| 14 | `CL.QT.CO.CODE` | `ClQueueType_CoCode` | String |  |  |
| 15 | `CL.QT.DEPT.CODE` | `ClQueueType_DeptCode` | String |  |  |
| 16 | `CL.QT.AUDITOR.CODE` | `ClQueueType_AuditorCode` | String |  |  |
| 17 | `CL.QT.AUDIT.DATE.TIME` | `ClQueueType_AuditDateTime` | String |  |  |
