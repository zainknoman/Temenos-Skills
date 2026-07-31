# POSPAY.CHECK.DETAILS — Table Schema

> Source: `INSERTS/I_F.POSPAY.CHECK.DETAILS` in `USRETL_PositivePay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CHK.CUSTOMER.ID` | `PospayCheckDetails_CustomerId` | TField |  |  |
| 2 | `PP.CHK.ISSUE.DATE` | `PospayCheckDetails_IssueDate` | TField |  |  |
| 3 | `PP.CHK.AMOUNT` | `PospayCheckDetails_Amount` | TField |  |  |
| 4 | `PP.CHK.CURRENCY` | `PospayCheckDetails_Currency` | TField |  |  |
| 5 | `PP.CHK.STATUS` | `PospayCheckDetails_Status` | TField |  |  |
| 6 | `PP.CHK.PROCESS.DATE` | `PospayCheckDetails_ProcessDate` | TField |  |  |
| 7 | `PP.CHK.TRANSACTION.REF` | `PospayCheckDetails_TransactionRef` | TField |  |  |
| 8 | `PP.CHK.ERROR.MESSAGE` | `PospayCheckDetails_ErrorMessage` | TField |  |  |
| 9 | `PP.CHK.COMMENTS` | `PospayCheckDetails_Comments` |  |  |  |
| 10 | `PP.CHK.CUSTOMER.DECISION` | `PospayCheckDetails_CustomerDecision` | TField |  |  |
| 11 | `PP.CHK.CUSTOMER.REASON` | `PospayCheckDetails_CustomerReason` |  |  |  |
| 12 | `PP.CHK.ID.COMP.1` | `PospayCheckDetails_IdComp1` | TField |  |  |
| 13 | `PP.CHK.ID.COMP.2` | `PospayCheckDetails_IdComp2` | TField |  |  |
| 14 | `PP.CHK.RESERVED.10` | `PospayCheckDetails_Reserved10` | TField |  |  |
| 15 | `PP.CHK.RESERVED.9` | `PospayCheckDetails_Reserved9` | TField |  |  |
| 16 | `PP.CHK.RESERVED.8` | `PospayCheckDetails_Reserved8` | TField |  |  |
| 17 | `PP.CHK.RESERVED.7` | `PospayCheckDetails_Reserved7` | TField |  |  |
| 18 | `PP.CHK.RESERVED.6` | `PospayCheckDetails_Reserved6` | TField |  |  |
| 19 | `PP.CHK.RESERVED.5` | `PospayCheckDetails_Reserved5` | TField |  |  |
| 20 | `PP.CHK.RESERVED.4` | `PospayCheckDetails_Reserved4` | TField |  |  |
| 21 | `PP.CHK.RESERVED.3` | `PospayCheckDetails_Reserved3` | TField |  |  |
| 22 | `PP.CHK.RESERVED.2` | `PospayCheckDetails_Reserved2` | TField |  |  |
| 23 | `PP.CHK.RESERVED.1` | `PospayCheckDetails_Reserved1` | TField |  |  |
| 24 | `PP.CHK.RECORD.STATUS` | `PospayCheckDetails_RecordStatus` | String |  |  |
| 25 | `PP.CHK.CURR.NO` | `PospayCheckDetails_CurrNo` | String |  |  |
| 26 | `PP.CHK.INPUTTER` | `PospayCheckDetails_Inputter` |  |  |  |
| 27 | `PP.CHK.DATE.TIME` | `PospayCheckDetails_DateTime` |  |  |  |
| 28 | `PP.CHK.AUTHORISER` | `PospayCheckDetails_Authoriser` | String |  |  |
| 29 | `PP.CHK.CO.CODE` | `PospayCheckDetails_CoCode` | String |  |  |
| 30 | `PP.CHK.DEPT.CODE` | `PospayCheckDetails_DeptCode` | String |  |  |
| 31 | `PP.CHK.AUDITOR.CODE` | `PospayCheckDetails_AuditorCode` | String |  |  |
| 32 | `PP.CHK.AUDIT.DATE.TIME` | `PospayCheckDetails_AuditDateTime` | String |  |  |
