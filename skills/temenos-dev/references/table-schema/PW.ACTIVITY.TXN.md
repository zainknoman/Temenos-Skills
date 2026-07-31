# PW.ACTIVITY.TXN — Table Schema

> Source: `INSERTS/I_F.PW.ACTIVITY.TXN` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.ACT.TXN.PROCESS` | `PwActivityTxn_Process` | TField |  | PW.ACTIVITY.TXN PROCESS This is an alphanumeric serial key to identify that identifies the PW.PROCESS that this PW.ACTIVITY.TXN record is part of. Validation Rules: System maintained and no-input field. A valid PW.PROCESS id |
| 2 | `PW.ACT.TXN.ACTIVITY` | `PwActivityTxn_Activity` | TField |  | PW.ACTIVITY.TXN ACTIVITY The PW.ACTIVITY key which defines which activity ids being run. Validation Rules: System maintained and no-input field. A valid PW.ACTIVITY Id. |
| 3 | `PW.ACT.TXN.OWNER` | `PwActivityTxn_Owner` | TField |  | PW.ACTIVITY.TXN OWNER The PW.PARTICIPANT key which defines which USER/ DEPT.ACCT.OFFICER group is responsible for this activity transaction. Defaulted from the PW.PROCESS record but can be changed to allocate the activity transaction record to another group. Validation Rules: A valid key of PW.PARTICIPANT |
| 4 | `PW.ACT.TXN.ASSIGN.DATE` | `PwActivityTxn_AssignDate` |  |  |  |
| 5 | `PW.ACT.TXN.ASSIGN.REASON` | `PwActivityTxn_AssignReason` |  |  |  |
| 6 | `PW.ACT.TXN.USER` | `PwActivityTxn_User` |  |  |  |
| 7 | `PW.ACT.TXN.START.DATE` | `PwActivityTxn_StartDate` | TField |  | PW.ACTIVITY.TXN START.DATE THE date the PW.PROCESS record was created by the system is defaulted into the START.DATE on this PW.ACTIVITY.TXN record. Validation Rules: Standard Date Field. |
| 8 | `PW.ACT.TXN.DUE.DATE` | `PwActivityTxn_DueDate` | TField | Yes | PW.ACTIVITY.TXN DUE.DATE The date on which the activity is due is defaulted to this field. This date is calculated by adding the value of the fields DEF.DURATION,EXPIRATION.HOURS and EXPIRATION.MINS from the PW.ACTIVITY record to the MONITOR.INIT.DATE Validation Rules: This is a non-mandatory field. Standard Date Type |
| 9 | `PW.ACT.TXN.COMPLETION.DATE` | `PwActivityTxn_CompletionDate` | TField | Yes | PW.ACTIVITY.TXN COMPLETION.DATE THE date the PW.ACTIVITY.TXN record is complete. This date is automatically defaulted onto the record when the record is complete &amp;#8211; when the PW.ACTIVITY STATUS.CODES and STATUS.RULES have been met and the complete flag for those fields is set to &amp;#8216;Yes&amp;#8217;. When the corresponding transaction has been run and it meets the STATUS.RULES set in the PW.ACTIVITY record which in turn changes the STATUS.CODES. When this STATUS.CODE matches what is defined in the PW.PROCESS.DEFINITION as COMPLETE.STAT and the PW.ACTIVITY COMPLETE flag for this STATUS.RULES is set to Yes, then this transaction will be seen as complete. Validation Rules: This is a non-mandatory field. Standard Date Type |
| 10 | `PW.ACT.TXN.TRANSACTION.REF` | `PwActivityTxn_TransactionRef` | TField |  | PW.ACTIVITY.TXN TRANSACTION.REF The Transaction reference or key to the activity/application that was just run for the activity. IE. If a new ACCOUNT record was created the new ACCOUNT number would appear in this field Validation Rules: System maintained and no-input field. |
| 11 | `PW.ACT.TXN.TARGET` | `PwActivityTxn_Target` | TField |  | PW.ACTIVITY.TXN TARGET This is the target from the associated PW.ACTIVITY record, that would normally be run from the T24 command line. EG. ACCOUNT, I F3 Validation Rules: Standard T24 application/version mentioned in PW.ACTIVITY System maintained and no-input field. |
| 12 | `PW.ACT.TXN.PATTERN.CONSTRUCT` | `PwActivityTxn_PatternConstruct` | TField |  | PW.ACTIVITY.TXN PATTERN.CONSTRUCT The PATTERN.CONSTRUCT key that holds name of the current construct which is being processed. Validation Rules: System maintained. This is a NOINPUT field. |
| 13 | `PW.ACT.TXN.ROUTE.RULE.VALN` | `PwActivityTxn_RouteRuleValn` | TField |  | PW.ACTIVITY.TXN ROUTE.RULE.VALN This holds the result of EVAL.RULE/EVAL.COND of corresponding ROUTE.TO construct. It has Boolean value either TRUE or FALSE. Validation Rules: System maintained. This is a NOINPUT field. |
| 14 | `PW.ACT.TXN.ROUTE.TO.ACTIVITY` | `PwActivityTxn_RouteToActivity` | TField |  | PW.ACTIVITY.TXN ROUTE.TO.ACTIVITY The activity stage in a process to which the process loops back. Validation Rules: System maintained. This is a NOINPUT field. |
| 15 | `PW.ACT.TXN.CONSTRUCT.STATUS` | `PwActivityTxn_ConstructStatus` | TField |  | PW.ACTIVITY.TXN CONSTRUCT.STATUS This denotes the status of corresponding pattern construct at runtime. It can either have the status of PENDING or COMPLETED. Validation Rules: System maintained. This is a NOINPUT field. |
| 16 | `PW.ACT.TXN.PW.ACTIVITY.STATUS` | `PwActivityTxn_PwActivityStatus` | TField |  | PW.ACTIVITY.TXN PW.ACTIVITY.STATUS The last status of this activity transaction. This can be the PW.ACTIVITY DEF.STATUS when the PW.ACTIVITY.TXN record is first created or the PW.ACTIVITY STATUS.CODES when a transaction has met a certain condition set out in the associated PW.ACTIVITY STATUS.RULES. Validation Rules: System maintained. This is a NOINPUT field. |
| 17 | `PW.ACT.TXN.ACTIVITY.TYPE` | `PwActivityTxn_ActivityType` | TField |  | PW.ACTIVITY.TXN ACTIVITY.TYPE Automatically defaulted from the ACTIVITY.TYPE field off the PW.ACTIVITY record. Validation Rules: System maintained and no-input field. Either MANUAL or AUTO ( as specified in PW.ACTIVITY) |
| 18 | `PW.ACT.TXN.RESULT.DATE` | `PwActivityTxn_ResultDate` |  |  |  |
| 19 | `PW.ACT.TXN.ACTIVITY.RESULT` | `PwActivityTxn_ActivityResult` |  |  |  |
| 20 | `PW.ACT.TXN.MAPPING.COMP` | `PwActivityTxn_MappingComp` | TField |  | PW.ACTIVITY.TXN MAPPING.COMP This is field is set to 'Y' when the activity gets executed for the first time and mapping is done. This is to avoid doing the mapping again when the activity is re-executed. Validation Rules: System maintained. This is a no-input field. |
| 21 | `PW.ACT.TXN.START.TIME` | `PwActivityTxn_StartTime` | TField |  | PW.ACTIVITY.TXN START.TIME To meet some of the statistical reporting requirements additional duration data needs to be stored on each PW.ACTIVITY.TXN record. We record Earliest possible start time: When the activity could have been started ie when the pre requisite tasks had been completed Validation Rules: System maintained. This is a NOINPUT field. Standard Time format. |
| 22 | `PW.ACT.TXN.STATUS` | `PwActivityTxn_Status` |  |  |  |
| 23 | `PW.ACT.TXN.END.DATE` | `PwActivityTxn_EndDate` |  |  |  |
| 24 | `PW.ACT.TXN.END.TIME` | `PwActivityTxn_EndTime` |  |  |  |
| 25 | `PW.ACT.TXN.TXN.ITERATION` | `PwActivityTxn_TxnIteration` | TField |  | PW.ACTIVITY.TXN TXN.ITERATION This denotes the the iteration no. if the current activity is a part of an iteration pattern. Validation Rules: System maintained. This is a NOINPUT field. |
| 26 | `PW.ACT.TXN.PARENT.ACT.TXN` | `PwActivityTxn_ParentActTxn` | TField |  | PW.ACTIVITY.TXN PARENT.ACT.TXN This holds the PW.ACTIVITY.TXN ID of corresponding construct. This can populated only at the time of the PARALLER.FLOW or SWITCH or RECURSIVE construct in process. Validation Rules: System maintained. This is a NOINPUT field. |
| 27 | `PW.ACT.TXN.UNIQUE.NAME` | `PwActivityTxn_UniqueName` | TField | Yes | PW.ACTIVITY.TXN UNIQUE.NAME This can be used when two or more identical ACTIVITY names are defined in the PW.PROCESS.DEFINITION. The UNIQUE.NAME is also used in conjunction with the workflow pattern consructs. UNIQUE.NAME is mandatory for every workflow pattern construct defined in the process. Validation Rules: System maintained. This is a NOINPUT field. |
| 28 | `PW.ACT.TXN.PARENT.PROCESS` | `PwActivityTxn_ParentProcess` | TField |  | PW.PROCESS PARENT.PROCESS PW.PROCESS Id in this field denotes the PARENT.PROCESS field value of the PW.PROCESS record which created this activity record. This is used for enquiry purposes. Validation Rules: System maintained. This is a NOINPUT field. |
| 29 | `PW.ACT.TXN.ORIGINATE.PROCESS` | `PwActivityTxn_OriginateProcess` | TField |  | PW.ACTIVITY.TXN ORIGINATE.PROCESS PW.PROCESS Id in this field has the PROCESS id which created the entire PW instance. This field is used to fetch all the ACTIVITY.TXN records of a particular PW instance. This is used for enquiry purposes. Validation Rules: System maintained. These are NOINPUT fields. |
| 30 | `PW.ACT.TXN.EXTERNAL.PROCESS` | `PwActivityTxn_ExternalProcess` | TField |  | Holds the Process name of the Activity triggered from BPEL |
| 31 | `PW.ACT.TXN.EXT.PROCESS.ID` | `PwActivityTxn_ExtProcessId` | TField |  | Holds the Process ID of the Activity triggered from BPEL |
| 32 | `PW.ACT.TXN.MONITOR.INIT.TIME` | `PwActivityTxn_MonitorInitTime` | TField |  | PW.ACTIVITY.TXN MONITOR.INIT.TIME The Time at which the activity is started is recorded and defaulted in this field. The Time should be read along with the MONITOR.INIT.DATE field. Validation Rules: System maintained. |
| 33 | `PW.ACT.TXN.MONITOR.INIT.DATE` | `PwActivityTxn_MonitorInitDate` | TField |  | PW.ACTIVITY.TXN MONITOR.INIT.DATE The date at which the activity was started is recorded and defaulted in this field. Validation Rules: System maintained. |
| 34 | `PW.ACT.TXN.DUE.TIME` | `PwActivityTxn_DueTime` | TField |  | PW.ACTIVITY.TXN DUE.TIME The time at which the activity has to be completed is calculated and defaulted to this field. The due time is read along with the DUE.DATE field Validation Rules: System maintained. |
| 35 | `PW.ACT.TXN.USER.ROLE` | `PwActivityTxn_UserRole` | TField |  | PW.ACTIVITY.TXN USER.ROLE This is a no-input field The value entered in the PW.ACTIVITY gets substituted into this field at run time |
| 36 | `PW.ACT.TXN.VERSION.ID` | `PwActivityTxn_VersionId` | TField |  | PW.ACTIVITY.TXN VERSION.ID Specifies the version of an activity run Validation Rules: This is a non-input field. Gets substituted from the PW.ACTIVITY being executed. |
| 37 | `PW.ACT.TXN.RESERVED.6` | `PwActivityTxn_Reserved6` | TField |  |  |
| 38 | `PW.ACT.TXN.RESERVED.5` | `PwActivityTxn_Reserved5` | TField |  |  |
| 39 | `PW.ACT.TXN.RESERVED.4` | `PwActivityTxn_Reserved4` | TField |  |  |
| 40 | `PW.ACT.TXN.RESERVED.3` | `PwActivityTxn_Reserved3` | TField |  |  |
| 41 | `PW.ACT.TXN.RESERVED.2` | `PwActivityTxn_Reserved2` | TField |  |  |
| 42 | `PW.ACT.TXN.RESERVED.1` | `PwActivityTxn_Reserved1` | TField |  |  |
| 43 | `PW.ACT.TXN.LOCAL.REF` | `PwActivityTxn_LocalRef` |  |  |  |
| 44 | `PW.ACT.TXN.OVERRIDE` | `PwActivityTxn_Override` |  |  |  |
| 45 | `PW.ACT.TXN.RECORD.STATUS` | `PwActivityTxn_RecordStatus` | String |  |  |
| 46 | `PW.ACT.TXN.CURR.NO` | `PwActivityTxn_CurrNo` | String |  |  |
| 47 | `PW.ACT.TXN.INPUTTER` | `PwActivityTxn_Inputter` |  |  |  |
| 48 | `PW.ACT.TXN.DATE.TIME` | `PwActivityTxn_DateTime` |  |  |  |
| 49 | `PW.ACT.TXN.AUTHORISER` | `PwActivityTxn_Authoriser` | String |  |  |
| 50 | `PW.ACT.TXN.CO.CODE` | `PwActivityTxn_CoCode` | String |  |  |
| 51 | `PW.ACT.TXN.DEPT.CODE` | `PwActivityTxn_DeptCode` | String |  |  |
| 52 | `PW.ACT.TXN.AUDITOR.CODE` | `PwActivityTxn_AuditorCode` | String |  |  |
| 53 | `PW.ACT.TXN.AUDIT.DATE.TIME` | `PwActivityTxn_AuditDateTime` | String |  |  |
| 54 | `PW.ACT.TXN.TARGET.API` | `PwActivityTxn_TargetApi` | TField |  |  |
