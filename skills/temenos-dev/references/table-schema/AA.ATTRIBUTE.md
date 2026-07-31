# AA.ATTRIBUTE — Table Schema

> Source: `INSERTS/I_F.AA.ATTRIBUTE` in `AA_Rules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ATR.DESCRIPTION` | `AaAttribute_Description` |  |  |  |
| 2 | `AA.ATR.PROPERTY.CLASS` | `AaAttribute_PropertyClass` | TField |  | Defines the list of Property Classes. The Property Class of the attribute for which the rules are defined is chosen here. |
| 3 | `AA.ATR.ATTRIBUTE` | `AaAttribute_Attribute` | TField |  | Defines the individual attribute for which the rules are defined in the record. This should be a valid attribute of the Property Class chosen in PROPERTY.CLASS field. |
| 4 | `AA.ATR.TYPE` | `AaAttribute_Type` | TField |  | This field defines the type of AA.ATTRIBUTE record. The attribute definition can either be a default or a negotiation rule. � Default This option is chosen when the attribute value has to be defaulted for all the drawings underneath a facility. After defaulting, the attribute can or cannot be negotiated at the facility level based on the Negotiation Rules of the particular drawing product for the attribute. � Negotiation Rule This option is chosen when a negotiation condition for the attribute is defined at the facility. When creating drawings, the condition here will be applied along with the product negotiation rule to the particular attributes. |
| 5 | `AA.ATR.NEGOTIATION.CONDITION` | `AaAttribute_NegotiationCondition` | TField |  | Defines the negotiation condition for the attribute specified. The condition should be a valid condition for the data type of the attribute. |
| 6 | `AA.ATR.ATTRIBUTE.RULE` | `AaAttribute_AttributeRule` | TField |  | Defines the rule for which this AA.ATTRIBUTE record is valid for. The rule should be defined in the following manner FIELD.NAME &lt;operator&gt; "VALUE". The field name should be a valid field of the PROPERTY.CLASS. For example, if the attribute record is valid only for a Periodic Interest then the condition should be as follows RATE.TYPE == "PERIODIC". |
| 7 | `AA.ATR.VALUE` | `AaAttribute_Value` | TField | No | Defines the value for the attribute. This is an optional field. This value will be defaulted at the Facility Sub arrangement condition if given. |
| 8 | `AA.ATR.MESSAGE` | `AaAttribute_Message` | TField |  | This field indicates the outcome when the negotiation rule is broken. Allows only two values ERROR or OVERRIDE. 1. ERROR When this option is chosen an error message is raised during the rule break. 2. OVERRIDE When this option is chosen only an override is thrown if the rule is broken. |
| 9 | `AA.ATR.OVERRIDE` | `AaAttribute_Override` |  |  |  |
| 10 | `AA.ATR.RECORD.STATUS` | `AaAttribute_RecordStatus` | String |  |  |
| 11 | `AA.ATR.CURR.NO` | `AaAttribute_CurrNo` | String |  |  |
| 12 | `AA.ATR.INPUTTER` | `AaAttribute_Inputter` |  |  |  |
| 13 | `AA.ATR.DATE.TIME` | `AaAttribute_DateTime` |  |  |  |
| 14 | `AA.ATR.AUTHORISER` | `AaAttribute_Authoriser` | String |  |  |
| 15 | `AA.ATR.CO.CODE` | `AaAttribute_CoCode` | String |  |  |
| 16 | `AA.ATR.DEPT.CODE` | `AaAttribute_DeptCode` | String |  |  |
| 17 | `AA.ATR.AUDITOR.CODE` | `AaAttribute_AuditorCode` | String |  |  |
| 18 | `AA.ATR.AUDIT.DATE.TIME` | `AaAttribute_AuditDateTime` | String |  |  |
