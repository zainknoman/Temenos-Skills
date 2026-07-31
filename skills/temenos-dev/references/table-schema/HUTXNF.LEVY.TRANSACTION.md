# HUTXNF.LEVY.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.HUTXNF.LEVY.TRANSACTION` in `HUTXNF_TransactionLevy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.LT.BOOKING.DATE` | `HutxnfLevyTransaction_BookingDate` | TField |  | Booking Date of the transaction. |
| 2 | `HU.LT.VALUE.DATE` | `HutxnfLevyTransaction_ValueDate` | TField |  | Value date of the transaction. |
| 3 | `HU.LT.TRANSACTION.CODE` | `HutxnfLevyTransaction_TransactionCode` | TField |  | The transaction codes of the transaction. |
| 4 | `HU.LT.TXN.CONTRACT.ID` | `HutxnfLevyTransaction_TxnContractId` | TField |  | This field holds the transaction reference for the transaction. |
| 5 | `HU.LT.ACCOUNT.TYPE` | `HutxnfLevyTransaction_AccountType` | TField |  | This field holds the account type (product code) of the transaction. |
| 6 | `HU.LT.GFO.CODE` | `HutxnfLevyTransaction_GfoCode` | TField |  | This field holds the GFO code of the client to be fetched from the field INDUS CLASSIFY in customer application. |
| 7 | `HU.LT.SECTOR.CODE` | `HutxnfLevyTransaction_SectorCode` | TField |  | This field holds the Sector code of the customer. |
| 8 | `HU.LT.LEVY.EXEMPT.AMT` | `HutxnfLevyTransaction_LevyExemptAmt` | TField |  | This field holds the transaction amount over and above which levy is eligible for private individual. |
| 9 | `HU.LT.LEVY.PERCENT.PVT.INDIVIDUAL` | `HutxnfLevyTransaction_LevyPercentPvtIndividual` | TField |  | This field holds the levy rate for the private individual. |
| 10 | `HU.LT.MAX.LEVY.AMT.PVT.INDIVIDUAL` | `HutxnfLevyTransaction_MaxLevyAmtPvtIndividual` | TField |  | This field holds the maximum Levy amount ceiling for private individual. |
| 11 | `HU.LT.LEVY.PERCENT.NONPVT.INDIVIDUAL` | `HutxnfLevyTransaction_LevyPercentNonpvtIndividual` | TField |  | This field holds the levy rate for the non-private individual. |
| 12 | `HU.LT.MAX.LEVY.AMT.NONPVT.INDIVIDUAL` | `HutxnfLevyTransaction_MaxLevyAmtNonpvtIndividual` | TField |  | This field holds the max levy amount ceiling for non-private individual. |
| 13 | `HU.LT.LEVY.PERCENT.CASH.WITHDRAWAL` | `HutxnfLevyTransaction_LevyPercentCashWithdrawal` | TField |  | This field holds the levy rate for the cash withdrawal transaction. |
| 14 | `HU.LT.LEVY.AMT.CONTACTLESS` | `HutxnfLevyTransaction_LevyAmtContactless` | TField |  | This field holds the annual levy amount for bank card purchase transactions per customer and per bankcard, if at least one transaction (in the given calendar year) is contactless. |
| 15 | `HU.LT.LEVY.AMT.NONCONTACTLESS` | `HutxnfLevyTransaction_LevyAmtNoncontactless` | TField |  | This field holds the annual levy amount for bank card purchase transactions per customer and per bankcard, if all purchase transactions (in the given calendar year) are other than contactless. |
| 16 | `HU.LT.TRANSACTION.AMOUNT` | `HutxnfLevyTransaction_TransactionAmount` | TField |  | This field holds the original transaction Amount. |
| 17 | `HU.LT.TRANSACTION.CURRENCY` | `HutxnfLevyTransaction_TransactionCurrency` | TField |  | This field holds the original transaction Currency. |
| 18 | `HU.LT.CONVERTED.AMOUNT` | `HutxnfLevyTransaction_ConvertedAmount` | TField |  | This field holds the transaction amount converted to HUF. |
| 19 | `HU.LT.EXCHANGE.RATE` | `HutxnfLevyTransaction_ExchangeRate` | TField |  | This field holds the exchange rate used for the conversion or the NBH rate if its a currency exchange transaction. |
| 20 | `HU.LT.DEBIT.ACCOUNT.NUMBER` | `HutxnfLevyTransaction_DebitAccountNumber` | TField |  | This field holds the debit account number. |
| 21 | `HU.LT.LEVY.ELIGIBLE` | `HutxnfLevyTransaction_LevyEligible` | TField |  | This field holds whether the levy is eligible or not. |
| 22 | `HU.LT.NONELIGIBILITY.REASON` | `HutxnfLevyTransaction_NoneligibilityReason` |  |  |  |
| 23 | `HU.LT.BASIS.LEVY.CALC.AMT` | `HutxnfLevyTransaction_BasisLevyCalcAmt` | TField |  | This field holds the base amount where exactly the Levy amount is calculated. |
| 24 | `HU.LT.LEVY.AMOUNT` | `HutxnfLevyTransaction_LevyAmount` | TField |  | This field holds the levy amount calculated. |
| 25 | `HU.LT.STATUS` | `HutxnfLevyTransaction_Status` | TField |  | This field holds the status of the transaction. |
| 26 | `HU.LT.CATEGORY.TYPE` | `HutxnfLevyTransaction_CategoryType` | TField |  | This field category type of the transaction. |
| 27 | `HU.LT.CHILD.TXN.CONTRACT.ID` | `HutxnfLevyTransaction_ChildTxnContractId` | TField |  | This field holds the child transaction reference for the transaction. |
| 28 | `HU.LT.RESERVED.9` | `HutxnfLevyTransaction_Reserved9` | TField |  |  |
| 29 | `HU.LT.RESERVED.8` | `HutxnfLevyTransaction_Reserved8` | TField |  |  |
| 30 | `HU.LT.RESERVED.7` | `HutxnfLevyTransaction_Reserved7` | TField |  |  |
| 31 | `HU.LT.RESERVED.6` | `HutxnfLevyTransaction_Reserved6` | TField |  |  |
| 32 | `HU.LT.RESERVED.5` | `HutxnfLevyTransaction_Reserved5` | TField |  |  |
| 33 | `HU.LT.RESERVED.4` | `HutxnfLevyTransaction_Reserved4` | TField |  |  |
| 34 | `HU.LT.RESERVED.3` | `HutxnfLevyTransaction_Reserved3` | TField |  |  |
| 35 | `HU.LT.RESERVED.2` | `HutxnfLevyTransaction_Reserved2` | TField |  |  |
| 36 | `HU.LT.RESERVED.1` | `HutxnfLevyTransaction_Reserved1` | TField |  |  |
| 37 | `HU.LT.LOCAL.REF` | `HutxnfLevyTransaction_LocalRef` |  |  |  |
