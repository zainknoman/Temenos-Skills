# EB.STATE.MACHINE — Table Schema

> Source: `INSERTS/I_F.EB.STATE.MACHINE` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SMC.CURR.STATE.METHOD` | `EbStateMachine_CurrStateMethod` | TField |  |  |
| 2 | `EB.SMC.RESERVED.11` | `EbStateMachine_Reserved11` | TField |  |  |
| 3 | `EB.SMC.RESERVED.10` | `EbStateMachine_Reserved10` | TField |  |  |
| 4 | `EB.SMC.RESERVED.9` | `EbStateMachine_Reserved9` | TField |  |  |
| 5 | `EB.SMC.RESERVED.8` | `EbStateMachine_Reserved8` | TField |  |  |
| 6 | `EB.SMC.RESERVED.7` | `EbStateMachine_Reserved7` | TField |  |  |
| 7 | `EB.SMC.RESERVED.6` | `EbStateMachine_Reserved6` | TField |  |  |
| 8 | `EB.SMC.RESERVED.5` | `EbStateMachine_Reserved5` | TField |  |  |
| 9 | `EB.SMC.RESERVED.4` | `EbStateMachine_Reserved4` | TField |  |  |
| 10 | `EB.SMC.RESERVED.3` | `EbStateMachine_Reserved3` | TField |  |  |
| 11 | `EB.SMC.RESERVED.2` | `EbStateMachine_Reserved2` | TField |  |  |
| 12 | `EB.SMC.RESERVED.1` | `EbStateMachine_Reserved1` | TField |  |  |
| 13 | `EB.SMC.LOCAL.REF` | `EbStateMachine_LocalRef` |  |  |  |
| 14 | `EB.SMC.OVERRIDE` | `EbStateMachine_Override` |  |  |  |
| 15 | `EB.SMC.RECORD.STATUS` | `EbStateMachine_RecordStatus` | String |  |  |
| 16 | `EB.SMC.CURR.NO` | `EbStateMachine_CurrNo` | String |  |  |
| 17 | `EB.SMC.INPUTTER` | `EbStateMachine_Inputter` |  |  |  |
| 18 | `EB.SMC.DATE.TIME` | `EbStateMachine_DateTime` |  |  |  |
| 19 | `EB.SMC.AUTHORISER` | `EbStateMachine_Authoriser` | String |  |  |
| 20 | `EB.SMC.CO.CODE` | `EbStateMachine_CoCode` | String |  |  |
| 21 | `EB.SMC.DEPT.CODE` | `EbStateMachine_DeptCode` | String |  |  |
| 22 | `EB.SMC.AUDITOR.CODE` | `EbStateMachine_AuditorCode` | String |  |  |
| 23 | `EB.SMC.AUDIT.DATE.TIME` | `EbStateMachine_AuditDateTime` | String |  |  |
