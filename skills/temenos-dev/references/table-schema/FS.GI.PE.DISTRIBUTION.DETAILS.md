# FS.GI.PE.DISTRIBUTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.DISTRIBUTION.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PE.DISTRIBUTION.DETAILS.FUND.ID` | `FsGiPeDistributionDetails_FundId` |  |  |  |
| 2 | `GI.PE.DISTRIBUTION.DETAILS.SHARE.CLASS.CODE` | `FsGiPeDistributionDetails_ShareClassCode` |  |  |  |
| 3 | `GI.PE.DISTRIBUTION.DETAILS.EVENT.ID` | `FsGiPeDistributionDetails_EventId` |  |  |  |
| 4 | `GI.PE.DISTRIBUTION.DETAILS.DISTRIBUTION.SEQUENCE.NUMBER` | `FsGiPeDistributionDetails_DistributionSequenceNumber` |  |  |  |
| 5 | `GI.PE.DISTRIBUTION.DETAILS.REGISTER.ID` | `FsGiPeDistributionDetails_RegisterId` |  |  |  |
| 6 | `GI.PE.DISTRIBUTION.DETAILS.ACCOUNT.REFERENCE` | `FsGiPeDistributionDetails_AccountReference` |  |  |  |
| 7 | `GI.PE.DISTRIBUTION.DETAILS.COMMITMENT.ID` | `FsGiPeDistributionDetails_CommitmentId` |  |  |  |
| 8 | `GI.PE.DISTRIBUTION.DETAILS.QUANTITY` | `FsGiPeDistributionDetails_Quantity` |  |  |  |
| 9 | `GI.PE.DISTRIBUTION.DETAILS.DISTRIBUTION.PERCENTAGE` | `FsGiPeDistributionDetails_DistributionPercentage` |  |  |  |
| 10 | `GI.PE.DISTRIBUTION.DETAILS.PROFIT.LOSS.DIST.AMOUNT` | `FsGiPeDistributionDetails_ProfitLossDistAmount` |  |  |  |
| 11 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE.PROFIT.LOSS.AMOUNT` | `FsGiPeDistributionDetails_OverrideProfitLossAmount` |  |  |  |
| 12 | `GI.PE.DISTRIBUTION.DETAILS.INCOME.DISTRIBUTION.AMOUNT` | `FsGiPeDistributionDetails_IncomeDistributionAmount` |  |  |  |
| 13 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE.INCOME.DIST.AMT` | `FsGiPeDistributionDetails_OverrideIncomeDistAmt` |  |  |  |
| 14 | `GI.PE.DISTRIBUTION.DETAILS.CAPITAL.DISTRIBUTION.AMOUNT` | `FsGiPeDistributionDetails_CapitalDistributionAmount` |  |  |  |
| 15 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE.CAPITAL.DIST.AMT` | `FsGiPeDistributionDetails_OverrideCapitalDistAmt` |  |  |  |
| 16 | `GI.PE.DISTRIBUTION.DETAILS.OTHER.AMOUNT` | `FsGiPeDistributionDetails_OtherAmount` |  |  |  |
| 17 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE.OTHER.AMOUNT` | `FsGiPeDistributionDetails_OverrideOtherAmount` |  |  |  |
| 18 | `GI.PE.DISTRIBUTION.DETAILS.DISTRIBUTED.AMOUNT.IN.QUO.CCY` | `FsGiPeDistributionDetails_DistributedAmountInQuoCcy` |  |  |  |
| 19 | `GI.PE.DISTRIBUTION.DETAILS.DISTRIBUTED.AMOUNT.IN.PAY.CCY` | `FsGiPeDistributionDetails_DistributedAmountInPayCcy` |  |  |  |
| 20 | `GI.PE.DISTRIBUTION.DETAILS.RECALLABLE.CAPITAL.AMOUNT` | `FsGiPeDistributionDetails_RecallableCapitalAmount` |  |  |  |
| 21 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE.RECALLABLE.CAP.AMT` | `FsGiPeDistributionDetails_OverrideRecallableCapAmt` |  |  |  |
| 22 | `GI.PE.DISTRIBUTION.DETAILS.OUT.RECALC.CAPITAL.AMOUNT` | `FsGiPeDistributionDetails_OutRecalcCapitalAmount` |  |  |  |
| 23 | `GI.PE.DISTRIBUTION.DETAILS.CANCEL.RECALC.CAPITAL.AMOUNT` | `FsGiPeDistributionDetails_CancelRecalcCapitalAmount` |  |  |  |
| 24 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE.CNCL.RECALLABLE.CAP` | `FsGiPeDistributionDetails_OverrideCnclRecallableCap` |  |  |  |
| 25 | `GI.PE.DISTRIBUTION.DETAILS.TAX.AMOUNT` | `FsGiPeDistributionDetails_TaxAmount` |  |  |  |
| 26 | `GI.PE.DISTRIBUTION.DETAILS.STATUS` | `FsGiPeDistributionDetails_Status` |  |  |  |
| 27 | `GI.PE.DISTRIBUTION.DETAILS.DEAL.REFERENCE` | `FsGiPeDistributionDetails_DealReference` |  |  |  |
| 28 | `GI.PE.DISTRIBUTION.DETAILS.ORDER.ID` | `FsGiPeDistributionDetails_OrderId` |  |  |  |
| 29 | `GI.PE.DISTRIBUTION.DETAILS.AGENT.ID` | `FsGiPeDistributionDetails_AgentId` |  |  |  |
| 30 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED10` | `FsGiPeDistributionDetails_Reserved10` |  |  |  |
| 31 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED9` | `FsGiPeDistributionDetails_Reserved9` |  |  |  |
| 32 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED8` | `FsGiPeDistributionDetails_Reserved8` |  |  |  |
| 33 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED7` | `FsGiPeDistributionDetails_Reserved7` |  |  |  |
| 34 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED6` | `FsGiPeDistributionDetails_Reserved6` |  |  |  |
| 35 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED5` | `FsGiPeDistributionDetails_Reserved5` |  |  |  |
| 36 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED4` | `FsGiPeDistributionDetails_Reserved4` |  |  |  |
| 37 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED3` | `FsGiPeDistributionDetails_Reserved3` |  |  |  |
| 38 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED2` | `FsGiPeDistributionDetails_Reserved2` |  |  |  |
| 39 | `GI.PE.DISTRIBUTION.DETAILS.RESERVED1` | `FsGiPeDistributionDetails_Reserved1` |  |  |  |
| 40 | `GI.PE.DISTRIBUTION.DETAILS.LOCAL.REF` | `FsGiPeDistributionDetails_LocalRef` |  |  |  |
| 41 | `GI.PE.DISTRIBUTION.DETAILS.OVERRIDE` | `FsGiPeDistributionDetails_Override` |  |  |  |
| 42 | `GI.PE.DISTRIBUTION.DETAILS.RECORD.STATUS` | `FsGiPeDistributionDetails_RecordStatus` |  |  |  |
| 43 | `GI.PE.DISTRIBUTION.DETAILS.CURR.NO` | `FsGiPeDistributionDetails_CurrNo` |  |  |  |
| 44 | `GI.PE.DISTRIBUTION.DETAILS.INPUTTER` | `FsGiPeDistributionDetails_Inputter` |  |  |  |
| 45 | `GI.PE.DISTRIBUTION.DETAILS.DATE.TIME` | `FsGiPeDistributionDetails_DateTime` |  |  |  |
| 46 | `GI.PE.DISTRIBUTION.DETAILS.AUTHORISER` | `FsGiPeDistributionDetails_Authoriser` |  |  |  |
| 47 | `GI.PE.DISTRIBUTION.DETAILS.CO.CODE` | `FsGiPeDistributionDetails_CoCode` |  |  |  |
| 48 | `GI.PE.DISTRIBUTION.DETAILS.DEPT.CODE` | `FsGiPeDistributionDetails_DeptCode` |  |  |  |
| 49 | `GI.PE.DISTRIBUTION.DETAILS.AUDITOR.CODE` | `FsGiPeDistributionDetails_AuditorCode` |  |  |  |
| 50 | `GI.PE.DISTRIBUTION.DETAILS.AUDIT.DATE.TIME` | `FsGiPeDistributionDetails_AuditDateTime` |  |  |  |
