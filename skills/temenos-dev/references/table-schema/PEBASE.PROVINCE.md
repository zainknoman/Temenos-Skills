# PEBASE.PROVINCE — Table Schema

> Source: `INSERTS/I_F.PEBASE.PROVINCE` in `PEBASE_CustomerCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PEBASE.PROV.PROVINCE` | `PebaseProvince_Province` | TField |  | Contains the Province Name. |
| 2 | `PEBASE.PROV.DEPARTMENT` | `PebaseProvince_Department` | TField |  | Contains the first 2 characters of the ID. This should be a valid PEBASE.DEPARTMENT ID |
| 3 | `PEBASE.PROV.RESERVED.5` | `PebaseProvince_Reserved5` | TField |  | Field for future use. |
| 4 | `PEBASE.PROV.RESERVED.4` | `PebaseProvince_Reserved4` | TField |  | Field for future use. |
| 5 | `PEBASE.PROV.RESERVED.3` | `PebaseProvince_Reserved3` | TField |  | Field for future use. |
| 6 | `PEBASE.PROV.RESERVED.2` | `PebaseProvince_Reserved2` | TField |  | Field for future use. |
| 7 | `PEBASE.PROV.RESERVED.1` | `PebaseProvince_Reserved1` | TField |  | Field for future use. |
| 8 | `PEBASE.PROV.LOCAL.REF` | `PebaseProvince_LocalRef` |  |  |  |
| 9 | `PEBASE.PROV.OVERRIDE` | `PebaseProvince_Override` |  |  |  |
| 10 | `PEBASE.PROV.RECORD.STATUS` | `PebaseProvince_RecordStatus` | String |  |  |
| 11 | `PEBASE.PROV.CURR.NO` | `PebaseProvince_CurrNo` | String |  |  |
| 12 | `PEBASE.PROV.INPUTTER` | `PebaseProvince_Inputter` |  |  |  |
| 13 | `PEBASE.PROV.DATE.TIME` | `PebaseProvince_DateTime` |  |  |  |
| 14 | `PEBASE.PROV.AUTHORISER` | `PebaseProvince_Authoriser` | String |  |  |
| 15 | `PEBASE.PROV.CO.CODE` | `PebaseProvince_CoCode` | String |  |  |
| 16 | `PEBASE.PROV.DEPT.CODE` | `PebaseProvince_DeptCode` | String |  |  |
| 17 | `PEBASE.PROV.AUDITOR.CODE` | `PebaseProvince_AuditorCode` | String |  |  |
| 18 | `PEBASE.PROV.AUDIT.DATE.TIME` | `PebaseProvince_AuditDateTime` | String |  |  |
