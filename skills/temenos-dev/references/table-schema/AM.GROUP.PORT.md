# AM.GROUP.PORT — Table Schema

> Source: `INSERTS/I_F.AM.GROUP.PORT` in `AM_Group.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.AGP.ACCOUNT.OFFICER` | `AmGroupPort_AccountOfficer` | TField | No | Controls the portfolios that are grouped together in the AM.GROUP.PORT record. Validation Rules: Optional. Must exist on the DEPT.ACCT.OFFICER file. When this field contains a value, the portfolios that are added to this group must belong to this ACCOUNT.OFFICER. |
| 2 | `AM.AGP.MNEMONIC` | `AmGroupPort_Mnemonic` | TField | No | Specifies an alternative easy means of referencing the Group. Like the ID, the Mnemonic must be unique. Care should be taken when assigning Mnemonics to Groups and some rules should ideally be defined across the bank to allow easy identification of the Groups by their Mnemonics. Note : For each Group, the System will automatically update the internal file "MNEMONIC.AM.GROUP.PORT" which allows the User to display the Groups in Mnemonic sequence instead of Group number. Validation Rules: Optional input. 3-20 type MNE (Uppercase alpha or numeric, first character alpha, or ".") characters. |
| 3 | `AM.AGP.SEC.ACC.NO` | `AmGroupPort_SecAccNo` |  |  |  |
| 4 | `AM.AGP.DYN.FLD.NAME` | `AmGroupPort_DynFldName` |  |  |  |
| 5 | `AM.AGP.DYN.OPERAND` | `AmGroupPort_DynOperand` |  |  |  |
| 6 | `AM.AGP.DYN.VALUE` | `AmGroupPort_DynValue` |  |  |  |
| 7 | `AM.AGP.SEL.SUB.FUNC` | `AmGroupPort_SelSubFunc` |  |  |  |
| 8 | `AM.AGP.SEL.MAIN.FUNC` | `AmGroupPort_SelMainFunc` |  |  |  |
| 9 | `AM.AGP.VAL.CURRENCY` | `AmGroupPort_ValCurrency` | TField | Yes | Identifies the currency in which the Portfolio Group consolidation should be done. When consolidating the Group, the amounts will be converted to this currency if it is present. Validation Rules: Mandatory input 3 characters currency code Must be present on the CURRENCY file. |
| 10 | `AM.AGP.DET.OR.CON.REP` | `AmGroupPort_DetOrConRep` | TField | Yes | Specifies the Type of report required for this Group. The report can be either Detailed report or Consolidated Report. Validation Rules: Mandatory Input. Only 4 values are accepted - 'Detail', 'Consolidated', 'None' and 'Both'. If left Blank, will be defaulted 'None' |
| 11 | `AM.AGP.P.N.CONSOLIDATE` | `AmGroupPort_PNConsolidate` |  |  |  |
| 12 | `AM.AGP.DEACTIVATED` | `AmGroupPort_Deactivated` | TField | No | Indicates whether the Group is Deactivated or Not. Only 2 values are allowed. 'Yes' or 'No'. Once if the Value is set to 'Yes', then the Group cannot be Activated again. Validation Rules: Optional Input. Only 2 values are allowed. 'Yes', 'No' and Blank. Default Value - 'No' |
| 13 | `AM.AGP.DEACTIVATED.DATE` | `AmGroupPort_DeactivatedDate` | TField |  | Specifies the date on which the Group is deactivated. Validation Rules: Noinput Field. |
| 14 | `AM.AGP.COMMENTS` | `AmGroupPort_Comments` |  |  |  |
| 15 | `AM.AGP.BACK.VAL.PERF.REQ` | `AmGroupPort_BackValPerfReq` | TField |  | Should the performance for this group be recalculated during a back valuation? Values for this field are YES and NO, defaults to NO. No change field. |
| 16 | `AM.AGP.BACK.VAL.FROM.DATE` | `AmGroupPort_BackValFromDate` | TField |  | This no input field only populated if BACK.VAL.PERF.REQ is YES. The date will default to the first day of the month in which the AM.GROUP.PORT record is input. |
| 17 | `AM.AGP.GROUP.TYPE` | `AmGroupPort_GroupType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 18 | `AM.AGP.INVESTMENT.PROGRAM` | `AmGroupPort_InvestmentProgram` | TField | Yes | The axis of the support model must match with the axis of the group level matrix. i.e. AXIS.X of the support model must match with AXIS.X of the group model, same rule applies for AXIS.Y also; else error message is raised. Group matrix can have two axis and the supporting matrix can have both or any one of the group matrix axis, but it can�t be the other way. Mandatory field because rebalancing must happen at group level and maximising the tax benefits must happen at sub portfolio level. If a link matrix is attached to any one of the model i.e. either supporting model or group level model, then a link matrix of the same type (axis should be in line with the attached linked matrix) has to be attached to the same axis member of the other model. Validation Rules: Alpha numeric |
| 19 | `AM.AGP.BENCHMARK` | `AmGroupPort_Benchmark` | TField |  | Accepts a valid record from AM.BENCHMARK application. |
| 20 | `AM.AGP.RESERVED7` | `AmGroupPort_Reserved7` | TField |  |  |
| 21 | `AM.AGP.RESERVED6` | `AmGroupPort_Reserved6` | TField |  |  |
| 22 | `AM.AGP.RESERVED5` | `AmGroupPort_Reserved5` | TField |  |  |
| 23 | `AM.AGP.RESERVED4` | `AmGroupPort_Reserved4` | TField |  |  |
| 24 | `AM.AGP.RESERVED3` | `AmGroupPort_Reserved3` | TField |  |  |
| 25 | `AM.AGP.LOCAL.REF` | `AmGroupPort_LocalRef` |  |  |  |
| 26 | `AM.AGP.OVERRIDE` | `AmGroupPort_Override` |  |  |  |
| 27 | `AM.AGP.RECORD.STATUS` | `AmGroupPort_RecordStatus` | String |  |  |
| 28 | `AM.AGP.CURR.NO` | `AmGroupPort_CurrNo` | String |  |  |
| 29 | `AM.AGP.INPUTTER` | `AmGroupPort_Inputter` |  |  |  |
| 30 | `AM.AGP.DATE.TIME` | `AmGroupPort_DateTime` |  |  |  |
| 31 | `AM.AGP.AUTHORISER` | `AmGroupPort_Authoriser` | String |  |  |
| 32 | `AM.AGP.CO.CODE` | `AmGroupPort_CoCode` | String |  |  |
| 33 | `AM.AGP.DEPT.CODE` | `AmGroupPort_DeptCode` | String |  |  |
| 34 | `AM.AGP.AUDITOR.CODE` | `AmGroupPort_AuditorCode` | String |  |  |
| 35 | `AM.AGP.AUDIT.DATE.TIME` | `AmGroupPort_AuditDateTime` | String |  |  |
