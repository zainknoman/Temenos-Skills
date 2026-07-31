# CMBASE.STATE — Table Schema

> Source: `INSERTS/I_F.CMBASE.STATE` in `CMBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMBASE.DESCRIPTION` | `CmbaseState_Description` |  |  |  |
| 2 | `CMBASE.STATE.CODE` | `CmbaseState_StateCode` | TField |  | It is the State Code |
| 3 | `CMBASE.RESERVED.10` | `CmbaseState_Reserved10` | TField |  | Reserved for future purpose |
| 4 | `CMBASE.RESERVED.9` | `CmbaseState_Reserved9` | TField |  | Reserved for future purpose |
| 5 | `CMBASE.RESERVED.8` | `CmbaseState_Reserved8` | TField |  | Reserved for future purpose |
| 6 | `CMBASE.RESERVED.7` | `CmbaseState_Reserved7` | TField |  | Reserved for future purpose |
| 7 | `CMBASE.RESERVED.6` | `CmbaseState_Reserved6` | TField |  | Reserved for future purpose |
| 8 | `CMBASE.RESERVED.5` | `CmbaseState_Reserved5` | TField |  | Reserved for future purpose |
| 9 | `CMBASE.RESERVED.4` | `CmbaseState_Reserved4` | TField |  | Reserved for future purpose |
| 10 | `CMBASE.RESERVED.3` | `CmbaseState_Reserved3` | TField |  | Reserved for future purpose |
| 11 | `CMBASE.RESERVED.2` | `CmbaseState_Reserved2` | TField |  | Reserved for future purpose |
| 12 | `CMBASE.RESERVED.1` | `CmbaseState_Reserved1` | TField |  | Reserved for future purpose |
| 13 | `CMBASE.LOCAL.REF` | `CmbaseState_LocalRef` |  |  |  |
| 14 | `CMBASE.OVERRIDE` | `CmbaseState_Override` |  |  |  |
| 15 | `CMBASE.RECORD.STATUS` | `CmbaseState_RecordStatus` | String |  |  |
| 16 | `CMBASE.CURR.NO` | `CmbaseState_CurrNo` | String |  |  |
| 17 | `CMBASE.INPUTTER` | `CmbaseState_Inputter` |  |  |  |
| 18 | `CMBASE.DATE.TIME` | `CmbaseState_DateTime` |  |  |  |
| 19 | `CMBASE.AUTHORISER` | `CmbaseState_Authoriser` | String |  |  |
| 20 | `CMBASE.CO.CODE` | `CmbaseState_CoCode` | String |  |  |
| 21 | `CMBASE.DEPT.CODE` | `CmbaseState_DeptCode` | String |  |  |
| 22 | `CMBASE.AUDITOR.CODE` | `CmbaseState_AuditorCode` | String |  |  |
| 23 | `CMBASE.AUDIT.DATE.TIME` | `CmbaseState_AuditDateTime` | String |  |  |
