# EV.UPDATE.REQUIREMENT.STATUS — Table Schema

> Source: `INSERTS/I_F.EV.UPDATE.REQUIREMENT.STATUS` in `EV_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EV.URS.ACTIVITY` | `EvUpdateRequirementStatus_Activity` | TField | Yes | To specify the activity being processed on the arrangement. Validation Rules: 1. Mandatory field. 2. Must be a valid record from AA.CLASS.TYPE.ACTIVITY. |
| 2 | `EV.URS.REQUIREMENT.STATUS.ID` | `EvUpdateRequirementStatus_RequirementStatusId` | TField |  | To specify the arrangement reference for which the activity is performed. |
| 3 | `EV.URS.EFFECTIVE.DATE` | `EvUpdateRequirementStatus_EffectiveDate` | TField |  | To specify the effective date of the activity being processed. If this is not given, the system date is defaulted. Validation Rules: A standard T24 date field. |
| 4 | `EV.URS.PROCESS.MODE` | `EvUpdateRequirementStatus_ProcessMode` | TField |  | To specify the mode in which the activity is performed. The possible values are: UPDATE - For new evidence request or update for the existing evidence requirements. AMEND - To update evidence requirement for an arrangement retaining the previous requirements. REVERSE - To reverse the evidence requirements DUE - To request a single event based evidence requirement when the event happens. |
| 5 | `EV.URS.EVIDENCE.REQUIREMENT` | `EvUpdateRequirementStatus_EvidenceRequirement` |  |  |  |
| 6 | `EV.URS.RELATED.REQUIREMENT` | `EvUpdateRequirementStatus_RelatedRequirement` |  |  |  |
| 7 | `EV.URS.START.DATE` | `EvUpdateRequirementStatus_StartDate` |  |  |  |
| 8 | `EV.URS.STATUS` | `EvUpdateRequirementStatus_Status` |  |  |  |
| 9 | `EV.URS.FREQUENCY` | `EvUpdateRequirementStatus_Frequency` |  |  |  |
| 10 | `EV.URS.GRACE.DATE` | `EvUpdateRequirementStatus_GraceDate` |  |  |  |
| 11 | `EV.URS.OPERAND` | `EvUpdateRequirementStatus_Operand` |  |  |  |
| 12 | `EV.URS.VALUE` | `EvUpdateRequirementStatus_Value` |  |  |  |
| 13 | `EV.URS.NOTES` | `EvUpdateRequirementStatus_Notes` |  |  |  |
| 14 | `EV.URS.RESERVED.10` | `EvUpdateRequirementStatus_Reserved10` |  |  |  |
| 15 | `EV.URS.RESERVED.9` | `EvUpdateRequirementStatus_Reserved9` |  |  |  |
| 16 | `EV.URS.RESERVED.8` | `EvUpdateRequirementStatus_Reserved8` |  |  |  |
| 17 | `EV.URS.RESERVED.7` | `EvUpdateRequirementStatus_Reserved7` |  |  |  |
| 18 | `EV.URS.RESERVED.6` | `EvUpdateRequirementStatus_Reserved6` |  |  |  |
| 19 | `EV.URS.CUSTOMER` | `EvUpdateRequirementStatus_Customer` |  |  |  |
| 20 | `EV.URS.DATE.CONVENTION` | `EvUpdateRequirementStatus_DateConvention` | TField |  | Holds the date convention method which is used to cycle the next frequency date would be defaulted from evidence requirement if not passed by the external module. |
| 21 | `EV.URS.BUS.DAY.CENTRE` | `EvUpdateRequirementStatus_BusDayCentre` |  |  |  |
| 22 | `EV.URS.RESERVED.5` | `EvUpdateRequirementStatus_Reserved5` | TField |  |  |
| 23 | `EV.URS.RESERVED.4` | `EvUpdateRequirementStatus_Reserved4` | TField |  |  |
| 24 | `EV.URS.RESERVED.3` | `EvUpdateRequirementStatus_Reserved3` | TField |  |  |
| 25 | `EV.URS.RESERVED.2` | `EvUpdateRequirementStatus_Reserved2` | TField |  |  |
| 26 | `EV.URS.RESERVED.1` | `EvUpdateRequirementStatus_Reserved1` | TField |  |  |
| 27 | `EV.URS.LOCAL.REF` | `EvUpdateRequirementStatus_LocalRef` |  |  |  |
| 28 | `EV.URS.OVERRIDE` | `EvUpdateRequirementStatus_Override` |  |  |  |
| 29 | `EV.URS.RECORD.STATUS` | `EvUpdateRequirementStatus_RecordStatus` | String |  |  |
| 30 | `EV.URS.CURR.NO` | `EvUpdateRequirementStatus_CurrNo` | String |  |  |
| 31 | `EV.URS.INPUTTER` | `EvUpdateRequirementStatus_Inputter` |  |  |  |
| 32 | `EV.URS.DATE.TIME` | `EvUpdateRequirementStatus_DateTime` |  |  |  |
| 33 | `EV.URS.AUTHORISER` | `EvUpdateRequirementStatus_Authoriser` | String |  |  |
| 34 | `EV.URS.CO.CODE` | `EvUpdateRequirementStatus_CoCode` | String |  |  |
| 35 | `EV.URS.DEPT.CODE` | `EvUpdateRequirementStatus_DeptCode` | String |  |  |
| 36 | `EV.URS.AUDITOR.CODE` | `EvUpdateRequirementStatus_AuditorCode` | String |  |  |
| 37 | `EV.URS.AUDIT.DATE.TIME` | `EvUpdateRequirementStatus_AuditDateTime` | String |  |  |
| 38 | `EV.URS.END.DATE` | `EvUpdateRequirementStatus_EndDate` |  |  |  |
| 39 | `EV.URS.NOTICE.DAYS` | `EvUpdateRequirementStatus_NoticeDays` |  |  |  |
| 40 | `EV.URS.AMENDMENT.DATE` | `EvUpdateRequirementStatus_AmendmentDate` |  |  |  |
| 41 | `EV.URS.ACTUAL.START.DATE` | `EvUpdateRequirementStatus_ActualStartDate` |  |  |  |
| 42 | `EV.URS.BASE.DATE` | `EvUpdateRequirementStatus_BaseDate` |  |  |  |
| 43 | `EV.URS.DATE.ADJUSTMENT` | `EvUpdateRequirementStatus_DateAdjustment` | TField |  | Date Adjustment represents whether the system should consider the adjusted date or unadjusted date while scheduling an event. This is passed from the external module. The possible values are : 1. Value - Unadjusted date to be considered. 2. Period - Adjusted date to be considered. |
| 44 | `EV.URS.ACTION` | `EvUpdateRequirementStatus_Action` |  |  |  |
