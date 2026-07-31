# SC.DEPO.MSG.MONITOR — Table Schema

> Source: `INSERTS/I_F.SC.DEPO.MSG.MONITOR` in `SC_SccEventNotification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.DMM.SECURITY.NO` | `ScDepoMsgMonitor_SecurityNo` | TField |  | This field will hold the security for which the MT564 message is received Validation Rules: Valid SECURITY.MASTER record |
| 2 | `SC.DMM.EVENT.TYPE` | `ScDepoMsgMonitor_EventType` | TField |  | This field denotes the corporate action event type Validation Rules: Valid DIARY.TYPE record |
| 3 | `SC.DMM.EX.DATE` | `ScDepoMsgMonitor_ExDate` | TField |  | This field denotes the ex-date of the corporate action event |
| 4 | `SC.DMM.MSG.TYPE` | `ScDepoMsgMonitor_MsgType` | TField |  | This field denotes the message type Validation Rules: Defaulted as 564 |
| 5 | `SC.DMM.MSG.RECD.DATE` | `ScDepoMsgMonitor_MsgRecdDate` | TField |  | This field denotes the date when the first MT564 was received |
| 6 | `SC.DMM.DEPOSITORY` | `ScDepoMsgMonitor_Depository` |  |  |  |
| 7 | `SC.DMM.MONITOR.DEPO` | `ScDepoMsgMonitor_MonitorDepo` |  |  |  |
| 8 | `SC.DMM.MANUAL.DEPOSITORY` | `ScDepoMsgMonitor_ManualDepository` |  |  |  |
| 9 | `SC.DMM.REMOVAL.DATE` | `ScDepoMsgMonitor_RemovalDate` |  |  |  |
| 10 | `SC.DMM.MANUAL.USER` | `ScDepoMsgMonitor_ManualUser` |  |  |  |
