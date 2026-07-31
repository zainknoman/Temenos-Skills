# CAMB.SL.REPAY.ACT.DETS — Table Schema

> Source: `INSERTS/I_F.CAMB.SL.REPAY.ACT.DETS` in `CASYLN_SyndicatedLending.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.REP.ACT.DET.EFF.DATE` | `CambSlRepayActDets_EffDate` |  |  |  |
| 2 | `SL.REP.ACT.DET.PARTICIPANT.ID` | `CambSlRepayActDets_ParticipantId` |  |  |  |
| 3 | `SL.REP.ACT.DET.FT.REF` | `CambSlRepayActDets_FtRef` |  |  |  |
| 4 | `SL.REP.ACT.DET.PRIN.AMT` | `CambSlRepayActDets_PrinAmt` |  |  |  |
| 5 | `SL.REP.ACT.DET.INT.AMT` | `CambSlRepayActDets_IntAmt` |  |  |  |
| 6 | `SL.REP.ACT.DET.RECORD.STATUS` | `CambSlRepayActDets_RecordStatus` |  |  |  |
| 7 | `SL.REP.ACT.DET.CURR.NO` | `CambSlRepayActDets_CurrNo` |  |  |  |
| 8 | `SL.REP.ACT.DET.INPUTTER` | `CambSlRepayActDets_Inputter` |  |  |  |
| 9 | `SL.REP.ACT.DET.DATE.TIME` | `CambSlRepayActDets_DateTime` |  |  |  |
| 10 | `SL.REP.ACT.DET.AUTHORISER` | `CambSlRepayActDets_Authoriser` |  |  |  |
| 11 | `SL.REP.ACT.DET.CO.CODE` | `CambSlRepayActDets_CoCode` |  |  |  |
| 12 | `SL.REP.ACT.DET.DEPT.CODE` | `CambSlRepayActDets_DeptCode` |  |  |  |
| 13 | `SL.REP.ACT.DET.AUDITOR.CODE` | `CambSlRepayActDets_AuditorCode` |  |  |  |
| 14 | `SL.REP.ACT.DET.AUDIT.DATE.TIME` | `CambSlRepayActDets_AuditDateTime` |  |  |  |
