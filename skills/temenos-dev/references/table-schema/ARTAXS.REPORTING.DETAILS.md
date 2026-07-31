# ARTAXS.REPORTING.DETAILS — Table Schema

> Source: `INSERTS/I_F.ARTAXS.REPORTING.DETAILS` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARTAXS.REPORT.DET.TRANSACTION.DATE` | `ArtaxsReportingDetails_TransactionDate` | TField |  | Date on which the transaction is executed. |
| 2 | `ARTAXS.REPORT.DET.ARRANGEMENT.ID` | `ArtaxsReportingDetails_ArrangementId` | TField |  | Id of the arrangement on which the tax is applied. |
| 3 | `ARTAXS.REPORT.DET.EXEMPTION.PARAMETER.ID` | `ArtaxsReportingDetails_ExemptionParameterId` | TField |  | Id of the record in ARTAXS.EXEMPTION.PARAMETER that was applied. |
| 4 | `ARTAXS.REPORT.DET.JURISDICTION` | `ArtaxsReportingDetails_Jurisdiction` | TField |  | Jurisdiction in the id of the exemption record configured in ARTAXS.EXEMPTION.PARAMETER. Possible values are: - Jurisdiction code given in the EB.LOOKUP>PROVINCE - The word ALL to identify the configuration applies for all the jurisdictions. - Jurisdiction Code field in SIRCREB padron. It is a code of 2 or 3 numbers including 00 and 000. |
| 5 | `ARTAXS.REPORT.DET.EXEMPT.PARAM.ACTIVITY` | `ArtaxsReportingDetails_ExemptParamActivity` | TField |  | Id of the activity configured in the exemption record in ARTAXS.EXEMPTION.PARAMETER. |
| 6 | `ARTAXS.REPORT.DET.EXEMPT.PARAM.ACTIVITY.CLASS` | `ArtaxsReportingDetails_ExemptParamActivityClass` | TField |  | Id of the activity class configured in the exemption record in ARTAXS.EXEMPTION.PARAMETER. |
| 7 | `ARTAXS.REPORT.DET.TRANSACTION.AAA.REF` | `ArtaxsReportingDetails_TransactionAaaRef` | TField |  | AA.ARRANGEMENT.ACTIVITY reference Id that triggered the activity to apply the tax on the transaction execution date. |
| 8 | `ARTAXS.REPORT.DET.TRANSACTION.ACTIVITY` | `ArtaxsReportingDetails_TransactionActivity` | TField |  | Id of the activity executed to apply the tax. This activity could be different due to the mapping. |
| 9 | `ARTAXS.REPORT.DET.TRANSACTION.TAX.PROPERTY` | `ArtaxsReportingDetails_TransactionTaxProperty` | TField |  | Id of the tax property for the tax applied.This property could be different due to the mapping. |
| 10 | `ARTAXS.REPORT.DET.TRANSACTION.PRODUCT.ID` | `ArtaxsReportingDetails_TransactionProductId` | TField |  | Id of the product on which the tax applies. This product Id could be different due to the mapping. |
| 11 | `ARTAXS.REPORT.DET.CBU` | `ArtaxsReportingDetails_Cbu` | TField |  | CBU of the account where the tax is applied. This field will be stored for savings and current accounts. |
| 12 | `ARTAXS.REPORT.DET.CUSTOMER.ID` | `ArtaxsReportingDetails_CustomerId` |  |  |  |
| 13 | `ARTAXS.REPORT.DET.LEGAL.ID` | `ArtaxsReportingDetails_LegalId` |  |  |  |
| 14 | `ARTAXS.REPORT.DET.LEGAL.DOC.NAME` | `ArtaxsReportingDetails_LegalDocName` |  |  |  |
| 15 | `ARTAXS.REPORT.DET.SIRCREB.CRC` | `ArtaxsReportingDetails_SircrebCrc` |  |  |  |
| 16 | `ARTAXS.REPORT.DET.CALC.BASE.AMOUNT` | `ArtaxsReportingDetails_CalcBaseAmount` | TField |  | Calculation base amount. This calculation base will depend on the tax and it is configured in ARTAXS.EXEMPTION.PARAMETER. |
| 17 | `ARTAXS.REPORT.DET.CALC.BASE.CURRENCY` | `ArtaxsReportingDetails_CalcBaseCurrency` | TField |  | Currency of the calculation base amount. |
| 18 | `ARTAXS.REPORT.DET.CALC.BASE.EXCHANGE.TYPE` | `ArtaxsReportingDetails_CalcBaseExchangeType` | TField |  | Exchange rate used to convert the calculation base amount to local currency. It corresponds to the exchange type configured for the calculation base in ARTAXS.EXCHANGE.PARAMETER for the tax type used. This field has to be filled up when CALC.BASE.CURRENCY is a foreign currency. |
| 19 | `ARTAXS.REPORT.DET.CALC.BASE.CURRENCY.MARKET` | `ArtaxsReportingDetails_CalcBaseCurrencyMarket` | TField |  | Currency market of the exchange rate used to convert the calculation base amount. It corresponds to the currency market configured for the calculation base in ARTAXS.EXCHANGE.PARAMETER for the tax type used. This field has to be filled up when CALC.BASE.CURRENCY is a foreign currency. |
| 20 | `ARTAXS.REPORT.DET.CALC.BASE.EXCHANGE.RATE` | `ArtaxsReportingDetails_CalcBaseExchangeRate` | TField |  | Exchange rate used to convert a foreign currency to local currency. It is based on the CALC.BASE.EXCHANGE.TYPE and CALC.BASE.CURRENCY.MARKET. This field has to be filled up when CALC.BASE.CURRENCY is a foreign currency. |
| 21 | `ARTAXS.REPORT.DET.TAX.AMOUNT` | `ArtaxsReportingDetails_TaxAmount` | TField |  | Tax amount calculated. This value will be stored either the tax is applied or exempted. |
| 22 | `ARTAXS.REPORT.DET.TAX.CURRENCY` | `ArtaxsReportingDetails_TaxCurrency` | TField |  | Currency of the tax amount. |
| 23 | `ARTAXS.REPORT.DET.TAX.EXCHANGE.TYPE` | `ArtaxsReportingDetails_TaxExchangeType` | TField |  | Exchange type used to convert the tax amount to local currency. It corresponds to the exchange type configured for the tax in ARTAXS.EXCHANGE.PARAMETER for the tax type used. This field has to be filled up when TAX.CURRENCY is a foreign currency. |
| 24 | `ARTAXS.REPORT.DET.TAX.CURRENCY.MARKET` | `ArtaxsReportingDetails_TaxCurrencyMarket` | TField |  | Currency market of the Exchange rate used to convert the tax amount. It corresponds to the currency market configured for the tax in ARTAXS.EXCHANGE.PARAMETER for the tax type used. This field has to be filled up when TAX.CURRENCY is a foreign currency. |
| 25 | `ARTAXS.REPORT.DET.TAX.EXCHANGE.RATE` | `ArtaxsReportingDetails_TaxExchangeRate` | TField |  | Exchange rate used to convert a foreign currency to local currency. It is based on the TAX.EXCHANGE.TYPE and TAX.EXCHANGE.CURRENCY.MARKET. This field has to be filled up when TAX.CURRENCY is a foreign currency. |
| 26 | `ARTAXS.REPORT.DET.EXEMPTION.FLAG` | `ArtaxsReportingDetails_ExemptionFlag` | TField |  | Flag to identify if any exemption is applied. This field will allow the user to identify if an exemption is applied no matter if this exemption has configured an exemption code or not. Possible values are: YES = Tax application is exempted NULL = Tax is applied |
| 27 | `ARTAXS.REPORT.DET.EXEMPTION.CODE` | `ArtaxsReportingDetails_ExemptionCode` | TField |  | Exemption code applied when the tax is not collected. |
| 28 | `ARTAXS.REPORT.DET.ACCOUNT.TYPE` | `ArtaxsReportingDetails_AccountType` | TField |  | Account Type for Turnover Tax Report |
| 29 | `ARTAXS.REPORT.DET.REGISTER.TYPE` | `ArtaxsReportingDetails_RegisterType` | TField |  | Register Type for Turnover Tax Report |
