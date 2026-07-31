# PM.DF.ENQ.MAPPER — Table Schema

> Source: `INSERTS/I_F.PM.DF.ENQ.MAPPER` in `PM_ReportingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PM.DM.DESCRIPTION` | `PmDfEnqMapper_Description` |  |  |  |
| 2 | `PM.DM.CUSTOMER.MAPPER` | `PmDfEnqMapper_CustomerMapper` | TField |  |  |
| 3 | `PM.DM.CATEGORY.MAPPER` | `PmDfEnqMapper_CategoryMapper` | TField |  |  |
| 4 | `PM.DM.RESERVED.15` | `PmDfEnqMapper_Reserved15` | TField |  |  |
| 5 | `PM.DM.RESERVED.14` | `PmDfEnqMapper_Reserved14` | TField |  |  |
| 6 | `PM.DM.RESERVED.13` | `PmDfEnqMapper_Reserved13` | TField |  |  |
| 7 | `PM.DM.RESERVED.12` | `PmDfEnqMapper_Reserved12` | TField |  |  |
| 8 | `PM.DM.RESERVED.11` | `PmDfEnqMapper_Reserved11` | TField |  |  |
| 9 | `PM.DM.RESERVED.10` | `PmDfEnqMapper_Reserved10` | TField |  |  |
| 10 | `PM.DM.RESERVED.9` | `PmDfEnqMapper_Reserved9` | TField |  |  |
| 11 | `PM.DM.RESERVED.8` | `PmDfEnqMapper_Reserved8` | TField |  |  |
| 12 | `PM.DM.RESERVED.7` | `PmDfEnqMapper_Reserved7` | TField |  |  |
| 13 | `PM.DM.RESERVED.6` | `PmDfEnqMapper_Reserved6` | TField |  |  |
| 14 | `PM.DM.RESERVED.5` | `PmDfEnqMapper_Reserved5` | TField |  |  |
| 15 | `PM.DM.RESERVED.4` | `PmDfEnqMapper_Reserved4` | TField |  |  |
| 16 | `PM.DM.RESERVED.3` | `PmDfEnqMapper_Reserved3` | TField |  |  |
| 17 | `PM.DM.RESERVED.2` | `PmDfEnqMapper_Reserved2` | TField |  |  |
| 18 | `PM.DM.RESERVED.1` | `PmDfEnqMapper_Reserved1` | TField |  |  |
| 19 | `PM.DM.LOCAL.REF` | `PmDfEnqMapper_LocalRef` |  |  |  |
| 20 | `PM.DM.OVERRIDE` | `PmDfEnqMapper_Override` |  |  |  |
| 21 | `PM.DM.RECORD.STATUS` | `PmDfEnqMapper_RecordStatus` | String |  |  |
| 22 | `PM.DM.CURR.NO` | `PmDfEnqMapper_CurrNo` | String |  |  |
| 23 | `PM.DM.INPUTTER` | `PmDfEnqMapper_Inputter` |  |  |  |
| 24 | `PM.DM.DATE.TIME` | `PmDfEnqMapper_DateTime` |  |  |  |
| 25 | `PM.DM.AUTHORISER` | `PmDfEnqMapper_Authoriser` | String |  |  |
| 26 | `PM.DM.CO.CODE` | `PmDfEnqMapper_CoCode` | String |  |  |
| 27 | `PM.DM.DEPT.CODE` | `PmDfEnqMapper_DeptCode` | String |  |  |
| 28 | `PM.DM.AUDITOR.CODE` | `PmDfEnqMapper_AuditorCode` | String |  |  |
| 29 | `PM.DM.AUDIT.DATE.TIME` | `PmDfEnqMapper_AuditDateTime` | String |  |  |
