# RLGAAP.ROLLING.BAL — Table Schema

> Source: `INSERTS/I_F.RLGAAP.ROLLING.BAL` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ROLL.ROLLING.BAL` | `RlgaapRollingBal_RollingBal` |  |  |  |
| 2 | `ROLL.RECORD.STATUS` | `RlgaapRollingBal_RecordStatus` | String |  |  |
| 3 | `ROLL.CURR.NO` | `RlgaapRollingBal_CurrNo` | String |  |  |
| 4 | `ROLL.INPUTTER` | `RlgaapRollingBal_Inputter` |  |  |  |
| 5 | `ROLL.DATE.TIME` | `RlgaapRollingBal_DateTime` |  |  |  |
| 6 | `ROLL.AUTHORISER` | `RlgaapRollingBal_Authoriser` | String |  |  |
| 7 | `ROLL.CO.CODE` | `RlgaapRollingBal_CoCode` | String |  |  |
| 8 | `ROLL.DEPT.CODE` | `RlgaapRollingBal_DeptCode` | String |  |  |
| 9 | `ROLL.AUDITOR.CODE` | `RlgaapRollingBal_AuditorCode` | String |  |  |
| 10 | `ROLL.AUDIT.DATE.TIME` | `RlgaapRollingBal_AuditDateTime` | String |  |  |
