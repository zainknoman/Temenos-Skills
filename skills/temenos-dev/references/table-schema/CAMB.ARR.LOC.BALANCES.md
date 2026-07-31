# CAMB.ARR.LOC.BALANCES — Table Schema

> Source: `INSERTS/I_F.CAMB.ARR.LOC.BALANCES` in `CALOCR_LineOfCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LOCB.NXT.PYMT.DUE.DATE` | `CambArrLocBalances_NxtPymtDueDate` | TField |  | Indicates the date on which the minimum amount has to be paid. |
| 2 | `LOCB.MIN.PYMT.AMOUNT` | `CambArrLocBalances_MinPymtAmount` | TField |  | This field is used to capture the minimum payment amount based on the next payment due date. The value is in CAMB.L.LOC.BAL.DETAILS |
| 3 | `LOCB.PAST.DUE.DATE` | `CambArrLocBalances_PastDueDate` | TField |  | Indicates the date on which the LOC goes past due. This field will always maintain the oldest date that the LOC went past due. |
| 4 | `LOCB.PAST.DUE.BALANCE` | `CambArrLocBalances_PastDueBalance` | TField |  | Contains the total Delinquent Balance as of the current day. This field will hold the cumulative total of balances that went delinquent over multiple interest periods |
| 5 | `LOCB.TOTAL.DUE` | `CambArrLocBalances_TotalDue` | TField |  | Total Balance Due that includes the sum of Minimum Payment Amount and Past Due Balance. |
| 6 | `LOCB.REQ.FOR.CLOSURE` | `CambArrLocBalances_ReqForClosure` | TField |  |  |
| 7 | `LOCB.CLOSURE.DATE` | `CambArrLocBalances_ClosureDate` | TField |  | Indicates the date the LOC is closed. Field gets updated during the closure activity of the LOC and details are moved to CAMB.ARR.LOC.BALANCES.HIST table, and field will be blank if LOC is live. |
| 8 | `LOCB.LAST.ACTIVITY` | `CambArrLocBalances_LastActivity` | TField |  | Indicate the last activity triggered on the account. Valid record of AA.ACTIVITY. |
| 9 | `LOCB.PD.STATUS` | `CambArrLocBalances_PdStatus` |  |  |  |
| 10 | `LOCB.PD.START.DATE` | `CambArrLocBalances_PdStartDate` |  |  |  |
| 11 | `LOCB.PD.END.DATE` | `CambArrLocBalances_PdEndDate` |  |  |  |
| 12 | `LOCB.PD.STATUS.COUNT` | `CambArrLocBalances_PdStatusCount` |  |  |  |
| 13 | `LOCB.PD.TOTAL.DAYS` | `CambArrLocBalances_PdTotalDays` |  |  |  |
| 14 | `LOCB.PD.BALANCE` | `CambArrLocBalances_PdBalance` |  |  |  |
| 15 | `LOCB.PD.OS.BALANCE` | `CambArrLocBalances_PdOsBalance` |  |  |  |
| 16 | `LOCB.DEEMED.SETTLE` | `CambArrLocBalances_DeemedSettle` |  |  |  |
| 17 | `LOCB.DR.INTEREST.AMT` | `CambArrLocBalances_DrInterestAmt` |  |  |  |
| 18 | `LOCB.DR.INTEREST.DATE` | `CambArrLocBalances_DrInterestDate` |  |  |  |
| 19 | `LOCB.REPAY.DATE` | `CambArrLocBalances_RepayDate` |  |  |  |
| 20 | `LOCB.REPAY.AMT` | `CambArrLocBalances_RepayAmt` |  |  |  |
| 21 | `LOCB.OVER.PD.STATUS` | `CambArrLocBalances_OverPdStatus` | TField |  | Indicates the overall PD Status. Worst status will be updated in this field and AA. |
| 22 | `LOCB.REASON.DELIQ.CURE` | `CambArrLocBalances_ReasonDeliqCure` | TField |  | Field to hold the reason for delinquency cure. |
| 23 | `LOCB.REASON.CHANGE` | `CambArrLocBalances_ReasonChange` |  |  |  |
| 24 | `LOCB.CHANGE.DETAILS` | `CambArrLocBalances_ChangeDetails` |  |  |  |
| 25 | `LOCB.REASON.CHANGE.DATE` | `CambArrLocBalances_ReasonChangeDate` |  |  |  |
| 26 | `LOCB.LAST.PAY.DATE` | `CambArrLocBalances_LastPayDate` | TField |  | Indicate the last repayment date towards LOC. Valid date field. |
| 27 | `LOCB.ACTUAL.MIN.PYMT.AMT` | `CambArrLocBalances_ActualMinPymtAmt` | TField |  | Indicates the actual minimum payment amount as of the next payment due date. |
| 28 | `LOCB.RECORD.STATUS` | `CambArrLocBalances_RecordStatus` | String |  |  |
| 29 | `LOCB.CURR.NO` | `CambArrLocBalances_CurrNo` | String |  |  |
| 30 | `LOCB.INPUTTER` | `CambArrLocBalances_Inputter` |  |  |  |
| 31 | `LOCB.DATE.TIME` | `CambArrLocBalances_DateTime` |  |  |  |
| 32 | `LOCB.AUTHORISER` | `CambArrLocBalances_Authoriser` | String |  |  |
| 33 | `LOCB.CO.CODE` | `CambArrLocBalances_CoCode` | String |  |  |
| 34 | `LOCB.DEPT.CODE` | `CambArrLocBalances_DeptCode` | String |  |  |
| 35 | `LOCB.AUDITOR.CODE` | `CambArrLocBalances_AuditorCode` | String |  |  |
| 36 | `LOCB.AUDIT.DATE.TIME` | `CambArrLocBalances_AuditDateTime` | String |  |  |
