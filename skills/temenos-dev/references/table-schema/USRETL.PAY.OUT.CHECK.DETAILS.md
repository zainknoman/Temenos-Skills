# USRETL.PAY.OUT.CHECK.DETAILS — Table Schema

> Source: `INSERTS/I_F.USRETL.PAY.OUT.CHECK.DETAILS` in `USRETL_CheckProduction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USRETL.POCD.CUSTOMER` | `UsretlPayOutCheckDetails_Customer` | TField |  | This field is used to store the CUSTOMER id for the check to be produced. Must be a valid CUSTOMER ID |
| 2 | `USRETL.POCD.ARRANGEMENT` | `UsretlPayOutCheckDetails_Arrangement` | TField |  | This field is used to store the ARRANGEMENT ID for the check to be produced. Must be a valid AA.ARRANGEMENT ID |
| 3 | `USRETL.POCD.PROPERTY.CLASS` | `UsretlPayOutCheckDetails_PropertyClass` | TField |  | This field is used to store the PROPERTY.CLASS id for the check to be produced. To identify which of the property class that the bill has been raised. Must be a valid AA.PROPERTY.CLASS ID |
| 4 | `USRETL.POCD.AMOUNT` | `UsretlPayOutCheckDetails_Amount` | TField |  | This field is used to store the amount value for the check to be produced. Initially it will be same as issue amount field value. To identify which bill amount has been raised during ISSUE.BILL. During MAKE.DUE if the amount varies from ISSUE.BILL then that amount will be updated. |
| 5 | `USRETL.POCD.DATE` | `UsretlPayOutCheckDetails_Date` | TField |  | This field is used to store the date for check to be produced. Initially it will be same as issue date field value. To identify which bill date has been raised during ISSUE.BILL. During MAKE.DUE if the date varies from ISSUE.BILL then that date will be updated. |
| 6 | `USRETL.POCD.DUE.AMOUNT` | `UsretlPayOutCheckDetails_DueAmount` | TField |  | This field is used to store the due amount value. To identify the bill due amount has been raised during MAKE.DUE. During MAKE.DUE if the amount varies from ISSUE.BILL then only the due amount will be updated. |
| 7 | `USRETL.POCD.DUE.DATE` | `UsretlPayOutCheckDetails_DueDate` | TField |  | This field is used to store the due date. To identify the bill due date has been raised during MAKE.DUE. During MAKE.DUE if the amount varies from ISSUE.BILL then only the due date will be updated. |
| 8 | `USRETL.POCD.ISSUE.AMOUNT` | `UsretlPayOutCheckDetails_IssueAmount` | TField |  | This field is used to store the issue amount value. To identify which bill amount has been raised during ISSUE.BILL. |
| 9 | `USRETL.POCD.ISSUE.DATE` | `UsretlPayOutCheckDetails_IssueDate` | TField |  | This field is used to store the issue date value. To identify which bill date has been raised during ISSUE.BILL. |
| 10 | `USRETL.POCD.REVIEW.STATUS` | `UsretlPayOutCheckDetails_ReviewStatus` | TField |  | This field is used to store the review status. During MAKE.DUE if the date varies from ISSUE.BILL then review status will be updated as PENDING. Valid options are PENDING and REVIEWED |
| 11 | `USRETL.POCD.ESCROW.REFUND` | `UsretlPayOutCheckDetails_EscrowRefund` | TField |  |  |
| 12 | `USRETL.POCD.PROCESS.FLAG` | `UsretlPayOutCheckDetails_ProcessFlag` | TField |  |  |
| 13 | `USRETL.POCD.RESERVED.18` | `UsretlPayOutCheckDetails_Reserved18` | TField |  |  |
| 14 | `USRETL.POCD.RESERVED.17` | `UsretlPayOutCheckDetails_Reserved17` | TField |  |  |
| 15 | `USRETL.POCD.RESERVED.16` | `UsretlPayOutCheckDetails_Reserved16` | TField |  |  |
| 16 | `USRETL.POCD.RESERVED.15` | `UsretlPayOutCheckDetails_Reserved15` | TField |  |  |
| 17 | `USRETL.POCD.RESERVED.14` | `UsretlPayOutCheckDetails_Reserved14` | TField |  |  |
| 18 | `USRETL.POCD.RESERVED.13` | `UsretlPayOutCheckDetails_Reserved13` | TField |  |  |
| 19 | `USRETL.POCD.RESERVED.12` | `UsretlPayOutCheckDetails_Reserved12` | TField |  |  |
| 20 | `USRETL.POCD.RESERVED.11` | `UsretlPayOutCheckDetails_Reserved11` | TField |  |  |
| 21 | `USRETL.POCD.RESERVED.10` | `UsretlPayOutCheckDetails_Reserved10` | TField |  |  |
| 22 | `USRETL.POCD.RESERVED.9` | `UsretlPayOutCheckDetails_Reserved9` | TField |  |  |
| 23 | `USRETL.POCD.RESERVED.8` | `UsretlPayOutCheckDetails_Reserved8` | TField |  |  |
| 24 | `USRETL.POCD.RESERVED.7` | `UsretlPayOutCheckDetails_Reserved7` | TField |  |  |
| 25 | `USRETL.POCD.RESERVED.6` | `UsretlPayOutCheckDetails_Reserved6` | TField |  |  |
| 26 | `USRETL.POCD.RESERVED.5` | `UsretlPayOutCheckDetails_Reserved5` | TField |  |  |
| 27 | `USRETL.POCD.RESERVED.4` | `UsretlPayOutCheckDetails_Reserved4` | TField |  |  |
| 28 | `USRETL.POCD.RESERVED.3` | `UsretlPayOutCheckDetails_Reserved3` | TField |  |  |
| 29 | `USRETL.POCD.RESERVED.2` | `UsretlPayOutCheckDetails_Reserved2` | TField |  |  |
| 30 | `USRETL.POCD.RESERVED.1` | `UsretlPayOutCheckDetails_Reserved1` | TField |  |  |
| 31 | `USRETL.POCD.RECORD.STATUS` | `UsretlPayOutCheckDetails_RecordStatus` | String |  |  |
| 32 | `USRETL.POCD.CURR.NO` | `UsretlPayOutCheckDetails_CurrNo` | String |  |  |
| 33 | `USRETL.POCD.INPUTTER` | `UsretlPayOutCheckDetails_Inputter` |  |  |  |
| 34 | `USRETL.POCD.DATE.TIME` | `UsretlPayOutCheckDetails_DateTime` |  |  |  |
| 35 | `USRETL.POCD.AUTHORISER` | `UsretlPayOutCheckDetails_Authoriser` | String |  |  |
| 36 | `USRETL.POCD.CO.CODE` | `UsretlPayOutCheckDetails_CoCode` | String |  |  |
| 37 | `USRETL.POCD.DEPT.CODE` | `UsretlPayOutCheckDetails_DeptCode` | String |  |  |
| 38 | `USRETL.POCD.AUDITOR.CODE` | `UsretlPayOutCheckDetails_AuditorCode` | String |  |  |
| 39 | `USRETL.POCD.AUDIT.DATE.TIME` | `UsretlPayOutCheckDetails_AuditDateTime` | String |  |  |
