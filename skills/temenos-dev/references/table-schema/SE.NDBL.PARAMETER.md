# SE.NDBL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SE.NDBL.PARAMETER` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NDBL.PAR.TOTAL.INJECT` | `SeNdblParameter_TotalInject` | TField |  |  |
| 2 | `NDBL.PAR.TOTAL.SELECT.INJECT` | `SeNdblParameter_TotalSelectInject` | TField |  |  |
| 3 | `NDBL.PAR.FATAL.NO` | `SeNdblParameter_FatalNo` | TField |  |  |
| 4 | `NDBL.PAR.FATAL.MOD` | `SeNdblParameter_FatalMod` | TField |  |  |
| 5 | `NDBL.PAR.CONCAT.MOD` | `SeNdblParameter_ConcatMod` | TField |  |  |
| 6 | `NDBL.PAR.NER.PARAMETER` | `SeNdblParameter_NerParameter` | TField |  |  |
| 7 | `NDBL.PAR.RESERVED.04` | `SeNdblParameter_Reserved04` | TField |  |  |
| 8 | `NDBL.PAR.RESERVED.03` | `SeNdblParameter_Reserved03` | TField |  |  |
| 9 | `NDBL.PAR.RESERVED.02` | `SeNdblParameter_Reserved02` | TField |  |  |
| 10 | `NDBL.PAR.RESERVED.01` | `SeNdblParameter_Reserved01` | TField |  |  |
| 11 | `NDBL.PAR.RECORD.STATUS` | `SeNdblParameter_RecordStatus` | String |  |  |
| 12 | `NDBL.PAR.CURR.NO` | `SeNdblParameter_CurrNo` | String |  |  |
| 13 | `NDBL.PAR.INPUTTER` | `SeNdblParameter_Inputter` |  |  |  |
| 14 | `NDBL.PAR.DATE.TIME` | `SeNdblParameter_DateTime` |  |  |  |
| 15 | `NDBL.PAR.AUTHORISER` | `SeNdblParameter_Authoriser` | String |  |  |
| 16 | `NDBL.PAR.CO.CODE` | `SeNdblParameter_CoCode` | String |  |  |
| 17 | `NDBL.PAR.DEPT.CODE` | `SeNdblParameter_DeptCode` | String |  |  |
| 18 | `NDBL.PAR.AUDITOR.CODE` | `SeNdblParameter_AuditorCode` | String |  |  |
| 19 | `NDBL.PAR.AUDIT.DATE.TIME` | `SeNdblParameter_AuditDateTime` | String |  |  |
