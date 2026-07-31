# LKWHTX.CUSTOMER.THRESHOLD.LIMIT — Table Schema

> Source: `INSERTS/I_F.LKWHTX.CUSTOMER.THRESHOLD.LIMIT` in `LKWHTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `THRESHOLD.CUSTOMER.THRESHOLD.LIMIT` | `LkwhtxCustomerThresholdLimit_CustomerThresholdLimit` | TField |  |  |
| 2 | `THRESHOLD.RECORD.STATUS` | `LkwhtxCustomerThresholdLimit_RecordStatus` | String |  |  |
| 3 | `THRESHOLD.CURR.NO` | `LkwhtxCustomerThresholdLimit_CurrNo` | String |  |  |
| 4 | `THRESHOLD.INPUTTER` | `LkwhtxCustomerThresholdLimit_Inputter` |  |  |  |
| 5 | `THRESHOLD.DATE.TIME` | `LkwhtxCustomerThresholdLimit_DateTime` |  |  |  |
| 6 | `THRESHOLD.AUTHORISER` | `LkwhtxCustomerThresholdLimit_Authoriser` | String |  |  |
| 7 | `THRESHOLD.CO.CODE` | `LkwhtxCustomerThresholdLimit_CoCode` | String |  |  |
| 8 | `THRESHOLD.DEPT.CODE` | `LkwhtxCustomerThresholdLimit_DeptCode` | String |  |  |
| 9 | `THRESHOLD.AUDITOR.CODE` | `LkwhtxCustomerThresholdLimit_AuditorCode` | String |  |  |
| 10 | `THRESHOLD.AUDIT.DATE.TIME` | `LkwhtxCustomerThresholdLimit_AuditDateTime` | String |  |  |
