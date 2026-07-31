# ITREGE.BANK.TRANSFERS — Table Schema

> Source: `INSERTS/I_F.ITREGE.BANK.TRANSFERS` in `ITREGE_BankTransfers.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.TRANSACTION.TYPE` | `ItregeBankTransfers_TransactionType` | TField |  | Transaction Type. |
| 2 | `ITREGE.AMOUNT.IN.FCY` | `ItregeBankTransfers_AmountInFcy` | TField |  | Amount in Foreign CCY. |
| 3 | `ITREGE.AMOUNT.IN.LCY` | `ItregeBankTransfers_AmountInLcy` | TField |  | Amount in Local CCY. |
| 4 | `ITREGE.CUST.PROVINCE` | `ItregeBankTransfers_CustProvince` | TField |  | Customer Province. |
| 5 | `ITREGE.CUST.COUNTRY` | `ItregeBankTransfers_CustCountry` | TField |  | Customer Country. |
| 6 | `ITREGE.TXN.DIRECTION` | `ItregeBankTransfers_TxnDirection` | TField |  | Transaction Direction. |
| 7 | `ITREGE.TXN.DATE` | `ItregeBankTransfers_TxnDate` | TField |  | Transaction Date. |
| 8 | `ITREGE.AMOUNT.CLASS` | `ItregeBankTransfers_AmountClass` | TField |  | Amount Class. |
| 9 | `ITREGE.CREDIT.TRANSFER.TYPE` | `ItregeBankTransfers_CreditTransferType` | TField |  | Type of Credit Transfer. |
| 10 | `ITREGE.SETTLE.METHODS` | `ItregeBankTransfers_SettleMethods` | TField |  | Settlement Method. |
| 11 | `ITREGE.CUST.RESIDENCE` | `ItregeBankTransfers_CustResidence` | TField |  |  |
| 12 | `ITREGE.CUST.SECTOR` | `ItregeBankTransfers_CustSector` | TField |  |  |
| 13 | `ITREGE.RESERVED.10` | `ItregeBankTransfers_Reserved10` | TField |  |  |
| 14 | `ITREGE.RESERVED.9` | `ItregeBankTransfers_Reserved9` | TField |  |  |
| 15 | `ITREGE.RESERVED.8` | `ItregeBankTransfers_Reserved8` | TField |  |  |
| 16 | `ITREGE.RESERVED.7` | `ItregeBankTransfers_Reserved7` | TField |  |  |
| 17 | `ITREGE.RESERVED.6` | `ItregeBankTransfers_Reserved6` | TField |  |  |
| 18 | `ITREGE.RESERVED.5` | `ItregeBankTransfers_Reserved5` | TField |  |  |
| 19 | `ITREGE.RESERVED.4` | `ItregeBankTransfers_Reserved4` | TField |  |  |
| 20 | `ITREGE.RESERVED.3` | `ItregeBankTransfers_Reserved3` | TField |  |  |
| 21 | `ITREGE.RESERVED.2` | `ItregeBankTransfers_Reserved2` | TField |  |  |
| 22 | `ITREGE.RESERVED.1` | `ItregeBankTransfers_Reserved1` | TField |  |  |
| 23 | `ITREGE.OVERRIDE` | `ItregeBankTransfers_Override` |  |  |  |
| 24 | `ITREGE.RECORD.STATUS` | `ItregeBankTransfers_RecordStatus` | String |  |  |
| 25 | `ITREGE.CURR.NO` | `ItregeBankTransfers_CurrNo` | String |  |  |
| 26 | `ITREGE.INPUTTER` | `ItregeBankTransfers_Inputter` |  |  |  |
| 27 | `ITREGE.DATE.TIME` | `ItregeBankTransfers_DateTime` |  |  |  |
| 28 | `ITREGE.AUTHORISER` | `ItregeBankTransfers_Authoriser` | String |  |  |
| 29 | `ITREGE.CO.CODE` | `ItregeBankTransfers_CoCode` | String |  |  |
| 30 | `ITREGE.DEPT.CODE` | `ItregeBankTransfers_DeptCode` | String |  |  |
| 31 | `ITREGE.AUDITOR.CODE` | `ItregeBankTransfers_AuditorCode` | String |  |  |
| 32 | `ITREGE.AUDIT.DATE.TIME` | `ItregeBankTransfers_AuditDateTime` | String |  |  |
