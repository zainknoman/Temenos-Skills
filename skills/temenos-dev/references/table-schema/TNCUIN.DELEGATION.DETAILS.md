# TNCUIN.DELEGATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.TNCUIN.DELEGATION.DETAILS` in `TNCUIN_CustomerCRM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.DEL.DESCRIPTION` | `TncuinDelegationDetails_Description` |  |  |  |
| 2 | `TNCUIN.DEL.GOVERNORATE` | `TncuinDelegationDetails_Governorate` | TField |  | This field stores the details of the Governorate for which the Delegation is created. Validation: This field should be a valid record from CMBASE.STATE |
| 3 | `TNCUIN.DEL.LOCAL.REF` | `TncuinDelegationDetails_LocalRef` |  |  |  |
| 4 | `TNCUIN.DEL.RESERVED.5` | `TncuinDelegationDetails_Reserved5` | TField |  |  |
| 5 | `TNCUIN.DEL.RESERVED.4` | `TncuinDelegationDetails_Reserved4` | TField |  |  |
| 6 | `TNCUIN.DEL.RESERVED.3` | `TncuinDelegationDetails_Reserved3` | TField |  |  |
| 7 | `TNCUIN.DEL.RESERVED.2` | `TncuinDelegationDetails_Reserved2` | TField |  |  |
| 8 | `TNCUIN.DEL.RESERVED.1` | `TncuinDelegationDetails_Reserved1` | TField |  |  |
| 9 | `TNCUIN.DEL.OVERRIDE` | `TncuinDelegationDetails_Override` |  |  |  |
| 10 | `TNCUIN.DEL.RECORD.STATUS` | `TncuinDelegationDetails_RecordStatus` | String |  |  |
| 11 | `TNCUIN.DEL.CURR.NO` | `TncuinDelegationDetails_CurrNo` | String |  |  |
| 12 | `TNCUIN.DEL.INPUTTER` | `TncuinDelegationDetails_Inputter` |  |  |  |
| 13 | `TNCUIN.DEL.DATE.TIME` | `TncuinDelegationDetails_DateTime` |  |  |  |
| 14 | `TNCUIN.DEL.AUTHORISER` | `TncuinDelegationDetails_Authoriser` | String |  |  |
| 15 | `TNCUIN.DEL.CO.CODE` | `TncuinDelegationDetails_CoCode` | String |  |  |
| 16 | `TNCUIN.DEL.DEPT.CODE` | `TncuinDelegationDetails_DeptCode` | String |  |  |
| 17 | `TNCUIN.DEL.AUDITOR.CODE` | `TncuinDelegationDetails_AuditorCode` | String |  |  |
| 18 | `TNCUIN.DEL.AUDIT.DATE.TIME` | `TncuinDelegationDetails_AuditDateTime` | String |  |  |
