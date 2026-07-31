# AA.PERIODIC.ATTRIBUTE.CLASS — Table Schema

> Source: `INSERTS/I_F.AA.PERIODIC.ATTRIBUTE.CLASS` in `AA_Rules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PAC.DESCRIPTION` | `AaPeriodicAttributeClass_Description` |  |  |  |
| 2 | `AA.PAC.PROPERTY.CLASS` | `AaPeriodicAttributeClass_PropertyClass` |  |  |  |
| 3 | `AA.PAC.ACTION` | `AaPeriodicAttributeClass_Action` |  |  |  |
| 4 | `AA.PAC.COMPARISON.TYPE` | `AaPeriodicAttributeClass_ComparisonType` |  |  |  |
| 5 | `AA.PAC.RULE.VAL.RTN` | `AaPeriodicAttributeClass_RuleValRtn` | TField |  | This field enables the user to define a routine to return the value for the comparison routine to do the compare from property record. This field must be a valid EB.API id. To enable a java component implementation the EB.API record must have a source type of METHOD and implement an interface defined in the EB.API record HOOK.AA.PERIODIC.ATTRIBUTE.CLASS. See the EB.API record HOOK.AA.PERIODIC.ATTRIBUTE.CLASS for the full list of supported interfaces, initially AA.RuleComparisonHook.getComparableValues(). Deprecated AA.RuleComparisonHook.getComparableValues(), use AA.RuleComparisonHook.getComparableStringValues() instead. Routine Arguments: Incoming : PROPERTY.ID : Property ID to which the rule is attached. START.DATE : Start Date for the Rule. (Depends on the Period Type and Period defined in AA.PERIODIC.ATTRIBUTE) END.DATE : End Date for the Rule. (Depends on the Period Type and Period defined in AA.PERIODIC.ATTRIBUTE) CURRENT.DATE : Effective Date on which rule is validated (Activity Effective Date) BALANCE.TYPE : BALANCE.TYPE field in Activity Restriction and RULE.SOURCE field in PRICING.RULES. ACTIVITY.IDS : Activity that will be used for Rule Evaluation. CURRENT.VALUE: In AA.PERIODIC.ATTRIBUTE, we could specify if the periodic attribute is to be evaluated for single arrangement or multiple arrangements i.e MULTI.ARRANGEMENT can be set as NULL, BUNDLE OR CRA 1.For null option this parameter value will be null 2.For BUNDLE option value will be passed in the following format Arrangement.id:@VM:Account.id:@VM:RecipientCcy 3.For CRA option value will be passed in the following format Arrangement.id:@VM:Account.id Return : START.VALUE : The value for the attribute on the Start Date. END.VALUE : The value for the attribute on the End Date. |
| 6 | `AA.PAC.DATA.TYPE` | `AaPeriodicAttributeClass_DataType` | TField | Yes | This field represents the Valid Data Type. For example : AMT, R, D etc., The attribute to which the periodic rule is defined should have a data type specified so that the existing core routines validate the rule content. Mandatory Input |
| 7 | `AA.PAC.TYPE` | `AaPeriodicAttributeClass_Type` |  |  |  |
| 8 | `AA.PAC.RULE.ERR.MSG` | `AaPeriodicAttributeClass_RuleErrMsg` | TField |  | This field represents error message that needs to be raised when the rule is broken. Should be valid record id of the file EB.ERROR |
| 9 | `AA.PAC.RULE.OVE.MSG` | `AaPeriodicAttributeClass_RuleOveMsg` | TField |  | This field represents override message that needs to be raised when the rule is broken. Should be a valid record id of the file OVERRIDE |
| 10 | `AA.PAC.SYSTEM.GENERATED` | `AaPeriodicAttributeClass_SystemGenerated` | TField |  | If it is set as YES, it indicates that the record is released by Temenos. |
| 11 | `AA.PAC.SOURCE.TYPE` | `AaPeriodicAttributeClass_SourceType` |  |  |  |
| 12 | `AA.PAC.RESERVED06` | `AaPeriodicAttributeClass_Reserved06` | TField |  |  |
| 13 | `AA.PAC.RESERVED05` | `AaPeriodicAttributeClass_Reserved05` | TField |  |  |
| 14 | `AA.PAC.RESERVED04` | `AaPeriodicAttributeClass_Reserved04` | TField |  |  |
| 15 | `AA.PAC.RESERVED03` | `AaPeriodicAttributeClass_Reserved03` | TField |  |  |
| 16 | `AA.PAC.RESERVED02` | `AaPeriodicAttributeClass_Reserved02` | TField |  |  |
| 17 | `AA.PAC.RESERVED01` | `AaPeriodicAttributeClass_Reserved01` | TField |  |  |
| 18 | `AA.PAC.RECORD.STATUS` | `AaPeriodicAttributeClass_RecordStatus` | String |  |  |
| 19 | `AA.PAC.CURR.NO` | `AaPeriodicAttributeClass_CurrNo` | String |  |  |
| 20 | `AA.PAC.INPUTTER` | `AaPeriodicAttributeClass_Inputter` |  |  |  |
| 21 | `AA.PAC.DATE.TIME` | `AaPeriodicAttributeClass_DateTime` |  |  |  |
| 22 | `AA.PAC.AUTHORISER` | `AaPeriodicAttributeClass_Authoriser` | String |  |  |
| 23 | `AA.PAC.CO.CODE` | `AaPeriodicAttributeClass_CoCode` | String |  |  |
| 24 | `AA.PAC.DEPT.CODE` | `AaPeriodicAttributeClass_DeptCode` | String |  |  |
| 25 | `AA.PAC.AUDITOR.CODE` | `AaPeriodicAttributeClass_AuditorCode` | String |  |  |
| 26 | `AA.PAC.AUDIT.DATE.TIME` | `AaPeriodicAttributeClass_AuditDateTime` | String |  |  |
