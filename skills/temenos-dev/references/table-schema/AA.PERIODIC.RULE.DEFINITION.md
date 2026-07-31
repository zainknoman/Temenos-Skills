# AA.PERIODIC.RULE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.AA.PERIODIC.RULE.DEFINITION` in `AA_Rules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRD.DESCRIPTION` | `AaPeriodicRuleDefinition_Description` |  |  |  |
| 2 | `AA.PRD.FULL.DESCRIPTION` | `AaPeriodicRuleDefinition_FullDescription` | TField |  | Detailed description of the definition. |
| 3 | `AA.PRD.RESERVED.1` | `AaPeriodicRuleDefinition_Reserved1` | TField |  |  |
| 4 | `AA.PRD.RESERVED.2` | `AaPeriodicRuleDefinition_Reserved2` | TField |  |  |
| 5 | `AA.PRD.RESERVED.3` | `AaPeriodicRuleDefinition_Reserved3` | TField |  |  |
| 6 | `AA.PRD.RESERVED.4` | `AaPeriodicRuleDefinition_Reserved4` | TField |  |  |
| 7 | `AA.PRD.RESERVED.5` | `AaPeriodicRuleDefinition_Reserved5` | TField |  |  |
| 8 | `AA.PRD.PERIODIC.ATTRIBUTE` | `AaPeriodicRuleDefinition_PeriodicAttribute` | TField |  |  |
| 9 | `AA.PRD.RULE.SOURCE` | `AaPeriodicRuleDefinition_RuleSource` |  |  |  |
| 10 | `AA.PRD.FILTER.BY.PRODUCT` | `AaPeriodicRuleDefinition_FilterByProduct` |  |  |  |
| 11 | `AA.PRD.RESERVED.6` | `AaPeriodicRuleDefinition_Reserved6` |  |  |  |
| 12 | `AA.PRD.RESERVED.7` | `AaPeriodicRuleDefinition_Reserved7` |  |  |  |
| 13 | `AA.PRD.RESERVED.8` | `AaPeriodicRuleDefinition_Reserved8` |  |  |  |
| 14 | `AA.PRD.RESERVED.9` | `AaPeriodicRuleDefinition_Reserved9` |  |  |  |
| 15 | `AA.PRD.RESERVED.10` | `AaPeriodicRuleDefinition_Reserved10` | TField |  |  |
| 16 | `AA.PRD.ACTION` | `AaPeriodicRuleDefinition_Action` | TField |  | Indicates if the definition should be proofed and published. After successful publishing the record cannot be changed, and the definition can only be changed by creating a new version. |
| 17 | `AA.PRD.EFFECTIVE.DATE` | `AaPeriodicRuleDefinition_EffectiveDate` | TField | Yes | Indicates when this version of the definition will be effective for processing. Mandatory if PUBLISH is "YES". Must be a date GE to Today and cannot be prior to the Effective Date of the previous version. |
| 18 | `AA.PRD.PUBLISH.STATUS` | `AaPeriodicRuleDefinition_PublishStatus` | TField |  | This field will contain the result of the publishing effort. Validation Rules a. Non Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Error |
| 19 | `AA.PRD.PUBLISH.ERROR` | `AaPeriodicRuleDefinition_PublishError` | TField |  | In the event of the publishing effort resulting in the PUBLISH.ERROR field being set to "Completed with Error", this field will contain error messages encountered 1.Associated Multi-value : Beginning with PUBLISH.ERROR and ending with ERROR.SUGGESTION. 2.Validation Rules a. Non Input. b. System Maintained |
| 20 | `AA.PRD.ERROR.SUGGESTION` | `AaPeriodicRuleDefinition_ErrorSuggestion` | TField |  | In the event of the publishing effort resulting in the PUBLISH.ERROR field being set to "Completed with Error", this field will contain suggestions provided in order to correct errors listed in the associated PUBLISH.ERROR 1.Associated Multi-value : Beginning with PUBLISH.ERROR and ending with ERROR.SUGGESTION. 2.Validation Rules a. Non Input. b. System Maintained |
| 21 | `AA.PRD.RESERVED.11` | `AaPeriodicRuleDefinition_Reserved11` | TField |  |  |
| 22 | `AA.PRD.RESERVED.12` | `AaPeriodicRuleDefinition_Reserved12` | TField |  |  |
| 23 | `AA.PRD.RESERVED.13` | `AaPeriodicRuleDefinition_Reserved13` | TField |  |  |
| 24 | `AA.PRD.RESERVED.14` | `AaPeriodicRuleDefinition_Reserved14` | TField |  |  |
| 25 | `AA.PRD.RESERVED.15` | `AaPeriodicRuleDefinition_Reserved15` | TField |  |  |
| 26 | `AA.PRD.REFERENCE` | `AaPeriodicRuleDefinition_Reference` | TField |  | This field contains the "ID" for the configuration reference. This is the same as the ID of the definition record without the version number |
| 27 | `AA.PRD.VERSION` | `AaPeriodicRuleDefinition_Version` | TField |  | The version number of the definition. This number will automatically be incremented when a new record is created. |
| 28 | `AA.PRD.RESERVED.16` | `AaPeriodicRuleDefinition_Reserved16` | TField |  |  |
| 29 | `AA.PRD.RESERVED.17` | `AaPeriodicRuleDefinition_Reserved17` | TField |  |  |
| 30 | `AA.PRD.RESERVED.18` | `AaPeriodicRuleDefinition_Reserved18` | TField |  |  |
| 31 | `AA.PRD.RESERVED.19` | `AaPeriodicRuleDefinition_Reserved19` | TField |  |  |
| 32 | `AA.PRD.RESERVED.20` | `AaPeriodicRuleDefinition_Reserved20` | TField |  |  |
| 33 | `AA.PRD.OVERRIDE` | `AaPeriodicRuleDefinition_Override` |  |  |  |
| 34 | `AA.PRD.RECORD.STATUS` | `AaPeriodicRuleDefinition_RecordStatus` | String |  |  |
| 35 | `AA.PRD.CURR.NO` | `AaPeriodicRuleDefinition_CurrNo` | String |  |  |
| 36 | `AA.PRD.INPUTTER` | `AaPeriodicRuleDefinition_Inputter` |  |  |  |
| 37 | `AA.PRD.DATE.TIME` | `AaPeriodicRuleDefinition_DateTime` |  |  |  |
| 38 | `AA.PRD.AUTHORISER` | `AaPeriodicRuleDefinition_Authoriser` | String |  |  |
| 39 | `AA.PRD.CO.CODE` | `AaPeriodicRuleDefinition_CoCode` | String |  |  |
| 40 | `AA.PRD.DEPT.CODE` | `AaPeriodicRuleDefinition_DeptCode` | String |  |  |
| 41 | `AA.PRD.AUDITOR.CODE` | `AaPeriodicRuleDefinition_AuditorCode` | String |  |  |
| 42 | `AA.PRD.AUDIT.DATE.TIME` | `AaPeriodicRuleDefinition_AuditDateTime` | String |  |  |
