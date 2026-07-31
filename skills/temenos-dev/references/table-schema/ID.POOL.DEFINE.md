# ID.POOL.DEFINE — Table Schema

> Source: `INSERTS/I_F.ID.POOL.DEFINE` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPD.EFFECTIVE.DATE` | `IdPoolDefine_EffectiveDate` | TField |  | The date from which the contract is linked to the Pool. Validation Rules: 1. Must be greater than the Pool Available date as defined in the table ID.POOL.PARAMETER. 2. Must be a standard T24 Date. |
| 2 | `ID.IPD.CURRENT.POOL` | `IdPoolDefine_CurrentPool` | TField |  | The Pool to which the contract is linked to. Validation Rules: 1. Must be a valid record from the table ID.POOL.PARAMETER. |
| 3 | `ID.IPD.RESERVED.10` | `IdPoolDefine_Reserved10` | TField |  |  |
| 4 | `ID.IPD.RESERVED.9` | `IdPoolDefine_Reserved9` | TField |  |  |
| 5 | `ID.IPD.RESERVED.8` | `IdPoolDefine_Reserved8` | TField |  |  |
| 6 | `ID.IPD.RESERVED.7` | `IdPoolDefine_Reserved7` | TField |  |  |
| 7 | `ID.IPD.RESERVED.6` | `IdPoolDefine_Reserved6` | TField |  |  |
| 8 | `ID.IPD.RESERVED.5` | `IdPoolDefine_Reserved5` | TField |  |  |
| 9 | `ID.IPD.RESERVED.4` | `IdPoolDefine_Reserved4` | TField |  |  |
| 10 | `ID.IPD.RESERVED.3` | `IdPoolDefine_Reserved3` | TField |  |  |
| 11 | `ID.IPD.RESERVED.2` | `IdPoolDefine_Reserved2` | TField |  |  |
| 12 | `ID.IPD.RESERVED.1` | `IdPoolDefine_Reserved1` | TField |  |  |
| 13 | `ID.IPD.LOCAL.REF` | `IdPoolDefine_LocalRef` |  |  |  |
| 14 | `ID.IPD.OVERRIDE` | `IdPoolDefine_Override` |  |  |  |
| 15 | `ID.IPD.RECORD.STATUS` | `IdPoolDefine_RecordStatus` | String |  |  |
| 16 | `ID.IPD.CURR.NO` | `IdPoolDefine_CurrNo` | String |  |  |
| 17 | `ID.IPD.INPUTTER` | `IdPoolDefine_Inputter` |  |  |  |
| 18 | `ID.IPD.DATE.TIME` | `IdPoolDefine_DateTime` |  |  |  |
| 19 | `ID.IPD.AUTHORISER` | `IdPoolDefine_Authoriser` | String |  |  |
| 20 | `ID.IPD.CO.CODE` | `IdPoolDefine_CoCode` | String |  |  |
| 21 | `ID.IPD.DEPT.CODE` | `IdPoolDefine_DeptCode` | String |  |  |
| 22 | `ID.IPD.AUDITOR.CODE` | `IdPoolDefine_AuditorCode` | String |  |  |
| 23 | `ID.IPD.AUDIT.DATE.TIME` | `IdPoolDefine_AuditDateTime` | String |  |  |
