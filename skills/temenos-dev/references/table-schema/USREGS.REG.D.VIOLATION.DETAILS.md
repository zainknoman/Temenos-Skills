# USREGS.REG.D.VIOLATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.REG.D.VIOLATION.DETAILS` in `USREGS_RegD.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REG.D.VIO.ACCT.TYPE` | `UsregsRegDViolationDetails_AcctType` | TField |  | This field will be used to indicate product type of the violated account. |
| 2 | `REG.D.VIO.MONTH` | `UsregsRegDViolationDetails_Month` | TField |  | Not used; Help text not available. |
| 3 | `REG.D.VIO.RESERVED.17` | `UsregsRegDViolationDetails_Reserved17` | TField |  |  |
| 4 | `REG.D.VIO.STATUS` | `UsregsRegDViolationDetails_Status` | TField |  | Not used; Help text not available. |
| 5 | `REG.D.VIO.REASON` | `UsregsRegDViolationDetails_Reason` | TField |  | Not used; Help text not available. |
| 6 | `REG.D.VIO.ACTIVITY` | `UsregsRegDViolationDetails_Activity` |  |  |  |
| 7 | `REG.D.VIO.ACTIVITY.NAME` | `UsregsRegDViolationDetails_ActivityName` |  |  |  |
| 8 | `REG.D.VIO.ACTIVITY.REF` | `UsregsRegDViolationDetails_ActivityRef` |  |  |  |
| 9 | `REG.D.VIO.DATE` | `UsregsRegDViolationDetails_Date` |  |  |  |
| 10 | `REG.D.VIO.ACTIVITY.COUNT` | `UsregsRegDViolationDetails_ActivityCount` |  |  |  |
| 11 | `REG.D.VIO.RESERVED.15` | `UsregsRegDViolationDetails_Reserved15` |  |  |  |
| 12 | `REG.D.VIO.RESERVED.14` | `UsregsRegDViolationDetails_Reserved14` |  |  |  |
| 13 | `REG.D.VIO.RESERVED.13` | `UsregsRegDViolationDetails_Reserved13` |  |  |  |
| 14 | `REG.D.VIO.TOTAL.TXN.COUNT` | `UsregsRegDViolationDetails_TotalTxnCount` | TField |  | Total number of Regulation-D transaction happened on this statement cycle. |
| 15 | `REG.D.VIO.DECREASE.COUNT.BY` | `UsregsRegDViolationDetails_DecreaseCountBy` | TField |  | This field will be used to reduce the net total of the Regulation-D transaction count. |
| 16 | `REG.D.VIO.DECREASE.COUNT.REASON` | `UsregsRegDViolationDetails_DecreaseCountReason` | TField |  | It will be used to mention the reason for decreasing the transaction count. |
| 17 | `REG.D.VIO.NET.TXN.COUNT` | `UsregsRegDViolationDetails_NetTxnCount` | TField |  | This will be a calculated value by subtracting the decrease count from total transaction count. |
| 18 | `REG.D.VIO.CUSTOMER.NO` | `UsregsRegDViolationDetails_CustomerNo` | TField |  | The customer of the account number will be stored. |
| 19 | `REG.D.VIO.ACCOUNT.NO` | `UsregsRegDViolationDetails_AccountNo` | TField |  | N.A |
| 20 | `REG.D.VIO.STMT.CYCLE.END` | `UsregsRegDViolationDetails_StmtCycleEnd` | TField |  | End date of this statement cycle. It will be updated when the record gets created. It will be account &apos; s statement generation date. |
| 21 | `REG.D.VIO.PRD.CHANGE.DATE` | `UsregsRegDViolationDetails_PrdChangeDate` | TField |  | The effective date of change product activity will be stored here. From this date the account &apos; s product type will be changed to Non-Regulation-D product which parameterized in violation action configuration record. |
| 22 | `REG.D.VIO.PRD.CHANGE.ACTIVITY` | `UsregsRegDViolationDetails_PrdChangeActivity` | TField |  | The activity reference of change product activity. It will be used to reverse the activity when violation status changed from Breached to Not Violated by decreasing the count manually. |
| 23 | `REG.D.VIO.PRD.CHANGE.PRODUCT` | `UsregsRegDViolationDetails_PrdChangeProduct` | TField |  | Target product or new product to which account changed due to change product activity. |
| 24 | `REG.D.VIO.DELIVERY.REF` | `UsregsRegDViolationDetails_DeliveryRef` |  |  |  |
| 25 | `REG.D.VIO.RESERVED.6` | `UsregsRegDViolationDetails_Reserved6` | TField |  |  |
| 26 | `REG.D.VIO.RESERVED.5` | `UsregsRegDViolationDetails_Reserved5` | TField |  |  |
| 27 | `REG.D.VIO.RESERVED.4` | `UsregsRegDViolationDetails_Reserved4` | TField |  |  |
| 28 | `REG.D.VIO.RESERVED.3` | `UsregsRegDViolationDetails_Reserved3` | TField |  |  |
| 29 | `REG.D.VIO.RESERVED.2` | `UsregsRegDViolationDetails_Reserved2` | TField |  |  |
| 30 | `REG.D.VIO.RESERVED.1` | `UsregsRegDViolationDetails_Reserved1` | TField |  |  |
| 31 | `REG.D.VIO.OVERRIDE` | `UsregsRegDViolationDetails_Override` |  |  |  |
| 32 | `REG.D.VIO.RECORD.STATUS` | `UsregsRegDViolationDetails_RecordStatus` | String |  |  |
| 33 | `REG.D.VIO.CURR.NO` | `UsregsRegDViolationDetails_CurrNo` | String |  |  |
| 34 | `REG.D.VIO.INPUTTER` | `UsregsRegDViolationDetails_Inputter` |  |  |  |
| 35 | `REG.D.VIO.DATE.TIME` | `UsregsRegDViolationDetails_DateTime` |  |  |  |
| 36 | `REG.D.VIO.AUTHORISER` | `UsregsRegDViolationDetails_Authoriser` | String |  |  |
| 37 | `REG.D.VIO.CO.CODE` | `UsregsRegDViolationDetails_CoCode` | String |  |  |
| 38 | `REG.D.VIO.DEPT.CODE` | `UsregsRegDViolationDetails_DeptCode` | String |  |  |
| 39 | `REG.D.VIO.AUDITOR.CODE` | `UsregsRegDViolationDetails_AuditorCode` | String |  |  |
| 40 | `REG.D.VIO.AUDIT.DATE.TIME` | `UsregsRegDViolationDetails_AuditDateTime` | String |  |  |
