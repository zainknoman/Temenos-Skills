# CG.TXN.BASE — Table Schema

> Source: `INSERTS/I_F.CG.TXN.BASE` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.TXN.SEC.CURRENCY` | `CgTxnBase_SecCurrency` | TField |  | This field will contain the currency code indicating the security currency as recorded on the underlyingSECURITY.MASTER file. All monetary values in the base record will be expressed in terms of this currency. |
| 2 | `CG.TXN.TRADE.DATE.TIME` | `CgTxnBase_TradeDateTime` |  |  |  |
| 3 | `CG.TXN.SEC.TRANS.ID` | `CgTxnBase_SecTransId` |  |  |  |
| 4 | `CG.TXN.ORIG.SAM` | `CgTxnBase_OrigSam` |  |  |  |
| 5 | `CG.TXN.TXN.TYPE` | `CgTxnBase_TxnType` |  |  |  |
| 6 | `CG.TXN.TRD.NOMINAL` | `CgTxnBase_TrdNominal` |  |  |  |
| 7 | `CG.TXN.TRD.VALUE` | `CgTxnBase_TrdValue` |  |  |  |
| 8 | `CG.TXN.ACCRUED.INT` | `CgTxnBase_AccruedInt` |  |  |  |
| 9 | `CG.TXN.EXPENSES` | `CgTxnBase_Expenses` |  |  |  |
| 10 | `CG.TXN.CG.NOMINAL` | `CgTxnBase_CgNominal` |  |  |  |
| 11 | `CG.TXN.CG.TRD.COST` | `CgTxnBase_CgTrdCost` |  |  |  |
| 12 | `CG.TXN.CG.PL` | `CgTxnBase_CgPl` |  |  |  |
| 13 | `CG.TXN.WHT.PL` | `CgTxnBase_WhtPl` |  |  |  |
| 14 | `CG.TXN.TXN.INDEX` | `CgTxnBase_TxnIndex` |  |  |  |
| 15 | `CG.TXN.PUR.TXN.ID` | `CgTxnBase_PurTxnId` |  |  |  |
| 16 | `CG.TXN.PUR.TXN.NOM` | `CgTxnBase_PurTxnNom` |  |  |  |
| 17 | `CG.TXN.PUR.TX.CG.PL` | `CgTxnBase_PurTxCgPl` |  |  |  |
| 18 | `CG.TXN.PUR.TX.INDEX` | `CgTxnBase_PurTxIndex` |  |  |  |
| 20 | `CG.TXN.PUR.AC.CG.PL` | `CgTxnBase_PurAcCgPl` |  |  |  |
| 21 | `CG.TXN.PUR.TXN.TIME` | `CgTxnBase_PurTxnTime` |  |  |  |
| 22 | `CG.TXN.CG.POSITION` | `CgTxnBase_CgPosition` |  |  |  |
| 23 | `CG.TXN.CG.COST.OF.POSN` | `CgTxnBase_CgCostOfPosn` |  |  |  |
| 24 | `CG.TXN.CG.PL.POSN` | `CgTxnBase_CgPlPosn` |  |  |  |
| 25 | `CG.TXN.WHT.PL.POSN` | `CgTxnBase_WhtPlPosn` |  |  |  |
| 26 | `CG.TXN.CG.ACCRUED.INT` | `CgTxnBase_CgAccruedInt` |  |  |  |
| 27 | `CG.TXN.CG.EXPENSES` | `CgTxnBase_CgExpenses` |  |  |  |
| 28 | `CG.TXN.CG.INT.POSN` | `CgTxnBase_CgIntPosn` |  |  |  |
| 29 | `CG.TXN.CG.EXP.POSN` | `CgTxnBase_CgExpPosn` |  |  |  |
| 30 | `CG.TXN.TAX.STATUS` | `CgTxnBase_TaxStatus` |  |  |  |
| 31 | `CG.TXN.CG.METHOD` | `CgTxnBase_CgMethod` |  |  |  |
| 32 | `CG.TXN.SRC.LCL.CGT` | `CgTxnBase_SrcLclCgt` |  |  |  |
| 33 | `CG.TXN.STMT.NOS` | `CgTxnBase_StmtNos` |  |  |  |
| 34 | `CG.TXN.ORIG.NOMINAL` | `CgTxnBase_OrigNominal` |  |  |  |
| 35 | `CG.TXN.ORIG.VALUE` | `CgTxnBase_OrigValue` |  |  |  |
| 36 | `CG.TXN.TRD.NOMINAL.ADJ` | `CgTxnBase_TrdNominalAdj` |  |  |  |
| 37 | `CG.TXN.CORP.TXN.ID` | `CgTxnBase_CorpTxnId` |  |  |  |
| 38 | `CG.TXN.CORP.TXN.TYPE` | `CgTxnBase_CorpTxnType` |  |  |  |
| 39 | `CG.TXN.CORP.TXN.DATE` | `CgTxnBase_CorpTxnDate` |  |  |  |
| 40 | `CG.TXN.PARAM.CONDITION` | `CgTxnBase_ParamCondition` | TField |  | The CG.PARAM.CONDITION that applies to this transaction base. |
| 41 | `CG.TXN.DATE.TIME.CGUPDT` | `CgTxnBase_DateTimeCgupdt` | TField |  | This field contains the date and time of the last update to the base record. Format will be YYYYMMDDHHMM, where YYYY specifies the year, MM specifies the month, DD specifies the day, HHspecifies the hour and MM specifies the minutes. |
| 42 | `CG.TXN.REVENUE.ASSET` | `CgTxnBase_RevenueAsset` | TField |  | When Revenue Asset is set in CG.INVENTORY.METHOD, then the Capital gain calculated and held in the CG.PL fieldwill be reported as a Revenue income. This field will be flagged as YES if it is a Revenue Asset |
| 43 | `CG.TXN.RESERVED7` | `CgTxnBase_Reserved7` | TField |  |  |
| 44 | `CG.TXN.RESERVED6` | `CgTxnBase_Reserved6` | TField |  |  |
| 45 | `CG.TXN.RESERVED5` | `CgTxnBase_Reserved5` | TField |  |  |
| 46 | `CG.TXN.RESERVED4` | `CgTxnBase_Reserved4` | TField |  |  |
| 47 | `CG.TXN.RESERVED3` | `CgTxnBase_Reserved3` | TField |  |  |
| 48 | `CG.TXN.RESERVED2` | `CgTxnBase_Reserved2` | TField |  |  |
| 49 | `CG.TXN.RESERVED1` | `CgTxnBase_Reserved1` | TField |  |  |
| 50 | `CG.TXN.RECORD.STATUS` | `CgTxnBase_RecordStatus` | String |  |  |
| 51 | `CG.TXN.CURR.NO` | `CgTxnBase_CurrNo` | String |  |  |
| 52 | `CG.TXN.INPUTTER` | `CgTxnBase_Inputter` |  |  |  |
| 53 | `CG.TXN.DATE.TIME` | `CgTxnBase_DateTime` |  |  |  |
| 54 | `CG.TXN.AUTHORISER` | `CgTxnBase_Authoriser` | String |  |  |
| 55 | `CG.TXN.CO.CODE` | `CgTxnBase_CoCode` | String |  |  |
| 56 | `CG.TXN.DEPT.CODE` | `CgTxnBase_DeptCode` | String |  |  |
| 57 | `CG.TXN.AUDITOR.CODE` | `CgTxnBase_AuditorCode` | String |  |  |
| 58 | `CG.TXN.AUDIT.DATE.TIME` | `CgTxnBase_AuditDateTime` | String |  |  |
| 59 | `CG.TXN.TAX.LOT.ID` | `CgTxnBase_TaxLotId` |  |  |  |
| 60 | `CG.TXN.TAX.LOT.STATUS` | `CgTxnBase_TaxLotStatus` |  |  |  |
| 61 | `CG.TXN.COST.PER.UNIT` | `CgTxnBase_CostPerUnit` |  |  |  |
| 62 | `CG.TXN.AVG.COST.PER.UNIT` | `CgTxnBase_AvgCostPerUnit` |  |  |  |
| 63 | `CG.TXN.AVG.COST` | `CgTxnBase_AvgCost` |  |  |  |
| 64 | `CG.TXN.CG.PL.LCY` | `CgTxnBase_CgPlLcy` |  |  |  |
| 65 | `CG.TXN.CG.LCY.EXCH.RATE` | `CgTxnBase_CgLcyExchRate` |  |  |  |
| 66 | `CG.TXN.CG.INVENTORY.METHOD` | `CgTxnBase_CgInventoryMethod` |  |  |  |
| 67 | `CG.TXN.CG.EXEMPT` | `CgTxnBase_CgExempt` |  |  |  |
| 68 | `CG.TXN.PUR.LT.CG.PL` | `CgTxnBase_PurLtCgPl` |  |  |  |
| 69 | `CG.TXN.PUR.ST.CG.PL` | `CgTxnBase_PurStCgPl` |  |  |  |
| 70 | `CG.TXN.CG.LT.PL` | `CgTxnBase_CgLtPl` |  |  |  |
| 71 | `CG.TXN.CG.ST.PL` | `CgTxnBase_CgStPl` |  |  |  |
| 72 | `CG.TXN.CG.LT.PL.LCY` | `CgTxnBase_CgLtPlLcy` |  |  |  |
| 73 | `CG.TXN.CG.ST.PL.LCY` | `CgTxnBase_CgStPlLcy` |  |  |  |
| 74 | `CG.TXN.PUR.LT.CG.INDEXED` | `CgTxnBase_PurLtCgIndexed` |  |  |  |
| 75 | `CG.TXN.PUR.LT.CG.DISCOUNT` | `CgTxnBase_PurLtCgDiscount` |  |  |  |
| 76 | `CG.TXN.PUR.LT.CG.STD` | `CgTxnBase_PurLtCgStd` |  |  |  |
| 77 | `CG.TXN.PUR.ST.CG.INDEXED` | `CgTxnBase_PurStCgIndexed` |  |  |  |
| 78 | `CG.TXN.PUR.ST.CG.DISCOUNT` | `CgTxnBase_PurStCgDiscount` |  |  |  |
| 79 | `CG.TXN.PUR.ST.CG.STD` | `CgTxnBase_PurStCgStd` |  |  |  |
| 80 | `CG.TXN.PUR.CG.PL` | `CgTxnBase_PurCgPl` |  |  |  |
| 81 | `CG.TXN.CORP.INCOME.PL` | `CgTxnBase_CorpIncomePl` |  |  |  |
| 82 | `CG.TXN.POOL.FACTOR` | `CgTxnBase_PoolFactor` |  |  |  |
| 83 | `CG.TXN.ADJ.POOL.FACTOR` | `CgTxnBase_AdjPoolFactor` |  |  |  |
| 84 | `CG.TXN.REVENUE.PL` | `CgTxnBase_RevenuePl` |  |  |  |
| 85 | `CG.TXN.INCOME.PL` | `CgTxnBase_IncomePl` |  |  |  |
| 86 | `CG.TXN.PUR.INCOME.PL` | `CgTxnBase_PurIncomePl` |  |  |  |
| 87 | `CG.TXN.PUR.DISP.RATIO` | `CgTxnBase_PurDispRatio` |  |  |  |
| 88 | `CG.TXN.ENT.SEC.TRANS.ID` | `CgTxnBase_EntSecTransId` |  |  |  |
| 89 | `CG.TXN.ENT.NOMINAL` | `CgTxnBase_EntNominal` |  |  |  |
| 90 | `CG.TXN.ENT.COST` | `CgTxnBase_EntCost` |  |  |  |
| 91 | `CG.TXN.CG.REDUCED.COST` | `CgTxnBase_CgReducedCost` |  |  |  |
| 92 | `CG.TXN.CG.INDEX.FACTOR` | `CgTxnBase_CgIndexFactor` |  |  |  |
| 93 | `CG.TXN.CG.INDEXED.COST` | `CgTxnBase_CgIndexedCost` |  |  |  |
| 94 | `CG.TXN.REVENUE.PL.LCY` | `CgTxnBase_RevenuePlLcy` |  |  |  |
| 95 | `CG.TXN.INCOME.PL.LCY` | `CgTxnBase_IncomePlLcy` |  |  |  |
| 96 | `CG.TXN.EFFECTIVE.DATE` | `CgTxnBase_EffectiveDate` |  |  |  |
| 97 | `CG.TXN.ENT.ACCRUED.INT` | `CgTxnBase_EntAccruedInt` |  |  |  |
| 98 | `CG.TXN.ENT.EXPENSES` | `CgTxnBase_EntExpenses` |  |  |  |
| 99 | `CG.TXN.SALE.TXN.ID` | `CgTxnBase_SaleTxnId` |  |  |  |
| 100 | `CG.TXN.SALE.TXN.NOM` | `CgTxnBase_SaleTxnNom` |  |  |  |
| 101 | `CG.TXN.ENT.INDEX.FACTOR` | `CgTxnBase_EntIndexFactor` |  |  |  |
| 102 | `CG.TXN.PUR.TAX.LOT.ID` | `CgTxnBase_PurTaxLotId` |  |  |  |
| 103 | `CG.TXN.EXT.CUSTODIAN` | `CgTxnBase_ExtCustodian` | TField |  | This field will contain the external custodian id for the records that are maintained separately for externalcustody positions. |
| 104 | `CG.TXN.CG.CURRENCY` | `CgTxnBase_CgCurrency` | TField |  | This field will hold the currency in which capital gains is calculated. This will hold the local currency if CG.CALC.LCY field is set to YES in CG.PARAMETER record else with securitycurrency. |
| 105 | `CG.TXN.REDUCED.COST` | `CgTxnBase_ReducedCost` |  |  |  |
| 106 | `CG.TXN.INDEXED.COST` | `CgTxnBase_IndexedCost` |  |  |  |
| 107 | `CG.TXN.DEST.BASE` | `CgTxnBase_DestBase` |  |  |  |
| 108 | `CG.TXN.DEST.TRANS.ID` | `CgTxnBase_DestTransId` |  |  |  |
| 109 | `CG.TXN.TRANS.ID` | `CgTxnBase_TransId` |  |  |  |
| 110 | `CG.TXN.SOURCE.BASE` | `CgTxnBase_SourceBase` |  |  |  |
| 111 | `CG.TXN.SOURCE.TRANS.ID` | `CgTxnBase_SourceTransId` |  |  |  |
| 112 | `CG.TXN.SOURCE.REBUILD` | `CgTxnBase_SourceRebuild` |  |  |  |
| 113 | `CG.TXN.ENT.REDUCED.COST` | `CgTxnBase_EntReducedCost` |  |  |  |
| 114 | `CG.TXN.STAPLED.SECURITY` | `CgTxnBase_StapledSecurity` | TField |  | This field will denote if the security is parent stapled or Child component security |
| 115 | `CG.TXN.ENT.INDEXED.COST` | `CgTxnBase_EntIndexedCost` |  |  |  |
| 116 | `CG.TXN.TRANS.TRADE.DATE` | `CgTxnBase_TransTradeDate` |  |  |  |
| 117 | `CG.TXN.TRANS.VALUE.DATE` | `CgTxnBase_TransValueDate` |  |  |  |
| 118 | `CG.TXN.DISALLOWED.NOM` | `CgTxnBase_DisallowedNom` |  |  |  |
| 119 | `CG.TXN.DISALLOWED.LOSS` | `CgTxnBase_DisallowedLoss` |  |  |  |
| 120 | `CG.TXN.DISALLOWED.BASE` | `CgTxnBase_DisallowedBase` |  |  |  |
| 121 | `CG.TXN.DISALLOWED.TXN` | `CgTxnBase_DisallowedTxn` |  |  |  |
| 122 | `CG.TXN.DIS.LOSS.TO.RPL.TXN` | `CgTxnBase_DisLossToRplTxn` |  |  |  |
| 123 | `CG.TXN.CG.TYPE.IND` | `CgTxnBase_CgTypeInd` |  |  |  |
| 124 | `CG.TXN.ORIGINAL.COST` | `CgTxnBase_OriginalCost` |  |  |  |
| 125 | `CG.TXN.CASH.NON.CASH` | `CgTxnBase_CashNonCash` |  |  |  |
| 126 | `CG.TXN.CORP.NOMINAL` | `CgTxnBase_CorpNominal` |  |  |  |
| 127 | `CG.TXN.CORP.TRD.COST` | `CgTxnBase_CorpTrdCost` |  |  |  |
| 128 | `CG.TXN.CORP.EXPENSES` | `CgTxnBase_CorpExpenses` |  |  |  |
| 129 | `CG.TXN.CORP.REDUCED.COST` | `CgTxnBase_CorpReducedCost` |  |  |  |
| 130 | `CG.TXN.CORP.ORIGINAL.COST` | `CgTxnBase_CorpOriginalCost` |  |  |  |
| 131 | `CG.TXN.CORP.DEMERGE.COST` | `CgTxnBase_CorpDemergeCost` |  |  |  |
| 132 | `CG.TXN.CORP.NOM.UPDATE` | `CgTxnBase_CorpNomUpdate` |  |  |  |
| 133 | `CG.TXN.CORP.PRE.CGT.DATE` | `CgTxnBase_CorpPreCgtDate` |  |  |  |
| 134 | `CG.TXN.CORP.NOTIONAL.COST` | `CgTxnBase_CorpNotionalCost` |  |  |  |
| 135 | `CG.TXN.CORP.DIFF.DATE.TIME` | `CgTxnBase_CorpDiffDateTime` |  |  |  |
| 136 | `CG.TXN.CORP.DIFF.COST` | `CgTxnBase_CorpDiffCost` |  |  |  |
| 137 | `CG.TXN.CORP.UPDATE` | `CgTxnBase_CorpUpdate` |  |  |  |
| 138 | `CG.TXN.CORP.TRADE.DATE` | `CgTxnBase_CorpTradeDate` |  |  |  |
| 139 | `CG.TXN.CORP.APPLN.ID` | `CgTxnBase_CorpApplnId` |  |  |  |
| 140 | `CG.TXN.CORP.DEST.BASE` | `CgTxnBase_CorpDestBase` |  |  |  |
| 141 | `CG.TXN.CORP.DEST.TRANS.ID` | `CgTxnBase_CorpDestTransId` |  |  |  |
| 142 | `CG.TXN.CG.ORIGINAL.COST` | `CgTxnBase_CgOriginalCost` |  |  |  |
| 143 | `CG.TXN.ENT.ORIGINAL.COST` | `CgTxnBase_EntOriginalCost` |  |  |  |
| 144 | `CG.TXN.NOM.DISP.RATIO` | `CgTxnBase_NomDispRatio` |  |  |  |
| 145 | `CG.TXN.STAPLED.COMPONENT.ID` | `CgTxnBase_StapledComponentId` |  |  |  |
| 146 | `CG.TXN.CORP.STAPLED.COMP.ID` | `CgTxnBase_CorpStapledCompId` |  |  |  |
| 147 | `CG.TXN.STAPLE.REBUILD` | `CgTxnBase_StapleRebuild` |  |  |  |
| 148 | `CG.TXN.PUR.TXN.PROCEEDS` | `CgTxnBase_PurTxnProceeds` |  |  |  |
| 149 | `CG.TXN.CORP.SECURITY.NO` | `CgTxnBase_CorpSecurityNo` |  |  |  |
| 150 | `CG.TXN.CORP.ELIG.NOMINAL` | `CgTxnBase_CorpEligNominal` |  |  |  |
| 151 | `CG.TXN.CG.EX.RATE.SETT` | `CgTxnBase_CgExRateSett` |  |  |  |
| 152 | `CG.TXN.FX.CG.PL` | `CgTxnBase_FxCgPl` |  |  |  |
| 153 | `CG.TXN.PUR.FX.CG.PL` | `CgTxnBase_PurFxCgPl` |  |  |  |
| 154 | `CG.TXN.CORP.TRANS.TRADE.DATE` | `CgTxnBase_CorpTransTradeDate` |  |  |  |
| 155 | `CG.TXN.CORP.TRANS.VALUE.DATE` | `CgTxnBase_CorpTransValueDate` |  |  |  |
| 156 | `CG.TXN.PARENT.TAX.LOT.ID` | `CgTxnBase_ParentTaxLotId` |  |  |  |
| 157 | `CG.TXN.STAPLING.EFF.DATE.TIME` | `CgTxnBase_StaplingEffDateTime` |  |  |  |
| 158 | `CG.TXN.UNSTAPLING.EFF.DATE.TIME` | `CgTxnBase_UnstaplingEffDateTime` |  |  |  |
| 159 | `CG.TXN.CORP.DEFERRED.RATE` | `CgTxnBase_CorpDeferredRate` |  |  |  |
| 160 | `CG.TXN.ENT.DEFERRED.RATE` | `CgTxnBase_EntDeferredRate` |  |  |  |
