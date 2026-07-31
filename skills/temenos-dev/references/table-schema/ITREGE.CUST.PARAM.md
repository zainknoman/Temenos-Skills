# ITREGE.CUST.PARAM — Table Schema

> Source: `INSERTS/I_F.ITREGE.CUST.PARAM` in `ITREGE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUST.PARAM.HEADER` | `ItregeCustParam_Header` | TField |  | The numeric number to be displayed in field for header |
| 2 | `CUST.PARAM.BODY` | `ItregeCustParam_Body` | TField |  | The numeric number to be displayed in field for body |
| 3 | `CUST.PARAM.FOOTER` | `ItregeCustParam_Footer` | TField |  | The numeric number to be displayed in field for footer |
| 4 | `CUST.PARAM.SUPPLY.CODE` | `ItregeCustParam_SupplyCode` | TField |  | The supply code to be defined in the file |
| 5 | `CUST.PARAM.INSTITUTION.CODE` | `ItregeCustParam_InstitutionCode` | TField |  |  |
| 6 | `CUST.PARAM.FORMAT.CODE` | `ItregeCustParam_FormatCode` | TField |  | The format code to be displayed for country code, sector code etc. |
| 7 | `CUST.PARAM.INDIVIDUAL.SECTOR` | `ItregeCustParam_IndividualSector` |  |  |  |
| 8 | `CUST.PARAM.LEGAL.SECTOR` | `ItregeCustParam_LegalSector` |  |  |  |
| 9 | `CUST.PARAM.OPERATOR.CODE` | `ItregeCustParam_OperatorCode` | TField |  | The operator sector to be populated which is unique from the source provider |
| 10 | `CUST.PARAM.DATA.SOURCE.CODE` | `ItregeCustParam_DataSourceCode` | TField |  | The data source to be populated which is unique from the source provider |
| 11 | `CUST.PARAM.EUROPE.COUNTRY.GROUP` | `ItregeCustParam_EuropeCountryGroup` | TField |  | Vetted to COUNTRY.GROUP application |
| 12 | `CUST.PARAM.FATCA.COUNTRY` | `ItregeCustParam_FatcaCountry` |  |  |  |
| 13 | `CUST.PARAM.ROLE.TYPE` | `ItregeCustParam_RoleType` |  |  |  |
| 14 | `CUST.PARAM.CUSTOMER.ROLE` | `ItregeCustParam_CustomerRole` |  |  |  |
| 15 | `CUST.PARAM.APPLICATION` | `ItregeCustParam_Application` |  |  |  |
| 16 | `CUST.PARAM.APPLICATION.FIELD` | `ItregeCustParam_ApplicationField` |  |  |  |
| 17 | `CUST.PARAM.POLITICALLY.EXPOSED` | `ItregeCustParam_PoliticallyExposed` |  |  |  |
| 18 | `CUST.PARAM.TRAP.CODE` | `ItregeCustParam_TrapCode` |  |  |  |
| 19 | `CUST.PARAM.PRODUCT.NAME` | `ItregeCustParam_ProductName` |  |  |  |
| 20 | `CUST.PARAM.ALT.ACCOUNT.TYPE` | `ItregeCustParam_AltAccountType` | TField |  | The alternate ID to be taken for IBAN number |
| 21 | `CUST.PARAM.INDUSTRY.CODE` | `ItregeCustParam_IndustryCode` | TField |  |  |
| 22 | `CUST.PARAM.PROPOSED.INDUSTRY.CODE` | `ItregeCustParam_ProposedIndustryCode` | TField |  |  |
| 23 | `CUST.PARAM.CURRENCY` | `ItregeCustParam_Currency` |  |  |  |
| 24 | `CUST.PARAM.CURRENCY.CODE` | `ItregeCustParam_CurrencyCode` |  |  |  |
| 25 | `CUST.PARAM.MINOR.ROLE.TYPE` | `ItregeCustParam_MinorRoleType` |  |  |  |
| 26 | `CUST.PARAM.ELIGIBLE.RELATION.CODE` | `ItregeCustParam_EligibleRelationCode` |  |  |  |
| 27 | `CUST.PARAM.PREPAID.PRODUCT` | `ItregeCustParam_PrepaidProduct` |  |  |  |
| 28 | `CUST.PARAM.MINOR.AGE.LIMIT` | `ItregeCustParam_MinorAgeLimit` | TField |  | The age limit for minor customers |
| 29 | `CUST.PARAM.CARD.ISSUE.STATUS` | `ItregeCustParam_CardIssueStatus` |  |  |  |
| 30 | `CUST.PARAM.CARD.CLOSE.STATUS` | `ItregeCustParam_CardCloseStatus` |  |  |  |
| 31 | `CUST.PARAM.CUSTOMER.RELATION.CODE` | `ItregeCustParam_CustomerRelationCode` |  |  |  |
| 32 | `CUST.PARAM.OVERRIDE` | `ItregeCustParam_Override` |  |  |  |
| 33 | `CUST.PARAM.RECORD.STATUS` | `ItregeCustParam_RecordStatus` | String |  |  |
| 34 | `CUST.PARAM.CURR.NO` | `ItregeCustParam_CurrNo` | String |  |  |
| 35 | `CUST.PARAM.INPUTTER` | `ItregeCustParam_Inputter` |  |  |  |
| 36 | `CUST.PARAM.DATE.TIME` | `ItregeCustParam_DateTime` |  |  |  |
| 37 | `CUST.PARAM.AUTHORISER` | `ItregeCustParam_Authoriser` | String |  |  |
| 38 | `CUST.PARAM.CO.CODE` | `ItregeCustParam_CoCode` | String |  |  |
| 39 | `CUST.PARAM.DEPT.CODE` | `ItregeCustParam_DeptCode` | String |  |  |
| 40 | `CUST.PARAM.AUDITOR.CODE` | `ItregeCustParam_AuditorCode` | String |  |  |
| 41 | `CUST.PARAM.CARD.TYPE` | `ItregeCustParam_CardType` | TField |  | Card type of the customer like debit or credit card |
| 42 | `CUST.PARAM.LEGAL.NATURE` | `ItregeCustParam_LegalNature` | TField |  |  |
| 43 | `CUST.PARAM.LEGAL.REP` | `ItregeCustParam_LegalRep` | TField |  |  |
| 44 | `CUST.PARAM.AUDIT.DATE.TIME` | `ItregeCustParam_AuditDateTime` | String |  |  |
