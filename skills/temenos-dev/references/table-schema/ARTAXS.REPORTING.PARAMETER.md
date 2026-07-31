# ARTAXS.REPORTING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ARTAXS.REPORTING.PARAMETER` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARTAXS.REPORT.PARAM.LEGAL.DOC.PRIORITY` | `ArtaxsReportingParameter_LegalDocPriority` |  |  |  |
| 2 | `ARTAXS.REPORT.PARAM.CALC.BASE.CURRENCY.MARKET` | `ArtaxsReportingParameter_CalcBaseCurrencyMarket` | TField |  | Currency market code to obtain the exchange rate to convert the transaction amount to local currency. |
| 3 | `ARTAXS.REPORT.PARAM.CALC.BASE.EXCHANGE.TYPE` | `ArtaxsReportingParameter_CalcBaseExchangeType` | TField |  | Exchange rate to convert the transaction amount to local currency. The possible values are: Buy, Mid, Sell. |
| 4 | `ARTAXS.REPORT.PARAM.TAX.CURRENCY.MARKET` | `ArtaxsReportingParameter_TaxCurrencyMarket` | TField |  | Currency market code to obtain the exchange rate to convert the tax amount to local currency. |
| 5 | `ARTAXS.REPORT.PARAM.TAX.EXCHANGE.TYPE` | `ArtaxsReportingParameter_TaxExchangeType` | TField |  | Exchange rate to convert the tax amount to local currency. The possible values are: Buy, Mid, Sell. |
| 6 | `ARTAXS.REPORT.PARAM.LOCAL.REF` | `ArtaxsReportingParameter_LocalRef` |  |  |  |
| 7 | `ARTAXS.REPORT.PARAM.OVERRIDE` | `ArtaxsReportingParameter_Override` |  |  |  |
| 8 | `ARTAXS.REPORT.PARAM.RECORD.STATUS` | `ArtaxsReportingParameter_RecordStatus` | String |  |  |
| 9 | `ARTAXS.REPORT.PARAM.CURR.NO` | `ArtaxsReportingParameter_CurrNo` | String |  |  |
| 10 | `ARTAXS.REPORT.PARAM.INPUTTER` | `ArtaxsReportingParameter_Inputter` |  |  |  |
| 11 | `ARTAXS.REPORT.PARAM.DATE.TIME` | `ArtaxsReportingParameter_DateTime` |  |  |  |
| 12 | `ARTAXS.REPORT.PARAM.AUTHORISER` | `ArtaxsReportingParameter_Authoriser` | String |  |  |
| 13 | `ARTAXS.REPORT.PARAM.CO.CODE` | `ArtaxsReportingParameter_CoCode` | String |  |  |
| 14 | `ARTAXS.REPORT.PARAM.DEPT.CODE` | `ArtaxsReportingParameter_DeptCode` | String |  |  |
| 15 | `ARTAXS.REPORT.PARAM.AUDITOR.CODE` | `ArtaxsReportingParameter_AuditorCode` | String |  |  |
| 16 | `ARTAXS.REPORT.PARAM.AUDIT.DATE.TIME` | `ArtaxsReportingParameter_AuditDateTime` | String |  |  |
