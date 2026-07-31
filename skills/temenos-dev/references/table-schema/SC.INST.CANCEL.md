# SC.INST.CANCEL — Table Schema

> Source: `INSERTS/I_F.SC.INST.CANCEL` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SIC.MSG.REF` | `ScInstCancel_MsgRef` | TField |  | This field is auto populated by the system Holds Original instruction reference (SEME) |
| 2 | `SC.SIC.REQUEST.CANCEL` | `ScInstCancel_RequestCancel` | TField |  | If set to Yes, the system will trigger a cancellation request Accepts value of YES |
| 3 | `SC.SIC.NARRATIVE` | `ScInstCancel_Narrative` | TField |  | Free format text for user to record cancellation details Input allowed Upto 35 characters |
| 4 | `SC.SIC.CANC.DELIV.REF` | `ScInstCancel_CancDelivRef` | TField |  | This field is auto populated value by the system with the reference of the cancellation message Holds Message reference of cancel request |
| 5 | `SC.SIC.CANC.MSG.STATUS` | `ScInstCancel_CancMsgStatus` | TField |  | This field denotes the status of the Cancellation request When user triggers Cancellation request, this field is updated as Cancellation Initiated When cancellation is accepted by both the counterparties, this field is updated as Cancellation Accepted |
| 6 | `SC.SIC.RESERVED.15` | `ScInstCancel_Reserved15` | TField |  |  |
| 7 | `SC.SIC.RESERVED.14` | `ScInstCancel_Reserved14` | TField |  |  |
| 8 | `SC.SIC.RESERVED.13` | `ScInstCancel_Reserved13` | TField |  |  |
| 9 | `SC.SIC.RESERVED.12` | `ScInstCancel_Reserved12` | TField |  |  |
| 10 | `SC.SIC.RESERVED.11` | `ScInstCancel_Reserved11` | TField |  |  |
| 11 | `SC.SIC.RESERVED.10` | `ScInstCancel_Reserved10` | TField |  |  |
| 12 | `SC.SIC.RESERVED.9` | `ScInstCancel_Reserved9` | TField |  |  |
| 13 | `SC.SIC.RESERVED.8` | `ScInstCancel_Reserved8` | TField |  |  |
| 14 | `SC.SIC.RESERVED.7` | `ScInstCancel_Reserved7` | TField |  |  |
| 15 | `SC.SIC.RESERVED.6` | `ScInstCancel_Reserved6` | TField |  |  |
| 16 | `SC.SIC.RESERVED.5` | `ScInstCancel_Reserved5` | TField |  |  |
| 17 | `SC.SIC.RESERVED.4` | `ScInstCancel_Reserved4` | TField |  |  |
| 18 | `SC.SIC.RESERVED.3` | `ScInstCancel_Reserved3` | TField |  |  |
| 19 | `SC.SIC.RESERVED.2` | `ScInstCancel_Reserved2` | TField |  |  |
| 20 | `SC.SIC.RESERVED.1` | `ScInstCancel_Reserved1` | TField |  |  |
| 21 | `SC.SIC.LOCAL.REF` | `ScInstCancel_LocalRef` |  |  |  |
| 22 | `SC.SIC.OVERRIDE` | `ScInstCancel_Override` |  |  |  |
| 23 | `SC.SIC.RECORD.STATUS` | `ScInstCancel_RecordStatus` | String |  |  |
| 24 | `SC.SIC.CURR.NO` | `ScInstCancel_CurrNo` | String |  |  |
| 25 | `SC.SIC.INPUTTER` | `ScInstCancel_Inputter` |  |  |  |
| 26 | `SC.SIC.DATE.TIME` | `ScInstCancel_DateTime` |  |  |  |
| 27 | `SC.SIC.AUTHORISER` | `ScInstCancel_Authoriser` | String |  |  |
| 28 | `SC.SIC.CO.CODE` | `ScInstCancel_CoCode` | String |  |  |
| 29 | `SC.SIC.DEPT.CODE` | `ScInstCancel_DeptCode` | String |  |  |
| 30 | `SC.SIC.AUDITOR.CODE` | `ScInstCancel_AuditorCode` | String |  |  |
| 31 | `SC.SIC.AUDIT.DATE.TIME` | `ScInstCancel_AuditDateTime` | String |  |  |
