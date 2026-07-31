# CP.PROCESS — Table Schema

> Source: `INSERTS/I_F.CP.PROCESS` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.PW.DESCRIPTION` | `CpProcess_Description` | TField | Yes | This field stores the description of the parameter defined as ID. Validation Rules: Mandatory field. |
| 2 | `CP.PW.VALUE` | `CpProcess_Value` | TField | Yes | This field stores the value of the parameter defined as ID. Validation Rules: Mandatory field. |
| 3 | `CP.PW.OBSERVATIONS` | `CpProcess_Observations` | TField |  | This field stores other infos regarding the parameter defined as ID. |
| 4 | `CP.PW.RESERVED.10` | `CpProcess_Reserved10` | TField |  |  |
| 5 | `CP.PW.RESERVED.9` | `CpProcess_Reserved9` | TField |  |  |
| 6 | `CP.PW.RESERVED.8` | `CpProcess_Reserved8` | TField |  |  |
| 7 | `CP.PW.RESERVED.7` | `CpProcess_Reserved7` | TField |  |  |
| 8 | `CP.PW.RESERVED.6` | `CpProcess_Reserved6` | TField |  |  |
| 9 | `CP.PW.RESERVED.5` | `CpProcess_Reserved5` | TField |  |  |
| 10 | `CP.PW.RESERVED.4` | `CpProcess_Reserved4` | TField |  |  |
| 11 | `CP.PW.RESERVED.3` | `CpProcess_Reserved3` | TField |  |  |
| 12 | `CP.PW.RESERVED.2` | `CpProcess_Reserved2` | TField |  |  |
| 13 | `CP.PW.RESERVED.1` | `CpProcess_Reserved1` | TField |  |  |
| 14 | `CP.PW.LOCAL.REF` | `CpProcess_LocalRef` |  |  |  |
| 15 | `CP.PW.OVERRIDE` | `CpProcess_Override` |  |  |  |
| 16 | `CP.PW.RECORD.STATUS` | `CpProcess_RecordStatus` | String |  |  |
| 17 | `CP.PW.CURR.NO` | `CpProcess_CurrNo` | String |  |  |
| 18 | `CP.PW.INPUTTER` | `CpProcess_Inputter` |  |  |  |
| 19 | `CP.PW.DATE.TIME` | `CpProcess_DateTime` |  |  |  |
| 20 | `CP.PW.AUTHORISER` | `CpProcess_Authoriser` | String |  |  |
| 21 | `CP.PW.CO.CODE` | `CpProcess_CoCode` | String |  |  |
| 22 | `CP.PW.DEPT.CODE` | `CpProcess_DeptCode` | String |  |  |
| 23 | `CP.PW.AUDITOR.CODE` | `CpProcess_AuditorCode` | String |  |  |
| 24 | `CP.PW.AUDIT.DATE.TIME` | `CpProcess_AuditDateTime` | String |  |  |
