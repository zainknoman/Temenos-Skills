# IF.OUTWARD.DESIGN.LANDING — Table Schema

> Source: `INSERTS/I_F.IF.OUTWARD.DESIGN.LANDING` in `IF_FlowCatalog.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.LT.SOURCE.TYPE` | `IfOutwardDesignLanding_SourceType` | TField |  | Overview This is a no input field used to record the type of the flow source. The flow could be originated from different sources of types Versions, Applications, TSA Service, Component Services, AA, Banking Framework or Inflow. Validation Rules This is a no-input field. |
| 2 | `IF.LT.SOURCE.NAME` | `IfOutwardDesignLanding_SourceName` | TField |  | Overview This is a no input field that holds the source where the flow is attached to. The source could be a Versions, Applications, TSA Service or Component Service. Validation Rules This is a no-input field. |
| 3 | `IF.LT.FLOW.ATTRIBUTES` | `IfOutwardDesignLanding_FlowAttributes` |  |  |  |
| 4 | `IF.LT.EVENT.PRIORITY` | `IfOutwardDesignLanding_EventPriority` | TField |  | Overview This field holds the priority of an event record provided while defining the flow in Event Designer. Validation Rules Only numeric values are allowed. |
| 5 | `IF.LT.QUEUE.NAME` | `IfOutwardDesignLanding_QueueName` | TField |  | Overview This field allows events to be delivered to a specific queue.This field holds the destination to deliver the events. Validation Rules If the flow attribute is WRITE.TO.QUEUE or RAW.XML then the queue name must be provided. This represents the queue to which the Raw IF Event would be posted when using direct posting. |
| 6 | `IF.LT.COMPANIES.LIST` | `IfOutwardDesignLanding_CompaniesList` |  |  |  |
| 7 | `IF.LT.EXIT.POINT.NAME` | `IfOutwardDesignLanding_ExitPointName` |  |  |  |
| 8 | `IF.LT.OVERRIDE.CODES` | `IfOutwardDesignLanding_OverrideCodes` |  |  |  |
| 9 | `IF.LT.EXIT.POINT.SOURCE` | `IfOutwardDesignLanding_ExitPointSource` |  |  |  |
| 10 | `IF.LT.RESERVED.1` | `IfOutwardDesignLanding_Reserved1` |  |  |  |
| 11 | `IF.LT.RESERVED.2` | `IfOutwardDesignLanding_Reserved2` |  |  |  |
| 12 | `IF.LT.RESERVED.3` | `IfOutwardDesignLanding_Reserved3` |  |  |  |
| 13 | `IF.LT.RESERVED.4` | `IfOutwardDesignLanding_Reserved4` |  |  |  |
| 14 | `IF.LT.RESERVED.5` | `IfOutwardDesignLanding_Reserved5` |  |  |  |
| 15 | `IF.LT.RESERVED.6` | `IfOutwardDesignLanding_Reserved6` |  |  |  |
| 16 | `IF.LT.RESERVED.7` | `IfOutwardDesignLanding_Reserved7` |  |  |  |
| 17 | `IF.LT.RESERVED.8` | `IfOutwardDesignLanding_Reserved8` |  |  |  |
| 18 | `IF.LT.RESERVED.9` | `IfOutwardDesignLanding_Reserved9` |  |  |  |
| 19 | `IF.LT.RESERVED.10` | `IfOutwardDesignLanding_Reserved10` |  |  |  |
| 20 | `IF.LT.FIELD.SOURCE` | `IfOutwardDesignLanding_FieldSource` |  |  |  |
| 21 | `IF.LT.FIELD.NAME` | `IfOutwardDesignLanding_FieldName` |  |  |  |
| 22 | `IF.LT.JOIN.DEFN` | `IfOutwardDesignLanding_JoinDefn` |  |  |  |
| 23 | `IF.LT.API.MAPPING` | `IfOutwardDesignLanding_ApiMapping` |  |  |  |
| 24 | `IF.LT.FIELD.TYPE` | `IfOutwardDesignLanding_FieldType` |  |  |  |
| 25 | `IF.LT.FIELD.XML.NAME` | `IfOutwardDesignLanding_FieldXmlName` |  |  |  |
| 26 | `IF.LT.OPERATION.NAME` | `IfOutwardDesignLanding_OperationName` |  |  |  |
| 27 | `IF.LT.INPUT.NAME` | `IfOutwardDesignLanding_InputName` |  |  |  |
| 28 | `IF.LT.FLOW.FIELDS` | `IfOutwardDesignLanding_FlowFields` |  |  |  |
| 29 | `IF.LT.RESERVED.14` | `IfOutwardDesignLanding_Reserved14` |  |  |  |
| 30 | `IF.LT.OUTPUT.NAME` | `IfOutwardDesignLanding_OutputName` |  |  |  |
| 31 | `IF.LT.RESERVED.16` | `IfOutwardDesignLanding_Reserved16` |  |  |  |
| 32 | `IF.LT.RESERVED.17` | `IfOutwardDesignLanding_Reserved17` |  |  |  |
| 33 | `IF.LT.PARAM.NAME` | `IfOutwardDesignLanding_ParamName` |  |  |  |
| 34 | `IF.LT.PARAM.DIRECTION` | `IfOutwardDesignLanding_ParamDirection` |  |  |  |
| 35 | `IF.LT.PARAM.TYPE` | `IfOutwardDesignLanding_ParamType` |  |  |  |
| 36 | `IF.LT.CORRELATION.ID.FIELD` | `IfOutwardDesignLanding_CorrelationIdField` | TField |  |  |
| 37 | `IF.LT.FLOW.DESCRIPTION` | `IfOutwardDesignLanding_FlowDescription` | TField |  |  |
| 38 | `IF.LT.RESERVED.23` | `IfOutwardDesignLanding_Reserved23` | TField |  |  |
| 39 | `IF.LT.RESERVED.24` | `IfOutwardDesignLanding_Reserved24` | TField |  |  |
| 40 | `IF.LT.RESERVED.25` | `IfOutwardDesignLanding_Reserved25` | TField |  |  |
| 41 | `IF.LT.RESERVED.26` | `IfOutwardDesignLanding_Reserved26` | TField |  |  |
| 42 | `IF.LT.RESERVED.27` | `IfOutwardDesignLanding_Reserved27` | TField |  |  |
| 43 | `IF.LT.RESERVED.28` | `IfOutwardDesignLanding_Reserved28` | TField |  |  |
| 44 | `IF.LT.RESERVED.29` | `IfOutwardDesignLanding_Reserved29` | TField |  |  |
| 45 | `IF.LT.RESERVED.30` | `IfOutwardDesignLanding_Reserved30` | TField |  |  |
| 46 | `IF.LT.OVERRIDE` | `IfOutwardDesignLanding_Override` |  |  |  |
| 47 | `IF.LT.RECORD.STATUS` | `IfOutwardDesignLanding_RecordStatus` | String |  |  |
| 48 | `IF.LT.CURR.NO` | `IfOutwardDesignLanding_CurrNo` | String |  |  |
| 49 | `IF.LT.INPUTTER` | `IfOutwardDesignLanding_Inputter` |  |  |  |
| 50 | `IF.LT.DATE.TIME` | `IfOutwardDesignLanding_DateTime` |  |  |  |
| 51 | `IF.LT.AUTHORISER` | `IfOutwardDesignLanding_Authoriser` | String |  |  |
| 52 | `IF.LT.CO.CODE` | `IfOutwardDesignLanding_CoCode` | String |  |  |
| 53 | `IF.LT.DEPT.CODE` | `IfOutwardDesignLanding_DeptCode` | String |  |  |
| 54 | `IF.LT.AUDITOR.CODE` | `IfOutwardDesignLanding_AuditorCode` | String |  |  |
| 55 | `IF.LT.AUDIT.DATE.TIME` | `IfOutwardDesignLanding_AuditDateTime` | String |  |  |
| 56 | `IF.LT.FIELD.DESCRIPTION` | `IfOutwardDesignLanding_FieldDescription` |  |  |  |
