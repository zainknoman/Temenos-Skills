# SEPA.MISMATCH.FILES — Table Schema

> Source: `INSERTS/I_F.SEPA.MISMATCH.FILES` in `EP_InwardProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEP.MIS.FILE.NAME` | `SepaMismatchFiles_FileName` |  |  |  |
| 2 | `SEP.MIS.STP.STATUS` | `SepaMismatchFiles_StpStatus` |  |  |  |
| 3 | `SEP.MIS.RECORD.STATUS` | `SepaMismatchFiles_RecordStatus` | String |  |  |
| 4 | `SEP.MIS.CURR.NO` | `SepaMismatchFiles_CurrNo` | String |  |  |
| 5 | `SEP.MIS.INPUTTER` | `SepaMismatchFiles_Inputter` |  |  |  |
| 6 | `SEP.MIS.DATE.TIME` | `SepaMismatchFiles_DateTime` |  |  |  |
| 7 | `SEP.MIS.AUTHORISER` | `SepaMismatchFiles_Authoriser` | String |  |  |
| 8 | `SEP.MIS.CO.CODE` | `SepaMismatchFiles_CoCode` | String |  |  |
| 9 | `SEP.MIS.DEPT.CODE` | `SepaMismatchFiles_DeptCode` | String |  |  |
| 10 | `SEP.MIS.AUDITOR.CODE` | `SepaMismatchFiles_AuditorCode` | String |  |  |
| 11 | `SEP.MIS.AUDIT.DATE.TIME` | `SepaMismatchFiles_AuditDateTime` | String |  |  |
