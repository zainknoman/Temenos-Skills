# FS.GI.APP.GROUP.COMMISSION — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.GROUP.COMMISSION` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.GROUP.COMMISSION.PARENT.REF.ID` | `FsGiAppGroupCommission_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.GROUP.COMMISSION.ORA.ROWID` | `FsGiAppGroupCommission_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.GROUP.COMMISSION.SHARE.CLASS.CODE` | `FsGiAppGroupCommission_ShareClassCode` | TField |  | Share class ID that needs to be linked to the fund commission group. Multifonds DB Column is TPART. |
| 4 | `FS.GI.APP.GROUP.COMMISSION.COMMISSION.GROUP` | `FsGiAppGroupCommission_CommissionGroup` | TField |  | Fund commission group created and linked to TA fund. Multifonds DB Column is CGROUP. |
| 5 | `FS.GI.APP.GROUP.COMMISSION.COMMISSION.FLAG` | `FsGiAppGroupCommission_CommissionFlag` | TField |  | Flag to enable commission. Multifonds DB Column is COMMISSION. |
| 6 | `FS.GI.APP.GROUP.COMMISSION.OPERATION.CODE` | `FsGiAppGroupCommission_OperationCode` | TField |  | Operation for which this group Commission Setup is to be used. Multifonds DB Column is COPERATION. |
| 7 | `FS.GI.APP.GROUP.COMMISSION.CONDITION.METHOD` | `FsGiAppGroupCommission_ConditionMethod` | TField |  | Condition method required for switch transactions to specify the links between the switched funds(0000 - NOCHECK, 0001 - Same fund and same unit a .). Auto populated for all other transactions. Multifonds DB Column is COND_METHOD. |
| 8 | `FS.GI.APP.GROUP.COMMISSION.REDEMPTION.METHOD` | `FsGiAppGroupCommission_RedemptionMethod` | TField |  | Commission method ID. Multifonds DB Column is METHOD. |
| 9 | `FS.GI.APP.GROUP.COMMISSION.PENALTY.TYPE` | `FsGiAppGroupCommission_PenaltyType` | TField |  | Period type or penalty type for debit operations. Multifonds DB Column is TYPE_PERIOD. |
| 10 | `FS.GI.APP.GROUP.COMMISSION.COMMISSION.TYPE` | `FsGiAppGroupCommission_CommissionType` | TField |  | Commission type for credit operations. Multifonds DB Column is TYPE_COMM. |
| 11 | `FS.GI.APP.GROUP.COMMISSION.CDSC.FLAG` | `FsGiAppGroupCommission_CdscFlag` | TField |  | Flag If ticked, it indicates that this fund share class has a CDSC calculation method. Multifonds DB Column is USE_CDSC. |
| 12 | `FS.GI.APP.GROUP.COMMISSION.CDSC.AGENT.ID` | `FsGiAppGroupCommission_CdscAgentId` | TField |  | Prefinancing agent ID for CDSC calculation. Multifonds DB Column is NOUTLET_CDSC. |
| 13 | `FS.GI.APP.GROUP.COMMISSION.USE.TOTAL.MAX.COMM` | `FsGiAppGroupCommission_UseTotalMaxComm` | TField |  | Flag allows manager charges calculations. This checkbox is only available in case commission type a 0006 a Distribution Percentagea is selected. Multifonds DB Column is MANAGER_CHGS. |
| 14 | `FS.GI.APP.GROUP.COMMISSION.COMM.ON.TOP.FLAG` | `FsGiAppGroupCommission_CommOnTopFlag` | TField |  | Comm Commission Exclude from Order Amount Flag, which when ticked enables the user to deal with net amount a only transactions in amount are impacted. Multifonds DB Column is FLG_TOP_COMM. |
| 15 | `FS.GI.APP.GROUP.COMMISSION.DISCOUNT.CALC` | `FsGiAppGroupCommission_DiscountCalc` | TField |  | Flag to enable or disable discount calculation when the &apos;Commission type&apos; is &apos;0007-Agent Structure&apos; or &apos;0006-Distribution percentage&apos;. Multifonds DB Column is FLG_DIS_CAL. |
| 16 | `FS.GI.APP.GROUP.COMMISSION.PERCENTAGE` | `FsGiAppGroupCommission_Percentage` | TField |  | Commission percentage. Multifonds DB Column is TUC_PCT. |
| 17 | `FS.GI.APP.GROUP.COMMISSION.MIN.PERCENTAGE` | `FsGiAppGroupCommission_MinPercentage` | TField | Yes | Minimum commission expressed in percentage. This field is mandatory when the commission is 0006 a Distribution percentage or 0008 a TA percentage method. This field cannot be greater than Max % field. Multifonds DB Column is PCT_MIN. |
| 18 | `FS.GI.APP.GROUP.COMMISSION.DEFLT.INI.CHARGE.PCT` | `FsGiAppGroupCommission_DefltIniChargePct` | TField |  | Maximum commission % allowed for the operation code by the fund. Multifonds DB Column is PCT_DEF_INT_CRG. |
| 19 | `FS.GI.APP.GROUP.COMMISSION.MAX.PERCENTAGE` | `FsGiAppGroupCommission_MaxPercentage` | TField | Yes | Maximum commission expressed in percentage. This field is mandatory when the commission is 0006 a Distribution percentage or 0008 a TA percentage method. This field cannot be smaller than Min% field. Multifonds DB Column is PCT_MAX. |
| 20 | `FS.GI.APP.GROUP.COMMISSION.TA.COMM.PCT` | `FsGiAppGroupCommission_TaCommPct` | TField | Yes | TA commission expressed in percent.It is mandatory when the commission type is &quot;0008 -TA percentage method&quot;. Min% + TA Commission % cannot be greater than Max% field. Multifonds DB Column is TA_PCT. |
| 21 | `FS.GI.APP.GROUP.COMMISSION.SCALE.CODE` | `FsGiAppGroupCommission_ScaleCode` | TField | Yes | It specifies the Scale name.Mandatory if Commission Type = &quot;0003-Scale&quot;. Applicable on credit transaction only. Multifonds DB Column is SCALE_NAME. |
| 22 | `FS.GI.APP.GROUP.COMMISSION.AMOUNT` | `FsGiAppGroupCommission_Amount` | TField |  | Fixed amount of the commission. Multifonds DB Column is TUC_MNT. |
| 23 | `FS.GI.APP.GROUP.COMMISSION.COMM.CURRENCY` | `FsGiAppGroupCommission_CommCurrency` | TField |  | Currency in which the commission is expressed if the selected commission type or penalty type is amount. Multifonds DB Column is CMON. |
| 24 | `FS.GI.APP.GROUP.COMMISSION.FLAT.CHARGE` | `FsGiAppGroupCommission_FlatCharge` | TField |  | Defines the fixed amount to be charged for the particular transaction kind, in addition to the commission. If no other currency is specified for the flat charge the fund reference currency applies. Multifonds DB Column is FLAT_CHARGE. |
| 25 | `FS.GI.APP.GROUP.COMMISSION.PERIOD` | `FsGiAppGroupCommission_Period` | TField | Yes | It specifies the period name. Mandatory if Period Type is &quot;0003-Period&quot;. Multifonds DB Column is PERIOD. |
| 26 | `FS.GI.APP.GROUP.COMMISSION.RESERVED10` | `FsGiAppGroupCommission_Reserved10` | TField |  |  |
| 27 | `FS.GI.APP.GROUP.COMMISSION.RESERVED9` | `FsGiAppGroupCommission_Reserved9` | TField |  |  |
| 28 | `FS.GI.APP.GROUP.COMMISSION.RESERVED8` | `FsGiAppGroupCommission_Reserved8` | TField |  |  |
| 29 | `FS.GI.APP.GROUP.COMMISSION.RESERVED7` | `FsGiAppGroupCommission_Reserved7` | TField |  |  |
| 30 | `FS.GI.APP.GROUP.COMMISSION.RESERVED6` | `FsGiAppGroupCommission_Reserved6` | TField |  |  |
| 31 | `FS.GI.APP.GROUP.COMMISSION.RESERVED5` | `FsGiAppGroupCommission_Reserved5` | TField |  |  |
| 32 | `FS.GI.APP.GROUP.COMMISSION.RESERVED4` | `FsGiAppGroupCommission_Reserved4` | TField |  |  |
| 33 | `FS.GI.APP.GROUP.COMMISSION.RESERVED3` | `FsGiAppGroupCommission_Reserved3` | TField |  |  |
| 34 | `FS.GI.APP.GROUP.COMMISSION.RESERVED2` | `FsGiAppGroupCommission_Reserved2` | TField |  |  |
| 35 | `FS.GI.APP.GROUP.COMMISSION.RESERVED1` | `FsGiAppGroupCommission_Reserved1` | TField |  |  |
| 36 | `FS.GI.APP.GROUP.COMMISSION.LOCAL.REF` | `FsGiAppGroupCommission_LocalRef` |  |  |  |
| 37 | `FS.GI.APP.GROUP.COMMISSION.OVERRIDE` | `FsGiAppGroupCommission_Override` |  |  |  |
| 38 | `FS.GI.APP.GROUP.COMMISSION.RECORD.STATUS` | `FsGiAppGroupCommission_RecordStatus` | String |  |  |
| 39 | `FS.GI.APP.GROUP.COMMISSION.CURR.NO` | `FsGiAppGroupCommission_CurrNo` | String |  |  |
| 40 | `FS.GI.APP.GROUP.COMMISSION.INPUTTER` | `FsGiAppGroupCommission_Inputter` |  |  |  |
| 41 | `FS.GI.APP.GROUP.COMMISSION.DATE.TIME` | `FsGiAppGroupCommission_DateTime` |  |  |  |
| 42 | `FS.GI.APP.GROUP.COMMISSION.AUTHORISER` | `FsGiAppGroupCommission_Authoriser` | String |  |  |
| 43 | `FS.GI.APP.GROUP.COMMISSION.CO.CODE` | `FsGiAppGroupCommission_CoCode` | String |  |  |
| 44 | `FS.GI.APP.GROUP.COMMISSION.DEPT.CODE` | `FsGiAppGroupCommission_DeptCode` | String |  |  |
| 45 | `FS.GI.APP.GROUP.COMMISSION.AUDITOR.CODE` | `FsGiAppGroupCommission_AuditorCode` | String |  |  |
| 46 | `FS.GI.APP.GROUP.COMMISSION.AUDIT.DATE.TIME` | `FsGiAppGroupCommission_AuditDateTime` | String |  |  |
