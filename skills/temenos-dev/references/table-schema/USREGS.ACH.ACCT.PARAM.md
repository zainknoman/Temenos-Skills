# USREGS.ACH.ACCT.PARAM — Table Schema

> Source: `INSERTS/I_F.USREGS.ACH.ACCT.PARAM` in `USREGS_ACH.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.ACH.ACCT.DESCRIPTION` | `UsregsAchAcctParam_Description` | TField |  |  |
| 2 | `US.ACH.ACCT.PAYIN.ACCOUNT` | `UsregsAchAcctParam_PayinAccount` |  |  |  |
| 3 | `US.ACH.ACCT.PAYOUT.ACCOUNT` | `UsregsAchAcctParam_PayoutAccount` |  |  |  |
| 4 | `US.ACH.ACCT.ACH.CLEAR.ACC` | `UsregsAchAcctParam_AchClearAcc` | TField |  |  |
| 5 | `US.ACH.ACCT.ACH.RETURN.ACCT` | `UsregsAchAcctParam_AchReturnAcct` | TField |  |  |
| 6 | `US.ACH.ACCT.RESERVED.17` | `UsregsAchAcctParam_Reserved17` | TField |  |  |
| 7 | `US.ACH.ACCT.ACH.VERSION.NAME` | `UsregsAchAcctParam_AchVersionName` | TField |  |  |
| 8 | `US.ACH.ACCT.ACH.TXN.TYPE` | `UsregsAchAcctParam_AchTxnType` |  |  |  |
| 9 | `US.ACH.ACCT.ACCT.TYPE` | `UsregsAchAcctParam_AcctType` |  |  |  |
| 10 | `US.ACH.ACCT.TXN.CODE` | `UsregsAchAcctParam_TxnCode` |  |  |  |
| 11 | `US.ACH.ACCT.RESERVED.16` | `UsregsAchAcctParam_Reserved16` |  |  |  |
| 12 | `US.ACH.ACCT.RESERVED.15` | `UsregsAchAcctParam_Reserved15` |  |  |  |
| 13 | `US.ACH.ACCT.RESERVED.14` | `UsregsAchAcctParam_Reserved14` |  |  |  |
| 14 | `US.ACH.ACCT.RESERVED.13` | `UsregsAchAcctParam_Reserved13` | TField |  |  |
| 15 | `US.ACH.ACCT.RESERVED.12` | `UsregsAchAcctParam_Reserved12` | TField |  |  |
| 16 | `US.ACH.ACCT.RESERVED.11` | `UsregsAchAcctParam_Reserved11` | TField |  |  |
| 17 | `US.ACH.ACCT.RESERVED.10` | `UsregsAchAcctParam_Reserved10` | TField |  |  |
| 18 | `US.ACH.ACCT.RESERVED.9` | `UsregsAchAcctParam_Reserved9` | TField |  |  |
| 19 | `US.ACH.ACCT.RESERVED.8` | `UsregsAchAcctParam_Reserved8` | TField |  |  |
| 20 | `US.ACH.ACCT.RESERVED.7` | `UsregsAchAcctParam_Reserved7` | TField |  |  |
| 21 | `US.ACH.ACCT.RESERVED.6` | `UsregsAchAcctParam_Reserved6` | TField |  |  |
| 22 | `US.ACH.ACCT.RESERVED.5` | `UsregsAchAcctParam_Reserved5` | TField |  |  |
| 23 | `US.ACH.ACCT.RESERVED.4` | `UsregsAchAcctParam_Reserved4` | TField |  |  |
| 24 | `US.ACH.ACCT.RESERVED.3` | `UsregsAchAcctParam_Reserved3` | TField |  |  |
| 25 | `US.ACH.ACCT.RESERVED.2` | `UsregsAchAcctParam_Reserved2` | TField |  |  |
| 26 | `US.ACH.ACCT.RESERVED.1` | `UsregsAchAcctParam_Reserved1` | TField |  |  |
| 27 | `US.ACH.ACCT.RECORD.STATUS` | `UsregsAchAcctParam_RecordStatus` | String |  |  |
| 28 | `US.ACH.ACCT.CURR.NO` | `UsregsAchAcctParam_CurrNo` | String |  |  |
| 29 | `US.ACH.ACCT.INPUTTER` | `UsregsAchAcctParam_Inputter` |  |  |  |
| 30 | `US.ACH.ACCT.DATE.TIME` | `UsregsAchAcctParam_DateTime` |  |  |  |
| 31 | `US.ACH.ACCT.AUTHORISER` | `UsregsAchAcctParam_Authoriser` | String |  |  |
| 32 | `US.ACH.ACCT.CO.CODE` | `UsregsAchAcctParam_CoCode` | String |  |  |
| 33 | `US.ACH.ACCT.DEPT.CODE` | `UsregsAchAcctParam_DeptCode` | String |  |  |
| 34 | `US.ACH.ACCT.AUDITOR.CODE` | `UsregsAchAcctParam_AuditorCode` | String |  |  |
| 35 | `US.ACH.ACCT.AUDIT.DATE.TIME` | `UsregsAchAcctParam_AuditDateTime` | String |  |  |
