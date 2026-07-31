# PP.INSUFFOUTB.OUR.CHARGE — Table Schema

> Source: `INSERTS/I_F.PP.INSUFFOUTB.OUR.CHARGE` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.IOO.CompanyID` | `PpInsuffoutbOurCharge_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.IOO.AccountType` | `PpInsuffoutbOurCharge_Accounttype` | TField | Yes | Indicates the type of the account. Possible Values are 1) I - Internal Account 2) N - Nostro Account 3) PL - Profit &amp; Loss Account 4) C - Customer Account 5) V - Vostro Account Validation Rules: Mandatory Input. |
| 3 | `PP.IOO.AccountCompanyID` | `PpInsuffoutbOurCharge_Accountcompanyid` | TField |  | Specifies the company ID of the account number. Validation Rules: No Input Field. Defaulted from the Company ID |
| 4 | `PP.IOO.Account` | `PpInsuffoutbOurCharge_Account` | TField | Yes | Indicates the account number to be used to debit in case the sending bank has not sent sufficient funds. Validation Rules: Mandatory Input. Should be valid T24 Account. |
| 5 | `PP.IOO.AccountCurrency` | `PpInsuffoutbOurCharge_Accountcurrency` | TField |  | Specifies the currency of the account number. Validation Rules: No Input Field. Defaulted to Account Currency |
| 6 | `PP.IOO.RESERVED.5` | `PpInsuffoutbOurCharge_Reserved5` | TField |  | Standard T24 String. No Input Field |
| 7 | `PP.IOO.RESERVED.4` | `PpInsuffoutbOurCharge_Reserved4` | TField |  | Standard T24 String. No Input Field |
| 8 | `PP.IOO.RESERVED.3` | `PpInsuffoutbOurCharge_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 9 | `PP.IOO.RESERVED.2` | `PpInsuffoutbOurCharge_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 10 | `PP.IOO.RESERVED.1` | `PpInsuffoutbOurCharge_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 11 | `PP.IOO.LOCAL.REF` | `PpInsuffoutbOurCharge_LocalRef` |  |  |  |
| 12 | `PP.IOO.OVERRIDE` | `PpInsuffoutbOurCharge_Override` |  |  |  |
| 13 | `PP.IOO.RECORD.STATUS` | `PpInsuffoutbOurCharge_RecordStatus` | String |  |  |
| 14 | `PP.IOO.CURR.NO` | `PpInsuffoutbOurCharge_CurrNo` | String |  |  |
| 15 | `PP.IOO.INPUTTER` | `PpInsuffoutbOurCharge_Inputter` |  |  |  |
| 16 | `PP.IOO.DATE.TIME` | `PpInsuffoutbOurCharge_DateTime` |  |  |  |
| 17 | `PP.IOO.AUTHORISER` | `PpInsuffoutbOurCharge_Authoriser` | String |  |  |
| 18 | `PP.IOO.CO.CODE` | `PpInsuffoutbOurCharge_CoCode` | String |  |  |
| 19 | `PP.IOO.DEPT.CODE` | `PpInsuffoutbOurCharge_DeptCode` | String |  |  |
| 20 | `PP.IOO.AUDITOR.CODE` | `PpInsuffoutbOurCharge_AuditorCode` | String |  |  |
| 21 | `PP.IOO.AUDIT.DATE.TIME` | `PpInsuffoutbOurCharge_AuditDateTime` | String |  |  |
