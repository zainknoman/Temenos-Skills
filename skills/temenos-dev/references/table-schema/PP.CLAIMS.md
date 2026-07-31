# PP.CLAIMS — Table Schema

> Source: `INSERTS/I_F.PP.CLAIMS` in `PP_ClaimsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CL.CompanyID` | `PpClaims_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.CL.ExpectedClaimAccountCompany` | `PpClaims_Expectedclaimaccountcompany` | TField |  | Holds 3 character company Code of expected claim account number. Validation Rules: Defaulted to the value set in field, 'CompanyCode' |
| 3 | `PP.CL.ExpectedClaimAccount` | `PpClaims_Expectedclaimaccount` | TField | Yes | Holds the Expected claim account number for a currency and company code combination. Validation Rules: Mandatory field. Value should be a valid account number as defined in ACCOUNT. |
| 4 | `PP.CL.ExpectedClaimAccountCurrency` | `PpClaims_Expectedclaimaccountcurrency` | TField |  | Holds 3 character currency code of expected claim account number. Validation Rules: Defaulted to the value set in field, 'CurrencyCode' |
| 5 | `PP.CL.ExpectedPLAccountCompany` | `PpClaims_Expectedplaccountcompany` | TField |  | Holds 3 character Company Code of expected P&amp;L account number. Validation Rules: Defaulted to the value set in field, 'CompanyCode' |
| 6 | `PP.CL.ExpectedPLAccount` | `PpClaims_Expectedplaccount` | TField |  | Holds the Expected P&amp;L account number for a currency and company code combination. Validation Rules: The value links to field,'CATEGORY.CODE' in CATEGORY. |
| 7 | `PP.CL.ExpectedPLAccountCurrency` | `PpClaims_Expectedplaccountcurrency` | TField |  | Holds 3 character currency code of expected P&amp;L account number. Validation Rules: Defaulted to the value set in field, 'CurrencyCode' |
| 8 | `PP.CL.PLAccountCompany` | `PpClaims_Placcountcompany` | TField |  | Holds 3 character company code of P&amp;L account number. Validation Rules: Defaulted to the value set in field, 'CompanyCode' |
| 9 | `PP.CL.PLAccount` | `PpClaims_Placcount` | TField | Yes | Holds Profit and Loss category code. Validation Rules: Mandatory field. 4 or 5 numeric characters. The value links to field, 'CATEGORY.CODE' in CATEGORY. |
| 10 | `PP.CL.PLAccountCurrency` | `PpClaims_Placcountcurrency` | TField |  | Holds 3 character currency code of P&amp;L account number. Validation Rules: Defaulted to the value set in field, 'CurrencyCode' |
| 11 | `PP.CL.RESERVED.5` | `PpClaims_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 12 | `PP.CL.RESERVED.4` | `PpClaims_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 13 | `PP.CL.RESERVED.3` | `PpClaims_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 14 | `PP.CL.RESERVED.2` | `PpClaims_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 15 | `PP.CL.RESERVED.1` | `PpClaims_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 16 | `PP.CL.LOCAL.REF` | `PpClaims_LocalRef` |  |  |  |
| 17 | `PP.CL.OVERRIDE` | `PpClaims_Override` |  |  |  |
| 18 | `PP.CL.RECORD.STATUS` | `PpClaims_RecordStatus` | String |  |  |
| 19 | `PP.CL.CURR.NO` | `PpClaims_CurrNo` | String |  |  |
| 20 | `PP.CL.INPUTTER` | `PpClaims_Inputter` |  |  |  |
| 21 | `PP.CL.DATE.TIME` | `PpClaims_DateTime` |  |  |  |
| 22 | `PP.CL.AUTHORISER` | `PpClaims_Authoriser` | String |  |  |
| 23 | `PP.CL.CO.CODE` | `PpClaims_CoCode` | String |  |  |
| 24 | `PP.CL.DEPT.CODE` | `PpClaims_DeptCode` | String |  |  |
| 25 | `PP.CL.AUDITOR.CODE` | `PpClaims_AuditorCode` | String |  |  |
| 26 | `PP.CL.AUDIT.DATE.TIME` | `PpClaims_AuditDateTime` | String |  |  |
