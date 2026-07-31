# SE.TEST.FILE.MAPPING — Table Schema

> Source: `INSERTS/I_F.SE.TEST.FILE.MAPPING` in `SE_SeatHeatMap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.TFM.DESCRIPTION` | `SeTestFileMapping_Description` |  |  |  |
| 2 | `SE.TFM.FILE.NAME` | `SeTestFileMapping_FileName` |  |  |  |
| 3 | `SE.TFM.RESERVED.5` | `SeTestFileMapping_Reserved5` | TField |  |  |
| 4 | `SE.TFM.RESERVED.4` | `SeTestFileMapping_Reserved4` | TField |  |  |
| 5 | `SE.TFM.RESERVED.3` | `SeTestFileMapping_Reserved3` | TField |  |  |
| 6 | `SE.TFM.RESERVED.2` | `SeTestFileMapping_Reserved2` | TField |  |  |
| 7 | `SE.TFM.RESERVED.1` | `SeTestFileMapping_Reserved1` | TField |  |  |
| 8 | `SE.TFM.RECORD.STATUS` | `SeTestFileMapping_RecordStatus` | String |  |  |
| 9 | `SE.TFM.CURR.NO` | `SeTestFileMapping_CurrNo` | String |  |  |
| 10 | `SE.TFM.INPUTTER` | `SeTestFileMapping_Inputter` |  |  |  |
| 11 | `SE.TFM.DATE.TIME` | `SeTestFileMapping_DateTime` |  |  |  |
| 12 | `SE.TFM.AUTHORISER` | `SeTestFileMapping_Authoriser` | String |  |  |
| 13 | `SE.TFM.CO.CODE` | `SeTestFileMapping_CoCode` | String |  |  |
| 14 | `SE.TFM.DEPT.CODE` | `SeTestFileMapping_DeptCode` | String |  |  |
| 15 | `SE.TFM.AUDITOR.CODE` | `SeTestFileMapping_AuditorCode` | String |  |  |
| 16 | `SE.TFM.AUDIT.DATE.TIME` | `SeTestFileMapping_AuditDateTime` | String |  |  |
