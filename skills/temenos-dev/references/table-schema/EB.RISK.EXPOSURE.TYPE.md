# EB.RISK.EXPOSURE.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.RISK.EXPOSURE.TYPE` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.RI.EXP.DESCRIPTION` | `EbRiskExposureType_Description` |  |  |  |
| 2 | `EB.RI.EXP.RESERVED05` | `EbRiskExposureType_Reserved05` |  |  |  |
| 3 | `EB.RI.EXP.RESERVED04` | `EbRiskExposureType_Reserved04` |  |  |  |
| 4 | `EB.RI.EXP.RESERVED03` | `EbRiskExposureType_Reserved03` |  |  |  |
| 5 | `EB.RI.EXP.RESERVED02` | `EbRiskExposureType_Reserved02` |  |  |  |
| 6 | `EB.RI.EXP.RESERVED01` | `EbRiskExposureType_Reserved01` |  |  |  |
| 7 | `EB.RI.EXP.RECORD.STATUS` | `EbRiskExposureType_RecordStatus` | String |  |  |
| 8 | `EB.RI.EXP.CURR.NO` | `EbRiskExposureType_CurrNo` | String |  |  |
| 9 | `EB.RI.EXP.INPUTTER` | `EbRiskExposureType_Inputter` |  |  |  |
| 10 | `EB.RI.EXP.DATE.TIME` | `EbRiskExposureType_DateTime` |  |  |  |
| 11 | `EB.RI.EXP.AUTHORISER` | `EbRiskExposureType_Authoriser` | String |  |  |
| 12 | `EB.RI.EXP.CO.CODE` | `EbRiskExposureType_CoCode` | String |  |  |
| 13 | `EB.RI.EXP.DEPT.CODE` | `EbRiskExposureType_DeptCode` | String |  |  |
| 14 | `EB.RI.EXP.AUDITOR.CODE` | `EbRiskExposureType_AuditorCode` | String |  |  |
| 15 | `EB.RI.EXP.AUDIT.DATE.TIME` | `EbRiskExposureType_AuditDateTime` | String |  |  |
