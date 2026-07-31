# EB.COMPARISON.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.COMPARISON.TYPE` in `AF_Rules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ECT.DESCRIPTION` | `EbComparisonType_Description` |  |  |  |
| 2 | `AA.ECT.VALID.DATA.TYPE` | `EbComparisonType_ValidDataType` |  |  |  |
| 3 | `AA.ECT.RULE.DEF.ROUTINE` | `EbComparisonType_RuleDefRoutine` | TField | Yes | This field enables the user to define a routine to validate that the definition of the rule values in the property or standard comparison rule are correct. This field is mandatory and must be a valid EB.API id. To enable a java component implementation the EB.API record must have a source type of METHOD and implement an interface defined in the EB.API record HOOK.EB.COMPARISON.TYPE.RUL.DEF.RTN. See the EB.API record HOOK.EB.COMPARISON.TYPE.RUL.DEF.RTN for the full list of supported interfaces, initially AA.RuleComparisonHook.validateNegotiableField(). The following are the routines that are used. AA.SINGLE.VALUE.RULE.VAL - Validation of single values for single value rules such as Min, Max etc. AA.LIST.VALUE.RULE.VAL - Validates a list of values supplied for list or range checks. |
| 4 | `AA.ECT.COMPARISON.ROUTINE` | `EbComparisonType_ComparisonRoutine` | TField | Yes | This field enables the user to define a routine to validate the entered value of an arrangement against the defined values in the product property definition. This field is mandatory and must be a valid EB.API id. To enable a java component implementation the EB.API record must have a source type of METHOD and implement an interface defined in the EB.API record HOOK.EB.COMPARISON.TYPE.COMPAR.RTN. See the EB.API record HOOK.EB.COMPARISON.TYPE.COMPAR.RTN for the full list of supported interfaces, initially AA.RuleComparisonHook.compareNegotiatedValue() |
| 5 | `AA.ECT.RULE.ERR.MSG` | `EbComparisonType_RuleErrMsg` | TField | Yes | This field is mandatory. The key to the EB.ERROR table to be used to generate an error message if the rule is broken. |
| 6 | `AA.ECT.RULE.OVE.MSG` | `EbComparisonType_RuleOveMsg` | TField | Yes | This field is mandatory. The key to the OVERRIDE table to be used to generate an override message if the rule is broken. |
| 7 | `AA.ECT.LOCAL.REF` | `EbComparisonType_LocalRef` |  |  |  |
| 8 | `AA.ECT.TYPE` | `EbComparisonType_Type` | TField | Yes | Indicates the Type of comparison to be used. Can take only the following values. 1. CAP 2. FLOOR 3. SOURCE - For this comparison type, NR.VALUE.SOURCE is mandatory. Values can be expanded in future. |
| 9 | `AA.ECT.RESERVED09` | `EbComparisonType_Reserved09` | TField |  |  |
| 10 | `AA.ECT.RESERVED08` | `EbComparisonType_Reserved08` | TField |  |  |
| 11 | `AA.ECT.RESERVED07` | `EbComparisonType_Reserved07` | TField |  |  |
| 12 | `AA.ECT.RESERVED06` | `EbComparisonType_Reserved06` | TField |  |  |
| 13 | `AA.ECT.RESERVED05` | `EbComparisonType_Reserved05` | TField |  |  |
| 14 | `AA.ECT.RESERVED04` | `EbComparisonType_Reserved04` | TField |  |  |
| 15 | `AA.ECT.RESERVED03` | `EbComparisonType_Reserved03` | TField |  |  |
| 16 | `AA.ECT.RESERVED02` | `EbComparisonType_Reserved02` | TField |  |  |
| 17 | `AA.ECT.RESERVED01` | `EbComparisonType_Reserved01` | TField |  |  |
| 18 | `AA.ECT.RECORD.STATUS` | `EbComparisonType_RecordStatus` | String |  |  |
| 19 | `AA.ECT.CURR.NO` | `EbComparisonType_CurrNo` | String |  |  |
| 20 | `AA.ECT.INPUTTER` | `EbComparisonType_Inputter` |  |  |  |
| 21 | `AA.ECT.DATE.TIME` | `EbComparisonType_DateTime` |  |  |  |
| 22 | `AA.ECT.AUTHORISER` | `EbComparisonType_Authoriser` | String |  |  |
| 23 | `AA.ECT.CO.CODE` | `EbComparisonType_CoCode` | String |  |  |
| 24 | `AA.ECT.DEPT.CODE` | `EbComparisonType_DeptCode` | String |  |  |
| 25 | `AA.ECT.AUDITOR.CODE` | `EbComparisonType_AuditorCode` | String |  |  |
| 26 | `AA.ECT.AUDIT.DATE.TIME` | `EbComparisonType_AuditDateTime` | String |  |  |
