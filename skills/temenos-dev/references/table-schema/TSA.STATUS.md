# TSA.STATUS — Table Schema

> Source: `INSERTS/I_F.TSA.STATUS` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TS.TSS.SERVER` | `TsaStatus_Server` | TField |  | The server on which the service Agent is running. This will be a valid server name in the system. Validation Rules: |
| 2 | `TS.TSS.AGENT.STATUS` | `TsaStatus_AgentStatus` | TField |  | The status of the current agent. This will store whether the agent is running of whether it has stopped. Validation Rules: |
| 3 | `TS.TSS.LAST.CONTACT` | `TsaStatus_LastContact` | TField |  | This field is updated by the Service Manager. This contains the last time a contact was made by the system to this agent. Validation Rules: |
| 4 | `TS.TSS.PROCESS.ID` | `TsaStatus_ProcessId` | TField |  | The process id of the current agent. This field contains the unique reference of the process that has been initiated by the current agent. Validation Rules: |
| 5 | `TS.TSS.CURRENT.SERVICE` | `TsaStatus_CurrentService` | TField |  | This field contains the service that is being run currently by the agent. Validation Rules: |
| 6 | `TS.TSS.NEXT.SERVICE` | `TsaStatus_NextService` | TField |  | This field contains the service that has been scheduled to run by the agent next. Validation Rules: |
| 7 | `TS.TSS.LAST.MESSAGE` | `TsaStatus_LastMessage` | TField |  | This field is updated by the Service Manager.This field holds the last output from the COMO. Gets updated when LAST.CONTACT time is updated. |
| 8 | `TS.TSS.COMO.NAME` | `TsaStatus_ComoName` | TField |  | This field holds the como name of the current agent. Validation Rules: Upto 30 character |
| 9 | `TS.TSS.JOB.PROGRESS` | `TsaStatus_JobProgress` | TField |  | This field tells in which stage of job processing we are in. Can hold the below values. 1=Processing Contracts 2=Selecting Contracts 3=Managing Control List 4=Selecting list file 5=Managing Batch record (in S.JOB.RUN) 6=Waiting on list record 7=Processing Single threaded |
| 10 | `TS.TSS.PORT.ID` | `TsaStatus_PortId` | TField |  | This field stores the jBASE port number on which the service agent is running. Validation Rules: |
| 11 | `TS.TSS.OPENS` | `TsaStatus_Opens` | TField |  | Number of Opens performed in this session. It is taken from SYSTEM(1027) |
| 12 | `TS.TSS.READS` | `TsaStatus_Reads` | TField |  | Number of Reads performed in this session. It is taken from SYSTEM(1027) |
| 13 | `TS.TSS.WRITES` | `TsaStatus_Writes` | TField |  | Number of Writes performed in this session. It is taken from SYSTEM(1027) |
| 14 | `TS.TSS.INPUTS` | `TsaStatus_Inputs` | TField |  | Number of Inputs performed in this session. It is taken from SYSTEM(1027) |
| 15 | `TS.TSS.EXECUTES` | `TsaStatus_Executes` | TField |  | Number of Executes performed in this session. It is taken from SYSTEM(1027) |
| 16 | `TS.TSS.DELETES` | `TsaStatus_Deletes` | TField |  | Number of Deletes performed in this session. It is taken from SYSTEM(1027) |
| 17 | `TS.TSS.CLEARFILES` | `TsaStatus_Clearfiles` | TField |  | Number of Clear files performed in this session. It is taken from SYSTEM(1027) |
| 18 | `TS.TSS.MEMORY` | `TsaStatus_Memory` | TField |  | Memory used in this session. It is taken from SYSTEM(1027) |
| 19 | `TS.TSS.T24.SESSION.NO` | `TsaStatus_T24SessionNo` | TField |  | The T24 Session Id generated unique to the session. This field contains the ID of T24.SESSION |
| 20 | `TS.TSS.SELECT.JOB` | `TsaStatus_SelectJob` | TField |  |  |
