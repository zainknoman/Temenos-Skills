# COUNTRY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.COUNTRY.PARAMETER` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CP.APPLY.ADDRESS.RULES` | `CountryParameter_ApplyAddressRules` | TField |  | If APPLY ADDRESS RULES is blank (N) then no validation will take place. If APPLY ADDRESS RULES is set to Yes, the system will check the address rule defined for the respective address country and address type. |
| 2 | `ST.CP.DEFAULT.ADDRESS.RULE` | `CountryParameter_DefaultAddressRule` | TField |  | Validated against the keys of ADDRESS.RULES table.Represents the default address to be used when there is not any address country rule defined for the Address Country. |
| 3 | `ST.CP.GENERIC.TYPE` | `CountryParameter_GenericType` |  |  |  |
| 4 | `ST.CP.GENERIC.RULE` | `CountryParameter_GenericRule` |  |  |  |
| 5 | `ST.CP.CARRIER.TYPE` | `CountryParameter_CarrierType` |  |  |  |
| 6 | `ST.CP.DEFAULT.TO.ADDR.OUT.FMT` | `CountryParameter_DefaultToAddrOutFmt` |  |  |  |
| 7 | `ST.CP.DE.FORMAT.CONVERSION` | `CountryParameter_DeFormatConversion` |  |  |  |
| 8 | `ST.CP.DEFAULT.OUTPUT.FMT` | `CountryParameter_DefaultOutputFmt` |  |  |  |
| 9 | `ST.CP.UPD.CONTACT.DATA.DIRECT` | `CountryParameter_UpdContactDataDirect` | TField |  | Specifies if the contact data (related to emails, phones) will be updated/captured directly on the correspondence delivery address. Please note that main/primary addresses (PRINT.1, EMAIL.1 and SMS.1) will be always updated based on the details captured in CustomerThe possible values are: YES, NO or blank. NO and blank have the same meaning. - If left blank or NO, only the Customer application will be used to create/update contact data in all SMS and EMAIL delivery addresses.The existing phone, sms and email will be used to update the DE.ADDRESS as per existing functionality. - If YES, the contact details will be created/updated directly in the additional EMAIL and SMS Delivery Addresses,with the exception of the primary addresses. Once this is set to YES it cannot be changed after that. |
| 10 | `ST.CP.UPD.ADDR.HOLD.OPT` | `CountryParameter_UpdAddressHoldOpt` |  |  |  |
| 11 | `ST.CP.UNSTRUCT.ADD.DEFAULT.FORMAT` | `CountryParameter_UnstructAddDefaultFormat` | TField |  | Identifies an unstructured address output format Valid ADDRESS.OUTPUT.FORMAT record ID should be provided, based on which the unstructured address output will be returned. If the field is opted then unstructured output format will be fetched from this default format If not opted based on the configuration of the fields DEFAULT.TO.ADDR.OUT.FMT and DEFAULT.OUTPUT.FMT the unstructured address output format will be fetched. Will return the unstructured format irrespective of the carrier, considering primary address of Customer |
| 12 | `ST.CP.RESERVED.7` | `CountryParameter_Reserved7` | TField |  |  |
| 13 | `ST.CP.RESERVED.6` | `CountryParameter_Reserved6` | TField |  |  |
| 14 | `ST.CP.RESERVED.5` | `CountryParameter_Reserved5` | TField |  |  |
| 15 | `ST.CP.RESERVED.4` | `CountryParameter_Reserved4` | TField |  |  |
| 16 | `ST.CP.RESERVED.3` | `CountryParameter_Reserved3` | TField |  |  |
| 17 | `ST.CP.RESERVED.2` | `CountryParameter_Reserved2` | TField |  |  |
| 18 | `ST.CP.RESERVED.1` | `CountryParameter_Reserved1` | TField |  |  |
| 19 | `ST.CP.LOCAL.REF` | `CountryParameter_LocalRef` |  |  |  |
| 20 | `ST.CP.OVERRIDE` | `CountryParameter_Override` |  |  |  |
| 21 | `ST.CP.RECORD.STATUS` | `CountryParameter_RecordStatus` | String |  |  |
| 22 | `ST.CP.CURR.NO` | `CountryParameter_CurrNo` | String |  |  |
| 23 | `ST.CP.INPUTTER` | `CountryParameter_Inputter` |  |  |  |
| 24 | `ST.CP.DATE.TIME` | `CountryParameter_DateTime` |  |  |  |
| 25 | `ST.CP.AUTHORISER` | `CountryParameter_Authoriser` | String |  |  |
| 26 | `ST.CP.CO.CODE` | `CountryParameter_CoCode` | String |  |  |
| 27 | `ST.CP.DEPT.CODE` | `CountryParameter_DeptCode` | String |  |  |
| 28 | `ST.CP.AUDITOR.CODE` | `CountryParameter_AuditorCode` | String |  |  |
| 29 | `ST.CP.AUDIT.DATE.TIME` | `CountryParameter_AuditDateTime` | String |  |  |
