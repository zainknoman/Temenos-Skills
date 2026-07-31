# CAMB.TELPAY.STOP.PYMT.LIST — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.STOP.PYMT.LIST` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TP.SPYMT.NOTE.TYPE` | `CambTelpayStopPymtList_NoteType` |  |  |  |
| 2 | `CAMB.TP.SPYMT.NOTE.ACTYPE` | `CambTelpayStopPymtList_NoteActype` |  |  |  |
| 3 | `CAMB.TP.SPYMT.NOTE.ACNO` | `CambTelpayStopPymtList_NoteAcno` |  |  |  |
| 4 | `CAMB.TP.SPYMT.NOTE.AMOUNT` | `CambTelpayStopPymtList_NoteAmount` |  |  |  |
| 5 | `CAMB.TP.SPYMT.NOTE.EFDATE` | `CambTelpayStopPymtList_NoteEfdate` |  |  |  |
| 6 | `CAMB.TP.SPYMT.NOTE.EXPDATE` | `CambTelpayStopPymtList_NoteExpdate` |  |  |  |
| 7 | `CAMB.TP.SPYMT.NOTE.TXN.TYPE` | `CambTelpayStopPymtList_NoteTxnType` |  |  |  |
| 8 | `CAMB.TP.SPYMT.NOTE.LINE1` | `CambTelpayStopPymtList_NoteLine1` |  |  |  |
| 9 | `CAMB.TP.SPYMT.NOTE.LINE2` | `CambTelpayStopPymtList_NoteLine2` |  |  |  |
| 10 | `CAMB.TP.SPYMT.NOTE.LINE3` | `CambTelpayStopPymtList_NoteLine3` |  |  |  |
| 11 | `CAMB.TP.SPYMT.NOTE.CHQDATE` | `CambTelpayStopPymtList_NoteChqdate` |  |  |  |
| 12 | `CAMB.TP.SPYMT.NOTE.CHQAMT` | `CambTelpayStopPymtList_NoteChqamt` |  |  |  |
| 13 | `CAMB.TP.SPYMT.NOTE.FIRST.CHQNO` | `CambTelpayStopPymtList_NoteFirstChqno` |  |  |  |
| 14 | `CAMB.TP.SPYMT.NOTE.LAST.CHQNO` | `CambTelpayStopPymtList_NoteLastChqno` |  |  |  |
| 15 | `CAMB.TP.SPYMT.NOTE.OVERRIDE` | `CambTelpayStopPymtList_NoteOverride` |  |  |  |
