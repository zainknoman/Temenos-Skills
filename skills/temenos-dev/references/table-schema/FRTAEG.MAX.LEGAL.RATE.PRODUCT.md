# FRTAEG.MAX.LEGAL.RATE.PRODUCT — Table Schema

> Source: `INSERTS/I_F.FRTAEG.MAX.LEGAL.RATE.PRODUCT` in `FRTAEG_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MLR.PROD.DESCRIPTION` | `FrtaegMaxLegalRateProduct_Description` | TField |  | Manul Input by Bank Users. For Example. 001 - Personal Loan 002 - Mortgage Loan etc Upto the Bank to decide. |
| 2 | `MLR.PROD.DATE` | `FrtaegMaxLegalRateProduct_Date` | TField |  | Date Format (Auto Default to Date in @ID) |
| 3 | `MLR.PROD.NO.OF.DECIMALS` | `FrtaegMaxLegalRateProduct_NoOfDecimals` | TField |  | Number. Defines the No of Decimals in MLR.RATE and also the No of Decimals to which the TEG / TAEG to be Rounded off. |
| 4 | `MLR.PROD.SECTOR` | `FrtaegMaxLegalRateProduct_Sector` |  |  |  |
| 5 | `MLR.PROD.CATEGORY` | `FrtaegMaxLegalRateProduct_Category` |  |  |  |
| 6 | `MLR.PROD.LOAN.FROM.AMOUNT` | `FrtaegMaxLegalRateProduct_LoanFromAmount` |  |  |  |
| 7 | `MLR.PROD.LOAN.TO.AMOUNT` | `FrtaegMaxLegalRateProduct_LoanToAmount` |  |  |  |
| 8 | `MLR.PROD.LOAN.FROM.TERM` | `FrtaegMaxLegalRateProduct_LoanFromTerm` |  |  |  |
| 9 | `MLR.PROD.LOAN.TO.TERM` | `FrtaegMaxLegalRateProduct_LoanToTerm` |  |  |  |
| 10 | `MLR.PROD.LOAN.MLR.RATE` | `FrtaegMaxLegalRateProduct_LoanMlrRate` |  |  |  |
| 11 | `MLR.PROD.INITIAL.MLR` | `FrtaegMaxLegalRateProduct_InitialMlr` |  |  |  |
| 12 | `MLR.PROD.LOAN.TYPE` | `FrtaegMaxLegalRateProduct_LoanType` |  |  |  |
| 13 | `MLR.PROD.PRINCIPAL.PROPERTY` | `FrtaegMaxLegalRateProduct_PrincipalProperty` |  |  |  |
| 14 | `MLR.PROD.INTEREST.PROPERTY` | `FrtaegMaxLegalRateProduct_InterestProperty` |  |  |  |
| 15 | `MLR.PROD.RESERVED.3` | `FrtaegMaxLegalRateProduct_Reserved3` | TField |  |  |
| 16 | `MLR.PROD.RESERVED.2` | `FrtaegMaxLegalRateProduct_Reserved2` | TField |  |  |
| 17 | `MLR.PROD.RESERVED.1` | `FrtaegMaxLegalRateProduct_Reserved1` | TField |  |  |
| 18 | `MLR.PROD.LOCAL.REF` | `FrtaegMaxLegalRateProduct_LocalRef` |  |  |  |
| 19 | `MLR.PROD.OVERRIDE` | `FrtaegMaxLegalRateProduct_Override` |  |  |  |
| 20 | `MLR.PROD.RECORD.STATUS` | `FrtaegMaxLegalRateProduct_RecordStatus` | String |  |  |
| 21 | `MLR.PROD.CURR.NO` | `FrtaegMaxLegalRateProduct_CurrNo` | String |  |  |
| 22 | `MLR.PROD.INPUTTER` | `FrtaegMaxLegalRateProduct_Inputter` |  |  |  |
| 23 | `MLR.PROD.DATE.TIME` | `FrtaegMaxLegalRateProduct_DateTime` |  |  |  |
| 24 | `MLR.PROD.AUTHORISER` | `FrtaegMaxLegalRateProduct_Authoriser` | String |  |  |
| 25 | `MLR.PROD.CO.CODE` | `FrtaegMaxLegalRateProduct_CoCode` | String |  |  |
| 26 | `MLR.PROD.DEPT.CODE` | `FrtaegMaxLegalRateProduct_DeptCode` | String |  |  |
| 27 | `MLR.PROD.AUDITOR.CODE` | `FrtaegMaxLegalRateProduct_AuditorCode` | String |  |  |
| 28 | `MLR.PROD.AUDIT.DATE.TIME` | `FrtaegMaxLegalRateProduct_AuditDateTime` | String |  |  |
