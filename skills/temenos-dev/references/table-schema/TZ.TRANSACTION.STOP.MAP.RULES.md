# TZ.TRANSACTION.STOP.MAP.RULES — Table Schema

> Source: `INSERTS/I_F.TZ.TRANSACTION.STOP.MAP.RULES` in `TZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TZ.TSMR.APPLICATION.NAME` | `TzTransactionStopMapRules_ApplicationName` | TField |  | This will be the first part of the ID, before the * for which the Mapping rules are being defined Validation Rule: Should be valid T24 Application |
| 2 | `TZ.TSMR.QUALIFIER.FIELD` | `TzTransactionStopMapRules_QualifierField` |  |  |  |
| 3 | `TZ.TSMR.QUALIFIER.OPERAND` | `TzTransactionStopMapRules_QualifierOperand` |  |  |  |
| 4 | `TZ.TSMR.VALUE` | `TzTransactionStopMapRules_Value` |  |  |  |
| 5 | `TZ.TSMR.VALUE.START` | `TzTransactionStopMapRules_ValueStart` |  |  |  |
| 6 | `TZ.TSMR.VALUE.END` | `TzTransactionStopMapRules_ValueEnd` |  |  |  |
| 7 | `TZ.TSMR.STOP.TYPE` | `TzTransactionStopMapRules_StopType` | TField |  | This field will be used to indicate the Stop Type/Channel represented by this transaction e.g ACH, Cheque clearing, etc Validation Rule: Should be a valid record id in TRASACTION.STOP.TYPE |
| 8 | `TZ.TSMR.ACCOUNT.FIELD` | `TzTransactionStopMapRules_AccountField` | TField |  | This is the field available in the application from where account details can be extracted. For example, DEBIT.ACCT.NO/CREDIT.ACCT.NO in Funds Transfer. This account detail is used to get the Transaction stop Instruction types for cross verification. Validation Rule: Fields defined in T24 for the application mentioned in the APPLICATION field are the only allowed values. |
| 9 | `TZ.TSMR.MATCH.ATTR` | `TzTransactionStopMapRules_MatchAttr` |  |  |  |
| 10 | `TZ.TSMR.MATCH.ATTR.EXT` | `TzTransactionStopMapRules_MatchAttrExt` |  |  |  |
| 11 | `TZ.TSMR.LINKED.APPLN` | `TzTransactionStopMapRules_LinkedAppln` |  |  |  |
| 12 | `TZ.TSMR.LINKED.BY` | `TzTransactionStopMapRules_LinkedBy` |  |  |  |
| 13 | `TZ.TSMR.LINKED.MATCH.ATTR` | `TzTransactionStopMapRules_LinkedMatchAttr` |  |  |  |
| 14 | `TZ.TSMR.LINKED.MATCH.ATTR.EXT` | `TzTransactionStopMapRules_LinkedMatchAttrExt` |  |  |  |
| 15 | `TZ.TSMR.HOOK.API` | `TzTransactionStopMapRules_HookApi` | TField |  | Field to attach any API routines for processing/modifications of transaction involved Attributes and Values taken during processing Arguments: MapRulesAttributes - Input - Contains the Attributes defined MapRulesAttributeValues - Input - Contains Attributes values - Output - Contains Processed Attributes values ReturnInfo Spare1 Spare2 Spare3 Validation Rule: Should have an Entry in EB.API |
| 16 | `TZ.TSMR.LOCAL.REF` | `TzTransactionStopMapRules_LocalRef` |  |  |  |
| 17 | `TZ.TSMR.OVERRIDE` | `TzTransactionStopMapRules_Override` |  |  |  |
| 18 | `TZ.TSMR.RECORD.STATUS` | `TzTransactionStopMapRules_RecordStatus` | String |  |  |
| 19 | `TZ.TSMR.CURR.NO` | `TzTransactionStopMapRules_CurrNo` | String |  |  |
| 20 | `TZ.TSMR.INPUTTER` | `TzTransactionStopMapRules_Inputter` |  |  |  |
| 21 | `TZ.TSMR.DATE.TIME` | `TzTransactionStopMapRules_DateTime` |  |  |  |
| 22 | `TZ.TSMR.AUTHORISER` | `TzTransactionStopMapRules_Authoriser` | String |  |  |
| 23 | `TZ.TSMR.CO.CODE` | `TzTransactionStopMapRules_CoCode` | String |  |  |
| 24 | `TZ.TSMR.DEPT.CODE` | `TzTransactionStopMapRules_DeptCode` | String |  |  |
| 25 | `TZ.TSMR.AUDITOR.CODE` | `TzTransactionStopMapRules_AuditorCode` | String |  |  |
| 26 | `TZ.TSMR.AUDIT.DATE.TIME` | `TzTransactionStopMapRules_AuditDateTime` | String |  |  |
| 27 | `TZ.TSMR.MATCH.ATTR.COND.FLD` | `TzTransactionStopMapRules_MatchAttrCondFld` |  |  |  |
| 28 | `TZ.TSMR.MATCH.ATTR.COND.OPR` | `TzTransactionStopMapRules_MatchAttrCondOpr` |  |  |  |
| 29 | `TZ.TSMR.MATCH.ATTR.COND.VAL` | `TzTransactionStopMapRules_MatchAttrCondVal` |  |  |  |
| 30 | `TZ.TSMR.LINKED.MATCH.COND.FLD` | `TzTransactionStopMapRules_LinkedMatchCondFld` |  |  |  |
| 31 | `TZ.TSMR.LINKED.MATCH.COND.OPR` | `TzTransactionStopMapRules_LinkedMatchCondOpr` |  |  |  |
| 32 | `TZ.TSMR.LINKED.MATCH.COND.VAL` | `TzTransactionStopMapRules_LinkedMatchCondVal` |  |  |  |
| 33 | `TZ.TSMR.PURPOSE` | `TzTransactionStopMapRules_Purpose` | TField |  | Purpose, will be added in this table to indicate the purpose of the rule. For now the Purpose field in the TZ.TRANSACTION.STOP.MAPP.RULES will support two values, but this can be extended in future: TransStop - will indicate the purpose of this rule is Transaction Stop Check RegReport - will indicate the purpose of this rule is to capture the payment regulatory reporting details The Purpose field will be automatically populated based on the third value in the ID, after the second *. If only one * is specified the Purpose will be considered as blank it'll be updated as TranStop |
