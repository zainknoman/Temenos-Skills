# CAMB.EFT.RETURNS.SEQ — Table Schema

> Source: `INSERTS/I_F.CAMB.EFT.RETURNS.SEQ` in `CACCPA_ClearingCPA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EFT.RET.SEQ.SEQ.NUMBER` | `CambEftReturnsSeq_SeqNumber` |  |  |  |
| 2 | `EFT.RET.SEQ.RESERVED.6` | `CambEftReturnsSeq_Reserved6` |  |  |  |
| 3 | `EFT.RET.SEQ.RESERVED.5` | `CambEftReturnsSeq_Reserved5` |  |  |  |
| 4 | `EFT.RET.SEQ.RESERVED.4` | `CambEftReturnsSeq_Reserved4` |  |  |  |
| 5 | `EFT.RET.SEQ.RESERVED.3` | `CambEftReturnsSeq_Reserved3` |  |  |  |
| 6 | `EFT.RET.SEQ.RESERVED.2` | `CambEftReturnsSeq_Reserved2` |  |  |  |
| 7 | `EFT.RET.SEQ.RESERVED.1` | `CambEftReturnsSeq_Reserved1` |  |  |  |
| 8 | `EFT.RET.SEQ.RECORD.STATUS` | `CambEftReturnsSeq_RecordStatus` |  |  |  |
| 9 | `EFT.RET.SEQ.CURR.NO` | `CambEftReturnsSeq_CurrNo` |  |  |  |
| 10 | `EFT.RET.SEQ.INPUTTER` | `CambEftReturnsSeq_Inputter` |  |  |  |
| 11 | `EFT.RET.SEQ.DATE.TIME` | `CambEftReturnsSeq_DateTime` |  |  |  |
| 12 | `EFT.RET.SEQ.AUTHORISER` | `CambEftReturnsSeq_Authoriser` |  |  |  |
| 13 | `EFT.RET.SEQ.CO.CODE` | `CambEftReturnsSeq_CoCode` |  |  |  |
| 14 | `EFT.RET.SEQ.DEPT.CODE` | `CambEftReturnsSeq_DeptCode` |  |  |  |
| 15 | `EFT.RET.SEQ.AUDITOR.CODE` | `CambEftReturnsSeq_AuditorCode` |  |  |  |
| 16 | `EFT.RET.SEQ.AUDIT.DATE.TIME` | `CambEftReturnsSeq_AuditDateTime` |  |  |  |
