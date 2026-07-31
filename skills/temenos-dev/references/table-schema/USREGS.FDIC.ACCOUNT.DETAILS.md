# USREGS.FDIC.ACCOUNT.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.FDIC.ACCOUNT.DETAILS` in `USREGS_FDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDIC.ACC.DETS.FDIC.ID` | `UsregsFdicAccountDetails_FdicId` | TField |  | Transaction reference id(FDIC.ID) |
| 2 | `FDIC.ACC.DETS.ACCOUNT` | `UsregsFdicAccountDetails_Account` | TField |  | Account id of the Transaction |
| 3 | `FDIC.ACC.DETS.CURRENCY` | `UsregsFdicAccountDetails_Currency` | TField |  | Account Currency of the Transaction |
| 4 | `FDIC.ACC.DETS.SUSP.ACCOUNT` | `UsregsFdicAccountDetails_SuspAccount` | TField |  | Settlement account to which the entries will be posted in case of FUNDS.TRANSFER transaction |
| 5 | `FDIC.ACC.DETS.FTTC` | `UsregsFdicAccountDetails_Fttc` | TField |  | A Valid FT.TXN.TYPE.CONDITION record id. |
| 6 | `FDIC.ACC.DETS.COMPANY.CODE` | `UsregsFdicAccountDetails_CompanyCode` | TField |  | Company where the Account exists |
| 7 | `FDIC.ACC.DETS.DP.ACCT.IDENTIFIER` | `UsregsFdicAccountDetails_DpAcctIdentifier` | TField |  | Account Identifier |
| 8 | `FDIC.ACC.DETS.DP.ACCT.IDENTIFIER.2` | `UsregsFdicAccountDetails_DpAcctIdentifier2` | TField |  | Account Identifier 2 |
| 9 | `FDIC.ACC.DETS.DP.ACCT.IDENTIFIER.3` | `UsregsFdicAccountDetails_DpAcctIdentifier3` | TField |  | Account Identifier 3 |
| 10 | `FDIC.ACC.DETS.DP.ACCT.IDENTIFIER.4` | `UsregsFdicAccountDetails_DpAcctIdentifier4` | TField |  | Account Identifier 4 |
| 11 | `FDIC.ACC.DETS.DP.ACCT.IDENTIFIER.5` | `UsregsFdicAccountDetails_DpAcctIdentifier5` | TField |  | Account Identifier 5 |
| 12 | `FDIC.ACC.DETS.DP.SUBACCT.IDENTIFIER` | `UsregsFdicAccountDetails_DpSubacctIdentifier` | TField |  | Sub Account Identifier |
| 13 | `FDIC.ACC.DETS.TXN.TYPE` | `UsregsFdicAccountDetails_TxnType` | TField |  | Valid transaction type(AUTO.HOLD,MANUAL.HOLD,HOLD.FILE,TRANS.FILE) |
| 14 | `FDIC.ACC.DETS.THRESHOLD.AMT` | `UsregsFdicAccountDetails_ThresholdAmt` | TField |  | Threshold amount for the account |
| 15 | `FDIC.ACC.DETS.HOLD.PERCENTAGE` | `UsregsFdicAccountDetails_HoldPercentage` | TField |  | Threshold percentage for the account |
| 16 | `FDIC.ACC.DETS.HOLD.AMOUNT` | `UsregsFdicAccountDetails_HoldAmount` | TField |  | Hold amount for the account |
| 17 | `FDIC.ACC.DETS.HOLD.TXN.DESCRIPTION` | `UsregsFdicAccountDetails_HoldTxnDescription` | TField |  | Description of the transaction |
| 18 | `FDIC.ACC.DETS.HOLD.START.DATE` | `UsregsFdicAccountDetails_HoldStartDate` | TField |  | Transaction date for AC.LOCKED.EVENTS. Will be updated only for Auto and Manual holds. For hold file, this information will be defaulted to processing date or system date |
| 19 | `FDIC.ACC.DETS.HOLD.END.DATE` | `UsregsFdicAccountDetails_HoldEndDate` | TField |  | Expiry date of AC.LOCKED.EVENTS. Will be updated only for Auto and Manual holds. For hold file, this information will be defaulted to processing date or system date |
| 20 | `FDIC.ACC.DETS.ACTION` | `UsregsFdicAccountDetails_Action` | TField |  | Action to be performed - ADD, REMOVE, CREDIT or DEBIT |
| 21 | `FDIC.ACC.DETS.CATEGORY` | `UsregsFdicAccountDetails_Category` | TField |  | Category of the account |
| 22 | `FDIC.ACC.DETS.PRODUCT.GROUP` | `UsregsFdicAccountDetails_ProductGroup` | TField |  | Product group of the account |
| 23 | `FDIC.ACC.DETS.PRODUCT` | `UsregsFdicAccountDetails_Product` | TField |  | Product of the account |
| 24 | `FDIC.ACC.DETS.DEBIT.AMT` | `UsregsFdicAccountDetails_DebitAmt` | TField |  | Debit amount for the account |
| 25 | `FDIC.ACC.DETS.CREDIT.AMT` | `UsregsFdicAccountDetails_CreditAmt` | TField |  | Credit amount for the account |
| 26 | `FDIC.ACC.DETS.CREDIT.AMT.LCY` | `UsregsFdicAccountDetails_CreditAmtLcy` | TField |  | Local equivalent of the credit amount posted as part the FDIC transaction |
| 27 | `FDIC.ACC.DETS.DEBIT.AMT.LCY` | `UsregsFdicAccountDetails_DebitAmtLcy` | TField |  | Local equivalent of the debit amount posted as part the FDIC transaction |
| 28 | `FDIC.ACC.DETS.EXCHANGE.RATE` | `UsregsFdicAccountDetails_ExchangeRate` | TField |  | Exchange rate used for converting the applicable threshold amount or incoming Amount from Regulation authority from local currency to the account currency |
| 29 | `FDIC.ACC.DETS.CUR.BALANCE.LCY` | `UsregsFdicAccountDetails_CurBalanceLcy` | TField |  | For foreign currency account this field contains the account current balance equivalent in local currency by applying EXCHANGE.RATE |
| 30 | `FDIC.ACC.DETS.AVAIL.BALANCE.LCY` | `UsregsFdicAccountDetails_AvailBalanceLcy` | TField |  | For foreign currency account this field contains the account available balance equivalent in local currency by applying EXCHANGE.RATE |
| 31 | `FDIC.ACC.DETS.HOLD.LCY` | `UsregsFdicAccountDetails_HoldLcy` | TField |  | Local equivalent of the hold amount posted or reversed as part the FDIC transaction |
| 32 | `FDIC.ACC.DETS.RESERVED.9` | `UsregsFdicAccountDetails_Reserved9` | TField |  |  |
| 33 | `FDIC.ACC.DETS.RESERVED.8` | `UsregsFdicAccountDetails_Reserved8` | TField |  |  |
| 34 | `FDIC.ACC.DETS.RESERVED.7` | `UsregsFdicAccountDetails_Reserved7` | TField |  |  |
| 35 | `FDIC.ACC.DETS.RESERVED.6` | `UsregsFdicAccountDetails_Reserved6` | TField |  |  |
| 36 | `FDIC.ACC.DETS.RESERVED.5` | `UsregsFdicAccountDetails_Reserved5` | TField |  |  |
| 37 | `FDIC.ACC.DETS.RESERVED.4` | `UsregsFdicAccountDetails_Reserved4` | TField |  |  |
| 38 | `FDIC.ACC.DETS.RESERVED.3` | `UsregsFdicAccountDetails_Reserved3` | TField |  |  |
| 39 | `FDIC.ACC.DETS.RESERVED.2` | `UsregsFdicAccountDetails_Reserved2` | TField |  |  |
| 40 | `FDIC.ACC.DETS.RESERVED.1` | `UsregsFdicAccountDetails_Reserved1` | TField |  |  |
