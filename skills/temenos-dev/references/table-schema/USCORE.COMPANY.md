# USCORE.COMPANY — Table Schema

> Source: `INSERTS/I_F.USCORE.COMPANY` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COMP.DET.TAX.ID` | `UscoreCompany_TaxId` | TField |  | This field is used to specify the Tax ID of the branch or lead company. Validation Rule: Alpha-numeric 1-10 digits |
| 2 | `COMP.DET.INCORP.CITY` | `UscoreCompany_IncorpCity` | TField |  | This field is used to specify the company's city of incorporation. Validation Rule: Alpha-numeric 1-30 digits |
| 3 | `COMP.DET.INCORP.COUNTY` | `UscoreCompany_IncorpCounty` | TField |  | This field is used to specify the company's county of incorporation. Validation Rule: Alpha-numeric 1-20 digits |
| 4 | `COMP.DET.INCORP.STATE` | `UscoreCompany_IncorpState` | TField |  | This field is used to specify the company's state of incorporation. Validation Rule: Alpha-numeric 1-2 digits |
| 5 | `COMP.DET.ZIP` | `UscoreCompany_Zip` | TField |  | This field is used to specify the ZIP code of the company's address. Validation Rule: Alpha-numeric 1-10 digits |
| 6 | `COMP.DET.ZIP4` | `UscoreCompany_Zip4` | TField |  | This field is used to specify the ZIP code of the company's address. Validation Rule: Alpha-numeric 1-10 digits |
| 7 | `COMP.DET.INCORP.DATE` | `UscoreCompany_IncorpDate` | TField |  | This field is used to specify the company's date of incorporation. Validation Rule: 11 digits valid date |
| 8 | `COMP.DET.NAICS.CODE` | `UscoreCompany_NaicsCode` | TField |  | This field is used to parameterize the NAICS code. Validation Rule: Numeric 1-6 digits |
| 9 | `COMP.DET.FAX` | `UscoreCompany_Fax` | TField |  | This field is used to define the FAX number of the company. Validation Rule: Numeric 1-10 digits, Consist of 3 digit area code and 7 digit FAX number. |
| 10 | `COMP.DET.PHONE.NO` | `UscoreCompany_PhoneNo` | TField |  |  |
| 11 | `COMP.DET.BANK.NUMBER` | `UscoreCompany_BankNumber` | TField |  |  |
| 12 | `COMP.DET.FDIC.CERTIFICATE.NO` | `UscoreCompany_FdicCertificateNo` | TField |  |  |
| 13 | `COMP.DET.ADDRESS.LINE.1` | `UscoreCompany_AddressLine1` | TField |  |  |
| 14 | `COMP.DET.ADDRESS.LINE.2` | `UscoreCompany_AddressLine2` | TField |  |  |
| 15 | `COMP.DET.ROUTING.NUMBER` | `UscoreCompany_Reserved20` |  |  |  |
| 16 | `COMP.DET.COUNTRY` | `UscoreCompany_Country` | TField |  | Country where the branch is located. |
| 17 | `COMP.DET.BRANCH.NAME` | `UscoreCompany_BranchName` | TField |  | Captures the name of the branch. |
| 18 | `COMP.DET.WEBSITE` | `UscoreCompany_BranchWeb` |  |  |  |
| 19 | `COMP.DET.RESERVED.16` | `UscoreCompany_Reserved16` | TField |  |  |
| 20 | `COMP.DET.RESERVED.15` | `UscoreCompany_Reserved15` | TField |  |  |
| 21 | `COMP.DET.RESERVED.14` | `UscoreCompany_Reserved14` | TField |  |  |
| 22 | `COMP.DET.RESERVED.13` | `UscoreCompany_Reserved13` | TField |  |  |
| 23 | `COMP.DET.RESERVED.12` | `UscoreCompany_Reserved12` | TField |  |  |
| 24 | `COMP.DET.RESERVED.11` | `UscoreCompany_Reserved11` | TField |  |  |
| 25 | `COMP.DET.RESERVED.10` | `UscoreCompany_Reserved10` | TField |  |  |
| 26 | `COMP.DET.RESERVED.9` | `UscoreCompany_Reserved9` | TField |  |  |
| 27 | `COMP.DET.RESERVED.8` | `UscoreCompany_Reserved8` | TField |  |  |
| 28 | `COMP.DET.RESERVED.7` | `UscoreCompany_Reserved7` | TField |  |  |
| 29 | `COMP.DET.RESERVED.6` | `UscoreCompany_Reserved6` | TField |  |  |
| 30 | `COMP.DET.RESERVED.5` | `UscoreCompany_Reserved5` | TField |  |  |
| 31 | `COMP.DET.RESERVED.4` | `UscoreCompany_Reserved4` | TField |  |  |
| 32 | `COMP.DET.RESERVED.3` | `UscoreCompany_Reserved3` | TField |  |  |
| 33 | `COMP.DET.RESERVED.2` | `UscoreCompany_Reserved2` | TField |  |  |
| 34 | `COMP.DET.RESERVED.1` | `UscoreCompany_Reserved1` | TField |  |  |
| 35 | `COMP.DET.LOCAL.REF` | `UscoreCompany_LocalRef` |  |  |  |
| 36 | `COMP.DET.RECORD.STATUS` | `UscoreCompany_RecordStatus` | String |  |  |
| 37 | `COMP.DET.CURR.NO` | `UscoreCompany_CurrNo` | String |  |  |
| 38 | `COMP.DET.INPUTTER` | `UscoreCompany_Inputter` |  |  |  |
| 39 | `COMP.DET.DATE.TIME` | `UscoreCompany_DateTime` |  |  |  |
| 40 | `COMP.DET.AUTHORISER` | `UscoreCompany_Authoriser` | String |  |  |
| 41 | `COMP.DET.CO.CODE` | `UscoreCompany_CoCode` | String |  |  |
| 42 | `COMP.DET.DEPT.CODE` | `UscoreCompany_DeptCode` | String |  |  |
| 43 | `COMP.DET.AUDITOR.CODE` | `UscoreCompany_AuditorCode` | String |  |  |
| 44 | `COMP.DET.AUDIT.DATE.TIME` | `UscoreCompany_AuditDateTime` | String |  |  |
