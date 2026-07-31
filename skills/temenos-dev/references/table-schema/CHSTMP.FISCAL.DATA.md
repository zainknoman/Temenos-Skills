# CHSTMP.FISCAL.DATA — Table Schema

> Source: `INSERTS/I_F.CHSTMP.FISCAL.DATA` in `CHSTMP_SwissTaxStatement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FISCDATA.SEC.GROUP` | `ChstmpFiscalData_SecGroup` | TField |  | High level security Classification. Eg. Share/Bond. |
| 2 | `FISCDATA.SEC.TYPE` | `ChstmpFiscalData_SecType` | TField |  | Classification of the security.type. eg. Share Nominal, Fund accumulation and Fund Distribution. |
| 3 | `FISCDATA.CURRENCY` | `ChstmpFiscalData_Currency` | TField |  | Currency of the security. |
| 4 | `FISCDATA.NOMINAL.VALUE` | `ChstmpFiscalData_NominalValue` | TField |  | Nominal value of the security. |
| 5 | `FISCDATA.QUOTATION.TYPE` | `ChstmpFiscalData_QuotationType` | TField |  | Instrument price definition type. Eg. Piece. |
| 6 | `FISCDATA.TAX.VALUE.CHF` | `ChstmpFiscalData_TaxValueChf` | TField |  | Previous year price for a instrument in CHF value. |
| 7 | `FISCDATA.PAYMENT.ID` | `ChstmpFiscalData_PaymentId` |  |  |  |
| 8 | `FISCDATA.PAYMENT.DATE` | `ChstmpFiscalData_PaymentDate` |  |  |  |
| 9 | `FISCDATA.PAYMENT.VALUE` | `ChstmpFiscalData_PaymentValue` |  |  |  |
| 10 | `FISCDATA.EXCHANGE.RATE` | `ChstmpFiscalData_ExchangeRate` |  |  |  |
| 11 | `FISCDATA.PAYMENT.VALUE.CHF` | `ChstmpFiscalData_PaymentValueChf` |  |  |  |
| 12 | `FISCDATA.EX.DATE` | `ChstmpFiscalData_ExDate` |  |  |  |
| 13 | `FISCDATA.CAPITAL.GAIN` | `ChstmpFiscalData_CapitalGain` |  |  |  |
| 14 | `FISCDATA.RESERVED.5` | `ChstmpFiscalData_Reserved5` |  |  |  |
| 15 | `FISCDATA.RESERVED.4` | `ChstmpFiscalData_Reserved4` | TField |  |  |
| 16 | `FISCDATA.RESERVED.3` | `ChstmpFiscalData_Reserved3` | TField |  |  |
| 17 | `FISCDATA.RESERVED.2` | `ChstmpFiscalData_Reserved2` | TField |  |  |
| 18 | `FISCDATA.RESERVED.1` | `ChstmpFiscalData_Reserved1` | TField |  |  |
| 19 | `FISCDATA.LOCAL.REF` | `ChstmpFiscalData_LocalRef` |  |  |  |
| 20 | `FISCDATA.OVERRIDE` | `ChstmpFiscalData_Override` |  |  |  |
| 21 | `FISCDATA.RECORD.STATUS` | `ChstmpFiscalData_RecordStatus` | String |  |  |
| 22 | `FISCDATA.CURR.NO` | `ChstmpFiscalData_CurrNo` | String |  |  |
| 23 | `FISCDATA.INPUTTER` | `ChstmpFiscalData_Inputter` |  |  |  |
| 24 | `FISCDATA.DATE.TIME` | `ChstmpFiscalData_DateTime` |  |  |  |
| 25 | `FISCDATA.AUTHORISER` | `ChstmpFiscalData_Authoriser` | String |  |  |
| 26 | `FISCDATA.CO.CODE` | `ChstmpFiscalData_CoCode` | String |  |  |
| 27 | `FISCDATA.DEPT.CODE` | `ChstmpFiscalData_DeptCode` | String |  |  |
| 28 | `FISCDATA.AUDITOR.CODE` | `ChstmpFiscalData_AuditorCode` | String |  |  |
| 29 | `FISCDATA.AUDIT.DATE.TIME` | `ChstmpFiscalData_AuditDateTime` | String |  |  |
