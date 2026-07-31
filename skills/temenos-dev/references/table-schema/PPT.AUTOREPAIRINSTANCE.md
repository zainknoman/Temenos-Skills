# PPT.AUTOREPAIRINSTANCE — Table Schema

> Source: `INSERTS/I_F.PPT.AUTOREPAIRINSTANCE` in `PP_AutomatedRepairToolService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPARI.AutoRepairInstanceName` | `PptAutorepairinstance_Autorepairinstancename` |  |  |  |
| 2 | `PPARI.AutoRepairInstanceDescription` | `PptAutorepairinstance_Autorepairinstancedescription` |  |  |  |
| 3 | `PPARI.AutoRepairRequestAPI` | `PptAutorepairinstance_Autorepairrequestapi` |  |  |  |
| 4 | `PPARI.AutoRepairResponseAPI` | `PptAutorepairinstance_Autorepairresponseapi` |  |  |  |
| 5 | `PPARI.RACAutoRepairInstance` | `PptAutorepairinstance_Racautorepairinstance` |  |  |  |
| 6 | `PPARI.RSCAutoRepairInstance` | `PptAutorepairinstance_Rscautorepairinstance` |  |  |  |
| 7 | `PPARI.EntryUserID` | `PptAutorepairinstance_Entryuserid` |  |  |  |
| 8 | `PPARI.EntryDateTime` | `PptAutorepairinstance_Entrydatetime` |  |  |  |
| 9 | `PPARI.ApproverUserID` | `PptAutorepairinstance_Approveruserid` |  |  |  |
| 10 | `PPARI.ApprovedDateTime` | `PptAutorepairinstance_Approveddatetime` |  |  |  |
