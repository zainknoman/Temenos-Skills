# FS.GI.PE.EVENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.EVENT.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.PE.EVENT.DETAILS.EVENT.ID` | `FsGiPeEventDetails_EventId` |  |  |  |
| 2 | `FS.GI.PE.EVENT.DETAILS.REGISTER.ID` | `FsGiPeEventDetails_RegisterId` |  |  |  |
| 3 | `FS.GI.PE.EVENT.DETAILS.COMMITMENT.ID` | `FsGiPeEventDetails_CommitmentId` |  |  |  |
| 4 | `FS.GI.PE.EVENT.DETAILS.FUND.ID` | `FsGiPeEventDetails_FundId` |  |  |  |
| 5 | `FS.GI.PE.EVENT.DETAILS.SHARE.CLASS.CODE` | `FsGiPeEventDetails_ShareClassCode` |  |  |  |
| 6 | `FS.GI.PE.EVENT.DETAILS.TRANCHE` | `FsGiPeEventDetails_Tranche` |  |  |  |
| 7 | `FS.GI.PE.EVENT.DETAILS.COMMITTED.CAPITAL.AMOUNT` | `FsGiPeEventDetails_CommittedCapitalAmount` |  |  |  |
| 8 | `FS.GI.PE.EVENT.DETAILS.UNCALLED.CAPITAL` | `FsGiPeEventDetails_UncalledCapital` |  |  |  |
| 9 | `FS.GI.PE.EVENT.DETAILS.EQUALISATION.AMOUNT` | `FsGiPeEventDetails_EqualisationAmount` |  |  |  |
| 10 | `FS.GI.PE.EVENT.DETAILS.EQUALISATION.AMOUNT.OVERRIDE` | `FsGiPeEventDetails_EqualisationAmountOverride` |  |  |  |
| 11 | `FS.GI.PE.EVENT.DETAILS.FINAL.EQUALISATION.AMOUNT` | `FsGiPeEventDetails_FinalEqualisationAmount` |  |  |  |
| 12 | `FS.GI.PE.EVENT.DETAILS.CAPITAL.CALL` | `FsGiPeEventDetails_CapitalCall` |  |  |  |
| 13 | `FS.GI.PE.EVENT.DETAILS.CAPITAL.CALL.OVERRIDE.AMOUNT` | `FsGiPeEventDetails_CapitalCallOverrideAmount` |  |  |  |
| 14 | `FS.GI.PE.EVENT.DETAILS.TOTAL.CALLED.AMOUNT` | `FsGiPeEventDetails_TotalCalledAmount` |  |  |  |
| 15 | `FS.GI.PE.EVENT.DETAILS.FEE.AMOUNT` | `FsGiPeEventDetails_FeeAmount` |  |  |  |
| 16 | `FS.GI.PE.EVENT.DETAILS.FEE.AMOUNT.OVERRIDE` | `FsGiPeEventDetails_FeeAmountOverride` |  |  |  |
| 17 | `FS.GI.PE.EVENT.DETAILS.FINAL.FEE.AMOUNT` | `FsGiPeEventDetails_FinalFeeAmount` |  |  |  |
| 18 | `FS.GI.PE.EVENT.DETAILS.STRUCTURING.FEES.PERCENTAGE` | `FsGiPeEventDetails_StructuringFeesPercentage` |  |  |  |
| 19 | `FS.GI.PE.EVENT.DETAILS.STRUCTURING.FEES.AMT` | `FsGiPeEventDetails_StructuringFeesAmt` |  |  |  |
| 20 | `FS.GI.PE.EVENT.DETAILS.STRUCTURING.FEES.AMT.OVERRIDE` | `FsGiPeEventDetails_StructuringFeesAmtOverride` |  |  |  |
| 21 | `FS.GI.PE.EVENT.DETAILS.FINAL.STRUCTURING.FEES.AMOUNT` | `FsGiPeEventDetails_FinalStructuringFeesAmount` |  |  |  |
| 22 | `FS.GI.PE.EVENT.DETAILS.RECALCULATED.CALL.AMOUNT` | `FsGiPeEventDetails_RecalculatedCallAmount` |  |  |  |
| 23 | `FS.GI.PE.EVENT.DETAILS.DIFFERENCE.IN.CALL.AMOUNT` | `FsGiPeEventDetails_DifferenceInCallAmount` |  |  |  |
| 24 | `FS.GI.PE.EVENT.DETAILS.COMPENSATION.LATE.INTEREST` | `FsGiPeEventDetails_CompensationLateInterest` |  |  |  |
| 25 | `FS.GI.PE.EVENT.DETAILS.COMPENSATION.LATE.INT.OVERRIDE` | `FsGiPeEventDetails_CompensationLateIntOverride` |  |  |  |
| 26 | `FS.GI.PE.EVENT.DETAILS.COMPENSATION.LATE.INT.FINAL` | `FsGiPeEventDetails_CompensationLateIntFinal` |  |  |  |
| 27 | `FS.GI.PE.EVENT.DETAILS.CALLED.OR.DISTRIBUTED.AMOUNT` | `FsGiPeEventDetails_CalledOrDistributedAmount` |  |  |  |
| 28 | `FS.GI.PE.EVENT.DETAILS.QUANTITY` | `FsGiPeEventDetails_Quantity` |  |  |  |
| 29 | `FS.GI.PE.EVENT.DETAILS.DEAL.REFERENCE` | `FsGiPeEventDetails_DealReference` |  |  |  |
| 30 | `FS.GI.PE.EVENT.DETAILS.LEG.LINK` | `FsGiPeEventDetails_LegLink` |  |  |  |
| 31 | `FS.GI.PE.EVENT.DETAILS.ADJUSTMENT.FLAG` | `FsGiPeEventDetails_AdjustmentFlag` |  |  |  |
| 32 | `FS.GI.PE.EVENT.DETAILS.SEQUENCE.NUMBER` | `FsGiPeEventDetails_SequenceNumber` |  |  |  |
| 33 | `FS.GI.PE.EVENT.DETAILS.RESERVED10` | `FsGiPeEventDetails_Reserved10` |  |  |  |
| 34 | `FS.GI.PE.EVENT.DETAILS.RESERVED9` | `FsGiPeEventDetails_Reserved9` |  |  |  |
| 35 | `FS.GI.PE.EVENT.DETAILS.RESERVED8` | `FsGiPeEventDetails_Reserved8` |  |  |  |
| 36 | `FS.GI.PE.EVENT.DETAILS.RESERVED7` | `FsGiPeEventDetails_Reserved7` |  |  |  |
| 37 | `FS.GI.PE.EVENT.DETAILS.RESERVED6` | `FsGiPeEventDetails_Reserved6` |  |  |  |
| 38 | `FS.GI.PE.EVENT.DETAILS.RESERVED5` | `FsGiPeEventDetails_Reserved5` |  |  |  |
| 39 | `FS.GI.PE.EVENT.DETAILS.RESERVED4` | `FsGiPeEventDetails_Reserved4` |  |  |  |
| 40 | `FS.GI.PE.EVENT.DETAILS.RESERVED3` | `FsGiPeEventDetails_Reserved3` |  |  |  |
| 41 | `FS.GI.PE.EVENT.DETAILS.RESERVED2` | `FsGiPeEventDetails_Reserved2` |  |  |  |
| 42 | `FS.GI.PE.EVENT.DETAILS.RESERVED1` | `FsGiPeEventDetails_Reserved1` |  |  |  |
| 43 | `FS.GI.PE.EVENT.DETAILS.LOCAL.REF` | `FsGiPeEventDetails_LocalRef` |  |  |  |
| 44 | `FS.GI.PE.EVENT.DETAILS.OVERRIDE` | `FsGiPeEventDetails_Override` |  |  |  |
| 45 | `FS.GI.PE.EVENT.DETAILS.RECORD.STATUS` | `FsGiPeEventDetails_RecordStatus` |  |  |  |
| 46 | `FS.GI.PE.EVENT.DETAILS.CURR.NO` | `FsGiPeEventDetails_CurrNo` |  |  |  |
| 47 | `FS.GI.PE.EVENT.DETAILS.INPUTTER` | `FsGiPeEventDetails_Inputter` |  |  |  |
| 48 | `FS.GI.PE.EVENT.DETAILS.DATE.TIME` | `FsGiPeEventDetails_DateTime` |  |  |  |
| 49 | `FS.GI.PE.EVENT.DETAILS.AUTHORISER` | `FsGiPeEventDetails_Authoriser` |  |  |  |
| 50 | `FS.GI.PE.EVENT.DETAILS.CO.CODE` | `FsGiPeEventDetails_CoCode` |  |  |  |
| 51 | `FS.GI.PE.EVENT.DETAILS.DEPT.CODE` | `FsGiPeEventDetails_DeptCode` |  |  |  |
| 52 | `FS.GI.PE.EVENT.DETAILS.AUDITOR.CODE` | `FsGiPeEventDetails_AuditorCode` |  |  |  |
| 53 | `FS.GI.PE.EVENT.DETAILS.AUDIT.DATE.TIME` | `FsGiPeEventDetails_AuditDateTime` |  |  |  |
