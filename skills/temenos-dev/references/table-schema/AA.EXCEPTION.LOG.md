# AA.EXCEPTION.LOG — Table Schema

> Source: `INSERTS/I_F.AA.EXCEPTION.LOG` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.EL.ACCOUNT.ID` | `AaExceptionLog_AccountId` | TField |  |  |
| 2 | `AA.EL.AC.ALTERNATE.REF` | `AaExceptionLog_AcAlternateRef` | TField |  |  |
| 3 | `AA.EL.ACTIVITY.REF` | `AaExceptionLog_ActivityRef` |  |  |  |
| 4 | `AA.EL.ACTIVITY.ID` | `AaExceptionLog_ActivityId` |  |  |  |
| 5 | `AA.EL.EFFECTIVE.DATE` | `AaExceptionLog_EffectiveDate` |  |  |  |
| 6 | `AA.EL.SYSTEM.DATE` | `AaExceptionLog_SystemDate` |  |  |  |
| 7 | `AA.EL.ACTIVITY.FUNCTION` | `AaExceptionLog_ActivityFunction` |  |  |  |
| 8 | `AA.EL.EXCEPTION.TYPE` | `AaExceptionLog_ExceptionType` |  |  |  |
| 9 | `AA.EL.EXCEPTION.SEVERITY` | `AaExceptionLog_ExceptionSeverity` |  |  |  |
| 10 | `AA.EL.EXCEPTION.DETAILS` | `AaExceptionLog_ExceptionDetails` |  |  |  |
| 11 | `AA.EL.EXCEPTION.VALUE` | `AaExceptionLog_ExceptionValue` |  |  |  |
