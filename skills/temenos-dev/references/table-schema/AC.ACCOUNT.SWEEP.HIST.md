# AC.ACCOUNT.SWEEP.HIST — Table Schema

> Source: `INSERTS/I_F.AC.ACCOUNT.SWEEP.HIST` in `ST_Sweeping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.SW.HIST.SWEEP.DATE` | `AcAccountSweepHist_SweepDate` |  |  |  |
| 2 | `AC.SW.HIST.SWEEP.REF` | `AcAccountSweepHist_SweepRef` |  |  |  |
| 3 | `AC.SW.HIST.SWEEP.AMOUNT` | `AcAccountSweepHist_SweepAmount` |  |  |  |
| 4 | `AC.SW.HIST.CP.GROUP.ID` | `AcAccountSweepHist_CpGroupId` |  |  |  |
| 5 | `AC.SW.HIST.CP.SEQ.NO` | `AcAccountSweepHist_CpSeqNo` |  |  |  |
| 6 | `AC.SW.HIST.DR.START.BAL` | `AcAccountSweepHist_DrStartBal` |  |  |  |
| 7 | `AC.SW.HIST.SWEEP.TYPE` | `AcAccountSweepHist_SweepType` |  |  |  |
| 8 | `AC.SW.HIST.AGREGATE.BAL` | `AcAccountSweepHist_AgregateBal` |  |  |  |
| 9 | `AC.SW.HIST.CASHFLOW.AMT` | `AcAccountSweepHist_CashflowAmt` |  |  |  |
| 10 | `AC.SW.HIST.BALANCE.USED` | `AcAccountSweepHist_BalanceUsed` |  |  |  |
| 11 | `AC.SW.HIST.REVERSAL.IND` | `AcAccountSweepHist_ReversalInd` |  |  |  |
| 12 | `AC.SW.HIST.FREQUENCY` | `AcAccountSweepHist_Frequency` |  |  |  |
| 13 | `AC.SW.HIST.NXT.RUN.DATE` | `AcAccountSweepHist_NxtRunDate` |  |  |  |
| 14 | `AC.SW.HIST.LINK.ID` | `AcAccountSweepHist_LinkId` |  |  |  |
| 15 | `AC.SW.HIST.SCHEDULE` | `AcAccountSweepHist_Schedule` |  |  |  |
| 16 | `AC.SW.HIST.PERCENTAGE` | `AcAccountSweepHist_Percentage` |  |  |  |
| 17 | `AC.SW.HIST.NETTING` | `AcAccountSweepHist_Netting` |  |  |  |
| 18 | `AC.SW.HIST.BACK.VALUE` | `AcAccountSweepHist_BackValue` |  |  |  |
| 19 | `AC.SW.HIST.CHARGE.AMT` | `AcAccountSweepHist_ChargeAmt` |  |  |  |
| 20 | `AC.SW.HIST.MAXIMUM.AMT` | `AcAccountSweepHist_MaximumAmt` |  |  |  |
| 21 | `AC.SW.HIST.MINIMUM.AMT` | `AcAccountSweepHist_MinimumAmt` |  |  |  |
| 22 | `AC.SW.HIST.CR.START.BAL` | `AcAccountSweepHist_CrStartBal` |  |  |  |
| 23 | `AC.SW.HIST.CASH.POOL.ID` | `AcAccountSweepHist_CashPoolId` |  |  |  |
| 24 | `AC.SW.HIST.OVERRIDE.AMT` | `AcAccountSweepHist_OverrideAmt` |  |  |  |
| 25 | `AC.SW.HIST.OVERRIDE.PERCNT` | `AcAccountSweepHist_OverridePercnt` |  |  |  |
| 26 | `AC.SW.HIST.AMT.ROUTINE` | `AcAccountSweepHist_AmtRoutine` |  |  |  |
| 27 | `AC.SW.HIST.UP.TO.AMOUNT` | `AcAccountSweepHist_UpToAmount` |  |  |  |
| 28 | `AC.SW.HIST.UP.TO.PERCENT` | `AcAccountSweepHist_UpToPercent` |  |  |  |
| 29 | `AC.SW.HIST.RERUN.IND` | `AcAccountSweepHist_RerunInd` |  |  |  |
| 30 | `AC.SW.HIST.MIN.TFR.DR` | `AcAccountSweepHist_MinTfrDr` |  |  |  |
| 31 | `AC.SW.HIST.MIN.TFR.CR` | `AcAccountSweepHist_MinTfrCr` |  |  |  |
| 32 | `AC.SW.HIST.TOT.ST.BAL` | `AcAccountSweepHist_TotStBal` |  |  |  |
| 33 | `AC.SW.HIST.SWEEP.EXCH.RATE` | `AcAccountSweepHist_SweepExchRate` |  |  |  |
| 34 | `AC.SW.HIST.MKTG.EXCH.PROFIT` | `AcAccountSweepHist_MktgExchProfit` |  |  |  |
| 35 | `AC.SW.HIST.TOT.SW.AMT` | `AcAccountSweepHist_TotSwAmt` |  |  |  |
| 36 | `AC.SW.HIST.BV.SW.DATE` | `AcAccountSweepHist_BvSwDate` |  |  |  |
| 37 | `AC.SW.HIST.ACTIVITY.BAL` | `AcAccountSweepHist_ActivityBal` |  |  |  |
| 38 | `AC.SW.HIST.ADJUSTED.AMT` | `AcAccountSweepHist_AdjustedAmt` |  |  |  |
| 39 | `AC.SW.HIST.RESERVED2` | `AcAccountSweepHist_Reserved2` |  |  |  |
| 40 | `AC.SW.HIST.CORRECTION.NO` | `AcAccountSweepHist_CorrectionNo` |  |  |  |
| 41 | `AC.SW.HIST.LOCKED.AMOUNT` | `AcAccountSweepHist_LockedAmount` |  |  |  |
