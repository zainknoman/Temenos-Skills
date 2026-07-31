# BFW.EVENT.DEFINITION — Table Schema

> Source: `INSERTS/I_F.BFW.EVENT.DEFINITION` in `AC_IFConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BED.DESCRIPTION` | `BfwEventDefinition_Description` |  |  |  |
| 2 | `BED.BASE.TABLE` | `BfwEventDefinition_BaseTable` | TField |  | This is a system maintained field to indicate that the event is triggered when a transaction occurs if the value in this field is STMT.ENTRY and event is triggered during statement production if the value in this field is ACCOUNT. The base table for the events from which the fields will be used to access the Enrichment table. validations: System maintained field. No Change Field. It must be a valid FILE.CONTROL record. 1. If first part of ID is ENTRY then value of this field is STMT.ENTRY 2. If first part of ID is STATEMENT then value of this field is ACCOUNT |
| 3 | `BED.SYS.ENRICHMENT.TABLE` | `BfwEventDefinition_SysEnrichmentTable` |  |  |  |
| 4 | `BED.SYS.BASE.LINK.API` | `BfwEventDefinition_SysBaseLinkApi` |  |  |  |
| 5 | `BED.SYS.BASE.LINK.FIELDS` | `BfwEventDefinition_SysBaseLinkFields` |  |  |  |
| 6 | `BED.RESERVED.20` | `BfwEventDefinition_Reserved20` |  |  |  |
| 7 | `BED.RESERVED.19` | `BfwEventDefinition_Reserved19` |  |  |  |
| 8 | `BED.RESERVED.18` | `BfwEventDefinition_Reserved18` |  |  |  |
| 9 | `BED.RESERVED.17` | `BfwEventDefinition_Reserved17` |  |  |  |
| 10 | `BED.RESERVED.16` | `BfwEventDefinition_Reserved16` |  |  |  |
| 11 | `BED.SYS.CALC.TABLE` | `BfwEventDefinition_SysCalcTable` |  |  |  |
| 12 | `BED.SYS.CALC.FIELDS.API` | `BfwEventDefinition_SysCalcFieldsApi` |  |  |  |
| 13 | `BED.USR.CALC.FIELDS.API` | `BfwEventDefinition_UsrCalcFieldsApi` |  |  |  |
| 14 | `BED.RESERVED.15` | `BfwEventDefinition_Reserved15` |  |  |  |
| 15 | `BED.RESERVED.14` | `BfwEventDefinition_Reserved14` |  |  |  |
| 16 | `BED.RESERVED.13` | `BfwEventDefinition_Reserved13` |  |  |  |
| 17 | `BED.RESERVED.12` | `BfwEventDefinition_Reserved12` |  |  |  |
| 18 | `BED.RESERVED.11` | `BfwEventDefinition_Reserved11` |  |  |  |
| 19 | `BED.SYS.MANDATORY.FIELDS` | `BfwEventDefinition_SysMandatoryFields` |  |  |  |
| 20 | `BED.USR.ENRICHMENT.TABLE` | `BfwEventDefinition_UsrEnrichmentTable` |  |  |  |
| 21 | `BED.RESERVED.10` | `BfwEventDefinition_Reserved10` |  |  |  |
| 22 | `BED.USR.BASE.LINK.FIELDS` | `BfwEventDefinition_UsrBaseLinkFields` |  |  |  |
| 23 | `BED.RESERVED.9` | `BfwEventDefinition_Reserved9` |  |  |  |
| 24 | `BED.RESERVED.8` | `BfwEventDefinition_Reserved8` |  |  |  |
| 25 | `BED.RESERVED.7` | `BfwEventDefinition_Reserved7` |  |  |  |
| 26 | `BED.RESERVED.6` | `BfwEventDefinition_Reserved6` |  |  |  |
| 27 | `BED.RESERVED.5` | `BfwEventDefinition_Reserved5` | TField |  |  |
| 28 | `BED.RESERVED.4` | `BfwEventDefinition_Reserved4` | TField |  |  |
| 29 | `BED.RESERVED.3` | `BfwEventDefinition_Reserved3` | TField |  |  |
| 30 | `BED.RESERVED.2` | `BfwEventDefinition_Reserved2` | TField |  |  |
| 31 | `BED.RESERVED.1` | `BfwEventDefinition_Reserved1` | TField |  |  |
| 32 | `BED.LOCAL.REF` | `BfwEventDefinition_LocalRef` |  |  |  |
| 33 | `BED.OVERRIDE` | `BfwEventDefinition_Override` |  |  |  |
| 34 | `BED.RECORD.STATUS` | `BfwEventDefinition_RecordStatus` | String |  |  |
| 35 | `BED.CURR.NO` | `BfwEventDefinition_CurrNo` | String |  |  |
| 36 | `BED.INPUTTER` | `BfwEventDefinition_Inputter` |  |  |  |
| 37 | `BED.DATE.TIME` | `BfwEventDefinition_DateTime` |  |  |  |
| 38 | `BED.AUTHORISER` | `BfwEventDefinition_Authoriser` | String |  |  |
| 39 | `BED.CO.CODE` | `BfwEventDefinition_CoCode` | String |  |  |
| 40 | `BED.DEPT.CODE` | `BfwEventDefinition_DeptCode` | String |  |  |
| 41 | `BED.AUDITOR.CODE` | `BfwEventDefinition_AuditorCode` | String |  |  |
| 42 | `BED.AUDIT.DATE.TIME` | `BfwEventDefinition_AuditDateTime` | String |  |  |
