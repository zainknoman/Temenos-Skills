# FS.GI.APP.COMMISSION.STRUCTURE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.COMMISSION.STRUCTURE` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.COMMISSION.STRUCTURE.PARENT.REF.ID` | `FsGiAppCommissionStructure_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.COMMISSION.STRUCTURE.ORA.ROWID` | `FsGiAppCommissionStructure_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.COMMISSION.STRUCTURE.COMM.STRUCTURE.ID` | `FsGiAppCommissionStructure_CommStructureId` | TField |  | Commission structure identification code. Multifonds DB Column is STRUCTURE_ID. |
| 4 | `FS.GI.APP.COMMISSION.STRUCTURE.COMM.STRUCTURE.NAME` | `FsGiAppCommissionStructure_CommStructureName` | TField |  | Commission structure description. Multifonds DB Column is STRUCTURE_NAME. |
| 5 | `FS.GI.APP.COMMISSION.STRUCTURE.COMM.STRUCTURE.TYPE` | `FsGiAppCommissionStructure_CommStructureType` | TField |  | Commission or trailer fees structure type. Multifonds DB Column is STRUCTURE_TYPE. |
| 6 | `FS.GI.APP.COMMISSION.STRUCTURE.PENALTY.TYPE` | `FsGiAppCommissionStructure_PenaltyType` | TField |  | Penalty type for debit operations. Multifonds DB Column is TYPE_PERIOD. |
| 7 | `FS.GI.APP.COMMISSION.STRUCTURE.COMMISSION.TYPE` | `FsGiAppCommissionStructure_CommissionType` | TField |  | Commission type for credit operations. Multifonds DB Column is TYPE_COMM. |
| 8 | `FS.GI.APP.COMMISSION.STRUCTURE.SETTLEMENT.MONEY.CODE` | `FsGiAppCommissionStructure_SettlementMoneyCode` | TField |  | Field used to manage due amount investment. Multifonds DB Column is CSETTLE_MONEY. |
| 9 | `FS.GI.APP.COMMISSION.STRUCTURE.COMMISSION.CODE` | `FsGiAppCommissionStructure_CommissionCode` | TField |  | Commission calculation depends on commission code parameterized at TA fund and structure level. Multifonds DB Column is CODE_COMMISSION. |
| 10 | `FS.GI.APP.COMMISSION.STRUCTURE.COMM.CODE.AMOUNT.ORDER` | `FsGiAppCommissionStructure_CommCodeAmountOrder` | TField |  | Base amount used for the commission calculations for the orders in amount. If this field is blank, system considers code parameterize in the field a Commission codea . Multifonds DB Column is CODE_COMMISSION_AMOUNT. |
| 11 | `FS.GI.APP.COMMISSION.STRUCTURE.PERCENTAGE` | `FsGiAppCommissionStructure_Percentage` | TField |  | Commission percentage. Multifonds DB Column is TUC_PCT. |
| 12 | `FS.GI.APP.COMMISSION.STRUCTURE.CREATION.PRICE.TERMS` | `FsGiAppCommissionStructure_CreationPriceTerms` | TField |  | Flag to indicate if the creation price to be applied instead of the Share price (subscription/ redemption). This is available only when the commission or penalty type = 0010 a Terms of business. Multifonds DB Column is FLG_PRICE_TERMS. |
| 13 | `FS.GI.APP.COMMISSION.STRUCTURE.USE.TOTAL.MAX.COMM` | `FsGiAppCommissionStructure_UseTotalMaxComm` | TField |  | Flag to allow manager charges calculations. This checkbox is only available in case commission type a 0006 a Distribution Percentagea is selected. Multifonds DB Column is MANAGER_CHGS. |
| 14 | `FS.GI.APP.COMMISSION.STRUCTURE.AGENT.COMM.PCT` | `FsGiAppCommissionStructure_AgentCommPct` | TField |  | Agent commission defined as flat percentage. Only used when the commission or penalty type = 0010 a Terms of business is chosen. Multifonds DB Column is OUTLET_TUC_PCT. |
| 15 | `FS.GI.APP.COMMISSION.STRUCTURE.AGENT.COMM.SCALE.CODE` | `FsGiAppCommissionStructure_AgentCommScaleCode` | TField |  | Agent commission defined as scale percentage where the scale type can only be &apos;4 - Degressive&apos; or &apos;5 - Cumulative&apos;. Only used when the commission or penalty type = 0010 a Terms of business is chosen. Multifonds DB Column is CSCALE_OUTLET_COMM. |
| 16 | `FS.GI.APP.COMMISSION.STRUCTURE.COMMISSION.DISCOUNT` | `FsGiAppCommissionStructure_CommissionDiscount` | TField | No | Allows defining the default discount % at order level. Optional, only used if the commission or penalty type is set to a 0009 a Dual pricing methoda . Multifonds DB Column is NDISCOUNT. |
| 17 | `FS.GI.APP.COMMISSION.STRUCTURE.AGENT.COMM.DISC.SCALE.CODE` | `FsGiAppCommissionStructure_AgentCommDiscScaleCode` | TField |  | Share price discount defined as scale percentage where the scale type can only be &apos;4 - Degressive&apos; or &apos;5 - Cumulative&apos;. Only used when the commission or penalty type = 0010 a Terms of business is chosen. Multifonds DB Column is CSCALE_NDISCOUNT. |
| 18 | `FS.GI.APP.COMMISSION.STRUCTURE.AMOUNT` | `FsGiAppCommissionStructure_Amount` | TField |  | Fixed amount of the commission. Multifonds DB Column is TUC_MNT. |
| 19 | `FS.GI.APP.COMMISSION.STRUCTURE.COMM.CURRENCY` | `FsGiAppCommissionStructure_CommCurrency` | TField |  | Currency in which the commission is expressed if the selected commission type or penalty type is amount. Multifonds DB Column is CMON. |
| 20 | `FS.GI.APP.COMMISSION.STRUCTURE.COMMISSION.WAIVER` | `FsGiAppCommissionStructure_CommissionWaiver` | TField | No | Commission waiver percentage. Optional, only used if the commission or penalty type is set to a 0009 a Dual pricing methoda . Allows defining the default waiver % at order level. Multifonds DB Column is NCOMM_WAIVER. |
| 21 | `FS.GI.APP.COMMISSION.STRUCTURE.WAIVER.COMM.SCALE.CODE` | `FsGiAppCommissionStructure_WaiverCommScaleCode` | TField |  | Commission waiver defined as scale percentage where the scale type can only be &apos;4 - Degressive&apos; or &apos;5 - Cumulative&apos;. Only used when the commission or penalty type = 0010 a Terms of business is chosen. Multifonds DB Column is CSCALE_NCOMM_WAIVER. |
| 22 | `FS.GI.APP.COMMISSION.STRUCTURE.SCALE` | `FsGiAppCommissionStructure_Scale` | TField | Yes | It specifies the Scale name. Mandatory if commission type is &quot;0003-Scale&quot;. Applicable on credit transaction only. Multifonds DB Column is SCALE_NAME. |
| 23 | `FS.GI.APP.COMMISSION.STRUCTURE.PERIOD` | `FsGiAppCommissionStructure_Period` | TField | Yes | It specifies the period name. Mandatory if Period Type is &quot;0003-Period&quot;. Multifonds DB Column is PERIOD. |
| 24 | `FS.GI.APP.COMMISSION.STRUCTURE.FLAT.CHARGE` | `FsGiAppCommissionStructure_FlatCharge` | TField |  | Defines the fixed amount to be charged for the particular transaction kind, in addition to the commission. If no other currency is specified for the flat charge the fund reference currency applies. Multifonds DB Column is FLAT_CHARGE. |
| 25 | `FS.GI.APP.COMMISSION.STRUCTURE.MGMT.COMMISSION` | `FsGiAppCommissionStructure_MgmtCommission` | TField |  | Management company commission amount (amount of commission to be distributed to the fund Management company). It is available only when commission type a 0006 a Distribution percentagea is chosen. Multifonds DB Column is MGMT_COMM. |
| 26 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED10` | `FsGiAppCommissionStructure_Reserved10` | TField |  |  |
| 27 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED9` | `FsGiAppCommissionStructure_Reserved9` | TField |  |  |
| 28 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED8` | `FsGiAppCommissionStructure_Reserved8` | TField |  |  |
| 29 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED7` | `FsGiAppCommissionStructure_Reserved7` | TField |  |  |
| 30 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED6` | `FsGiAppCommissionStructure_Reserved6` | TField |  |  |
| 31 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED5` | `FsGiAppCommissionStructure_Reserved5` | TField |  |  |
| 32 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED4` | `FsGiAppCommissionStructure_Reserved4` | TField |  |  |
| 33 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED3` | `FsGiAppCommissionStructure_Reserved3` | TField |  |  |
| 34 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED2` | `FsGiAppCommissionStructure_Reserved2` | TField |  |  |
| 35 | `FS.GI.APP.COMMISSION.STRUCTURE.RESERVED1` | `FsGiAppCommissionStructure_Reserved1` | TField |  |  |
| 36 | `FS.GI.APP.COMMISSION.STRUCTURE.LOCAL.REF` | `FsGiAppCommissionStructure_LocalRef` |  |  |  |
| 37 | `FS.GI.APP.COMMISSION.STRUCTURE.OVERRIDE` | `FsGiAppCommissionStructure_Override` |  |  |  |
| 38 | `FS.GI.APP.COMMISSION.STRUCTURE.RECORD.STATUS` | `FsGiAppCommissionStructure_RecordStatus` | String |  |  |
| 39 | `FS.GI.APP.COMMISSION.STRUCTURE.CURR.NO` | `FsGiAppCommissionStructure_CurrNo` | String |  |  |
| 40 | `FS.GI.APP.COMMISSION.STRUCTURE.INPUTTER` | `FsGiAppCommissionStructure_Inputter` |  |  |  |
| 41 | `FS.GI.APP.COMMISSION.STRUCTURE.DATE.TIME` | `FsGiAppCommissionStructure_DateTime` |  |  |  |
| 42 | `FS.GI.APP.COMMISSION.STRUCTURE.AUTHORISER` | `FsGiAppCommissionStructure_Authoriser` | String |  |  |
| 43 | `FS.GI.APP.COMMISSION.STRUCTURE.CO.CODE` | `FsGiAppCommissionStructure_CoCode` | String |  |  |
| 44 | `FS.GI.APP.COMMISSION.STRUCTURE.DEPT.CODE` | `FsGiAppCommissionStructure_DeptCode` | String |  |  |
| 45 | `FS.GI.APP.COMMISSION.STRUCTURE.AUDITOR.CODE` | `FsGiAppCommissionStructure_AuditorCode` | String |  |  |
| 46 | `FS.GI.APP.COMMISSION.STRUCTURE.AUDIT.DATE.TIME` | `FsGiAppCommissionStructure_AuditDateTime` | String |  |  |
