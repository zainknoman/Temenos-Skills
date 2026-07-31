# FS.GI.PE.EVENT.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.EVENT.MASTER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PE.EVENT.MASTER.EVENT.ID` | `FsGiPeEventMaster_EventId` |  |  |  |
| 2 | `GI.PE.EVENT.MASTER.FUND.ID` | `FsGiPeEventMaster_FundId` |  |  |  |
| 3 | `GI.PE.EVENT.MASTER.SHARE.CLASS.CODE` | `FsGiPeEventMaster_ShareClassCode` |  |  |  |
| 4 | `GI.PE.EVENT.MASTER.TRANCHE` | `FsGiPeEventMaster_Tranche` |  |  |  |
| 5 | `GI.PE.EVENT.MASTER.EVENT.DATE` | `FsGiPeEventMaster_EventDate` |  |  |  |
| 6 | `GI.PE.EVENT.MASTER.SETTLEMENT.DATE` | `FsGiPeEventMaster_SettlementDate` |  |  |  |
| 7 | `GI.PE.EVENT.MASTER.AMOUNT` | `FsGiPeEventMaster_Amount` |  |  |  |
| 8 | `GI.PE.EVENT.MASTER.CALL.PERCENTAGE` | `FsGiPeEventMaster_CallPercentage` |  |  |  |
| 9 | `GI.PE.EVENT.MASTER.STATUS` | `FsGiPeEventMaster_Status` |  |  |  |
| 10 | `GI.PE.EVENT.MASTER.STRUCTURING.FEES.AMT` | `FsGiPeEventMaster_StructuringFeesAmt` |  |  |  |
| 11 | `GI.PE.EVENT.MASTER.STRUCTURING.FEES.PERCENTAGE` | `FsGiPeEventMaster_StructuringFeesPercentage` |  |  |  |
| 12 | `GI.PE.EVENT.MASTER.STRUCTURING.FEES.IMPACT.SHARES` | `FsGiPeEventMaster_StructuringFeesImpactShares` |  |  |  |
| 13 | `GI.PE.EVENT.MASTER.PRICE` | `FsGiPeEventMaster_Price` |  |  |  |
| 14 | `GI.PE.EVENT.MASTER.PRICE.PAID.UP` | `FsGiPeEventMaster_PricePaidUp` |  |  |  |
| 15 | `GI.PE.EVENT.MASTER.SEQUENCE.NUMBER` | `FsGiPeEventMaster_SequenceNumber` |  |  |  |
| 16 | `GI.PE.EVENT.MASTER.FEE.AMOUNT` | `FsGiPeEventMaster_FeeAmount` |  |  |  |
| 17 | `GI.PE.EVENT.MASTER.INSIDE.OUTSIDE.COMMITMENT` | `FsGiPeEventMaster_InsideOutsideCommitment` |  |  |  |
| 18 | `GI.PE.EVENT.MASTER.IMPACT.SHARES` | `FsGiPeEventMaster_ImpactShares` |  |  |  |
| 19 | `GI.PE.EVENT.MASTER.MESSAGE` | `FsGiPeEventMaster_Message` |  |  |  |
| 20 | `GI.PE.EVENT.MASTER.LINKED.SEQUENCE` | `FsGiPeEventMaster_LinkedSequence` |  |  |  |
| 21 | `GI.PE.EVENT.MASTER.PE.RE.COMMENT` | `FsGiPeEventMaster_PeReComment` |  |  |  |
| 22 | `GI.PE.EVENT.MASTER.GROUP.ID` | `FsGiPeEventMaster_GroupId` |  |  |  |
| 23 | `GI.PE.EVENT.MASTER.FULL.REDEMPTION.FLAG` | `FsGiPeEventMaster_FullRedemptionFlag` |  |  |  |
| 24 | `GI.PE.EVENT.MASTER.LAST.CAPITAL.CALL.FLAG` | `FsGiPeEventMaster_LastCapitalCallFlag` |  |  |  |
| 25 | `GI.PE.EVENT.MASTER.FULL.STRUCTURING.FEES.FLAG` | `FsGiPeEventMaster_FullStructuringFeesFlag` |  |  |  |
| 26 | `GI.PE.EVENT.MASTER.LATE.INT.TRUE.UP.NATURE.FLAG` | `FsGiPeEventMaster_LateIntTrueUpNatureFlag` |  |  |  |
| 27 | `GI.PE.EVENT.MASTER.LATE.INT.BEN.EXIST.INVEST.FLAG` | `FsGiPeEventMaster_LateIntBenExistInvestFlag` |  |  |  |
| 28 | `GI.PE.EVENT.MASTER.LATE.INT.BEN.FUND.FLAG` | `FsGiPeEventMaster_LateIntBenFundFlag` |  |  |  |
| 29 | `GI.PE.EVENT.MASTER.RESERVED10` | `FsGiPeEventMaster_Reserved10` |  |  |  |
| 30 | `GI.PE.EVENT.MASTER.RESERVED9` | `FsGiPeEventMaster_Reserved9` |  |  |  |
| 31 | `GI.PE.EVENT.MASTER.RESERVED8` | `FsGiPeEventMaster_Reserved8` |  |  |  |
| 32 | `GI.PE.EVENT.MASTER.RESERVED7` | `FsGiPeEventMaster_Reserved7` |  |  |  |
| 33 | `GI.PE.EVENT.MASTER.RESERVED6` | `FsGiPeEventMaster_Reserved6` |  |  |  |
| 34 | `GI.PE.EVENT.MASTER.RESERVED5` | `FsGiPeEventMaster_Reserved5` |  |  |  |
| 35 | `GI.PE.EVENT.MASTER.RESERVED4` | `FsGiPeEventMaster_Reserved4` |  |  |  |
| 36 | `GI.PE.EVENT.MASTER.RESERVED3` | `FsGiPeEventMaster_Reserved3` |  |  |  |
| 37 | `GI.PE.EVENT.MASTER.RESERVED2` | `FsGiPeEventMaster_Reserved2` |  |  |  |
| 38 | `GI.PE.EVENT.MASTER.RESERVED1` | `FsGiPeEventMaster_Reserved1` |  |  |  |
| 39 | `GI.PE.EVENT.MASTER.LOCAL.REF` | `FsGiPeEventMaster_LocalRef` |  |  |  |
| 40 | `GI.PE.EVENT.MASTER.OVERRIDE` | `FsGiPeEventMaster_Override` |  |  |  |
| 41 | `GI.PE.EVENT.MASTER.RECORD.STATUS` | `FsGiPeEventMaster_RecordStatus` |  |  |  |
| 42 | `GI.PE.EVENT.MASTER.CURR.NO` | `FsGiPeEventMaster_CurrNo` |  |  |  |
| 43 | `GI.PE.EVENT.MASTER.INPUTTER` | `FsGiPeEventMaster_Inputter` |  |  |  |
| 44 | `GI.PE.EVENT.MASTER.DATE.TIME` | `FsGiPeEventMaster_DateTime` |  |  |  |
| 45 | `GI.PE.EVENT.MASTER.AUTHORISER` | `FsGiPeEventMaster_Authoriser` |  |  |  |
| 46 | `GI.PE.EVENT.MASTER.CO.CODE` | `FsGiPeEventMaster_CoCode` |  |  |  |
| 47 | `GI.PE.EVENT.MASTER.DEPT.CODE` | `FsGiPeEventMaster_DeptCode` |  |  |  |
| 48 | `GI.PE.EVENT.MASTER.AUDITOR.CODE` | `FsGiPeEventMaster_AuditorCode` |  |  |  |
| 49 | `GI.PE.EVENT.MASTER.AUDIT.DATE.TIME` | `FsGiPeEventMaster_AuditDateTime` |  |  |  |
