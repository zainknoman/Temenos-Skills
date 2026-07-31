# MDI.TERM.PROD.SUMM.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.TERM.PROD.SUMM.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.TERM.PROD.ITEM.REQ` | `MdiTermProdSummWork_ItemReq` |  |  |  |
| 2 | `MDI.TERM.PROD.ITEM.SENT` | `MdiTermProdSummWork_ItemSent` |  |  |  |
| 3 | `MDI.TERM.PROD.MORE.FLAG` | `MdiTermProdSummWork_MoreFlag` |  |  |  |
| 4 | `MDI.TERM.PROD.PAN.NO` | `MdiTermProdSummWork_PanNo` |  |  |  |
| 5 | `MDI.TERM.PROD.MEMBER.NO` | `MdiTermProdSummWork_MemberNo` |  |  |  |
| 6 | `MDI.TERM.PROD.TERMPROD.TYPE` | `MdiTermProdSummWork_TermprodType` |  |  |  |
| 7 | `MDI.TERM.PROD.TERMPROD.ID` | `MdiTermProdSummWork_TermprodId` |  |  |  |
| 8 | `MDI.TERM.PROD.SERIES` | `MdiTermProdSummWork_Series` |  |  |  |
| 9 | `MDI.TERM.PROD.SUB.TYPE` | `MdiTermProdSummWork_SubType` |  |  |  |
| 10 | `MDI.TERM.PROD.CUSTOMER.TYPE` | `MdiTermProdSummWork_CustomerType` |  |  |  |
| 11 | `MDI.TERM.PROD.PRINCIPAL` | `MdiTermProdSummWork_Principal` |  |  |  |
| 12 | `MDI.TERM.PROD.WORK.BALANCE` | `MdiTermProdSummWork_WorkBalance` |  |  |  |
| 13 | `MDI.TERM.PROD.ORIG.DEPOSIT.AMT` | `MdiTermProdSummWork_OrigDepositAmt` |  |  |  |
| 14 | `MDI.TERM.PROD.TOTAL.DEPOSIT.AMT` | `MdiTermProdSummWork_TotalDepositAmt` |  |  |  |
| 15 | `MDI.TERM.PROD.CNT.OF.RATES` | `MdiTermProdSummWork_CntOfRates` |  |  |  |
| 16 | `MDI.TERM.PROD.TERM.RATE` | `MdiTermProdSummWork_TermRate` |  |  |  |
| 17 | `MDI.TERM.PROD.TERM.CCY` | `MdiTermProdSummWork_TermCcy` |  |  |  |
| 18 | `MDI.TERM.PROD.INT.CCY` | `MdiTermProdSummWork_IntCcy` |  |  |  |
| 19 | `MDI.TERM.PROD.START.DATE` | `MdiTermProdSummWork_StartDate` |  |  |  |
| 20 | `MDI.TERM.PROD.CASH.DATE` | `MdiTermProdSummWork_CashDate` |  |  |  |
| 21 | `MDI.TERM.PROD.TERM.LENTH` | `MdiTermProdSummWork_TermLenth` |  |  |  |
| 22 | `MDI.TERM.PROD.TERM.FREQ` | `MdiTermProdSummWork_TermFreq` |  |  |  |
| 23 | `MDI.TERM.PROD.INT.LENTH` | `MdiTermProdSummWork_IntLenth` |  |  |  |
| 24 | `MDI.TERM.PROD.INT.FREQ` | `MdiTermProdSummWork_IntFreq` |  |  |  |
| 25 | `MDI.TERM.PROD.MATURITY.DATE` | `MdiTermProdSummWork_MaturityDate` |  |  |  |
| 26 | `MDI.TERM.PROD.FIRST.INT.RATE` | `MdiTermProdSummWork_FirstIntRate` |  |  |  |
| 27 | `MDI.TERM.PROD.NEXT.INT.RATE` | `MdiTermProdSummWork_NextIntRate` |  |  |  |
| 28 | `MDI.TERM.PROD.INT.PROD.TYPE` | `MdiTermProdSummWork_IntProdType` |  |  |  |
| 29 | `MDI.TERM.PROD.INT.PROD.ID` | `MdiTermProdSummWork_IntProdId` |  |  |  |
| 30 | `MDI.TERM.PROD.INT.TO.IND` | `MdiTermProdSummWork_IntToInd` |  |  |  |
| 31 | `MDI.TERM.PROD.INT.MEMBER.ID` | `MdiTermProdSummWork_IntMemberId` |  |  |  |
| 32 | `MDI.TERM.PROD.MATURITY.BIN` | `MdiTermProdSummWork_MaturityBin` |  |  |  |
| 33 | `MDI.TERM.PROD.MATURITY.BRANCH` | `MdiTermProdSummWork_MaturityBranch` |  |  |  |
| 34 | `MDI.TERM.PROD.MATURITY.MEMBER.ID` | `MdiTermProdSummWork_MaturityMemberId` |  |  |  |
| 35 | `MDI.TERM.PROD.MATURITY.IND` | `MdiTermProdSummWork_MaturityInd` |  |  |  |
| 36 | `MDI.TERM.PROD.MATURITY.PROD.TYPE` | `MdiTermProdSummWork_MaturityProdType` |  |  |  |
| 37 | `MDI.TERM.PROD.MATURITY.PROD.ID` | `MdiTermProdSummWork_MaturityProdId` |  |  |  |
| 38 | `MDI.TERM.PROD.RSP.NUMBER` | `MdiTermProdSummWork_RspNumber` |  |  |  |
| 39 | `MDI.TERM.PROD.RENEW.RATE` | `MdiTermProdSummWork_RenewRate` |  |  |  |
| 40 | `MDI.TERM.PROD.TERM.SPLIT` | `MdiTermProdSummWork_TermSplit` |  |  |  |
| 41 | `MDI.TERM.PROD.PRIMEPLUS` | `MdiTermProdSummWork_Primeplus` |  |  |  |
| 42 | `MDI.TERM.PROD.TRANS.BIN.INT` | `MdiTermProdSummWork_TransBinInt` |  |  |  |
| 43 | `MDI.TERM.PROD.TRANS.BRANCH.INT` | `MdiTermProdSummWork_TransBranchInt` |  |  |  |
| 44 | `MDI.TERM.PROD.ROLL.TYPE` | `MdiTermProdSummWork_RollType` |  |  |  |
| 45 | `MDI.TERM.PROD.ROLL.SERIES` | `MdiTermProdSummWork_RollSeries` |  |  |  |
| 46 | `MDI.TERM.PROD.IS.MARKET.INDEX` | `MdiTermProdSummWork_IsMarketIndex` |  |  |  |
| 47 | `MDI.TERM.PROD.PART.PERCENT` | `MdiTermProdSummWork_PartPercent` |  |  |  |
| 48 | `MDI.TERM.PROD.BEGIN.MARKET.INDEX` | `MdiTermProdSummWork_BeginMarketIndex` |  |  |  |
| 49 | `MDI.TERM.PROD.END.MARKET.INDEX` | `MdiTermProdSummWork_EndMarketIndex` |  |  |  |
| 50 | `MDI.TERM.PROD.DESCRIPTION` | `MdiTermProdSummWork_Description` |  |  |  |
| 51 | `MDI.TERM.PROD.ALLOW.WITHDRAWAL` | `MdiTermProdSummWork_AllowWithdrawal` |  |  |  |
| 52 | `MDI.TERM.PROD.RENEW.UNTIL.DATE` | `MdiTermProdSummWork_RenewUntilDate` |  |  |  |
| 53 | `MDI.TERM.PROD.RENEW.TRANS.AMT` | `MdiTermProdSummWork_RenewTransAmt` |  |  |  |
| 54 | `MDI.TERM.PROD.INT.EARNED.YTD` | `MdiTermProdSummWork_IntEarnedYtd` |  |  |  |
| 55 | `MDI.TERM.PROD.INT.PAID.YTD` | `MdiTermProdSummWork_IntPaidYtd` |  |  |  |
| 56 | `MDI.TERM.PROD.INT.EARNED.LY` | `MdiTermProdSummWork_IntEarnedLy` |  |  |  |
| 57 | `MDI.TERM.PROD.PRIME.MEM.NAME` | `MdiTermProdSummWork_PrimeMemName` |  |  |  |
| 58 | `MDI.TERM.PROD.TERM.FOREIGN.PERSON` | `MdiTermProdSummWork_TermForeignPerson` |  |  |  |
| 59 | `MDI.TERM.PROD.JOINT.MEM.NAME` | `MdiTermProdSummWork_JointMemName` |  |  |  |
| 60 | `MDI.TERM.PROD.RESERVED.10` | `MdiTermProdSummWork_Reserved10` |  |  |  |
| 61 | `MDI.TERM.PROD.RESERVED.9` | `MdiTermProdSummWork_Reserved9` |  |  |  |
| 62 | `MDI.TERM.PROD.RESERVED.8` | `MdiTermProdSummWork_Reserved8` |  |  |  |
| 63 | `MDI.TERM.PROD.RESERVED.7` | `MdiTermProdSummWork_Reserved7` |  |  |  |
| 64 | `MDI.TERM.PROD.RESERVED.6` | `MdiTermProdSummWork_Reserved6` |  |  |  |
| 65 | `MDI.TERM.PROD.RESERVED.5` | `MdiTermProdSummWork_Reserved5` |  |  |  |
| 66 | `MDI.TERM.PROD.RESERVED.4` | `MdiTermProdSummWork_Reserved4` |  |  |  |
| 67 | `MDI.TERM.PROD.RESERVED.3` | `MdiTermProdSummWork_Reserved3` |  |  |  |
| 68 | `MDI.TERM.PROD.RESERVED.2` | `MdiTermProdSummWork_Reserved2` |  |  |  |
| 69 | `MDI.TERM.PROD.RESERVED.1` | `MdiTermProdSummWork_Reserved1` |  |  |  |
| 70 | `MDI.TERM.PROD.LOCAL.REF` | `MdiTermProdSummWork_LocalRef` |  |  |  |
