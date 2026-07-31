# SASIMA.MAPPING — Table Schema

> Source: `INSERTS/I_F.SASIMA.MAPPING` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.SI.SASIMA.CODE` | `SasimaMapping_SasimaCode` |  |  |  |
| 2 | `SA.SI.SASIMA.DESC` | `SasimaMapping_SasimaDesc` |  |  |  |
| 3 | `SA.SI.T24.CODE` | `SasimaMapping_T24Code` |  |  |  |
| 4 | `SA.SI.T24.DESC` | `SasimaMapping_T24Desc` |  |  |  |
| 5 | `SA.SI.RECORD.STATUS` | `SasimaMapping_RecordStatus` | String |  |  |
| 6 | `SA.SI.CURR.NO` | `SasimaMapping_CurrNo` | String |  |  |
| 7 | `SA.SI.INPUTTER` | `SasimaMapping_Inputter` |  |  |  |
| 8 | `SA.SI.DATE.TIME` | `SasimaMapping_DateTime` |  |  |  |
| 9 | `SA.SI.AUTHORISER` | `SasimaMapping_Authoriser` | String |  |  |
| 10 | `SA.SI.CO.CODE` | `SasimaMapping_CoCode` | String |  |  |
| 11 | `SA.SI.DEPT.CODE` | `SasimaMapping_DeptCode` | String |  |  |
| 12 | `SA.SI.AUDITOR.CODE` | `SasimaMapping_AuditorCode` | String |  |  |
| 13 | `SA.SI.AUDIT.DATE.TIME` | `SasimaMapping_AuditDateTime` | String |  |  |
