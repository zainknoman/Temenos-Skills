# RRR.LINKED.APPS — Table Schema

> Source: `INSERTS/I_F.RRR.LINKED.APPS` in `RT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RRR.LI.APPLICATION` | `RrrLinkedApps_Application` |  |  |  |
| 2 | `RRR.LI.RULE.ID` | `RrrLinkedApps_RuleId` |  |  |  |
| 3 | `RRR.LI.CRS.FLAG` | `RrrLinkedApps_CrsFlag` |  |  |  |
| 4 | `RRR.LI.FATCA.FLAG` | `RrrLinkedApps_FatcaFlag` |  |  |  |
| 5 | `RRR.LI.QI.FLAG` | `RrrLinkedApps_QiFlag` |  |  |  |
