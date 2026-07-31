# EB.STATE — Table Schema

> Source: `INSERTS/I_F.EB.STATE` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.STA.ENTRY.ACTION` | `EbState_EntryAction` |  |  |  |
| 2 | `EB.STA.RESERVED.9` | `EbState_Reserved9` |  |  |  |
| 3 | `EB.STA.RESERVED.8` | `EbState_Reserved8` |  |  |  |
| 4 | `EB.STA.RESERVED.7` | `EbState_Reserved7` |  |  |  |
| 5 | `EB.STA.RESERVED.6` | `EbState_Reserved6` |  |  |  |
| 6 | `EB.STA.TRANS.NAME` | `EbState_TransName` |  |  |  |
| 7 | `EB.STA.TRANS.EVENT` | `EbState_TransEvent` |  |  |  |
| 8 | `EB.STA.TRANS.GUARD.METHOD` | `EbState_TransGuardMethod` |  |  |  |
| 9 | `EB.STA.TRANS.IS.AUTO` | `EbState_TransIsAuto` |  |  |  |
| 10 | `EB.STA.TRANS.TARGET.STATE` | `EbState_TransTargetState` |  |  |  |
| 11 | `EB.STA.RESERVED.5` | `EbState_Reserved5` |  |  |  |
| 12 | `EB.STA.RESERVED.4` | `EbState_Reserved4` |  |  |  |
| 13 | `EB.STA.RESERVED.3` | `EbState_Reserved3` |  |  |  |
| 14 | `EB.STA.RESERVED.2` | `EbState_Reserved2` |  |  |  |
| 15 | `EB.STA.RESERVED.1` | `EbState_Reserved1` |  |  |  |
| 16 | `EB.STA.LOCAL.REF` | `EbState_LocalRef` |  |  |  |
| 17 | `EB.STA.OVERRIDE` | `EbState_Override` |  |  |  |
| 18 | `EB.STA.RECORD.STATUS` | `EbState_RecordStatus` |  |  |  |
| 19 | `EB.STA.CURR.NO` | `EbState_CurrNo` |  |  |  |
| 20 | `EB.STA.INPUTTER` | `EbState_Inputter` |  |  |  |
| 21 | `EB.STA.DATE.TIME` | `EbState_DateTime` |  |  |  |
| 22 | `EB.STA.AUTHORISER` | `EbState_Authoriser` |  |  |  |
| 23 | `EB.STA.CO.CODE` | `EbState_CoCode` |  |  |  |
| 24 | `EB.STA.DEPT.CODE` | `EbState_DeptCode` |  |  |  |
| 25 | `EB.STA.AUDITOR.CODE` | `EbState_AuditorCode` |  |  |  |
| 26 | `EB.STA.AUDIT.DATE.TIME` | `EbState_AuditDateTime` |  |  |  |
