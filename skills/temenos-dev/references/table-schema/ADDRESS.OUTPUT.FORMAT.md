# ADDRESS.OUTPUT.FORMAT — Table Schema

> Source: `INSERTS/I_F.ADDRESS.OUTPUT.FORMAT` in `PY_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AOF.DESCRIPTION` | `AddressOutputFormat_Description` | TField | Yes | Represents the description of address output format. This is a mandatory field. Validation Rules: The value for this field can be of free-text with the maximum length of 70. |
| 2 | `AOF.OUTPUT.ITEM` | `AddressOutputFormat_OutputItem` |  |  |  |
| 3 | `AOF.ADDRESS.ATTRIBUTE` | `AddressOutputFormat_AddressAttribute` |  |  |  |
| 4 | `AOF.PREFIX.TEXT` | `AddressOutputFormat_PrefixText` |  |  |  |
| 5 | `AOF.SUFFIX.TEXT` | `AddressOutputFormat_SuffixText` |  |  |  |
| 6 | `AOF.MAX.LENGTH` | `AddressOutputFormat_MaxLength` |  |  |  |
| 7 | `AOF.NO.LINES.PER.OUTPUTITEM` | `AddressOutputFormat_NoLinesPerOutputitem` |  |  |  |
| 8 | `AOF.MAXIMUM.LINES` | `AddressOutputFormat_MaximumLines` | TField | No | Indicates the maximum lines to be inputted for the respective address output. If the system determines the output has more lines than the maximum lines defined here, the system will only consider the first maximum lines, the remaining will be ignored. This is an optional field with the maximum length of 2. |
| 9 | `AOF.NULL.LINES.ALLOWED` | `AddressOutputFormat_NullLinesAllowed` | TField |  | Indicates if the system should include an output item which is evaluated as blank in the address output. This is an options field with the options "YES_NO_" Validation Rules: If marked as YES, the system will not remove the null output items. If marked as NO or left empty, the system removes the null, output items. The default value is NO. |
| 10 | `AOF.API.OUTPUT.FORMAT` | `AddressOutputFormat_ApiOutputFormat` | TField | No | Identifies the routine to be called by the system. It allows Country and local layer to attach a routine to implement more complex output format rules. If the routine attached, the output address from API will take precedence over whatever the output format is defined. This is an optional field. IN/OUT arguments for the API: InArg1 - InRequestValidateAO InArg1(ApplId) - The requesting appplication id InArg1(Appl) - The requesting application InArg1(ApplRec) - The requesting application record InArg1(FormattedAddress) - Customer level lead company to determine COUNTRY.PARAMETER, If not 'SYSTEM' InArg1(Conversion) - Conversion name InArg2 - Reserved1 InArg3 - Reserved2 OutArg1 - OutResponseValidateAO OutArg1(returnDeliveryAdd) - Address rule applied delivery address OutArg1(Error) - Error if any OutArg2 - Reserved3 Validation Rules: The routine inputted in this field must have an entry in EB.API. |
| 11 | `AOF.RESERVED.10` | `AddressOutputFormat_Reserved10` | TField |  |  |
| 12 | `AOF.RESERVED.9` | `AddressOutputFormat_Reserved9` | TField |  |  |
| 13 | `AOF.RESERVED.8` | `AddressOutputFormat_Reserved8` | TField |  |  |
| 14 | `AOF.RESERVED.7` | `AddressOutputFormat_Reserved7` | TField |  |  |
| 15 | `AOF.RESERVED.6` | `AddressOutputFormat_Reserved6` | TField |  |  |
| 16 | `AOF.RESERVED.5` | `AddressOutputFormat_Reserved5` | TField |  |  |
| 17 | `AOF.RESERVED.4` | `AddressOutputFormat_Reserved4` | TField |  |  |
| 18 | `AOF.RESERVED.3` | `AddressOutputFormat_Reserved3` | TField |  |  |
| 19 | `AOF.RESERVED.2` | `AddressOutputFormat_Reserved2` | TField |  |  |
| 20 | `AOF.RESERVED.1` | `AddressOutputFormat_Reserved1` | TField |  |  |
| 21 | `AOF.LOCAL.REF` | `AddressOutputFormat_LocalRef` |  |  |  |
| 22 | `AOF.OVERRIDE` | `AddressOutputFormat_Override` |  |  |  |
| 23 | `AOF.RECORD.STATUS` | `AddressOutputFormat_RecordStatus` | String |  |  |
| 24 | `AOF.CURR.NO` | `AddressOutputFormat_CurrNo` | String |  |  |
| 25 | `AOF.INPUTTER` | `AddressOutputFormat_Inputter` |  |  |  |
| 26 | `AOF.DATE.TIME` | `AddressOutputFormat_DateTime` |  |  |  |
| 27 | `AOF.AUTHORISER` | `AddressOutputFormat_Authoriser` | String |  |  |
| 28 | `AOF.CO.CODE` | `AddressOutputFormat_CoCode` | String |  |  |
| 29 | `AOF.DEPT.CODE` | `AddressOutputFormat_DeptCode` | String |  |  |
| 30 | `AOF.AUDITOR.CODE` | `AddressOutputFormat_AuditorCode` | String |  |  |
| 31 | `AOF.AUDIT.DATE.TIME` | `AddressOutputFormat_AuditDateTime` | String |  |  |
