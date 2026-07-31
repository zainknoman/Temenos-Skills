# PW.PROCESS.DEFINITION.CATALOGUE — Table Schema

> Source: `INSERTS/I_F.PW.PROCESS.DEFINITION.CATALOGUE` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.DEF.CATALOGUE.DESCRIPTION` | `PwProcessDefinitionCatalogue_Description` |  |  |  |
| 2 | `PW.DEF.CATALOGUE.SHORT.DESC` | `PwProcessDefinitionCatalogue_ShortDesc` |  |  |  |
| 3 | `PW.DEF.CATALOGUE.DEF.DURATION` | `PwProcessDefinitionCatalogue_DefDuration` | TField | Yes | PW.PROCESS.DEFINITION DEF.DURATION Default duration of this entire process in definable units. Validation Rules: 1-3 numeric characters. Mandatory field. |
| 4 | `PW.DEF.CATALOGUE.ACTIVITY` | `PwProcessDefinitionCatalogue_Activity` |  |  |  |
| 5 | `PW.DEF.CATALOGUE.PRE.REQ.VAR.NAME` | `PwProcessDefinitionCatalogue_PreReqVarName` |  |  |  |
| 6 | `PW.DEF.CATALOGUE.PRE.REQ.VAR.OPERAND` | `PwProcessDefinitionCatalogue_PreReqVarOperand` |  |  |  |
| 7 | `PW.DEF.CATALOGUE.PRE.REQ.VAR.VALUE` | `PwProcessDefinitionCatalogue_PreReqVarValue` |  |  |  |
| 8 | `PW.DEF.CATALOGUE.PRE.REQ.VAR.OPERATION` | `PwProcessDefinitionCatalogue_PreReqVarOperation` |  |  |  |
| 9 | `PW.DEF.CATALOGUE.PRE.REQ.ACT` | `PwProcessDefinitionCatalogue_PreReqAct` |  |  |  |
| 10 | `PW.DEF.CATALOGUE.PRE.REQ.STAT` | `PwProcessDefinitionCatalogue_PreReqStat` |  |  |  |
| 11 | `PW.DEF.CATALOGUE.PRE.REQ.RULE` | `PwProcessDefinitionCatalogue_PreReqRule` |  |  |  |
| 12 | `PW.DEF.CATALOGUE.OPERATION` | `PwProcessDefinitionCatalogue_Operation` |  |  |  |
| 13 | `PW.DEF.CATALOGUE.PRE.REQ.CONSTR` | `PwProcessDefinitionCatalogue_PreReqConstr` |  |  |  |
| 14 | `PW.DEF.CATALOGUE.UNIQUE.NAME` | `PwProcessDefinitionCatalogue_UniqueName` |  |  |  |
| 15 | `PW.DEF.CATALOGUE.TIME.TRIGGER` | `PwProcessDefinitionCatalogue_TimeTrigger` |  |  |  |
| 16 | `PW.DEF.CATALOGUE.FOLLOW.ON.ACT` | `PwProcessDefinitionCatalogue_FollowOnAct` |  |  |  |
| 17 | `PW.DEF.CATALOGUE.EB.MAPPING` | `PwProcessDefinitionCatalogue_EbMapping` |  |  |  |
| 18 | `PW.DEF.CATALOGUE.PRE.REQ.EVAL` | `PwProcessDefinitionCatalogue_PreReqEval` |  |  |  |
| 19 | `PW.DEF.CATALOGUE.RECU.EVAL.RULE` | `PwProcessDefinitionCatalogue_RecuEvalRule` |  |  |  |
| 20 | `PW.DEF.CATALOGUE.RECU.EVAL.COND` | `PwProcessDefinitionCatalogue_RecuEvalCond` |  |  |  |
| 21 | `PW.DEF.CATALOGUE.PATTERN.CONSTR` | `PwProcessDefinitionCatalogue_PatternConstr` |  |  |  |
| 22 | `PW.DEF.CATALOGUE.EVAL.CONDITION` | `PwProcessDefinitionCatalogue_EvalCondition` |  |  |  |
| 23 | `PW.DEF.CATALOGUE.EVAL.RULE` | `PwProcessDefinitionCatalogue_EvalRule` |  |  |  |
| 24 | `PW.DEF.CATALOGUE.ROUTE.TO.ACT` | `PwProcessDefinitionCatalogue_RouteToAct` |  |  |  |
| 25 | `PW.DEF.CATALOGUE.ROUTE.ACT.STATUS` | `PwProcessDefinitionCatalogue_RouteActStatus` |  |  |  |
| 26 | `PW.DEF.CATALOGUE.FLOW.ACT` | `PwProcessDefinitionCatalogue_FlowAct` |  |  |  |
| 27 | `PW.DEF.CATALOGUE.CASE.ACTIVITY` | `PwProcessDefinitionCatalogue_CaseActivity` |  |  |  |
| 28 | `PW.DEF.CATALOGUE.DEF.ACTIVITY` | `PwProcessDefinitionCatalogue_DefActivity` |  |  |  |
| 29 | `PW.DEF.CATALOGUE.ACTIVITY.OWNER` | `PwProcessDefinitionCatalogue_ActivityOwner` |  |  |  |
| 30 | `PW.DEF.CATALOGUE.RESERVED.12` | `PwProcessDefinitionCatalogue_Reserved12` |  |  |  |
| 31 | `PW.DEF.CATALOGUE.PROCESS.COMPLETION.STATUS` | `PwProcessDefinitionCatalogue_ProcessCompletionStatus` |  |  |  |
| 32 | `PW.DEF.CATALOGUE.ALLOWED.STATUS` | `PwProcessDefinitionCatalogue_AllowedStatus` |  |  |  |
| 33 | `PW.DEF.CATALOGUE.PROCESS.ACTIVITY` | `PwProcessDefinitionCatalogue_ProcessActivity` |  |  |  |
| 34 | `PW.DEF.CATALOGUE.ACTIVITY.STATUS` | `PwProcessDefinitionCatalogue_ActivityStatus` |  |  |  |
| 35 | `PW.DEF.CATALOGUE.PROCESS.CONSTR` | `PwProcessDefinitionCatalogue_ProcessConstr` |  |  |  |
| 36 | `PW.DEF.CATALOGUE.CONSTR.STATUS` | `PwProcessDefinitionCatalogue_ConstrStatus` |  |  |  |
| 37 | `PW.DEF.CATALOGUE.PROCESS.STATUS.RULE` | `PwProcessDefinitionCatalogue_ProcessStatusRule` |  |  |  |
| 38 | `PW.DEF.CATALOGUE.VERSION.ID` | `PwProcessDefinitionCatalogue_VersionId` | TField |  | PW.PROCESS.DEFINITION VERSION.ID Specifies the latest version of a process definition Validation Rules: This is a non-input field. Gets auto incremented by one when a process definition is published |
| 39 | `PW.DEF.CATALOGUE.PUBLISHED` | `PwProcessDefinitionCatalogue_Published` | TField |  | PW.PROCESS.DEFINITION PUBLISHED This field holds the information whether the particular process definition has been published Validation Rules: This is a non-input field. >When any changes are made to the PWD except DEF.VER.TO.USE field, this field changes to 'NO' This field changes to 'YES' when the process definition is published |
| 40 | `PW.DEF.CATALOGUE.RESERVED.1` | `PwProcessDefinitionCatalogue_Reserved1` | TField |  |  |
| 41 | `PW.DEF.CATALOGUE.OWNER` | `PwProcessDefinitionCatalogue_Owner` | TField |  | Specifies the user(s) who is/are privileged to execute the current process Validation Rules: : Input must have an existing code on PW.PARTICIPANT |
| 42 | `PW.DEF.CATALOGUE.PROC.STAT.EVAL` | `PwProcessDefinitionCatalogue_ProcStatEval` | TField | No | This can accept any valid keys of EB.RULE.GATEWAY. This is mutually exclusive with ALLOWED.STATUS, PROCESS.ACTIVITY, ACTIVITY.STATUS adn PROCESS.STATUS.RULE multi-value field set. Validation Rules: 0-35 characters Optional field |
| 43 | `PW.DEF.CATALOGUE.SLA` | `PwProcessDefinitionCatalogue_Sla` | TField |  | PW.PROCESS.DEFINITION SLA This field is used to define a SLA(Service Level Agreement) for the process. INPUT only when SG product is installed otherwise NOINPUT. Validation Rules: Up to 35 alphanumeric characters. Must be a valid record from SG.SLA application. |
| 44 | `PW.DEF.CATALOGUE.PROCESS.XML` | `PwProcessDefinitionCatalogue_ProcessXml` | TField |  | Contains the project name of the process model as defined in the plug-in user interface. |
| 45 | `PW.DEF.CATALOGUE.PROCESS.VAR.TYPE` | `PwProcessDefinitionCatalogue_ProcessVarType` |  |  |  |
| 46 | `PW.DEF.CATALOGUE.PROCESS.VAR.NAME` | `PwProcessDefinitionCatalogue_ProcessVarName` |  |  |  |
| 47 | `PW.DEF.CATALOGUE.PROCESS.VAR.VALUE` | `PwProcessDefinitionCatalogue_ProcessVarValue` |  |  |  |
| 48 | `PW.DEF.CATALOGUE.LOCAL.REF` | `PwProcessDefinitionCatalogue_LocalRef` |  |  |  |
| 49 | `PW.DEF.CATALOGUE.OVERRIDE` | `PwProcessDefinitionCatalogue_Override` |  |  |  |
| 50 | `PW.DEF.CATALOGUE.RECORD.STATUS` | `PwProcessDefinitionCatalogue_RecordStatus` | String |  |  |
| 51 | `PW.DEF.CATALOGUE.CURR.NO` | `PwProcessDefinitionCatalogue_CurrNo` | String |  |  |
| 52 | `PW.DEF.CATALOGUE.INPUTTER` | `PwProcessDefinitionCatalogue_Inputter` |  |  |  |
| 53 | `PW.DEF.CATALOGUE.DATE.TIME` | `PwProcessDefinitionCatalogue_DateTime` |  |  |  |
| 54 | `PW.DEF.CATALOGUE.AUTHORISER` | `PwProcessDefinitionCatalogue_Authoriser` | String |  |  |
| 55 | `PW.DEF.CATALOGUE.CO.CODE` | `PwProcessDefinitionCatalogue_CoCode` | String |  |  |
| 56 | `PW.DEF.CATALOGUE.DEPT.CODE` | `PwProcessDefinitionCatalogue_DeptCode` | String |  |  |
| 57 | `PW.DEF.CATALOGUE.AUDITOR.CODE` | `PwProcessDefinitionCatalogue_AuditorCode` | String |  |  |
| 58 | `PW.DEF.CATALOGUE.AUDIT.DATE.TIME` | `PwProcessDefinitionCatalogue_AuditDateTime` | String |  |  |
| 59 | `PW.DEF.CATALOGUE.INFLOW.PROCESS` | `PwProcessDefinitionCatalogue_InflowProcess` | TField |  |  |
| 60 | `PW.DEF.CATALOGUE.OPEN.BRACKET` | `PwProcessDefinitionCatalogue_OpenBracket` |  |  |  |
| 61 | `PW.DEF.CATALOGUE.CLOSE.BRACKET` | `PwProcessDefinitionCatalogue_CloseBracket` |  |  |  |
