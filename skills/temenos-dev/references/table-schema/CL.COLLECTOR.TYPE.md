# CL.COLLECTOR.TYPE — Table Schema

> Source: `INSERTS/I_F.CL.COLLECTOR.TYPE` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.CTYPE.DESCRIPTION` | `ClCollectorType_Description` |  |  |  |
| 2 | `CL.CTYPE.INT.EXT.FLG` | `ClCollectorType_IntExtFlg` | TField |  | Whether this collector type is internal or external to the bank. Validation Rules: I for Internal, E for External. |
| 3 | `CL.CTYPE.QUEUE.TYPE` | `ClCollectorType_QueueType` |  |  |  |
| 4 | `CL.CTYPE.MAIN.ACTION` | `ClCollectorType_MainAction` |  |  |  |
| 5 | `CL.CTYPE.LOCAL.REF` | `ClCollectorType_LocalRef` |  |  |  |
| 6 | `CL.CTYPE.RESERVED.5` | `ClCollectorType_Reserved5` | TField |  |  |
| 7 | `CL.CTYPE.RESERVED.4` | `ClCollectorType_Reserved4` | TField |  |  |
| 8 | `CL.CTYPE.RESERVED.3` | `ClCollectorType_Reserved3` | TField |  |  |
| 9 | `CL.CTYPE.RESERVED.2` | `ClCollectorType_Reserved2` | TField |  |  |
| 10 | `CL.CTYPE.RESERVED.1` | `ClCollectorType_Reserved1` | TField |  |  |
| 11 | `CL.CTYPE.RECORD.STATUS` | `ClCollectorType_RecordStatus` | String |  |  |
| 12 | `CL.CTYPE.CURR.NO` | `ClCollectorType_CurrNo` | String |  |  |
| 13 | `CL.CTYPE.INPUTTER` | `ClCollectorType_Inputter` |  |  |  |
| 14 | `CL.CTYPE.DATE.TIME` | `ClCollectorType_DateTime` |  |  |  |
| 15 | `CL.CTYPE.AUTHORISER` | `ClCollectorType_Authoriser` | String |  |  |
| 16 | `CL.CTYPE.CO.CODE` | `ClCollectorType_CoCode` | String |  |  |
| 17 | `CL.CTYPE.DEPT.CODE` | `ClCollectorType_DeptCode` | String |  |  |
| 18 | `CL.CTYPE.AUDITOR.CODE` | `ClCollectorType_AuditorCode` | String |  |  |
| 19 | `CL.CTYPE.AUDIT.DATE.TIME` | `ClCollectorType_AuditDateTime` | String |  |  |
