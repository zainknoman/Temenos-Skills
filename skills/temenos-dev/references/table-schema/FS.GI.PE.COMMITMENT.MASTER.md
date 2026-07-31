# FS.GI.PE.COMMITMENT.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.PE.COMMITMENT.MASTER` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.PE.COMMITMENT.MASTER.REGISTER.ID` | `FsGiPeCommitmentMaster_RegisterId` |  |  |  |
| 2 | `GI.PE.COMMITMENT.MASTER.STATUS` | `FsGiPeCommitmentMaster_Status` |  |  |  |
| 3 | `GI.PE.COMMITMENT.MASTER.COMMITMENT.ID` | `FsGiPeCommitmentMaster_CommitmentId` |  |  |  |
| 4 | `GI.PE.COMMITMENT.MASTER.TRANCHE` | `FsGiPeCommitmentMaster_Tranche` |  |  |  |
| 5 | `GI.PE.COMMITMENT.MASTER.FUND.ID` | `FsGiPeCommitmentMaster_FundId` |  |  |  |
| 6 | `GI.PE.COMMITMENT.MASTER.LEGAL.ENTITY.ID` | `FsGiPeCommitmentMaster_LegalEntityId` |  |  |  |
| 7 | `GI.PE.COMMITMENT.MASTER.SHARE.CLASS.CODE` | `FsGiPeCommitmentMaster_ShareClassCode` |  |  |  |
| 8 | `GI.PE.COMMITMENT.MASTER.FUND.MASTER.CCY` | `FsGiPeCommitmentMaster_FundMasterCcy` |  |  |  |
| 9 | `GI.PE.COMMITMENT.MASTER.COMMITTED.CAPITAL.AMOUNT` | `FsGiPeCommitmentMaster_CommittedCapitalAmount` |  |  |  |
| 10 | `GI.PE.COMMITMENT.MASTER.UNCALLED.CAPITAL` | `FsGiPeCommitmentMaster_UncalledCapital` |  |  |  |
| 11 | `GI.PE.COMMITMENT.MASTER.RECALLABLE.CAPITAL.AMOUNT` | `FsGiPeCommitmentMaster_RecallableCapitalAmount` |  |  |  |
| 12 | `GI.PE.COMMITMENT.MASTER.COMMITMENT.START.DATE` | `FsGiPeCommitmentMaster_CommitmentStartDate` |  |  |  |
| 13 | `GI.PE.COMMITMENT.MASTER.COMMITMENT.END.DATE` | `FsGiPeCommitmentMaster_CommitmentEndDate` |  |  |  |
| 14 | `GI.PE.COMMITMENT.MASTER.FREE.TEXT` | `FsGiPeCommitmentMaster_FreeText` |  |  |  |
| 15 | `GI.PE.COMMITMENT.MASTER.CANCEL.DATE` | `FsGiPeCommitmentMaster_CancelDate` |  |  |  |
| 16 | `GI.PE.COMMITMENT.MASTER.TRANSFER.FLAG` | `FsGiPeCommitmentMaster_TransferFlag` |  |  |  |
| 17 | `GI.PE.COMMITMENT.MASTER.IN.REGISTER.ID` | `FsGiPeCommitmentMaster_InRegisterId` |  |  |  |
| 18 | `GI.PE.COMMITMENT.MASTER.ADJUSTMENT.FLAG` | `FsGiPeCommitmentMaster_AdjustmentFlag` |  |  |  |
| 19 | `GI.PE.COMMITMENT.MASTER.PREVIOUS.REGISTER.2` | `FsGiPeCommitmentMaster_PreviousRegister2` |  |  |  |
| 20 | `GI.PE.COMMITMENT.MASTER.PREVIOUS.TRANSFER.FLAG` | `FsGiPeCommitmentMaster_PreviousTransferFlag` |  |  |  |
| 21 | `GI.PE.COMMITMENT.MASTER.SWITCH.FLAG` | `FsGiPeCommitmentMaster_SwitchFlag` |  |  |  |
| 22 | `GI.PE.COMMITMENT.MASTER.DEFAULTING.FLAG` | `FsGiPeCommitmentMaster_DefaultingFlag` |  |  |  |
| 23 | `GI.PE.COMMITMENT.MASTER.PREFERENTIAL.FLAG` | `FsGiPeCommitmentMaster_PreferentialFlag` |  |  |  |
| 24 | `GI.PE.COMMITMENT.MASTER.SWITCH.DATE` | `FsGiPeCommitmentMaster_SwitchDate` |  |  |  |
| 25 | `GI.PE.COMMITMENT.MASTER.IN.FUND.ID` | `FsGiPeCommitmentMaster_InFundId` |  |  |  |
| 26 | `GI.PE.COMMITMENT.MASTER.IN.SHARE.CLASS` | `FsGiPeCommitmentMaster_InShareClass` |  |  |  |
| 27 | `GI.PE.COMMITMENT.MASTER.SWITCH.OUT.PRICE` | `FsGiPeCommitmentMaster_SwitchOutPrice` |  |  |  |
| 28 | `GI.PE.COMMITMENT.MASTER.SWITCH.IN.PRICE` | `FsGiPeCommitmentMaster_SwitchInPrice` |  |  |  |
| 29 | `GI.PE.COMMITMENT.MASTER.TRANCHE.2` | `FsGiPeCommitmentMaster_Tranche2` |  |  |  |
| 30 | `GI.PE.COMMITMENT.MASTER.TRANSFER.PERCENTAGE` | `FsGiPeCommitmentMaster_TransferPercentage` |  |  |  |
| 31 | `GI.PE.COMMITMENT.MASTER.TRANSFER.QUANTITY` | `FsGiPeCommitmentMaster_TransferQuantity` |  |  |  |
| 32 | `GI.PE.COMMITMENT.MASTER.TRANSFER.DATE` | `FsGiPeCommitmentMaster_TransferDate` |  |  |  |
| 33 | `GI.PE.COMMITMENT.MASTER.TRANSFER.PRICE` | `FsGiPeCommitmentMaster_TransferPrice` |  |  |  |
| 34 | `GI.PE.COMMITMENT.MASTER.STRUCTURING.FEES.AMT` | `FsGiPeCommitmentMaster_StructuringFeesAmt` |  |  |  |
| 35 | `GI.PE.COMMITMENT.MASTER.STRUCTURING.FEES.AMT.BALANCE` | `FsGiPeCommitmentMaster_StructuringFeesAmtBalance` |  |  |  |
| 36 | `GI.PE.COMMITMENT.MASTER.STRUCTURING.FEES.EXPIRY.DATE` | `FsGiPeCommitmentMaster_StructuringFeesExpiryDate` |  |  |  |
| 37 | `GI.PE.COMMITMENT.MASTER.STRUCTURING.FEES.EXPIRY.FLAG` | `FsGiPeCommitmentMaster_StructuringFeesExpiryFlag` |  |  |  |
| 38 | `GI.PE.COMMITMENT.MASTER.COMMITMENT.EXPIRY.DATE` | `FsGiPeCommitmentMaster_CommitmentExpiryDate` |  |  |  |
| 39 | `GI.PE.COMMITMENT.MASTER.COMMITMENT.EXPIRY.FLAG` | `FsGiPeCommitmentMaster_CommitmentExpiryFlag` |  |  |  |
| 40 | `GI.PE.COMMITMENT.MASTER.STRUCTURING.FEES.EXPIRY.EXE` | `FsGiPeCommitmentMaster_StructuringFeesExpiryExe` |  |  |  |
| 41 | `GI.PE.COMMITMENT.MASTER.EQ.BYPASSED.FLAG` | `FsGiPeCommitmentMaster_EqBypassedFlag` |  |  |  |
| 42 | `GI.PE.COMMITMENT.MASTER.RESERVED10` | `FsGiPeCommitmentMaster_Reserved10` |  |  |  |
| 43 | `GI.PE.COMMITMENT.MASTER.RESERVED9` | `FsGiPeCommitmentMaster_Reserved9` |  |  |  |
| 44 | `GI.PE.COMMITMENT.MASTER.RESERVED8` | `FsGiPeCommitmentMaster_Reserved8` |  |  |  |
| 45 | `GI.PE.COMMITMENT.MASTER.RESERVED7` | `FsGiPeCommitmentMaster_Reserved7` |  |  |  |
| 46 | `GI.PE.COMMITMENT.MASTER.RESERVED6` | `FsGiPeCommitmentMaster_Reserved6` |  |  |  |
| 47 | `GI.PE.COMMITMENT.MASTER.RESERVED5` | `FsGiPeCommitmentMaster_Reserved5` |  |  |  |
| 48 | `GI.PE.COMMITMENT.MASTER.RESERVED4` | `FsGiPeCommitmentMaster_Reserved4` |  |  |  |
| 49 | `GI.PE.COMMITMENT.MASTER.RESERVED3` | `FsGiPeCommitmentMaster_Reserved3` |  |  |  |
| 50 | `GI.PE.COMMITMENT.MASTER.RESERVED2` | `FsGiPeCommitmentMaster_Reserved2` |  |  |  |
| 51 | `GI.PE.COMMITMENT.MASTER.RESERVED1` | `FsGiPeCommitmentMaster_Reserved1` |  |  |  |
| 52 | `GI.PE.COMMITMENT.MASTER.LOCAL.REF` | `FsGiPeCommitmentMaster_LocalRef` |  |  |  |
| 53 | `GI.PE.COMMITMENT.MASTER.OVERRIDE` | `FsGiPeCommitmentMaster_Override` |  |  |  |
| 54 | `GI.PE.COMMITMENT.MASTER.RECORD.STATUS` | `FsGiPeCommitmentMaster_RecordStatus` |  |  |  |
| 55 | `GI.PE.COMMITMENT.MASTER.CURR.NO` | `FsGiPeCommitmentMaster_CurrNo` |  |  |  |
| 56 | `GI.PE.COMMITMENT.MASTER.INPUTTER` | `FsGiPeCommitmentMaster_Inputter` |  |  |  |
| 57 | `GI.PE.COMMITMENT.MASTER.DATE.TIME` | `FsGiPeCommitmentMaster_DateTime` |  |  |  |
| 58 | `GI.PE.COMMITMENT.MASTER.AUTHORISER` | `FsGiPeCommitmentMaster_Authoriser` |  |  |  |
| 59 | `GI.PE.COMMITMENT.MASTER.CO.CODE` | `FsGiPeCommitmentMaster_CoCode` |  |  |  |
| 60 | `GI.PE.COMMITMENT.MASTER.DEPT.CODE` | `FsGiPeCommitmentMaster_DeptCode` |  |  |  |
| 61 | `GI.PE.COMMITMENT.MASTER.AUDITOR.CODE` | `FsGiPeCommitmentMaster_AuditorCode` |  |  |  |
| 62 | `GI.PE.COMMITMENT.MASTER.AUDIT.DATE.TIME` | `FsGiPeCommitmentMaster_AuditDateTime` |  |  |  |
