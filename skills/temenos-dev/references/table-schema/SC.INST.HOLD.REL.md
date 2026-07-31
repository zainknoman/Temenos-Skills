# SC.INST.HOLD.REL — Table Schema

> Source: `INSERTS/I_F.SC.INST.HOLD.REL` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SHR.MSG.REF` | `ScInstHoldRel_MsgRef` | TField |  |  |
| 2 | `SC.SHR.HOLD.REQ` | `ScInstHoldRel_HoldReq` | TField |  |  |
| 3 | `SC.SHR.HOLD.DELIV.REF` | `ScInstHoldRel_HoldDelivRef` |  |  |  |
| 4 | `SC.SHR.RELEASE.REQ` | `ScInstHoldRel_ReleaseReq` | TField |  |  |
| 5 | `SC.SHR.REL.DELIV.REF` | `ScInstHoldRel_RelDelivRef` |  |  |  |
| 6 | `SC.SHR.NARRATIVE` | `ScInstHoldRel_Narrative` | TField |  |  |
| 7 | `SC.SHR.HOLD.REL.STATUS` | `ScInstHoldRel_HoldRelStatus` | TField |  |  |
| 8 | `SC.SHR.RESERVED.15` | `ScInstHoldRel_Reserved15` | TField |  |  |
| 9 | `SC.SHR.RESERVED.14` | `ScInstHoldRel_Reserved14` | TField |  |  |
| 10 | `SC.SHR.RESERVED.13` | `ScInstHoldRel_Reserved13` | TField |  |  |
| 11 | `SC.SHR.RESERVED.12` | `ScInstHoldRel_Reserved12` | TField |  |  |
| 12 | `SC.SHR.RESERVED.11` | `ScInstHoldRel_Reserved11` | TField |  |  |
| 13 | `SC.SHR.RESERVED.10` | `ScInstHoldRel_Reserved10` | TField |  |  |
| 14 | `SC.SHR.RESERVED.9` | `ScInstHoldRel_Reserved9` | TField |  |  |
| 15 | `SC.SHR.RESERVED.8` | `ScInstHoldRel_Reserved8` | TField |  |  |
| 16 | `SC.SHR.RESERVED.7` | `ScInstHoldRel_Reserved7` | TField |  |  |
| 17 | `SC.SHR.RESERVED.6` | `ScInstHoldRel_Reserved6` | TField |  |  |
| 18 | `SC.SHR.RESERVED.5` | `ScInstHoldRel_Reserved5` | TField |  |  |
| 19 | `SC.SHR.RESERVED.4` | `ScInstHoldRel_Reserved4` | TField |  |  |
| 20 | `SC.SHR.RESERVED.3` | `ScInstHoldRel_Reserved3` | TField |  |  |
| 21 | `SC.SHR.RESERVED.2` | `ScInstHoldRel_Reserved2` | TField |  |  |
| 22 | `SC.SHR.RESERVED.1` | `ScInstHoldRel_Reserved1` | TField |  |  |
| 23 | `SC.SHR.LOCAL.REF` | `ScInstHoldRel_LocalRef` |  |  |  |
| 24 | `SC.SHR.OVERRIDE` | `ScInstHoldRel_Override` |  |  |  |
| 25 | `SC.SHR.RECORD.STATUS` | `ScInstHoldRel_RecordStatus` | String |  |  |
| 26 | `SC.SHR.CURR.NO` | `ScInstHoldRel_CurrNo` | String |  |  |
| 27 | `SC.SHR.INPUTTER` | `ScInstHoldRel_Inputter` |  |  |  |
| 28 | `SC.SHR.DATE.TIME` | `ScInstHoldRel_DateTime` |  |  |  |
| 29 | `SC.SHR.AUTHORISER` | `ScInstHoldRel_Authoriser` | String |  |  |
| 30 | `SC.SHR.CO.CODE` | `ScInstHoldRel_CoCode` | String |  |  |
| 31 | `SC.SHR.DEPT.CODE` | `ScInstHoldRel_DeptCode` | String |  |  |
| 32 | `SC.SHR.AUDITOR.CODE` | `ScInstHoldRel_AuditorCode` | String |  |  |
| 33 | `SC.SHR.AUDIT.DATE.TIME` | `ScInstHoldRel_AuditDateTime` | String |  |  |
