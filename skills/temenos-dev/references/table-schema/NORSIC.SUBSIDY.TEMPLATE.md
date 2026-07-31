# NORSIC.SUBSIDY.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.NORSIC.SUBSIDY.TEMPLATE` in `NORSIC_SubsidyInterestCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORSUB.DESCRIPTION` | `NorsicSubsidyTemplate_Description` |  |  |  |
| 2 | `NORSUB.DEDUCTIBLE.RATE` | `NorsicSubsidyTemplate_DeductibleRate` | TField |  | It is used to define the interest rate paid by the state treasury of interest exceeding interest rate. |
| 3 | `NORSUB.LOAN.YEAR` | `NorsicSubsidyTemplate_LoanYear` |  |  |  |
| 4 | `NORSUB.SUBSIDY.PERCENTAGE` | `NorsicSubsidyTemplate_SubsidyPercentage` |  |  |  |
| 5 | `NORSUB.EXPIRY.DATE` | `NorsicSubsidyTemplate_ExpiryDate` | TField |  | This field will hold the expiry date of the current interest subsidy template. |
| 6 | `NORSUB.SUBSIDY.MAX.RATE` | `NorsicSubsidyTemplate_SubsidyMaxRate` | TField |  | This field will hold the maximum interest rate. |
| 7 | `NORSUB.LOCAL.REF` | `NorsicSubsidyTemplate_LocalRef` |  |  |  |
| 8 | `NORSUB.OVERRIDE` | `NorsicSubsidyTemplate_Override` |  |  |  |
| 9 | `NORSUB.RECORD.STATUS` | `NorsicSubsidyTemplate_RecordStatus` | String |  |  |
| 10 | `NORSUB.CURR.NO` | `NorsicSubsidyTemplate_CurrNo` | String |  |  |
| 11 | `NORSUB.INPUTTER` | `NorsicSubsidyTemplate_Inputter` |  |  |  |
| 12 | `NORSUB.DATE.TIME` | `NorsicSubsidyTemplate_DateTime` |  |  |  |
| 13 | `NORSUB.AUTHORISER` | `NorsicSubsidyTemplate_Authoriser` | String |  |  |
| 14 | `NORSUB.CO.CODE` | `NorsicSubsidyTemplate_CoCode` | String |  |  |
| 15 | `NORSUB.DEPT.CODE` | `NorsicSubsidyTemplate_DeptCode` | String |  |  |
| 16 | `NORSUB.AUDITOR.CODE` | `NorsicSubsidyTemplate_AuditorCode` | String |  |  |
| 17 | `NORSUB.AUDIT.DATE.TIME` | `NorsicSubsidyTemplate_AuditDateTime` | String |  |  |
