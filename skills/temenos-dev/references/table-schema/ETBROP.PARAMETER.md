# ETBROP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ETBROP.PARAMETER` in `ETBROP_CashiersPaymentOrderDD.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ETBROP.PARAMETER.CPODD.TYPE` | `EtbropParameter_CpoddType` |  |  |  |
| 2 | `ETBROP.PARAMETER.CPODD.LONG.OUTSTNG.DAYS` | `EtbropParameter_CpoddLongOutstngDays` | TField |  | This field holds the number of Calendar days, from Issue Date, after which to identify CPO/DD as Long Outstanding. |
| 3 | `ETBROP.PARAMETER.CPODD.UNCLAIMED.DAYS` | `EtbropParameter_CpoddUnclaimedDays` | TField |  | This field holds the number of Calendar days, from Issue Date, after which to transfer the amount of CPO/DD from Branch Payable Account to HO Unclaimed Account. |
| 4 | `ETBROP.PARAMETER.CPODD.UNCLAIMED.ACCT.TRNSFR` | `EtbropParameter_CpoddUnclaimedAcctTrnsfr` | TField |  | The value in this field indicates the transfer of Instrument Amount to HO by Automatic or Manual. |
| 5 | `ETBROP.PARAMETER.CPODD.HO.UNCLAIMED.ACCT` | `EtbropParameter_CpoddHoUnclaimedAcct` | TField |  | To define the Head Office Internal Account for transfer of unclaimed instrument amount from Branch to Head Office unclaimed account. |
| 6 | `ETBROP.PARAMETER.LONG.STATUS` | `EtbropParameter_LongStatus` | TField |  | This will define the number of days for a transaction to categorize it as Long Outstanding Minimum value = Zero or Null Maximum � 999Days. If the field is defined as Zero or Null, the transaction will not be identified as long outstanding. |
| 7 | `ETBROP.PARAMETER.TRFR.TO.UNCLAIMED` | `EtbropParameter_TrfrToUnclaimed` | TField |  | This will define the number of days from the date of deposit / account debit after which the funds will be transferred to HO payable account. E.g � 180 days. |
| 8 | `ETBROP.PARAMETER.HO.LMTS.UNCLAIMED.ACCT` | `EtbropParameter_HoLmtsUnclaimedAcct` | TField |  | This will define the HO internal account for transfer of Long outstanding amount from the branch to the HO payable account. |
| 9 | `ETBROP.PARAMETER.STALE.CHEQUE.VALIDITY.PERIOD` | `EtbropParameter_StaleChequeValidityPeriod` | TField |  | This will define the Cheque Validity Period. |
| 10 | `ETBROP.PARAMETER.RESERVED.2` | `EtbropParameter_Reserved2` | TField |  |  |
| 11 | `ETBROP.PARAMETER.RESERVED.3` | `EtbropParameter_Reserved3` | TField |  |  |
| 12 | `ETBROP.PARAMETER.RESERVED.4` | `EtbropParameter_Reserved4` | TField |  |  |
| 13 | `ETBROP.PARAMETER.RESERVED.5` | `EtbropParameter_Reserved5` | TField |  |  |
| 14 | `ETBROP.PARAMETER.RESERVED.6` | `EtbropParameter_Reserved6` | TField |  |  |
| 15 | `ETBROP.PARAMETER.RESERVED.7` | `EtbropParameter_Reserved7` | TField |  |  |
| 16 | `ETBROP.PARAMETER.RESERVED.8` | `EtbropParameter_Reserved8` | TField |  |  |
| 17 | `ETBROP.PARAMETER.RESERVED.9` | `EtbropParameter_Reserved9` | TField |  |  |
| 18 | `ETBROP.PARAMETER.RESERVED.10` | `EtbropParameter_Reserved10` | TField |  |  |
| 19 | `ETBROP.PARAMETER.LOCAL.REF` | `EtbropParameter_LocalRef` |  |  |  |
| 20 | `ETBROP.PARAMETER.OVERRIDE` | `EtbropParameter_Override` |  |  |  |
| 21 | `ETBROP.PARAMETER.RECORD.STATUS` | `EtbropParameter_RecordStatus` | String |  |  |
| 22 | `ETBROP.PARAMETER.CURR.NO` | `EtbropParameter_CurrNo` | String |  |  |
| 23 | `ETBROP.PARAMETER.INPUTTER` | `EtbropParameter_Inputter` |  |  |  |
| 24 | `ETBROP.PARAMETER.DATE.TIME` | `EtbropParameter_DateTime` |  |  |  |
| 25 | `ETBROP.PARAMETER.AUTHORISER` | `EtbropParameter_Authoriser` | String |  |  |
| 26 | `ETBROP.PARAMETER.CO.CODE` | `EtbropParameter_CoCode` | String |  |  |
| 27 | `ETBROP.PARAMETER.DEPT.CODE` | `EtbropParameter_DeptCode` | String |  |  |
| 28 | `ETBROP.PARAMETER.AUDITOR.CODE` | `EtbropParameter_AuditorCode` | String |  |  |
| 29 | `ETBROP.PARAMETER.AUDIT.DATE.TIME` | `EtbropParameter_AuditDateTime` | String |  |  |
