# UB.PAYER.DETAIL — Table Schema

> Source: `INSERTS/I_F.UB.PAYER.DETAIL` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PA.DET.PAYEE.ID` | `UbPayerDetail_PayeeId` |  |  |  |
| 2 | `UB.PA.DET.PAYER.ACCT.NO` | `UbPayerDetail_PayerAcctNo` |  |  |  |
| 3 | `UB.PA.DET.NICK.NAME` | `UbPayerDetail_NickName` |  |  |  |
| 4 | `UB.PA.DET.RESERVED.14` | `UbPayerDetail_Reserved14` |  |  |  |
| 5 | `UB.PA.DET.RESERVED.13` | `UbPayerDetail_Reserved13` |  |  |  |
| 6 | `UB.PA.DET.RESERVED.12` | `UbPayerDetail_Reserved12` |  |  |  |
| 7 | `UB.PA.DET.RESERVED.11` | `UbPayerDetail_Reserved11` |  |  |  |
| 8 | `UB.PA.DET.LOCAL.REF` | `UbPayerDetail_LocalRef` |  |  |  |
| 9 | `UB.PA.DET.RESERVED.10` | `UbPayerDetail_Reserved10` | TField |  |  |
| 10 | `UB.PA.DET.RESERVED.9` | `UbPayerDetail_Reserved9` | TField |  |  |
| 11 | `UB.PA.DET.RESERVED.8` | `UbPayerDetail_Reserved8` | TField |  |  |
| 12 | `UB.PA.DET.RESERVED.7` | `UbPayerDetail_Reserved7` | TField |  |  |
| 13 | `UB.PA.DET.RESERVED.6` | `UbPayerDetail_Reserved6` | TField |  |  |
| 14 | `UB.PA.DET.RESERVED.5` | `UbPayerDetail_Reserved5` | TField |  |  |
| 15 | `UB.PA.DET.RESERVED.4` | `UbPayerDetail_Reserved4` | TField |  |  |
| 16 | `UB.PA.DET.RESERVED.3` | `UbPayerDetail_Reserved3` | TField |  |  |
| 17 | `UB.PA.DET.RESERVED.2` | `UbPayerDetail_Reserved2` | TField |  |  |
| 18 | `UB.PA.DET.RESERVED.1` | `UbPayerDetail_Reserved1` | TField |  |  |
| 19 | `UB.PA.DET.OVERRIDE` | `UbPayerDetail_Override` |  |  |  |
| 20 | `UB.PA.DET.RECORD.STATUS` | `UbPayerDetail_RecordStatus` | String |  |  |
| 21 | `UB.PA.DET.CURR.NO` | `UbPayerDetail_CurrNo` | String |  |  |
| 22 | `UB.PA.DET.INPUTTER` | `UbPayerDetail_Inputter` |  |  |  |
| 23 | `UB.PA.DET.DATE.TIME` | `UbPayerDetail_DateTime` |  |  |  |
| 24 | `UB.PA.DET.AUTHORISER` | `UbPayerDetail_Authoriser` | String |  |  |
| 25 | `UB.PA.DET.CO.CODE` | `UbPayerDetail_CoCode` | String |  |  |
| 26 | `UB.PA.DET.DEPT.CODE` | `UbPayerDetail_DeptCode` | String |  |  |
| 27 | `UB.PA.DET.AUDITOR.CODE` | `UbPayerDetail_AuditorCode` | String |  |  |
| 28 | `UB.PA.DET.AUDIT.DATE.TIME` | `UbPayerDetail_AuditDateTime` | String |  |  |
