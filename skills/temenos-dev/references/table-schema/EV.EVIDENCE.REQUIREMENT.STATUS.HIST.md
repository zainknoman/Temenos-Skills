# EV.EVIDENCE.REQUIREMENT.STATUS.HIST — Table Schema

> Source: `INSERTS/I_F.EV.EVIDENCE.REQUIREMENT.STATUS.HIST` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.EVRSH.EVIDENCE.REQUIREMENT` | `EvEvidenceRequirementStatusHist_EvidenceRequirement` |  |  |  |
| 2 | `EV.EVRSH.SOURCE` | `EvEvidenceRequirementStatusHist_Source` |  |  |  |
| 3 | `EV.EVRSH.STATUS` | `EvEvidenceRequirementStatusHist_Status` |  |  |  |
| 4 | `EV.EVRSH.EVIDENCE.TYPE` | `EvEvidenceRequirementStatusHist_EvidenceType` |  |  |  |
| 5 | `EV.EVRSH.EVIDENCE` | `EvEvidenceRequirementStatusHist_Evidence` |  |  |  |
| 6 | `EV.EVRSH.EVIDENCE.STATUS` | `EvEvidenceRequirementStatusHist_EvidenceStatus` |  |  |  |
| 7 | `EV.EVRSH.RESERVED.1` | `EvEvidenceRequirementStatusHist_Reserved1` |  |  |  |
| 8 | `EV.EVRSH.VERIFIED` | `EvEvidenceRequirementStatusHist_Verified` |  |  |  |
| 9 | `EV.EVRSH.EVIDENCE.OWNER` | `EvEvidenceRequirementStatusHist_EvidenceOwner` |  |  |  |
| 10 | `EV.EVRSH.EVIDENCE.ATTRIBUTE` | `EvEvidenceRequirementStatusHist_EvidenceAttribute` |  |  |  |
| 11 | `EV.EVRSH.RELATED.REQUIREMENT` | `EvEvidenceRequirementStatusHist_RelatedRequirement` |  |  |  |
| 12 | `EV.EVRSH.DATA.ELEMENT` | `EvEvidenceRequirementStatusHist_DataElement` |  |  |  |
| 13 | `EV.EVRSH.OPERAND` | `EvEvidenceRequirementStatusHist_Operand` |  |  |  |
| 14 | `EV.EVRSH.VALUE` | `EvEvidenceRequirementStatusHist_Value` |  |  |  |
| 15 | `EV.EVRSH.REQUIREMENT.FREQUENCY` | `EvEvidenceRequirementStatusHist_RequirementFrequency` |  |  |  |
| 16 | `EV.EVRSH.GRACE.DAYS.UNTIL` | `EvEvidenceRequirementStatusHist_GraceDaysUntil` |  |  |  |
| 17 | `EV.EVRSH.STATUS.DATE` | `EvEvidenceRequirementStatusHist_StatusDate` |  |  |  |
| 18 | `EV.EVRSH.DATE.CONVENTION` | `EvEvidenceRequirementStatusHist_DateConvention` | TField |  |  |
| 19 | `EV.EVRSH.BUS.DAY.CENTRE` | `EvEvidenceRequirementStatusHist_BusDayCentre` |  |  |  |
| 20 | `EV.EVRSH.CUSTOMER` | `EvEvidenceRequirementStatusHist_Customer` |  |  |  |
| 21 | `EV.EVRSH.REQUIREMENT.CATEGORY` | `EvEvidenceRequirementStatusHist_RequirementCategory` |  |  |  |
| 22 | `EV.EVRSH.START.DATE` | `EvEvidenceRequirementStatusHist_StartDate` |  |  |  |
| 23 | `EV.EVRSH.END.DATE` | `EvEvidenceRequirementStatusHist_EndDate` |  |  |  |
| 24 | `EV.EVRSH.NOTICE.DAYS` | `EvEvidenceRequirementStatusHist_NoticeDays` |  |  |  |
| 25 | `EV.EVRSH.AMENDMENT.DATE` | `EvEvidenceRequirementStatusHist_AmendmentDate` |  |  |  |
| 26 | `EV.EVRSH.COMPLEX.DATA.ELEMENT` | `EvEvidenceRequirementStatusHist_ComplexDataElement` |  |  |  |
| 27 | `EV.EVRSH.ACTUAL.START.DATE` | `EvEvidenceRequirementStatusHist_ActualStartDate` |  |  |  |
| 28 | `EV.EVRSH.BASE.DATE` | `EvEvidenceRequirementStatusHist_BaseDate` |  |  |  |
| 29 | `EV.EVRSH.ACTUAL.DATE` | `EvEvidenceRequirementStatusHist_ActualDate` |  |  |  |
| 30 | `EV.EVRSH.LAST.DATE` | `EvEvidenceRequirementStatusHist_LastDate` |  |  |  |
| 31 | `EV.EVRSH.ACTIVE.DATA.ELEMENT` | `EvEvidenceRequirementStatusHist_ActiveDataElement` |  |  |  |
| 32 | `EV.EVRSH.ACTIVE.COMPLEX.DATA.ELEMENT` | `EvEvidenceRequirementStatusHist_ActiveComplexDataElement` |  |  |  |
| 33 | `EV.EVRSH.ACTIVE.OPERAND` | `EvEvidenceRequirementStatusHist_ActiveOperand` |  |  |  |
| 34 | `EV.EVRSH.ACTIVE.VALUE` | `EvEvidenceRequirementStatusHist_ActiveValue` |  |  |  |
| 35 | `EV.EVRSH.ACTIVE.START.DATE` | `EvEvidenceRequirementStatusHist_ActiveStartDate` |  |  |  |
| 36 | `EV.EVRSH.ACTIVE.END.DATE` | `EvEvidenceRequirementStatusHist_ActiveEndDate` |  |  |  |
| 37 | `EV.EVRSH.ACTIVE.NOTICE.DAYS` | `EvEvidenceRequirementStatusHist_ActiveNoticeDays` |  |  |  |
| 38 | `EV.EVRSH.ACTIVE.ACTUAL.START.DATE` | `EvEvidenceRequirementStatusHist_ActiveActualStartDate` |  |  |  |
| 39 | `EV.EVRSH.ACTIVE.BASE.DATE` | `EvEvidenceRequirementStatusHist_ActiveBaseDate` |  |  |  |
| 40 | `EV.EVRSH.ACTIVE.REQUIREMENT.FREQUENCY` | `EvEvidenceRequirementStatusHist_ActiveRequirementFrequency` |  |  |  |
| 41 | `EV.EVRSH.LINKED.STATUS.ID` | `EvEvidenceRequirementStatusHist_LinkedStatusId` | TField |  |  |
| 42 | `EV.EVRSH.DATE.ADJUSTMENT` | `EvEvidenceRequirementStatusHist_DateAdjustment` | TField |  |  |
