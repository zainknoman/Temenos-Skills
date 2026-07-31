# STO.TYPE — Table Schema

> Source: `INSERTS/I_F.STO.TYPE` in `AC_StandingOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STO.TYP.DESCRIPTION` | `StoType_Description` |  |  |  |
| 2 | `STO.TYP.USER.ROUTINE` | `StoType_UserRoutine` | TField |  | Validation Rules: |
| 3 | `STO.TYP.DAYS.DELIVERY` | `StoType_DaysDelivery` | TField |  | This field provides a default value for the field DAYS.DELIVERY in STO for the STO type of STO.This specifies the number of working days to add to the STO frequency date to give the value date of a standing order. |
| 4 | `STO.TYP.PROC.DATE.TYPE` | `StoType_ProcDateType` | TField | No | This field indicates whether the STO.TYPE supports generation of FUNDS TRANSFER from STANDING.ORDER, 'n' days prior to the Frequency Date as mentioned in DAYS.PRIOR Validation Rules: Optional input Valid values are CVD and Blank Allowed only when DAYS.PRIOR is entered |
| 5 | `STO.TYP.DAYS.PRIOR` | `StoType_DaysPrior` | TField | No | This field indicates the number of days prior to the frequency date, on which the FT is to be generated Validation Rules: Optional input Valid values are nW, nC and Blank, where 'n' stands for the number of days Allowed only when PROC.DATE.TYPE is entered |
| 6 | `STO.TYP.GEN.ADVICE` | `StoType_GenAdvice` | TField | No | This field is used to specify the events for which delivery message has to be generated for a STANDING.ORDER. Events like modification, cancellation or expiry of a STO record could be setup here to generate advices. When this is left blank, the default delivery advice would be generated only during creation or modification of a standing order record. Validation Rules: Valid values are AMEND, EXPIRY, CANCEL, ALL or blank Optional field |
| 7 | `STO.TYP.NON.STP` | `StoType_NonStp` | TField | No | This field is used to specifiy if the FUNDS.TRANSFER record generated via STO processing should be put on hold or should this be created immediately. If this is set to YES, then, FT would be put on hold for user modification else FT would be generated immediately and authorised by system automatically. Validation Rules: Valid values are YES OR left blank Optional field |
| 8 | `STO.TYP.FT.TXN.TYPE` | `StoType_FtTxnType` |  |  |  |
| 9 | `STO.TYP.FT.VERSION` | `StoType_FtVersion` |  |  |  |
| 10 | `STO.TYP.PO.PRD.NAME` | `StoType_PoPrdName` |  |  |  |
| 11 | `STO.TYP.PO.VERSION` | `StoType_PoVersion` |  |  |  |
| 12 | `STO.TYP.SET.TIMEOUT` | `StoType_SetTimeout` | TField |  |  |
| 13 | `STO.TYP.COMPANY.CODE` | `StoType_CompanyCode` |  |  |  |
| 14 | `STO.TYP.COMP.EXECUTION.STAGE` | `StoType_CompExecutionStage` |  |  |  |
| 15 | `STO.TYP.LOCAL.REF` | `StoType_LocalRef` |  |  |  |
| 16 | `STO.TYP.RECORD.STATUS` | `StoType_RecordStatus` | String |  |  |
| 17 | `STO.TYP.CURR.NO` | `StoType_CurrNo` | String |  |  |
| 18 | `STO.TYP.INPUTTER` | `StoType_Inputter` |  |  |  |
| 19 | `STO.TYP.DATE.TIME` | `StoType_DateTime` |  |  |  |
| 20 | `STO.TYP.AUTHORISER` | `StoType_Authoriser` | String |  |  |
| 21 | `STO.TYP.CO.CODE` | `StoType_CoCode` | String |  |  |
| 22 | `STO.TYP.DEPT.CODE` | `StoType_DeptCode` | String |  |  |
| 23 | `STO.TYP.AUDITOR.CODE` | `StoType_AuditorCode` | String |  |  |
| 24 | `STO.TYP.AUDIT.DATE.TIME` | `StoType_AuditDateTime` | String |  |  |
| 25 | `STO.TYP.COMP.EXECUTION.TIME` | `StoType_CompExecutionTime` |  |  |  |
| 26 | `STO.TYP.EXECUTION.STAGE` | `StoType_ExecutionStage` | TField | No | This field is used to holds the execution stage specific to the STO.TYPE. Validation Rules: Optional field Valid values are EOD, SOD and ONLINE For BI and BO type STO, EOD is not allowed since it is the Default Execution Stage. For STO with types other than BI and BO, SOD is not allowed since it is the Default Execution Stage. ONLINE Execution Stage is not allowed for BI,BO,BP,OL types When ExecutionStage is not defined in STANDING.ORDER, this field value will be defaulted in STANDING.ORDER if Company specific Execution Stage i.e COMPANY.EXECUTION.STAGE is null |
| 27 | `STO.TYP.EXECUTION.TIME` | `StoType_ExecutionTime` | TField |  | This field is used to holds the execution time specific to the STO.TYPE. Validation Rules: should be in HH:MM format Allowed only when ExecutionStage is ONLINE When ExecutionTime is not defined in STANDING.ORDER, this field value will be defaulted in STANDING.ORDER if Company specific Execution Time i.e COMPANY.EXECUTION.TIME is null |
| 28 | `STO.TYP.EXECUTION.HIST.DETAILS` | `StoType_ExecutionHistDetails` | TField |  | This field is used to holds the number of historic multi-values of the execution details that the system will keep on the STO before moving the records history file. Validation Rules: should be a valid number |
| 29 | `STO.TYP.SUPPRESS.FWD.ENTRY` | `StoType_SuppressFwdEntry` | TField |  | This field is used to hold the flag in order to suppress the Forward Entries raised for FI type STOs |
| 30 | `STO.TYP.ERROR.DET.RETENTION` | `StoType_ErrorDetRetention` | TField |  | This field defines how many multi-values of error details set (fields Error Date, Error Ul Appl Id and Error Details) in STANDING.ORDER to be retained. For example, if this field is defined as 3 and already 3 Error Date are there in STANDING.ORDER then for 4th Error Date, it will delete the 1st Error Date and insert 4th in last multi-value set. Deletion of old set will follow First In First Out principal. Validation Rules: Should be a valid number between 1 and 999 |
