# FS.GA.REBATE.FEE.AMOUNT.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.REBATE.FEE.AMOUNT.DEFINITION` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.FUND.ID` | `FsGaRebateFeeAmountDefinition_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.INTERNAL.SECURITY.ID` | `FsGaRebateFeeAmountDefinition_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 3 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.CORRESPONDENT` | `FsGaRebateFeeAmountDefinition_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.SERVICE.CODE` | `FsGaRebateFeeAmountDefinition_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 5 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.LOT.NUMBER` | `FsGaRebateFeeAmountDefinition_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 6 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.MANAGER.CODE` | `FsGaRebateFeeAmountDefinition_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 7 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.FROM.DT` | `FsGaRebateFeeAmountDefinition_FromDt` | TField |  | From Date Multifonds DB Column is DDEBUT. |
| 8 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.TO.DT` | `FsGaRebateFeeAmountDefinition_ToDt` | TField |  | To Date Multifonds DB Column is DFIN. |
| 9 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.AMOUNT.OR.PERCENT` | `FsGaRebateFeeAmountDefinition_AmountOrPercent` | TField |  | Enter the percentage or amount of the fee Multifonds DB Column is MNTPRT. |
| 10 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.REBATE.PERCENTAGE` | `FsGaRebateFeeAmountDefinition_RebatePercentage` | TField |  | Rebate Percentage Multifonds DB Column is MNTPRT_NOTAX. |
| 11 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.REBATE.TYPE` | `FsGaRebateFeeAmountDefinition_RebateType` | TField |  | Specify the rebate type 1 for Income and 2 for Capital. Multifonds DB Column is REBATE_TYPE. |
| 12 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.GROUP.MULTICLASS` | `FsGaRebateFeeAmountDefinition_GroupMulticlass` | TField |  | In case of a fund having multiple share classes and if the fee is linked to a particular share class, hence the multi-class group code must be entered in this field Multifonds DB Column is CODE_GRP_MULTICLASS. |
| 13 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.SCALE.CODE.FOR.CHARGES` | `FsGaRebateFeeAmountDefinition_ScaleCodeForCharges` | TField |  | If the fee type is equal to "5 - Scale", a scale code needs to be entered. These scale codes must have been created before via the button scale. Multifonds DB Column is CBAREME_VAL. |
| 14 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED10` | `FsGaRebateFeeAmountDefinition_Reserved10` | TField |  |  |
| 15 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED9` | `FsGaRebateFeeAmountDefinition_Reserved9` | TField |  |  |
| 16 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED8` | `FsGaRebateFeeAmountDefinition_Reserved8` | TField |  |  |
| 17 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED7` | `FsGaRebateFeeAmountDefinition_Reserved7` | TField |  |  |
| 18 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED6` | `FsGaRebateFeeAmountDefinition_Reserved6` | TField |  |  |
| 19 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED5` | `FsGaRebateFeeAmountDefinition_Reserved5` | TField |  |  |
| 20 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED4` | `FsGaRebateFeeAmountDefinition_Reserved4` | TField |  |  |
| 21 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED3` | `FsGaRebateFeeAmountDefinition_Reserved3` | TField |  |  |
| 22 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED2` | `FsGaRebateFeeAmountDefinition_Reserved2` | TField |  |  |
| 23 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RESERVED1` | `FsGaRebateFeeAmountDefinition_Reserved1` | TField |  |  |
| 24 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.RECORD.STATUS` | `FsGaRebateFeeAmountDefinition_RecordStatus` | String |  |  |
| 25 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.CURR.NO` | `FsGaRebateFeeAmountDefinition_CurrNo` | String |  |  |
| 26 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.INPUTTER` | `FsGaRebateFeeAmountDefinition_Inputter` |  |  |  |
| 27 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.DATE.TIME` | `FsGaRebateFeeAmountDefinition_DateTime` |  |  |  |
| 28 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.AUTHORISER` | `FsGaRebateFeeAmountDefinition_Authoriser` | String |  |  |
| 29 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.CO.CODE` | `FsGaRebateFeeAmountDefinition_CoCode` | String |  |  |
| 30 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.DEPT.CODE` | `FsGaRebateFeeAmountDefinition_DeptCode` | String |  |  |
| 31 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.AUDITOR.CODE` | `FsGaRebateFeeAmountDefinition_AuditorCode` | String |  |  |
| 32 | `FS.GA.REBATE.FEE.AMOUNT.DEFINITION.AUDIT.DATE.TIME` | `FsGaRebateFeeAmountDefinition_AuditDateTime` | String |  |  |
