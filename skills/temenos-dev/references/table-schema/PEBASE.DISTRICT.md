# PEBASE.DISTRICT — Table Schema

> Source: `INSERTS/I_F.PEBASE.DISTRICT` in `PEBASE_CustomerCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PEBASE.DIST.DISTRICT` | `PebaseDistrict_District` | TField |  | Contains the description of the District |
| 2 | `PEBASE.DIST.PROVINCE` | `PebaseDistrict_Province` | TField |  | Contains the first 4 characters of the ID. This should be a valid PEBASE.PROVINCE ID |
| 3 | `PEBASE.DIST.DEPARTMENT` | `PebaseDistrict_Department` | TField |  | Contains the first 2 characters of the ID. This should be a valid PEBASE.DEPARTMENT ID |
| 4 | `PEBASE.DIST.RESERVED.5` | `PebaseDistrict_Reserved5` | TField |  | Field for future use. |
| 5 | `PEBASE.DIST.RESERVED.4` | `PebaseDistrict_Reserved4` | TField |  | Field for future use. |
| 6 | `PEBASE.DIST.RESERVED.3` | `PebaseDistrict_Reserved3` | TField |  | Field for future use. |
| 7 | `PEBASE.DIST.RESERVED.2` | `PebaseDistrict_Reserved2` | TField |  | Field for future use. |
| 8 | `PEBASE.DIST.RESERVED.1` | `PebaseDistrict_Reserved1` | TField |  | Field for future use. |
| 9 | `PEBASE.DIST.LOCAL.REF` | `PebaseDistrict_LocalRef` |  |  |  |
| 10 | `PEBASE.DIST.OVERRIDE` | `PebaseDistrict_Override` |  |  |  |
| 11 | `PEBASE.DIST.RECORD.STATUS` | `PebaseDistrict_RecordStatus` | String |  |  |
| 12 | `PEBASE.DIST.CURR.NO` | `PebaseDistrict_CurrNo` | String |  |  |
| 13 | `PEBASE.DIST.INPUTTER` | `PebaseDistrict_Inputter` |  |  |  |
| 14 | `PEBASE.DIST.DATE.TIME` | `PebaseDistrict_DateTime` |  |  |  |
| 15 | `PEBASE.DIST.AUTHORISER` | `PebaseDistrict_Authoriser` | String |  |  |
| 16 | `PEBASE.DIST.CO.CODE` | `PebaseDistrict_CoCode` | String |  |  |
| 17 | `PEBASE.DIST.DEPT.CODE` | `PebaseDistrict_DeptCode` | String |  |  |
| 18 | `PEBASE.DIST.AUDITOR.CODE` | `PebaseDistrict_AuditorCode` | String |  |  |
| 19 | `PEBASE.DIST.AUDIT.DATE.TIME` | `PebaseDistrict_AuditDateTime` | String |  |  |
