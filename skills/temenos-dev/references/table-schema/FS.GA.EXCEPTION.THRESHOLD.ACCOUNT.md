# FS.GA.EXCEPTION.THRESHOLD.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.FS.GA.EXCEPTION.THRESHOLD.ACCOUNT` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.PARENT.REF.ID` | `FsGaExceptionThresholdAccount_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.ORA.ROWID` | `FsGaExceptionThresholdAccount_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.CONTROL.NUMBER` | `FsGaExceptionThresholdAccount_ControlNumber` | TField |  | Control Number linked to Process Multifonds DB Column is TYP_CONTROLE. |
| 4 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.VAR` | `FsGaExceptionThresholdAccount_Var` | TField |  | Ticked - System will check the variation of the account parameterized under Group of Account. Unticked - System will check the Balance of account parameterized under Group of Account. Multifonds DB Column is FLG_VAR. |
| 5 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.GROUP.OF.ACCOUNT1` | `FsGaExceptionThresholdAccount_GroupOfAccount1` | TField |  | Groups which are created in the Group of account button is parameterized in this field. Every single account included in the group of account are subject to control. Multifonds DB Column is GROUP_NRUBR_1. |
| 6 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.SUM1` | `FsGaExceptionThresholdAccount_Sum1` | TField |  | Sum Ticked &amp; Variation Unticked: Control is done on the sum of the balance of all the account included in the group of account in part 1st (For more details refer UG) Multifonds DB Column is FLG_SUM_1. |
| 7 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.LOGICAL.CODE` | `FsGaExceptionThresholdAccount_LogicalCode` | TField |  | Refers to the logical code used to define the control. E.g., &lt;(Less Thanks), &gt;=(Greater than or Equal ) etc. Multifonds DB Column is COD_OPERATION. |
| 8 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.TYPE.OF.EXCEPTION.MONITOR` | `FsGaExceptionThresholdAccount_TypeOfExceptionMonitor` | TField |  | Refers to different Type of Exceptions. E.g., Amount, Percent, or Percentage of the Portfolio etc. Multifonds DB Column is TYP_CONNAV. |
| 9 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.VALUE.OF.EXCEPTION.MONITOR` | `FsGaExceptionThresholdAccount_ValueOfExceptionMonitor` | TField |  | User has to define the threshold amount or absolute figure for control in this field. This is in relation to the Type defined. Multifonds DB Column is MNT_PCT. |
| 10 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.GROUP.OF.ACCOUNT3` | `FsGaExceptionThresholdAccount_GroupOfAccount3` | TField |  | This field will be populated with a group of acct to be checked. If the group of acc is the same as in part 1 and the Var. ticked then it means the second part will be the variation of the prev day. Multifonds DB Column is GROUP_NRUBR_3. |
| 11 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.SUM3` | `FsGaExceptionThresholdAccount_Sum3` | TField |  | This is applicable of the Group of account part 3rd. Rest of the functionality is same as explained for Sum (Part 1st). Multifonds DB Column is FLG_SUM_3. |
| 12 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.SPECIFIC` | `FsGaExceptionThresholdAccount_Specific` | TField |  | If user ticks this field, a specific control will be applicable. The control is related to annualizing the fees. Multifonds DB Column is FLG_SPEC. |
| 13 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.SEQUENCE.NO` | `FsGaExceptionThresholdAccount_SequenceNo` | TField |  | Sequence Number of the control Multifonds DB Column is NREGLE. |
| 14 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.NUMBER.OF.NAV` | `FsGaExceptionThresholdAccount_NumberOfNav` | TField |  | Number of day between last NAV day and current NAV day) Multifonds DB Column is NO_OF_NAVS. |
| 15 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.O.NAV` | `FsGaExceptionThresholdAccount_ONav` | TField |  | Flag O NAV Multifonds DB Column is FLG_ONAV. |
| 16 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED10` | `FsGaExceptionThresholdAccount_Reserved10` | TField |  |  |
| 17 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED9` | `FsGaExceptionThresholdAccount_Reserved9` | TField |  |  |
| 18 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED8` | `FsGaExceptionThresholdAccount_Reserved8` | TField |  |  |
| 19 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED7` | `FsGaExceptionThresholdAccount_Reserved7` | TField |  |  |
| 20 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED6` | `FsGaExceptionThresholdAccount_Reserved6` | TField |  |  |
| 21 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED5` | `FsGaExceptionThresholdAccount_Reserved5` | TField |  |  |
| 22 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED4` | `FsGaExceptionThresholdAccount_Reserved4` | TField |  |  |
| 23 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED3` | `FsGaExceptionThresholdAccount_Reserved3` | TField |  |  |
| 24 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED2` | `FsGaExceptionThresholdAccount_Reserved2` | TField |  |  |
| 25 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RESERVED1` | `FsGaExceptionThresholdAccount_Reserved1` | TField |  |  |
| 26 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.LOCAL.REF` | `FsGaExceptionThresholdAccount_LocalRef` |  |  |  |
| 27 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.OVERRIDE` | `FsGaExceptionThresholdAccount_Override` |  |  |  |
| 28 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.RECORD.STATUS` | `FsGaExceptionThresholdAccount_RecordStatus` | String |  |  |
| 29 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.CURR.NO` | `FsGaExceptionThresholdAccount_CurrNo` | String |  |  |
| 30 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.INPUTTER` | `FsGaExceptionThresholdAccount_Inputter` |  |  |  |
| 31 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.DATE.TIME` | `FsGaExceptionThresholdAccount_DateTime` |  |  |  |
| 32 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.AUTHORISER` | `FsGaExceptionThresholdAccount_Authoriser` | String |  |  |
| 33 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.CO.CODE` | `FsGaExceptionThresholdAccount_CoCode` | String |  |  |
| 34 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.DEPT.CODE` | `FsGaExceptionThresholdAccount_DeptCode` | String |  |  |
| 35 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.AUDITOR.CODE` | `FsGaExceptionThresholdAccount_AuditorCode` | String |  |  |
| 36 | `FS.GA.EXCEPTION.THRESHOLD.ACCOUNT.AUDIT.DATE.TIME` | `FsGaExceptionThresholdAccount_AuditDateTime` | String |  |  |
