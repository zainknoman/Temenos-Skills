# CBR.ACCOUNT.STATUS — Table Schema

> Source: `INSERTS/I_F.CBR.ACCOUNT.STATUS` in `FINEXT_CBR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBR.STAT.ACCOUNT.STATUS` | `CbrAccountStatus_AccountStatus` | TField |  |  |
| 2 | `CBR.STAT.RESERVED.1` | `CbrAccountStatus_Reserved1` | TField |  |  |
| 3 | `CBR.STAT.RESERVED.2` | `CbrAccountStatus_Reserved2` | TField |  |  |
| 4 | `CBR.STAT.RESERVED.3` | `CbrAccountStatus_Reserved3` | TField |  |  |
| 5 | `CBR.STAT.RESERVED.4` | `CbrAccountStatus_Reserved4` | TField |  |  |
| 6 | `CBR.STAT.RESERVED.5` | `CbrAccountStatus_Reserved5` | TField |  |  |
| 7 | `CBR.STAT.RESERVED.6` | `CbrAccountStatus_Reserved6` | TField |  |  |
| 8 | `CBR.STAT.RESERVED.7` | `CbrAccountStatus_Reserved7` | TField |  |  |
| 9 | `CBR.STAT.RESERVED.8` | `CbrAccountStatus_Reserved8` | TField |  |  |
| 10 | `CBR.STAT.RESERVED.9` | `CbrAccountStatus_Reserved9` | TField |  |  |
| 11 | `CBR.STAT.RESERVED.10` | `CbrAccountStatus_Reserved10` | TField |  |  |
| 12 | `CBR.STAT.RECORD.STATUS` | `CbrAccountStatus_RecordStatus` | String |  |  |
| 13 | `CBR.STAT.CURR.NO` | `CbrAccountStatus_CurrNo` | String |  |  |
| 14 | `CBR.STAT.INPUTTER` | `CbrAccountStatus_Inputter` |  |  |  |
| 15 | `CBR.STAT.DATE.TIME` | `CbrAccountStatus_DateTime` |  |  |  |
| 16 | `CBR.STAT.AUTHORISER` | `CbrAccountStatus_Authoriser` | String |  |  |
| 17 | `CBR.STAT.CO.CODE` | `CbrAccountStatus_CoCode` | String |  |  |
| 18 | `CBR.STAT.DEPT.CODE` | `CbrAccountStatus_DeptCode` | String |  |  |
| 19 | `CBR.STAT.AUDITOR.CODE` | `CbrAccountStatus_AuditorCode` | String |  |  |
| 20 | `CBR.STAT.AUDIT.DATE.TIME` | `CbrAccountStatus_AuditDateTime` | String |  |  |
