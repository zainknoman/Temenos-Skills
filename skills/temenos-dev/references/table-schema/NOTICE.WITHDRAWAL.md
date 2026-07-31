# NOTICE.WITHDRAWAL — Table Schema

> Source: `INSERTS/I_F.NOTICE.WITHDRAWAL` in `AC_PaymentNetting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SA.NW.NOTICE.DATE` | `NoticeWithdrawal_NoticeDate` |  |  |  |
| 2 | `SA.NW.NOTICE.AMOUNT` | `NoticeWithdrawal_NoticeAmount` |  |  |  |
| 3 | `SA.NW.DATE.AVAIL.FROM` | `NoticeWithdrawal_DateAvailFrom` |  |  |  |
| 4 | `SA.NW.DATE.AVAIL.UPTO` | `NoticeWithdrawal_DateAvailUpto` |  |  |  |
| 5 | `SA.NW.NOTICE.AMT.TAKEN` | `NoticeWithdrawal_NoticeAmtTaken` |  |  |  |
| 6 | `SA.NW.FREE.AMT.TAKEN` | `NoticeWithdrawal_FreeAmtTaken` |  |  |  |
| 7 | `SA.NW.FREE.PERIOD.END` | `NoticeWithdrawal_FreePeriodEnd` |  |  |  |
| 8 | `SA.NW.RESERVED.5` | `NoticeWithdrawal_Reserved5` | TField |  | This field is reserved for future use. |
| 9 | `SA.NW.RESERVED.4` | `NoticeWithdrawal_Reserved4` | TField |  | This field is reserved for future use. |
| 10 | `SA.NW.RESERVED.3` | `NoticeWithdrawal_Reserved3` | TField |  | This field is reserved for future use. |
| 11 | `SA.NW.RESERVED.2` | `NoticeWithdrawal_Reserved2` | TField |  |  |
| 12 | `SA.NW.LOCAL.REF` | `NoticeWithdrawal_LocalRef` |  |  |  |
| 13 | `SA.NW.RECORD.STATUS` | `NoticeWithdrawal_RecordStatus` | String |  |  |
| 14 | `SA.NW.CURR.NO` | `NoticeWithdrawal_CurrNo` | String |  |  |
| 15 | `SA.NW.INPUTTER` | `NoticeWithdrawal_Inputter` |  |  |  |
| 16 | `SA.NW.DATE.TIME` | `NoticeWithdrawal_DateTime` |  |  |  |
| 17 | `SA.NW.AUTHORISER` | `NoticeWithdrawal_Authoriser` | String |  |  |
| 18 | `SA.NW.CO.CODE` | `NoticeWithdrawal_CoCode` | String |  |  |
| 19 | `SA.NW.DEPT.CODE` | `NoticeWithdrawal_DeptCode` | String |  |  |
| 20 | `SA.NW.AUDITOR.CODE` | `NoticeWithdrawal_AuditorCode` | String |  |  |
| 21 | `SA.NW.AUDIT.DATE.TIME` | `NoticeWithdrawal_AuditDateTime` | String |  |  |
