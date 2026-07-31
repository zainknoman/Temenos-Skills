# PROLENDER.PAY.OUT — Table Schema

> Source: `INSERTS/I_F.PROLENDER.PAY.OUT` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRL.PO.REQ.RQ` | `ProlenderPayOut_ReqRq` |  |  |  |
| 2 | `PRL.PO.REQ.DESC` | `ProlenderPayOut_ReqDesc` |  |  |  |
| 3 | `PRL.PO.CUID` | `ProlenderPayOut_Cuid` |  |  |  |
| 4 | `PRL.PO.USERID` | `ProlenderPayOut_Userid` |  |  |  |
| 5 | `PRL.PO.PASSWORD` | `ProlenderPayOut_Password` |  |  |  |
| 6 | `PRL.PO.REQUEST.ID` | `ProlenderPayOut_RequestId` |  |  |  |
| 7 | `PRL.PO.TIMESTAMP` | `ProlenderPayOut_Timestamp` |  |  |  |
| 8 | `PRL.PO.STATUS.CODE` | `ProlenderPayOut_StatusCode` |  |  |  |
| 9 | `PRL.PO.ENTITY.CODE` | `ProlenderPayOut_EntityCode` |  |  |  |
| 10 | `PRL.PO.ENTITY.TYPE` | `ProlenderPayOut_EntityType` |  |  |  |
| 11 | `PRL.PO.MESSAGE.CODE` | `ProlenderPayOut_MessageCode` |  |  |  |
| 12 | `PRL.PO.MESSAGE.TEXT` | `ProlenderPayOut_MessageText` |  |  |  |
| 13 | `PRL.PO.LOAN.ACCOUNT.NO` | `ProlenderPayOut_LoanAccountNo` |  |  |  |
| 14 | `PRL.PO.TRAN.CODE` | `ProlenderPayOut_TranCode` |  |  |  |
| 15 | `PRL.PO.EFFECTIVE.DATE` | `ProlenderPayOut_EffectiveDate` |  |  |  |
| 16 | `PRL.PO.PAYOUT.AMOUNT` | `ProlenderPayOut_PayoutAmount` |  |  |  |
| 17 | `PRL.PO.RECORD.STATUS` | `ProlenderPayOut_RecordStatus` |  |  |  |
| 18 | `PRL.PO.CURR.NO` | `ProlenderPayOut_CurrNo` |  |  |  |
| 19 | `PRL.PO.INPUTTER` | `ProlenderPayOut_Inputter` |  |  |  |
| 20 | `PRL.PO.DATE.TIME` | `ProlenderPayOut_DateTime` |  |  |  |
| 21 | `PRL.PO.AUTHORISER` | `ProlenderPayOut_Authoriser` |  |  |  |
| 22 | `PRL.PO.CO.CODE` | `ProlenderPayOut_CoCode` |  |  |  |
| 23 | `PRL.PO.DEPT.CODE` | `ProlenderPayOut_DeptCode` |  |  |  |
| 24 | `PRL.PO.AUDITOR.CODE` | `ProlenderPayOut_AuditorCode` |  |  |  |
| 25 | `PRL.PO.AUDIT.DATE.TIME` | `ProlenderPayOut_AuditDateTime` |  |  |  |
