# FS.GA.NAV.CONTROL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CONTROL.PARAMETER` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CONTROL.PARAMETER.PARENT.REF.ID` | `FsGaNavControlParameter_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CONTROL.PARAMETER.ORA.ROWID` | `FsGaNavControlParameter_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CONTROL.PARAMETER.SEQUENCE.NO` | `FsGaNavControlParameter_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 4 | `FS.GA.NAV.CONTROL.PARAMETER.CONTROL.NUMBER` | `FsGaNavControlParameter_ControlNumber` | TField |  | Control Number linked to Process Multifonds DB Column is TYP_CONTROLE. |
| 5 | `FS.GA.NAV.CONTROL.PARAMETER.TYPE.OF.EXCEPTION.MONITOR` | `FsGaNavControlParameter_TypeOfExceptionMonitor` | TField |  | Refers to different Type of Exceptions. E.g., Amount, Percent, or Percentage of the Portfolio etc. Multifonds DB Column is TYP_CONNAV. |
| 6 | `FS.GA.NAV.CONTROL.PARAMETER.OPERATOR.CODE` | `FsGaNavControlParameter_OperatorCode` | TField |  | In this field user can choose the parameter to define the NAV Control Parameter. Like &lt;(less than) =(equal to) &gt;(greater than) etc Multifonds DB Column is COD_OPERATION1. |
| 7 | `FS.GA.NAV.CONTROL.PARAMETER.VALUES` | `FsGaNavControlParameter_Values` | TField |  | This field refers to the value of the control parameter which can be represented in forms of number like amount, %, or quantity etc Multifonds DB Column is NOMBRE1. |
| 8 | `FS.GA.NAV.CONTROL.PARAMETER.CURRENCY.1` | `FsGaNavControlParameter_Currency1` | TField |  | Currnecy code 1 Multifonds DB Column is CMON1. |
| 9 | `FS.GA.NAV.CONTROL.PARAMETER.OPERATOR2` | `FsGaNavControlParameter_Operator2` | TField |  | Operator2 Multifonds DB Column is COD_OPERATION2. |
| 10 | `FS.GA.NAV.CONTROL.PARAMETER.VALUE2` | `FsGaNavControlParameter_Value2` | TField |  | Value2 Multifonds DB Column is NOMBRE2. |
| 11 | `FS.GA.NAV.CONTROL.PARAMETER.CURRENCY.2` | `FsGaNavControlParameter_Currency2` | TField |  | Currnecy code 2 Multifonds DB Column is CMON2. |
| 12 | `FS.GA.NAV.CONTROL.PARAMETER.ERROR.TYPE` | `FsGaNavControlParameter_ErrorType` | TField |  | It displays the type of error like -Fatal, Warning &amp; Fatal at NAV accounting Multifonds DB Column is TYP_ERROR. |
| 13 | `FS.GA.NAV.CONTROL.PARAMETER.ALL.FUND` | `FsGaNavControlParameter_AllFund` | TField |  | The tick box is activated to define default tolerances. Multifonds DB Column is ALL_FUNDS. |
| 14 | `FS.GA.NAV.CONTROL.PARAMETER.TYPE.OF.TOLERANCE` | `FsGaNavControlParameter_TypeOfTolerance` | TField |  | 1 - Absolute Value 2 - Pct. NAV Tolerance Multifonds DB Column is ABSOLUTE_PCT_VALUE. |
| 15 | `FS.GA.NAV.CONTROL.PARAMETER.SEQUENCE` | `FsGaNavControlParameter_Sequence` | TField |  | Sequence No Multifonds DB Column is XNREGLE. |
| 16 | `FS.GA.NAV.CONTROL.PARAMETER.EXCLUSION.OF.TRANSACTIONS` | `FsGaNavControlParameter_ExclusionOfTransactions` | TField |  | Exclusion of new transactions Multifonds DB Column is FLG_EXCLUDE. |
| 17 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED10` | `FsGaNavControlParameter_Reserved10` | TField |  |  |
| 18 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED9` | `FsGaNavControlParameter_Reserved9` | TField |  |  |
| 19 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED8` | `FsGaNavControlParameter_Reserved8` | TField |  |  |
| 20 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED7` | `FsGaNavControlParameter_Reserved7` | TField |  |  |
| 21 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED6` | `FsGaNavControlParameter_Reserved6` | TField |  |  |
| 22 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED5` | `FsGaNavControlParameter_Reserved5` | TField |  |  |
| 23 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED4` | `FsGaNavControlParameter_Reserved4` | TField |  |  |
| 24 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED3` | `FsGaNavControlParameter_Reserved3` | TField |  |  |
| 25 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED2` | `FsGaNavControlParameter_Reserved2` | TField |  |  |
| 26 | `FS.GA.NAV.CONTROL.PARAMETER.RESERVED1` | `FsGaNavControlParameter_Reserved1` | TField |  |  |
| 27 | `FS.GA.NAV.CONTROL.PARAMETER.LOCAL.REF` | `FsGaNavControlParameter_LocalRef` |  |  |  |
| 28 | `FS.GA.NAV.CONTROL.PARAMETER.OVERRIDE` | `FsGaNavControlParameter_Override` |  |  |  |
| 29 | `FS.GA.NAV.CONTROL.PARAMETER.RECORD.STATUS` | `FsGaNavControlParameter_RecordStatus` | String |  |  |
| 30 | `FS.GA.NAV.CONTROL.PARAMETER.CURR.NO` | `FsGaNavControlParameter_CurrNo` | String |  |  |
| 31 | `FS.GA.NAV.CONTROL.PARAMETER.INPUTTER` | `FsGaNavControlParameter_Inputter` |  |  |  |
| 32 | `FS.GA.NAV.CONTROL.PARAMETER.DATE.TIME` | `FsGaNavControlParameter_DateTime` |  |  |  |
| 33 | `FS.GA.NAV.CONTROL.PARAMETER.AUTHORISER` | `FsGaNavControlParameter_Authoriser` | String |  |  |
| 34 | `FS.GA.NAV.CONTROL.PARAMETER.CO.CODE` | `FsGaNavControlParameter_CoCode` | String |  |  |
| 35 | `FS.GA.NAV.CONTROL.PARAMETER.DEPT.CODE` | `FsGaNavControlParameter_DeptCode` | String |  |  |
| 36 | `FS.GA.NAV.CONTROL.PARAMETER.AUDITOR.CODE` | `FsGaNavControlParameter_AuditorCode` | String |  |  |
| 37 | `FS.GA.NAV.CONTROL.PARAMETER.AUDIT.DATE.TIME` | `FsGaNavControlParameter_AuditDateTime` | String |  |  |
