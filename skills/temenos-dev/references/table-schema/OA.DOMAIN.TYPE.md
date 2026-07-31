# OA.DOMAIN.TYPE — Table Schema

> Source: `INSERTS/I_F.OA.DOMAIN.TYPE` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.DT.DESCRIPTION` | `OaDomainType_Description` |  |  |  |
| 2 | `OA.DT.FULL.DESC` | `OaDomainType_FullDesc` |  |  |  |
| 3 | `OA.DT.DOMAIN.CLASS` | `OaDomainType_DomainClass` | TField |  | Indicates the OA.DOMAIN.CLASS to which this Domain type belongs. |
| 4 | `OA.DT.FORMLET.CLASS` | `OaDomainType_FormletClass` |  |  |  |
| 5 | `OA.DT.FORMLET` | `OaDomainType_Formlet` |  |  |  |
| 6 | `OA.DT.MANDATORY` | `OaDomainType_Mandatory` |  |  |  |
| 7 | `OA.DT.RESERVED.10` | `OaDomainType_Reserved10` | TField |  |  |
| 8 | `OA.DT.RESERVED.9` | `OaDomainType_Reserved9` | TField |  |  |
| 9 | `OA.DT.RESERVED.8` | `OaDomainType_Reserved8` | TField |  |  |
| 10 | `OA.DT.RESERVED.7` | `OaDomainType_Reserved7` | TField |  |  |
| 11 | `OA.DT.RESERVED.6` | `OaDomainType_Reserved6` | TField |  |  |
| 12 | `OA.DT.RESERVED.5` | `OaDomainType_Reserved5` | TField |  |  |
| 13 | `OA.DT.RESERVED.4` | `OaDomainType_Reserved4` | TField |  |  |
| 14 | `OA.DT.RESERVED.3` | `OaDomainType_Reserved3` | TField |  |  |
| 15 | `OA.DT.RESERVED.2` | `OaDomainType_Reserved2` | TField |  |  |
| 16 | `OA.DT.RESERVED.1` | `OaDomainType_Reserved1` | TField |  |  |
| 17 | `OA.DT.LOCAL.REF` | `OaDomainType_LocalRef` |  |  |  |
| 18 | `OA.DT.OVERRIDE` | `OaDomainType_Override` |  |  |  |
| 19 | `OA.DT.RECORD.STATUS` | `OaDomainType_RecordStatus` | String |  |  |
| 20 | `OA.DT.CURR.NO` | `OaDomainType_CurrNo` | String |  |  |
| 21 | `OA.DT.INPUTTER` | `OaDomainType_Inputter` |  |  |  |
| 22 | `OA.DT.DATE.TIME` | `OaDomainType_DateTime` |  |  |  |
| 23 | `OA.DT.AUTHORISER` | `OaDomainType_Authoriser` | String |  |  |
| 24 | `OA.DT.CO.CODE` | `OaDomainType_CoCode` | String |  |  |
| 25 | `OA.DT.DEPT.CODE` | `OaDomainType_DeptCode` | String |  |  |
| 26 | `OA.DT.AUDITOR.CODE` | `OaDomainType_AuditorCode` | String |  |  |
| 27 | `OA.DT.AUDIT.DATE.TIME` | `OaDomainType_AuditDateTime` | String |  |  |
