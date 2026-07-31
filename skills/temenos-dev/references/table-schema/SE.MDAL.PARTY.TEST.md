# SE.MDAL.PARTY.TEST — Table Schema

> Source: `INSERTS/I_F.SE.MDAL.PARTY.TEST` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.MD.DEBIT.PARTY.ID` | `SeMdalPartyTest_DebitPartyId` | TField |  |  |
| 2 | `SE.MD.DEBIT.PARTY.TITLE` | `SeMdalPartyTest_DebitPartyTitle` | TField |  |  |
| 3 | `SE.MD.DEBIT.PARTY.FIRSTNAME` | `SeMdalPartyTest_DebitPartyFirstname` | TField |  |  |
| 4 | `SE.MD.DEBIT.PARTY.ADD.FROM.DATE` | `SeMdalPartyTest_DebitPartyAddFromDate` |  |  |  |
| 5 | `SE.MD.DEBIT.PARTY.ADD.TO.DATE` | `SeMdalPartyTest_DebitPartyAddToDate` |  |  |  |
| 6 | `SE.MD.DEBIT.PARTY.CITY` | `SeMdalPartyTest_DebitPartyCity` |  |  |  |
| 7 | `SE.MD.DEBIT.PARTY.COUNTRY` | `SeMdalPartyTest_DebitPartyCountry` |  |  |  |
| 8 | `SE.MD.DEBIT.RESERVEDFIELDS.07` | `SeMdalPartyTest_DebitReservedfields07` |  |  |  |
| 9 | `SE.MD.DEBIT.RESERVEDFIELDS.06` | `SeMdalPartyTest_DebitReservedfields06` |  |  |  |
| 10 | `SE.MD.DEBIT.RESERVEDFIELDS.05` | `SeMdalPartyTest_DebitReservedfields05` |  |  |  |
| 11 | `SE.MD.DEBIT.PARTY.EXTN.KEY` | `SeMdalPartyTest_DebitPartyExtnKey` |  |  |  |
| 12 | `SE.MD.DEBIT.PARTY.EXTN.VALUE` | `SeMdalPartyTest_DebitPartyExtnValue` |  |  |  |
| 13 | `SE.MD.DEBIT.PARTY.ANNUAL.CURRENCY` | `SeMdalPartyTest_DebitPartyAnnualCurrency` | TField |  |  |
| 14 | `SE.MD.DEBIT.PARTY.ANNUAL.INCOME` | `SeMdalPartyTest_DebitPartyAnnualIncome` | TField |  |  |
| 15 | `SE.MD.DEBIT.PARTY.LEGALID.KEY` | `SeMdalPartyTest_DebitPartyLegalidKey` |  |  |  |
| 16 | `SE.MD.DEBIT.PARTY.LEGALID.VALUE` | `SeMdalPartyTest_DebitPartyLegalidValue` |  |  |  |
| 17 | `SE.MD.DEBIT.PARTY.EMP.STATUS` | `SeMdalPartyTest_DebitPartyEmpStatus` | TField |  |  |
| 18 | `SE.MD.DEBIT.PARTY.EMP.FROM.DATE` | `SeMdalPartyTest_DebitPartyEmpFromDate` |  |  |  |
| 19 | `SE.MD.DEBIT.PARTY.EMP.TO.DATE` | `SeMdalPartyTest_DebitPartyEmpToDate` |  |  |  |
| 20 | `SE.MD.DEBIT.PARTY.EMPLOYER` | `SeMdalPartyTest_DebitPartyEmployer` |  |  |  |
| 21 | `SE.MD.DEBIT.PARTY.DOCUMENT.TYPE` | `SeMdalPartyTest_DebitPartyDocumentType` | TField |  |  |
| 22 | `SE.MD.DEBIT.PARTY.DOC.ISSUED.BY` | `SeMdalPartyTest_DebitPartyDocIssuedBy` | TField |  |  |
| 23 | `SE.MD.CREDIT.PARTY.ID` | `SeMdalPartyTest_CreditPartyId` | TField |  |  |
| 24 | `SE.MD.CREDIT.PARTY.TITLE` | `SeMdalPartyTest_CreditPartyTitle` | TField |  |  |
| 25 | `SE.MD.CREDIT.PARTY.FIRSTNAME` | `SeMdalPartyTest_CreditPartyFirstname` | TField |  |  |
| 26 | `SE.MD.CREDIT.PARTY.ADD.FROM.DATE` | `SeMdalPartyTest_CreditPartyAddFromDate` |  |  |  |
| 27 | `SE.MD.CREDIT.PARTY.ADD.TO.DATE` | `SeMdalPartyTest_CreditPartyAddToDate` |  |  |  |
| 28 | `SE.MD.CREDIT.PARTY.CITY` | `SeMdalPartyTest_CreditPartyCity` |  |  |  |
| 29 | `SE.MD.CREDIT.PARTY.COUNTRY` | `SeMdalPartyTest_CreditPartyCountry` |  |  |  |
| 30 | `SE.MD.CREDIT.RESERVEDFIELDS.04` | `SeMdalPartyTest_CreditReservedfields04` |  |  |  |
| 31 | `SE.MD.CREDIT.RESERVEDFIELDS.03` | `SeMdalPartyTest_CreditReservedfields03` |  |  |  |
| 32 | `SE.MD.CREDIT.RESERVEDFIELDS.02` | `SeMdalPartyTest_CreditReservedfields02` |  |  |  |
| 33 | `SE.MD.CREDIT.RESERVEDFIELDS.01` | `SeMdalPartyTest_CreditReservedfields01` |  |  |  |
| 34 | `SE.MD.CREDIT.PARTY.EXTN.KEY` | `SeMdalPartyTest_CreditPartyExtnKey` |  |  |  |
| 35 | `SE.MD.CREDIT.PARTY.EXTN.VALUE` | `SeMdalPartyTest_CreditPartyExtnValue` |  |  |  |
| 36 | `SE.MD.CREDIT.PARTY.ANNUAL.CURRENCY` | `SeMdalPartyTest_CreditPartyAnnualCurrency` | TField |  |  |
| 37 | `SE.MD.CREDIT.PARTY.ANNUAL.INCOME` | `SeMdalPartyTest_CreditPartyAnnualIncome` | TField |  |  |
| 38 | `SE.MD.CREDIT.PARTY.LEGALID.KEY` | `SeMdalPartyTest_CreditPartyLegalidKey` |  |  |  |
| 39 | `SE.MD.CREDIT.PARTY.LEGALID.VALUE` | `SeMdalPartyTest_CreditPartyLegalidValue` |  |  |  |
| 40 | `SE.MD.CREDIT.PARTY.EMP.STATUS` | `SeMdalPartyTest_CreditPartyEmpStatus` | TField |  |  |
| 41 | `SE.MD.CREDIT.PARTY.EMP.FROM.DATE` | `SeMdalPartyTest_CreditPartyEmpFromDate` |  |  |  |
| 42 | `SE.MD.CREDIT.PARTY.EMP.TO.DATE` | `SeMdalPartyTest_CreditPartyEmpToDate` |  |  |  |
| 43 | `SE.MD.CREDIT.PARTY.EMPLOYER` | `SeMdalPartyTest_CreditPartyEmployer` |  |  |  |
| 44 | `SE.MD.CREDIT.PARTY.DOCUMENT.TYPE` | `SeMdalPartyTest_CreditPartyDocumentType` | TField |  |  |
| 45 | `SE.MD.CREDIT.PARTY.DOC.ISSUED.BY` | `SeMdalPartyTest_CreditPartyDocIssuedBy` | TField |  |  |
| 46 | `SE.MD.LOCAL.DEBIT.PARTY.ID` | `SeMdalPartyTest_LocalDebitPartyId` | TField |  |  |
| 47 | `SE.MD.LOCAL.DEBIT.PARTY.NAME` | `SeMdalPartyTest_LocalDebitPartyName` | TField |  |  |
| 48 | `SE.MD.LOCAL.CREDIT.PARTY.ID` | `SeMdalPartyTest_LocalCreditPartyId` | TField |  |  |
| 49 | `SE.MD.LOCAL.CREDIT.PARTY.NAME` | `SeMdalPartyTest_LocalCreditPartyName` | TField |  |  |
| 50 | `SE.MD.LOCAL.REF` | `SeMdalPartyTest_LocalRef` |  |  |  |
| 51 | `SE.MD.OVERRIDE` | `SeMdalPartyTest_Override` |  |  |  |
| 52 | `SE.MD.RECORD.STATUS` | `SeMdalPartyTest_RecordStatus` | String |  |  |
| 53 | `SE.MD.CURR.NO` | `SeMdalPartyTest_CurrNo` | String |  |  |
| 54 | `SE.MD.INPUTTER` | `SeMdalPartyTest_Inputter` |  |  |  |
| 55 | `SE.MD.DATE.TIME` | `SeMdalPartyTest_DateTime` |  |  |  |
| 56 | `SE.MD.AUTHORISER` | `SeMdalPartyTest_Authoriser` | String |  |  |
| 57 | `SE.MD.CO.CODE` | `SeMdalPartyTest_CoCode` | String |  |  |
| 58 | `SE.MD.DEPT.CODE` | `SeMdalPartyTest_DeptCode` | String |  |  |
| 59 | `SE.MD.AUDITOR.CODE` | `SeMdalPartyTest_AuditorCode` | String |  |  |
| 60 | `SE.MD.AUDIT.DATE.TIME` | `SeMdalPartyTest_AuditDateTime` | String |  |  |
