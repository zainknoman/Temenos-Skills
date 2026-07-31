# CONDITION.PRIORITY — Table Schema

> Source: `INSERTS/I_F.CONDITION.PRIORITY` in `ST_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CPR.DESCRIPTION` | `ConditionPriority_Description` |  |  |  |
| 2 | `EB.CPR.APPS.ALLOWED` | `ConditionPriority_AppsAllowed` |  |  |  |
| 3 | `EB.CPR.PRIORITY.ITEM` | `ConditionPriority_PriorityItem` |  |  |  |
| 4 | `EB.CPR.PRTY.VALIDATION` | `ConditionPriority_PrtyValidation` |  |  |  |
| 5 | `EB.CPR.GEN.COND.KEEP` | `ConditionPriority_GenCondKeep` |  |  |  |
| 6 | `EB.CPR.GROUP.COND.KEEP` | `ConditionPriority_GroupCondKeep` |  |  |  |
| 7 | `EB.CPR.OVERRIDE` | `ConditionPriority_Override` |  |  |  |
| 8 | `EB.CPR.RECORD.STATUS` | `ConditionPriority_RecordStatus` | String |  |  |
| 9 | `EB.CPR.CURR.NO` | `ConditionPriority_CurrNo` | String |  |  |
| 10 | `EB.CPR.INPUTTER` | `ConditionPriority_Inputter` |  |  |  |
| 11 | `EB.CPR.DATE.TIME` | `ConditionPriority_DateTime` |  |  |  |
| 12 | `EB.CPR.AUTHORISER` | `ConditionPriority_Authoriser` | String |  |  |
| 13 | `EB.CPR.CO.CODE` | `ConditionPriority_CoCode` | String |  |  |
| 14 | `EB.CPR.DEPT.CODE` | `ConditionPriority_DeptCode` | String |  |  |
| 15 | `EB.CPR.AUDITOR.CODE` | `ConditionPriority_AuditorCode` | String |  |  |
| 16 | `EB.CPR.AUDIT.DATE.TIME` | `ConditionPriority_AuditDateTime` | String |  |  |
| 17 | `EB.CPR.REBUILD.CUSTOMER.CHG` | `ConditionPriority_RebuildCustomerChg` | TField |  | Field to indicate whether CUSTOMER.CHARGE record needs to be rebuild online or not Allowed options: CUSTOMER - This option allows CUSTOMER.CHARGE to be updated Online based on latest data from CUSTOMER, FCSI and QCSI tables as applicable When CONDITION.PRIORITY&gt;TAX record is configured with FCSI and QCSI related priority items, creation or update of FCSI and QCSI (as applicable) based on Customer data is also handled Online during CUSTOMER processing and direct amendments of FCSI or QCSI table may also trigger rebuilding of CUSTOMER.CHARGE online When left blank, system will continue to rebuild CUSTOMER.CHARGE based on CUSTOMER.ACT or CONDITION.PRIORITY definition changes in COB Validation Rules: Field Input allowed only when the current record key is SYSTEM |
