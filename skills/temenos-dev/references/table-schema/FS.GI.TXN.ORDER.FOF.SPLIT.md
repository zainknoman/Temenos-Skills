# FS.GI.TXN.ORDER.FOF.SPLIT — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.ORDER.FOF.SPLIT` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.ORDER.FOF.SPLIT.PARENT.REF.ID` | `FsGiTxnOrderFofSplit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.TXN.ORDER.FOF.SPLIT.ORA.ROWID` | `FsGiTxnOrderFofSplit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.TXN.ORDER.FOF.SPLIT.ORDER.ID` | `FsGiTxnOrderFofSplit_OrderId` | TField |  | Order identification number. Multifonds DB Column is NORDER. |
| 4 | `FS.GI.TXN.ORDER.FOF.SPLIT.FOF.FUND.ID` | `FsGiTxnOrderFofSplit_FofFundId` | TField |  | Fund of Funds in which order being placed. Multifonds DB Column is NPTF_FOF. |
| 5 | `FS.GI.TXN.ORDER.FOF.SPLIT.FUND.ID` | `FsGiTxnOrderFofSplit_FundId` | TField |  | Fund which is linked as underlying fund to the Order Fund of Funds. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.TXN.ORDER.FOF.SPLIT.SHARE.CLASS.CODE` | `FsGiTxnOrderFofSplit_ShareClassCode` | TField |  | Fund share class of underlying fund which is linked to the order fund of funds. Multifonds DB Column is TPART. |
| 7 | `FS.GI.TXN.ORDER.FOF.SPLIT.SPLIT.PERCENTAGE` | `FsGiTxnOrderFofSplit_SplitPercentage` | TField |  | Split percentage of Fund of funds proportion of the investment. Multifonds DB Column is PCT_SPLIT. |
| 8 | `FS.GI.TXN.ORDER.FOF.SPLIT.SPLIT.AMOUNT` | `FsGiTxnOrderFofSplit_SplitAmount` | TField |  | Split amount of Fund of funds proportion of the investment. Multifonds DB Column is SPLIT_AMOUNT. |
| 9 | `FS.GI.TXN.ORDER.FOF.SPLIT.THRESHOLD.FLAG` | `FsGiTxnOrderFofSplit_ThresholdFlag` | TField |  | Flag to indicate threshold is applied. Multifonds DB Column is FLG_THRESHOLD. |
| 10 | `FS.GI.TXN.ORDER.FOF.SPLIT.THRESHOLD.AMOUNT` | `FsGiTxnOrderFofSplit_ThresholdAmount` | TField |  | Threshold amount for the underlying TA fund. Multifonds DB Column is THRESHOLD_AMT. |
| 11 | `FS.GI.TXN.ORDER.FOF.SPLIT.CURRENCY` | `FsGiTxnOrderFofSplit_Currency` | TField |  | Threshold currency code (in 3 letter format eg: USD). Multifonds DB Column is THRESHOLD_CMON. |
| 12 | `FS.GI.TXN.ORDER.FOF.SPLIT.SELECTED.PRICE` | `FsGiTxnOrderFofSplit_SelectedPrice` | TField |  | Select Price to be applied for the order. Multifonds DB Column is SELECT_PRICE. |
| 13 | `FS.GI.TXN.ORDER.FOF.SPLIT.FORCED.PRICE` | `FsGiTxnOrderFofSplit_ForcedPrice` | TField |  | Forced NAV price to be applied for the order. Multifonds DB Column is FORCE_PRICE. |
| 14 | `FS.GI.TXN.ORDER.FOF.SPLIT.AGENT.ID` | `FsGiTxnOrderFofSplit_AgentId` | TField |  | Agent Internal ID. Multifonds DB Column is NOUTLET. |
| 15 | `FS.GI.TXN.ORDER.FOF.SPLIT.OPERATION.CODE` | `FsGiTxnOrderFofSplit_OperationCode` | TField |  | Transaction type of the fund of funds order. Multifonds DB Column is COPERATION. |
| 16 | `FS.GI.TXN.ORDER.FOF.SPLIT.DEAL.REFERENCE` | `FsGiTxnOrderFofSplit_DealReference` | TField |  | Deal reference number of the order. Multifonds DB Column is DEAL_REF. |
| 17 | `FS.GI.TXN.ORDER.FOF.SPLIT.IN.DEAL.REFERENCE` | `FsGiTxnOrderFofSplit_InDealReference` | TField |  | Leg In Deal reference number of the order. Multifonds DB Column is DEAL_REF_IN. |
| 18 | `FS.GI.TXN.ORDER.FOF.SPLIT.LEG.LINK` | `FsGiTxnOrderFofSplit_LegLink` | TField |  | Leg link for switch / transfer order. Multifonds DB Column is LEG_LINK. |
| 19 | `FS.GI.TXN.ORDER.FOF.SPLIT.EFFECTIVE.DATE` | `FsGiTxnOrderFofSplit_EffectiveDate` | TField |  | The date from which the fund of fund functionality will be effective. Multifonds DB Column is EFFECTIVE_DATE. |
| 20 | `FS.GI.TXN.ORDER.FOF.SPLIT.END.DATE` | `FsGiTxnOrderFofSplit_EndDate` | TField |  | End date till which the fund of fund functionality will be effective. Multifonds DB Column is END_DATE. |
| 21 | `FS.GI.TXN.ORDER.FOF.SPLIT.SEQUENCE.ID` | `FsGiTxnOrderFofSplit_SequenceId` | TField |  | Sequence ID for the fund of fund split. Multifonds DB Column is SEQUENCE_NO. |
| 22 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED10` | `FsGiTxnOrderFofSplit_Reserved10` | TField |  |  |
| 23 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED9` | `FsGiTxnOrderFofSplit_Reserved9` | TField |  |  |
| 24 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED8` | `FsGiTxnOrderFofSplit_Reserved8` | TField |  |  |
| 25 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED7` | `FsGiTxnOrderFofSplit_Reserved7` | TField |  |  |
| 26 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED6` | `FsGiTxnOrderFofSplit_Reserved6` | TField |  |  |
| 27 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED5` | `FsGiTxnOrderFofSplit_Reserved5` | TField |  |  |
| 28 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED4` | `FsGiTxnOrderFofSplit_Reserved4` | TField |  |  |
| 29 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED3` | `FsGiTxnOrderFofSplit_Reserved3` | TField |  |  |
| 30 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED2` | `FsGiTxnOrderFofSplit_Reserved2` | TField |  |  |
| 31 | `FS.GI.TXN.ORDER.FOF.SPLIT.RESERVED1` | `FsGiTxnOrderFofSplit_Reserved1` | TField |  |  |
| 32 | `FS.GI.TXN.ORDER.FOF.SPLIT.LOCAL.REF` | `FsGiTxnOrderFofSplit_LocalRef` |  |  |  |
| 33 | `FS.GI.TXN.ORDER.FOF.SPLIT.OVERRIDE` | `FsGiTxnOrderFofSplit_Override` |  |  |  |
| 34 | `FS.GI.TXN.ORDER.FOF.SPLIT.RECORD.STATUS` | `FsGiTxnOrderFofSplit_RecordStatus` | String |  |  |
| 35 | `FS.GI.TXN.ORDER.FOF.SPLIT.CURR.NO` | `FsGiTxnOrderFofSplit_CurrNo` | String |  |  |
| 36 | `FS.GI.TXN.ORDER.FOF.SPLIT.INPUTTER` | `FsGiTxnOrderFofSplit_Inputter` |  |  |  |
| 37 | `FS.GI.TXN.ORDER.FOF.SPLIT.DATE.TIME` | `FsGiTxnOrderFofSplit_DateTime` |  |  |  |
| 38 | `FS.GI.TXN.ORDER.FOF.SPLIT.AUTHORISER` | `FsGiTxnOrderFofSplit_Authoriser` | String |  |  |
| 39 | `FS.GI.TXN.ORDER.FOF.SPLIT.CO.CODE` | `FsGiTxnOrderFofSplit_CoCode` | String |  |  |
| 40 | `FS.GI.TXN.ORDER.FOF.SPLIT.DEPT.CODE` | `FsGiTxnOrderFofSplit_DeptCode` | String |  |  |
| 41 | `FS.GI.TXN.ORDER.FOF.SPLIT.AUDITOR.CODE` | `FsGiTxnOrderFofSplit_AuditorCode` | String |  |  |
| 42 | `FS.GI.TXN.ORDER.FOF.SPLIT.AUDIT.DATE.TIME` | `FsGiTxnOrderFofSplit_AuditDateTime` | String |  |  |
