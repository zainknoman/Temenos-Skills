# AA.APR.TYPE — Table Schema

> Source: `INSERTS/I_F.AA.APR.TYPE` in `AA_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AT.DESCRIPTION` | `AaAprType_Description` |  |  |  |
| 2 | `AA.AT.FULL.DESCRIPTION` | `AaAprType_FullDescription` |  |  |  |
| 3 | `AA.AT.SOURCE.TYPE` | `AaAprType_SourceType` | TField | Yes | To identify source, based on which the APR will be calculated. This will be an indicator for the system to know what are the parameters needed to calculate the APR. Allowed Values: - Cashflow - Interest Validation Rules: This is a Mandatory field. If SOURCE.TYPE is 'Interest', then CALC.API is mandatory. |
| 4 | `AA.AT.CALC.API` | `AaAprType_CalcApi` | TField |  | A user configurable routine that calculates the APR based on the source type. Validation Rules: Should be defined in EB.API. |
| 5 | `AA.AT.LOCAL.REF` | `AaAprType_LocalRef` |  |  |  |
| 6 | `AA.AT.OVERRIDE` | `AaAprType_Override` |  |  |  |
| 7 | `AA.AT.RECORD.STATUS` | `AaAprType_RecordStatus` | String |  |  |
| 8 | `AA.AT.CURR.NO` | `AaAprType_CurrNo` | String |  |  |
| 9 | `AA.AT.INPUTTER` | `AaAprType_Inputter` |  |  |  |
| 10 | `AA.AT.DATE.TIME` | `AaAprType_DateTime` |  |  |  |
| 11 | `AA.AT.AUTHORISER` | `AaAprType_Authoriser` | String |  |  |
| 12 | `AA.AT.CO.CODE` | `AaAprType_CoCode` | String |  |  |
| 13 | `AA.AT.DEPT.CODE` | `AaAprType_DeptCode` | String |  |  |
| 14 | `AA.AT.AUDITOR.CODE` | `AaAprType_AuditorCode` | String |  |  |
| 15 | `AA.AT.AUDIT.DATE.TIME` | `AaAprType_AuditDateTime` | String |  |  |
| 16 | `AA.AT.DAY.BASIS` | `AaAprType_DayBasis` | TField |  |  |
| 17 | `AA.AT.RECALC.METHOD` | `AaAprType_RecalcMethod` | TField |  | This field describes the recalculation method for the APR calculation "Validation Rules:" This field can be input only if the SOURCE.TYPE is 'Cashflow' Allowed Values: 1. Principal Outstanding - To calculate the APR based on current principal balance 2. Present Value - To calculate the APR based on net present value |
