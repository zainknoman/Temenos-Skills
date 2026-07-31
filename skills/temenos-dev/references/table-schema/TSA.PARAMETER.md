# TSA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TSA.PARAMETER` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TS.PARM.REVIEW.TIME` | `TsaParameter_ReviewTime` | TField |  | This field holds the review time by the Service Manager of all the agents that are running currently. The system does a periodical review of all the agents running in the system. The delay time during every review can be specified in this field. Validation Rules: Numeric Value - (3 digits) |
| 2 | `TS.PARM.DEATH.WATCH` | `TsaParameter_DeathWatch` | TField |  | This field holds the seconds for the death watch. The system if it does not find a contact with a particular agent for a time greater than the death watch will mark the particular agent as DEAD. The Service Manager will review the response from every agent and will act upon agents that don't respond for a given period of time. Validation Rules: Up to 3 digits numeric value. |
| 3 | `TS.PARM.HIGHEST.AGENT` | `TsaParameter_HighestAgent` | TField |  | This field holds the highest agent that is running as a part of TSA.SERVICE. The system while starting every agent for different service updates the highest number of agent in this field. Validation Rules: System maintained NOINPUT field. |
| 4 | `TS.PARM.STOPPAGE.TIME` | `TsaParameter_StoppageTime` | TField | Yes | Time interval specified for a service to be monitored for the number of crashes as specified in the field STOP.COUNT. Validation Rules: : 1. Non-mandatory field, accepts numeric value 2. STOPPAGE.TIME should be greater than the time specified in TIME.OUT 4. If DEATH.WATCH time is left blank then STOPPAGE.TIME should be greater than the default time 300. |
| 5 | `TS.PARM.STOP.COUNT` | `TsaParameter_StopCount` | TField | Yes | Number of crashed that is allowed for a service in a time period as specified in the field STOPPAGE.TIME. 1.Non-mandatory field, accepts numeric value 2.If this field is allowed to input only when STOPPAGE.TIME field is specified. e.g. STOPPAGE.TIME = 80 STOP.COUNT = 2 Here the Service can have 2 crashes in a time period of 80 seconds. At the third crash within 80 seconds, Service will be stopped. |
| 6 | `TS.PARM.SELECT.DEATH.WATCH` | `TsaParameter_SelectDeathWatch` | TField |  |  |
| 7 | `TS.PARM.DATE.CHANGE.COB.LINK` | `TsaParameter_DateChangeCobLink` | TField |  | This field is to enable the date change service functionality for TI clients.When the field is set to 'YES' and TI.DATE.CHANGE.SERVICE is started/stopped, corresponding COB record is started/stopped. Validation Rules: When date change is enabled, COB service record cannot be accessed directly. When field is "NO" or "NULL", date change service is not enabled and COB record is considered |
| 8 | `TS.PARM.DYNAMIC.PROVISIONING` | `TsaParameter_DynamicProvisioning` | TField |  | This field is to enable dynamic provisioning feature for cloud deployments This will enable the automatic UpScaling and DownScaling of agents based on the elastic attributes defined in workload profile Validation Rules Valid input Yes or Null Deployment mode field should be set to CLOUD in SPF record to enable this field. |
| 9 | `TS.PARM.QUEUE.JOBS` | `TsaParameter_QueueJobs` |  |  |  |
| 10 | `TS.PARM.BUSINESS.STAGE.COB` | `TsaParameter_BusinessStageCob` |  |  |  |
| 11 | `TS.PARM.COMMIT.SIZE` | `TsaParameter_CommitSize` | TField |  | The value in this field will be considered as a factor for determining commit number for queue jobs during select stage |
| 12 | `TS.PARM.LOCAL.REF` | `TsaParameter_LocalRef` |  |  |  |
| 13 | `TS.PARM.RECORD.STATUS` | `TsaParameter_RecordStatus` | String |  |  |
| 14 | `TS.PARM.CURR.NO` | `TsaParameter_CurrNo` | String |  |  |
| 15 | `TS.PARM.INPUTTER` | `TsaParameter_Inputter` |  |  |  |
| 16 | `TS.PARM.DATE.TIME` | `TsaParameter_DateTime` |  |  |  |
| 17 | `TS.PARM.AUTHORISER` | `TsaParameter_Authoriser` | String |  |  |
| 18 | `TS.PARM.CO.CODE` | `TsaParameter_CoCode` | String |  |  |
| 19 | `TS.PARM.DEPT.CODE` | `TsaParameter_DeptCode` | String |  |  |
| 20 | `TS.PARM.AUDITOR.CODE` | `TsaParameter_AuditorCode` | String |  |  |
| 21 | `TS.PARM.AUDIT.DATE.TIME` | `TsaParameter_AuditDateTime` | String |  |  |
| 22 | `TS.PARM.LOCK.RETRY.THRESHOLD` | `TsaParameter_LockRetryThreshold` | TField |  | This field is to enable effective utilisation of agents for non-locking batches. added to specify the maximum number of times we must keep trying to run the same BATCH before skipping to the next BATCH in the same stage Validation Rules: : It should be a valid numeric value lesser than 11 digits |
| 23 | `TS.PARM.STOP.ALL.AGENTS` | `TsaParameter_StopAllAgents` | TField |  | This field if enabled, will stop all the agents currently running in cloud deployment Validation Rules Valid input Yes or Null Dynamic provisioning field in TSA.PARAMETER should be enabled for this field. |
| 24 | `TS.PARM.DEFAULT.WORK.PROFILE` | `TsaParameter_DefaultWorkProfile` | TField |  |  |
| 25 | `TS.PARM.DEFAULT.USER` | `TsaParameter_DefaultUser` | TField |  |  |
| 26 | `TS.PARM.PACKAGE.DEPLOYMENT` | `TsaParameter_PackageDeployment` | TField |  | This field when set to ACTIVE, indicates that the package deployment mode is activated and that no other services should be allowed to be started till this is completed. Only those service which have the attribute "RUN.AT.DEPLOY" set to "YES" will be considered. Validation Rules Valid input Active or Null Not allowed when there are currently running non deployment services. |
| 27 | `TS.PARM.ATTRIBUTE.NAME` | `TsaParameter_AttributeName` |  |  |  |
| 28 | `TS.PARM.ATTRIBUTE.VALUE` | `TsaParameter_AttributeValue` |  |  |  |
| 29 | `TS.PARM.UPGRADE.IMAGE` | `TsaParameter_UpgradeImage` | TField |  |  |
| 30 | `TS.PARM.INACTIVE.IMAGE` | `TsaParameter_InactiveImage` | TField |  | This field if enabled,is used to identify the inactive image to provide smooth exit of agents for switch over period Validation Rules Dynamic provisioning field in TSA.PARAMETER should be enabled for this field. |
| 31 | `TS.PARM.VERIFICATION.INTERVAL.REQD` | `TsaParameter_VerificationIntervalReqd` | TField |  | This field if set would enable verification interval during online upgrade Validation Rules Valid input Yes or Null Dynamic provisioning field in TSA.PARAMETER should be enabled for this field. |
