# DE.BUSINESS.SERVICE.RULES — Table Schema

> Source: `INSERTS/I_F.DE.BUSINESS.SERVICE.RULES` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.BSR.DOMAIN` | `DeBusinessServiceRules_Domain` | TField |  | This decide the channel/service to which the rule applies.Must be a Delivery Carrier defined in Transact. |
| 2 | `DE.BSR.MESSAGE.NAME.ID` | `DeBusinessServiceRules_MessageNameId` | TField |  | Indicates the message type to which the rule applies to. |
| 3 | `DE.BSR.BUSINESS.APPLICATION` | `DeBusinessServiceRules_BusinessApplication` | TField | No | Indicates the Business Application which has generated the message. Optional, if not provided this means it applies to the message type and service, irrespective of the Business Application generating the message |
| 4 | `DE.BSR.APP.CONTEXT.FIELD` | `DeBusinessServiceRules_AppContextField` | TField | No | Indicates the application context field to which the rule applies to.Optional, if not provided this means it applies to the message type and service, irrespective of the application context |
| 5 | `DE.BSR.APP.CONTEXT.VALUE` | `DeBusinessServiceRules_AppContextValue` | TField | No | Indicates the application context field to which the rule applies to.Optional, if not provided this means it applies to the message type and service, irrespective of the application context |
| 6 | `DE.BSR.START.DATE` | `DeBusinessServiceRules_StartDate` | TField | No | Optional, the date when the rule becomes effective.If no date is specified then the rule is effective immediately. |
| 7 | `DE.BSR.END.DATE` | `DeBusinessServiceRules_EndDate` | TField |  | The last date when the rule applies.If no date is specified then the rule is effective immediately. |
| 8 | `DE.BSR.BUSINESS.SERVICE` | `DeBusinessServiceRules_BusinessService` | TField |  | The Business Service. |
| 9 | `DE.BSR.STATUS` | `DeBusinessServiceRules_Status` | TField |  | Allowed values are Active,Cancelled,Expired .Will be set to Active by default. If the rule has an end date and the date is crossed the system will mark the rule as Expired. |
| 10 | `DE.BSR.RELEASE` | `DeBusinessServiceRules_Release` | TField |  | In order to activate the rule book changes and expire the old configurations, a new RELEASE field is introduced. The rule is active and applies to any rulebook if the Release field is blank. The rule is ignored if the Release field is not equal to the Current Release field in the SWIFT.PARAMETER for the corresponding DE.CARRIER. The Delivery framework will have the ability to consider the records that either contain the current release (Release field equal to the Current Release in SWIFT.PARAMETER) or those which have the Release field as blank. Once the Current Release is changed in the SWIFT.PARAMETER; the records with the Release equal to the Previous Release of SWIFT.PARAMETER will be moved to History. Validation Rules: Should be a valid year. |
| 11 | `DE.BSR.RESERVED.9` | `DeBusinessServiceRules_Reserved9` | TField |  |  |
| 12 | `DE.BSR.RESERVED.8` | `DeBusinessServiceRules_Reserved8` | TField |  |  |
| 13 | `DE.BSR.RESERVED.7` | `DeBusinessServiceRules_Reserved7` | TField |  |  |
| 14 | `DE.BSR.RESERVED.6` | `DeBusinessServiceRules_Reserved6` | TField |  |  |
| 15 | `DE.BSR.RESERVED.5` | `DeBusinessServiceRules_Reserved5` | TField |  |  |
| 16 | `DE.BSR.RESERVED.4` | `DeBusinessServiceRules_Reserved4` | TField |  |  |
| 17 | `DE.BSR.RESERVED.3` | `DeBusinessServiceRules_Reserved3` | TField |  |  |
| 18 | `DE.BSR.RESERVED.2` | `DeBusinessServiceRules_Reserved2` | TField |  |  |
| 19 | `DE.BSR.RESERVED.1` | `DeBusinessServiceRules_Reserved1` | TField |  |  |
| 20 | `DE.BSR.LOCAL.REF` | `DeBusinessServiceRules_LocalRef` |  |  |  |
| 21 | `DE.BSR.OVERRIDE` | `DeBusinessServiceRules_Override` |  |  |  |
| 22 | `DE.BSR.RECORD.STATUS` | `DeBusinessServiceRules_RecordStatus` | String |  |  |
| 23 | `DE.BSR.CURR.NO` | `DeBusinessServiceRules_CurrNo` | String |  |  |
| 24 | `DE.BSR.INPUTTER` | `DeBusinessServiceRules_Inputter` |  |  |  |
| 25 | `DE.BSR.DATE.TIME` | `DeBusinessServiceRules_DateTime` |  |  |  |
| 26 | `DE.BSR.AUTHORISER` | `DeBusinessServiceRules_Authoriser` | String |  |  |
| 27 | `DE.BSR.CO.CODE` | `DeBusinessServiceRules_CoCode` | String |  |  |
| 28 | `DE.BSR.DEPT.CODE` | `DeBusinessServiceRules_DeptCode` | String |  |  |
| 29 | `DE.BSR.AUDITOR.CODE` | `DeBusinessServiceRules_AuditorCode` | String |  |  |
| 30 | `DE.BSR.AUDIT.DATE.TIME` | `DeBusinessServiceRules_AuditDateTime` | String |  |  |
