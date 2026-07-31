# EB.MCI.EXECUTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.EB.MCI.EXECUTION.DETAILS` in `EI_MCI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MCI.ED.TXN.REF` | `EbMciExecutionDetails_TxnRef` | TField |  | This field specifies the reference of the Mass Change Instruction that is behind this Execution and that which has resulted in this execution detail. |
| 2 | `EB.MCI.ED.TARGET.APP` | `EbMciExecutionDetails_TargetApp` | TField |  | This field specifies the application that has been the target of change in this execution. |
| 3 | `EB.MCI.ED.TARGET.ID` | `EbMciExecutionDetails_TargetId` | TField |  | This field specifies the ID of target record that change has been applied to it. |
| 4 | `EB.MCI.ED.COMPANY.CODE` | `EbMciExecutionDetails_CompanyCode` | TField |  | This field specifies the company ID that target objects belong to. |
| 5 | `EB.MCI.ED.EXCLUDE` | `EbMciExecutionDetails_Exclude` | TField |  | This field specifies whether this record is excluded from change or not. |
| 6 | `EB.MCI.ED.REASON` | `EbMciExecutionDetails_Reason` | TField |  | This field specifies the reason of exclusion. |
| 7 | `EB.MCI.ED.ACTION` | `EbMciExecutionDetails_Action` | TField |  | This field holds the status of Mass Change Instruction TASK like Execute or Verify. |
| 8 | `EB.MCI.ED.PROCESSING.DATE` | `EbMciExecutionDetails_ProcessingDate` | TField |  | This field holds the processing date of Mass Change Instruction. |
| 9 | `EB.MCI.ED.ACTIVITY` | `EbMciExecutionDetails_Activity` | TField |  | This field contains activity name from Mass Change Instruction. |
| 10 | `EB.MCI.ED.EXEC.STATUS` | `EbMciExecutionDetails_ExecStatus` | TField |  | This field specifies the status of execution and it can be one of the following values: Processed: if the Execution was successful. Failed: if the Execution Failed - OFS returned an Error Message Skipped: if the Execution was skipped because of --Old Value didn't match with Record Value --Condition Rule didn't satisfy --Lookup Rule didn't satisfy --If there is an Unauthorised record existing for the Target Record |
| 11 | `EB.MCI.ED.EXEC.REF` | `EbMciExecutionDetails_ExecRef` | TField |  | This field specifies the reference of execution. This may be the same as the Target Record ID (in cases where the Business Operation is essentially an amendment of an existing record such as CUSTOMER) or different (in cases where the Business Operation is an Activity run on the Target such as AA.ARRANGEMENT in which case, this will be the AA.ARRANGEMENT.ACTIVITY ID. |
| 12 | `EB.MCI.ED.STATUS.MSG` | `EbMciExecutionDetails_StatusMsg` |  |  |  |
| 13 | `EB.MCI.ED.TARGET.REC.STATUS` | `EbMciExecutionDetails_TargetRecStatus` | TField |  | This field specifies the status of target record after execution. |
| 14 | `EB.MCI.ED.NAO.OVERRIDES` | `EbMciExecutionDetails_NaoOverrides` |  |  |  |
| 15 | `EB.MCI.ED.ATTRIBUTE` | `EbMciExecutionDetails_Attribute` |  |  |  |
| 16 | `EB.MCI.ED.OLD.VALUE` | `EbMciExecutionDetails_OldValue` |  |  |  |
| 17 | `EB.MCI.ED.NEW.VALUE` | `EbMciExecutionDetails_NewValue` |  |  |  |
| 18 | `EB.MCI.ED.RESERVED.1` | `EbMciExecutionDetails_Reserved1` | TField |  |  |
| 19 | `EB.MCI.ED.RESERVED.2` | `EbMciExecutionDetails_Reserved2` | TField |  |  |
| 20 | `EB.MCI.ED.RESERVED.3` | `EbMciExecutionDetails_Reserved3` | TField |  |  |
| 21 | `EB.MCI.ED.RESERVED.4` | `EbMciExecutionDetails_Reserved4` | TField |  |  |
| 22 | `EB.MCI.ED.RESERVED.5` | `EbMciExecutionDetails_Reserved5` | TField |  |  |
| 23 | `EB.MCI.ED.LOCAL.REF` | `EbMciExecutionDetails_LocalRef` |  |  |  |
| 24 | `EB.MCI.ED.OVERRIDE` | `EbMciExecutionDetails_Override` |  |  |  |
| 25 | `EB.MCI.ED.RECORD.STATUS` | `EbMciExecutionDetails_RecordStatus` | String |  |  |
| 26 | `EB.MCI.ED.CURR.NO` | `EbMciExecutionDetails_CurrNo` | String |  |  |
| 27 | `EB.MCI.ED.INPUTTER` | `EbMciExecutionDetails_Inputter` |  |  |  |
| 28 | `EB.MCI.ED.DATE.TIME` | `EbMciExecutionDetails_DateTime` |  |  |  |
| 29 | `EB.MCI.ED.AUTHORISER` | `EbMciExecutionDetails_Authoriser` | String |  |  |
| 30 | `EB.MCI.ED.CO.CODE` | `EbMciExecutionDetails_CoCode` | String |  |  |
| 31 | `EB.MCI.ED.DEPT.CODE` | `EbMciExecutionDetails_DeptCode` | String |  |  |
| 32 | `EB.MCI.ED.AUDITOR.CODE` | `EbMciExecutionDetails_AuditorCode` | String |  |  |
| 33 | `EB.MCI.ED.AUDIT.DATE.TIME` | `EbMciExecutionDetails_AuditDateTime` | String |  |  |
