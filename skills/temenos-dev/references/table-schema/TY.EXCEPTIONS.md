# TY.EXCEPTIONS — Table Schema

> Source: `INSERTS/I_F.TY.EXCEPTIONS` in `TY_Exceptions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.EXCEP.DESCRIPTION` | `TyExceptions_Description` |  |  |  |
| 2 | `TY.EXCEP.EXCEPTION` | `TyExceptions_Exception` |  |  |  |
| 3 | `TY.EXCEP.RESERVED.10` | `TyExceptions_Reserved10` | TField |  |  |
| 4 | `TY.EXCEP.RESERVED.9` | `TyExceptions_Reserved9` | TField |  |  |
| 5 | `TY.EXCEP.RESERVED.8` | `TyExceptions_Reserved8` | TField |  |  |
| 6 | `TY.EXCEP.RESERVED.7` | `TyExceptions_Reserved7` | TField |  |  |
| 7 | `TY.EXCEP.RESERVED.6` | `TyExceptions_Reserved6` | TField |  |  |
| 8 | `TY.EXCEP.RESERVED.5` | `TyExceptions_Reserved5` | TField |  |  |
| 9 | `TY.EXCEP.RESERVED.4` | `TyExceptions_Reserved4` | TField |  |  |
| 10 | `TY.EXCEP.RESERVED.3` | `TyExceptions_Reserved3` | TField |  |  |
| 11 | `TY.EXCEP.RESERVED.2` | `TyExceptions_Reserved2` | TField |  |  |
| 12 | `TY.EXCEP.RESERVED.1` | `TyExceptions_Reserved1` | TField |  |  |
| 13 | `TY.EXCEP.LOCAL.REF` | `TyExceptions_LocalRef` |  |  |  |
| 14 | `TY.EXCEP.OVERRIDE` | `TyExceptions_Override` |  |  |  |
| 15 | `TY.EXCEP.RECORD.STATUS` | `TyExceptions_RecordStatus` | String |  |  |
| 16 | `TY.EXCEP.CURR.NO` | `TyExceptions_CurrNo` | String |  |  |
| 17 | `TY.EXCEP.INPUTTER` | `TyExceptions_Inputter` |  |  |  |
| 18 | `TY.EXCEP.DATE.TIME` | `TyExceptions_DateTime` |  |  |  |
| 19 | `TY.EXCEP.AUTHORISER` | `TyExceptions_Authoriser` | String |  |  |
| 20 | `TY.EXCEP.CO.CODE` | `TyExceptions_CoCode` | String |  |  |
| 21 | `TY.EXCEP.DEPT.CODE` | `TyExceptions_DeptCode` | String |  |  |
| 22 | `TY.EXCEP.AUDITOR.CODE` | `TyExceptions_AuditorCode` | String |  |  |
| 23 | `TY.EXCEP.AUDIT.DATE.TIME` | `TyExceptions_AuditDateTime` | String |  |  |
