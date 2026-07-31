# USRSRS.ACCT.DETAILS — Table Schema

> Source: `INSERTS/I_F.USRSRS.ACCT.DETAILS` in `USRSRS_RetailSweepPgm.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RSW.ACCT.CUSTOMER` | `UsrsrsAcctDetails_Customer` | TField |  | Primary owner of the Account. Validation Rules |
| 2 | `RSW.ACCT.SWEEP.REFERENCE` | `UsrsrsAcctDetails_SweepReference` | TField | Yes | The Reserve Sweep Reference ID is utilized when defining the default Reserve Sweep requirement for a selected T24 Product. Links to the EB.LOOKUP table RETSWEEPPGM Validation Rules Mandatory Field. Multi-Value field set. |
| 3 | `RSW.ACCT.TXN.ACCT` | `UsrsrsAcctDetails_TxnAcct` | TField |  | Account number of the Transaction account. Validation Rules |
| 4 | `RSW.ACCT.TXN.ACCT.STATUS` | `UsrsrsAcctDetails_TxnAcctStatus` | TField |  | Field to indicate the status of the transaction Account. ACTIVE status indicates that the primary account has an active transaction and non-transaction account. CLOSED status indicates that sweep for the primary account has been deactivated and hence the transaction account that was originally created for sweep purpose is now in Closed status. EXCEPTION status indicates that there was an issue with the Account created or Account Closure Process. Validation Rules |
| 5 | `RSW.ACCT.TXN.ACCT.STATUS.DATE` | `UsrsrsAcctDetails_TxnAcctStatusDate` | TField |  | Date on which the transaction account status was updated. Validation Rules |
| 6 | `RSW.ACCT.TXN.ACCT.BAL` | `UsrsrsAcctDetails_TxnAcctBal` | TField |  | Closing balance of the transaction account as of the previous day. Validation Rules |
| 7 | `RSW.ACCT.NONTXN.ACCT` | `UsrsrsAcctDetails_NontxnAcct` | TField |  | Account number of the Non-transaction account. Validation Rules |
| 8 | `RSW.ACCT.NONTXN.ACCT.STATUS` | `UsrsrsAcctDetails_NontxnAcctStatus` | TField |  | Field to indicate the status of the non-transaction Account. ACTIVE status indicates that the primary account has an active transaction and non-transaction account. CLOSED status indicates that sweep for the primary account has been deactivated and hence the transaction account that was originally created for sweep purpose is now in Closed status. EXCEPTION status indicates that there was an issue with the Account created or Account Closure Process. Validation Rules |
| 9 | `RSW.ACCT.NONTXN.ACCT.STATUS.DATE` | `UsrsrsAcctDetails_NontxnAcctStatusDate` | TField |  | Date on which the non-transaction account status was updated. Validation Rules |
| 10 | `RSW.ACCT.NONTXN.ACCT.BAL` | `UsrsrsAcctDetails_NontxnAcctBal` | TField |  | Closing balance of the non-transaction account as of the previous day. Validation Rules |
| 11 | `RSW.ACCT.TARGET.BALANCE` | `UsrsrsAcctDetails_TargetBalance` | TField |  | The target balance that will be considered for sweep between the transaction and non-transaction account.The balance will be reviewed at the start of every month based on the average balance of the Primary account Validation Rules Value should be in ascending order within a sub-value set. |
| 12 | `RSW.ACCT.EFFECTIVE.DATE` | `UsrsrsAcctDetails_EffectiveDate` | TField |  | Date on which the account was created. Validation Rules |
| 13 | `RSW.ACCT.LAST.UPD.DATE` | `UsrsrsAcctDetails_LastUpdDate` | TField |  | Date on which the last update was done. Validation Rules |
| 14 | `RSW.ACCT.RSSW.REGD.CNT` | `UsrsrsAcctDetails_RsswRegdCnt` | TField |  | Number of times there was a balance movement from non-transaction account to transaction account, during the current month, due to negative balances in transaction account. Validation Rules |
| 15 | `RSW.ACCT.RSSW.REGD.VIOLATION` | `UsrsrsAcctDetails_RsswRegdViolation` | TField |  | Field to indicate if Reg D Violation has happened for the reserve sweep requirement.If the field holds a value Y, no further target balance sweeps will be done between Transaction account and Non-transaction account. Validation Rules Yes or Null field |
| 16 | `RSW.ACCT.ACCT.MVMT.TODAY` | `UsrsrsAcctDetails_AcctMvmtToday` | TField |  | Field to indicate if there was any account balance movements for the day that happened on the account.This information will be used by services to identify if the account needs to be picked for processing. During start of month however, all accounts are picked and processed. Validation Rules Yes or Null field |
| 17 | `RSW.ACCT.RESERVE.ACCT.STATUS` | `UsrsrsAcctDetails_ReserveAcctStatus` | TField |  | Field to hold the status of Reserve sweep for the arrangement. Active indicates that the arrangement has a valid sweep linked. If it is set to Cancelled, the sweep process is deactivated. Validation Rules |
| 18 | `RSW.ACCT.LINK.ACCT.NO` | `UsrsrsAcctDetails_LinkAcctNo` | TField |  | T24 Account number of the arrangement Validation Rules |
| 19 | `RSW.ACCT.PRIME.ACCT.CATEGORY` | `UsrsrsAcctDetails_PrimeAcctCategory` | TField |  | Category of the Primary account. Validation Rules |
| 20 | `RSW.ACCT.PRIME.ACCT.BAL` | `UsrsrsAcctDetails_PrimeAcctBal` | TField |  | Closing balance of the Primary as of the previous day. Validation Rules |
| 21 | `RSW.ACCT.PREV.MTH.AVG.BAL` | `UsrsrsAcctDetails_PrevMthAvgBal` | TField |  | Previous Month Average balance of the account based on which the Target Balance was calculated. Validation Rules |
| 22 | `RSW.ACCT.COMPANY` | `UsrsrsAcctDetails_Company` | TField |  | Company or the lead company where the Primary account exists. Validation Rules |
| 23 | `RSW.ACCT.LOCAL.REF` | `UsrsrsAcctDetails_LocalRef` |  |  |  |
| 24 | `RSW.ACCT.TAKEOVER.DATE` | `UsrsrsAcctDetails_TakeoverDate` | TField |  |  |
| 25 | `RSW.ACCT.RESERVED.14` | `UsrsrsAcctDetails_Reserved14` | TField |  |  |
| 26 | `RSW.ACCT.RESERVED.13` | `UsrsrsAcctDetails_Reserved13` | TField |  |  |
| 27 | `RSW.ACCT.RESERVED.12` | `UsrsrsAcctDetails_Reserved12` | TField |  |  |
| 28 | `RSW.ACCT.RESERVED.11` | `UsrsrsAcctDetails_Reserved11` | TField |  |  |
| 29 | `RSW.ACCT.RESERVED.10` | `UsrsrsAcctDetails_Reserved10` | TField |  |  |
| 30 | `RSW.ACCT.RESERVED.9` | `UsrsrsAcctDetails_Reserved9` | TField |  |  |
| 31 | `RSW.ACCT.RESERVED.8` | `UsrsrsAcctDetails_Reserved8` | TField |  |  |
| 32 | `RSW.ACCT.RESERVED.7` | `UsrsrsAcctDetails_Reserved7` | TField |  |  |
| 33 | `RSW.ACCT.RESERVED.6` | `UsrsrsAcctDetails_Reserved6` | TField |  |  |
| 34 | `RSW.ACCT.RESERVED.5` | `UsrsrsAcctDetails_Reserved5` | TField |  |  |
| 35 | `RSW.ACCT.RESERVED.4` | `UsrsrsAcctDetails_Reserved4` | TField |  |  |
| 36 | `RSW.ACCT.RESERVED.3` | `UsrsrsAcctDetails_Reserved3` | TField |  |  |
| 37 | `RSW.ACCT.RESERVED.2` | `UsrsrsAcctDetails_Reserved2` | TField |  |  |
| 38 | `RSW.ACCT.RESERVED.1` | `UsrsrsAcctDetails_Reserved1` | TField |  |  |
