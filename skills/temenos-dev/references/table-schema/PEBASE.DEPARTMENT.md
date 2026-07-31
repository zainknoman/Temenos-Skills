# PEBASE.DEPARTMENT — Table Schema

> Source: `INSERTS/I_F.PEBASE.DEPARTMENT` in `PEBASE_CustomerCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PEBASE.DEP.DEPARTMENT` | `PebaseDepartment_Department` | TField |  | Contains the department name of the Postal address. |
| 2 | `PEBASE.DEP.RESERVED.5` | `PebaseDepartment_Reserved5` | TField |  | Field for future use. |
| 3 | `PEBASE.DEP.RESERVED.4` | `PebaseDepartment_Reserved4` | TField |  | Field for future use. |
| 4 | `PEBASE.DEP.RESERVED.3` | `PebaseDepartment_Reserved3` | TField |  | Field for future use. |
| 5 | `PEBASE.DEP.RESERVED.2` | `PebaseDepartment_Reserved2` | TField |  | Field for future use. |
| 6 | `PEBASE.DEP.RESERVED.1` | `PebaseDepartment_Reserved1` | TField |  | Field for future use. |
| 7 | `PEBASE.DEP.LOCAL.REF` | `PebaseDepartment_LocalRef` |  |  |  |
| 8 | `PEBASE.DEP.OVERRIDE` | `PebaseDepartment_Override` |  |  |  |
| 9 | `PEBASE.DEP.RECORD.STATUS` | `PebaseDepartment_RecordStatus` | String |  |  |
| 10 | `PEBASE.DEP.CURR.NO` | `PebaseDepartment_CurrNo` | String |  |  |
| 11 | `PEBASE.DEP.INPUTTER` | `PebaseDepartment_Inputter` |  |  |  |
| 12 | `PEBASE.DEP.DATE.TIME` | `PebaseDepartment_DateTime` |  |  |  |
| 13 | `PEBASE.DEP.AUTHORISER` | `PebaseDepartment_Authoriser` | String |  |  |
| 14 | `PEBASE.DEP.CO.CODE` | `PebaseDepartment_CoCode` | String |  |  |
| 15 | `PEBASE.DEP.DEPT.CODE` | `PebaseDepartment_DeptCode` | String |  |  |
| 16 | `PEBASE.DEP.AUDITOR.CODE` | `PebaseDepartment_AuditorCode` | String |  |  |
| 17 | `PEBASE.DEP.AUDIT.DATE.TIME` | `PebaseDepartment_AuditDateTime` | String |  |  |
