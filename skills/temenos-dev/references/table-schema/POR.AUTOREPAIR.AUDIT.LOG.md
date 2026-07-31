# POR.AUTOREPAIR.AUDIT.LOG — Table Schema

> Source: `INSERTS/I_F.POR.AUTOREPAIR.AUDIT.LOG` in `PP_AutomatedRepairToolService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPARL.CompanyID` | `PorAutorepairAuditLog_Companyid` |  |  |  |
| 2 | `PPARL.FTNumber` | `PorAutorepairAuditLog_Ftnumber` |  |  |  |
| 3 | `PPARL.TableName` | `PorAutorepairAuditLog_Tablename` |  |  |  |
| 4 | `PPARL.RecordID` | `PorAutorepairAuditLog_Recordid` |  |  |  |
| 5 | `PPARL.FieldName` | `PorAutorepairAuditLog_Fieldname` |  |  |  |
| 6 | `PPARL.OldValue` | `PorAutorepairAuditLog_Oldvalue` |  |  |  |
| 7 | `PPARL.NewValue` | `PorAutorepairAuditLog_Newvalue` |  |  |  |
| 8 | `PPARL.FileReference` | `PorAutorepairAuditLog_Filereference` |  |  |  |
