# USREGS.FDIC.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.USREGS.FDIC.TRANSACTION` in `USREGS_FDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDIC.TXN.DESCRIPTION` | `UsregsFdicTransaction_Description` |  |  |  |
| 2 | `FDIC.TXN.EFFECTIVE.DATE` | `UsregsFdicTransaction_EffectiveDate` | TField |  | Effective date to create AC.LOCKED.EVENTS for an account |
| 3 | `FDIC.TXN.EXPIRATION.DATE` | `UsregsFdicTransaction_ExpirationDate` | TField |  | Expiration date to create AC.LOCKED.EVENTS for an account |
| 4 | `FDIC.TXN.FDIC.FILE.NAME` | `UsregsFdicTransaction_FdicFileName` | TField |  | FDIC file name |
| 5 | `FDIC.TXN.ACCOUNT` | `UsregsFdicTransaction_Account` |  |  |  |
| 6 | `FDIC.TXN.CURRENCY` | `UsregsFdicTransaction_Currency` |  |  |  |
| 7 | `FDIC.TXN.BALANCE.THRESHOLD` | `UsregsFdicTransaction_BalanceThreshold` |  |  |  |
| 8 | `FDIC.TXN.HOLD.PERCENTAGE` | `UsregsFdicTransaction_HoldPercentage` |  |  |  |
| 9 | `FDIC.TXN.RESERVED.15` | `UsregsFdicTransaction_Reserved15` |  |  |  |
| 10 | `FDIC.TXN.RESERVED.14` | `UsregsFdicTransaction_Reserved14` |  |  |  |
| 11 | `FDIC.TXN.RESERVED.13` | `UsregsFdicTransaction_Reserved13` |  |  |  |
| 12 | `FDIC.TXN.RESERVED.12` | `UsregsFdicTransaction_Reserved12` |  |  |  |
| 13 | `FDIC.TXN.RESERVED.11` | `UsregsFdicTransaction_Reserved11` |  |  |  |
| 14 | `FDIC.TXN.TXN.TYPE` | `UsregsFdicTransaction_TxnType` | TField |  | Transaction types can be AUTO.HOLD,MANUAL.HOLD,HOLD.FILE,TRANS.FILE. |
| 15 | `FDIC.TXN.STATUS` | `UsregsFdicTransaction_Status` | TField |  | Status of the Transaction |
| 16 | `FDIC.TXN.RESERVED.10` | `UsregsFdicTransaction_Reserved10` | TField |  |  |
| 17 | `FDIC.TXN.RESERVED.9` | `UsregsFdicTransaction_Reserved9` | TField |  |  |
| 18 | `FDIC.TXN.RESERVED.8` | `UsregsFdicTransaction_Reserved8` | TField |  |  |
| 19 | `FDIC.TXN.RESERVED.7` | `UsregsFdicTransaction_Reserved7` | TField |  |  |
| 20 | `FDIC.TXN.RESERVED.6` | `UsregsFdicTransaction_Reserved6` | TField |  |  |
| 21 | `FDIC.TXN.RESERVED.5` | `UsregsFdicTransaction_Reserved5` | TField |  |  |
| 22 | `FDIC.TXN.RESERVED.4` | `UsregsFdicTransaction_Reserved4` | TField |  |  |
| 23 | `FDIC.TXN.RESERVED.3` | `UsregsFdicTransaction_Reserved3` | TField |  |  |
| 24 | `FDIC.TXN.RESERVED.2` | `UsregsFdicTransaction_Reserved2` | TField |  |  |
| 25 | `FDIC.TXN.RESERVED.1` | `UsregsFdicTransaction_Reserved1` | TField |  |  |
| 26 | `FDIC.TXN.LOCAL.REF` | `UsregsFdicTransaction_LocalRef` |  |  |  |
| 27 | `FDIC.TXN.OVERRIDE` | `UsregsFdicTransaction_Override` |  |  |  |
| 28 | `FDIC.TXN.RECORD.STATUS` | `UsregsFdicTransaction_RecordStatus` | String |  |  |
| 29 | `FDIC.TXN.CURR.NO` | `UsregsFdicTransaction_CurrNo` | String |  |  |
| 30 | `FDIC.TXN.INPUTTER` | `UsregsFdicTransaction_Inputter` |  |  |  |
| 31 | `FDIC.TXN.DATE.TIME` | `UsregsFdicTransaction_DateTime` |  |  |  |
| 32 | `FDIC.TXN.AUTHORISER` | `UsregsFdicTransaction_Authoriser` | String |  |  |
| 33 | `FDIC.TXN.CO.CODE` | `UsregsFdicTransaction_CoCode` | String |  |  |
| 34 | `FDIC.TXN.DEPT.CODE` | `UsregsFdicTransaction_DeptCode` | String |  |  |
| 35 | `FDIC.TXN.AUDITOR.CODE` | `UsregsFdicTransaction_AuditorCode` | String |  |  |
| 36 | `FDIC.TXN.AUDIT.DATE.TIME` | `UsregsFdicTransaction_AuditDateTime` | String |  |  |
