# PP.AUTO.REPAIR.INSTANCE — Table Schema

> Source: `INSERTS/I_F.PP.AUTO.REPAIR.INSTANCE` in `PP_AutomatedRepairToolService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.ARI.AutoRepairInstanceDesc` | `PpAutoRepairInstance_Autorepairinstancedesc` |  |  |  |
| 2 | `PP.ARI.AutoRepairRequestAPI` | `PpAutoRepairInstance_Autorepairrequestapi` | TField |  |  |
| 3 | `PP.ARI.AutoRepairResponseAPI` | `PpAutoRepairInstance_Autorepairresponseapi` | TField |  |  |
| 4 | `PP.ARI.LOCAL.REF` | `PpAutoRepairInstance_LocalRef` |  |  |  |
| 5 | `PP.ARI.RESERVED.5` | `PpAutoRepairInstance_Reserved5` | TField |  |  |
| 6 | `PP.ARI.RESERVED.4` | `PpAutoRepairInstance_Reserved4` | TField |  |  |
| 7 | `PP.ARI.RESERVED.3` | `PpAutoRepairInstance_Reserved3` | TField |  |  |
| 8 | `PP.ARI.RESERVED.2` | `PpAutoRepairInstance_Reserved2` | TField |  |  |
| 9 | `PP.ARI.RESERVED.1` | `PpAutoRepairInstance_Reserved1` | TField |  |  |
| 10 | `PP.ARI.OVERRIDE` | `PpAutoRepairInstance_Override` |  |  |  |
| 11 | `PP.ARI.RECORD.STATUS` | `PpAutoRepairInstance_RecordStatus` | String |  |  |
| 12 | `PP.ARI.CURR.NO` | `PpAutoRepairInstance_CurrNo` | String |  |  |
| 13 | `PP.ARI.INPUTTER` | `PpAutoRepairInstance_Inputter` |  |  |  |
| 14 | `PP.ARI.DATE.TIME` | `PpAutoRepairInstance_DateTime` |  |  |  |
| 15 | `PP.ARI.AUTHORISER` | `PpAutoRepairInstance_Authoriser` | String |  |  |
| 16 | `PP.ARI.CO.CODE` | `PpAutoRepairInstance_CoCode` | String |  |  |
| 17 | `PP.ARI.DEPT.CODE` | `PpAutoRepairInstance_DeptCode` | String |  |  |
| 18 | `PP.ARI.AUDITOR.CODE` | `PpAutoRepairInstance_AuditorCode` | String |  |  |
| 19 | `PP.ARI.AUDIT.DATE.TIME` | `PpAutoRepairInstance_AuditDateTime` | String |  |  |
