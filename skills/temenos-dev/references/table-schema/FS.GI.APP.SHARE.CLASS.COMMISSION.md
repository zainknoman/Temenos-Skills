# FS.GI.APP.SHARE.CLASS.COMMISSION — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.SHARE.CLASS.COMMISSION` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.SHARE.CLASS.COMMISSION.PARENT.REF.ID` | `FsGiAppShareClassCommission_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.SHARE.CLASS.COMMISSION.ORA.ROWID` | `FsGiAppShareClassCommission_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.SHARE.CLASS.COMMISSION.SHARE.CLASS.CODE` | `FsGiAppShareClassCommission_ShareClassCode` | TField |  | Share Class ID for commission setup is to be used. Multifonds DB Column is TPART. |
| 4 | `FS.GI.APP.SHARE.CLASS.COMMISSION.OPERATION.CODE` | `FsGiAppShareClassCommission_OperationCode` | TField |  | Operation code for which this Commission setup is to be used. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.APP.SHARE.CLASS.COMMISSION.COMMISSION.FLAG` | `FsGiAppShareClassCommission_CommissionFlag` | TField |  | Flag to specify whether commission is applicable for the share class and operation code. Multifonds DB Column is COMMISSION. |
| 6 | `FS.GI.APP.SHARE.CLASS.COMMISSION.REDEMPTION.METHOD` | `FsGiAppShareClassCommission_RedemptionMethod` | TField |  | Redemption method code. Multifonds DB Column is METHOD. |
| 7 | `FS.GI.APP.SHARE.CLASS.COMMISSION.CONDITION.METHOD` | `FsGiAppShareClassCommission_ConditionMethod` | TField |  | Condition method required for switch transactions to specify the links between the switched funds. Auto populated for all other transactions. Multifonds DB Column is COND_METHOD. |
| 8 | `FS.GI.APP.SHARE.CLASS.COMMISSION.HISTORICAL.FLAG` | `FsGiAppShareClassCommission_HistoricalFlag` | TField |  | Commission Historical Flag. Multifonds DB Column is FLG_HIST. |
| 9 | `FS.GI.APP.SHARE.CLASS.COMMISSION.PENALTY.TYPE` | `FsGiAppShareClassCommission_PenaltyType` | TField |  | Penalty type for debit operations. Multifonds DB Column is TYPE_PERIOD. |
| 10 | `FS.GI.APP.SHARE.CLASS.COMMISSION.PERIOD` | `FsGiAppShareClassCommission_Period` | TField | Yes | It specifies the period name. Mandatory if Period Type is &quot;0003-Period&quot;. Multifonds DB Column is PERIOD. |
| 11 | `FS.GI.APP.SHARE.CLASS.COMMISSION.CDSC.FLAG` | `FsGiAppShareClassCommission_CdscFlag` | TField |  | CDSC Flag. Multifonds DB Column is USE_CDSC. |
| 12 | `FS.GI.APP.SHARE.CLASS.COMMISSION.CDSC.AGENT.ID` | `FsGiAppShareClassCommission_CdscAgentId` | TField |  | Prefinancing ID for CDSC. Multifonds DB Column is NOUTLET_CDSC. |
| 13 | `FS.GI.APP.SHARE.CLASS.COMMISSION.USE.TOTAL.MAX.COMM` | `FsGiAppShareClassCommission_UseTotalMaxComm` | TField |  | Flag allows manager charges calculations. This checkbox is only available in case commission type a 0006 a Distribution Percentagea is selected. Multifonds DB Column is MANAGER_CHGS. |
| 14 | `FS.GI.APP.SHARE.CLASS.COMMISSION.COMM.ON.TOP.FLAG` | `FsGiAppShareClassCommission_CommOnTopFlag` | TField |  | Commission exclude from order amount flag. Multifonds DB Column is FLG_TOP_COMM. |
| 15 | `FS.GI.APP.SHARE.CLASS.COMMISSION.DISCOUNT.CALC.FLAG` | `FsGiAppShareClassCommission_DiscountCalcFlag` | TField |  | Flag to enable discount calculation in case of credit operation codes. Multifonds DB Column is FLG_DIS_CAL. |
| 16 | `FS.GI.APP.SHARE.CLASS.COMMISSION.COMM.TYPE` | `FsGiAppShareClassCommission_CommType` | TField |  | Commission type for credit operations(0001 - Percentage, 0002 - Amount, a .). Multifonds DB Column is TYPE_COMM. |
| 17 | `FS.GI.APP.SHARE.CLASS.COMMISSION.SCALE` | `FsGiAppShareClassCommission_Scale` | TField | Yes | It specifies the scale name. Mandatory if commission type is &quot;0003-Scale&quot;. Applicable on credit transaction only. Multifonds DB Column is SCALE_NAME. |
| 18 | `FS.GI.APP.SHARE.CLASS.COMMISSION.AMOUNT` | `FsGiAppShareClassCommission_Amount` | TField |  | Fixed amount of the commission. Multifonds DB Column is TUC_MNT. |
| 19 | `FS.GI.APP.SHARE.CLASS.COMMISSION.FLAT.CHARGE` | `FsGiAppShareClassCommission_FlatCharge` | TField |  | Flat charge amount applied in addition to any commission. Multifonds DB Column is FLAT_CHARGE. |
| 20 | `FS.GI.APP.SHARE.CLASS.COMMISSION.PERCENTAGE` | `FsGiAppShareClassCommission_Percentage` | TField |  | Commission percentage. Multifonds DB Column is TUC_PCT. |
| 21 | `FS.GI.APP.SHARE.CLASS.COMMISSION.MIN.PERCENTAGE` | `FsGiAppShareClassCommission_MinPercentage` | TField |  | Minimum commission percentage. Multifonds DB Column is PCT_MIN. |
| 22 | `FS.GI.APP.SHARE.CLASS.COMMISSION.COMMISSION.CURRENCY` | `FsGiAppShareClassCommission_CommissionCurrency` | TField |  | Currency of the commission amount. Multifonds DB Column is CMON. |
| 23 | `FS.GI.APP.SHARE.CLASS.COMMISSION.MAX.PERCENTAGE` | `FsGiAppShareClassCommission_MaxPercentage` | TField |  | Maximum commission percentage. Multifonds DB Column is PCT_MAX. |
| 24 | `FS.GI.APP.SHARE.CLASS.COMMISSION.TA.COMM.PCT` | `FsGiAppShareClassCommission_TaCommPct` | TField |  | Exception commission percentage for commission type TA commission which will be considered to calculate the commission for this order. Multifonds DB Column is TA_PCT. |
| 25 | `FS.GI.APP.SHARE.CLASS.COMMISSION.DEFLT.INI.CHARGE.PCT` | `FsGiAppShareClassCommission_DefltIniChargePct` | TField |  | Maximum commission percentage allowed for the operation code by the fund. Multifonds DB Column is PCT_DEF_INT_CRG. |
| 26 | `FS.GI.APP.SHARE.CLASS.COMMISSION.LEGAL.ENTITY.ID` | `FsGiAppShareClassCommission_LegalEntityId` | TField |  | Legal Entity ID linked to the Fund and share class. Multifonds DB Column is NTFC. |
| 27 | `FS.GI.APP.SHARE.CLASS.COMMISSION.TA.FUND.ID` | `FsGiAppShareClassCommission_TaFundId` | TField |  | Fund ID linked to the share class. Multifonds DB Column is NPTF. |
| 28 | `FS.GI.APP.SHARE.CLASS.COMMISSION.FUND.ID` | `FsGiAppShareClassCommission_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 29 | `FS.GI.APP.SHARE.CLASS.COMMISSION.CLASS.CURRENCY` | `FsGiAppShareClassCommission_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 30 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED10` | `FsGiAppShareClassCommission_Reserved10` | TField |  |  |
| 31 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED9` | `FsGiAppShareClassCommission_Reserved9` | TField |  |  |
| 32 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED8` | `FsGiAppShareClassCommission_Reserved8` | TField |  |  |
| 33 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED7` | `FsGiAppShareClassCommission_Reserved7` | TField |  |  |
| 34 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED6` | `FsGiAppShareClassCommission_Reserved6` | TField |  |  |
| 35 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED5` | `FsGiAppShareClassCommission_Reserved5` | TField |  |  |
| 36 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED4` | `FsGiAppShareClassCommission_Reserved4` | TField |  |  |
| 37 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED3` | `FsGiAppShareClassCommission_Reserved3` | TField |  |  |
| 38 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED2` | `FsGiAppShareClassCommission_Reserved2` | TField |  |  |
| 39 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RESERVED1` | `FsGiAppShareClassCommission_Reserved1` | TField |  |  |
| 40 | `FS.GI.APP.SHARE.CLASS.COMMISSION.LOCAL.REF` | `FsGiAppShareClassCommission_LocalRef` |  |  |  |
| 41 | `FS.GI.APP.SHARE.CLASS.COMMISSION.OVERRIDE` | `FsGiAppShareClassCommission_Override` |  |  |  |
| 42 | `FS.GI.APP.SHARE.CLASS.COMMISSION.RECORD.STATUS` | `FsGiAppShareClassCommission_RecordStatus` | String |  |  |
| 43 | `FS.GI.APP.SHARE.CLASS.COMMISSION.CURR.NO` | `FsGiAppShareClassCommission_CurrNo` | String |  |  |
| 44 | `FS.GI.APP.SHARE.CLASS.COMMISSION.INPUTTER` | `FsGiAppShareClassCommission_Inputter` |  |  |  |
| 45 | `FS.GI.APP.SHARE.CLASS.COMMISSION.DATE.TIME` | `FsGiAppShareClassCommission_DateTime` |  |  |  |
| 46 | `FS.GI.APP.SHARE.CLASS.COMMISSION.AUTHORISER` | `FsGiAppShareClassCommission_Authoriser` | String |  |  |
| 47 | `FS.GI.APP.SHARE.CLASS.COMMISSION.CO.CODE` | `FsGiAppShareClassCommission_CoCode` | String |  |  |
| 48 | `FS.GI.APP.SHARE.CLASS.COMMISSION.DEPT.CODE` | `FsGiAppShareClassCommission_DeptCode` | String |  |  |
| 49 | `FS.GI.APP.SHARE.CLASS.COMMISSION.AUDITOR.CODE` | `FsGiAppShareClassCommission_AuditorCode` | String |  |  |
| 50 | `FS.GI.APP.SHARE.CLASS.COMMISSION.AUDIT.DATE.TIME` | `FsGiAppShareClassCommission_AuditDateTime` | String |  |  |
