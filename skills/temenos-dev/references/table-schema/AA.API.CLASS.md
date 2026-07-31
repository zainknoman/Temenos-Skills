# AA.API.CLASS — Table Schema

> Source: `INSERTS/I_F.AA.API.CLASS` in `AF_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.APC.DESCRIPTION` | `AaApiClass_Description` |  |  |  |
| 2 | `AA.APC.FULL.DESC` | `AaApiClass_FullDesc` |  |  |  |
| 3 | `AA.APC.TYPE` | `AaApiClass_Type` |  |  |  |
| 4 | `AA.APC.RESERVED.10` | `AaApiClass_Reserved10` | TField |  |  |
| 5 | `AA.APC.RESERVED.9` | `AaApiClass_Reserved9` | TField |  |  |
| 6 | `AA.APC.RESERVED.8` | `AaApiClass_Reserved8` | TField |  |  |
| 7 | `AA.APC.RESERVED.7` | `AaApiClass_Reserved7` | TField |  |  |
| 8 | `AA.APC.RESERVED.6` | `AaApiClass_Reserved6` | TField |  |  |
| 9 | `AA.APC.RESERVED.5` | `AaApiClass_Reserved5` | TField |  |  |
| 10 | `AA.APC.RESERVED.4` | `AaApiClass_Reserved4` | TField |  |  |
| 11 | `AA.APC.RESERVED.3` | `AaApiClass_Reserved3` | TField |  |  |
| 12 | `AA.APC.RESERVED.2` | `AaApiClass_Reserved2` | TField |  |  |
| 13 | `AA.APC.RESERVED.1` | `AaApiClass_Reserved1` | TField |  |  |
| 14 | `AA.APC.LOCAL.REF` | `AaApiClass_LocalRef` |  |  |  |
| 15 | `AA.APC.OVERRIDE` | `AaApiClass_Override` |  |  |  |
| 16 | `AA.APC.RECORD.STATUS` | `AaApiClass_RecordStatus` | String |  |  |
| 17 | `AA.APC.CURR.NO` | `AaApiClass_CurrNo` | String |  |  |
| 18 | `AA.APC.INPUTTER` | `AaApiClass_Inputter` |  |  |  |
| 19 | `AA.APC.DATE.TIME` | `AaApiClass_DateTime` |  |  |  |
| 20 | `AA.APC.AUTHORISER` | `AaApiClass_Authoriser` | String |  |  |
| 21 | `AA.APC.CO.CODE` | `AaApiClass_CoCode` | String |  |  |
| 22 | `AA.APC.DEPT.CODE` | `AaApiClass_DeptCode` | String |  |  |
| 23 | `AA.APC.AUDITOR.CODE` | `AaApiClass_AuditorCode` | String |  |  |
| 24 | `AA.APC.AUDIT.DATE.TIME` | `AaApiClass_AuditDateTime` | String |  |  |
