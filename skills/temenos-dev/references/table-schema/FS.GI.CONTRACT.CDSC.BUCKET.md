# FS.GI.CONTRACT.CDSC.BUCKET — Table Schema

> Source: `INSERTS/I_F.FS.GI.CONTRACT.CDSC.BUCKET` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.CONTRACT.CDSC.BUCKET.PARENT.REF.ID` | `FsGiContractCdscBucket_ParentRefId` |  |  |  |
| 2 | `FS.GI.CONTRACT.CDSC.BUCKET.ORA.ROWID` | `FsGiContractCdscBucket_OraRowid` |  |  |  |
| 3 | `FS.GI.CONTRACT.CDSC.BUCKET.BUCKET.ID` | `FsGiContractCdscBucket_BucketId` |  |  |  |
| 4 | `FS.GI.CONTRACT.CDSC.BUCKET.ORDER.ID` | `FsGiContractCdscBucket_OrderId` |  |  |  |
| 5 | `FS.GI.CONTRACT.CDSC.BUCKET.DEAL.REFERENCE` | `FsGiContractCdscBucket_DealReference` |  |  |  |
| 6 | `FS.GI.CONTRACT.CDSC.BUCKET.AGENT.ID` | `FsGiContractCdscBucket_AgentId` |  |  |  |
| 7 | `FS.GI.CONTRACT.CDSC.BUCKET.TRADE.DATE` | `FsGiContractCdscBucket_TradeDate` |  |  |  |
| 8 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY` | `FsGiContractCdscBucket_Quantity` |  |  |  |
| 9 | `FS.GI.CONTRACT.CDSC.BUCKET.APPLIED.NAV` | `FsGiContractCdscBucket_AppliedNav` |  |  |  |
| 10 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.FREE.SHARE` | `FsGiContractCdscBucket_QuantityFreeShare` |  |  |  |
| 11 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.USED` | `FsGiContractCdscBucket_QuantityUsed` |  |  |  |
| 12 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.USED.PERCENT` | `FsGiContractCdscBucket_QuantityUsedPercent` |  |  |  |
| 13 | `FS.GI.CONTRACT.CDSC.BUCKET.LEG.LINK` | `FsGiContractCdscBucket_LegLink` |  |  |  |
| 14 | `FS.GI.CONTRACT.CDSC.BUCKET.ORDER.LINKED.ID` | `FsGiContractCdscBucket_OrderLinkedId` |  |  |  |
| 15 | `FS.GI.CONTRACT.CDSC.BUCKET.CONTRACT.ID` | `FsGiContractCdscBucket_ContractId` |  |  |  |
| 16 | `FS.GI.CONTRACT.CDSC.BUCKET.REGISTER.ID` | `FsGiContractCdscBucket_RegisterId` |  |  |  |
| 17 | `FS.GI.CONTRACT.CDSC.BUCKET.FUND.ID` | `FsGiContractCdscBucket_FundId` |  |  |  |
| 18 | `FS.GI.CONTRACT.CDSC.BUCKET.SHARE.CLASS.CODE` | `FsGiContractCdscBucket_ShareClassCode` |  |  |  |
| 19 | `FS.GI.CONTRACT.CDSC.BUCKET.LEGAL.ENTITY.ID` | `FsGiContractCdscBucket_LegalEntityId` |  |  |  |
| 20 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.SWITCH.OUT` | `FsGiContractCdscBucket_QuantitySwitchOut` |  |  |  |
| 21 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.SWITCH.OUT.PERCENT` | `FsGiContractCdscBucket_QuantitySwitchOutPercent` |  |  |  |
| 22 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.SWITCH.IN` | `FsGiContractCdscBucket_QuantitySwitchIn` |  |  |  |
| 23 | `FS.GI.CONTRACT.CDSC.BUCKET.NAV` | `FsGiContractCdscBucket_Nav` |  |  |  |
| 24 | `FS.GI.CONTRACT.CDSC.BUCKET.LINKED.CONTRACT.ID` | `FsGiContractCdscBucket_LinkedContractId` |  |  |  |
| 25 | `FS.GI.CONTRACT.CDSC.BUCKET.BUCKET.FLAG` | `FsGiContractCdscBucket_BucketFlag` |  |  |  |
| 26 | `FS.GI.CONTRACT.CDSC.BUCKET.STATUS` | `FsGiContractCdscBucket_Status` |  |  |  |
| 27 | `FS.GI.CONTRACT.CDSC.BUCKET.LINKED.BUCKET.ID` | `FsGiContractCdscBucket_LinkedBucketId` |  |  |  |
| 28 | `FS.GI.CONTRACT.CDSC.BUCKET.CONTRACT.AMOUNT.USED` | `FsGiContractCdscBucket_ContractAmountUsed` |  |  |  |
| 29 | `FS.GI.CONTRACT.CDSC.BUCKET.FUND.AMOUNT.MASTER.CCY` | `FsGiContractCdscBucket_FundAmountMasterCcy` |  |  |  |
| 30 | `FS.GI.CONTRACT.CDSC.BUCKET.TOTAL.COMMISSION` | `FsGiContractCdscBucket_TotalCommission` |  |  |  |
| 31 | `FS.GI.CONTRACT.CDSC.BUCKET.INVESTOR.AMOUNT` | `FsGiContractCdscBucket_InvestorAmount` |  |  |  |
| 32 | `FS.GI.CONTRACT.CDSC.BUCKET.AMOUNT.NAV` | `FsGiContractCdscBucket_AmountNav` |  |  |  |
| 33 | `FS.GI.CONTRACT.CDSC.BUCKET.CREDIT.FLAG` | `FsGiContractCdscBucket_CreditFlag` |  |  |  |
| 34 | `FS.GI.CONTRACT.CDSC.BUCKET.CONTRACT.OPERATION.CODE` | `FsGiContractCdscBucket_ContractOperationCode` |  |  |  |
| 35 | `FS.GI.CONTRACT.CDSC.BUCKET.QUANTITY.SWITCH.OUT.ACT` | `FsGiContractCdscBucket_QuantitySwitchOutAct` |  |  |  |
| 36 | `FS.GI.CONTRACT.CDSC.BUCKET.NAV.PRICE.ACT` | `FsGiContractCdscBucket_NavPriceAct` |  |  |  |
| 37 | `FS.GI.CONTRACT.CDSC.BUCKET.TEMP.CONTRACT` | `FsGiContractCdscBucket_TempContract` |  |  |  |
| 38 | `FS.GI.CONTRACT.CDSC.BUCKET.COMMISSION.CDSC.BUCKET` | `FsGiContractCdscBucket_CommissionCdscBucket` |  |  |  |
| 39 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED10` | `FsGiContractCdscBucket_Reserved10` |  |  |  |
| 40 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED9` | `FsGiContractCdscBucket_Reserved9` |  |  |  |
| 41 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED8` | `FsGiContractCdscBucket_Reserved8` |  |  |  |
| 42 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED7` | `FsGiContractCdscBucket_Reserved7` |  |  |  |
| 43 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED6` | `FsGiContractCdscBucket_Reserved6` |  |  |  |
| 44 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED5` | `FsGiContractCdscBucket_Reserved5` |  |  |  |
| 45 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED4` | `FsGiContractCdscBucket_Reserved4` |  |  |  |
| 46 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED3` | `FsGiContractCdscBucket_Reserved3` |  |  |  |
| 47 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED2` | `FsGiContractCdscBucket_Reserved2` |  |  |  |
| 48 | `FS.GI.CONTRACT.CDSC.BUCKET.RESERVED1` | `FsGiContractCdscBucket_Reserved1` |  |  |  |
| 49 | `FS.GI.CONTRACT.CDSC.BUCKET.LOCAL.REF` | `FsGiContractCdscBucket_LocalRef` |  |  |  |
| 50 | `FS.GI.CONTRACT.CDSC.BUCKET.OVERRIDE` | `FsGiContractCdscBucket_Override` |  |  |  |
| 51 | `FS.GI.CONTRACT.CDSC.BUCKET.RECORD.STATUS` | `FsGiContractCdscBucket_RecordStatus` |  |  |  |
| 52 | `FS.GI.CONTRACT.CDSC.BUCKET.CURR.NO` | `FsGiContractCdscBucket_CurrNo` |  |  |  |
| 53 | `FS.GI.CONTRACT.CDSC.BUCKET.INPUTTER` | `FsGiContractCdscBucket_Inputter` |  |  |  |
| 54 | `FS.GI.CONTRACT.CDSC.BUCKET.DATE.TIME` | `FsGiContractCdscBucket_DateTime` |  |  |  |
| 55 | `FS.GI.CONTRACT.CDSC.BUCKET.AUTHORISER` | `FsGiContractCdscBucket_Authoriser` |  |  |  |
| 56 | `FS.GI.CONTRACT.CDSC.BUCKET.CO.CODE` | `FsGiContractCdscBucket_CoCode` |  |  |  |
| 57 | `FS.GI.CONTRACT.CDSC.BUCKET.DEPT.CODE` | `FsGiContractCdscBucket_DeptCode` |  |  |  |
| 58 | `FS.GI.CONTRACT.CDSC.BUCKET.AUDITOR.CODE` | `FsGiContractCdscBucket_AuditorCode` |  |  |  |
| 59 | `FS.GI.CONTRACT.CDSC.BUCKET.AUDIT.DATE.TIME` | `FsGiContractCdscBucket_AuditDateTime` |  |  |  |
