# BRDEPO.WITHDRAWAL.DETAILS — Table Schema

> Source: `INSERTS/I_F.BRDEPO.WITHDRAWAL.DETAILS` in `BRDEPO_CDBPreAndPostFixado.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BRDEPO.WITHDRAWAL.DETAILS.ARRANGEMENT.ID` | `BrdepoWithdrawalDetails_ArrangementId` | TField |  | ID of the Arrangement which is being withdrawn. |
| 2 | `BRDEPO.WITHDRAWAL.DETAILS.WITHDRAWAL.DATE` | `BrdepoWithdrawalDetails_WithdrawalDate` | TField |  | Date on which the withdrawal is requested to be made |
| 3 | `BRDEPO.WITHDRAWAL.DETAILS.CREATION.DATE` | `BrdepoWithdrawalDetails_CreationDate` | TField |  |  |
| 4 | `BRDEPO.WITHDRAWAL.DETAILS.PAYMENT.ORDER.AMOUNT` | `BrdepoWithdrawalDetails_PaymentOrderAmount` | TField |  | If a partial withdrawal is made, it will store the amount of which the payment order is being made. |
| 5 | `BRDEPO.WITHDRAWAL.DETAILS.REQUESTED.AMOUNT` | `BrdepoWithdrawalDetails_RequestedAmount` | TField |  | If a partial withdrawal is made, it will store the amount requested at the enquiry level. |
| 6 | `BRDEPO.WITHDRAWAL.DETAILS.TRANSACTION.CURRENCY` | `BrdepoWithdrawalDetails_TransactionCurrency` | TField |  | Currency of the arrangement. |
| 7 | `BRDEPO.WITHDRAWAL.DETAILS.ACCOUNT.NUMBER` | `BrdepoWithdrawalDetails_AccountNumber` | TField |  | Account number which will be deposited. |
| 8 | `BRDEPO.WITHDRAWAL.DETAILS.TOTAL.WITHDRAWAL` | `BrdepoWithdrawalDetails_TotalWithdrawal` | TField |  |  |
| 9 | `BRDEPO.WITHDRAWAL.DETAILS.OFS.TXN.ID` | `BrdepoWithdrawalDetails_OfsTxnId` | TField |  | Holds the ID of either the AA.ARRANGEMENT.ACTIVITY or the ID of the PAYMENT.ORDER |
| 10 | `BRDEPO.WITHDRAWAL.DETAILS.REVERSE.TXN` | `BrdepoWithdrawalDetails_ReverseTxn` | TField |  | Check Box that indicates if the process is a reversal of the Withdrawal. |
| 11 | `BRDEPO.WITHDRAWAL.DETAILS.WITHDRAWAL.STATUS` | `BrdepoWithdrawalDetails_WithdrawalStatus` | TField |  | Indicates the current status of the withdrawal. |
| 12 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.10` | `BrdepoWithdrawalDetails_Reserved10` | TField |  |  |
| 13 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.9` | `BrdepoWithdrawalDetails_Reserved9` | TField |  |  |
| 14 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.8` | `BrdepoWithdrawalDetails_Reserved8` | TField |  |  |
| 15 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.7` | `BrdepoWithdrawalDetails_Reserved7` | TField |  |  |
| 16 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.6` | `BrdepoWithdrawalDetails_Reserved6` | TField |  |  |
| 17 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.5` | `BrdepoWithdrawalDetails_Reserved5` | TField |  |  |
| 18 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.4` | `BrdepoWithdrawalDetails_Reserved4` | TField |  |  |
| 19 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.3` | `BrdepoWithdrawalDetails_Reserved3` | TField |  |  |
| 20 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.2` | `BrdepoWithdrawalDetails_Reserved2` | TField |  |  |
| 21 | `BRDEPO.WITHDRAWAL.DETAILS.RESERVED.1` | `BrdepoWithdrawalDetails_Reserved1` | TField |  |  |
| 22 | `BRDEPO.WITHDRAWAL.DETAILS.LOCAL.REF` | `BrdepoWithdrawalDetails_LocalRef` |  |  |  |
| 23 | `BRDEPO.WITHDRAWAL.DETAILS.OVERRIDE` | `BrdepoWithdrawalDetails_Override` |  |  |  |
| 24 | `BRDEPO.WITHDRAWAL.DETAILS.RECORD.STATUS` | `BrdepoWithdrawalDetails_RecordStatus` | String |  |  |
| 25 | `BRDEPO.WITHDRAWAL.DETAILS.CURR.NO` | `BrdepoWithdrawalDetails_CurrNo` | String |  |  |
| 26 | `BRDEPO.WITHDRAWAL.DETAILS.INPUTTER` | `BrdepoWithdrawalDetails_Inputter` |  |  |  |
| 27 | `BRDEPO.WITHDRAWAL.DETAILS.DATE.TIME` | `BrdepoWithdrawalDetails_DateTime` |  |  |  |
| 28 | `BRDEPO.WITHDRAWAL.DETAILS.AUTHORISER` | `BrdepoWithdrawalDetails_Authoriser` | String |  |  |
| 29 | `BRDEPO.WITHDRAWAL.DETAILS.CO.CODE` | `BrdepoWithdrawalDetails_CoCode` | String |  |  |
| 30 | `BRDEPO.WITHDRAWAL.DETAILS.DEPT.CODE` | `BrdepoWithdrawalDetails_DeptCode` | String |  |  |
| 31 | `BRDEPO.WITHDRAWAL.DETAILS.AUDITOR.CODE` | `BrdepoWithdrawalDetails_AuditorCode` | String |  |  |
| 32 | `BRDEPO.WITHDRAWAL.DETAILS.AUDIT.DATE.TIME` | `BrdepoWithdrawalDetails_AuditDateTime` | String |  |  |
