# ADDRESS.OUTPUT.RULES — Table Schema

> Source: `INSERTS/I_F.ADDRESS.OUTPUT.RULES` in `PY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AOR.DESCRIPTION` | `AddressOutputRules_Description` | TField | Yes | This will represent the description of the address country output rule for a specific country for various carriers. This is a mandatory field. Validation Rules: The value for this field can be of free-text with the maximum length of 70. |
| 2 | `AOR.CARRIER.TYPE` | `AddressOutputRules_CarrierType` |  |  |  |
| 3 | `AOR.TO.ADDR.OUTPUT.AMT` | `AddressOutputRules_ToAddrOutputAmt` |  |  |  |
| 4 | `AOR.DE.FORMAT.CONVERSION` | `AddressOutputRules_DeFormatConversion` |  |  |  |
| 5 | `AOR.OUTPUT.FORMAT` | `AddressOutputRules_OutputFormat` |  |  |  |
| 6 | `AOR.UNSTRUCT.ADD.DEFAULT.FORMAT` | `AddressOutputRules_UnstructAddDefaultFormat` | TField |  | Identifies an unstructured address output format Valid ADDRESS.OUTPUT.FORMAT record ID should be provided, based on which the unstructured address output will be returned. If the field is opted then unstructured output format will be fetched from this default format If not opted based on the configuration of the fields DEFAULT.TO.ADDR.OUT.FMT and DEFAULT.OUTPUT.FMT the unstructured address output format will be fetched. Will return the unstructured format irrespective of the carrier, considering primary address of Customer |
| 7 | `AOR.RESERVED.9` | `AddressOutputRules_Reserved9` | TField |  |  |
| 8 | `AOR.RESERVED.8` | `AddressOutputRules_Reserved8` | TField |  |  |
| 9 | `AOR.RESERVED.7` | `AddressOutputRules_Reserved7` | TField |  |  |
| 10 | `AOR.RESERVED.6` | `AddressOutputRules_Reserved6` | TField |  |  |
| 11 | `AOR.RESERVED.5` | `AddressOutputRules_Reserved5` | TField |  |  |
| 12 | `AOR.RESERVED.4` | `AddressOutputRules_Reserved4` | TField |  |  |
| 13 | `AOR.RESERVED.3` | `AddressOutputRules_Reserved3` | TField |  |  |
| 14 | `AOR.RESERVED.2` | `AddressOutputRules_Reserved2` | TField |  |  |
| 15 | `AOR.RESERVED.1` | `AddressOutputRules_Reserved1` | TField |  |  |
| 16 | `AOR.LOCAL.REF` | `AddressOutputRules_LocalRef` |  |  |  |
| 17 | `AOR.OVERRIDE` | `AddressOutputRules_Override` |  |  |  |
| 18 | `AOR.RECORD.STATUS` | `AddressOutputRules_RecordStatus` | String |  |  |
| 19 | `AOR.CURR.NO` | `AddressOutputRules_CurrNo` | String |  |  |
| 20 | `AOR.INPUTTER` | `AddressOutputRules_Inputter` |  |  |  |
| 21 | `AOR.DATE.TIME` | `AddressOutputRules_DateTime` |  |  |  |
| 22 | `AOR.AUTHORISER` | `AddressOutputRules_Authoriser` | String |  |  |
| 23 | `AOR.CO.CODE` | `AddressOutputRules_CoCode` | String |  |  |
| 24 | `AOR.DEPT.CODE` | `AddressOutputRules_DeptCode` | String |  |  |
| 25 | `AOR.AUDITOR.CODE` | `AddressOutputRules_AuditorCode` | String |  |  |
| 26 | `AOR.AUDIT.DATE.TIME` | `AddressOutputRules_AuditDateTime` | String |  |  |
