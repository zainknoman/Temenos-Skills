# SEAT.SEQUENCER — Table Schema

> Source: `INSERTS/I_F.SEAT.SEQUENCER` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.SS.SEL.FLD.NAME` | `SeatSequencer_SelFldName` |  |  |  |
| 2 | `SE.SS.SEL.CRITERIA` | `SeatSequencer_SelCriteria` |  |  |  |
| 3 | `SE.SS.BATCH.SIZE` | `SeatSequencer_BatchSize` |  |  |  |
| 4 | `SE.SS.RESERVED.4` | `SeatSequencer_Reserved4` |  |  |  |
| 5 | `SE.SS.RESERVED.3` | `SeatSequencer_Reserved3` |  |  |  |
| 6 | `SE.SS.RESERVED.2` | `SeatSequencer_Reserved2` |  |  |  |
| 7 | `SE.SS.RESERVED.1` | `SeatSequencer_Reserved1` |  |  |  |
| 8 | `SE.SS.RECORD.STATUS` | `SeatSequencer_RecordStatus` |  |  |  |
| 9 | `SE.SS.CURR.NO` | `SeatSequencer_CurrNo` |  |  |  |
| 10 | `SE.SS.INPUTTER` | `SeatSequencer_Inputter` |  |  |  |
| 11 | `SE.SS.DATE.TIME` | `SeatSequencer_DateTime` |  |  |  |
| 12 | `SE.SS.AUTHORISER` | `SeatSequencer_Authoriser` |  |  |  |
| 13 | `SE.SS.CO.CODE` | `SeatSequencer_CoCode` |  |  |  |
| 14 | `SE.SS.DEPT.CODE` | `SeatSequencer_DeptCode` |  |  |  |
| 15 | `SE.SS.AUDITOR.CODE` | `SeatSequencer_AuditorCode` |  |  |  |
| 16 | `SE.SS.AUDIT.DATE.TIME` | `SeatSequencer_AuditDateTime` |  |  |  |
