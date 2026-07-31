# OC.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.OC.CUSTOMER` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.CUS.LEGAL.ENTITY.ID` | `OcCustomer_LegalEntityId` | TField | Yes | Legal Entity Identifier of the bank or the fund managed by the bank. LEI will be used for precise, reliable and unique Identification of each party in a derivatives trade. Validation Rules: Mandatory field for OC related processing and if LE.PARAMETER is not configured. Conditionally mandatory based on the Entity type and if LE.PARAMETER is configured. Up to 40 Alphanumeric Characters. Should be NULL for the Individual Customers If specified, the 20 digit identifier is validated against LE.DIRECTORY (if LE is licensed and configured) |
| 2 | `OC.CUS.ID.TYPE` | `OcCustomer_IdType` | TField | Yes | This field identifies the data type of the value given in the above Legal Identifier Field. Mandatory field. Validation Rules: valid values are LEI,INTERNAL,BIC and OTHER. |
| 3 | `OC.CUS.FINANCIAL.CPARTY` | `OcCustomer_FinancialCparty` | TField | Yes | Denotes whether the customer is a financial counterparty. Mandatory field. Validation Rules: Valid values are yes and no. |
| 4 | `OC.CUS.CORPORATE.SECTOR` | `OcCustomer_CorporateSector` | TField | Yes | Denotes corporate sector of the customer. Valid values are defined in EB.LOOKUP and hence user can configure desired values in future. Validation Rules: Conditionally mandatory field.If financial counterparty is set to yes,then this field becomes mandatory. Valid values are Assurance,Credit Institution,Investment Firm,Insurance Undertaking,Alternative Investment Firm,Other. |
| 5 | `OC.CUS.CLEARING.THRESHOLD` | `OcCustomer_ClearingThreshold` | TField | Yes | Denotes whether the customer, if it is a non-financial entity, reached the clearing threshold limit or not. If financial counterparty field is NO, then clearing threshold field becomes mandatory. Validation Rules: Valid values are above and below. |
| 6 | `OC.CUS.CUSTOMER.TYPE` | `OcCustomer_CustomerType` |  |  |  |
| 7 | `OC.CUS.RESERVED.20` | `OcCustomer_Reserved20` |  |  |  |
| 8 | `OC.CUS.RESERVED.19` | `OcCustomer_Reserved19` |  |  |  |
| 9 | `OC.CUS.RESERVED.18` | `OcCustomer_Reserved18` |  |  |  |
| 10 | `OC.CUS.RESERVED.17` | `OcCustomer_Reserved17` |  |  |  |
| 11 | `OC.CUS.RESERVED.16` | `OcCustomer_Reserved16` |  |  |  |
| 12 | `OC.CUS.CUSTOMER.REGULATOR` | `OcCustomer_CustomerRegulator` | TField | No | Denotes the counterparty Regulator under whose jurisdiction the customer/Counterparty operates. Optional field. Validation Rules: Should be a Valid ID in OC.REGULATOR. |
| 13 | `OC.CUS.REGULATORY.CLASS` | `OcCustomer_RegulatoryClass` | TField | No | Denotes the regulatory classification of the Customer/Counterparty counterparty. Optional field. Validation Rules: Valid Values are Swap Dealer,Major Swap Participant,Financial Counterparty,Non-Financial Counterparty +,Non-Financial Counterparty -,Individual and Other. |
| 14 | `OC.CUS.REPORTING.CUSTOMER` | `OcCustomer_ReportingCustomer` | TField | Conditional | Denotes how the customer side reporting requirement is fulfilled, where dual reporting is mandatory. Optional field. Validation Rules: Valid values are yes, delegated and null. If regulatory classification is individual, then reporting customer must be null. Yes means the customer/counterparty reports the trade details for himself and also for T24 bank. Delegated means T24 bank reports for the Customer/counterparty. Null Means T24 bank and Customer/counterparty report for themselves. |
| 15 | `OC.CUS.MASTER.AGREEMENT` | `OcCustomer_MasterAgreement` | TField | No | denotes other agreements apart from ISDA agreements between T24 Bank and the Customer/ Counterparty. Optional field. |
| 16 | `OC.CUS.USI.NAME.SPACE` | `OcCustomer_UsiNameSpace` | TField | Yes | Denotes the name space given by CFTC or any other regulator to the Customer/Counterparty while registering. Conditionally mandatory field. If regulator is CFTC, then the field becomes mandatory. Validation rules: 20 character alpha numeric. |
| 17 | `OC.CUS.TR.REP.ID` | `OcCustomer_TrRepId` |  |  |  |
| 18 | `OC.CUS.TR.ACC.REF` | `OcCustomer_TrAccRef` |  |  |  |
| 19 | `OC.CUS.RESERVED.15` | `OcCustomer_Reserved15` |  |  |  |
| 20 | `OC.CUS.RESERVED.14` | `OcCustomer_Reserved14` |  |  |  |
| 21 | `OC.CUS.RESERVED.13` | `OcCustomer_Reserved13` |  |  |  |
| 22 | `OC.CUS.RESERVED.12` | `OcCustomer_Reserved12` |  |  |  |
| 23 | `OC.CUS.RESERVED.11` | `OcCustomer_Reserved11` |  |  |  |
| 24 | `OC.CUS.NATIONAL.ID` | `OcCustomer_NationalId` | TField | Yes | To hold NCI-National Client Identifier code of physical persons The determination of NCI is addressed through a separate processing logic, not within the scope of this table. Once the NCI is derived using this logic for an individual customer, the same is required to be captured into this field. Field is made inputtable only if LE.PARAMETER is configured. Validation rules: Conditionally mandatory field. If the Customer is an individual then field becomes mandatory. Upto 20 Alphanumeric characters. Should be NULL for the Entity Customers |
| 25 | `OC.CUS.UMBRELLA.ENTITY` | `OcCustomer_UmbrellaEntity` | TField | No | This field refers to the LEI code of the Umbrella Entity Field is inputtable only if LE.PARAMETER is configured and is validated againt LE.DIRECTORY. Validation rules: Optional field. Upto 20 Alphanumeric characters. Required only if the Customer is a SUB.FUND under some entity. For legal entities differentiated as sub-fund entities, the sub fund entity and the umbrella entity should have a valid registered LEI (as in the case of derivatives) |
| 26 | `OC.CUS.RESERVED.8` | `OcCustomer_Reserved8` | TField |  |  |
| 27 | `OC.CUS.RESERVED.7` | `OcCustomer_Reserved7` | TField |  |  |
| 28 | `OC.CUS.RESERVED.6` | `OcCustomer_Reserved6` | TField |  |  |
| 29 | `OC.CUS.RESERVED.5` | `OcCustomer_Reserved5` | TField |  |  |
| 30 | `OC.CUS.RESERVED.4` | `OcCustomer_Reserved4` | TField |  |  |
| 31 | `OC.CUS.RESERVED.3` | `OcCustomer_Reserved3` | TField |  |  |
| 32 | `OC.CUS.RESERVED.2` | `OcCustomer_Reserved2` | TField |  |  |
| 33 | `OC.CUS.LOCAL.REF` | `OcCustomer_LocalRef` |  |  |  |
| 34 | `OC.CUS.OVERRIDE` | `OcCustomer_Override` |  |  |  |
| 35 | `OC.CUS.RECORD.STATUS` | `OcCustomer_RecordStatus` | String |  |  |
| 36 | `OC.CUS.CURR.NO` | `OcCustomer_CurrNo` | String |  |  |
| 37 | `OC.CUS.INPUTTER` | `OcCustomer_Inputter` |  |  |  |
| 38 | `OC.CUS.DATE.TIME` | `OcCustomer_DateTime` |  |  |  |
| 39 | `OC.CUS.AUTHORISER` | `OcCustomer_Authoriser` | String |  |  |
| 40 | `OC.CUS.CO.CODE` | `OcCustomer_CoCode` | String |  |  |
| 41 | `OC.CUS.DEPT.CODE` | `OcCustomer_DeptCode` | String |  |  |
| 42 | `OC.CUS.AUDITOR.CODE` | `OcCustomer_AuditorCode` | String |  |  |
| 43 | `OC.CUS.AUDIT.DATE.TIME` | `OcCustomer_AuditDateTime` | String |  |  |
