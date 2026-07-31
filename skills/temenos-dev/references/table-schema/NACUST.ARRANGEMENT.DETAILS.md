# NACUST.ARRANGEMENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.NACUST.ARRANGEMENT.DETAILS` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NA.ARR.FIN.MVMT.FLAG` | `NacustArrangementDetails_FinMvmtFlag` | TField |  | Y or N field to indicate if there were any financial activity in the arrangement. Validation Rules |
| 2 | `NA.ARR.FIN.MVMT.DATE` | `NacustArrangementDetails_FinMvmtDate` | TField |  | Date on which the last financial activity occurred in the arrangement. Validation Rules |
| 3 | `NA.ARR.AUTO.CLOSURE.DATE` | `NacustArrangementDetails_AutoClosureDate` | TField |  | This is the date when the auto closure status last updated |
| 4 | `NA.ARR.AUTO.CLOSURE.TYPE` | `NacustArrangementDetails_AutoClosureType` | TField |  | The account status that triggers auto account closure Possible values OVERDRAFT ESCHEAT |
| 5 | `NA.ARR.AUTO.CLOSURE.STATUS` | `NacustArrangementDetails_AutoClosureStatus` | TField |  | Status to indicate the various stages of account closure process Possible values applicable for auto closure type OVERDRAFT PRE.CLOSURE - When the overdraft status of account is moved to PRC in OVERDRAFT.STATUS field in table AA.ACCOUNT.DETAILS CLOSURE.MAINTENANCE - When the overdraft status of account moves to ATC in OVERDRAFT.STATUS field in table AA.ACCOUNT.DETAILS TXN.CLOSURE - This is the status when the system initiates the closure process to happen during COB STOPPED - When there is any exception in auto closure process during COB after N number of retries, status will be moved to stopped. Number of retries should be parameterized in table USRETL.PARAMETER in field AC.CLOSE.MAX.ATTEMPTS COMPLETED - When account closure is successfully completed. Possible values applicable for auto closure type ESCHEAT TXN.CLOSURE - This is the status when the system initiates the closure process to happen during COB STOPPED - When there is any exception in auto closure process during COB after N number of retries, status will be moved to stopped. Number of retries should be parameterized in table USRETL.PARAMETER in field AC.CLOSE.MAX.ATTEMPTS COMPLETED - When account closure is successfully completed. |
| 6 | `NA.ARR.AUTO.CLOSURE.REASON` | `NacustArrangementDetails_AutoClosureReason` | TField |  | The reason for account closure. |
| 7 | `NA.ARR.CLOSURE.ERROR.REASON` | `NacustArrangementDetails_ClosureErrorReason` |  |  |  |
| 8 | `NA.ARR.ACCRUED.INTEREST` | `NacustArrangementDetails_AccruedInterest` | TField |  | The total of accrued interest if any during OD period as on closing date. |
| 9 | `NA.ARR.RETAINED.CHARGES` | `NacustArrangementDetails_RetainedCharges` | TField |  | The total of deferred and due charges on account closure. |
| 10 | `NA.ARR.OD.CHARGE` | `NacustArrangementDetails_OdCharge` | TField |  | The total of NSF/OD charges on account closure. |
| 11 | `NA.ARR.CHGOFF.AMOUNT` | `NacustArrangementDetails_ChgoffAmount` | TField |  | The charge off amount of the account during closure excluding NSF/OD Charge. |
| 12 | `NA.ARR.CLOSE.ATTEMPTS.CNT` | `NacustArrangementDetails_CloseAttemptsCnt` | TField |  | Number of attempts made to perform the account closure. |
| 13 | `NA.ARR.LAST.ACTIVITY.DATE` | `NacustArrangementDetails_LastActivityDate` | TField |  | Maintains the activity date for qualified customer initiated transaction. |
| 14 | `NA.ARR.ACTIVITY.REF` | `NacustArrangementDetails_ActivityRef` |  |  |  |
| 15 | `NA.ARR.ACTIVITY.DATE` | `NacustArrangementDetails_ActivityDate` |  |  |  |
| 16 | `NA.ARR.NA.ARR.DUE.CHARGES` | `NacustArrangementDetails_DueCharges` | TField |  |  |
| 17 | `NA.ARR.ACCT.OD.STATUS` | `NacustArrangementDetails_AcctOdStatus` | TField |  |  |
| 18 | `NA.ARR.ACCT.OPEN.STATE` | `NacustArrangementDetails_AcctOpenState` | TField |  | Denotes the state in which account was opened. |
| 19 | `NA.ARR.RESERVED.9` | `NacustArrangementDetails_Reserved9` | TField |  |  |
| 20 | `NA.ARR.RESERVED.8` | `NacustArrangementDetails_Reserved8` | TField |  |  |
| 21 | `NA.ARR.RESERVED.7` | `NacustArrangementDetails_Reserved7` | TField |  |  |
| 22 | `NA.ARR.RESERVED.6` | `NacustArrangementDetails_Reserved6` | TField |  |  |
| 23 | `NA.ARR.RESERVED.5` | `NacustArrangementDetails_Reserved5` | TField |  |  |
| 24 | `NA.ARR.RESERVED.4` | `NacustArrangementDetails_Reserved4` | TField |  |  |
| 25 | `NA.ARR.RESERVED.3` | `NacustArrangementDetails_Reserved3` | TField |  |  |
| 26 | `NA.ARR.RESERVED.2` | `NacustArrangementDetails_Reserved2` | TField |  |  |
| 27 | `NA.ARR.RESERVED.1` | `NacustArrangementDetails_Reserved1` | TField |  |  |
