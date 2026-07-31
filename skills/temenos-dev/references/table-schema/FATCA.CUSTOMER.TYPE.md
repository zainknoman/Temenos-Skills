# FATCA.CUSTOMER.TYPE — Table Schema

> Source: `INSERTS/I_F.FATCA.CUSTOMER.TYPE` in `FA_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.CT.DESCRIPTION` | `FatcaCustomerType_Description` | TField | Yes | Holds the descriptive information of the record. VALIDATION RULES: Any free text Mandatory field |
| 2 | `FA.CT.CUSTOMER.TYPE` | `FatcaCustomerType_CustomerType` | TField |  | Holds the type under which a customer is identified |
| 3 | `FA.CT.CUS.FIELD.NAME` | `FatcaCustomerType_CusFieldName` |  |  |  |
| 4 | `FA.CT.CUS.OPERATOR` | `FatcaCustomerType_CusOperator` |  |  |  |
| 5 | `FA.CT.CUS.FIELD.VALUE` | `FatcaCustomerType_CusFieldValue` |  |  |  |
| 6 | `FA.CT.RESERVED.07` | `FatcaCustomerType_Reserved07` | TField |  |  |
| 7 | `FA.CT.RESERVED.06` | `FatcaCustomerType_Reserved06` | TField |  |  |
| 8 | `FA.CT.RESERVED.05` | `FatcaCustomerType_Reserved05` | TField |  |  |
| 9 | `FA.CT.RESERVED.04` | `FatcaCustomerType_Reserved04` | TField |  |  |
| 10 | `FA.CT.RESERVED.03` | `FatcaCustomerType_Reserved03` | TField |  |  |
| 11 | `FA.CT.RESERVED.02` | `FatcaCustomerType_Reserved02` | TField |  |  |
| 12 | `FA.CT.RESERVED.01` | `FatcaCustomerType_Reserved01` | TField |  |  |
| 13 | `FA.CT.LOCAL.REF` | `FatcaCustomerType_LocalRef` |  |  |  |
| 14 | `FA.CT.OVERRIDE` | `FatcaCustomerType_Override` |  |  |  |
| 15 | `FA.CT.RECORD.STATUS` | `FatcaCustomerType_RecordStatus` | String |  |  |
| 16 | `FA.CT.CURR.NO` | `FatcaCustomerType_CurrNo` | String |  |  |
| 17 | `FA.CT.INPUTTER` | `FatcaCustomerType_Inputter` |  |  |  |
| 18 | `FA.CT.DATE.TIME` | `FatcaCustomerType_DateTime` |  |  |  |
| 19 | `FA.CT.AUTHORISER` | `FatcaCustomerType_Authoriser` | String |  |  |
| 20 | `FA.CT.CO.CODE` | `FatcaCustomerType_CoCode` | String |  |  |
| 21 | `FA.CT.DEPT.CODE` | `FatcaCustomerType_DeptCode` | String |  |  |
| 22 | `FA.CT.AUDITOR.CODE` | `FatcaCustomerType_AuditorCode` | String |  |  |
| 23 | `FA.CT.AUDIT.DATE.TIME` | `FatcaCustomerType_AuditDateTime` | String |  |  |
