# PP.CURRENCY — Table Schema

> Source: `INSERTS/I_F.PP.CURRENCY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.CCY.CompanyID` | `PpCurrency_Companyid` | TField |  | Indicates the FTD company ID for which the record is created. It is NOINPUT field. On click of validate button, Company ID gets autopopulated from FTD Company. Examples: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PP.CCY.CountryCode` | `PpCurrency_Countrycode` | TField |  | Holds a 2 character unique code which specifies the country code. Validation Rules: The entry should be an existing record in COUNTRY |
| 3 | `PP.CCY.CurrencyGroup` | `PpCurrency_Currencygroup` | TField | No | Specific the group under which the currency should be grouped together. Validation Rules: This is an optional field. |
| 4 | `PP.CCY.CurrencyName` | `PpCurrency_Currencyname` | TField | Yes | Mentions the name of the currency in free text. Example: US Dollars, Indian Rupees Validation Rules: Mandatory field. This field can hold upto 35 alphanumeric characters as a value. |
| 5 | `PP.CCY.FractionalDigit` | `PpCurrency_Fractionaldigit` | TField | Yes | Indicates the fractional digit for the currency for principal amount and taxes if Chargefractionaldigit is defined. If chargefractionaldigit is blank then this field will hold the fractional digits for principal amount, taxes and charge. Example: Japanese yen has 0 decimals, USD has 2 decimals and Kuwaiti dinar has 3 decimals. Validation Rules: Mandatory field. The value can range from 0 to 9 only. |
| 6 | `PP.CCY.CountryName` | `PpCurrency_Countryname` | TField | No | Name of the country to which a currency belongs. In only exceptional cases such as the currency being EUR, a currency may have more than one country. Validation Rules: This is an optional field. |
| 7 | `PP.CCY.FXLimit` | `PpCurrency_Fxlimit` | TField | Yes | Specifies the limit in the foreign currency upto which a payment can be processed STP. When any currency undergoes a FOREX conversion, the converted value will be checked against the value to this field in order to determine if the payment can be processed as STP. If the converted value has exceeded this limit, the payment is marked as 'Non-STP' by the payments hub. Validation Rules: Mandatory field. This field can hold upto 17 numeric characters as a value. |
| 8 | `PP.CCY.WeekendDay1` | `PpCurrency_Weekendday1` | TField |  | Specifies the first one-working day in a week. Eg Saturday. Western countries observe Saturday as the first weekend where else many Middle-east countries observe Friday as the first weekend. Possible values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| 9 | `PP.CCY.WeekendDay2` | `PpCurrency_Weekendday2` | TField |  | Specifies the second one-working day in a week. Eg Sunday. Western countries observe Sunday as the second weekend where else many Middle-east countries observe Saturday as the second weekend. Possible values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| 10 | `PP.CCY.OverrideThroughUpload` | `PpCurrency_Overridethroughupload` | TField |  | Indicates if currency record can be updated from an automated upload process. Possible values: Y - The entry is manually updated and can be overridden by the upload process. N � The entry is manual updated and the upload process should not override it. Validation Rules: User can edit the content of this field with possible values only. |
| 11 | `PP.CCY.ExoticCurrency` | `PpCurrency_Exoticcurrency` | TField |  | A currency can be defined as an exotic currency by setting this field to 'Y' Possible values are : Y, N, Blank If the field is set to N or blank then the currency is a non exotic currency An exotic currency is a thinly traded currency in a country and hence banks will not have correspondents in that currency to process payments By defining a currency as an exotic currency, system will allow payments to be routed to a correspondent based on the debit currency (Usually it is based on transaction currency) Example : A payment debiting customer in EUR and with transaction currency RSD (Defined as exotic) will enable payment to be routed to a EUR correspondent bank |
| 12 | `PP.CCY.ChargeFractionalDigit` | `PpCurrency_Chargefractionaldigit` | TField | No | Indicates the fractional digit for charge amount only Example: Japanese yen has 0 decimals, USD has 2 decimals and Kuwaiti dinar has 3 decimals. Validation Rules: Optional field. The value can range from 0 to 9 only. |
| 13 | `PP.CCY.RESERVED.3` | `PpCurrency_Reserved3` | TField |  | Standard T24 String. No Input Field |
| 14 | `PP.CCY.RESERVED.2` | `PpCurrency_Reserved2` | TField |  | Standard T24 String. No Input Field |
| 15 | `PP.CCY.RESERVED.1` | `PpCurrency_Reserved1` | TField |  | Standard T24 String. No Input Field |
| 16 | `PP.CCY.LOCAL.REF` | `PpCurrency_LocalRef` |  |  |  |
| 17 | `PP.CCY.OVERRIDE` | `PpCurrency_Override` |  |  |  |
| 18 | `PP.CCY.RECORD.STATUS` | `PpCurrency_RecordStatus` | String |  |  |
| 19 | `PP.CCY.CURR.NO` | `PpCurrency_CurrNo` | String |  |  |
| 20 | `PP.CCY.INPUTTER` | `PpCurrency_Inputter` |  |  |  |
| 21 | `PP.CCY.DATE.TIME` | `PpCurrency_DateTime` |  |  |  |
| 22 | `PP.CCY.AUTHORISER` | `PpCurrency_Authoriser` | String |  |  |
| 23 | `PP.CCY.CO.CODE` | `PpCurrency_CoCode` | String |  |  |
| 24 | `PP.CCY.DEPT.CODE` | `PpCurrency_DeptCode` | String |  |  |
| 25 | `PP.CCY.AUDITOR.CODE` | `PpCurrency_AuditorCode` | String |  |  |
| 26 | `PP.CCY.AUDIT.DATE.TIME` | `PpCurrency_AuditDateTime` | String |  |  |
