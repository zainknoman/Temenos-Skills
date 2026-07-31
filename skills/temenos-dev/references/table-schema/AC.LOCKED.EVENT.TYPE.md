# AC.LOCKED.EVENT.TYPE — Table Schema

> Source: `INSERTS/I_F.AC.LOCKED.EVENT.TYPE` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.LCK.TYPE.DESCRIPTION` | `AcLockedEventType_Description` |  |  |  |
| 2 | `AC.LCK.TYPE.ACCOUNT.LINK` | `AcLockedEventType_AccountLink` | TField | Yes | Identifies if the locked amount must be applied to the single account or to all the accounts in the hierarchy Validation Rules: Mandatory input. |
| 3 | `AC.LCK.TYPE.CHECK.NOTICE` | `AcLockedEventType_CheckNotice` | TField |  | Flag to verify whether to check notice available amount for Arrangements |
| 4 | `AC.LCK.TYPE.RESERVED.4` | `AcLockedEventType_Reserved4` |  |  |  |
| 5 | `AC.LCK.TYPE.RESERVED.3` | `AcLockedEventType_Reserved3` | TField |  |  |
| 6 | `AC.LCK.TYPE.RESERVED.2` | `AcLockedEventType_Reserved2` | TField |  |  |
| 7 | `AC.LCK.TYPE.RESERVED.1` | `AcLockedEventType_Reserved1` | TField |  |  |
| 8 | `AC.LCK.TYPE.LOCAL.REF` | `AcLockedEventType_LocalRef` |  |  |  |
| 9 | `AC.LCK.TYPE.OVERRIDE` | `AcLockedEventType_Override` |  |  |  |
| 10 | `AC.LCK.TYPE.RECORD.STATUS` | `AcLockedEventType_RecordStatus` | String |  |  |
| 11 | `AC.LCK.TYPE.CURR.NO` | `AcLockedEventType_CurrNo` | String |  |  |
| 12 | `AC.LCK.TYPE.INPUTTER` | `AcLockedEventType_Inputter` |  |  |  |
| 13 | `AC.LCK.TYPE.DATE.TIME` | `AcLockedEventType_DateTime` |  |  |  |
| 14 | `AC.LCK.TYPE.AUTHORISER` | `AcLockedEventType_Authoriser` | String |  |  |
| 15 | `AC.LCK.TYPE.CO.CODE` | `AcLockedEventType_CoCode` | String |  |  |
| 16 | `AC.LCK.TYPE.DEPT.CODE` | `AcLockedEventType_DeptCode` | String |  |  |
| 17 | `AC.LCK.TYPE.AUDITOR.CODE` | `AcLockedEventType_AuditorCode` | String |  |  |
| 18 | `AC.LCK.TYPE.AUDIT.DATE.TIME` | `AcLockedEventType_AuditDateTime` | String |  |  |
