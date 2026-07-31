# LE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LE.PARAMETER` in `LE_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LE.LP.ENTITY.RULE` | `LeParameter_EntityRule` | TField | Conditional | RULE to identify whether a customer is an individual customer or an entity or a sub-fund customer. This should return a value of NCI or LEI or SUB.FUND respectively. Optional Field Validation Rules: Should be a valid EB.RULE.GATEWAY id Upto 65 Alphanumeric Characters. Either ENTITY.API or ENTITY.RULE is mandatory |
| 2 | `LE.LP.ENTITY.API` | `LeParameter_EntityApi` | TField | Conditional | API to identify whether a customer is an individual customer or an entity or a sub-fund customer. This should return a value of NCI or LEI or SUB.FUND respectively. The input arguments to this API are Customer ID, Customer Record and the output arguments are EntityType and Error followed by an argument reserved for future use. Optional Field Validation Rules: Should be a valid EB.API id Upto 65 Alphanumeric Characters. Either ENTITY.API or ENTITY.RULE is mandatory |
| 3 | `LE.LP.NOTIFY.EXP.DAYS` | `LeParameter_NotifyExpDays` | TField | No | LEIs with �lapsed� status are not considered valid LEIs. Due to the lead-time involved in acquiring a new LEI via the LOU registration process, bank can set up an override message to notify the end user that the LEI is due for renewal, XX days prior to renewal date. This will help the entity customer to take appropriate action to obtain a valid LEI prior to the next trade. Optional Field Validation Rules: Numbers between 1 and 999 are allowed. |
| 4 | `LE.LP.RESERVED.10` | `LeParameter_Reserved10` | TField |  |  |
| 5 | `LE.LP.RESERVED.09` | `LeParameter_Reserved09` | TField |  |  |
| 6 | `LE.LP.RESERVED.08` | `LeParameter_Reserved08` | TField |  |  |
| 7 | `LE.LP.RESERVED.07` | `LeParameter_Reserved07` | TField |  |  |
| 8 | `LE.LP.RESERVED.06` | `LeParameter_Reserved06` | TField |  |  |
| 9 | `LE.LP.RESERVED.05` | `LeParameter_Reserved05` | TField |  |  |
| 10 | `LE.LP.RESERVED.04` | `LeParameter_Reserved04` | TField |  |  |
| 11 | `LE.LP.RESERVED.03` | `LeParameter_Reserved03` | TField |  |  |
| 12 | `LE.LP.RESERVED.02` | `LeParameter_Reserved02` | TField |  |  |
| 13 | `LE.LP.RESERVED.01` | `LeParameter_Reserved01` | TField |  |  |
| 14 | `LE.LP.LOCAL.REF` | `LeParameter_LocalRef` |  |  |  |
| 15 | `LE.LP.RECORD.STATUS` | `LeParameter_RecordStatus` | String |  |  |
| 16 | `LE.LP.CURR.NO` | `LeParameter_CurrNo` | String |  |  |
| 17 | `LE.LP.INPUTTER` | `LeParameter_Inputter` |  |  |  |
| 18 | `LE.LP.DATE.TIME` | `LeParameter_DateTime` |  |  |  |
| 19 | `LE.LP.AUTHORISER` | `LeParameter_Authoriser` | String |  |  |
| 20 | `LE.LP.CO.CODE` | `LeParameter_CoCode` | String |  |  |
| 21 | `LE.LP.DEPT.CODE` | `LeParameter_DeptCode` | String |  |  |
| 22 | `LE.LP.AUDITOR.CODE` | `LeParameter_AuditorCode` | String |  |  |
| 23 | `LE.LP.AUDIT.DATE.TIME` | `LeParameter_AuditDateTime` | String |  |  |
