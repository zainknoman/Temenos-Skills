# ITREGE.TXN.REPORT.PARAM — Table Schema

> Source: `INSERTS/I_F.ITREGE.TXN.REPORT.PARAM` in `ITREGE_Transactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.TXN.PARAM.THRESHOLD.AMOUNT` | `ItregeTxnReportParam_ThresholdAmount` | TField |  |  |
| 2 | `ITREGE.TXN.PARAM.BANK.CODE` | `ItregeTxnReportParam_BankCode` | TField |  | Bank Code has to be configured in this field. This field supports alphanumeric characters. |
| 3 | `ITREGE.TXN.PARAM.INFORMATION.TYPE` | `ItregeTxnReportParam_InformationType` | TField |  | This field accepts 2 Values as input.1. O - Operations2. R - Relationship |
| 4 | `ITREGE.TXN.PARAM.PRODUCT.TO.EXCLUDE` | `ItregeTxnReportParam_ProductToExclude` |  |  |  |
| 5 | `ITREGE.TXN.PARAM.ORIGIN.PROCEDURE.CODE` | `ItregeTxnReportParam_OriginProcedureCode` | TField |  | This field holds the value of Originator code where the transaction originates. e.g 'T24' |
| 6 | `ITREGE.TXN.PARAM.CURRENCY.CODE.FORMAT` | `ItregeTxnReportParam_CurrencyCodeFormat` | TField |  | Currency Code format has to be configured in this application. e.g 'UIC' |
| 7 | `ITREGE.TXN.PARAM.COUNTRY.CODE.FORMAT` | `ItregeTxnReportParam_CountryCodeFormat` | TField |  | Country Code format has be configured in this application. eg. 'UIC' |
| 8 | `ITREGE.TXN.PARAM.AMOUNT.FLAG` | `ItregeTxnReportParam_AmountFlag` | TField |  | Amount in the report can be shown in the currency configured in this field. This fields accepts 2 Values as input.1. Euro2. Lire |
| 9 | `ITREGE.TXN.PARAM.ALT.ACCT.TYPE` | `ItregeTxnReportParam_AltAcctType` | TField |  | Alternative Account Type can be configured here. eg 'T24.IBAN' |
| 10 | `ITREGE.TXN.PARAM.INDIVIDUAL.SECTOR` | `ItregeTxnReportParam_IndividualSector` |  |  |  |
| 11 | `ITREGE.TXN.PARAM.LEGAL.SECTOR` | `ItregeTxnReportParam_LegalSector` |  |  |  |
| 12 | `ITREGE.TXN.PARAM.RELATION.TYPE` | `ItregeTxnReportParam_RelationType` |  |  |  |
| 13 | `ITREGE.TXN.PARAM.RELATION.CODE` | `ItregeTxnReportParam_RelationCode` |  |  |  |
| 14 | `ITREGE.TXN.PARAM.RELATIONSHIP.TYPE` | `ItregeTxnReportParam_RelationshipType` |  |  |  |
| 15 | `ITREGE.TXN.PARAM.PRODUCT` | `ItregeTxnReportParam_Product` |  |  |  |
| 16 | `ITREGE.TXN.PARAM.DFE.ID.REC.A` | `ItregeTxnReportParam_DfeIdRecA` | TField |  | DFE Mapping/Parameter ID name for Record Type A has to be configured here |
| 17 | `ITREGE.TXN.PARAM.DFE.ID.REC.E` | `ItregeTxnReportParam_DfeIdRecE` | TField |  | DFE Mapping/Parameter ID name for Record Type E has to be configured here |
| 18 | `ITREGE.TXN.PARAM.DFE.ID.REC.F` | `ItregeTxnReportParam_DfeIdRecF` | TField |  | DFE Mapping/Parameter ID name for Record Type F has to be configured here |
| 19 | `ITREGE.TXN.PARAM.FLOW.SENDING.NUMBER` | `ItregeTxnReportParam_FlowSendingNumber` | TField |  | This field shows the number of times the report has sent on a particular day. |
| 20 | `ITREGE.TXN.PARAM.CURRENCY` | `ItregeTxnReportParam_Currency` |  |  |  |
| 21 | `ITREGE.TXN.PARAM.UIC.CURRENCY.CODE` | `ItregeTxnReportParam_UicCurrencyCode` |  |  |  |
| 22 | `ITREGE.TXN.PARAM.INTERMEDIARY.TYPE` | `ItregeTxnReportParam_IntermediaryType` |  |  |  |
| 23 | `ITREGE.TXN.PARAM.ABI.CODE` | `ItregeTxnReportParam_AbiCode` |  |  |  |
| 24 | `ITREGE.TXN.PARAM.TAX.CODE` | `ItregeTxnReportParam_TaxCode` |  |  |  |
| 25 | `ITREGE.TXN.PARAM.RESERVED.3` | `ItregeTxnReportParam_Reserved3` | TField |  |  |
| 26 | `ITREGE.TXN.PARAM.RESERVED.2` | `ItregeTxnReportParam_Reserved2` | TField |  |  |
| 27 | `ITREGE.TXN.PARAM.RESERVED.1` | `ItregeTxnReportParam_Reserved1` | TField |  |  |
| 28 | `ITREGE.TXN.PARAM.LOCAL.REF` | `ItregeTxnReportParam_LocalRef` |  |  |  |
| 29 | `ITREGE.TXN.PARAM.OVERRIDE` | `ItregeTxnReportParam_Override` |  |  |  |
| 30 | `ITREGE.TXN.PARAM.RECORD.STATUS` | `ItregeTxnReportParam_RecordStatus` | String |  |  |
| 31 | `ITREGE.TXN.PARAM.CURR.NO` | `ItregeTxnReportParam_CurrNo` | String |  |  |
| 32 | `ITREGE.TXN.PARAM.INPUTTER` | `ItregeTxnReportParam_Inputter` |  |  |  |
| 33 | `ITREGE.TXN.PARAM.DATE.TIME` | `ItregeTxnReportParam_DateTime` |  |  |  |
| 34 | `ITREGE.TXN.PARAM.AUTHORISER` | `ItregeTxnReportParam_Authoriser` | String |  |  |
| 35 | `ITREGE.TXN.PARAM.CO.CODE` | `ItregeTxnReportParam_CoCode` | String |  |  |
| 36 | `ITREGE.TXN.PARAM.DEPT.CODE` | `ItregeTxnReportParam_DeptCode` | String |  |  |
| 37 | `ITREGE.TXN.PARAM.AUDITOR.CODE` | `ItregeTxnReportParam_AuditorCode` | String |  |  |
| 38 | `ITREGE.TXN.PARAM.AUDIT.DATE.TIME` | `ItregeTxnReportParam_AuditDateTime` | String |  |  |
