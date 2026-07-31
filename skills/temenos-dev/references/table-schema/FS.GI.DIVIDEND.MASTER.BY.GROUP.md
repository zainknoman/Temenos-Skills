# FS.GI.DIVIDEND.MASTER.BY.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.MASTER.BY.GROUP` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIV.MAST.GRP.GROUP.ID` | `FsGiDividendMasterByGroup_GroupId` |  |  |  |
| 2 | `GI.DIV.MAST.GRP.SEQUENCE.NUMBER` | `FsGiDividendMasterByGroup_SequenceNumber` |  |  |  |
| 3 | `GI.DIV.MAST.GRP.STATUS` | `FsGiDividendMasterByGroup_Status` |  |  |  |
| 4 | `GI.DIV.MAST.GRP.DIVIDEND.QUOT.CCY.FLAG` | `FsGiDividendMasterByGroup_DividendQuotCcyFlag` |  |  |  |
| 5 | `GI.DIV.MAST.GRP.INTERNAL.CASH.FLAG` | `FsGiDividendMasterByGroup_InternalCashFlag` |  |  |  |
| 6 | `GI.DIV.MAST.GRP.EXTERNAL.CASH.FLAG` | `FsGiDividendMasterByGroup_ExternalCashFlag` |  |  |  |
| 7 | `GI.DIV.MAST.GRP.DEEMED.DISTRIBUTION.FLAG` | `FsGiDividendMasterByGroup_DeemedDistributionFlag` |  |  |  |
| 8 | `GI.DIV.MAST.GRP.GROUP.UPDATE.ONLY` | `FsGiDividendMasterByGroup_GroupUpdateOnly` |  |  |  |
| 9 | `GI.DIV.MAST.GRP.AUTOMATIC.MASTER.CREATION` | `FsGiDividendMasterByGroup_AutomaticMasterCreation` |  |  |  |
| 10 | `GI.DIV.MAST.GRP.FUND.ID` | `FsGiDividendMasterByGroup_FundId` |  |  |  |
| 11 | `GI.DIV.MAST.GRP.SHARE.CLASS.CODE` | `FsGiDividendMasterByGroup_ShareClassCode` |  |  |  |
| 12 | `GI.DIV.MAST.GRP.DIVIDEND.RATE.PER.SHARE` | `FsGiDividendMasterByGroup_DividendRatePerShare` |  |  |  |
| 13 | `GI.DIV.MAST.GRP.TISD` | `FsGiDividendMasterByGroup_Tisd` |  |  |  |
| 14 | `GI.DIV.MAST.GRP.RECORD.DATE` | `FsGiDividendMasterByGroup_RecordDate` |  |  |  |
| 15 | `GI.DIV.MAST.GRP.EXECUTION.DATE` | `FsGiDividendMasterByGroup_ExecutionDate` |  |  |  |
| 16 | `GI.DIV.MAST.GRP.SETTLEMENT.DATE` | `FsGiDividendMasterByGroup_SettlementDate` |  |  |  |
| 17 | `GI.DIV.MAST.GRP.REINVESTMENT.TRADE.DATE` | `FsGiDividendMasterByGroup_ReinvestmentTradeDate` |  |  |  |
| 18 | `GI.DIV.MAST.GRP.REINVESTMENT.VALUE.DATE` | `FsGiDividendMasterByGroup_ReinvestmentValueDate` |  |  |  |
| 19 | `GI.DIV.MAST.GRP.NAV.DATE` | `FsGiDividendMasterByGroup_NavDate` |  |  |  |
| 20 | `GI.DIV.MAST.GRP.AVERAGE.EQUALIZATION.RATE` | `FsGiDividendMasterByGroup_AverageEqualizationRate` |  |  |  |
| 21 | `GI.DIV.MAST.GRP.INCOME.TYPE` | `FsGiDividendMasterByGroup_IncomeType` |  |  |  |
| 22 | `GI.DIV.MAST.GRP.DISTRIBUTION.TYPE` | `FsGiDividendMasterByGroup_DistributionType` |  |  |  |
| 23 | `GI.DIV.MAST.GRP.PAYABLE.DATE` | `FsGiDividendMasterByGroup_PayableDate` |  |  |  |
| 24 | `GI.DIV.MAST.GRP.FRANKED.INCOME.PERCENTAGE` | `FsGiDividendMasterByGroup_FrankedIncomePercentage` |  |  |  |
| 25 | `GI.DIV.MAST.GRP.UNFRANKED.NON.FOREIGN.INCOME` | `FsGiDividendMasterByGroup_UnfrankedNonForeignIncome` |  |  |  |
| 26 | `GI.DIV.MAST.GRP.UNFRANKED.FOREIGN.INCOME` | `FsGiDividendMasterByGroup_UnfrankedForeignIncome` |  |  |  |
| 27 | `GI.DIV.MAST.GRP.CORPORATION.TAX.AMOUNT` | `FsGiDividendMasterByGroup_CorporationTaxAmount` |  |  |  |
| 28 | `GI.DIV.MAST.GRP.CORPORATION.TAX.RATE` | `FsGiDividendMasterByGroup_CorporationTaxRate` |  |  |  |
| 29 | `GI.DIV.MAST.GRP.LEGAL.ENTITY.ID` | `FsGiDividendMasterByGroup_LegalEntityId` |  |  |  |
| 30 | `GI.DIV.MAST.GRP.ACTION` | `FsGiDividendMasterByGroup_Action` |  |  |  |
| 31 | `GI.DIV.MAST.GRP.TEMPLATE.ID` | `FsGiDividendMasterByGroup_TemplateId` |  |  |  |
| 32 | `GI.DIV.MAST.GRP.BATCH.STATUS` | `FsGiDividendMasterByGroup_BatchStatus` |  |  |  |
| 33 | `GI.DIV.MAST.GRP.PAYMENT.STATUS` | `FsGiDividendMasterByGroup_PaymentStatus` |  |  |  |
| 34 | `GI.DIV.MAST.GRP.SHARE.STATUS` | `FsGiDividendMasterByGroup_ShareStatus` |  |  |  |
| 35 | `GI.DIV.MAST.GRP.SHARE.PAYMENT.STATUS` | `FsGiDividendMasterByGroup_SharePaymentStatus` |  |  |  |
| 36 | `GI.DIV.MAST.GRP.CANCELLED.DIVIDEND.FLAG` | `FsGiDividendMasterByGroup_CancelledDividendFlag` |  |  |  |
| 37 | `GI.DIV.MAST.GRP.VALIDATED.DATE` | `FsGiDividendMasterByGroup_ValidatedDate` |  |  |  |
| 38 | `GI.DIV.MAST.GRP.MAKER.INFO` | `FsGiDividendMasterByGroup_MakerInfo` |  |  |  |
| 39 | `GI.DIV.MAST.GRP.TOTAL.GROSS.DIVIDEND.AMOUNT` | `FsGiDividendMasterByGroup_TotalGrossDividendAmount` |  |  |  |
| 40 | `GI.DIV.MAST.GRP.TOTAL.GROSS.DIV.ROUNDING.DIFF` | `FsGiDividendMasterByGroup_TotalGrossDivRoundingDiff` |  |  |  |
| 41 | `GI.DIV.MAST.GRP.TOTAL.NET.DIVIDEND.AMOUNT` | `FsGiDividendMasterByGroup_TotalNetDividendAmount` |  |  |  |
| 42 | `GI.DIV.MAST.GRP.TOTAL.DIVIDEND.TAX.AMOUNT` | `FsGiDividendMasterByGroup_TotalDividendTaxAmount` |  |  |  |
| 43 | `GI.DIV.MAST.GRP.TOTAL.GROSS.DIV.PAYMENT.AMT` | `FsGiDividendMasterByGroup_TotalGrossDivPaymentAmt` |  |  |  |
| 44 | `GI.DIV.MAST.GRP.TOTAL.NET.DIV.PAYMENT.AMT` | `FsGiDividendMasterByGroup_TotalNetDivPaymentAmt` |  |  |  |
| 45 | `GI.DIV.MAST.GRP.PAYMENT.CURRENCY` | `FsGiDividendMasterByGroup_PaymentCurrency` |  |  |  |
| 46 | `GI.DIV.MAST.GRP.BATCH.MESSAGE` | `FsGiDividendMasterByGroup_BatchMessage` |  |  |  |
| 47 | `GI.DIV.MAST.GRP.GROUP.UPDATE.DUMMY.FLAG` | `FsGiDividendMasterByGroup_GroupUpdateDummyFlag` |  |  |  |
| 48 | `GI.DIV.MAST.GRP.RESERVED10` | `FsGiDividendMasterByGroup_Reserved10` |  |  |  |
| 49 | `GI.DIV.MAST.GRP.RESERVED9` | `FsGiDividendMasterByGroup_Reserved9` |  |  |  |
| 50 | `GI.DIV.MAST.GRP.RESERVED8` | `FsGiDividendMasterByGroup_Reserved8` |  |  |  |
| 51 | `GI.DIV.MAST.GRP.RESERVED7` | `FsGiDividendMasterByGroup_Reserved7` |  |  |  |
| 52 | `GI.DIV.MAST.GRP.RESERVED6` | `FsGiDividendMasterByGroup_Reserved6` |  |  |  |
| 53 | `GI.DIV.MAST.GRP.RESERVED5` | `FsGiDividendMasterByGroup_Reserved5` |  |  |  |
| 54 | `GI.DIV.MAST.GRP.RESERVED4` | `FsGiDividendMasterByGroup_Reserved4` |  |  |  |
| 55 | `GI.DIV.MAST.GRP.RESERVED3` | `FsGiDividendMasterByGroup_Reserved3` |  |  |  |
| 56 | `GI.DIV.MAST.GRP.RESERVED2` | `FsGiDividendMasterByGroup_Reserved2` |  |  |  |
| 57 | `GI.DIV.MAST.GRP.RESERVED1` | `FsGiDividendMasterByGroup_Reserved1` |  |  |  |
| 58 | `GI.DIV.MAST.GRP.LOCAL.REF` | `FsGiDividendMasterByGroup_LocalRef` |  |  |  |
| 59 | `GI.DIV.MAST.GRP.OVERRIDE` | `FsGiDividendMasterByGroup_Override` |  |  |  |
| 60 | `GI.DIV.MAST.GRP.RECORD.STATUS` | `FsGiDividendMasterByGroup_RecordStatus` |  |  |  |
| 61 | `GI.DIV.MAST.GRP.CURR.NO` | `FsGiDividendMasterByGroup_CurrNo` |  |  |  |
| 62 | `GI.DIV.MAST.GRP.INPUTTER` | `FsGiDividendMasterByGroup_Inputter` |  |  |  |
| 63 | `GI.DIV.MAST.GRP.DATE.TIME` | `FsGiDividendMasterByGroup_DateTime` |  |  |  |
| 64 | `GI.DIV.MAST.GRP.AUTHORISER` | `FsGiDividendMasterByGroup_Authoriser` |  |  |  |
| 65 | `GI.DIV.MAST.GRP.CO.CODE` | `FsGiDividendMasterByGroup_CoCode` |  |  |  |
| 66 | `GI.DIV.MAST.GRP.DEPT.CODE` | `FsGiDividendMasterByGroup_DeptCode` |  |  |  |
| 67 | `GI.DIV.MAST.GRP.AUDITOR.CODE` | `FsGiDividendMasterByGroup_AuditorCode` |  |  |  |
| 68 | `GI.DIV.MAST.GRP.AUDIT.DATE.TIME` | `FsGiDividendMasterByGroup_AuditDateTime` |  |  |  |
