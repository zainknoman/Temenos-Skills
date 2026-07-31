# FS.GI.CONTRACT.PF.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GI.CONTRACT.PF.LINK` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.CONTRACT.PF.LINK.PARENT.REF.ID` | `FsGiContractPfLink_ParentRefId` |  |  |  |
| 2 | `FS.GI.CONTRACT.PF.LINK.ORA.ROWID` | `FsGiContractPfLink_OraRowid` |  |  |  |
| 3 | `FS.GI.CONTRACT.PF.LINK.CONTACT.LINKED` | `FsGiContractPfLink_ContactLinked` |  |  |  |
| 4 | `FS.GI.CONTRACT.PF.LINK.DEAL.REFERENCE` | `FsGiContractPfLink_DealReference` |  |  |  |
| 5 | `FS.GI.CONTRACT.PF.LINK.QUANTITY.USED` | `FsGiContractPfLink_QuantityUsed` |  |  |  |
| 6 | `FS.GI.CONTRACT.PF.LINK.LEG.LINK` | `FsGiContractPfLink_LegLink` |  |  |  |
| 7 | `FS.GI.CONTRACT.PF.LINK.REGISTER.ID` | `FsGiContractPfLink_RegisterId` |  |  |  |
| 8 | `FS.GI.CONTRACT.PF.LINK.LEGAL.ENTITY.ID` | `FsGiContractPfLink_LegalEntityId` |  |  |  |
| 9 | `FS.GI.CONTRACT.PF.LINK.FUND.ID` | `FsGiContractPfLink_FundId` |  |  |  |
| 10 | `FS.GI.CONTRACT.PF.LINK.SHARE.CLASS.CODE` | `FsGiContractPfLink_ShareClassCode` |  |  |  |
| 11 | `FS.GI.CONTRACT.PF.LINK.CONTRACT.ID` | `FsGiContractPfLink_ContractId` |  |  |  |
| 12 | `FS.GI.CONTRACT.PF.LINK.ORDER.ID` | `FsGiContractPfLink_OrderId` |  |  |  |
| 13 | `FS.GI.CONTRACT.PF.LINK.TRADE.DATE` | `FsGiContractPfLink_TradeDate` |  |  |  |
| 14 | `FS.GI.CONTRACT.PF.LINK.QUANTITY.LEFT` | `FsGiContractPfLink_QuantityLeft` |  |  |  |
| 15 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.CREDIT.LEFT` | `FsGiContractPfLink_EqualisationCreditLeft` |  |  |  |
| 16 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.DEBIT.LEFT` | `FsGiContractPfLink_EqualisationDebitLeft` |  |  |  |
| 17 | `FS.GI.CONTRACT.PF.LINK.REFUNDABLE.EQUALISATION.CR` | `FsGiContractPfLink_RefundableEqualisationCr` |  |  |  |
| 18 | `FS.GI.CONTRACT.PF.LINK.REFUNDABLE.EQUALISATION.DB` | `FsGiContractPfLink_RefundableEqualisationDb` |  |  |  |
| 19 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.CREDIT.USED` | `FsGiContractPfLink_EqualisationCreditUsed` |  |  |  |
| 20 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.DEBIT.USED` | `FsGiContractPfLink_EqualisationDebitUsed` |  |  |  |
| 21 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.CREDIT.LOST` | `FsGiContractPfLink_EqualisationCreditLost` |  |  |  |
| 22 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.DEBIT.LOST` | `FsGiContractPfLink_EqualisationDebitLost` |  |  |  |
| 23 | `FS.GI.CONTRACT.PF.LINK.TOTAL.PERFORMANCE.FEE` | `FsGiContractPfLink_TotalPerformanceFee` |  |  |  |
| 24 | `FS.GI.CONTRACT.PF.LINK.STATUS` | `FsGiContractPfLink_Status` |  |  |  |
| 25 | `FS.GI.CONTRACT.PF.LINK.EQ.DEBIT.FOR.CREDIT` | `FsGiContractPfLink_EqDebitForCredit` |  |  |  |
| 26 | `FS.GI.CONTRACT.PF.LINK.EQ.DEBIT.NOT.DEDUCTED` | `FsGiContractPfLink_EqDebitNotDeducted` |  |  |  |
| 27 | `FS.GI.CONTRACT.PF.LINK.TRANSFER.HISORICAL` | `FsGiContractPfLink_TransferHisorical` |  |  |  |
| 28 | `FS.GI.CONTRACT.PF.LINK.TRANSFER.OUT.REGISTER` | `FsGiContractPfLink_TransferOutRegister` |  |  |  |
| 29 | `FS.GI.CONTRACT.PF.LINK.REVISED.CUMUL.REL.PERF` | `FsGiContractPfLink_RevisedCumulRelPerf` |  |  |  |
| 30 | `FS.GI.CONTRACT.PF.LINK.REVISED.HWM` | `FsGiContractPfLink_RevisedHwm` |  |  |  |
| 31 | `FS.GI.CONTRACT.PF.LINK.REVISED.GAV` | `FsGiContractPfLink_RevisedGav` |  |  |  |
| 32 | `FS.GI.CONTRACT.PF.LINK.EQUALISATION.USED.FLAG` | `FsGiContractPfLink_EqualisationUsedFlag` |  |  |  |
| 33 | `FS.GI.CONTRACT.PF.LINK.DB.CR` | `FsGiContractPfLink_DbCr` |  |  |  |
| 34 | `FS.GI.CONTRACT.PF.LINK.SEQUENCE.NUMBER` | `FsGiContractPfLink_SequenceNumber` |  |  |  |
| 35 | `FS.GI.CONTRACT.PF.LINK.UNRESET.REF.NAV` | `FsGiContractPfLink_UnresetRefNav` |  |  |  |
| 36 | `FS.GI.CONTRACT.PF.LINK.UNRESET.CUMUL.REL.PERF` | `FsGiContractPfLink_UnresetCumulRelPerf` |  |  |  |
| 37 | `FS.GI.CONTRACT.PF.LINK.TRANSFER.CONTRACT` | `FsGiContractPfLink_TransferContract` |  |  |  |
| 38 | `FS.GI.CONTRACT.PF.LINK.TRANSFER.AGENT` | `FsGiContractPfLink_TransferAgent` |  |  |  |
| 39 | `FS.GI.CONTRACT.PF.LINK.TRANSFER.ORDER` | `FsGiContractPfLink_TransferOrder` |  |  |  |
| 40 | `FS.GI.CONTRACT.PF.LINK.ORIGINAL.TRANSFER.HISTO` | `FsGiContractPfLink_OriginalTransferHisto` |  |  |  |
| 41 | `FS.GI.CONTRACT.PF.LINK.REFERENCE.NAV` | `FsGiContractPfLink_ReferenceNav` |  |  |  |
| 42 | `FS.GI.CONTRACT.PF.LINK.GAV.USED` | `FsGiContractPfLink_GavUsed` |  |  |  |
| 43 | `FS.GI.CONTRACT.PF.LINK.CRP.USED` | `FsGiContractPfLink_CrpUsed` |  |  |  |
| 44 | `FS.GI.CONTRACT.PF.LINK.ORIGINAL.CONTRACT.ID` | `FsGiContractPfLink_OriginalContractId` |  |  |  |
| 45 | `FS.GI.CONTRACT.PF.LINK.ORIGINAL.AGENT.ID` | `FsGiContractPfLink_OriginalAgentId` |  |  |  |
| 46 | `FS.GI.CONTRACT.PF.LINK.ORIGINAL.REGISTER.ID` | `FsGiContractPfLink_OriginalRegisterId` |  |  |  |
| 47 | `FS.GI.CONTRACT.PF.LINK.ORIGINAL.ORDER.ID` | `FsGiContractPfLink_OriginalOrderId` |  |  |  |
| 48 | `FS.GI.CONTRACT.PF.LINK.REVISED.CUMUL.REL.PERF.DATE` | `FsGiContractPfLink_RevisedCumulRelPerfDate` |  |  |  |
| 49 | `FS.GI.CONTRACT.PF.LINK.RESERVED10` | `FsGiContractPfLink_Reserved10` |  |  |  |
| 50 | `FS.GI.CONTRACT.PF.LINK.RESERVED9` | `FsGiContractPfLink_Reserved9` |  |  |  |
| 51 | `FS.GI.CONTRACT.PF.LINK.RESERVED8` | `FsGiContractPfLink_Reserved8` |  |  |  |
| 52 | `FS.GI.CONTRACT.PF.LINK.RESERVED7` | `FsGiContractPfLink_Reserved7` |  |  |  |
| 53 | `FS.GI.CONTRACT.PF.LINK.RESERVED6` | `FsGiContractPfLink_Reserved6` |  |  |  |
| 54 | `FS.GI.CONTRACT.PF.LINK.RESERVED5` | `FsGiContractPfLink_Reserved5` |  |  |  |
| 55 | `FS.GI.CONTRACT.PF.LINK.RESERVED4` | `FsGiContractPfLink_Reserved4` |  |  |  |
| 56 | `FS.GI.CONTRACT.PF.LINK.RESERVED3` | `FsGiContractPfLink_Reserved3` |  |  |  |
| 57 | `FS.GI.CONTRACT.PF.LINK.RESERVED2` | `FsGiContractPfLink_Reserved2` |  |  |  |
| 58 | `FS.GI.CONTRACT.PF.LINK.RESERVED1` | `FsGiContractPfLink_Reserved1` |  |  |  |
| 59 | `FS.GI.CONTRACT.PF.LINK.LOCAL.REF` | `FsGiContractPfLink_LocalRef` |  |  |  |
| 60 | `FS.GI.CONTRACT.PF.LINK.OVERRIDE` | `FsGiContractPfLink_Override` |  |  |  |
| 61 | `FS.GI.CONTRACT.PF.LINK.RECORD.STATUS` | `FsGiContractPfLink_RecordStatus` |  |  |  |
| 62 | `FS.GI.CONTRACT.PF.LINK.CURR.NO` | `FsGiContractPfLink_CurrNo` |  |  |  |
| 63 | `FS.GI.CONTRACT.PF.LINK.INPUTTER` | `FsGiContractPfLink_Inputter` |  |  |  |
| 64 | `FS.GI.CONTRACT.PF.LINK.DATE.TIME` | `FsGiContractPfLink_DateTime` |  |  |  |
| 65 | `FS.GI.CONTRACT.PF.LINK.AUTHORISER` | `FsGiContractPfLink_Authoriser` |  |  |  |
| 66 | `FS.GI.CONTRACT.PF.LINK.CO.CODE` | `FsGiContractPfLink_CoCode` |  |  |  |
| 67 | `FS.GI.CONTRACT.PF.LINK.DEPT.CODE` | `FsGiContractPfLink_DeptCode` |  |  |  |
| 68 | `FS.GI.CONTRACT.PF.LINK.AUDITOR.CODE` | `FsGiContractPfLink_AuditorCode` |  |  |  |
| 69 | `FS.GI.CONTRACT.PF.LINK.AUDIT.DATE.TIME` | `FsGiContractPfLink_AuditDateTime` |  |  |  |
