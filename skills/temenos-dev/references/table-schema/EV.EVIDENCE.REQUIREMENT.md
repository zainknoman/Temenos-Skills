# EV.EVIDENCE.REQUIREMENT — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.REQUIREMENT` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVR.DESCRIPTION` | `EvEvidenceRequirement_Description` |  |  |  |
| 2 | `EV.EVR.FULL.DESC` | `EvEvidenceRequirement_FullDesc` | TField |  | The full description of the Evidence requirement. |
| 3 | `EV.EVR.REQUIREMENT.TYPE` | `EvEvidenceRequirement_RequirementType` | TField |  | The type of requirement that the evidence requirement has to be processed. The possible values are : SINGLE - To specify a single Evidence application. RULES - To specify multiple Evidences separated by boolean operation. RELATED.REQUIREMENT - To specify a related requirement which will act as main requirement. DATA.ELEMENT.RULE - To specify a data element criteria. |
| 4 | `EV.EVR.RULE` | `EvEvidenceRequirement_Rule` | TField |  | Rules will be defined to satisfy each requirement. Rules are defined using evidence types combined with Boolean operators |
| 5 | `EV.EVR.RELATED.REQUIREMENT` | `EvEvidenceRequirement_RelatedRequirement` | TField |  | The related requirement of the given evidence requirement. This is the requirement on which the data element rule is applied. |
| 6 | `EV.EVR.DATA.ELEMENT` | `EvEvidenceRequirement_DataElement` | TField |  | The compliance rule on the data elements of related requirements. Example � RETURN.ON.EQUITY &gt;= 30 RETURN.ON.EQUITY is an AA.DATA.ELEMENT record id where the data source is indicated. Validation will be made to check whether the data element belongs the evidence type of the related requirement. Data operand and value will be supplied by servicing application. |
| 7 | `EV.EVR.REVIEW.TYPE` | `EvEvidenceRequirement_ReviewType` | TField | Yes | Accepts the value Periodic or Event if set to periodic then the field REQUIREMENT.FREQUENCY becomes mandatory |
| 8 | `EV.EVR.REVIEW.FREQUENCY` | `EvEvidenceRequirement_ReviewFrequency` | TField |  | Allows to define frequency for the evidence requirement is the requirement is periodic |
| 9 | `EV.EVR.NOTICE.DAYS` | `EvEvidenceRequirement_NoticeDays` | TField |  | Number of days before the next due frequency prior to which the upcoming due covenant reports has to be generated. |
| 10 | `EV.EVR.GRACE.DAYS` | `EvEvidenceRequirement_GraceDays` | TField |  | Number of days after which the evidence requirement is expected to become overdue. |
| 11 | `EV.EVR.RESERVED.4` | `EvEvidenceRequirement_Reserved4` | TField |  |  |
| 12 | `EV.EVR.RESERVED.3` | `EvEvidenceRequirement_Reserved3` | TField |  |  |
| 13 | `EV.EVR.RESERVED.2` | `EvEvidenceRequirement_Reserved2` | TField |  |  |
| 14 | `EV.EVR.RESERVED.1` | `EvEvidenceRequirement_Reserved1` | TField |  |  |
| 15 | `EV.EVR.LOCAL.REF` | `EvEvidenceRequirement_LocalRef` |  |  |  |
| 16 | `EV.EVR.RECORD.STATUS` | `EvEvidenceRequirement_RecordStatus` | String |  |  |
| 17 | `EV.EVR.CURR.NO` | `EvEvidenceRequirement_CurrNo` | String |  |  |
| 18 | `EV.EVR.INPUTTER` | `EvEvidenceRequirement_Inputter` |  |  |  |
| 19 | `EV.EVR.DATE.TIME` | `EvEvidenceRequirement_DateTime` |  |  |  |
| 20 | `EV.EVR.AUTHORISER` | `EvEvidenceRequirement_Authoriser` | String |  |  |
| 21 | `EV.EVR.CO.CODE` | `EvEvidenceRequirement_CoCode` | String |  |  |
| 22 | `EV.EVR.DEPT.CODE` | `EvEvidenceRequirement_DeptCode` | String |  |  |
| 23 | `EV.EVR.AUDITOR.CODE` | `EvEvidenceRequirement_AuditorCode` | String |  |  |
| 24 | `EV.EVR.AUDIT.DATE.TIME` | `EvEvidenceRequirement_AuditDateTime` | String |  |  |
| 25 | `EV.EVR.REQUIREMENT.CATEGORY` | `EvEvidenceRequirement_RequirementCategory` | TField |  | This field allows to group the evidence requirement by category. Refers to EB.LOOKUP |
| 26 | `EV.EVR.COMPLEX.DATA.ELEMENT` | `EvEvidenceRequirement_ComplexDataElement` | TField |  | Used to specify complex data element rule for related requirements .It will support calculations by combining two or more data element�s value. |
