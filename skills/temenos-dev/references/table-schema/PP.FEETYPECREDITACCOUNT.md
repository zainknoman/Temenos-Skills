# PP.FEETYPECREDITACCOUNT — Table Schema

> Source: `INSERTS/I_F.PP.FEETYPECREDITACCOUNT` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.FEC.CompanyID` | `PpFeetypecreditaccount_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.FEC.CRAccountCompanyID` | `PpFeetypecreditaccount_Craccountcompanyid` | TField |  | Indicates the company ID of the credit account which is linked to the fee type. The value is same as the value to field, 'CompanyID'. Validation Rules: No input field. |
| 3 | `PP.FEC.CRAccount` | `PpFeetypecreditaccount_Craccount` | TField |  | Indicates the credit account linked to the fee type. Validation Rules: 35 characters of type 'ACCA'. |
| 4 | `PP.FEC.CRAccountCurrency` | `PpFeetypecreditaccount_Craccountcurrency` | TField | Yes | Indicates the currency code of the credit account which is linked to the fee type. Validation Rules: Mandatory field. 3 alphanumeric characters. The value links to field 'CurrencyCode' in PP.CURRENCY. |
| 5 | `PP.FEC.CRAccountType` | `PpFeetypecreditaccount_Craccounttype` | TField | Yes | Indicates the type of the credit account which is linked to the fee type. Possible values: PL - Profile and Loss account Vostro - Vostro account Nostro - Nostro account Suspense - Internal suspense account Validation Rules: Mandatory field. A value can be defined only from the possible values as mentioned. |
| 6 | `PP.FEC.RESERVED.5` | `PpFeetypecreditaccount_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.FEC.RESERVED.4` | `PpFeetypecreditaccount_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.FEC.RESERVED.3` | `PpFeetypecreditaccount_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.FEC.RESERVED.2` | `PpFeetypecreditaccount_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.FEC.RESERVED.1` | `PpFeetypecreditaccount_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 11 | `PP.FEC.LOCAL.REF` | `PpFeetypecreditaccount_LocalRef` |  |  |  |
| 12 | `PP.FEC.OVERRIDE` | `PpFeetypecreditaccount_Override` |  |  |  |
| 13 | `PP.FEC.RECORD.STATUS` | `PpFeetypecreditaccount_RecordStatus` | String |  |  |
| 14 | `PP.FEC.CURR.NO` | `PpFeetypecreditaccount_CurrNo` | String |  |  |
| 15 | `PP.FEC.INPUTTER` | `PpFeetypecreditaccount_Inputter` |  |  |  |
| 16 | `PP.FEC.DATE.TIME` | `PpFeetypecreditaccount_DateTime` |  |  |  |
| 17 | `PP.FEC.AUTHORISER` | `PpFeetypecreditaccount_Authoriser` | String |  |  |
| 18 | `PP.FEC.CO.CODE` | `PpFeetypecreditaccount_CoCode` | String |  |  |
| 19 | `PP.FEC.DEPT.CODE` | `PpFeetypecreditaccount_DeptCode` | String |  |  |
| 20 | `PP.FEC.AUDITOR.CODE` | `PpFeetypecreditaccount_AuditorCode` | String |  |  |
| 21 | `PP.FEC.AUDIT.DATE.TIME` | `PpFeetypecreditaccount_AuditDateTime` | String |  |  |
