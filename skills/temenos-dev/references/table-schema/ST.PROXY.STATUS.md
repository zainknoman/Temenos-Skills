# ST.PROXY.STATUS — Table Schema

> Source: `INSERTS/I_F.ST.PROXY.STATUS` in `ST_AliasManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.PRS.DESCRIPTION` | `StProxyStatus_Description` |  |  |  |
| 2 | `ST.PRS.INDICATOR` | `StProxyStatus_Indicator` |  |  |  |
| 3 | `ST.PRS.NEXT.STATUS` | `StProxyStatus_NextStatus` |  |  |  |
| 4 | `ST.PRS.NEXT.STATUS.API` | `StProxyStatus_NextStatusApi` |  |  |  |
| 5 | `ST.PRS.RESERVED05` | `StProxyStatus_Reserved05` | TField |  |  |
| 6 | `ST.PRS.RESERVED04` | `StProxyStatus_Reserved04` | TField |  |  |
| 7 | `ST.PRS.RESERVED03` | `StProxyStatus_Reserved03` | TField |  |  |
| 8 | `ST.PRS.RESERVED02` | `StProxyStatus_Reserved02` | TField |  |  |
| 9 | `ST.PRS.RESERVED01` | `StProxyStatus_Reserved01` | TField |  |  |
| 10 | `ST.PRS.LOCAL.REF` | `StProxyStatus_LocalRef` |  |  |  |
| 11 | `ST.PRS.OVERRIDE` | `StProxyStatus_Override` |  |  |  |
| 12 | `ST.PRS.RECORD.STATUS` | `StProxyStatus_RecordStatus` | String |  |  |
| 13 | `ST.PRS.CURR.NO` | `StProxyStatus_CurrNo` | String |  |  |
| 14 | `ST.PRS.INPUTTER` | `StProxyStatus_Inputter` |  |  |  |
| 15 | `ST.PRS.DATE.TIME` | `StProxyStatus_DateTime` |  |  |  |
| 16 | `ST.PRS.AUTHORISER` | `StProxyStatus_Authoriser` | String |  |  |
| 17 | `ST.PRS.CO.CODE` | `StProxyStatus_CoCode` | String |  |  |
| 18 | `ST.PRS.DEPT.CODE` | `StProxyStatus_DeptCode` | String |  |  |
| 19 | `ST.PRS.AUDITOR.CODE` | `StProxyStatus_AuditorCode` | String |  |  |
| 20 | `ST.PRS.AUDIT.DATE.TIME` | `StProxyStatus_AuditDateTime` | String |  |  |
