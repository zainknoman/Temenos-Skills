# MXACCT.AA.REJECTED.ACTIVITIES — Table Schema

> Source: `INSERTS/I_F.MXACCT.AA.REJECTED.ACTIVITIES` in `MXACCT_UDILimitAccount.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.REJ.ACT.PRODUCT.GROUP` | `MxacctAaRejectedActivities_ProductGroup` | TField |  | The product group that belongs to the credit account. |
| 2 | `AA.REJ.ACT.PRODUCT` | `MxacctAaRejectedActivities_Product` | TField |  | The product that belongs to the credit account |
| 3 | `AA.REJ.ACT.CUSTOMER` | `MxacctAaRejectedActivities_Customer` | TField |  | Customer id owner of credit account. |
| 4 | `AA.REJ.ACT.ACCOUNT` | `MxacctAaRejectedActivities_Account` | TField |  | The credit account number |
| 5 | `AA.REJ.ACT.ACCOUNT.OPEN.CHANNEL` | `MxacctAaRejectedActivities_AccountOpenChannel` | TField |  | T24 Channel where the credit account was opened |
| 6 | `AA.REJ.ACT.ACCOUNT.OPEN.DATE` | `MxacctAaRejectedActivities_AccountOpenDate` | TField |  | Opening date and activation of the credit account |
| 7 | `AA.REJ.ACT.LIMIT.CURRENCY` | `MxacctAaRejectedActivities_LimitCurrency` | TField |  | The deposit restriction limit value that is applied to the product. |
| 8 | `AA.REJ.ACT.LIMIT.CCY.LCY` | `MxacctAaRejectedActivities_LimitCcyLcy` | TField |  | The deposit restriction limit that is applied to the product but expressed in the local currency of the account. For example MXP. |
| 9 | `AA.REJ.ACT.TX.VALUE.DATE` | `MxacctAaRejectedActivities_TxValueDate` | TField |  |  |
| 10 | `AA.REJ.ACT.TX.BOOKING.DATE` | `MxacctAaRejectedActivities_TxBookingDate` | TField |  |  |
| 11 | `AA.REJ.ACT.TX.TYPE` | `MxacctAaRejectedActivities_TxType` | TField |  |  |
| 12 | `AA.REJ.ACT.TX.STATUS` | `MxacctAaRejectedActivities_TxStatus` | TField |  |  |
| 13 | `AA.REJ.ACT.TX.REFERENCE` | `MxacctAaRejectedActivities_TxReference` | TField |  |  |
| 14 | `AA.REJ.ACT.TX.AMOUNT` | `MxacctAaRejectedActivities_TxAmount` | TField |  |  |
| 15 | `AA.REJ.ACT.TX.CCY` | `MxacctAaRejectedActivities_TxCcy` | TField |  |  |
| 16 | `AA.REJ.ACT.TX.REJECTED.REASON` | `MxacctAaRejectedActivities_TxRejectedReason` | TField |  |  |
| 17 | `AA.REJ.ACT.TX.REJECTED.DATE` | `MxacctAaRejectedActivities_TxRejectedDate` | TField |  |  |
| 18 | `AA.REJ.ACT.DEBIT.ACCOUNT` | `MxacctAaRejectedActivities_DebitAccount` | TField |  | External Debit Account Number. |
| 19 | `AA.REJ.ACT.DEBIT.CUSTOMER.NAME` | `MxacctAaRejectedActivities_DebitCustomerName` | TField |  | Customer Name of external Debit Account |
| 20 | `AA.REJ.ACT.DEBIT.BANK` | `MxacctAaRejectedActivities_DebitBank` | TField |  | Bank name of external debit account. |
| 21 | `AA.REJ.ACT.RESERVED.15` | `MxacctAaRejectedActivities_Reserved15` | TField |  | Reserved 15 |
| 22 | `AA.REJ.ACT.RESERVED.14` | `MxacctAaRejectedActivities_Reserved14` | TField |  | Reserved 14 |
| 23 | `AA.REJ.ACT.RESERVED.13` | `MxacctAaRejectedActivities_Reserved13` | TField |  | Reserved 13 |
| 24 | `AA.REJ.ACT.RESERVED.12` | `MxacctAaRejectedActivities_Reserved12` | TField |  | Reserved 12 |
| 25 | `AA.REJ.ACT.RESERVED.11` | `MxacctAaRejectedActivities_Reserved11` | TField |  | Reserved 11 |
| 26 | `AA.REJ.ACT.RESERVED.10` | `MxacctAaRejectedActivities_Reserved10` | TField |  | Reserved 10 |
| 27 | `AA.REJ.ACT.RESERVED.9` | `MxacctAaRejectedActivities_Reserved9` | TField |  | Reserved 9 |
| 28 | `AA.REJ.ACT.RESERVED.8` | `MxacctAaRejectedActivities_Reserved8` | TField |  | Reserved 8 |
| 29 | `AA.REJ.ACT.RESERVED.7` | `MxacctAaRejectedActivities_Reserved7` | TField |  | Reserved 7 |
| 30 | `AA.REJ.ACT.RESERVED.6` | `MxacctAaRejectedActivities_Reserved6` | TField |  | Reserved 6 |
| 31 | `AA.REJ.ACT.RESERVED.5` | `MxacctAaRejectedActivities_Reserved5` | TField |  | Reserved 5 |
| 32 | `AA.REJ.ACT.RESERVED.4` | `MxacctAaRejectedActivities_Reserved4` | TField |  | Reserved 4 |
| 33 | `AA.REJ.ACT.RESERVED.3` | `MxacctAaRejectedActivities_Reserved3` | TField |  | Reserved 3 |
| 34 | `AA.REJ.ACT.RESERVED.2` | `MxacctAaRejectedActivities_Reserved2` | TField |  | Reserved 2 |
| 35 | `AA.REJ.ACT.RESERVED.1` | `MxacctAaRejectedActivities_Reserved1` | TField |  | Reserved 1 |
| 36 | `AA.REJ.ACT.LOCAL.REF` | `MxacctAaRejectedActivities_LocalRef` |  |  |  |
