# TNFCOP.TRADE.TITLE.ADV.PAYMENT — Table Schema

> Source: `INSERTS/I_F.TNFCOP.TRADE.TITLE.ADV.PAYMENT` in `TNFCOP_TradeTitle.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TCE.ADV.PAYMENT.CUSTOMER.ID` | `TnfcopTradeTitleAdvPayment_CustomerId` | TField |  | This field denotes the customer ID which received the Advance Payment |
| 2 | `TCE.ADV.PAYMENT.TITLE.CODE` | `TnfcopTradeTitleAdvPayment_TitleCode` | TField |  | This field denotes the Title code used to store Advance Payment |
| 3 | `TCE.ADV.PAYMENT.CREDIT.ACCOUNT.NUMBER` | `TnfcopTradeTitleAdvPayment_CreditAccountNumber` | TField |  | This field denotes the Credit account number which received the advance payment |
| 4 | `TCE.ADV.PAYMENT.TRANSACTION.CURRENCY` | `TnfcopTradeTitleAdvPayment_TransactionCurrency` | TField |  | This field denotes the currency of the amount received as Advance payment |
| 5 | `TCE.ADV.PAYMENT.AMT.TO.BE.SETTLED` | `TnfcopTradeTitleAdvPayment_AmtToBeSettled` | TField |  | This field denotes the amount received as Advance payment |
| 6 | `TCE.ADV.PAYMENT.LINKED.TRADE.TITLE` | `TnfcopTradeTitleAdvPayment_LinkedTradeTitle` | TField |  | This field denotes Trade Title ID linked with Advance payment |
| 7 | `TCE.ADV.PAYMENT.LOCAL.REF` | `TnfcopTradeTitleAdvPayment_LocalRef` |  |  |  |
| 8 | `TCE.ADV.PAYMENT.RESERVED.5` | `TnfcopTradeTitleAdvPayment_Reserved5` | TField |  |  |
| 9 | `TCE.ADV.PAYMENT.RESERVED.4` | `TnfcopTradeTitleAdvPayment_Reserved4` | TField |  |  |
| 10 | `TCE.ADV.PAYMENT.RESERVED.3` | `TnfcopTradeTitleAdvPayment_Reserved3` | TField |  |  |
| 11 | `TCE.ADV.PAYMENT.RESERVED.2` | `TnfcopTradeTitleAdvPayment_Reserved2` | TField |  |  |
| 12 | `TCE.ADV.PAYMENT.RESERVED.1` | `TnfcopTradeTitleAdvPayment_Reserved1` | TField |  |  |
| 13 | `TCE.ADV.PAYMENT.OVERRIDE` | `TnfcopTradeTitleAdvPayment_Override` |  |  |  |
