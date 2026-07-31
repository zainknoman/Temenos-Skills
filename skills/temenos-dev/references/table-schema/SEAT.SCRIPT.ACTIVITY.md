# SEAT.SCRIPT.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.ACTIVITY` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.SCR.ACTY.DESCRIPTION` | `SeatScriptActivity_Description` |  |  |  |
| 2 | `SE.SCR.ACTY.SUFFIX` | `SeatScriptActivity_Suffix` |  |  |  |
| 3 | `SE.SCR.ACTY.TEST.BASE` | `SeatScriptActivity_TestBase` | TField |  | A valid record in SEAT.TESTBASE. Indicates the test base, for which the scenario has been created. |
| 4 | `SE.SCR.ACTY.UPLOAD.STATUS` | `SeatScriptActivity_UploadStatus` | TField |  | Initially will be input by the user with ACTIVE. If any error is encountered during Regression Run, will be updated with ERROR. Scripts with Status equal to ACTIVE will only be considered for upload. The Status is applicable for all the scripts under the ID. There is no provision to select single scripts. Will be updated only for the first error in the script sequence. Valid values are: ACTIVE - Will be considered for single or bulk upload PENDING, ANALYSIS, HOLD - Indicates that product teams are working on the Scenario and therefore, the scripts will NOT be considered for upload ERROR - Indicates the scenario has encountered an error. REG.SETUP - A status indicates that the error is on account of Regression Static Base. REG.ERROR - A status indicates that the error is not anything to do with the scripts or results. It is Regression error and therefore needs to be resolved by Regression team before next upload. |
| 5 | `SE.SCR.ACTY.RESULT.FILES` | `SeatScriptActivity_ResultFiles` | TField |  | Indicates the ID of SEAT.SCRIPT.RESULT.FILES that has to be considered for validating the results. Validation: The contents shall be a valid record in SEAT.SCRIPT.RESULT.FILES. Populated by the system when a record is created in SEAT.SCRIPT.RESULT.FILES with the same ID as that of SEAT.SCRIPT.ACTIVITY. Generally shall be the ID of the SEAT.SCRIPT.ACTIVITY. But when separate result files need to be defined for different test bases, can contain a suffix that is a valid record in SCRIPT.TESTBASE. The suffix, if present, will be validated against the contents in TEST.BASE field. |
| 6 | `SE.SCR.ACTY.ERROR.TRACE` | `SeatScriptActivity_ErrorTrace` |  |  |  |
| 7 | `SE.SCR.ACTY.NOTES` | `SeatScriptActivity_Notes` |  |  |  |
| 8 | `SE.SCR.ACTY.FUNCTIONALITY.ID` | `SeatScriptActivity_FunctionalityId` |  |  |  |
| 9 | `SE.SCR.ACTY.COMPONENT` | `SeatScriptActivity_Component` |  |  |  |
| 10 | `SE.SCR.ACTY.PRODUCT` | `SeatScriptActivity_Product` | TField |  |  |
| 11 | `SE.SCR.ACTY.PRE.PRIMARY.PRODUCT` | `SeatScriptActivity_PrePrimaryProduct` |  |  |  |
| 12 | `SE.SCR.ACTY.EXCLUDE.SCENARIO` | `SeatScriptActivity_ExcludeScenario` | TField |  | This field is used to identify IIB scenarios. If set to YES, then this scenario will be excluded from TAFC regression. |
| 13 | `SE.SCR.ACTY.OFS.SOURCE` | `SeatScriptActivity_OfsSource` | TField |  |  |
| 14 | `SE.SCR.ACTY.RESERVED.6` | `SeatScriptActivity_Reserved6` | TField |  |  |
| 15 | `SE.SCR.ACTY.RESERVED.5` | `SeatScriptActivity_Reserved5` | TField |  |  |
| 16 | `SE.SCR.ACTY.RESERVED.4` | `SeatScriptActivity_Reserved4` | TField |  |  |
| 17 | `SE.SCR.ACTY.RESERVED.3` | `SeatScriptActivity_Reserved3` | TField |  |  |
| 18 | `SE.SCR.ACTY.RESERVED.2` | `SeatScriptActivity_Reserved2` | TField |  |  |
| 19 | `SE.SCR.ACTY.RESERVED.1` | `SeatScriptActivity_Reserved1` | TField |  |  |
| 20 | `SE.SCR.ACTY.OVERRIDE` | `SeatScriptActivity_Override` |  |  |  |
| 21 | `SE.SCR.ACTY.RECORD.STATUS` | `SeatScriptActivity_RecordStatus` | String |  |  |
| 22 | `SE.SCR.ACTY.CURR.NO` | `SeatScriptActivity_CurrNo` | String |  |  |
| 23 | `SE.SCR.ACTY.INPUTTER` | `SeatScriptActivity_Inputter` |  |  |  |
| 24 | `SE.SCR.ACTY.DATE.TIME` | `SeatScriptActivity_DateTime` |  |  |  |
| 25 | `SE.SCR.ACTY.AUTHORISER` | `SeatScriptActivity_Authoriser` | String |  |  |
| 26 | `SE.SCR.ACTY.CO.CODE` | `SeatScriptActivity_CoCode` | String |  |  |
| 27 | `SE.SCR.ACTY.DEPT.CODE` | `SeatScriptActivity_DeptCode` | String |  |  |
| 28 | `SE.SCR.ACTY.AUDITOR.CODE` | `SeatScriptActivity_AuditorCode` | String |  |  |
| 29 | `SE.SCR.ACTY.AUDIT.DATE.TIME` | `SeatScriptActivity_AuditDateTime` | String |  |  |
