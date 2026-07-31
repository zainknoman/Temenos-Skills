# AA.PERIODIC.RULE.CATALOG — Table Schema

> Source: `INSERTS/I_F.AA.PERIODIC.RULE.CATALOG` in `AA_Rules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PRC.DESCRIPTION` | `AaPeriodicRuleCatalog_Description` |  |  |  |
| 2 | `AA.PRC.FULL.DESCRIPTION` | `AaPeriodicRuleCatalog_FullDescription` | TField |  | Detailed description of the definition. |
| 3 | `AA.PRC.RESERVED.1` | `AaPeriodicRuleCatalog_Reserved1` | TField |  |  |
| 4 | `AA.PRC.RESERVED.2` | `AaPeriodicRuleCatalog_Reserved2` | TField |  |  |
| 5 | `AA.PRC.RESERVED.3` | `AaPeriodicRuleCatalog_Reserved3` | TField |  |  |
| 6 | `AA.PRC.RESERVED.4` | `AaPeriodicRuleCatalog_Reserved4` | TField |  |  |
| 7 | `AA.PRC.RESERVED.5` | `AaPeriodicRuleCatalog_Reserved5` | TField |  |  |
| 8 | `AA.PRC.PERIODIC.ATTRIBUTE` | `AaPeriodicRuleCatalog_PeriodicAttribute` | TField |  |  |
| 9 | `AA.PRC.RULE.SOURCE` | `AaPeriodicRuleCatalog_RuleSource` |  |  |  |
| 10 | `AA.PRC.FILTER.BY.PRODUCT` | `AaPeriodicRuleCatalog_FilterByProduct` |  |  |  |
| 11 | `AA.PRC.RESERVED.6` | `AaPeriodicRuleCatalog_Reserved6` |  |  |  |
| 12 | `AA.PRC.RESERVED.7` | `AaPeriodicRuleCatalog_Reserved7` |  |  |  |
| 13 | `AA.PRC.RESERVED.8` | `AaPeriodicRuleCatalog_Reserved8` |  |  |  |
| 14 | `AA.PRC.RESERVED.9` | `AaPeriodicRuleCatalog_Reserved9` |  |  |  |
| 15 | `AA.PRC.RESERVED.10` | `AaPeriodicRuleCatalog_Reserved10` | TField |  |  |
| 16 | `AA.PRC.ACTION` | `AaPeriodicRuleCatalog_Action` | TField |  | Indicates if the definition should be proofed and published. After successful publishing the record cannot be changed, and the definition can only be changed by creating a new version. |
| 17 | `AA.PRC.EFFECTIVE.DATE` | `AaPeriodicRuleCatalog_EffectiveDate` | TField | Yes | Indicates when this version of the definition will be effective for processing. Mandatory if PUBLISH is "YES". Must be a date GE to Today and cannot be prior to the Effective Date of the previous version. |
| 18 | `AA.PRC.PUBLISH.STATUS` | `AaPeriodicRuleCatalog_PublishStatus` | TField |  | This field will contain the result of the publishing effort. 1) Validation Rules a. Non Input. b. System Maintained c. Allowed values are : Completed Successfully or Completed with Error |
| 19 | `AA.PRC.PUBLISH.ERROR` | `AaPeriodicRuleCatalog_PublishError` | TField |  | In the event of the publishing effort resulting in the PUBLISH.ERROR field being set to "Completed with Error", this field will contain error messages encountered 1) Associated Multi-value : Beginning with PUBLISH.ERROR and ending with ERROR.SUGGESTION 2) Validation Rules a. Non Input. b. System Maintained |
| 20 | `AA.PRC.ERROR.SUGGESTION` | `AaPeriodicRuleCatalog_ErrorSuggestion` | TField |  | In the event of the publishing effort resulting in the PUBLISH.ERROR field being set to "Completed with Error", this field will contain suggestions provided in order to correct errors listed in the associated PUBLISH.ERROR 1) Associated Multi-value : Beginning with PUBLISH.ERROR and ending with ERROR.SUGGESTION 2) Validation Rules a. Non Input. b. System Maintained |
| 21 | `AA.PRC.RESERVED.11` | `AaPeriodicRuleCatalog_Reserved11` | TField |  |  |
| 22 | `AA.PRC.RESERVED.12` | `AaPeriodicRuleCatalog_Reserved12` | TField |  |  |
| 23 | `AA.PRC.RESERVED.13` | `AaPeriodicRuleCatalog_Reserved13` | TField |  |  |
| 24 | `AA.PRC.RESERVED.14` | `AaPeriodicRuleCatalog_Reserved14` | TField |  |  |
| 25 | `AA.PRC.RESERVED.15` | `AaPeriodicRuleCatalog_Reserved15` | TField |  |  |
| 26 | `AA.PRC.REFERENCE` | `AaPeriodicRuleCatalog_Reference` | TField |  | This field contains the "ID" for the configuration reference. This is the same as the ID of the definition record without the version number |
| 27 | `AA.PRC.VERSION` | `AaPeriodicRuleCatalog_Version` | TField |  |  |
| 28 | `AA.PRC.RESERVED.16` | `AaPeriodicRuleCatalog_Reserved16` | TField |  |  |
| 29 | `AA.PRC.RESERVED.17` | `AaPeriodicRuleCatalog_Reserved17` | TField |  |  |
| 30 | `AA.PRC.RESERVED.18` | `AaPeriodicRuleCatalog_Reserved18` | TField |  |  |
| 31 | `AA.PRC.RESERVED.19` | `AaPeriodicRuleCatalog_Reserved19` | TField |  |  |
| 32 | `AA.PRC.RESERVED.20` | `AaPeriodicRuleCatalog_Reserved20` | TField |  |  |
| 33 | `AA.PRC.OVERRIDE` | `AaPeriodicRuleCatalog_Override` |  |  |  |
