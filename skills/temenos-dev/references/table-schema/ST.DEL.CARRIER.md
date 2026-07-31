# ST.DEL.CARRIER — Table Schema

> Source: `INSERTS/I_F.ST.DEL.CARRIER` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CARR.DESCRIPTION` | `StDelCarrier_Description` | TField |  | This will represent the description of the Carrier. |
| 2 | `ST.CARR.RESERVED.5` | `StDelCarrier_Reserved5` | TField |  |  |
| 3 | `ST.CARR.RESERVED.4` | `StDelCarrier_Reserved4` | TField |  |  |
| 4 | `ST.CARR.RESERVED.3` | `StDelCarrier_Reserved3` | TField |  |  |
| 5 | `ST.CARR.RESERVED.2` | `StDelCarrier_Reserved2` | TField |  |  |
| 6 | `ST.CARR.RESERVED.1` | `StDelCarrier_Reserved1` | TField |  |  |
| 7 | `ST.CARR.LOCAL.REF` | `StDelCarrier_LocalRef` |  |  |  |
| 8 | `ST.CARR.OVERRIDE` | `StDelCarrier_Override` |  |  |  |
| 9 | `ST.CARR.RECORD.STATUS` | `StDelCarrier_RecordStatus` | String |  |  |
| 10 | `ST.CARR.CURR.NO` | `StDelCarrier_CurrNo` | String |  |  |
| 11 | `ST.CARR.INPUTTER` | `StDelCarrier_Inputter` |  |  |  |
| 12 | `ST.CARR.DATE.TIME` | `StDelCarrier_DateTime` |  |  |  |
| 13 | `ST.CARR.AUTHORISER` | `StDelCarrier_Authoriser` | String |  |  |
| 14 | `ST.CARR.CO.CODE` | `StDelCarrier_CoCode` | String |  |  |
| 15 | `ST.CARR.DEPT.CODE` | `StDelCarrier_DeptCode` | String |  |  |
| 16 | `ST.CARR.AUDITOR.CODE` | `StDelCarrier_AuditorCode` | String |  |  |
| 17 | `ST.CARR.AUDIT.DATE.TIME` | `StDelCarrier_AuditDateTime` | String |  |  |
