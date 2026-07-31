# SASIMA.HISTORY — Table Schema

> Source: `INSERTS/I_F.SASIMA.HISTORY` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.HIS.AACS` | `SasimaHistory_Aacs` | TField |  | Reserved for future use. |
| 2 | `SA.HIS.APST` | `SasimaHistory_Apst` | TField |  | Reserved for future use. |
| 3 | `SA.HIS.STS` | `SasimaHistory_Sts` | TField |  | Reserved for future use. |
| 4 | `SA.HIS.PURGE.DATE` | `SasimaHistory_PurgeDate` | TField |  |  |
| 5 | `SA.HIS.RESERVED.1` | `SasimaHistory_Reserved1` |  |  |  |
| 6 | `SA.HIS.RESERVED.2` | `SasimaHistory_Reserved2` | TField |  |  |
| 7 | `SA.HIS.RESERVED.3` | `SasimaHistory_Reserved3` | TField |  |  |
| 8 | `SA.HIS.RESERVED.4` | `SasimaHistory_Reserved4` | TField |  |  |
| 9 | `SA.HIS.RECORD.STATUS` | `SasimaHistory_RecordStatus` | String |  |  |
| 10 | `SA.HIS.CURR.NO` | `SasimaHistory_CurrNo` | String |  |  |
| 11 | `SA.HIS.INPUTTER` | `SasimaHistory_Inputter` |  |  |  |
| 12 | `SA.HIS.DATE.TIME` | `SasimaHistory_DateTime` |  |  |  |
| 13 | `SA.HIS.AUTHORISER` | `SasimaHistory_Authoriser` | String |  |  |
| 14 | `SA.HIS.CO.CODE` | `SasimaHistory_CoCode` | String |  |  |
| 15 | `SA.HIS.DEPT.CODE` | `SasimaHistory_DeptCode` | String |  |  |
| 16 | `SA.HIS.AUDITOR.CODE` | `SasimaHistory_AuditorCode` | String |  |  |
| 17 | `SA.HIS.AUDIT.DATE.TIME` | `SasimaHistory_AuditDateTime` | String |  |  |
