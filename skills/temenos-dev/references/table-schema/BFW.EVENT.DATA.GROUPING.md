# BFW.EVENT.DATA.GROUPING — Table Schema

> Source: `INSERTS/I_F.BFW.EVENT.DATA.GROUPING` in `AC_IFConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BDG.DESCRIPTION` | `BfwEventDataGrouping_Description` |  |  |  |
| 2 | `BDG.PATH` | `BfwEventDataGrouping_Path` |  |  |  |
| 3 | `BDG.MESSAGE.TYPE` | `BfwEventDataGrouping_MessageType` |  |  |  |
| 4 | `BDG.RESERVED.20` | `BfwEventDataGrouping_Reserved20` |  |  |  |
| 5 | `BDG.RESERVED.19` | `BfwEventDataGrouping_Reserved19` |  |  |  |
| 6 | `BDG.RESERVED.18` | `BfwEventDataGrouping_Reserved18` |  |  |  |
| 7 | `BDG.RESERVED.17` | `BfwEventDataGrouping_Reserved17` |  |  |  |
| 8 | `BDG.RESERVED.16` | `BfwEventDataGrouping_Reserved16` |  |  |  |
| 9 | `BDG.DISPLAY.NAME` | `BfwEventDataGrouping_DisplayName` | TField | Yes | Specifies an alias name used to refer the Tag path(s). As a tag path may be too lengthy to be mapped in IF Designer during the design-time, a meaningful and short Display name will be assigned to each of the XML tag grouping. For example: Consider the tag path Entry>TransactionDetails>BankTransactionCode>Domain>Code Instead of using this path an alias name can be defined as Entry_BkTxCd and in design time this alias name will be used instead of the tag path. During statement production Microservices will understand the alias name and the corresponding tag path by consuming this table. This field accepts only unique value (i.e.) a Display name defined in one BFW.EVENT.DATA.GROUPING record cannot be repeated again . Validation Rules: 1. Mandatory Input and NOCHANGE field 2. Allowed characters - (a-z), (A-Z), (0-9) and the special character "_" (only underscore is allowed) 3. First character must be an alphabet |
| 10 | `BDG.DISPLAY.DECISION` | `BfwEventDataGrouping_DisplayDecision` | TField | Conditional | Specifies whether a Display Name is mandatory or optional in the flow for the CAMT message. The default Display Decision is "OPTIONAL". Records released by Temenos will have the Display Decision updated as "MANDATORY" for the Display names that are mandatory in CAMT schema. The other system records and user created records will have the default value defined. This field is not allowed for user input or amendment. Validation Rules: 1. Valid values are MANDATORY_OPTIONAL 2. Default value is OPTIONAL 3. Field not allowed for user input or amendment |
| 11 | `BDG.MANUAL.DISPLAY.DECISION` | `BfwEventDataGrouping_ManualDisplayDecision` | TField | Conditional | Allows the user to make an optional display decision as mandatory and can be reverted to optional. This field is enabled for user input only if "DISPLAY.DECISION" is "OPTIONAL". This field, if defined will precede over the DISPLAY.DECISION field. Validation Rules: 1. Valid values are MANDATORY_OPTIONAL_NULL 2. Default value is NULL 3. Field allowed for input or amendment only if DISPLAY.DECISION is set to "OPTIONAL" |
| 12 | `BDG.EVENT.TYPE` | `BfwEventDataGrouping_EventType` |  |  |  |
| 13 | `BDG.DATA.TYPE` | `BfwEventDataGrouping_DataType` | TField | No | Specifies the type of value or format that is applicable for a Display name Eg. String, Numeric, Amount, Currency, Date etc There is no validation to check whether data type defined is valid or not during record creation. If the field is blank then it will be considered as string during run time. Validation Rules: 1. Optional input and NOCHANGE once defined |
| 14 | `BDG.SYSTEM.GENERATED` | `BfwEventDataGrouping_SystemGenerated` | TField |  | Field to indicate whether a record is controlled by the USER or SYSTEM which is updated based on site reference. Validations Rules: 1. NOINPUT field 2. Valid values are SYSTEM_USER 3. Reversal not allowed if SYSTEM.GENERATED is "SYSTEM" |
| 15 | `BDG.RESERVED.15` | `BfwEventDataGrouping_Reserved15` | TField |  |  |
| 16 | `BDG.RESERVED.14` | `BfwEventDataGrouping_Reserved14` | TField |  |  |
| 17 | `BDG.RESERVED.13` | `BfwEventDataGrouping_Reserved13` | TField |  |  |
| 18 | `BDG.RESERVED.12` | `BfwEventDataGrouping_Reserved12` | TField |  |  |
| 19 | `BDG.RESERVED.11` | `BfwEventDataGrouping_Reserved11` | TField |  |  |
| 20 | `BDG.RESERVED.10` | `BfwEventDataGrouping_Reserved10` | TField |  |  |
| 21 | `BDG.RESERVED.9` | `BfwEventDataGrouping_Reserved9` | TField |  |  |
| 22 | `BDG.RESERVED.8` | `BfwEventDataGrouping_Reserved8` | TField |  |  |
| 23 | `BDG.RESERVED.7` | `BfwEventDataGrouping_Reserved7` | TField |  |  |
| 24 | `BDG.RESERVED.6` | `BfwEventDataGrouping_Reserved6` | TField |  |  |
| 25 | `BDG.RESERVED.5` | `BfwEventDataGrouping_Reserved5` | TField |  |  |
| 26 | `BDG.RESERVED.4` | `BfwEventDataGrouping_Reserved4` | TField |  |  |
| 27 | `BDG.RESERVED.3` | `BfwEventDataGrouping_Reserved3` | TField |  |  |
| 28 | `BDG.RESERVED.2` | `BfwEventDataGrouping_Reserved2` | TField |  |  |
| 29 | `BDG.RESERVED.1` | `BfwEventDataGrouping_Reserved1` | TField |  |  |
| 30 | `BDG.LOCAL.REF` | `BfwEventDataGrouping_LocalRef` |  |  |  |
| 31 | `BDG.OVERRIDE` | `BfwEventDataGrouping_Override` |  |  |  |
| 32 | `BDG.RECORD.STATUS` | `BfwEventDataGrouping_RecordStatus` | String |  |  |
| 33 | `BDG.CURR.NO` | `BfwEventDataGrouping_CurrNo` | String |  |  |
| 34 | `BDG.INPUTTER` | `BfwEventDataGrouping_Inputter` |  |  |  |
| 35 | `BDG.DATE.TIME` | `BfwEventDataGrouping_DateTime` |  |  |  |
| 36 | `BDG.AUTHORISER` | `BfwEventDataGrouping_Authoriser` | String |  |  |
| 37 | `BDG.CO.CODE` | `BfwEventDataGrouping_CoCode` | String |  |  |
| 38 | `BDG.DEPT.CODE` | `BfwEventDataGrouping_DeptCode` | String |  |  |
| 39 | `BDG.AUDITOR.CODE` | `BfwEventDataGrouping_AuditorCode` | String |  |  |
| 40 | `BDG.AUDIT.DATE.TIME` | `BfwEventDataGrouping_AuditDateTime` | String |  |  |
