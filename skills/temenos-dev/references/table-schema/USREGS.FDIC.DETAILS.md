# USREGS.FDIC.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.FDIC.DETAILS` in `USREGS_FDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDIC.DETS.ACCOUNT` | `UsregsFdicDetails_Account` | TField |  | Account id of the transaction |
| 2 | `FDIC.DETS.SUSP.ACCOUNT` | `UsregsFdicDetails_SuspAccount` | TField |  | Account to which settlement has been done in case of FUNDS.TRANSFER transaction |
| 3 | `FDIC.DETS.COMPANY.CODE` | `UsregsFdicDetails_CompanyCode` | TField |  | Company where the Account exists |
| 4 | `FDIC.DETS.BRANCH` | `UsregsFdicDetails_Branch` | TField |  | Branch to which the account belongs |
| 5 | `FDIC.DETS.CATEGORY` | `UsregsFdicDetails_Category` | TField |  | Category id of the Account |
| 6 | `FDIC.DETS.PRODUCT.GROUP` | `UsregsFdicDetails_ProductGroup` | TField |  | Product group of the Account |
| 7 | `FDIC.DETS.PRODUCT` | `UsregsFdicDetails_Product` | TField |  | Product of the Account |
| 8 | `FDIC.DETS.CUR.BALANCE` | `UsregsFdicDetails_CurBalance` | TField |  | Current balance of the Account |
| 9 | `FDIC.DETS.THRESHOLD.AMOUNT` | `UsregsFdicDetails_ThresholdAmount` | TField |  | Threshold amount for the Account |
| 10 | `FDIC.DETS.HOLD.PERCENTAGE` | `UsregsFdicDetails_HoldPercentage` | TField |  | Hold percentage for the Account |
| 11 | `FDIC.DETS.HOLD.AMOUNT` | `UsregsFdicDetails_HoldAmount` | TField |  | The FDIC Amount on an account that is the either being locked or reversed on the account |
| 12 | `FDIC.DETS.CREDIT.AMOUNT` | `UsregsFdicDetails_CreditAmount` | TField |  | The FDIC Amount on an account that is credited to the account |
| 13 | `FDIC.DETS.DEBIT.AMOUNT` | `UsregsFdicDetails_DebitAmount` | TField |  | The FDIC Amount on an account that is debited from the account |
| 14 | `FDIC.DETS.AVAILABLE.BALANCE` | `UsregsFdicDetails_AvailableBalance` | TField |  | Available balance for the Account, it is the Account balance reduced by the FDIC Hold Amount |
| 15 | `FDIC.DETS.TXN.REFERENCE` | `UsregsFdicDetails_TxnReference` | TField |  | Transaction Reference created for the FDIC Transaction. It can be a AC.LOCKED.EVENT or an FUNDS.TRANSFER transaction reference |
| 16 | `FDIC.DETS.STATUS` | `UsregsFdicDetails_Status` | TField |  | Status of the Transaction |
| 17 | `FDIC.DETS.FDIC.TRANSACTION` | `UsregsFdicDetails_FdicTransaction` | TField |  | USREGS.FDIC.TRANSACTION record ID |
| 18 | `FDIC.DETS.TXN.TYPE` | `UsregsFdicDetails_TxnType` | TField |  | Transaction types can be AUTO.HOLD,MANUAL.HOLD,HOLD.FILE,TRANS.FILE. It is the FDIC.TRANSACTION type that initiated the processing |
| 19 | `FDIC.DETS.ACTION` | `UsregsFdicDetails_Action` | TField |  |  |
| 20 | `FDIC.DETS.CREDIT.AMT.LCY` | `UsregsFdicDetails_CreditAmtLcy` | TField |  | Local equivalent of the credit amount posted as part the FDIC transaction |
| 21 | `FDIC.DETS.DEBIT.AMT.LCY` | `UsregsFdicDetails_DebitAmtLcy` | TField |  | Local equivalent of the debit amount posted as part the FDIC transaction |
| 22 | `FDIC.DETS.EXCHANGE.RATE` | `UsregsFdicDetails_ExchangeRate` | TField |  | Exchange rate used for converting the applicable threshold amount or incoming Amount from Regulation authority from local currency to the account currency |
| 23 | `FDIC.DETS.CUR.BALANCE.LCY` | `UsregsFdicDetails_CurBalanceLcy` | TField |  | For foreign currency account this field contains the account current balance equivalent in local currency by applying EXCHANGE.RATE |
| 24 | `FDIC.DETS.AVAIL.BALANCE.LCY` | `UsregsFdicDetails_AvailBalanceLcy` | TField |  | For foreign currency account this field contains the account available balance equivalent in local currency by applying EXCHANGE.RATE |
| 25 | `FDIC.DETS.HOLD.LCY` | `UsregsFdicDetails_HoldLcy` | TField |  | Local equivalent of the hold amount posted or reversed as part the FDIC transaction |
| 26 | `FDIC.DETS.RESERVED.9` | `UsregsFdicDetails_Reserved9` | TField |  |  |
| 27 | `FDIC.DETS.RESERVED.8` | `UsregsFdicDetails_Reserved8` | TField |  |  |
| 28 | `FDIC.DETS.RESERVED.7` | `UsregsFdicDetails_Reserved7` | TField |  |  |
| 29 | `FDIC.DETS.RESERVED.6` | `UsregsFdicDetails_Reserved6` | TField |  |  |
| 30 | `FDIC.DETS.RESERVED.5` | `UsregsFdicDetails_Reserved5` | TField |  |  |
| 31 | `FDIC.DETS.RESERVED.4` | `UsregsFdicDetails_Reserved4` | TField |  |  |
| 32 | `FDIC.DETS.RESERVED.3` | `UsregsFdicDetails_Reserved3` | TField |  |  |
| 33 | `FDIC.DETS.RESERVED.2` | `UsregsFdicDetails_Reserved2` | TField |  |  |
| 34 | `FDIC.DETS.RESERVED.1` | `UsregsFdicDetails_Reserved1` | TField |  |  |
