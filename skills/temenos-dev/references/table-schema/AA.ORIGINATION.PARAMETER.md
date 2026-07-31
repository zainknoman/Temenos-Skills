# AA.ORIGINATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AA.ORIGINATION.PARAMETER` in `AF_ClassFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.OP.DESCRIPTION` | `AaOriginationParameter_Description` |  |  |  |
| 2 | `AA.OP.FULL.DESCRIPTION` | `AaOriginationParameter_FullDescription` |  |  |  |
| 3 | `AA.OP.APPLICATION.INACTIVE.PERIOD` | `AaOriginationParameter_ApplicationInactivePeriod` | TField |  |  |
| 4 | `AA.OP.APPLICATION.ARCHIVE.PERIOD` | `AaOriginationParameter_ApplicationArchivePeriod` | TField |  |  |
| 5 | `AA.OP.ARCHIVE.PERIOD` | `AaOriginationParameter_ArchivePeriod` | TField |  |  |
| 6 | `AA.OP.RESERVED.10` | `AaOriginationParameter_Reserved10` | TField |  |  |
| 7 | `AA.OP.RESERVED.9` | `AaOriginationParameter_Reserved9` | TField |  |  |
| 8 | `AA.OP.RESERVED.8` | `AaOriginationParameter_Reserved8` | TField |  |  |
| 9 | `AA.OP.RESERVED.7` | `AaOriginationParameter_Reserved7` | TField |  |  |
| 10 | `AA.OP.RESERVED.6` | `AaOriginationParameter_Reserved6` | TField |  |  |
| 11 | `AA.OP.RESERVED.5` | `AaOriginationParameter_Reserved5` | TField |  |  |
| 12 | `AA.OP.RESERVED.4` | `AaOriginationParameter_Reserved4` | TField |  |  |
| 13 | `AA.OP.RESERVED.3` | `AaOriginationParameter_Reserved3` | TField |  |  |
| 14 | `AA.OP.RESERVED.2` | `AaOriginationParameter_Reserved2` | TField |  |  |
| 15 | `AA.OP.RESERVED.1` | `AaOriginationParameter_Reserved1` | TField |  |  |
| 16 | `AA.OP.RECORD.STATUS` | `AaOriginationParameter_RecordStatus` | String |  |  |
| 17 | `AA.OP.CURR.NO` | `AaOriginationParameter_CurrNo` | String |  |  |
| 18 | `AA.OP.INPUTTER` | `AaOriginationParameter_Inputter` |  |  |  |
| 19 | `AA.OP.DATE.TIME` | `AaOriginationParameter_DateTime` |  |  |  |
| 20 | `AA.OP.AUTHORISER` | `AaOriginationParameter_Authoriser` | String |  |  |
| 21 | `AA.OP.CO.CODE` | `AaOriginationParameter_CoCode` | String |  |  |
| 22 | `AA.OP.DEPT.CODE` | `AaOriginationParameter_DeptCode` | String |  |  |
| 23 | `AA.OP.AUDITOR.CODE` | `AaOriginationParameter_AuditorCode` | String |  |  |
| 24 | `AA.OP.AUDIT.DATE.TIME` | `AaOriginationParameter_AuditDateTime` | String |  |  |
