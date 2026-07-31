# ATM.STMT.REQ — Table Schema

> Source: `INSERTS/I_F.ATM.STMT.REQ` in `ATMFRM_Statement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ATM.STMT.ACCT.NO` | `AtmStmtReq_AcctNo` |  |  |  |
| 2 | `ATM.STMT.CUSTOMER.ID` | `AtmStmtReq_CustomerId` |  |  |  |
| 3 | `ATM.STMT.REQ.DATE` | `AtmStmtReq_ReqDate` |  |  |  |
| 4 | `ATM.STMT.REQ.STATUS` | `AtmStmtReq_ReqStatus` |  |  |  |
| 5 | `ATM.STMT.STMT.PERIOD` | `AtmStmtReq_StmtPeriod` |  |  |  |
| 6 | `ATM.STMT.LOCAL.REF` | `AtmStmtReq_LocalRef` |  |  |  |
| 7 | `ATM.STMT.RESERVED.9` | `AtmStmtReq_Reserved9` |  |  |  |
| 8 | `ATM.STMT.RESERVED.8` | `AtmStmtReq_Reserved8` |  |  |  |
| 9 | `ATM.STMT.RESERVED.7` | `AtmStmtReq_Reserved7` |  |  |  |
| 10 | `ATM.STMT.RESERVED.6` | `AtmStmtReq_Reserved6` |  |  |  |
| 11 | `ATM.STMT.RESERVED.5` | `AtmStmtReq_Reserved5` |  |  |  |
| 12 | `ATM.STMT.RESERVED.4` | `AtmStmtReq_Reserved4` |  |  |  |
| 13 | `ATM.STMT.RESERVED.3` | `AtmStmtReq_Reserved3` |  |  |  |
| 14 | `ATM.STMT.RESERVED.2` | `AtmStmtReq_Reserved2` |  |  |  |
| 15 | `ATM.STMT.RESERVED.1` | `AtmStmtReq_Reserved1` |  |  |  |
| 16 | `ATM.STMT.OVERRIDE` | `AtmStmtReq_Override` |  |  |  |
| 17 | `ATM.STMT.RECORD.STATUS` | `AtmStmtReq_RecordStatus` |  |  |  |
| 18 | `ATM.STMT.CURR.NO` | `AtmStmtReq_CurrNo` |  |  |  |
| 19 | `ATM.STMT.INPUTTER` | `AtmStmtReq_Inputter` |  |  |  |
| 20 | `ATM.STMT.DATE.TIME` | `AtmStmtReq_DateTime` |  |  |  |
| 21 | `ATM.STMT.AUTHORISER` | `AtmStmtReq_Authoriser` |  |  |  |
| 22 | `ATM.STMT.CO.CODE` | `AtmStmtReq_CoCode` |  |  |  |
| 23 | `ATM.STMT.DEPT.CODE` | `AtmStmtReq_DeptCode` |  |  |  |
| 24 | `ATM.STMT.AUDITOR.CODE` | `AtmStmtReq_AuditorCode` |  |  |  |
| 25 | `ATM.STMT.AUDIT.DATE.TIME` | `AtmStmtReq_AuditDateTime` |  |  |  |
