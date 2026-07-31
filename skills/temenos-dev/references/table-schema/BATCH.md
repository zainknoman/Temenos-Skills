# BATCH — Table Schema

> Source: `INSERTS/I_F.BATCH` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BAT.BATCH.STAGE` | `Batch_BatchStage` | A (alphanumeric) | Conditional | This field allows the user to group the processes into four distinct stages (Application, System, Reporting Start of day and Online). Within the batch control system, each stage verifies that all the processes in the previous stage have completed successfully before continuing. If no sequence number (process dependency) has been appended to the batch stage, then this process can be run concurrently within the stage. However if a sequence number (e.g. A009) has been specified then the process can be run only when all other processes with sequence numbers lower than this have completed successfully. Processes with the same sequence number can be run concurrently. Modifications to the sequence number should adhere to the following guidelines: 1. Sequence numbers in the range 000 to 099 should not be modified. 2. Sequence numbers in the range 100 to 899 - only the last two digits should be modified. 3. Sequence numbers 900 - 999 should not be modified. Certain restrictions apply to the system on the number of processes that can share a given stage based on the sequence. Pls. refer User Guide for more explanation on this. Validation Rules: 1-4 type A (alphanumeric) characters. The first character is used to define the stage, it must be one of the following: A - Application D - Start of Day R - Reporting S - System O - Online The remaining 3 characters (optional process sequence number) should be numeric. Mandatory input. |
| 2 | `BAT.DEFAULT.PRINTER` | `Batch_DefaultPrinter` | A (alphanumeric) |  | Specifies the default printer and form name to which all output is to be directed for the process. If no printer name has been specified in field PRINTER.NAME for the individual jobs, then this field allows the user to define a default printer to direct all output to for the process. If this field is left blank and no printer has been specified for the individual jobs, then the output is sent to the default SYSTEM printer defined in DE.FORM.TYPE. Examples: PR1 - Direct output to system printer PR1. /STFORM - Direct output to system printer with a form type of STFORM. PR1/STFORM - Direct output to printer PR1 with a form type of STFORM. Validation Rules: 0-35 type A (alphanumeric) characters. These can define: 'Printer name' (system defined) or 'Printer name'/'Form name' or /'Form name' The 'Printer name' must be a valid system printer and exist on file F.PRINTER.ID. The 'Form name' must be a valid entry on file F.DE.FORM.TYPE. |
| 3 | `BAT.PROCESS.STATUS` | `Batch_ProcessStatus` | TField |  | Indicates the current process status. Some common status values are: 0 - Ready 1 - Running 2 - Completed successfully 3 - On hold or in error Validation Rules: Numeric. System maintained. This is a NOINPUT field. |
| 4 | `BAT.BATCH.ENVIRONMENT` | `Batch_BatchEnvironment` | TField | Yes | Defines the environment to run the process in, i.e foreground or background. A foreground process will be run directly on the users terminal, whereas a background process will run as a phantom task. The background facility allows the user to run a number of processes concurrently. Validation Rules: 1 uppercase alpha character. F - Foreground B - Background (Mandatory input) The background option may only be used for those processes which are in the reporting stage. |
| 5 | `BAT.DEPARTMENT.CODE` | `Batch_DepartmentCode` | A (alphanumeric) |  | This field specifies the department code to be used when running the process in the batch control system. Validation Rules: 0-4 type A (alphanumeric) characters. Must be a valid record on the DEPT.ACCT.OFFICER file. |
| 6 | `BAT.JOB.NAME` | `Batch_JobName` |  |  |  |
| 7 | `BAT.VERIFICATION` | `Batch_Verification` |  |  |  |
| 8 | `BAT.FREQUENCY` | `Batch_Frequency` |  |  |  |
| 9 | `BAT.NEXT.RUN.DATE` | `Batch_NextRunDate` |  |  |  |
| 10 | `BAT.PRINTER.NAME` | `Batch_PrinterName` |  |  |  |
| 11 | `BAT.DATA` | `Batch_Data` |  |  |  |
| 12 | `BAT.JOB.STATUS` | `Batch_JobStatus` |  |  |  |
| 13 | `BAT.LAST.RUN.DATE` | `Batch_LastRunDate` |  |  |  |
| 14 | `BAT.JOB.MESSAGE` | `Batch_JobMessage` |  |  |  |
| 15 | `BAT.USER` | `Batch_User` |  |  |  |
| 16 | `BAT.SELECT.AHEAD` | `Batch_SelectAhead` |  |  |  |
| 17 | `BAT.CLEAR.STATIC.CACHE` | `Batch_ClearStaticCache` | TField |  | This field signifies whether to clear the static cache while processing each job in a batch process |
| 18 | `BAT.POST.UPGRADE` | `Batch_PostUpgrade` | TField |  |  |
| 19 | `BAT.LOCK.RETRY.COUNT` | `Batch_LockRetryCount` | TField |  | This field is used to indicate how many times there has been a failed contention for lock while executing this BATCH during COB. It is cleared and reset to 0 on successful completion of this BATCH. |
| 20 | `BAT.LOCAL.REF` | `Batch_LocalRef` |  |  |  |
| 21 | `BAT.RESERVED.1` | `Batch_Reserved1` | TField |  |  |
| 22 | `BAT.RESERVED.2` | `Batch_Reserved2` | TField |  |  |
| 23 | `BAT.RESERVED.3` | `Batch_Reserved3` | TField |  |  |
| 24 | `BAT.RESERVED.4` | `Batch_Reserved4` | TField |  |  |
| 25 | `BAT.RESERVED.5` | `Batch_Reserved5` | TField |  |  |
| 26 | `BAT.RESERVED.6` | `Batch_Reserved6` | TField |  |  |
| 27 | `BAT.RECORD.STATUS` | `Batch_RecordStatus` | String |  |  |
| 28 | `BAT.CURR.NO` | `Batch_CurrNo` | String |  |  |
| 29 | `BAT.INPUTTER` | `Batch_Inputter` |  |  |  |
| 30 | `BAT.DATE.TIME` | `Batch_DateTime` |  |  |  |
| 31 | `BAT.AUTHORISER` | `Batch_Authoriser` | String |  |  |
| 32 | `BAT.CO.CODE` | `Batch_CoCode` | String |  |  |
| 33 | `BAT.DEPT.CODE` | `Batch_DeptCode` | String |  |  |
| 34 | `BAT.AUDITOR.CODE` | `Batch_AuditorCode` | String |  |  |
| 35 | `BAT.AUDIT.DATE.TIME` | `Batch_AuditDateTime` | String |  |  |
| 36 | `BAT.MAIN.STAGE` | `Batch_MainStage` | TField |  | Indicates the COB Main stages under which a batch record can be classified. Validation Rules: Valid values are: APPLICATION, SYSTEM, REPORTING, START.OF.DAY, ONLINE MAIN.STAGE, COB.STAGE, COB.STAGE.SEQ fields are related each other and Required only for COB related batch record, not allowed for service related batch records. COB Framework will use these field values to run business stage COB if BUSINESS.STAGE.COB is enabled in TSA.PARAMETER. |
| 37 | `BAT.COB.STAGE` | `Batch_CobStage` | TField | Yes | Indicates the COB sub stages under which a batch record can be classified. It is drop down field with list of hardcoded sub stages of each main stage indicating prefix as A,S,R,D,O. Validation Rules: System fetches valid COB stages for its corresponding Main stage only after all the COB BATCH records business stage classification is finalized and made available in T24 Build 1. Any incorrect sub stage selected for main stage will raise error. For example, When MAIN.STAGE = SYSTEM, then COB.STAGE should be sub stage of SYSTEM, i.e S-[substage] System fetches valid COB Stages of corresponding MAIN.STAGE and do this validation. 2. Mandatory when MAIN.STAGE is defined. Valid format: A-[SubStage], S-[SubStage], R-[SubStage], D-[SubStage],O-[SubStage] For example, A-DATE, A-PRECONTRACT, A-POSTCONTRACT, S-REPORTING, S-FINANCIAL, R-CONTRACT, D-DATE,O-CONTRACTS something like a valid business sub stages. |
| 38 | `BAT.COB.STAGE.SEQ` | `Batch_CobStageSeq` | TField |  | Indicates the COB sub stage sequence under which a batch record can be classified. It is system updated field based on MAIN.STAGE and COB.STAGE contains valid values. System updates same value in BATCH.STAGE if left empty for COB related batch record. Validation Rules: If Main stage and COB stage is valid then this COB.STAGE.SEQ gets updated by system. This field cannot have null value when valid MAIN.STAGE and COB.STAGE is defined. For example, When MAIN.STAGE = SYSTEM, then COB.STAGE = S-FINANCIAL , then COB.STAGE.SEQ can be SNNN i.e Batch stage format |
