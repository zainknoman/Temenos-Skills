# SC.TRADE.MSG.DETS — Table Schema

> Source: `INSERTS/I_F.SC.TRADE.MSG.DETS` in `SP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TRDET.TRADE.ID` | `ScTradeMsgDets_TradeId` | TField |  | This field should hold Trade Reference for the incoming message reference. When an incoming Securities Trade Confirmation Message (setr.027) is received, System will identify Trade for reference in message. If there are multiple Trades/No Trade available for the order, then this field will be left blank. User will be allowed to edit this field only when system couldn't identify trade while processing Securities Trade Confirmation message. |
| 2 | `SC.TRDET.MSG.TYPE` | `ScTradeMsgDets_MsgType` |  |  |  |
| 3 | `SC.TRDET.INW.DEL.REF` | `ScTradeMsgDets_InwDelRef` |  |  |  |
| 4 | `SC.TRDET.SENDER.ID` | `ScTradeMsgDets_SenderId` |  |  |  |
| 5 | `SC.TRDET.MSG.PROCESS.STATUS` | `ScTradeMsgDets_MsgProcessStatus` |  |  |  |
| 6 | `SC.TRDET.SP.STATUS` | `ScTradeMsgDets_SpStatus` |  |  |  |
| 7 | `SC.TRDET.LINK.MSG.REF` | `ScTradeMsgDets_LinkMsgRef` |  |  |  |
| 8 | `SC.TRDET.ACTION.STATUS` | `ScTradeMsgDets_ActionStatus` |  |  |  |
| 9 | `SC.TRDET.ACTION.NOTES` | `ScTradeMsgDets_ActionNotes` |  |  |  |
| 10 | `SC.TRDET.LATEST.MSG` | `ScTradeMsgDets_LatestMsg` | TField |  | Updated with value from MSG.TYPE of Latest multivalue Validation Rules: NOINPUT field |
| 11 | `SC.TRDET.LATEST.REF` | `ScTradeMsgDets_LatestRef` | TField |  | Updated with value from INW.DEL.REF of Latest multivalue Validation Rules: NOINPUT field |
| 12 | `SC.TRDET.LATEST.SENDER` | `ScTradeMsgDets_LatestSender` | TField |  | Updated with value from SENDER.ID of Latest multivalue Validation Rules: NOINPUT field |
| 13 | `SC.TRDET.LATEST.MSG.PROC.STATUS` | `ScTradeMsgDets_LatestMsgProcStatus` | TField |  | Updated with value from MSG.PROCESS.STATUS of Latest multivalue Validation Rules: NOINPUT field |
| 14 | `SC.TRDET.LATEST.SP.STATUS` | `ScTradeMsgDets_LatestSpStatus` | TField |  | Updated with value from SP.STATUS of Latest multivalue Validation Rules: NOINPUT field |
| 15 | `SC.TRDET.LATEST.LINK.REF` | `ScTradeMsgDets_LatestLinkRef` | TField |  | Updated with value from LINK.MSG.REF of Latest multivalue Validation Rules: NOINPUT field |
| 16 | `SC.TRDET.LATEST.ACT.STATUS` | `ScTradeMsgDets_LatestActStatus` | TField |  | Updated with value from ACTION.STATUS of Latest multivalue Validation Rules: NOINPUT field |
| 17 | `SC.TRDET.LATEST.ACT.NOTES` | `ScTradeMsgDets_LatestActNotes` |  |  |  |
| 18 | `SC.TRDET.LOCAL.REF` | `ScTradeMsgDets_LocalRef` |  |  |  |
| 19 | `SC.TRDET.OVERRIDE` | `ScTradeMsgDets_Override` |  |  |  |
| 20 | `SC.TRDET.RECORD.STATUS` | `ScTradeMsgDets_RecordStatus` | String |  |  |
| 21 | `SC.TRDET.CURR.NO` | `ScTradeMsgDets_CurrNo` | String |  |  |
| 22 | `SC.TRDET.INPUTTER` | `ScTradeMsgDets_Inputter` |  |  |  |
| 23 | `SC.TRDET.DATE.TIME` | `ScTradeMsgDets_DateTime` |  |  |  |
| 24 | `SC.TRDET.AUTHORISER` | `ScTradeMsgDets_Authoriser` | String |  |  |
| 25 | `SC.TRDET.CO.CODE` | `ScTradeMsgDets_CoCode` | String |  |  |
| 26 | `SC.TRDET.DEPT.CODE` | `ScTradeMsgDets_DeptCode` | String |  |  |
| 27 | `SC.TRDET.AUDITOR.CODE` | `ScTradeMsgDets_AuditorCode` | String |  |  |
| 28 | `SC.TRDET.AUDIT.DATE.TIME` | `ScTradeMsgDets_AuditDateTime` | String |  |  |
| 29 | `SC.TRDET.MSG.NET.AMOUNT` | `ScTradeMsgDets_MsgNetAmount` |  |  |  |
| 30 | `SC.TRDET.MSG.GROSS.AMOUNT` | `ScTradeMsgDets_MsgGrossAmount` |  |  |  |
| 31 | `SC.TRDET.MSG.CONF.QTY` | `ScTradeMsgDets_MsgConfQty` |  |  |  |
| 32 | `SC.TRDET.RESERVED.4` | `ScTradeMsgDets_Reserved4` | TField |  |  |
| 33 | `SC.TRDET.RESERVED.3` | `ScTradeMsgDets_Reserved3` | TField |  |  |
| 34 | `SC.TRDET.RESERVED.2` | `ScTradeMsgDets_Reserved2` | TField |  |  |
| 35 | `SC.TRDET.RESERVED.1` | `ScTradeMsgDets_Reserved1` | TField |  |  |
| 36 | `SC.TRDET.CHG.QUALIFIER` | `ScTradeMsgDets_ChgQualifier` |  |  |  |
| 37 | `SC.TRDET.MSG.VALUE` | `ScTradeMsgDets_MsgValue` |  |  |  |
| 38 | `SC.TRDET.TRD.VALUE` | `ScTradeMsgDets_TrdValue` |  |  |  |
| 39 | `SC.TRDET.MSG.PRICE` | `ScTradeMsgDets_MsgPrice` |  |  |  |
