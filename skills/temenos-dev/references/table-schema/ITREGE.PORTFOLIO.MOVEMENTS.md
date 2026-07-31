# ITREGE.PORTFOLIO.MOVEMENTS — Table Schema

> Source: `INSERTS/I_F.ITREGE.PORTFOLIO.MOVEMENTS` in `ITREGE_PortfolioMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PORTFOLIO.MOVEMENTS.TRANSACTION.REF` | `ItregePortfolioMovements_TransactionRef` | TField |  | This field holds transaction reference id. Value links to the @ID of POR.TRANSACTION table. |
| 2 | `PORTFOLIO.MOVEMENTS.AMOUNT.IN.FCY` | `ItregePortfolioMovements_AmountInFcy` | TField |  | Indicates the amount for which the payment needs to be processed. |
| 3 | `PORTFOLIO.MOVEMENTS.AMOUNT.IN.LCY` | `ItregePortfolioMovements_AmountInLcy` | TField |  | Specifies The counter Value. |
| 4 | `PORTFOLIO.MOVEMENTS.CUST.RESI.CODE` | `ItregePortfolioMovements_CustResiCode` | TField |  | Customer UIC |
| 5 | `PORTFOLIO.MOVEMENTS.CUSTOMER.COUNTRY` | `ItregePortfolioMovements_CustomerCountry` | TField |  | Indicates the country code or country group present in the IBAN of the Beneficiary. |
| 6 | `PORTFOLIO.MOVEMENTS.TRANSACTION.DATE` | `ItregePortfolioMovements_TransactionDate` | TField |  | This is the date from which funds are available to the party for withdrawal. |
| 7 | `PORTFOLIO.MOVEMENTS.COLL.TYPE.CODES` | `ItregePortfolioMovements_CollTypeCodes` | TField |  | Value links to field COLL.TYPE.CODE in ITREGE.TRANSACTIONS.PARAM table. |
| 8 | `PORTFOLIO.MOVEMENTS.BILL.TYPE.CODES` | `ItregePortfolioMovements_BillTypeCodes` | TField |  | Value links to field BILL.TYPE.EXCH in ITREGE.TRANSACTIONS.PARAM table. |
| 9 | `PORTFOLIO.MOVEMENTS.SECTOR` | `ItregePortfolioMovements_Sector` | TField |  | Value links to field CUST.SECTOR in ITREGE.TRANSACTIONS.PARAM table. |
| 10 | `PORTFOLIO.MOVEMENTS.NO.OF.TXN` | `ItregePortfolioMovements_NoOfTxn` | TField |  | No of transactions if bulk transaction. In case of single transaction, the value is 1. |
| 11 | `PORTFOLIO.MOVEMENTS.RESERVED.8` | `ItregePortfolioMovements_Reserved8` | TField |  |  |
| 12 | `PORTFOLIO.MOVEMENTS.RESERVED.7` | `ItregePortfolioMovements_Reserved7` | TField |  |  |
| 13 | `PORTFOLIO.MOVEMENTS.RESERVED.6` | `ItregePortfolioMovements_Reserved6` | TField |  |  |
| 14 | `PORTFOLIO.MOVEMENTS.RESERVED.5` | `ItregePortfolioMovements_Reserved5` | TField |  |  |
| 15 | `PORTFOLIO.MOVEMENTS.RESERVED.4` | `ItregePortfolioMovements_Reserved4` | TField |  |  |
| 16 | `PORTFOLIO.MOVEMENTS.RESERVED.3` | `ItregePortfolioMovements_Reserved3` | TField |  |  |
| 17 | `PORTFOLIO.MOVEMENTS.RESERVED.2` | `ItregePortfolioMovements_Reserved2` | TField |  |  |
| 18 | `PORTFOLIO.MOVEMENTS.RESERVED.1` | `ItregePortfolioMovements_Reserved1` | TField |  |  |
| 19 | `PORTFOLIO.MOVEMENTS.LOCAL.REF` | `ItregePortfolioMovements_LocalRef` |  |  |  |
| 20 | `PORTFOLIO.MOVEMENTS.RECORD.STATUS` | `ItregePortfolioMovements_RecordStatus` | String |  |  |
| 21 | `PORTFOLIO.MOVEMENTS.CURR.NO` | `ItregePortfolioMovements_CurrNo` | String |  |  |
| 22 | `PORTFOLIO.MOVEMENTS.INPUTTER` | `ItregePortfolioMovements_Inputter` |  |  |  |
| 23 | `PORTFOLIO.MOVEMENTS.DATE.TIME` | `ItregePortfolioMovements_DateTime` |  |  |  |
| 24 | `PORTFOLIO.MOVEMENTS.AUTHORISER` | `ItregePortfolioMovements_Authoriser` | String |  |  |
| 25 | `PORTFOLIO.MOVEMENTS.CO.CODE` | `ItregePortfolioMovements_CoCode` | String |  |  |
| 26 | `PORTFOLIO.MOVEMENTS.DEPT.CODE` | `ItregePortfolioMovements_DeptCode` | String |  |  |
| 27 | `PORTFOLIO.MOVEMENTS.AUDITOR.CODE` | `ItregePortfolioMovements_AuditorCode` | String |  |  |
| 28 | `PORTFOLIO.MOVEMENTS.AUDIT.DATE.TIME` | `ItregePortfolioMovements_AuditDateTime` | String |  |  |
