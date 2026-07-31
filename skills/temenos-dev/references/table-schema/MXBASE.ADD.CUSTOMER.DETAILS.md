# MXBASE.ADD.CUSTOMER.DETAILS — Table Schema

> Source: `INSERTS/I_F.MXBASE.ADD.CUSTOMER.DETAILS` in `MXBASE_CustomerRegulatory.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MXBASE.CUST.TYPE.EMPOWERED` | `MxbaseAddCustomerDetails_TypeEmpowered` |  |  |  |
| 2 | `MXBASE.CUST.EMPOWERED.ID` | `MxbaseAddCustomerDetails_EmpoweredId` |  |  |  |
| 3 | `MXBASE.CUST.EMPLOYMENT.STATUS` | `MxbaseAddCustomerDetails_EmploymentStatus` |  |  |  |
| 4 | `MXBASE.CUST.RISK.CLASS` | `MxbaseAddCustomerDetails_RiskClass` | TField |  | This file holds risk classification. |
| 5 | `MXBASE.CUST.RISK.CLASS.DATE` | `MxbaseAddCustomerDetails_RiskClassDate` | TField |  | This field holds risk classification date. |
| 6 | `MXBASE.CUST.COMMENTS` | `MxbaseAddCustomerDetails_Comments` | TField |  | This field holds additional comments if needed. |
| 7 | `MXBASE.CUST.RELATION.CLIENT` | `MxbaseAddCustomerDetails_RelationClient` | TField |  | This field holds the client related. Option field which will accept yes or no. |
| 8 | `MXBASE.CUST.ACCREDITATION.TYPE` | `MxbaseAddCustomerDetails_AccreditationType` | TField |  | This field holds the accreditation type of relationship. |
| 9 | `MXBASE.CUST.RELATION.TYPE` | `MxbaseAddCustomerDetails_RelationType` | TField |  | This field holds the relationship type. |
| 10 | `MXBASE.CUST.CNBV.ECONOMIC.GROUP` | `MxbaseAddCustomerDetails_CnbvEconomicGroup` | TField |  | This field holds the economic group of the CNBV. |
| 11 | `MXBASE.CUST.CORPORATE.CUSTOMER.TYPE` | `MxbaseAddCustomerDetails_CorporateCustomerType` | TField |  | This field holds the customer type for corporate customers. |
| 12 | `MXBASE.CUST.LIMITED.COMPANY` | `MxbaseAddCustomerDetails_LimitedCompany` | TField |  | This field holds the type of company. |
| 13 | `MXBASE.CUST.MXBASE.CONSTITUTION.TYPE` | `MxbaseAddCustomerDetails_MxbaseConstitutionType` |  |  |  |
| 14 | `MXBASE.CUST.REGISTRATION.COMPANY.NO` | `MxbaseAddCustomerDetails_RegistrationCompanyNo` |  |  |  |
| 15 | `MXBASE.CUST.DATE.REGISTRATION` | `MxbaseAddCustomerDetails_DateRegistration` |  |  |  |
| 16 | `MXBASE.CUST.END.REGISTRATION` | `MxbaseAddCustomerDetails_EndRegistration` |  |  |  |
| 17 | `MXBASE.CUST.COUNTRY.REGISTERED` | `MxbaseAddCustomerDetails_CountryRegistered` |  |  |  |
| 18 | `MXBASE.CUST.STATE.REGISTERED` | `MxbaseAddCustomerDetails_StateRegistered` |  |  |  |
| 19 | `MXBASE.CUST.MUNICIPALITY.REGISTERED` | `MxbaseAddCustomerDetails_MunicipalityRegistered` |  |  |  |
| 20 | `MXBASE.CUST.TOMO` | `MxbaseAddCustomerDetails_Tomo` |  |  |  |
| 21 | `MXBASE.CUST.FOLIO` | `MxbaseAddCustomerDetails_Folio` |  |  |  |
| 22 | `MXBASE.CUST.ASIENTO` | `MxbaseAddCustomerDetails_Asiento` |  |  |  |
| 23 | `MXBASE.CUST.CAPITAL` | `MxbaseAddCustomerDetails_Capital` |  |  |  |
| 24 | `MXBASE.CUST.NOTARY.NAME` | `MxbaseAddCustomerDetails_NotaryName` |  |  |  |
| 25 | `MXBASE.CUST.NOTARY.FATHER.LAST.NAME` | `MxbaseAddCustomerDetails_NotaryFatherLastName` |  |  |  |
| 26 | `MXBASE.CUST.NOTARY.MOTHER.LAST.NAME` | `MxbaseAddCustomerDetails_NotaryMotherLastName` |  |  |  |
| 27 | `MXBASE.CUST.NOTARY.LEGAL.DOC.NAME` | `MxbaseAddCustomerDetails_NotaryLegalDocName` |  |  |  |
| 28 | `MXBASE.CUST.REGISTRATION.NOTARY.NUMBER` | `MxbaseAddCustomerDetails_RegistrationNotaryNumber` |  |  |  |
| 29 | `MXBASE.CUST.NOTARY.STATE` | `MxbaseAddCustomerDetails_NotaryState` |  |  |  |
| 30 | `MXBASE.CUST.EXPIRY.DATE` | `MxbaseAddCustomerDetails_ExpiryDate` |  |  |  |
| 31 | `MXBASE.CUST.TYPE.SIGNATURE` | `MxbaseAddCustomerDetails_TypeSignature` | TField |  | This field holds the Type of the signature. |
| 32 | `MXBASE.CUST.JOB.POSITION` | `MxbaseAddCustomerDetails_JobPosition` | TField |  | This field holds the job position. |
| 33 | `MXBASE.CUST.REFERRAL.LAST.NAME` | `MxbaseAddCustomerDetails_ReferralLastName` |  |  |  |
| 34 | `MXBASE.CUST.REFERRAL.MOTHER.MAIDEN.NAME` | `MxbaseAddCustomerDetails_ReferralMotherMaidenName` |  |  |  |
| 35 | `MXBASE.CUST.REFERRAL.PHONE.NUMBER.1` | `MxbaseAddCustomerDetails_ReferralPhoneNumber1` |  |  |  |
| 36 | `MXBASE.CUST.REFERRAL.PHONE.NUMBER.2` | `MxbaseAddCustomerDetails_ReferralPhoneNumber2` |  |  |  |
| 37 | `MXBASE.CUST.REFERRAL.TELEPHONE.NUMBER` | `MxbaseAddCustomerDetails_ReferralTelephoneNumber` |  |  |  |
| 38 | `MXBASE.CUST.REFERRAL.EMAIL` | `MxbaseAddCustomerDetails_ReferralEmail` |  |  |  |
| 39 | `MXBASE.CUST.BANK.REFERENCE` | `MxbaseAddCustomerDetails_BankReference` |  |  |  |
| 40 | `MXBASE.CUST.BRANCH` | `MxbaseAddCustomerDetails_Branch` |  |  |  |
| 41 | `MXBASE.CUST.ACCOUNT.TYPE` | `MxbaseAddCustomerDetails_AccountType` |  |  |  |
| 42 | `MXBASE.CUST.ACCOUNT.NUMBER` | `MxbaseAddCustomerDetails_AccountNumber` |  |  |  |
| 43 | `MXBASE.CUST.ACCOUNT.SINCE` | `MxbaseAddCustomerDetails_AccountSince` |  |  |  |
| 44 | `MXBASE.CUST.NUMBER.OF.EMPLOYEES` | `MxbaseAddCustomerDetails_NumberOfEmployees` | TField |  | This field holds the number of employees. |
| 45 | `MXBASE.CUST.GEO.COVERAGE` | `MxbaseAddCustomerDetails_GeoCoverage` | TField |  | This field holds the geographic coverage of the bank. |
| 46 | `MXBASE.CUST.OTHERS` | `MxbaseAddCustomerDetails_Others` | TField |  | This field holds other economic information needed. |
| 47 | `MXBASE.CUST.NUMBER.OF.BRANCH` | `MxbaseAddCustomerDetails_NumberOfBranch` | TField |  | This field holds the number of branches held by the bank. |
| 48 | `MXBASE.CUST.MAIN.CITIES` | `MxbaseAddCustomerDetails_MainCities` |  |  |  |
| 49 | `MXBASE.CUST.PRODUCT.SERVICES` | `MxbaseAddCustomerDetails_ProductServices` |  |  |  |
| 50 | `MXBASE.CUST.TOTAL.ANNUAL.SALES` | `MxbaseAddCustomerDetails_TotalAnnualSales` | TField |  | This field holds the total annual sales. |
| 51 | `MXBASE.CUST.TOTAL.ASSETS` | `MxbaseAddCustomerDetails_TotalAssets` | TField |  | This field holds the total assets held by the client. |
| 52 | `MXBASE.CUST.TOTAL.LIABILITY` | `MxbaseAddCustomerDetails_TotalLiability` | TField |  | This field holds the total liabilities held by the client. |
| 53 | `MXBASE.CUST.STOCK.HOLDER.EQUITY` | `MxbaseAddCustomerDetails_StockHolderEquity` | TField |  | Stock holders equity. This is a no input field. The value is calculated automatically based on the total asset and liabilities. |
| 54 | `MXBASE.CUST.IMPORTATION.AMOUNT` | `MxbaseAddCustomerDetails_ImportationAmount` | TField |  | This field holds the total amount of the importations. |
| 55 | `MXBASE.CUST.IMPORTATION.COUNTRIES` | `MxbaseAddCustomerDetails_ImportationCountries` | TField |  | This field holds the countries from where imporations happen. |
| 56 | `MXBASE.CUST.IMPORTATION.EXPORTATION` | `MxbaseAddCustomerDetails_ImportationExportation` | TField |  | This field holds the total amount of exporations. |
| 57 | `MXBASE.CUST.EXPORTATION.COUNTRIES` | `MxbaseAddCustomerDetails_ExportationCountries` | TField |  | This field holds the countries to which it is exported. |
| 58 | `MXBASE.CUST.ACCOUNT.PURPOSE` | `MxbaseAddCustomerDetails_AccountPurpose` | TField |  | This field holds the purpose of opening the account. |
| 59 | `MXBASE.CUST.OTHER.PURPOSE` | `MxbaseAddCustomerDetails_OtherPurpose` | TField |  | This field holds the other reasons for openig the account. |
| 60 | `MXBASE.CUST.SOURCE.REC` | `MxbaseAddCustomerDetails_SourceRec` | TField |  | This field holds the source of the Income. |
| 61 | `MXBASE.CUST.OTHER.SOURCE` | `MxbaseAddCustomerDetails_OtherSource` | TField |  | This field holds the other sources of income. |
| 62 | `MXBASE.CUST.MONTHLY.APPROX.INCOME` | `MxbaseAddCustomerDetails_MonthlyApproxIncome` | TField |  | This field holds the approximate monthly income. |
| 63 | `MXBASE.CUST.TYPE` | `MxbaseAddCustomerDetails_Type` | TField |  | This field holds the types of income. |
| 64 | `MXBASE.CUST.APPROX` | `MxbaseAddCustomerDetails_Approx` | TField |  | This field holds the approximate percentage of the income. |
| 65 | `MXBASE.CUST.DAILY.MIN.AMOUNT` | `MxbaseAddCustomerDetails_DailyMinAmount` | TField |  | This field holds the daily minimum amount utilized. |
| 66 | `MXBASE.CUST.DAILY.MAX.AMOUNT` | `MxbaseAddCustomerDetails_DailyMaxAmount` | TField |  | This field holds the daily maximum amount utilized. |
| 67 | `MXBASE.CUST.TRANSFER.DAILY.MINIMUM` | `MxbaseAddCustomerDetails_TransferDailyMinimum` | TField |  | This field holds the minimum amount transferred daily. |
| 68 | `MXBASE.CUST.DAILY.TRANSFER.MAXIMUM` | `MxbaseAddCustomerDetails_DailyTransferMaximum` | TField |  | This field holds the maximum amount transferred daily. |
| 69 | `MXBASE.CUST.TYPE.OF.OPERATION` | `MxbaseAddCustomerDetails_TypeOfOperation` |  |  |  |
| 70 | `MXBASE.CUST.TRANSACTION.AMOUNT.MONTHLY` | `MxbaseAddCustomerDetails_TransactionAmountMonthly` |  |  |  |
| 71 | `MXBASE.CUST.TRANSACTION.OPERATION.NUMBER` | `MxbaseAddCustomerDetails_TransactionOperationNumber` |  |  |  |
| 72 | `MXBASE.CUST.NUMBER.OF.TRUST` | `MxbaseAddCustomerDetails_NumberOfTrust` | TField |  | This field holds the number of the trust or mandate. |
| 73 | `MXBASE.CUST.TYPE.TRUST` | `MxbaseAddCustomerDetails_TypeTrust` | TField |  | This field holds the type of the trust or mandate. |
| 74 | `MXBASE.CUST.CONSTITUTION.STATE` | `MxbaseAddCustomerDetails_ConstitutionState` | TField |  | This field holds the state of the constitution. |
| 75 | `MXBASE.CUST.CONSTITUTION.DATE` | `MxbaseAddCustomerDetails_ConstitutionDate` | TField |  | This field holds the date of constitution. |
| 76 | `MXBASE.CUST.TYPE.INSTITUTE` | `MxbaseAddCustomerDetails_TypeInstitute` | TField |  | This field holds the type of the institutions. |
| 77 | `MXBASE.CUST.NAME.INSTITUTE` | `MxbaseAddCustomerDetails_NameInstitute` | TField |  | This field holds the name of intitutions |
| 78 | `MXBASE.CUST.TRUST.PURPOSE` | `MxbaseAddCustomerDetails_TrustPurpose` | TField |  | This field holds the trust purpose |
| 79 | `MXBASE.CUST.ECONOMIC.ACTIVITY` | `MxbaseAddCustomerDetails_EconomicActivity` | TField |  |  |
| 80 | `MXBASE.CUST.OVERRIDE` | `MxbaseAddCustomerDetails_Override` |  |  |  |
| 81 | `MXBASE.CUST.RECORD.STATUS` | `MxbaseAddCustomerDetails_RecordStatus` | String |  |  |
| 82 | `MXBASE.CUST.CURR.NO` | `MxbaseAddCustomerDetails_CurrNo` | String |  |  |
| 83 | `MXBASE.CUST.INPUTTER` | `MxbaseAddCustomerDetails_Inputter` |  |  |  |
| 84 | `MXBASE.CUST.DATE.TIME` | `MxbaseAddCustomerDetails_DateTime` |  |  |  |
| 85 | `MXBASE.CUST.AUTHORISER` | `MxbaseAddCustomerDetails_Authoriser` | String |  |  |
| 86 | `MXBASE.CUST.CO.CODE` | `MxbaseAddCustomerDetails_CoCode` | String |  |  |
| 87 | `MXBASE.CUST.DEPT.CODE` | `MxbaseAddCustomerDetails_DeptCode` | String |  |  |
| 88 | `MXBASE.CUST.AUDITOR.CODE` | `MxbaseAddCustomerDetails_AuditorCode` | String |  |  |
| 89 | `MXBASE.CUST.AUDIT.DATE.TIME` | `MxbaseAddCustomerDetails_AuditDateTime` | String |  |  |
| 90 | `MXBASE.CUST.REFERRAL.FIRST.NAME` | `MxbaseAddCustomerDetails_ReferralFirstName` |  |  |  |
| 91 | `MXBASE.CUST.REFERRAL.SECOND.NAME` | `MxbaseAddCustomerDetails_ReferralSecondName` |  |  |  |
