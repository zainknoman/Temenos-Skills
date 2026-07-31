# FS.GI.PE.DISTRIBUTION.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.DISTRIBUTION.MASTER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PE.DISTRIBUTION.MASTER.EVENT.ID` | `FsGiPeDistributionMaster_EventId` |  |  |  |
| 2 | `GI.PE.DISTRIBUTION.MASTER.FUND.ID` | `FsGiPeDistributionMaster_FundId` |  |  |  |
| 3 | `GI.PE.DISTRIBUTION.MASTER.SHARE.CLASS.CODE` | `FsGiPeDistributionMaster_ShareClassCode` |  |  |  |
| 4 | `GI.PE.DISTRIBUTION.MASTER.QUOTATION.CURRENCY` | `FsGiPeDistributionMaster_QuotationCurrency` |  |  |  |
| 5 | `GI.PE.DISTRIBUTION.MASTER.TRANCHE` | `FsGiPeDistributionMaster_Tranche` |  |  |  |
| 6 | `GI.PE.DISTRIBUTION.MASTER.LEGAL.ENTITY.ID` | `FsGiPeDistributionMaster_LegalEntityId` |  |  |  |
| 7 | `GI.PE.DISTRIBUTION.MASTER.NAV.PRICE` | `FsGiPeDistributionMaster_NavPrice` |  |  |  |
| 8 | `GI.PE.DISTRIBUTION.MASTER.RECORD.DATE` | `FsGiPeDistributionMaster_RecordDate` |  |  |  |
| 9 | `GI.PE.DISTRIBUTION.MASTER.EX.DATE` | `FsGiPeDistributionMaster_ExDate` |  |  |  |
| 10 | `GI.PE.DISTRIBUTION.MASTER.TRADE.DATE` | `FsGiPeDistributionMaster_TradeDate` |  |  |  |
| 11 | `GI.PE.DISTRIBUTION.MASTER.VALUE.DATE` | `FsGiPeDistributionMaster_ValueDate` |  |  |  |
| 12 | `GI.PE.DISTRIBUTION.MASTER.DISTRIBUTION.SEQUENCE.NUMBER` | `FsGiPeDistributionMaster_DistributionSequenceNumber` |  |  |  |
| 13 | `GI.PE.DISTRIBUTION.MASTER.STATUS` | `FsGiPeDistributionMaster_Status` |  |  |  |
| 14 | `GI.PE.DISTRIBUTION.MASTER.GROUP.ID` | `FsGiPeDistributionMaster_GroupId` |  |  |  |
| 15 | `GI.PE.DISTRIBUTION.MASTER.LINK.DIST.SEQUENCE.NUMBER` | `FsGiPeDistributionMaster_LinkDistSequenceNumber` |  |  |  |
| 16 | `GI.PE.DISTRIBUTION.MASTER.AMOUNT.PER.SHARE.FLAG` | `FsGiPeDistributionMaster_AmountPerShareFlag` |  |  |  |
| 17 | `GI.PE.DISTRIBUTION.MASTER.GLOBAL.AMOUNT.FLAG` | `FsGiPeDistributionMaster_GlobalAmountFlag` |  |  |  |
| 18 | `GI.PE.DISTRIBUTION.MASTER.PROFIT.LOSS.DIST.AMOUNT` | `FsGiPeDistributionMaster_ProfitLossDistAmount` |  |  |  |
| 19 | `GI.PE.DISTRIBUTION.MASTER.INCOME.DISTRIBUTION.AMOUNT` | `FsGiPeDistributionMaster_IncomeDistributionAmount` |  |  |  |
| 20 | `GI.PE.DISTRIBUTION.MASTER.CAPITAL.DISTRIBUTION.AMOUNT` | `FsGiPeDistributionMaster_CapitalDistributionAmount` |  |  |  |
| 21 | `GI.PE.DISTRIBUTION.MASTER.OTHER.AMOUNT` | `FsGiPeDistributionMaster_OtherAmount` |  |  |  |
| 22 | `GI.PE.DISTRIBUTION.MASTER.RECALLABLE.CAPITAL.AMOUNT` | `FsGiPeDistributionMaster_RecallableCapitalAmount` |  |  |  |
| 23 | `GI.PE.DISTRIBUTION.MASTER.EXPIRY.DATE` | `FsGiPeDistributionMaster_ExpiryDate` |  |  |  |
| 24 | `GI.PE.DISTRIBUTION.MASTER.DISTRIBUTED.AMOUNT.IN.QUO.CCY` | `FsGiPeDistributionMaster_DistributedAmountInQuoCcy` |  |  |  |
| 25 | `GI.PE.DISTRIBUTION.MASTER.DIST.QUOTATION.CURRENCY` | `FsGiPeDistributionMaster_DistQuotationCurrency` |  |  |  |
| 26 | `GI.PE.DISTRIBUTION.MASTER.DISTRIBUTED.AMOUNT.IN.PAY.CCY` | `FsGiPeDistributionMaster_DistributedAmountInPayCcy` |  |  |  |
| 27 | `GI.PE.DISTRIBUTION.MASTER.DIST.PAYMENT.CURRENCY` | `FsGiPeDistributionMaster_DistPaymentCurrency` |  |  |  |
| 28 | `GI.PE.DISTRIBUTION.MASTER.MESSAGE` | `FsGiPeDistributionMaster_Message` |  |  |  |
| 29 | `GI.PE.DISTRIBUTION.MASTER.PE.RE.COMMENT` | `FsGiPeDistributionMaster_PeReComment` |  |  |  |
| 30 | `GI.PE.DISTRIBUTION.MASTER.RESERVED10` | `FsGiPeDistributionMaster_Reserved10` |  |  |  |
| 31 | `GI.PE.DISTRIBUTION.MASTER.RESERVED9` | `FsGiPeDistributionMaster_Reserved9` |  |  |  |
| 32 | `GI.PE.DISTRIBUTION.MASTER.RESERVED8` | `FsGiPeDistributionMaster_Reserved8` |  |  |  |
| 33 | `GI.PE.DISTRIBUTION.MASTER.RESERVED7` | `FsGiPeDistributionMaster_Reserved7` |  |  |  |
| 34 | `GI.PE.DISTRIBUTION.MASTER.RESERVED6` | `FsGiPeDistributionMaster_Reserved6` |  |  |  |
| 35 | `GI.PE.DISTRIBUTION.MASTER.RESERVED5` | `FsGiPeDistributionMaster_Reserved5` |  |  |  |
| 36 | `GI.PE.DISTRIBUTION.MASTER.RESERVED4` | `FsGiPeDistributionMaster_Reserved4` |  |  |  |
| 37 | `GI.PE.DISTRIBUTION.MASTER.RESERVED3` | `FsGiPeDistributionMaster_Reserved3` |  |  |  |
| 38 | `GI.PE.DISTRIBUTION.MASTER.RESERVED2` | `FsGiPeDistributionMaster_Reserved2` |  |  |  |
| 39 | `GI.PE.DISTRIBUTION.MASTER.RESERVED1` | `FsGiPeDistributionMaster_Reserved1` |  |  |  |
| 40 | `GI.PE.DISTRIBUTION.MASTER.LOCAL.REF` | `FsGiPeDistributionMaster_LocalRef` |  |  |  |
| 41 | `GI.PE.DISTRIBUTION.MASTER.OVERRIDE` | `FsGiPeDistributionMaster_Override` |  |  |  |
| 42 | `GI.PE.DISTRIBUTION.MASTER.RECORD.STATUS` | `FsGiPeDistributionMaster_RecordStatus` |  |  |  |
| 43 | `GI.PE.DISTRIBUTION.MASTER.CURR.NO` | `FsGiPeDistributionMaster_CurrNo` |  |  |  |
| 44 | `GI.PE.DISTRIBUTION.MASTER.INPUTTER` | `FsGiPeDistributionMaster_Inputter` |  |  |  |
| 45 | `GI.PE.DISTRIBUTION.MASTER.DATE.TIME` | `FsGiPeDistributionMaster_DateTime` |  |  |  |
| 46 | `GI.PE.DISTRIBUTION.MASTER.AUTHORISER` | `FsGiPeDistributionMaster_Authoriser` |  |  |  |
| 47 | `GI.PE.DISTRIBUTION.MASTER.CO.CODE` | `FsGiPeDistributionMaster_CoCode` |  |  |  |
| 48 | `GI.PE.DISTRIBUTION.MASTER.DEPT.CODE` | `FsGiPeDistributionMaster_DeptCode` |  |  |  |
| 49 | `GI.PE.DISTRIBUTION.MASTER.AUDITOR.CODE` | `FsGiPeDistributionMaster_AuditorCode` |  |  |  |
| 50 | `GI.PE.DISTRIBUTION.MASTER.AUDIT.DATE.TIME` | `FsGiPeDistributionMaster_AuditDateTime` |  |  |  |
