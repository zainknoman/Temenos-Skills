# ILSBLF.FRAMEWORK.AGREEMENT — Table Schema

> Source: `INSERTS/I_F.ILSBLF.FRAMEWORK.AGREEMENT` in `ILSBLF_AgreementConditions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILSBLF.FA.CUSTOMER` | `IlsblfFrameworkAgreement_Customer` | TField |  | This indicates the customer for whom the lending/borrowing limit is being set. |
| 2 | `ILSBLF.FA.PORTFOLIO` | `IlsblfFrameworkAgreement_Portfolio` | TField |  | This indicates the portfolio for which the lending/borrowing limit is being set. |
| 3 | `ILSBLF.FA.STOCK.EXCHANGE` | `IlsblfFrameworkAgreement_StockExchange` | TField |  | This indicates the Stock exchange for which the lending/borrowing limit is being set. |
| 4 | `ILSBLF.FA.SECURITY.TYPE` | `IlsblfFrameworkAgreement_SecurityType` | TField |  | This indicates the Security Type which the lending/borrowing limit is being set. |
| 5 | `ILSBLF.FA.SECURITY.CODE` | `IlsblfFrameworkAgreement_SecurityCode` | TField |  | This indicates the Security for which the lending/borrowing limit is being set. |
| 6 | `ILSBLF.FA.DEFAULT.PERIOD` | `IlsblfFrameworkAgreement_DefaultPeriod` | TField |  | The default period associated with the SBL transactions at this hierarchy. |
| 7 | `ILSBLF.FA.EXPIRY.DATE` | `IlsblfFrameworkAgreement_ExpiryDate` | TField |  | This indicates the date till the record holds valid. |
| 8 | `ILSBLF.FA.CURRENCY` | `IlsblfFrameworkAgreement_Currency` | TField |  | The currency in which the amount fields of the agreement are specified. |
| 9 | `ILSBLF.FA.MIN.LENDING.AMT` | `IlsblfFrameworkAgreement_MinLendingAmt` | TField |  | This indicates the minimum lending amount for the SBL trade in the specified currency. |
| 10 | `ILSBLF.FA.MIN.LENDING.PCT` | `IlsblfFrameworkAgreement_MinLendingPct` | TField |  | This indicates the minimum lending limit percentage. |
| 11 | `ILSBLF.FA.MAX.LENDING.AMT` | `IlsblfFrameworkAgreement_MaxLendingAmt` | TField |  | This indicates the maximum lending amount for the SBL trade in the SBL trade currency |
| 12 | `ILSBLF.FA.MAX.LENDING.PCT` | `IlsblfFrameworkAgreement_MaxLendingPct` | TField |  | This indicates the maximum lending percentage for the SBL trade. |
| 13 | `ILSBLF.FA.MIN.BORROWING.AMT` | `IlsblfFrameworkAgreement_MinBorrowingAmt` | TField |  | This indicates the minimum borrowing amount for the SBL trade in the SBL trade currency. |
| 14 | `ILSBLF.FA.MIN.BORROWING.PCT` | `IlsblfFrameworkAgreement_MinBorrowingPct` | TField |  | This indicates the minimum borrowing limit percentage. |
| 15 | `ILSBLF.FA.MAX.BORROWING.AMT` | `IlsblfFrameworkAgreement_MaxBorrowingAmt` | TField |  | This indicates the maximum borrowing amount for the SBL trade in the SBL trade currency. |
| 16 | `ILSBLF.FA.MAX.BORROWING.PCT` | `IlsblfFrameworkAgreement_MaxBorrowingPct` | TField |  | This indicates the maximum borrowing limit percentage. |
| 17 | `ILSBLF.FA.ALLOWED.TO.OWN.BOOK.LEND` | `IlsblfFrameworkAgreement_AllowedToOwnBookLend` | TField |  | Indicates if the customer/portfolio is permitted to lend to own book. |
| 18 | `ILSBLF.FA.ALLOWED.TO.OWN.BOOK.BORROW` | `IlsblfFrameworkAgreement_AllowedToOwnBookBorrow` | TField |  | Indicates if the customer/portfolio is permitted to borrow from own book portfolios. |
| 19 | `ILSBLF.FA.TRM.BRW.BF.EXP.DATE` | `IlsblfFrameworkAgreement_TrmBrwBfExpDate` | TField |  | Checkbox/Flag to indicate if the borrowing agreement can be terminated prior to the expiry date. |
| 20 | `ILSBLF.FA.TRM.LND.BF.EXP.DATE` | `IlsblfFrameworkAgreement_TrmLndBfExpDate` | TField |  | Checkbox/Flag to indicate if the lending agreement can be terminated prior to the expiry date. |
| 21 | `ILSBLF.FA.CALL.DAYS` | `IlsblfFrameworkAgreement_CallDays` | TField |  | This is expected to hold the number of Call days. |
| 22 | `ILSBLF.FA.FINE.PCT` | `IlsblfFrameworkAgreement_FinePct` | TField |  | This is expected to hold the fine % in case of contract breaches. |
| 23 | `ILSBLF.FA.EXCLUDED.INSTR` | `IlsblfFrameworkAgreement_ExcludedInstr` |  |  |  |
| 24 | `ILSBLF.FA.LOCAL.REF` | `IlsblfFrameworkAgreement_LocalRef` |  |  |  |
| 25 | `ILSBLF.FA.OVERRIDE` | `IlsblfFrameworkAgreement_Override` |  |  |  |
| 26 | `ILSBLF.FA.RECORD.STATUS` | `IlsblfFrameworkAgreement_RecordStatus` | String |  |  |
| 27 | `ILSBLF.FA.CURR.NO` | `IlsblfFrameworkAgreement_CurrNo` | String |  |  |
| 28 | `ILSBLF.FA.INPUTTER` | `IlsblfFrameworkAgreement_Inputter` |  |  |  |
| 29 | `ILSBLF.FA.DATE.TIME` | `IlsblfFrameworkAgreement_DateTime` |  |  |  |
| 30 | `ILSBLF.FA.AUTHORISER` | `IlsblfFrameworkAgreement_Authoriser` | String |  |  |
| 31 | `ILSBLF.FA.CO.CODE` | `IlsblfFrameworkAgreement_CoCode` | String |  |  |
| 32 | `ILSBLF.FA.DEPT.CODE` | `IlsblfFrameworkAgreement_DeptCode` | String |  |  |
| 33 | `ILSBLF.FA.AUDITOR.CODE` | `IlsblfFrameworkAgreement_AuditorCode` | String |  |  |
| 34 | `ILSBLF.FA.AUDIT.DATE.TIME` | `IlsblfFrameworkAgreement_AuditDateTime` | String |  |  |
