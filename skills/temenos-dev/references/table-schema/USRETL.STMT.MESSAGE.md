# USRETL.STMT.MESSAGE — Table Schema

> Source: `INSERTS/I_F.USRETL.STMT.MESSAGE` in `USRETL_CombinedStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.CST.MSG.TEXT` | `UsretlStmtMessage_MsgText` |  |  |  |
| 2 | `AC.CST.ACH.TXN.TYPE` | `UsretlStmtMessage_AchTxnType` |  |  |  |
| 3 | `AC.CST.OD.MSG.TEXT` | `UsretlStmtMessage_OdMsgText` |  |  |  |
| 4 | `AC.CST.OD.THRESHOLD` | `UsretlStmtMessage_OdThreshold` | TField |  | This field is used to capture maximum number of overdraft transactions, which bank allows before adding counseling message to customers' statements. If customer exceeds the number of overdraft transactions defined in this field, counseling message captured in OD.MSG.TEXT will be added to customer's statement. |
| 5 | `AC.CST.RESERVED.8` | `UsretlStmtMessage_Reserved8` | TField |  |  |
| 6 | `AC.CST.RESERVED.7` | `UsretlStmtMessage_Reserved7` | TField |  |  |
| 7 | `AC.CST.RESERVED.6` | `UsretlStmtMessage_Reserved6` | TField |  |  |
| 8 | `AC.CST.RESERVED.5` | `UsretlStmtMessage_Reserved5` | TField |  |  |
| 9 | `AC.CST.RESERVED.4` | `UsretlStmtMessage_Reserved4` | TField |  |  |
| 10 | `AC.CST.RESERVED.3` | `UsretlStmtMessage_Reserved3` | TField |  |  |
| 11 | `AC.CST.RESERVED.2` | `UsretlStmtMessage_Reserved2` | TField |  |  |
| 12 | `AC.CST.RESERVED.1` | `UsretlStmtMessage_Reserved1` | TField |  |  |
| 13 | `AC.CST.RECORD.STATUS` | `UsretlStmtMessage_RecordStatus` | String |  |  |
| 14 | `AC.CST.CURR.NO` | `UsretlStmtMessage_CurrNo` | String |  |  |
| 15 | `AC.CST.INPUTTER` | `UsretlStmtMessage_Inputter` |  |  |  |
| 16 | `AC.CST.DATE.TIME` | `UsretlStmtMessage_DateTime` |  |  |  |
| 17 | `AC.CST.AUTHORISER` | `UsretlStmtMessage_Authoriser` | String |  |  |
| 18 | `AC.CST.CO.CODE` | `UsretlStmtMessage_CoCode` | String |  |  |
| 19 | `AC.CST.DEPT.CODE` | `UsretlStmtMessage_DeptCode` | String |  |  |
| 20 | `AC.CST.AUDITOR.CODE` | `UsretlStmtMessage_AuditorCode` | String |  |  |
| 21 | `AC.CST.AUDIT.DATE.TIME` | `UsretlStmtMessage_AuditDateTime` | String |  |  |
