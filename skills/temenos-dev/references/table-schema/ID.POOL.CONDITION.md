# ID.POOL.CONDITION — Table Schema

> Source: `INSERTS/I_F.ID.POOL.CONDITION` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IPC.DESCRIPTION` | `IdPoolCondition_Description` |  |  |  |
| 2 | `ID.IPC.DEFAULT.POOL` | `IdPoolCondition_DefaultPool` | TField | Yes | The default pool to which the contract will be related to in case the contract details does not match with any of the pool condition during evaluation of the contract. Validation Rules: 1. Must be a valid record from the application ID.POOL.PARAMETER 2. Mandatory Input. |
| 3 | `ID.IPC.POOL` | `IdPoolCondition_Pool` |  |  |  |
| 4 | `ID.IPC.APPL.FIELD.NAME` | `IdPoolCondition_ApplFieldName` |  |  |  |
| 5 | `ID.IPC.FIELD.OPERATOR` | `IdPoolCondition_FieldOperator` |  |  |  |
| 6 | `ID.IPC.VALUE.FROM` | `IdPoolCondition_ValueFrom` |  |  |  |
| 7 | `ID.IPC.VALUE.TO` | `IdPoolCondition_ValueTo` |  |  |  |
| 8 | `ID.IPC.FIELD.OPERATION` | `IdPoolCondition_FieldOperation` |  |  |  |
| 9 | `ID.IPC.RESERVED.16` | `IdPoolCondition_Reserved16` |  |  |  |
| 10 | `ID.IPC.RESERVED.15` | `IdPoolCondition_Reserved15` |  |  |  |
| 11 | `ID.IPC.RESERVED.14` | `IdPoolCondition_Reserved14` |  |  |  |
| 12 | `ID.IPC.RESERVED.13` | `IdPoolCondition_Reserved13` |  |  |  |
| 13 | `ID.IPC.RESERVED.12` | `IdPoolCondition_Reserved12` |  |  |  |
| 14 | `ID.IPC.RESERVED.11` | `IdPoolCondition_Reserved11` |  |  |  |
| 15 | `ID.IPC.RESERVED.10` | `IdPoolCondition_Reserved10` | TField |  |  |
| 16 | `ID.IPC.RESERVED.9` | `IdPoolCondition_Reserved9` | TField |  |  |
| 17 | `ID.IPC.RESERVED.8` | `IdPoolCondition_Reserved8` | TField |  |  |
| 18 | `ID.IPC.RESERVED.7` | `IdPoolCondition_Reserved7` | TField |  |  |
| 19 | `ID.IPC.RESERVED.6` | `IdPoolCondition_Reserved6` | TField |  |  |
| 20 | `ID.IPC.RESERVED.5` | `IdPoolCondition_Reserved5` | TField |  |  |
| 21 | `ID.IPC.RESERVED.4` | `IdPoolCondition_Reserved4` | TField |  |  |
| 22 | `ID.IPC.RESERVED.3` | `IdPoolCondition_Reserved3` | TField |  |  |
| 23 | `ID.IPC.RESERVED.2` | `IdPoolCondition_Reserved2` | TField |  |  |
| 24 | `ID.IPC.RESERVED.1` | `IdPoolCondition_Reserved1` | TField |  |  |
| 25 | `ID.IPC.LOCAL.REF` | `IdPoolCondition_LocalRef` |  |  |  |
| 26 | `ID.IPC.OVERRIDE` | `IdPoolCondition_Override` |  |  |  |
| 27 | `ID.IPC.RECORD.STATUS` | `IdPoolCondition_RecordStatus` | String |  |  |
| 28 | `ID.IPC.CURR.NO` | `IdPoolCondition_CurrNo` | String |  |  |
| 29 | `ID.IPC.INPUTTER` | `IdPoolCondition_Inputter` |  |  |  |
| 30 | `ID.IPC.DATE.TIME` | `IdPoolCondition_DateTime` |  |  |  |
| 31 | `ID.IPC.AUTHORISER` | `IdPoolCondition_Authoriser` | String |  |  |
| 32 | `ID.IPC.CO.CODE` | `IdPoolCondition_CoCode` | String |  |  |
| 33 | `ID.IPC.DEPT.CODE` | `IdPoolCondition_DeptCode` | String |  |  |
| 34 | `ID.IPC.AUDITOR.CODE` | `IdPoolCondition_AuditorCode` | String |  |  |
| 35 | `ID.IPC.AUDIT.DATE.TIME` | `IdPoolCondition_AuditDateTime` | String |  |  |
