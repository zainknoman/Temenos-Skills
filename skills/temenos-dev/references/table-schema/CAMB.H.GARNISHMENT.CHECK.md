# CAMB.H.GARNISHMENT.CHECK — Table Schema

> Source: `INSERTS/I_F.CAMB.H.GARNISHMENT.CHECK` in `CABASE_AMLInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.GC.NAME.RANGE` | `CambHGarnishmentCheck_NameRange` | TField |  | This field is used to define the name range for garnishment check. Allowed values are 5 alphanumeric character. Validation - If the field is defined with value, then system will check the GRN.CHK.FIELD EQ NAME, if matches then system will valudated as per the value define while creating customer record. |
| 2 | `CAMB.GC.GRN.CHK.FIELD` | `CambHGarnishmentCheck_GrnChkField` |  |  |  |
| 3 | `CAMB.GC.RESERVED.2` | `CambHGarnishmentCheck_Reserved2` | TField |  |  |
| 4 | `CAMB.GC.RESERVED.3` | `CambHGarnishmentCheck_Reserved3` | TField |  |  |
| 5 | `CAMB.GC.RESERVED.4` | `CambHGarnishmentCheck_Reserved4` | TField |  |  |
| 6 | `CAMB.GC.RESERVED.5` | `CambHGarnishmentCheck_Reserved5` | TField |  |  |
| 7 | `CAMB.GC.RECORD.STATUS` | `CambHGarnishmentCheck_RecordStatus` | String |  |  |
| 8 | `CAMB.GC.CURR.NO` | `CambHGarnishmentCheck_CurrNo` | String |  |  |
| 9 | `CAMB.GC.INPUTTER` | `CambHGarnishmentCheck_Inputter` |  |  |  |
| 10 | `CAMB.GC.DATE.TIME` | `CambHGarnishmentCheck_DateTime` |  |  |  |
| 11 | `CAMB.GC.AUTHORISER` | `CambHGarnishmentCheck_Authoriser` | String |  |  |
| 12 | `CAMB.GC.CO.CODE` | `CambHGarnishmentCheck_CoCode` | String |  |  |
| 13 | `CAMB.GC.DEPT.CODE` | `CambHGarnishmentCheck_DeptCode` | String |  |  |
| 14 | `CAMB.GC.AUDITOR.CODE` | `CambHGarnishmentCheck_AuditorCode` | String |  |  |
| 15 | `CAMB.GC.AUDIT.DATE.TIME` | `CambHGarnishmentCheck_AuditDateTime` | String |  |  |
