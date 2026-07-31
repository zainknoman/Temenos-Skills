# AA.SIMULATION.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.SIMULATION.TYPE` in `AA_Quotation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ST.NAME` | `AaSimulationType_Name` |  |  |  |
| 2 | `AA.ST.DESCRIPTION` | `AaSimulationType_Description` |  |  |  |
| 3 | `AA.ST.PRODUCT.LINE` | `AaSimulationType_ProductLine` | TField | Yes | Simulation Type defined only applies to the ProductLine defined in this field. Mandatory field |
| 4 | `AA.ST.ACTIVITY` | `AaSimulationType_Activity` | TField | Yes | The activity that is associated with the Simulation Type, i.e. when the activity that will be processed when the Simulation Type is included in the scenario in the Quotation Class. Mandatory field. |
| 5 | `AA.ST.RESERVED.10` | `AaSimulationType_Reserved10` | TField |  |  |
| 6 | `AA.ST.RESERVED.9` | `AaSimulationType_Reserved9` | TField |  |  |
| 7 | `AA.ST.RESERVED.8` | `AaSimulationType_Reserved8` | TField |  |  |
| 8 | `AA.ST.RESERVED.7` | `AaSimulationType_Reserved7` | TField |  |  |
| 9 | `AA.ST.RESERVED.6` | `AaSimulationType_Reserved6` | TField |  |  |
| 10 | `AA.ST.INPUT` | `AaSimulationType_Input` |  |  |  |
| 11 | `AA.ST.INPUT.MANDATORY` | `AaSimulationType_InputMandatory` |  |  |  |
| 12 | `AA.ST.MAP.TO.AAA.FIELD` | `AaSimulationType_MapToAaaField` |  |  |  |
| 13 | `AA.ST.MAP.TO.PROPERTY` | `AaSimulationType_MapToProperty` |  |  |  |
| 14 | `AA.ST.MAP.TO.PROPERTY.FIELD` | `AaSimulationType_MapToPropertyField` |  |  |  |
| 15 | `AA.ST.RESERVED.5` | `AaSimulationType_Reserved5` | TField |  |  |
| 16 | `AA.ST.RESERVED.4` | `AaSimulationType_Reserved4` | TField |  |  |
| 17 | `AA.ST.RESERVED.3` | `AaSimulationType_Reserved3` | TField |  |  |
| 18 | `AA.ST.RESERVED.2` | `AaSimulationType_Reserved2` | TField |  |  |
| 19 | `AA.ST.RESERVED.1` | `AaSimulationType_Reserved1` | TField |  |  |
| 20 | `AA.ST.LOCAL.REF` | `AaSimulationType_LocalRef` |  |  |  |
| 21 | `AA.ST.OVERRIDE` | `AaSimulationType_Override` |  |  |  |
| 22 | `AA.ST.RECORD.STATUS` | `AaSimulationType_RecordStatus` | String |  |  |
| 23 | `AA.ST.CURR.NO` | `AaSimulationType_CurrNo` | String |  |  |
| 24 | `AA.ST.INPUTTER` | `AaSimulationType_Inputter` |  |  |  |
| 25 | `AA.ST.DATE.TIME` | `AaSimulationType_DateTime` |  |  |  |
| 26 | `AA.ST.AUTHORISER` | `AaSimulationType_Authoriser` | String |  |  |
| 27 | `AA.ST.CO.CODE` | `AaSimulationType_CoCode` | String |  |  |
| 28 | `AA.ST.DEPT.CODE` | `AaSimulationType_DeptCode` | String |  |  |
| 29 | `AA.ST.AUDITOR.CODE` | `AaSimulationType_AuditorCode` | String |  |  |
| 30 | `AA.ST.AUDIT.DATE.TIME` | `AaSimulationType_AuditDateTime` | String |  |  |
