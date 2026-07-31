# ADDRESS.RULES — Table Schema

> Source: `INSERTS/I_F.ADDRESS.RULES` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ADRL.DESCRIPTION` | `AddressRules_Description` | TField |  | This will represent the description of the address rules. |
| 2 | `ADRL.ADDRESS.ATTRIBUTE` | `AddressRules_AddressAttribute` |  |  |  |
| 3 | `ADRL.LABEL` | `AddressRules_Label` |  |  |  |
| 4 | `ADRL.MIN.LENGTH` | `AddressRules_MinLength` |  |  |  |
| 5 | `ADRL.MAX.LENGTH` | `AddressRules_MaxLength` |  |  |  |
| 6 | `ADRL.CHAR.TYPE` | `AddressRules_CharType` |  |  |  |
| 7 | `ADRL.PATTERN.MATCH` | `AddressRules_PatternMatch` |  |  |  |
| 8 | `ADRL.LOOKUP.LIST` | `AddressRules_LookupList` |  |  |  |
| 9 | `ADRL.LOOKUP.APPLICATION` | `AddressRules_LookupApplication` |  |  |  |
| 10 | `ADRL.VALIDATION.API` | `AddressRules_ValidationApi` | TField |  | This will represent a hook to a local routine which may be used for complex rules. AddressRuleValidationApi (RecId,ApplRec,OutResponse,Reserved1,Reserved2,Reserved3,Err) OutResponse - Will contain the below array of values. It should delimited with '_' for each attribute. If a particular value marker doesn't has the value also the delimiter should be assigned. InParams: RecId - The id new value. ApplRec - The application record OutParams: OutResponse&lt;AttributeName&gt; OutResponse&lt;AttributeLabel&gt; OutResponse&lt;MinLength&gt; OutResponse&lt;MaxLength&gt; OutResponse&lt;CharType&gt; OutResponse&lt;Pattern&gt; OutResponse&lt;LooupList&gt; OutResponse&lt;LookupApp&gt; OutResponse&lt;DirectData&gt; For any attribute if the direct data is available, it will consider that value as attribute value Otherwise validations will happen based on the other outresponse(maxlength,minlength etc..) values for the particular attribute This will be the allowed values Reserved1 - Reserved for future Reserved2 - Reserved for future Reserved3 - Reserved for future Err - If any error Validation Rules: If given, and the length/char/pattern match/lookup list/lookup table is also given the values returned back from API will overwrite them |
| 11 | `ADRL.RESERVED.10` | `AddressRules_Reserved10` | TField |  |  |
| 12 | `ADRL.RESERVED.9` | `AddressRules_Reserved9` | TField |  |  |
| 13 | `ADRL.RESERVED.8` | `AddressRules_Reserved8` | TField |  |  |
| 14 | `ADRL.RESERVED.7` | `AddressRules_Reserved7` | TField |  |  |
| 15 | `ADRL.RESERVED.6` | `AddressRules_Reserved6` | TField |  |  |
| 16 | `ADRL.RESERVED.5` | `AddressRules_Reserved5` | TField |  |  |
| 17 | `ADRL.RESERVED.4` | `AddressRules_Reserved4` | TField |  |  |
| 18 | `ADRL.RESERVED.3` | `AddressRules_Reserved3` | TField |  |  |
| 19 | `ADRL.RESERVED.2` | `AddressRules_Reserved2` | TField |  |  |
| 20 | `ADRL.RESERVED.1` | `AddressRules_Reserved1` | TField |  |  |
| 21 | `ADRL.LOCAL.REF` | `AddressRules_LocalRef` |  |  |  |
| 22 | `ADRL.OVERRIDE` | `AddressRules_Override` |  |  |  |
| 23 | `ADRL.RECORD.STATUS` | `AddressRules_RecordStatus` | String |  |  |
| 24 | `ADRL.CURR.NO` | `AddressRules_CurrNo` | String |  |  |
| 25 | `ADRL.INPUTTER` | `AddressRules_Inputter` |  |  |  |
| 26 | `ADRL.DATE.TIME` | `AddressRules_DateTime` |  |  |  |
| 27 | `ADRL.AUTHORISER` | `AddressRules_Authoriser` | String |  |  |
| 28 | `ADRL.CO.CODE` | `AddressRules_CoCode` | String |  |  |
| 29 | `ADRL.DEPT.CODE` | `AddressRules_DeptCode` | String |  |  |
| 30 | `ADRL.AUDITOR.CODE` | `AddressRules_AuditorCode` | String |  |  |
| 31 | `ADRL.AUDIT.DATE.TIME` | `AddressRules_AuditDateTime` | String |  |  |
