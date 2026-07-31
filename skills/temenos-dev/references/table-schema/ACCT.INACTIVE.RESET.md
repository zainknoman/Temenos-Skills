# ACCT.INACTIVE.RESET — Table Schema

> Source: `INSERTS/I_F.ACCT.INACTIVE.RESET` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.IR.RESET.DATE` | `AcctInactiveReset_ResetDate` | TField |  | Specifies the date on which the Inactive Marker in the corresponding Account record is reset by this record. In Authorised records this field contains the date of the last time the Inactive Marker in the corresponding Account record was reset. In Unauthorised records, this field contains the current date, i.e. the date on which the Account will be reset by Authorising the record. Validation Rules: Standard Date format. This is a NOINPUT field. |
| 2 | `AC.IR.RESERVED.5` | `AcctInactiveReset_Reserved5` | TField |  |  |
| 3 | `AC.IR.RESERVED.4` | `AcctInactiveReset_Reserved4` | TField |  |  |
| 4 | `AC.IR.RESERVED.3` | `AcctInactiveReset_Reserved3` | TField |  |  |
| 5 | `AC.IR.RESERVED.2` | `AcctInactiveReset_Reserved2` | TField |  |  |
| 6 | `AC.IR.RESERVED.1` | `AcctInactiveReset_Reserved1` | TField |  |  |
| 7 | `AC.IR.LOCAL.REF` | `AcctInactiveReset_LocalRef` |  |  |  |
| 8 | `AC.IR.RECORD.STATUS` | `AcctInactiveReset_RecordStatus` | String |  |  |
| 9 | `AC.IR.CURR.NO` | `AcctInactiveReset_CurrNo` | String |  |  |
| 10 | `AC.IR.INPUTTER` | `AcctInactiveReset_Inputter` |  |  |  |
| 11 | `AC.IR.DATE.TIME` | `AcctInactiveReset_DateTime` |  |  |  |
| 12 | `AC.IR.AUTHORISER` | `AcctInactiveReset_Authoriser` | String |  |  |
| 13 | `AC.IR.CO.CODE` | `AcctInactiveReset_CoCode` | String |  |  |
| 14 | `AC.IR.DEPT.CODE` | `AcctInactiveReset_DeptCode` | String |  |  |
| 15 | `AC.IR.AUDITOR.CODE` | `AcctInactiveReset_AuditorCode` | String |  |  |
| 16 | `AC.IR.AUDIT.DATE.TIME` | `AcctInactiveReset_AuditDateTime` | String |  |  |
