# SEAT.IO.DETAIL — Table Schema

> Source: `INSERTS/I_F.SEAT.IO.DETAIL` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.SID.IO.OPERATION` | `SeatIoDetail_IoOperation` |  |  |  |
| 2 | `SE.SID.FILE.NAME` | `SeatIoDetail_FileName` |  |  |  |
| 3 | `SE.SID.RESERVED.10` | `SeatIoDetail_Reserved10` | TField |  |  |
| 4 | `SE.SID.RESERVED.9` | `SeatIoDetail_Reserved9` | TField |  |  |
| 5 | `SE.SID.RESERVED.8` | `SeatIoDetail_Reserved8` | TField |  |  |
| 6 | `SE.SID.RESERVED.7` | `SeatIoDetail_Reserved7` | TField |  |  |
| 7 | `SE.SID.RESERVED.6` | `SeatIoDetail_Reserved6` | TField |  |  |
| 8 | `SE.SID.RESERVED.5` | `SeatIoDetail_Reserved5` | TField |  |  |
| 9 | `SE.SID.RESERVED.4` | `SeatIoDetail_Reserved4` | TField |  |  |
| 10 | `SE.SID.RESERVED.3` | `SeatIoDetail_Reserved3` | TField |  |  |
| 11 | `SE.SID.RESERVED.2` | `SeatIoDetail_Reserved2` | TField |  |  |
| 12 | `SE.SID.RESERVED.1` | `SeatIoDetail_Reserved1` | TField |  |  |
