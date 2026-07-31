# PP.MSGPAYMENTTYPECHANNEL — Table Schema

> Source: `INSERTS/I_F.PP.MSGPAYMENTTYPECHANNEL` in `PP_MessageMappingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.MPC.DESCRIPTION` | `PpMsgpaymenttypechannel_Description` |  |  |  |
| 2 | `PP.MPC.RESERVED.5` | `PpMsgpaymenttypechannel_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 3 | `PP.MPC.RESERVED.4` | `PpMsgpaymenttypechannel_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 4 | `PP.MPC.RESERVED.3` | `PpMsgpaymenttypechannel_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 5 | `PP.MPC.RESERVED.2` | `PpMsgpaymenttypechannel_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 6 | `PP.MPC.RESERVED.1` | `PpMsgpaymenttypechannel_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.MPC.LOCAL.REF` | `PpMsgpaymenttypechannel_LocalRef` |  |  |  |
| 8 | `PP.MPC.OVERRIDE` | `PpMsgpaymenttypechannel_Override` |  |  |  |
| 9 | `PP.MPC.RECORD.STATUS` | `PpMsgpaymenttypechannel_RecordStatus` | String |  |  |
| 10 | `PP.MPC.CURR.NO` | `PpMsgpaymenttypechannel_CurrNo` | String |  |  |
| 11 | `PP.MPC.INPUTTER` | `PpMsgpaymenttypechannel_Inputter` |  |  |  |
| 12 | `PP.MPC.DATE.TIME` | `PpMsgpaymenttypechannel_DateTime` |  |  |  |
| 13 | `PP.MPC.AUTHORISER` | `PpMsgpaymenttypechannel_Authoriser` | String |  |  |
| 14 | `PP.MPC.CO.CODE` | `PpMsgpaymenttypechannel_CoCode` | String |  |  |
| 15 | `PP.MPC.DEPT.CODE` | `PpMsgpaymenttypechannel_DeptCode` | String |  |  |
| 16 | `PP.MPC.AUDITOR.CODE` | `PpMsgpaymenttypechannel_AuditorCode` | String |  |  |
| 17 | `PP.MPC.AUDIT.DATE.TIME` | `PpMsgpaymenttypechannel_AuditDateTime` | String |  |  |
