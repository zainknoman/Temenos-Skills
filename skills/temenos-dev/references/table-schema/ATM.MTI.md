# ATM.MTI — Table Schema

> Source: `INSERTS/I_F.ATM.MTI` in `ATMFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.MTI.DESCRIPTION` | `AtmMti_Description` |  |  |  |
| 2 | `ATM.MTI.LOCAL.REF` | `AtmMti_LocalRef` |  |  |  |
| 3 | `ATM.MTI.RESERVED.5` | `AtmMti_Reserved5` |  |  |  |
| 4 | `ATM.MTI.RESERVED.4` | `AtmMti_Reserved4` |  |  |  |
| 5 | `ATM.MTI.RESERVED.3` | `AtmMti_Reserved3` |  |  |  |
| 6 | `ATM.MTI.RESERVED.2` | `AtmMti_Reserved2` |  |  |  |
| 7 | `ATM.MTI.RESERVED.1` | `AtmMti_Reserved1` |  |  |  |
| 8 | `ATM.MTI.RECORD.STATUS` | `AtmMti_RecordStatus` |  |  |  |
| 9 | `ATM.MTI.CURR.NO` | `AtmMti_CurrNo` |  |  |  |
| 10 | `ATM.MTI.INPUTTER` | `AtmMti_Inputter` |  |  |  |
| 11 | `ATM.MTI.DATE.TIME` | `AtmMti_DateTime` |  |  |  |
| 12 | `ATM.MTI.AUTHORISER` | `AtmMti_Authoriser` |  |  |  |
| 13 | `ATM.MTI.CO.CODE` | `AtmMti_CoCode` |  |  |  |
| 14 | `ATM.MTI.DEPT.CODE` | `AtmMti_DeptCode` |  |  |  |
| 15 | `ATM.MTI.AUDITOR.CODE` | `AtmMti_AuditorCode` |  |  |  |
| 16 | `ATM.MTI.AUDIT.DATE.TIME` | `AtmMti_AuditDateTime` |  |  |  |
