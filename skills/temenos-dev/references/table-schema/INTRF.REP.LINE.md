# INTRF.REP.LINE — Table Schema

> Source: `INSERTS/I_F.INTRF.REP.LINE` in `CANVSN_Navision.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INTRF.RL.LINE.BALANCE` | `IntrfRepLine_LineBalance` | TField |  | Purpose of the field is used to define whether the extract should display the summary or Detail.If summary is defined then system will display the overall summary of the balance.IF Detail is defined the system will display the full detial about the PL/AL details.Allowed values are Detail / Summary |
| 2 | `INTRF.RL.DETAIL.TYPE` | `IntrfRepLine_DetailType` |  |  |  |
| 3 | `INTRF.RL.DESC` | `IntrfRepLine_Desc` |  |  |  |
| 4 | `INTRF.RL.AL.PL` | `IntrfRepLine_AlPl` | TField |  | Purpose of the field is used to define the whether the extract should consider the AL or PL consol.If AL (Assets &amp; Liabilities) is defined then the line is considered as AL line.If PL (Profit &amp; Loss) is defiend then the line is considered as PL line. |
| 5 | `INTRF.RL.TERM` | `IntrfRepLine_Term` | TField |  |  |
| 6 | `INTRF.RL.DESC.MAPPING` | `IntrfRepLine_DescMapping` | TField |  | This field holds the description mapping for the Navision Extract |
| 7 | `INTRF.RL.SYSTEM.ID` | `IntrfRepLine_SystemId` |  |  |  |
| 8 | `INTRF.RL.INTF.FIELD.NAME` | `IntrfRepLine_IntfFieldName` |  |  |  |
| 9 | `INTRF.RL.APPL.FIELD.NAME` | `IntrfRepLine_ApplFieldName` |  |  |  |
| 10 | `INTRF.RL.CONV.PARAM` | `IntrfRepLine_ConvParam` |  |  |  |
| 11 | `INTRF.RL.CONV.FUNC` | `IntrfRepLine_ConvFunc` |  |  |  |
| 12 | `INTRF.RL.RESERVED.3` | `IntrfRepLine_Reserved3` | TField |  |  |
| 13 | `INTRF.RL.RESERVED.2` | `IntrfRepLine_Reserved2` | TField |  |  |
| 14 | `INTRF.RL.RESERVED.1` | `IntrfRepLine_Reserved1` | TField |  |  |
| 15 | `INTRF.RL.LOCAL.REF` | `IntrfRepLine_LocalRef` |  |  |  |
| 16 | `INTRF.RL.OVERRIDE` | `IntrfRepLine_Override` |  |  |  |
| 17 | `INTRF.RL.RECORD.STATUS` | `IntrfRepLine_RecordStatus` | String |  |  |
| 18 | `INTRF.RL.CURR.NO` | `IntrfRepLine_CurrNo` | String |  |  |
| 19 | `INTRF.RL.INPUTTER` | `IntrfRepLine_Inputter` |  |  |  |
| 20 | `INTRF.RL.DATE.TIME` | `IntrfRepLine_DateTime` |  |  |  |
| 21 | `INTRF.RL.AUTHORISER` | `IntrfRepLine_Authoriser` | String |  |  |
| 22 | `INTRF.RL.CO.CODE` | `IntrfRepLine_CoCode` | String |  |  |
| 23 | `INTRF.RL.DEPT.CODE` | `IntrfRepLine_DeptCode` | String |  |  |
| 24 | `INTRF.RL.AUDITOR.CODE` | `IntrfRepLine_AuditorCode` | String |  |  |
| 25 | `INTRF.RL.AUDIT.DATE.TIME` | `IntrfRepLine_AuditDateTime` | String |  |  |
