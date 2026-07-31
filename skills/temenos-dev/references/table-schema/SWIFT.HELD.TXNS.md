# SWIFT.HELD.TXNS — Table Schema

> Source: `INSERTS/I_F.SWIFT.HELD.TXNS` in `USREGS_RegE.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SWF.COUNTDOWN.TRANSACTION.REF` | `SwiftHeldTxns_TransactionRef` | TField |  | This field will hold the FT Number (POR.TRANSACTION record key) |
| 2 | `SWF.COUNTDOWN.COMPANY.ID` | `SwiftHeldTxns_CompanyId` | TField |  | This field will indicate the company ID for which the record is created |
| 3 | `SWF.COUNTDOWN.PO.PRODUCT` | `SwiftHeldTxns_PoProduct` | TField |  | Field holds the value of the payment order product. |
| 4 | `SWF.COUNTDOWN.DISCLOSURE.EMAIL` | `SwiftHeldTxns_DisclosureEmail` | TField |  | This field holds the value of customer's primary email address |
| 5 | `SWF.COUNTDOWN.DISCLOSURE.TIME` | `SwiftHeldTxns_DisclosureTime` | TField |  | Field will hold the value of actual date and time stamp of disclosure sent to the customer. |
| 6 | `SWF.COUNTDOWN.CONFIRMATION.TIME` | `SwiftHeldTxns_ConfirmationTime` | TField |  | Field will hold the value of actual date and time stamp of disclosure received by the customer. |
| 7 | `SWF.COUNTDOWN.STATUS` | `SwiftHeldTxns_Status` | TField |  | Status of the swift held transaction. Valid values are NEW, RESEND, ERROR, VALIDATED, DISCLOSURE.SENT, DISCLOSURE.DELIVERED. |
| 8 | `SWF.COUNTDOWN.COUNTDOWN` | `SwiftHeldTxns_Countdown` | TField |  | This field will hold the value of REGE Countdown indicator. |
| 9 | `SWF.COUNTDOWN.COUNTER` | `SwiftHeldTxns_Counter` | TField |  | Numeric field to configure SWIFT countdown period in minutes. Maximum limit for this field must be two digits. The difference between the current time and delivery confirmation time. |
| 10 | `SWF.COUNTDOWN.COUNTDOWN.PERIOD` | `SwiftHeldTxns_CountdownPeriod` | TField |  | Numeric field to configure the SWIFT Countdown period in minutes. |
| 11 | `SWF.COUNTDOWN.PROOF.INDICATOR` | `SwiftHeldTxns_ProofIndicator` | TField |  | This field is an indicator of proof of payment disclosure has been sent to customer or not. |
| 12 | `SWF.COUNTDOWN.SENDER.NAME` | `SwiftHeldTxns_SenderName` | TField |  |  |
| 13 | `SWF.COUNTDOWN.DEBIT.ACCOUNT` | `SwiftHeldTxns_DebitAccount` | TField |  | Debit account of the SWIFT transaction |
| 14 | `SWF.COUNTDOWN.DEBIT.VALUE.DATE` | `SwiftHeldTxns_DebitValueDate` | TField |  | Debit value date |
| 15 | `SWF.COUNTDOWN.CREDIT.MAIN.AMOUNT` | `SwiftHeldTxns_CreditMainAmount` | TField |  | Credit amount of the transaction |
| 16 | `SWF.COUNTDOWN.CUSTOMER.ID` | `SwiftHeldTxns_CustomerId` | TField |  | Customer ID of the debit account |
| 17 | `SWF.COUNTDOWN.ADDRESS` | `SwiftHeldTxns_Address` |  |  |  |
| 18 | `SWF.COUNTDOWN.BENEFICIARY.NAME` | `SwiftHeldTxns_BeneficiaryName` | TField |  | Name of the customer owning the beneficiary account |
| 19 | `SWF.COUNTDOWN.LOCATION` | `SwiftHeldTxns_Location` |  |  |  |
| 20 | `SWF.COUNTDOWN.BANK.TRANSFER` | `SwiftHeldTxns_BankTransfer` | TField |  | Bank Transfer |
| 21 | `SWF.COUNTDOWN.DEBIT.MAIN.AMOUNT` | `SwiftHeldTxns_DebitMainAmount` | TField |  | Transfer amount to beneficiary |
| 22 | `SWF.COUNTDOWN.FEE.DESCRIPTION` | `SwiftHeldTxns_FeeDescription` |  |  |  |
| 23 | `SWF.COUNTDOWN.FEE.TYPE` | `SwiftHeldTxns_FeeType` |  |  |  |
| 24 | `SWF.COUNTDOWN.CHARGE.AMOUNT` | `SwiftHeldTxns_ChargeAmount` |  |  |  |
| 25 | `SWF.COUNTDOWN.TOTAL.DEBIT` | `SwiftHeldTxns_TotalDebit` | TField |  | Total Debit amount. |
| 26 | `SWF.COUNTDOWN.CONFIRM.EMAIL` | `SwiftHeldTxns_ConfirmEmail` | TField |  | This is to store the Confirmation Email address. |
| 27 | `SWF.COUNTDOWN.NOTIF.EMAIL` | `SwiftHeldTxns_NotifEmail` | TField |  | This is to store the notification email address. |
| 28 | `SWF.COUNTDOWN.RESERVED.15` | `SwiftHeldTxns_Reserved15` |  |  |  |
| 29 | `SWF.COUNTDOWN.RESERVED.14` | `SwiftHeldTxns_Reserved14` |  |  |  |
| 30 | `SWF.COUNTDOWN.RESERVED.13` | `SwiftHeldTxns_Reserved13` |  |  |  |
| 31 | `SWF.COUNTDOWN.RESERVED.12` | `SwiftHeldTxns_Reserved12` | TField |  |  |
| 32 | `SWF.COUNTDOWN.RESERVED.11` | `SwiftHeldTxns_Reserved11` | TField |  |  |
| 33 | `SWF.COUNTDOWN.RESERVED.10` | `SwiftHeldTxns_Reserved10` | TField |  |  |
| 34 | `SWF.COUNTDOWN.RESERVED.9` | `SwiftHeldTxns_Reserved9` | TField |  |  |
| 35 | `SWF.COUNTDOWN.RESERVED.8` | `SwiftHeldTxns_Reserved8` | TField |  |  |
| 36 | `SWF.COUNTDOWN.RESERVED.7` | `SwiftHeldTxns_Reserved7` | TField |  |  |
| 37 | `SWF.COUNTDOWN.RESERVED.6` | `SwiftHeldTxns_Reserved6` | TField |  |  |
| 38 | `SWF.COUNTDOWN.RESERVED.5` | `SwiftHeldTxns_Reserved5` | TField |  |  |
| 39 | `SWF.COUNTDOWN.RESERVED.4` | `SwiftHeldTxns_Reserved4` | TField |  |  |
| 40 | `SWF.COUNTDOWN.RESERVED.3` | `SwiftHeldTxns_Reserved3` | TField |  |  |
| 41 | `SWF.COUNTDOWN.RESERVED.2` | `SwiftHeldTxns_Reserved2` | TField |  |  |
| 42 | `SWF.COUNTDOWN.RESERVED.1` | `SwiftHeldTxns_Reserved1` | TField |  |  |
| 43 | `SWF.COUNTDOWN.LOCAL.REF` | `SwiftHeldTxns_LocalRef` |  |  |  |
| 44 | `SWF.COUNTDOWN.OVERRIDE` | `SwiftHeldTxns_Override` |  |  |  |
| 45 | `SWF.COUNTDOWN.RECORD.STATUS` | `SwiftHeldTxns_RecordStatus` | String |  |  |
| 46 | `SWF.COUNTDOWN.CURR.NO` | `SwiftHeldTxns_CurrNo` | String |  |  |
| 47 | `SWF.COUNTDOWN.INPUTTER` | `SwiftHeldTxns_Inputter` |  |  |  |
| 48 | `SWF.COUNTDOWN.DATE.TIME` | `SwiftHeldTxns_DateTime` |  |  |  |
| 49 | `SWF.COUNTDOWN.AUTHORISER` | `SwiftHeldTxns_Authoriser` | String |  |  |
| 50 | `SWF.COUNTDOWN.CO.CODE` | `SwiftHeldTxns_CoCode` | String |  |  |
| 51 | `SWF.COUNTDOWN.DEPT.CODE` | `SwiftHeldTxns_DeptCode` | String |  |  |
| 52 | `SWF.COUNTDOWN.AUDITOR.CODE` | `SwiftHeldTxns_AuditorCode` | String |  |  |
| 53 | `SWF.COUNTDOWN.AUDIT.DATE.TIME` | `SwiftHeldTxns_AuditDateTime` | String |  |  |
