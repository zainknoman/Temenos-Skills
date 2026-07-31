# UB.PAYER.ACCT — Table Schema

> Source: `INSERTS/I_F.UB.PAYER.ACCT` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PA.PAYEE.ID` | `UbPayerAcct_PayeeId` |  |  |  |
| 2 | `UB.PA.PAYER.AC.NO` | `UbPayerAcct_PayerAcNo` |  |  |  |
| 3 | `UB.PA.PAYER.FROM.AC` | `UbPayerAcct_PayerFromAc` |  |  |  |
| 4 | `UB.PA.STATUS` | `UbPayerAcct_Status` |  |  |  |
| 5 | `UB.PA.LOCAL.REF` | `UbPayerAcct_LocalRef` |  |  |  |
| 6 | `UB.PA.TIME.STAMP` | `UbPayerAcct_TimeStamp` | TField |  | Field to store the date and time details of the status updation. |
| 7 | `UB.PA.RESERVED.9` | `UbPayerAcct_Reserved9` | TField |  |  |
| 8 | `UB.PA.RESERVED.8` | `UbPayerAcct_Reserved8` | TField |  |  |
| 9 | `UB.PA.RESERVED.7` | `UbPayerAcct_Reserved7` | TField |  |  |
| 10 | `UB.PA.RESERVED.6` | `UbPayerAcct_Reserved6` | TField |  |  |
| 11 | `UB.PA.RESERVED.5` | `UbPayerAcct_Reserved5` | TField |  |  |
| 12 | `UB.PA.RESERVED.4` | `UbPayerAcct_Reserved4` | TField |  |  |
| 13 | `UB.PA.RESERVED.3` | `UbPayerAcct_Reserved3` | TField |  |  |
| 14 | `UB.PA.RESERVED.2` | `UbPayerAcct_Reserved2` | TField |  |  |
| 15 | `UB.PA.RESERVED.1` | `UbPayerAcct_Reserved1` | TField |  |  |
| 16 | `UB.PA.OVERRIDE` | `UbPayerAcct_Override` |  |  |  |
| 17 | `UB.PA.RECORD.STATUS` | `UbPayerAcct_RecordStatus` | String |  |  |
| 18 | `UB.PA.CURR.NO` | `UbPayerAcct_CurrNo` | String |  |  |
| 19 | `UB.PA.INPUTTER` | `UbPayerAcct_Inputter` |  |  |  |
| 20 | `UB.PA.DATE.TIME` | `UbPayerAcct_DateTime` |  |  |  |
| 21 | `UB.PA.AUTHORISER` | `UbPayerAcct_Authoriser` | String |  |  |
| 22 | `UB.PA.CO.CODE` | `UbPayerAcct_CoCode` | String |  |  |
| 23 | `UB.PA.DEPT.CODE` | `UbPayerAcct_DeptCode` | String |  |  |
| 24 | `UB.PA.AUDITOR.CODE` | `UbPayerAcct_AuditorCode` | String |  |  |
| 25 | `UB.PA.AUDIT.DATE.TIME` | `UbPayerAcct_AuditDateTime` | String |  |  |
| 26 | `UB.PA.NICK.NAME` | `UbPayerAcct_NickName` |  |  |  |
