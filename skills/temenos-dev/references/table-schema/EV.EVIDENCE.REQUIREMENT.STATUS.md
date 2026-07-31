# EV.EVIDENCE.REQUIREMENT.STATUS — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.REQUIREMENT.STATUS` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVRS.EVIDENCE.REQUIREMENT` | `EvEvidenceRequirementStatus_EvidenceRequirement` |  |  |  |
| 2 | `EV.EVRS.SOURCE` | `EvEvidenceRequirementStatus_Source` |  |  |  |
| 3 | `EV.EVRS.STATUS` | `EvEvidenceRequirementStatus_Status` |  |  |  |
| 4 | `EV.EVRS.EVIDENCE.TYPE` | `EvEvidenceRequirementStatus_EvidenceType` |  |  |  |
| 5 | `EV.EVRS.EVIDENCE` | `EvEvidenceRequirementStatus_Evidence` |  |  |  |
| 6 | `EV.EVRS.EVIDENCE.STATUS` | `EvEvidenceRequirementStatus_EvidenceStatus` |  |  |  |
| 7 | `EV.EVRS.RESERVED.1` | `EvEvidenceRequirementStatus_Reserved1` |  |  |  |
| 8 | `EV.EVRS.VERIFIED` | `EvEvidenceRequirementStatus_Verified` |  |  |  |
| 9 | `EV.EVRS.EVIDENCE.OWNER` | `EvEvidenceRequirementStatus_EvidenceOwner` |  |  |  |
| 10 | `EV.EVRS.EVIDENCE.ATTRIBUTE` | `EvEvidenceRequirementStatus_EvidenceAttribute` |  |  |  |
| 11 | `EV.EVRS.RELATED.REQUIREMENT` | `EvEvidenceRequirementStatus_RelatedRequirement` |  |  |  |
| 12 | `EV.EVRS.DATA.ELEMENT` | `EvEvidenceRequirementStatus_DataElement` |  |  |  |
| 13 | `EV.EVRS.OPERAND` | `EvEvidenceRequirementStatus_Operand` |  |  |  |
| 14 | `EV.EVRS.VALUE` | `EvEvidenceRequirementStatus_Value` |  |  |  |
| 15 | `EV.EVRS.REQUIREMENT.FREQUENCY` | `EvEvidenceRequirementStatus_RequirementFrequency` |  |  |  |
| 16 | `EV.EVRS.GRACE.DAYS.UNTIL` | `EvEvidenceRequirementStatus_GraceDaysUntil` |  |  |  |
| 17 | `EV.EVRS.STATUS.DATE` | `EvEvidenceRequirementStatus_StatusDate` |  |  |  |
| 18 | `EV.EVRS.DATE.CONVENTION` | `EvEvidenceRequirementStatus_DateConvention` | TField |  | Holds the date convention method which is used to cycle the next frequency date would be defaulted from evidence requirement if not passed by the external module. |
| 19 | `EV.EVRS.BUS.DAY.CENTRE` | `EvEvidenceRequirementStatus_BusDayCentre` |  |  |  |
| 20 | `EV.EVRS.CUSTOMER` | `EvEvidenceRequirementStatus_Customer` |  |  |  |
| 21 | `EV.EVRS.REQUIREMENT.CATEGORY` | `EvEvidenceRequirementStatus_RequirementCategory` |  |  |  |
| 22 | `EV.EVRS.START.DATE` | `EvEvidenceRequirementStatus_StartDate` |  |  |  |
| 23 | `EV.EVRS.END.DATE` | `EvEvidenceRequirementStatus_EndDate` |  |  |  |
| 24 | `EV.EVRS.NOTICE.DAYS` | `EvEvidenceRequirementStatus_NoticeDays` |  |  |  |
| 25 | `EV.EVRS.AMENDMENT.DATE` | `EvEvidenceRequirementStatus_AmendmentDate` |  |  |  |
| 26 | `EV.EVRS.COMPLEX.DATA.ELEMENT` | `EvEvidenceRequirementStatus_ComplexDataElement` |  |  |  |
| 27 | `EV.EVRS.ACTUAL.START.DATE` | `EvEvidenceRequirementStatus_ActualStartDate` |  |  |  |
| 28 | `EV.EVRS.BASE.DATE` | `EvEvidenceRequirementStatus_BaseDate` |  |  |  |
| 29 | `EV.EVRS.ACTUAL.DATE` | `EvEvidenceRequirementStatus_ActualDate` |  |  |  |
| 30 | `EV.EVRS.LAST.DATE` | `EvEvidenceRequirementStatus_LastDate` |  |  |  |
| 31 | `EV.EVRS.ACTIVE.DATA.ELEMENT` | `EvEvidenceRequirementStatus_ActiveDataElement` |  |  |  |
| 32 | `EV.EVRS.ACTIVE.COMPLEX.DATA.ELEMENT` | `EvEvidenceRequirementStatus_ActiveComplexDataElement` |  |  |  |
| 33 | `EV.EVRS.ACTIVE.OPERAND` | `EvEvidenceRequirementStatus_ActiveOperand` |  |  |  |
| 34 | `EV.EVRS.ACTIVE.VALUE` | `EvEvidenceRequirementStatus_ActiveValue` |  |  |  |
| 35 | `EV.EVRS.ACTIVE.START.DATE` | `EvEvidenceRequirementStatus_ActiveStartDate` |  |  |  |
| 36 | `EV.EVRS.ACTIVE.END.DATE` | `EvEvidenceRequirementStatus_ActiveEndDate` |  |  |  |
| 37 | `EV.EVRS.ACTIVE.NOTICE.DAYS` | `EvEvidenceRequirementStatus_ActiveNoticeDays` |  |  |  |
| 38 | `EV.EVRS.ACTIVE.ACTUAL.START.DATE` | `EvEvidenceRequirementStatus_ActiveActualStartDate` |  |  |  |
| 39 | `EV.EVRS.ACTIVE.BASE.DATE` | `EvEvidenceRequirementStatus_ActiveBaseDate` |  |  |  |
| 40 | `EV.EVRS.ACTIVE.REQUIREMENT.FREQUENCY` | `EvEvidenceRequirementStatus_ActiveRequirementFrequency` |  |  |  |
| 41 | `EV.EVRS.LINKED.STATUS.ID` | `EvEvidenceRequirementStatus_LinkedStatusId` | TField |  | Reserved for Future use |
| 42 | `EV.EVRS.DATE.ADJUSTMENT` | `EvEvidenceRequirementStatus_DateAdjustment` | TField |  | Date Adjustment represents whether the system should consider the adjusted date or unadjusted date while scheduling an event. This is passed from the external module. The possible values are : 1. Value - Unadjusted date to be considered. 2. Period - Adjusted date to be considered. |
