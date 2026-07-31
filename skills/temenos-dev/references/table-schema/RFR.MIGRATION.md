# RFR.MIGRATION — Table Schema

> Source: `INSERTS/I_F.RFR.MIGRATION` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RFR.MG.DESCRIPTION` | `RfrMigration_Description` |  |  |  |
| 2 | `RFR.MG.APPLICATION.NAME` | `RfrMigration_ApplicationName` | TField | Yes | Application or product used for migration. Example : LD.LOANS.AND.DEPOSITS, SAVINGS.ACCOUNT in case of AA Validation rules: Mandatory input Should be a valid application or a product in case of arrangement |
| 3 | `RFR.MG.IBOR.CUTOFF.DATE` | `RfrMigration_IborCutoffDate` | TField | Yes | IBOR Discontinuation date Validation rules: Mandatory input Back value date is not possible |
| 4 | `RFR.MG.VERSION.NAME` | `RfrMigration_VersionName` | TField | Yes | Valid version of application used for RFR migration process. Validation rules: Mandatory input Must be a valid version for the application |
| 5 | `RFR.MG.OFS.ROUTINE` | `RfrMigration_OfsRoutine` | TField | Yes | Routine call to get the OFS message that will be posted for Execution mode. Validation rules: Mandatory input Must be a valid routine |
| 6 | `RFR.MG.MODE` | `RfrMigration_Mode` | TField | Yes | Define the type of migration Preview: Used for the verification process. Contract update does not take place Execute: Actual contract update is carried out Validation rule: Mandatory input Valid values: Preview OR Execute |
| 7 | `RFR.MG.INT.PERIOD.END.DATE` | `RfrMigration_IntPeriodEndDate` | TField | Yes | Define Interest period end date Validation rules: Mandatory input for EXECUTE mode Valid values: Valid date and blank Blank : Process all contracts (applicable only for Preview mode) |
| 8 | `RFR.MG.APPL.FIELD.NAME` | `RfrMigration_ApplFieldName` |  |  |  |
| 9 | `RFR.MG.FIELD.OPERAND` | `RfrMigration_FieldOperand` |  |  |  |
| 10 | `RFR.MG.VALUE.FROM` | `RfrMigration_ValueFrom` |  |  |  |
| 11 | `RFR.MG.VALUE.TO` | `RfrMigration_ValueTo` |  |  |  |
| 12 | `RFR.MG.ROUTINE.NAME` | `RfrMigration_RoutineName` | TField | Yes | Routine Name which will identify the records to be processed Validation rule: Either APPL.FIELD.NAME or ROUTINE.NAME is mandatory. But both cannot be entered |
| 13 | `RFR.MG.RESERVED.5` | `RfrMigration_Reserved5` | TField |  |  |
| 14 | `RFR.MG.RESERVED.4` | `RfrMigration_Reserved4` | TField |  |  |
| 15 | `RFR.MG.RESERVED.3` | `RfrMigration_Reserved3` | TField |  |  |
| 16 | `RFR.MG.RESERVED.2` | `RfrMigration_Reserved2` | TField |  |  |
| 17 | `RFR.MG.RESERVED.1` | `RfrMigration_Reserved1` | TField |  |  |
| 18 | `RFR.MG.LOCAL.REF` | `RfrMigration_LocalRef` |  |  |  |
| 19 | `RFR.MG.OVERRIDE` | `RfrMigration_Override` |  |  |  |
| 20 | `RFR.MG.RECORD.STATUS` | `RfrMigration_RecordStatus` | String |  |  |
| 21 | `RFR.MG.CURR.NO` | `RfrMigration_CurrNo` | String |  |  |
| 22 | `RFR.MG.INPUTTER` | `RfrMigration_Inputter` |  |  |  |
| 23 | `RFR.MG.DATE.TIME` | `RfrMigration_DateTime` |  |  |  |
| 24 | `RFR.MG.AUTHORISER` | `RfrMigration_Authoriser` | String |  |  |
| 25 | `RFR.MG.CO.CODE` | `RfrMigration_CoCode` | String |  |  |
| 26 | `RFR.MG.DEPT.CODE` | `RfrMigration_DeptCode` | String |  |  |
| 27 | `RFR.MG.AUDITOR.CODE` | `RfrMigration_AuditorCode` | String |  |  |
| 28 | `RFR.MG.AUDIT.DATE.TIME` | `RfrMigration_AuditDateTime` | String |  |  |
