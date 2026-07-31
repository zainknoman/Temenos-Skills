# STOP.REQUEST.STATUS — Table Schema

> Source: `INSERTS/I_F.STOP.REQUEST.STATUS` in `CQ_ChqPaymentStop.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STP.REQ.DIRECTION` | `StpReqDirection` |  |  |  |
| 2 | `STP.REQ.DRAWER.BANK.ACCOUNT` | `StpReqDrawerBnkAcct` |  |  |  |
| 3 | `STP.REQ.DRAWER.CUSTOMER.NUMBER` | `StpReqDrawerCustNo` |  |  |  |
| 4 | `STP.REQ.CHEQUE.NUMBER` | `StpReqChqNumber` |  |  |  |
| 5 | `STP.REQ.CHEQUE.TYPE` | `StpReqChqType` |  |  |  |
| 6 | `STP.REQ.CHEQUE.CURRENCY` | `StpReqChqCcy` |  |  |  |
| 7 | `STP.REQ.CHEQUE.AMOUNT` | `StpReqChqAmt` |  |  |  |
| 8 | `STP.REQ.DATE.OF.ISSUE` | `StpReqDateOfIss` |  |  |  |
| 9 | `STP.REQ.VALUE.DATE` | `StpReqValueDt` |  |  |  |
| 10 | `STP.REQ.IN.DRAWER.BANK` | `StpReqInDrawerBnk` |  |  |  |
| 11 | `STP.REQ.DRAWEE.BANK.BIC` | `StpReqDraweeBnkBic` |  |  |  |
| 12 | `STP.REQ.IN.PAYEE` | `StpReqInPayee` |  |  |  |
| 13 | `STP.REQ.PAYEE.ACCOUNT.NO` | `StpReqPayeeAccNo` |  |  |  |
| 14 | `STP.REQ.PAYEE.NAME.ADDRESS` | `StpReqPayeeNameAddr` |  |  |  |
| 15 | `STP.REQ.ANSWERS` | `StpReqAnswers` |  |  |  |
| 16 | `STP.REQ.REFERENCE` | `StpReqReference` |  |  |  |
| 17 | `STP.REQ.IN.DELIVERY.REF` | `StpReqInDeliveryRef` |  |  |  |
| 18 | `STP.REQ.IN.PROCESS.ERR` | `StpReqInProcessErr` |  |  |  |
| 19 | `STP.REQ.CHQ.ISSUE.ACCT` | `StpReqChqIssueAcct` |  |  |  |
| 20 | `STP.REQ.RESERVED.5` | `StpReqReserved5` |  |  |  |
| 21 | `STP.REQ.RESERVED.4` | `StpReqReserved4` |  |  |  |
| 22 | `STP.REQ.RESERVED.3` | `StpReqReserved3` |  |  |  |
| 23 | `STP.REQ.RESERVED.2` | `StpReqReserved2` |  |  |  |
| 24 | `STP.REQ.RESERVED.1` | `StpReqReserved1` |  |  |  |
| 25 | `STP.REQ.LOCAL.REF` | `StpReqLocalRef` |  |  |  |
| 26 | `STP.REQ.OVERRIDE` | `StpReqOverride` |  |  |  |
| 27 | `STP.REQ.RECORD.STATUS` | `StpReqRecordStatus` |  |  |  |
| 28 | `STP.REQ.CURR.NO` | `StpReqCurrNo` |  |  |  |
| 29 | `STP.REQ.INPUTTER` | `StpReqInputter` |  |  |  |
| 30 | `STP.REQ.DATE.TIME` | `StpReqDateTime` |  |  |  |
| 31 | `STP.REQ.AUTHORISER` | `StpReqAuthoriser` |  |  |  |
| 32 | `STP.REQ.CO.CODE` | `StpReqCoCode` |  |  |  |
| 33 | `STP.REQ.DEPT.CODE` | `StpReqDeptCode` |  |  |  |
| 34 | `STP.REQ.AUDITOR.CODE` | `StpReqAuditorCode` |  |  |  |
| 35 | `STP.REQ.AUDIT.DATE.TIME` | `StpReqAuditDateTime` |  |  |  |
