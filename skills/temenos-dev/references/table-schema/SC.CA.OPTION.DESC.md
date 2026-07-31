# SC.CA.OPTION.DESC — Table Schema

> Source: `INSERTS/I_F.SC.CA.OPTION.DESC` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.DES.DESCRIPTION` | `ScCaOptionDesc_Description` |  |  |  |
| 2 | `SC.DES.RESERVED1` | `ScCaOptionDesc_Reserved1` | TField |  |  |
| 3 | `SC.DES.RESERVED2` | `ScCaOptionDesc_Reserved2` | TField |  |  |
| 4 | `SC.DES.RESERVED3` | `ScCaOptionDesc_Reserved3` | TField |  |  |
| 5 | `SC.DES.RESERVED4` | `ScCaOptionDesc_Reserved4` | TField |  |  |
| 6 | `SC.DES.RESERVED5` | `ScCaOptionDesc_Reserved5` | TField |  |  |
| 7 | `SC.DES.RECORD.STATUS` | `ScCaOptionDesc_RecordStatus` | String |  |  |
| 8 | `SC.DES.CURR.NO` | `ScCaOptionDesc_CurrNo` | String |  |  |
| 9 | `SC.DES.INPUTTER` | `ScCaOptionDesc_Inputter` |  |  |  |
| 10 | `SC.DES.DATE.TIME` | `ScCaOptionDesc_DateTime` |  |  |  |
| 11 | `SC.DES.AUTHORISER` | `ScCaOptionDesc_Authoriser` | String |  |  |
| 12 | `SC.DES.CO.CODE` | `ScCaOptionDesc_CoCode` | String |  |  |
| 13 | `SC.DES.DEPT.CODE` | `ScCaOptionDesc_DeptCode` | String |  |  |
| 14 | `SC.DES.AUDITOR.CODE` | `ScCaOptionDesc_AuditorCode` | String |  |  |
| 15 | `SC.DES.AUDIT.DATE.TIME` | `ScCaOptionDesc_AuditDateTime` | String |  |  |
