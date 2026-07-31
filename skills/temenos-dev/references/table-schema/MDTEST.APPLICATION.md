# MDTEST.APPLICATION — Table Schema

> Source: `INSERTS/I_F.MDTEST.APPLICATION` in `SE_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEMD.CUSTOMER.ID` | `MdtestApplication_CustomerId` | TField |  |  |
| 2 | `SEMD.CUSTOMER.GENDER` | `MdtestApplication_CustomerGender` | TField |  |  |
| 3 | `SEMD.ACCOUNT.ID` | `MdtestApplication_AccountId` | TField |  |  |
| 4 | `SEMD.ACCOUNT.CURRENCY` | `MdtestApplication_AccountCurrency` | TField |  |  |
| 5 | `SEMD.RECORD.STATUS` | `MdtestApplication_RecordStatus` | String |  |  |
| 6 | `SEMD.CURR.NO` | `MdtestApplication_CurrNo` | String |  |  |
| 7 | `SEMD.INPUTTER` | `MdtestApplication_Inputter` |  |  |  |
| 8 | `SEMD.DATE.TIME` | `MdtestApplication_DateTime` |  |  |  |
| 9 | `SEMD.AUTHORISER` | `MdtestApplication_Authoriser` | String |  |  |
| 10 | `SEMD.CO.CODE` | `MdtestApplication_CoCode` | String |  |  |
| 11 | `SEMD.DEPT.CODE` | `MdtestApplication_DeptCode` | String |  |  |
| 12 | `SEMD.AUDITOR.CODE` | `MdtestApplication_AuditorCode` | String |  |  |
| 13 | `SEMD.AUDIT.DATE.TIME` | `MdtestApplication_AuditDateTime` | String |  |  |
| 14 | `SEMD.CUSTOMER.NAME` | `MdtestApplication_CustomerName` | TField |  |  |
| 15 | `SEMD.CUSTOMER.STATUS` | `MdtestApplication_CustomerStatus` | TField |  |  |
| 16 | `SEMD.CUSTOMER.TYPE` | `MdtestApplication_CustomerType` | TField |  |  |
| 17 | `SEMD.COUNTRY.GROUP` | `MdtestApplication_CountryGroup` | TField |  |  |
| 18 | `SEMD.COUNTRY` | `MdtestApplication_Country` |  |  |  |
| 19 | `SEMD.TRANSACTION.CODE` | `MdtestApplication_TransactionCode` | TField |  |  |
| 20 | `SEMD.SHORT.DESC` | `MdtestApplication_ShortDesc` | TField |  |  |
| 21 | `SEMD.STMT.NARR` | `MdtestApplication_StmtNarr` | TField |  |  |
