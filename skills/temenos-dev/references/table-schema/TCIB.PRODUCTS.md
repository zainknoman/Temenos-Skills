# TCIB.PRODUCTS — Table Schema

> Source: `INSERTS/I_F.TCIB.PRODUCTS` in `CATCIB_TCIBOnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCIB.PROD.ALLOWED.TO.OPEN` | `TcibProducts_AllowedToOpen` | TField |  | YES or NO field to indicate whether this can be opened |
| 2 | `TCIB.PROD.PROPERTY` | `TcibProducts_Property` |  |  |  |
| 3 | `TCIB.PROD.FIELD.NAME` | `TcibProducts_FieldName` |  |  |  |
| 4 | `TCIB.PROD.FIELD.VALUE` | `TcibProducts_FieldValue` |  |  |  |
| 5 | `TCIB.PROD.RESERVED.1` | `TcibProducts_Reserved1` | TField |  |  |
| 6 | `TCIB.PROD.RESERVED.2` | `TcibProducts_Reserved2` | TField |  |  |
| 7 | `TCIB.PROD.RESERVED.3` | `TcibProducts_Reserved3` | TField |  |  |
| 8 | `TCIB.PROD.RESERVED.4` | `TcibProducts_Reserved4` | TField |  |  |
| 9 | `TCIB.PROD.RESERVED.5` | `TcibProducts_Reserved5` | TField |  |  |
| 10 | `TCIB.PROD.RESERVED.6` | `TcibProducts_Reserved6` | TField |  |  |
| 11 | `TCIB.PROD.RESERVED.7` | `TcibProducts_Reserved7` | TField |  |  |
| 12 | `TCIB.PROD.RESERVED.8` | `TcibProducts_Reserved8` | TField |  |  |
| 13 | `TCIB.PROD.RESERVED.9` | `TcibProducts_Reserved9` | TField |  |  |
| 14 | `TCIB.PROD.RESERVED.10` | `TcibProducts_Reserved10` | TField |  |  |
| 15 | `TCIB.PROD.OVERRIDE` | `TcibProducts_Override` |  |  |  |
| 16 | `TCIB.PROD.RECORD.STATUS` | `TcibProducts_RecordStatus` | String |  |  |
| 17 | `TCIB.PROD.CURR.NO` | `TcibProducts_CurrNo` | String |  |  |
| 18 | `TCIB.PROD.INPUTTER` | `TcibProducts_Inputter` |  |  |  |
| 19 | `TCIB.PROD.DATE.TIME` | `TcibProducts_DateTime` |  |  |  |
| 20 | `TCIB.PROD.AUTHORISER` | `TcibProducts_Authoriser` | String |  |  |
| 21 | `TCIB.PROD.CO.CODE` | `TcibProducts_CoCode` | String |  |  |
| 22 | `TCIB.PROD.DEPT.CODE` | `TcibProducts_DeptCode` | String |  |  |
| 23 | `TCIB.PROD.AUDITOR.CODE` | `TcibProducts_AuditorCode` | String |  |  |
| 24 | `TCIB.PROD.AUDIT.DATE.TIME` | `TcibProducts_AuditDateTime` | String |  |  |
