# DE.DISTINGUISH.NAME.RULES — Table Schema

> Source: `INSERTS/I_F.DE.DISTINGUISH.NAME.RULES` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.DNR.SCOPE` | `DeDistinguishNameRules_Scope` | TField |  | Indicates if the scope of this rule applies to the Requestor ( sender) of the message or to the Responder Validation Rules: Values can be either Requestor or Responder |
| 2 | `DE.DNR.DOMAIN` | `DeDistinguishNameRules_Domain` | TField |  | This decide the channel to which the rule applies. Must be a Delivery Carrier defined in Transact If not specified it means any Channel ( Delivery Carrier) |
| 3 | `DE.DNR.CUSTOMER` | `DeDistinguishNameRules_Customer` | TField |  | The customer number for which the rule applies. Must be a valid Customer Number. If not supplied this means any customer |
| 4 | `DE.DNR.ADDRESS` | `DeDistinguishNameRules_Address` | TField |  | Indicates the address (BIC) to which the rule applies. If not supplied this means any address |
| 5 | `DE.DNR.MESSAGE.TYPE` | `DeDistinguishNameRules_MessageType` | TField |  | Indicates the message type to which the rule applies to. If not supplied this means any Message type |
| 6 | `DE.DNR.CURRENCY` | `DeDistinguishNameRules_Currency` | TField |  | Indicates the currency to which the rule applies to. If not supplied this means any currency |
| 7 | `DE.DNR.APP.CONTEXT.FIELD` | `DeDistinguishNameRules_AppContextField` | TField |  | Indicates the application context field to which the rule applies to. If not supplied this means any |
| 8 | `DE.DNR.APP.CONTEXT.VALUE` | `DeDistinguishNameRules_AppContextValue` | TField |  | Indicates the application context field value to which the rule applies to. If not supplied this means any |
| 9 | `DE.DNR.START.DATE` | `DeDistinguishNameRules_StartDate` | TField | No | The date when the rule becomes effective Optional.If no date is specified then the rule is effective immediately |
| 10 | `DE.DNR.END.DATE` | `DeDistinguishNameRules_EndDate` | TField |  | The last date when the rule applies If no date is specified then the rule is effective indefinetely |
| 11 | `DE.DNR.DISTINGUISH.NAME.RULE` | `DeDistinguishNameRules_DistinguishNameRule` | TField |  | The rule to determine the distinguish name based on the supplied address Validation Rules: Options: None DefaultDNLevel3: This will consider the To/From Address ( this is expected to be a BIC) and will form the level 3 Distinguish name as per CBPR Rules : ou=last 3 chars from BIC11 or xxx if BIC8 or 9, converted to smalls, o=BIC8(converted to small cases), o=swift DefaultDNLevel2 : this will consider the To/From Address ( this is expected to be a BIC) and will form the level 2 Distinguish name using the following rule: o=BIC8( converted to small cases), o=swift Cannot be used at same time with Distinguish Name |
| 12 | `DE.DNR.DISTINGUISH.NAME` | `DeDistinguishNameRules_DistinguishName` | TField |  | The distinguish name to be used Validation Rules: Cannot be used at same time with Distinguish Name Rule |
| 13 | `DE.DNR.STATUS` | `DeDistinguishNameRules_Status` | TField |  | Indicates Status of Distinguished Rules Validation Rules: Allowed Values:Acttive,Cancelled,Expired Status will be Active by default If the rule has an end date and the date is crossed the system will mark the rule as Expired |
| 14 | `DE.DNR.LOCAL.REF` | `DeDistinguishNameRules_LocalRef` |  |  |  |
| 15 | `DE.DNR.OVERRIDE` | `DeDistinguishNameRules_Override` |  |  |  |
| 16 | `DE.DNR.RECORD.STATUS` | `DeDistinguishNameRules_RecordStatus` | String |  |  |
| 17 | `DE.DNR.CURR.NO` | `DeDistinguishNameRules_CurrNo` | String |  |  |
| 18 | `DE.DNR.INPUTTER` | `DeDistinguishNameRules_Inputter` |  |  |  |
| 19 | `DE.DNR.DATE.TIME` | `DeDistinguishNameRules_DateTime` |  |  |  |
| 20 | `DE.DNR.AUTHORISER` | `DeDistinguishNameRules_Authoriser` | String |  |  |
| 21 | `DE.DNR.CO.CODE` | `DeDistinguishNameRules_CoCode` | String |  |  |
| 22 | `DE.DNR.DEPT.CODE` | `DeDistinguishNameRules_DeptCode` | String |  |  |
| 23 | `DE.DNR.AUDITOR.CODE` | `DeDistinguishNameRules_AuditorCode` | String |  |  |
| 24 | `DE.DNR.AUDIT.DATE.TIME` | `DeDistinguishNameRules_AuditDateTime` | String |  |  |
| 25 | `DE.DNR.RELEASE` | `DeDistinguishNameRules_Release` | TField |  | In order to activate the rule book changes and expire the old configurations, a new RELEASE field is introduced. The rule is active and applies to any rulebook if the Release field is blank. The rule is ignored if the Release field is not equal to the Current Release field in the SWIFT.PARAMETER for the corresponding DE.CARRIER. The Delivery framework will have the ability to consider the records that either contain the current release (Release field equal to the Current Release in SWIFT.PARAMETER) or those which have the Release field as blank. Once the Current Release is changed in the SWIFT.PARAMETER; the records with the Release equal to the Previous Release of SWIFT.PARAMETER will be moved to History. Validation Rules: Should be a valid year. |
