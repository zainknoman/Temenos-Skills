# SC.ISSUER — Table Schema

> Source: `INSERTS/I_F.SC.ISSUER` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ISS.DESCRIPTION` | `ScIssuer_Description` |  |  |  |
| 2 | `SC.ISS.RESERVED.1` | `ScIssuer_Reserved1` | TField |  |  |
| 3 | `SC.ISS.RESERVED.2` | `ScIssuer_Reserved2` | TField |  |  |
| 4 | `SC.ISS.RESERVED.3` | `ScIssuer_Reserved3` | TField |  |  |
| 5 | `SC.ISS.RESERVED.4` | `ScIssuer_Reserved4` | TField |  |  |
| 6 | `SC.ISS.RESERVED.5` | `ScIssuer_Reserved5` | TField |  |  |
| 7 | `SC.ISS.RESERVED.6` | `ScIssuer_Reserved6` | TField |  |  |
| 8 | `SC.ISS.RESERVED.7` | `ScIssuer_Reserved7` | TField |  |  |
| 9 | `SC.ISS.RESERVED.8` | `ScIssuer_Reserved8` | TField |  |  |
| 10 | `SC.ISS.RESERVED.9` | `ScIssuer_Reserved9` | TField |  |  |
| 11 | `SC.ISS.RESERVED.10` | `ScIssuer_Reserved10` | TField |  |  |
| 12 | `SC.ISS.LOCAL.REF` | `ScIssuer_LocalRef` |  |  |  |
| 13 | `SC.ISS.RECORD.STATUS` | `ScIssuer_RecordStatus` | String |  |  |
| 14 | `SC.ISS.CURR.NO` | `ScIssuer_CurrNo` | String |  |  |
| 15 | `SC.ISS.INPUTTER` | `ScIssuer_Inputter` |  |  |  |
| 16 | `SC.ISS.DATE.TIME` | `ScIssuer_DateTime` |  |  |  |
| 17 | `SC.ISS.AUTHORISER` | `ScIssuer_Authoriser` | String |  |  |
| 18 | `SC.ISS.CO.CODE` | `ScIssuer_CoCode` | String |  |  |
| 19 | `SC.ISS.DEPT.CODE` | `ScIssuer_DeptCode` | String |  |  |
| 20 | `SC.ISS.AUDITOR.CODE` | `ScIssuer_AuditorCode` | String |  |  |
| 21 | `SC.ISS.AUDIT.DATE.TIME` | `ScIssuer_AuditDateTime` | String |  |  |
