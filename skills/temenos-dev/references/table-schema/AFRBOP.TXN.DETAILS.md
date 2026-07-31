# AFRBOP.TXN.DETAILS — Table Schema

> Source: `INSERTS/I_F.AFRBOP.TXN.DETAILS` in `AFRBOP_BalanceOfPayment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRBOP.TXN.CUSTOMER.ID` | `AfrbopTxnDetails_CustomerId` | TField |  | This field hold Customer involved in the transaction |
| 2 | `AFRBOP.TXN.AMOUNT.LCY` | `AfrbopTxnDetails_AmountLcy` | TField |  | Transaction amount expressed in local currency |
| 3 | `AFRBOP.TXN.CURRENCY` | `AfrbopTxnDetails_Currency` | TField |  | This field hold Foreign Currency code |
| 4 | `AFRBOP.TXN.TRANS.DIRECTION` | `AfrbopTxnDetails_TransDirection` | TField |  | Transaction Type will be Debit or Credit |
| 5 | `AFRBOP.TXN.LOCAL.REF` | `AfrbopTxnDetails_LocalRef` |  |  |  |
| 6 | `AFRBOP.TXN.BOOKING.DATE` | `AfrbopTxnDetails_BookingDate` | TField |  | This field gives the Booking Date of the transaction |
| 7 | `AFRBOP.TXN.RESERVED.4` | `AfrbopTxnDetails_Reserved4` | TField |  | This field is reserved for future use |
| 8 | `AFRBOP.TXN.RESERVED.3` | `AfrbopTxnDetails_Reserved3` | TField |  | This field is reserved for future use |
| 9 | `AFRBOP.TXN.RESERVED.2` | `AfrbopTxnDetails_Reserved2` | TField |  | This field is reserved for future use |
| 10 | `AFRBOP.TXN.RESERVED.1` | `AfrbopTxnDetails_Reserved1` | TField |  | This field is reserved for future use |
