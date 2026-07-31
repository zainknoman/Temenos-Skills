# USREGS.CTR.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.CTR.DETAILS` in `USREGS_CTR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `US.CTR.CUSTOMER.NAME` | `UsregsCtrDetails_CustomerName` | TField |  | Name of the customer involved in the transaction. No input field. Field value would be defaulted from SHORT.NAME from the CUSTOMER record for CUSTOMER.1/2(TT), DEBIT.CUSTOMER/CREDIT. CUSTOMER(FT) OR PRIMARY.CUSTOMER(TFS). |
| 2 | `US.CTR.CTR.EXEMPT` | `UsregsCtrDetails_CtrExempt` | TField |  | Shows whether customer is exempt from CTR or not. No input field. Defaulted from CUSTOMER record CTR.EXEMPT. |
| 3 | `US.CTR.TXN.ID` | `UsregsCtrDetails_TxnId` |  |  |  |
| 4 | `US.CTR.TRANSACTOR` | `UsregsCtrDetails_Transactor` |  |  |  |
| 5 | `US.CTR.LEGAL.ID` | `UsregsCtrDetails_LegalId` |  |  |  |
| 6 | `US.CTR.TXN.ACCOUNT` | `UsregsCtrDetails_TxnAccount` |  |  |  |
| 7 | `US.CTR.TXN.CURRENCY` | `UsregsCtrDetails_TxnCurrency` |  |  |  |
| 8 | `US.CTR.TXN.AMOUNT.LCY` | `UsregsCtrDetails_TxnAmountLcy` |  |  |  |
| 9 | `US.CTR.CASH.IN.FCY` | `UsregsCtrDetails_CashInFcy` |  |  |  |
| 10 | `US.CTR.TXN.FCY.COUNTRY` | `UsregsCtrDetails_TxnFcyCountry` |  |  |  |
| 11 | `US.CTR.TXN.DESCRIPTION` | `UsregsCtrDetails_TxnDescription` |  |  |  |
| 12 | `US.CTR.CASH.OUT.FCY` | `UsregsCtrDetails_CashOutFcy` |  |  |  |
| 13 | `US.CTR.RESERVED.24` | `UsregsCtrDetails_Reserved24` |  |  |  |
| 14 | `US.CTR.RESERVED.23` | `UsregsCtrDetails_Reserved23` |  |  |  |
| 15 | `US.CTR.IN.TOTAL.AMT` | `UsregsCtrDetails_InTotalAmt` | TField |  | Shows the total of all LCY and FCY deposits for the day in USD. No input field. This is a total of all TXN.AMOUNT.LCY. |
| 16 | `US.CTR.OUT.TOTAL.AMT` | `UsregsCtrDetails_OutTotalAmt` | TField |  | Shows the total of all LCY and FCY withdrawals for the day in USD. No input field. This is a total of all TXN.AMOUNT.LCY. |
| 17 | `US.CTR.LIMIT.EXCEED` | `UsregsCtrDetails_LimitExceed` | TField |  | Shows whether the total cash deposits or withdrawals has exceeded the threshold amount set. No input field. |
| 18 | `US.CTR.REPORT.CTR` | `UsregsCtrDetails_ReportCtr` | TField |  | Shows whether the cash transactions for this customer are to be reported. No input field. This field gets set at the enquiry. |
| 19 | `US.CTR.DATE.OF.TXN` | `UsregsCtrDetails_DateOfTxn` | TField |  |  |
| 20 | `US.CTR.RESERVED.21` | `UsregsCtrDetails_Reserved21` | TField |  |  |
| 21 | `US.CTR.RESERVED.20` | `UsregsCtrDetails_Reserved20` | TField |  |  |
| 22 | `US.CTR.RESERVED.19` | `UsregsCtrDetails_Reserved19` | TField |  |  |
| 23 | `US.CTR.RESERVED.18` | `UsregsCtrDetails_Reserved18` | TField |  |  |
| 24 | `US.CTR.RESERVED.17` | `UsregsCtrDetails_Reserved17` | TField |  |  |
| 25 | `US.CTR.RESERVED.16` | `UsregsCtrDetails_Reserved16` | TField |  |  |
| 26 | `US.CTR.RESERVED.15` | `UsregsCtrDetails_Reserved15` | TField |  |  |
| 27 | `US.CTR.RESERVED.14` | `UsregsCtrDetails_Reserved14` | TField |  |  |
| 28 | `US.CTR.RESERVED.13` | `UsregsCtrDetails_Reserved13` | TField |  |  |
| 29 | `US.CTR.RESERVED.12` | `UsregsCtrDetails_Reserved12` | TField |  |  |
| 30 | `US.CTR.RESERVED.11` | `UsregsCtrDetails_Reserved11` | TField |  |  |
| 31 | `US.CTR.RESERVED.10` | `UsregsCtrDetails_Reserved10` | TField |  |  |
| 32 | `US.CTR.RESERVED.9` | `UsregsCtrDetails_Reserved9` | TField |  |  |
| 33 | `US.CTR.RESERVED.8` | `UsregsCtrDetails_Reserved8` | TField |  |  |
| 34 | `US.CTR.RESERVED.7` | `UsregsCtrDetails_Reserved7` | TField |  |  |
| 35 | `US.CTR.RESERVED.6` | `UsregsCtrDetails_Reserved6` | TField |  |  |
| 36 | `US.CTR.RESERVED.5` | `UsregsCtrDetails_Reserved5` | TField |  |  |
| 37 | `US.CTR.RESERVED.4` | `UsregsCtrDetails_Reserved4` | TField |  |  |
| 38 | `US.CTR.RESERVED.3` | `UsregsCtrDetails_Reserved3` | TField |  |  |
| 39 | `US.CTR.RESERVED.2` | `UsregsCtrDetails_Reserved2` | TField |  |  |
| 40 | `US.CTR.RESERVED.1` | `UsregsCtrDetails_Reserved1` | TField |  |  |
| 41 | `US.CTR.OVERRIDE` | `UsregsCtrDetails_Override` |  |  |  |
| 42 | `US.CTR.RECORD.STATUS` | `UsregsCtrDetails_RecordStatus` | String |  |  |
| 43 | `US.CTR.CURR.NO` | `UsregsCtrDetails_CurrNo` | String |  |  |
| 44 | `US.CTR.INPUTTER` | `UsregsCtrDetails_Inputter` |  |  |  |
| 45 | `US.CTR.DATE.TIME` | `UsregsCtrDetails_DateTime` |  |  |  |
| 46 | `US.CTR.AUTHORISER` | `UsregsCtrDetails_Authoriser` | String |  |  |
| 47 | `US.CTR.CO.CODE` | `UsregsCtrDetails_CoCode` | String |  |  |
| 48 | `US.CTR.DEPT.CODE` | `UsregsCtrDetails_DeptCode` | String |  |  |
| 49 | `US.CTR.AUDITOR.CODE` | `UsregsCtrDetails_AuditorCode` | String |  |  |
| 50 | `US.CTR.AUDIT.DATE.TIME` | `UsregsCtrDetails_AuditDateTime` | String |  |  |
