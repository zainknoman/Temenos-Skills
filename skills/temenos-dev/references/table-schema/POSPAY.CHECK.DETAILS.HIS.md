# POSPAY.CHECK.DETAILS.HIS — Table Schema

> Source: `INSERTS/I_F.POSPAY.CHECK.DETAILS.HIS` in `USRETL_PositivePay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CHK.CUSTOMER.ID` | `PospayCheckDetailsHis_CustomerId` | TField |  |  |
| 2 | `PP.CHK.ISSUE.DATE` | `PospayCheckDetailsHis_IssueDate` | TField |  |  |
| 3 | `PP.CHK.AMOUNT` | `PospayCheckDetailsHis_Amount` | TField |  |  |
| 4 | `PP.CHK.CURRENCY` | `PospayCheckDetailsHis_Currency` | TField |  |  |
| 5 | `PP.CHK.STATUS` | `PospayCheckDetailsHis_Status` | TField |  |  |
| 6 | `PP.CHK.PROCESS.DATE` | `PospayCheckDetailsHis_ProcessDate` | TField |  |  |
| 7 | `PP.CHK.TRANSACTION.REF` | `PospayCheckDetailsHis_TransactionRef` | TField |  |  |
| 8 | `PP.CHK.ERROR.MESSAGE` | `PospayCheckDetailsHis_ErrorMessage` | TField |  |  |
| 9 | `PP.CHK.COMMENTS` | `PospayCheckDetailsHis_Comments` |  |  |  |
| 10 | `PP.CHK.CUSTOMER.DECISION` | `PospayCheckDetailsHis_CustomerDecision` | TField |  |  |
| 11 | `PP.CHK.CUSTOMER.REASON` | `PospayCheckDetailsHis_CustomerReason` |  |  |  |
| 12 | `PP.CHK.ID.COMP.1` | `PospayCheckDetailsHis_IdComp1` | TField |  |  |
| 13 | `PP.CHK.ID.COMP.2` | `PospayCheckDetailsHis_IdComp2` | TField |  |  |
| 14 | `PP.CHK.RESERVED.10` | `PospayCheckDetailsHis_Reserved10` | TField |  |  |
| 15 | `PP.CHK.RESERVED.9` | `PospayCheckDetailsHis_Reserved9` | TField |  |  |
| 16 | `PP.CHK.RESERVED.8` | `PospayCheckDetailsHis_Reserved8` | TField |  |  |
| 17 | `PP.CHK.RESERVED.7` | `PospayCheckDetailsHis_Reserved7` | TField |  |  |
| 18 | `PP.CHK.RESERVED.6` | `PospayCheckDetailsHis_Reserved6` | TField |  |  |
| 19 | `PP.CHK.RESERVED.5` | `PospayCheckDetailsHis_Reserved5` | TField |  |  |
| 20 | `PP.CHK.RESERVED.4` | `PospayCheckDetailsHis_Reserved4` | TField |  |  |
| 21 | `PP.CHK.RESERVED.3` | `PospayCheckDetailsHis_Reserved3` | TField |  |  |
| 22 | `PP.CHK.RESERVED.2` | `PospayCheckDetailsHis_Reserved2` | TField |  |  |
| 23 | `PP.CHK.RESERVED.1` | `PospayCheckDetailsHis_Reserved1` | TField |  |  |
| 24 | `PP.CHK.RECORD.STATUS` | `PospayCheckDetailsHis_RecordStatus` | String |  |  |
| 25 | `PP.CHK.CURR.NO` | `PospayCheckDetailsHis_CurrNo` | String |  |  |
| 26 | `PP.CHK.INPUTTER` | `PospayCheckDetailsHis_Inputter` |  |  |  |
| 27 | `PP.CHK.DATE.TIME` | `PospayCheckDetailsHis_DateTime` |  |  |  |
| 28 | `PP.CHK.AUTHORISER` | `PospayCheckDetailsHis_Authoriser` | String |  |  |
| 29 | `PP.CHK.CO.CODE` | `PospayCheckDetailsHis_CoCode` | String |  |  |
| 30 | `PP.CHK.DEPT.CODE` | `PospayCheckDetailsHis_DeptCode` | String |  |  |
| 31 | `PP.CHK.AUDITOR.CODE` | `PospayCheckDetailsHis_AuditorCode` | String |  |  |
| 32 | `PP.CHK.AUDIT.DATE.TIME` | `PospayCheckDetailsHis_AuditDateTime` | String |  |  |
