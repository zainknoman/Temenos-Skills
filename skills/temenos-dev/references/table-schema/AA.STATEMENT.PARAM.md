# AA.STATEMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.AA.STATEMENT.PARAM` in `AA_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.SP.PROP.CLASS` | `AaStatementParam_PropClass` |  |  |  |
| 2 | `AA.SP.RESERVED.1` | `AaStatementParam_Reserved1` |  |  |  |
| 3 | `AA.SP.PROP.NAME` | `AaStatementParam_PropName` |  |  |  |
| 4 | `AA.SP.PROP.DESC` | `AaStatementParam_PropDesc` |  |  |  |
| 5 | `AA.SP.INCLUDE.RB` | `AaStatementParam_IncludeRb` |  |  |  |
| 6 | `AA.SP.BAL.GROUP.NAME` | `AaStatementParam_BalGroupName` |  |  |  |
| 7 | `AA.SP.BAL.GROUP.DESC` | `AaStatementParam_BalGroupDesc` |  |  |  |
| 8 | `AA.SP.RESERVED.3` | `AaStatementParam_Reserved3` |  |  |  |
| 9 | `AA.SP.BAL.TYPE` | `AaStatementParam_BalType` |  |  |  |
| 10 | `AA.SP.BAL.GROUP` | `AaStatementParam_BalGroup` |  |  |  |
| 11 | `AA.SP.RESERVED.4` | `AaStatementParam_Reserved4` |  |  |  |
| 12 | `AA.SP.RESERVED.5` | `AaStatementParam_Reserved5` |  |  |  |
| 13 | `AA.SP.RESERVED.6` | `AaStatementParam_Reserved6` |  |  |  |
| 14 | `AA.SP.RESERVED.7` | `AaStatementParam_Reserved7` |  |  |  |
| 15 | `AA.SP.CR.NARR.COND` | `AaStatementParam_CrNarrCond` |  |  |  |
| 16 | `AA.SP.CR.NARR.TEXT` | `AaStatementParam_CrNarrText` |  |  |  |
| 17 | `AA.SP.RESERVED.8` | `AaStatementParam_Reserved8` |  |  |  |
| 18 | `AA.SP.DR.NARR.COND` | `AaStatementParam_DrNarrCond` |  |  |  |
| 19 | `AA.SP.DR.NARR.TEXT` | `AaStatementParam_DrNarrText` |  |  |  |
| 20 | `AA.SP.RESERVED.9` | `AaStatementParam_Reserved9` |  |  |  |
| 21 | `AA.SP.RESERVED.10` | `AaStatementParam_Reserved10` |  |  |  |
| 22 | `AA.SP.RESERVED.11` | `AaStatementParam_Reserved11` |  |  |  |
| 23 | `AA.SP.RESERVED.12` | `AaStatementParam_Reserved12` |  |  |  |
| 24 | `AA.SP.ATTRIBUTES` | `AaStatementParam_Attributes` |  |  |  |
| 25 | `AA.SP.HIDE.ACTIVITY` | `AaStatementParam_HideActivity` |  |  |  |
| 26 | `AA.SP.REVERSAL.CHARS` | `AaStatementParam_ReversalChars` | TField |  | Two characters to be used for marking reversal statement lines |
| 27 | `AA.SP.SPLIT.ACT.CLASS` | `AaStatementParam_SplitActClass` |  |  |  |
| 28 | `AA.SP.IN.ACT.CLASS` | `AaStatementParam_InActClass` |  |  |  |
| 29 | `AA.SP.PROC.RULE` | `AaStatementParam_ProcRule` |  |  |  |
| 30 | `AA.SP.MERG.ACTIVITY` | `AaStatementParam_MergActivity` |  |  |  |
| 31 | `AA.SP.WITH.ACTIVITY` | `AaStatementParam_WithActivity` |  |  |  |
| 32 | `AA.SP.LOCAL.REF` | `AaStatementParam_LocalRef` |  |  |  |
| 33 | `AA.SP.OVERRIDE` | `AaStatementParam_Override` |  |  |  |
| 34 | `AA.SP.RECORD.STATUS` | `AaStatementParam_RecordStatus` | String |  |  |
| 35 | `AA.SP.CURR.NO` | `AaStatementParam_CurrNo` | String |  |  |
| 36 | `AA.SP.INPUTTER` | `AaStatementParam_Inputter` |  |  |  |
| 37 | `AA.SP.DATE.TIME` | `AaStatementParam_DateTime` |  |  |  |
| 38 | `AA.SP.AUTHORISER` | `AaStatementParam_Authoriser` | String |  |  |
| 39 | `AA.SP.CO.CODE` | `AaStatementParam_CoCode` | String |  |  |
| 40 | `AA.SP.DEPT.CODE` | `AaStatementParam_DeptCode` | String |  |  |
| 41 | `AA.SP.AUDITOR.CODE` | `AaStatementParam_AuditorCode` | String |  |  |
| 42 | `AA.SP.AUDIT.DATE.TIME` | `AaStatementParam_AuditDateTime` | String |  |  |
| 43 | `AA.SP.INC.ACTIVITY` | `AaStatementParam_IncActivity` |  |  |  |
| 44 | `AA.SP.INC.NARR.FORMAT` | `AaStatementParam_IncNarrFormat` |  |  |  |
| 45 | `AA.SP.INC.RULE` | `AaStatementParam_IncRule` |  |  |  |
