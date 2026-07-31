# FS.GI.WEM.EXCEPTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.EXCEPTION.DETAILS` in `FS_WemProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.WEM.EXCEPTION.DETAILS.PARENT.REF.ID` | `FsGiWemExceptionDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.WEM.EXCEPTION.DETAILS.ORA.ROWID` | `FsGiWemExceptionDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.WEM.EXCEPTION.DETAILS.EXCHANGE.GROUP` | `FsGiWemExceptionDetails_ExchangeGroup` | TField |  | Workflow Exception Management (WEM) exchange group for which there is exception. Multifonds DB Column is CGROUPE_COURS. |
| 4 | `FS.GI.WEM.EXCEPTION.DETAILS.PARENT.TYPE` | `FsGiWemExceptionDetails_ParentType` | TField |  | Parent type. Multifonds DB Column is ENTITY_TYPE. |
| 5 | `FS.GI.WEM.EXCEPTION.DETAILS.PARENT.ID` | `FsGiWemExceptionDetails_ParentId` | TField |  | Parent ID. Multifonds DB Column is ENTITY_ID. |
| 6 | `FS.GI.WEM.EXCEPTION.DETAILS.FUND.ID` | `FsGiWemExceptionDetails_FundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 7 | `FS.GI.WEM.EXCEPTION.DETAILS.SHARE.CLASS.CODE` | `FsGiWemExceptionDetails_ShareClassCode` | TField |  | Fund Share Class. Multifonds DB Column is TPARTS. |
| 8 | `FS.GI.WEM.EXCEPTION.DETAILS.SECURITY.ISIN.CODE` | `FsGiWemExceptionDetails_SecurityIsinCode` | TField |  | Security ISIN code. Multifonds DB Column is ISIN_CODE. |
| 9 | `FS.GI.WEM.EXCEPTION.DETAILS.TRADE.DATE` | `FsGiWemExceptionDetails_TradeDate` | TField |  | Trade date of the WEM process. Multifonds DB Column is DOPER. |
| 10 | `FS.GI.WEM.EXCEPTION.DETAILS.STEP.PROCESS.GROUP` | `FsGiWemExceptionDetails_StepProcessGroup` | TField |  | Current process group for which exception is encountered. Multifonds DB Column is STEP_PROC_GRP. |
| 11 | `FS.GI.WEM.EXCEPTION.DETAILS.WEM.PROCESS.TYPE` | `FsGiWemExceptionDetails_WemProcessType` | TField |  | User defined code to describe a process type. Multifonds DB Column is CPROCESS. |
| 12 | `FS.GI.WEM.EXCEPTION.DETAILS.CONTROL.NUMBER` | `FsGiWemExceptionDetails_ControlNumber` | TField |  | Unique control number. Multifonds DB Column is TYP_CTRL_ID. |
| 13 | `FS.GI.WEM.EXCEPTION.DETAILS.EXCEPTION.STATUS` | `FsGiWemExceptionDetails_ExceptionStatus` | TField |  | WEM exception status. Multifonds DB Column is MF_STATUS. |
| 14 | `FS.GI.WEM.EXCEPTION.DETAILS.ERROR.TYPE` | `FsGiWemExceptionDetails_ErrorType` | TField |  | Error type. For example : &apos;0001 - Warning&apos; or &apos;0002 - Blocking&apos;. Multifonds DB Column is ERROR_TYPE. |
| 15 | `FS.GI.WEM.EXCEPTION.DETAILS.ERROR.MESSAGE` | `FsGiWemExceptionDetails_ErrorMessage` | TField |  | Error message for the exception. Multifonds DB Column is ERROR_MSG. |
| 16 | `FS.GI.WEM.EXCEPTION.DETAILS.JUSTIFICATION` | `FsGiWemExceptionDetails_Justification` | TField |  | Justification for the exception. Multifonds DB Column is JUSTIFICATION. |
| 17 | `FS.GI.WEM.EXCEPTION.DETAILS.LINKED.FILE.NAME` | `FsGiWemExceptionDetails_LinkedFileName` | TField |  | Linked file name. Multifonds DB Column is LINK_FILE. |
| 18 | `FS.GI.WEM.EXCEPTION.DETAILS.DESCRIPTION` | `FsGiWemExceptionDetails_Description` | TField |  | Description of approval. Multifonds DB Column is DESCRIPTION. |
| 19 | `FS.GI.WEM.EXCEPTION.DETAILS.SUBMITTED.BY` | `FsGiWemExceptionDetails_SubmittedBy` | TField |  | User who submitted exception. Multifonds DB Column is SUBMITTED_BY. |
| 20 | `FS.GI.WEM.EXCEPTION.DETAILS.SUBMITTED.DATE` | `FsGiWemExceptionDetails_SubmittedDate` | TField |  | Exception submitted date. Multifonds DB Column is DSUBMITTED. |
| 21 | `FS.GI.WEM.EXCEPTION.DETAILS.VALIDATED.BY` | `FsGiWemExceptionDetails_ValidatedBy` | TField |  | User who validated exception. Multifonds DB Column is VALIDATED_BY. |
| 22 | `FS.GI.WEM.EXCEPTION.DETAILS.VALIDATED.DATE` | `FsGiWemExceptionDetails_ValidatedDate` | TField |  | Exception validated date. Multifonds DB Column is DVALIDATED. |
| 23 | `FS.GI.WEM.EXCEPTION.DETAILS.REJECTED.USER` | `FsGiWemExceptionDetails_RejectedUser` | TField |  | User who rejected exception. Multifonds DB Column is REJECTED_BY. |
| 24 | `FS.GI.WEM.EXCEPTION.DETAILS.REJECTED.DATE` | `FsGiWemExceptionDetails_RejectedDate` | TField |  | Exception rejected date. Multifonds DB Column is DREJECTED. |
| 25 | `FS.GI.WEM.EXCEPTION.DETAILS.EXCEPTION.REJECTION.REASON` | `FsGiWemExceptionDetails_ExceptionRejectionReason` | TField |  | Reason for rejecting exception. Multifonds DB Column is REJECTION_REASON. |
| 26 | `FS.GI.WEM.EXCEPTION.DETAILS.WEM.CONTROL.SEQUENCE` | `FsGiWemExceptionDetails_WemControlSequence` | TField |  | WEM control sequence number. Multifonds DB Column is CTRL_SEQ. |
| 27 | `FS.GI.WEM.EXCEPTION.DETAILS.THRESHOLD.TYPE` | `FsGiWemExceptionDetails_ThresholdType` | TField |  | Threshold type. Multifonds DB Column is TYP_THRESH. |
| 28 | `FS.GI.WEM.EXCEPTION.DETAILS.SITUATION.DATE` | `FsGiWemExceptionDetails_SituationDate` | TField |  | Situation date for the exception. Multifonds DB Column is SITUATION_DATE. |
| 29 | `FS.GI.WEM.EXCEPTION.DETAILS.EXCEPTION.DELETE.FLAG` | `FsGiWemExceptionDetails_ExceptionDeleteFlag` | TField |  | Exception delete flag. Multifonds DB Column is FLG_DEL. |
| 30 | `FS.GI.WEM.EXCEPTION.DETAILS.ACCRUAL.SIMULATION.FLAG` | `FsGiWemExceptionDetails_AccrualSimulationFlag` | TField |  | Accrual simulation flag. Multifonds DB Column is FLG_ACC_SIM. |
| 31 | `FS.GI.WEM.EXCEPTION.DETAILS.TA.FUND.ID` | `FsGiWemExceptionDetails_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF_TA. |
| 32 | `FS.GI.WEM.EXCEPTION.DETAILS.WEM.EXCEPTION.SEQUENCE` | `FsGiWemExceptionDetails_WemExceptionSequence` | TField |  | WEM exception sequence number. Multifonds DB Column is EXCEP_SEQ. |
| 33 | `FS.GI.WEM.EXCEPTION.DETAILS.ORIGINAL.TRADE.DATE` | `FsGiWemExceptionDetails_OriginalTradeDate` | TField |  | Original trade date. Multifonds DB Column is ORIG_DCTA. |
| 34 | `FS.GI.WEM.EXCEPTION.DETAILS.CONDITIONAL.CONTROL.SEQUENCE` | `FsGiWemExceptionDetails_ConditionalControlSequence` | TField |  | Conditional control setup sequence number to maintain new index logic. Multifonds DB Column is COND_CTRL_SEQ. |
| 35 | `FS.GI.WEM.EXCEPTION.DETAILS.ORDER.ID` | `FsGiWemExceptionDetails_OrderId` | TField |  | Order number. Multifonds DB Column is NORDER. |
| 36 | `FS.GI.WEM.EXCEPTION.DETAILS.AGENT.ID` | `FsGiWemExceptionDetails_AgentId` | TField |  | Agent internal ID linked to the exchange group and fund. Multifonds DB Column is NOUTLET. |
| 37 | `FS.GI.WEM.EXCEPTION.DETAILS.FUND.GROUP.DESCRIPTION` | `FsGiWemExceptionDetails_FundGroupDescription` | TField |  | Fund group description. Multifonds DB Column is FUND_GROUP_DESC. |
| 38 | `FS.GI.WEM.EXCEPTION.DETAILS.ENTITY.DESCRIPTION` | `FsGiWemExceptionDetails_EntityDescription` | TField |  | Entity description. Multifonds DB Column is ENTITY_DESC. |
| 39 | `FS.GI.WEM.EXCEPTION.DETAILS.FUND.DESCRIPTION` | `FsGiWemExceptionDetails_FundDescription` | TField |  | Fund name. Multifonds DB Column is FUND_NAME. |
| 40 | `FS.GI.WEM.EXCEPTION.DETAILS.STEP.DESCRIPTION` | `FsGiWemExceptionDetails_StepDescription` | TField |  | WEM Step description. Multifonds DB Column is STEP_PROC_GRP_DESC. |
| 41 | `FS.GI.WEM.EXCEPTION.DETAILS.CONTROL.DESCRIPTION` | `FsGiWemExceptionDetails_ControlDescription` | TField |  | WEM control description. Multifonds DB Column is CONTROL. |
| 42 | `FS.GI.WEM.EXCEPTION.DETAILS.STATUS.DESCRIPTION` | `FsGiWemExceptionDetails_StatusDescription` | TField |  | Status description. Multifonds DB Column is STATUS. |
| 43 | `FS.GI.WEM.EXCEPTION.DETAILS.TYPE.DESCRIPTION` | `FsGiWemExceptionDetails_TypeDescription` | TField |  | Error type description. Multifonds DB Column is ERROR_TYPE_DESC. |
| 44 | `FS.GI.WEM.EXCEPTION.DETAILS.SUB.STEP.DESCRIPTION` | `FsGiWemExceptionDetails_SubStepDescription` | TField |  | WEM Sub step description. Multifonds DB Column is CPROCESS_DESC. |
| 45 | `FS.GI.WEM.EXCEPTION.DETAILS.WEM.EXCEPTION.BUTTON` | `FsGiWemExceptionDetails_WemExceptionButton` | TField |  | WEM exception button. Multifonds DB Column is WEM_EXP_BUTTON. |
| 46 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED10` | `FsGiWemExceptionDetails_Reserved10` | TField |  |  |
| 47 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED9` | `FsGiWemExceptionDetails_Reserved9` | TField |  |  |
| 48 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED8` | `FsGiWemExceptionDetails_Reserved8` | TField |  |  |
| 49 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED7` | `FsGiWemExceptionDetails_Reserved7` | TField |  |  |
| 50 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED6` | `FsGiWemExceptionDetails_Reserved6` | TField |  |  |
| 51 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED5` | `FsGiWemExceptionDetails_Reserved5` | TField |  |  |
| 52 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED4` | `FsGiWemExceptionDetails_Reserved4` | TField |  |  |
| 53 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED3` | `FsGiWemExceptionDetails_Reserved3` | TField |  |  |
| 54 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED2` | `FsGiWemExceptionDetails_Reserved2` | TField |  |  |
| 55 | `FS.GI.WEM.EXCEPTION.DETAILS.RESERVED1` | `FsGiWemExceptionDetails_Reserved1` | TField |  |  |
| 56 | `FS.GI.WEM.EXCEPTION.DETAILS.LOCAL.REF` | `FsGiWemExceptionDetails_LocalRef` |  |  |  |
| 57 | `FS.GI.WEM.EXCEPTION.DETAILS.OVERRIDE` | `FsGiWemExceptionDetails_Override` |  |  |  |
| 58 | `FS.GI.WEM.EXCEPTION.DETAILS.RECORD.STATUS` | `FsGiWemExceptionDetails_RecordStatus` | String |  |  |
| 59 | `FS.GI.WEM.EXCEPTION.DETAILS.CURR.NO` | `FsGiWemExceptionDetails_CurrNo` | String |  |  |
| 60 | `FS.GI.WEM.EXCEPTION.DETAILS.INPUTTER` | `FsGiWemExceptionDetails_Inputter` |  |  |  |
| 61 | `FS.GI.WEM.EXCEPTION.DETAILS.DATE.TIME` | `FsGiWemExceptionDetails_DateTime` |  |  |  |
| 62 | `FS.GI.WEM.EXCEPTION.DETAILS.AUTHORISER` | `FsGiWemExceptionDetails_Authoriser` | String |  |  |
| 63 | `FS.GI.WEM.EXCEPTION.DETAILS.CO.CODE` | `FsGiWemExceptionDetails_CoCode` | String |  |  |
| 64 | `FS.GI.WEM.EXCEPTION.DETAILS.DEPT.CODE` | `FsGiWemExceptionDetails_DeptCode` | String |  |  |
| 65 | `FS.GI.WEM.EXCEPTION.DETAILS.AUDITOR.CODE` | `FsGiWemExceptionDetails_AuditorCode` | String |  |  |
| 66 | `FS.GI.WEM.EXCEPTION.DETAILS.AUDIT.DATE.TIME` | `FsGiWemExceptionDetails_AuditDateTime` | String |  |  |
