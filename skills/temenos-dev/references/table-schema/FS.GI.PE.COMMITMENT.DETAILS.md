# FS.GI.PE.COMMITMENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.COMMITMENT.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PE.COMMITMENT.DETAILS.REGISTER.ID` | `FsGiPeCommitmentDetails_RegisterId` |  |  |  |
| 2 | `GI.PE.COMMITMENT.DETAILS.FUND.ID` | `FsGiPeCommitmentDetails_FundId` |  |  |  |
| 3 | `GI.PE.COMMITMENT.DETAILS.COMMITMENT.ID` | `FsGiPeCommitmentDetails_CommitmentId` |  |  |  |
| 4 | `GI.PE.COMMITMENT.DETAILS.CAPITAL.INVESTMENT.ID` | `FsGiPeCommitmentDetails_CapitalInvestmentId` |  |  |  |
| 5 | `GI.PE.COMMITMENT.DETAILS.SEQUENCE.NUMBER` | `FsGiPeCommitmentDetails_SequenceNumber` |  |  |  |
| 6 | `GI.PE.COMMITMENT.DETAILS.EVENT.ID` | `FsGiPeCommitmentDetails_EventId` |  |  |  |
| 7 | `GI.PE.COMMITMENT.DETAILS.PE.RE.COMMENT` | `FsGiPeCommitmentDetails_PeReComment` |  |  |  |
| 8 | `GI.PE.COMMITMENT.DETAILS.COMMITTED.CAPITAL.AMOUNT` | `FsGiPeCommitmentDetails_CommittedCapitalAmount` |  |  |  |
| 9 | `GI.PE.COMMITMENT.DETAILS.INVESTED.AMOUNT` | `FsGiPeCommitmentDetails_InvestedAmount` |  |  |  |
| 10 | `GI.PE.COMMITMENT.DETAILS.FINAL.EQUALISATION.AMOUNT` | `FsGiPeCommitmentDetails_FinalEqualisationAmount` |  |  |  |
| 11 | `GI.PE.COMMITMENT.DETAILS.FINAL.FEE.AMOUNT` | `FsGiPeCommitmentDetails_FinalFeeAmount` |  |  |  |
| 12 | `GI.PE.COMMITMENT.DETAILS.STRUCTURING.FEES.AMT` | `FsGiPeCommitmentDetails_StructuringFeesAmt` |  |  |  |
| 13 | `GI.PE.COMMITMENT.DETAILS.COMPENSATION.LATE.INTEREST` | `FsGiPeCommitmentDetails_CompensationLateInterest` |  |  |  |
| 14 | `GI.PE.COMMITMENT.DETAILS.LATE.PAYMENT.INTEREST` | `FsGiPeCommitmentDetails_LatePaymentInterest` |  |  |  |
| 15 | `GI.PE.COMMITMENT.DETAILS.IMPACT.ON.SHARES` | `FsGiPeCommitmentDetails_ImpactOnShares` |  |  |  |
| 16 | `GI.PE.COMMITMENT.DETAILS.IMPACT.ON.UNCALLED.CAPITAL` | `FsGiPeCommitmentDetails_ImpactOnUncalledCapital` |  |  |  |
| 17 | `GI.PE.COMMITMENT.DETAILS.IMPACT.ON.STRUCTURING.FEES` | `FsGiPeCommitmentDetails_ImpactOnStructuringFees` |  |  |  |
| 18 | `GI.PE.COMMITMENT.DETAILS.DISTRIBUTED.AMOUNT.IN.QUO.CCY` | `FsGiPeCommitmentDetails_DistributedAmountInQuoCcy` |  |  |  |
| 19 | `GI.PE.COMMITMENT.DETAILS.RECALLABLE.CAPITAL.AMOUNT` | `FsGiPeCommitmentDetails_RecallableCapitalAmount` |  |  |  |
| 20 | `GI.PE.COMMITMENT.DETAILS.EXPIRY.DATE` | `FsGiPeCommitmentDetails_ExpiryDate` |  |  |  |
| 21 | `GI.PE.COMMITMENT.DETAILS.EVENT.DATE` | `FsGiPeCommitmentDetails_EventDate` |  |  |  |
| 22 | `GI.PE.COMMITMENT.DETAILS.SETTLEMENT.DATE` | `FsGiPeCommitmentDetails_SettlementDate` |  |  |  |
| 23 | `GI.PE.COMMITMENT.DETAILS.DUE.DATE` | `FsGiPeCommitmentDetails_DueDate` |  |  |  |
| 24 | `GI.PE.COMMITMENT.DETAILS.TRANSFER.DATE` | `FsGiPeCommitmentDetails_TransferDate` |  |  |  |
| 25 | `GI.PE.COMMITMENT.DETAILS.SWITCH.DATE` | `FsGiPeCommitmentDetails_SwitchDate` |  |  |  |
| 26 | `GI.PE.COMMITMENT.DETAILS.MESSAGE` | `FsGiPeCommitmentDetails_Message` |  |  |  |
| 27 | `GI.PE.COMMITMENT.DETAILS.STATUS` | `FsGiPeCommitmentDetails_Status` |  |  |  |
| 28 | `GI.PE.COMMITMENT.DETAILS.ORDER.ID` | `FsGiPeCommitmentDetails_OrderId` |  |  |  |
| 29 | `GI.PE.COMMITMENT.DETAILS.AGENT.ID` | `FsGiPeCommitmentDetails_AgentId` |  |  |  |
| 30 | `GI.PE.COMMITMENT.DETAILS.DEAL.REFERENCE` | `FsGiPeCommitmentDetails_DealReference` |  |  |  |
| 31 | `GI.PE.COMMITMENT.DETAILS.LEG.LINK` | `FsGiPeCommitmentDetails_LegLink` |  |  |  |
| 32 | `GI.PE.COMMITMENT.DETAILS.DISTRIBUTION.SEQUENCE.NUMBER` | `FsGiPeCommitmentDetails_DistributionSequenceNumber` |  |  |  |
| 33 | `GI.PE.COMMITMENT.DETAILS.BULKED.ORDER.SEQ` | `FsGiPeCommitmentDetails_BulkedOrderSeq` |  |  |  |
| 34 | `GI.PE.COMMITMENT.DETAILS.LINKED.SEQUENCE` | `FsGiPeCommitmentDetails_LinkedSequence` |  |  |  |
| 35 | `GI.PE.COMMITMENT.DETAILS.GROUP.ID` | `FsGiPeCommitmentDetails_GroupId` |  |  |  |
| 36 | `GI.PE.COMMITMENT.DETAILS.REGISTER.IN` | `FsGiPeCommitmentDetails_RegisterIn` |  |  |  |
| 37 | `GI.PE.COMMITMENT.DETAILS.COMMITMENT.ID.2` | `FsGiPeCommitmentDetails_CommitmentId2` |  |  |  |
| 38 | `GI.PE.COMMITMENT.DETAILS.FUND.LINK` | `FsGiPeCommitmentDetails_FundLink` |  |  |  |
| 39 | `GI.PE.COMMITMENT.DETAILS.LINKED.SHARE.CLASS.CODE` | `FsGiPeCommitmentDetails_LinkedShareClassCode` |  |  |  |
| 40 | `GI.PE.COMMITMENT.DETAILS.RECALLABLE.FLAG` | `FsGiPeCommitmentDetails_RecallableFlag` |  |  |  |
| 41 | `GI.PE.COMMITMENT.DETAILS.QUANTITY` | `FsGiPeCommitmentDetails_Quantity` |  |  |  |
| 42 | `GI.PE.COMMITMENT.DETAILS.TRANSFER.PRICE` | `FsGiPeCommitmentDetails_TransferPrice` |  |  |  |
| 43 | `GI.PE.COMMITMENT.DETAILS.RESERVED10` | `FsGiPeCommitmentDetails_Reserved10` |  |  |  |
| 44 | `GI.PE.COMMITMENT.DETAILS.RESERVED9` | `FsGiPeCommitmentDetails_Reserved9` |  |  |  |
| 45 | `GI.PE.COMMITMENT.DETAILS.RESERVED8` | `FsGiPeCommitmentDetails_Reserved8` |  |  |  |
| 46 | `GI.PE.COMMITMENT.DETAILS.RESERVED7` | `FsGiPeCommitmentDetails_Reserved7` |  |  |  |
| 47 | `GI.PE.COMMITMENT.DETAILS.RESERVED6` | `FsGiPeCommitmentDetails_Reserved6` |  |  |  |
| 48 | `GI.PE.COMMITMENT.DETAILS.RESERVED5` | `FsGiPeCommitmentDetails_Reserved5` |  |  |  |
| 49 | `GI.PE.COMMITMENT.DETAILS.RESERVED4` | `FsGiPeCommitmentDetails_Reserved4` |  |  |  |
| 50 | `GI.PE.COMMITMENT.DETAILS.RESERVED3` | `FsGiPeCommitmentDetails_Reserved3` |  |  |  |
| 51 | `GI.PE.COMMITMENT.DETAILS.RESERVED2` | `FsGiPeCommitmentDetails_Reserved2` |  |  |  |
| 52 | `GI.PE.COMMITMENT.DETAILS.RESERVED1` | `FsGiPeCommitmentDetails_Reserved1` |  |  |  |
| 53 | `GI.PE.COMMITMENT.DETAILS.LOCAL.REF` | `FsGiPeCommitmentDetails_LocalRef` |  |  |  |
| 54 | `GI.PE.COMMITMENT.DETAILS.OVERRIDE` | `FsGiPeCommitmentDetails_Override` |  |  |  |
| 55 | `GI.PE.COMMITMENT.DETAILS.RECORD.STATUS` | `FsGiPeCommitmentDetails_RecordStatus` |  |  |  |
| 56 | `GI.PE.COMMITMENT.DETAILS.CURR.NO` | `FsGiPeCommitmentDetails_CurrNo` |  |  |  |
| 57 | `GI.PE.COMMITMENT.DETAILS.INPUTTER` | `FsGiPeCommitmentDetails_Inputter` |  |  |  |
| 58 | `GI.PE.COMMITMENT.DETAILS.DATE.TIME` | `FsGiPeCommitmentDetails_DateTime` |  |  |  |
| 59 | `GI.PE.COMMITMENT.DETAILS.AUTHORISER` | `FsGiPeCommitmentDetails_Authoriser` |  |  |  |
| 60 | `GI.PE.COMMITMENT.DETAILS.CO.CODE` | `FsGiPeCommitmentDetails_CoCode` |  |  |  |
| 61 | `GI.PE.COMMITMENT.DETAILS.DEPT.CODE` | `FsGiPeCommitmentDetails_DeptCode` |  |  |  |
| 62 | `GI.PE.COMMITMENT.DETAILS.AUDITOR.CODE` | `FsGiPeCommitmentDetails_AuditorCode` |  |  |  |
| 63 | `GI.PE.COMMITMENT.DETAILS.AUDIT.DATE.TIME` | `FsGiPeCommitmentDetails_AuditDateTime` |  |  |  |
