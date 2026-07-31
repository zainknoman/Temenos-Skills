# PW.PROCESS.DEFINITION — Table Schema

> Source: `INSERTS/I_F.PW.PROCESS.DEFINITION` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.DEF.DESCRIPTION` | `PwProcessDefinition_Description` |  |  |  |
| 2 | `PW.DEF.SHORT.DESC` | `PwProcessDefinition_ShortDesc` |  |  |  |
| 3 | `PW.DEF.DEF.DURATION` | `PwProcessDefinition_DefDuration` | TField | Yes | PW.PROCESS.DEFINITION DEF.DURATION Default duration of this entire process in definable units. Validation Rules: 1-3 numeric characters. Mandatory field. |
| 4 | `PW.DEF.ACTIVITY` | `PwProcessDefinition_Activity` |  |  |  |
| 5 | `PW.DEF.PRE.REQ.VAR.NAME` | `PwProcessDefinition_PreReqVarName` |  |  |  |
| 6 | `PW.DEF.PRE.REQ.VAR.OPERAND` | `PwProcessDefinition_PreReqVarOperand` |  |  |  |
| 7 | `PW.DEF.PRE.REQ.VAR.VALUE` | `PwProcessDefinition_PreReqVarValue` |  |  |  |
| 8 | `PW.DEF.PRE.REQ.VAR.OPERATION` | `PwProcessDefinition_PreReqVarOperation` |  |  |  |
| 9 | `PW.DEF.PRE.REQ.ACT` | `PwProcessDefinition_PreReqAct` |  |  |  |
| 10 | `PW.DEF.PRE.REQ.STAT` | `PwProcessDefinition_PreReqStat` |  |  |  |
| 11 | `PW.DEF.PRE.REQ.RULE` | `PwProcessDefinition_PreReqRule` |  |  |  |
| 12 | `PW.DEF.OPERATION` | `PwProcessDefinition_Operation` |  |  |  |
| 13 | `PW.DEF.PRE.REQ.CONSTR` | `PwProcessDefinition_PreReqConstr` |  |  |  |
| 14 | `PW.DEF.UNIQUE.NAME` | `PwProcessDefinition_UniqueName` |  |  |  |
| 15 | `PW.DEF.TIME.TRIGGER` | `PwProcessDefinition_TimeTrigger` |  |  |  |
| 16 | `PW.DEF.FOLLOW.ON.ACT` | `PwProcessDefinition_FollowOnAct` |  |  |  |
| 17 | `PW.DEF.EB.MAPPING` | `PwProcessDefinition_EbMapping` |  |  |  |
| 18 | `PW.DEF.PRE.REQ.EVAL` | `PwProcessDefinition_PreReqEval` |  |  |  |
| 19 | `PW.DEF.RECU.EVAL.RULE` | `PwProcessDefinition_RecuEvalRule` |  |  |  |
| 20 | `PW.DEF.RECU.EVAL.COND` | `PwProcessDefinition_RecuEvalCond` |  |  |  |
| 21 | `PW.DEF.PATTERN.CONSTR` | `PwProcessDefinition_PatternConstr` |  |  |  |
| 22 | `PW.DEF.EVAL.CONDITION` | `PwProcessDefinition_EvalCondition` |  |  |  |
| 23 | `PW.DEF.EVAL.RULE` | `PwProcessDefinition_EvalRule` |  |  |  |
| 24 | `PW.DEF.ROUTE.TO.ACT` | `PwProcessDefinition_RouteToAct` |  |  |  |
| 25 | `PW.DEF.ROUTE.ACT.STATUS` | `PwProcessDefinition_RouteActStatus` |  |  |  |
| 26 | `PW.DEF.FLOW.ACT` | `PwProcessDefinition_FlowAct` |  |  |  |
| 27 | `PW.DEF.CASE.ACTIVITY` | `PwProcessDefinition_CaseActivity` |  |  |  |
| 28 | `PW.DEF.DEF.ACTIVITY` | `PwProcessDefinition_DefActivity` |  |  |  |
| 29 | `PW.DEF.ACTIVITY.OWNER` | `PwProcessDefinition_ActivityOwner` |  |  |  |
| 30 | `PW.DEF.RESERVED.12` | `PwProcessDefinition_Reserved12` |  |  |  |
| 31 | `PW.DEF.PROCESS.COMPLETION.STATUS` | `PwProcessDefinition_ProcessCompletionStatus` |  |  |  |
| 32 | `PW.DEF.ALLOWED.STATUS` | `PwProcessDefinition_AllowedStatus` |  |  |  |
| 33 | `PW.DEF.PROCESS.ACTIVITY` | `PwProcessDefinition_ProcessActivity` |  |  |  |
| 34 | `PW.DEF.ACTIVITY.STATUS` | `PwProcessDefinition_ActivityStatus` |  |  |  |
| 35 | `PW.DEF.PROCESS.CONSTR` | `PwProcessDefinition_ProcessConstr` |  |  |  |
| 36 | `PW.DEF.CONSTR.STATUS` | `PwProcessDefinition_ConstrStatus` |  |  |  |
| 37 | `PW.DEF.PROCESS.STATUS.RULE` | `PwProcessDefinition_ProcessStatusRule` |  |  |  |
| 38 | `PW.DEF.VERSION.ID` | `PwProcessDefinition_VersionId` | TField |  | PW.PROCESS.DEFINITION VERSION.ID Specifies the latest version of a process definition Validation Rules: This is a non-input field. Gets auto incremented by one when a process definition is published |
| 39 | `PW.DEF.PUBLISHED` | `PwProcessDefinition_Published` | TField |  | PW.PROCESS.DEFINITION PUBLISHED This field holds the information whether the particular process definition has been published Validation Rules: This is a non-input field. Can take values �YES�, �NO� When any changes are made to the PWD except DEF.VER.TO.USE field, this field changes to 'NO' This field changes to 'YES' when the process definition is published |
| 40 | `PW.DEF.RESERVED.1` | `PwProcessDefinition_Reserved1` | TField |  |  |
| 41 | `PW.DEF.OWNER` | `PwProcessDefinition_Owner` | TField |  | Specifies the user(s) who is/are privileged to execute the current process Validation Rules: : Input must have an existing code on PW.PARTICIPANT |
| 42 | `PW.DEF.PROC.STAT.EVAL` | `PwProcessDefinition_ProcStatEval` | TField | No | This can accept any valid keys of EB.RULE.GATEWAY. This is mutually exclusive with ALLOWED.STATUS, PROCESS.ACTIVITY, ACTIVITY.STATUS adn PROCESS.STATUS.RULE multi-value field set. Validation Rules: 0-35 characters Optional field |
| 43 | `PW.DEF.SLA` | `PwProcessDefinition_Sla` | TField |  | PW.PROCESS.DEFINITION SLA This field is used to define a SLA(Service Level Agreement) for the process. INPUT only when SG product is installed otherwise NOINPUT. Validation Rules: Up to 35 alphanumeric characters. Must be a valid record from SG.SLA application. |
| 44 | `PW.DEF.PROCESS.XML` | `PwProcessDefinition_ProcessXml` | TField |  | Contains the project name of the process model as defined in the plug-in user interface. |
| 45 | `PW.DEF.PROCESS.VAR.TYPE` | `PwProcessDefinition_ProcessVarType` |  |  |  |
| 46 | `PW.DEF.PROCESS.VAR.NAME` | `PwProcessDefinition_ProcessVarName` |  |  |  |
| 47 | `PW.DEF.PROCESS.VAR.VALUE` | `PwProcessDefinition_ProcessVarValue` |  |  |  |
| 48 | `PW.DEF.LOCAL.REF` | `PwProcessDefinition_LocalRef` |  |  |  |
| 49 | `PW.DEF.OVERRIDE` | `PwProcessDefinition_Override` |  |  |  |
| 50 | `PW.DEF.RECORD.STATUS` | `PwProcessDefinition_RecordStatus` | String |  |  |
| 51 | `PW.DEF.CURR.NO` | `PwProcessDefinition_CurrNo` | String |  |  |
| 52 | `PW.DEF.INPUTTER` | `PwProcessDefinition_Inputter` |  |  |  |
| 53 | `PW.DEF.DATE.TIME` | `PwProcessDefinition_DateTime` |  |  |  |
| 54 | `PW.DEF.AUTHORISER` | `PwProcessDefinition_Authoriser` | String |  |  |
| 55 | `PW.DEF.CO.CODE` | `PwProcessDefinition_CoCode` | String |  |  |
| 56 | `PW.DEF.DEPT.CODE` | `PwProcessDefinition_DeptCode` | String |  |  |
| 57 | `PW.DEF.AUDITOR.CODE` | `PwProcessDefinition_AuditorCode` | String |  |  |
| 58 | `PW.DEF.AUDIT.DATE.TIME` | `PwProcessDefinition_AuditDateTime` | String |  |  |
| 59 | `PW.DEF.INFLOW.PROCESS` | `PwProcessDefinition_InflowProcess` | TField |  |  |
| 60 | `PW.DEF.OPEN.BRACKET` | `PwProcessDefinition_OpenBracket` |  |  |  |
| 61 | `PW.DEF.CLOSE.BRACKET` | `PwProcessDefinition_CloseBracket` |  |  |  |
