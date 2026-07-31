# LC.DISCREPANCY.CONDITIONS — Table Schema

> Source: `INSERTS/I_F.LC.DISCREPANCY.CONDITIONS` in `LC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LDC.DESCRIPTION` | `LcDiscrepancyConditions_Description` |  |  |  |
| 2 | `LDC.DISCREPANCY.TXT` | `LcDiscrepancyConditions_DiscrepancyTxt` |  |  |  |
| 3 | `LDC.DR.DECIS.FLD` | `LcDiscrepancyConditions_DrDecisFld` |  |  |  |
| 4 | `LDC.DECISION` | `LcDiscrepancyConditions_Decision` |  |  |  |
| 5 | `LDC.LC.DECIS.FLD` | `LcDiscrepancyConditions_LcDecisFld` |  |  |  |
| 6 | `LDC.DISCREPANCY.RTN` | `LcDiscrepancyConditions_DiscrepancyRtn` |  |  |  |
| 7 | `LDC.RECORD.STATUS` | `LcDiscrepancyConditions_RecordStatus` | String |  |  |
| 8 | `LDC.CURR.NO` | `LcDiscrepancyConditions_CurrNo` | String |  |  |
| 9 | `LDC.INPUTTER` | `LcDiscrepancyConditions_Inputter` |  |  |  |
| 10 | `LDC.DATE.TIME` | `LcDiscrepancyConditions_DateTime` |  |  |  |
| 11 | `LDC.AUTHORISER` | `LcDiscrepancyConditions_Authoriser` | String |  |  |
| 12 | `LDC.CO.CODE` | `LcDiscrepancyConditions_CoCode` | String |  |  |
| 13 | `LDC.DEPT.CODE` | `LcDiscrepancyConditions_DeptCode` | String |  |  |
| 14 | `LDC.AUDITOR.CODE` | `LcDiscrepancyConditions_AuditorCode` | String |  |  |
| 15 | `LDC.AUDIT.DATE.TIME` | `LcDiscrepancyConditions_AuditDateTime` | String |  |  |
