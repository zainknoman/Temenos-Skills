# SY.IMF — Table Schema

> Source: `INSERTS/I_F.SY.IMF` in `XF_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.IMF.DESCRIPTION` | `SyImf_Description` |  |  |  |
| 2 | `SY.IMF.VARIANT` | `SyImf_Variant` | TField |  |  |
| 3 | `SY.IMF.CONTRACT.STATUS` | `SyImf_ContractStatus` | TField |  |  |
| 4 | `SY.IMF.CUSTOMER` | `SyImf_Customer` | TField |  |  |
| 5 | `SY.IMF.PORTFOLIO` | `SyImf_Portfolio` | TField |  |  |
| 6 | `SY.IMF.CONTRACT.CCY` | `SyImf_ContractCcy` | TField |  |  |
| 7 | `SY.IMF.TRADE.DATE` | `SyImf_TradeDate` | TField |  |  |
| 8 | `SY.IMF.VALUE.DATE` | `SyImf_ValueDate` | TField |  |  |
| 9 | `SY.IMF.MATURITY.DATE` | `SyImf_MaturityDate` | TField |  |  |
| 10 | `SY.IMF.DEPOSIT.CATEGORY` | `SyImf_DepositCategory` | TField |  |  |
| 11 | `SY.IMF.DEPOSIT.CCY` | `SyImf_DepositCcy` | TField |  |  |
| 12 | `SY.IMF.DEPOSIT.AMT` | `SyImf_DepositAmt` | TField |  |  |
| 13 | `SY.IMF.DEPOSIT.BASE.INT` | `SyImf_DepositBaseInt` | TField |  |  |
| 14 | `SY.IMF.DEPOSIT.SPREAD` | `SyImf_DepositSpread` | TField |  |  |
| 15 | `SY.IMF.DEPOSIT.INT` | `SyImf_DepositInt` | TField |  |  |
| 16 | `SY.IMF.DEP.ACCOUNT` | `SyImf_DepAccount` | TField |  |  |
| 17 | `SY.IMF.DEP.INT.AMT` | `SyImf_DepIntAmt` | TField |  |  |
| 18 | `SY.IMF.DEP.DAY.BASIS` | `SyImf_DepDayBasis` | TField |  |  |
| 19 | `SY.IMF.DEP.INT.KEY` | `SyImf_DepIntKey` | TField |  |  |
| 20 | `SY.IMF.LOAN.CATEGORY` | `SyImf_LoanCategory` | TField |  |  |
| 21 | `SY.IMF.LOAN.CCY` | `SyImf_LoanCcy` | TField |  |  |
| 22 | `SY.IMF.LOAN.AMT` | `SyImf_LoanAmt` | TField |  |  |
| 23 | `SY.IMF.LOAN.BASE.INT` | `SyImf_LoanBaseInt` | TField |  |  |
| 24 | `SY.IMF.LOAN.SPREAD` | `SyImf_LoanSpread` | TField |  |  |
| 25 | `SY.IMF.LOAN.LIQ.ACCOUNT` | `SyImf_LoanLiqAccount` | TField |  |  |
| 26 | `SY.IMF.LOAN.INT` | `SyImf_LoanInt` | TField |  |  |
| 27 | `SY.IMF.LOAN.INT.AMT` | `SyImf_LoanIntAmt` | TField |  |  |
| 28 | `SY.IMF.LOAN.DAY.BASIS` | `SyImf_LoanDayBasis` | TField |  |  |
| 29 | `SY.IMF.SPOT.RATE` | `SyImf_SpotRate` | TField |  |  |
| 30 | `SY.IMF.LOAN.PI.KEY` | `SyImf_LoanPiKey` | TField |  |  |
| 31 | `SY.IMF.SUPPRESS.UNDERLYING` | `SyImf_SuppressUnderlying` | TField |  |  |
| 32 | `SY.IMF.AUTO.ROLLOVER.TERM` | `SyImf_AutoRolloverTerm` | TField |  |  |
| 33 | `SY.IMF.MANUAL.ROLLOVER` | `SyImf_ManualRollover` | TField |  |  |
| 34 | `SY.IMF.ROLLOVER.TYPE` | `SyImf_RolloverType` | TField |  |  |
| 35 | `SY.IMF.ROLLOVER.DATE` | `SyImf_RolloverDate` | TField |  |  |
| 36 | `SY.IMF.DEP.PRIN.ADJUST` | `SyImf_DepPrinAdjust` | TField |  |  |
| 37 | `SY.IMF.DEP.NEW.INT.RATE` | `SyImf_DepNewIntRate` | TField |  |  |
| 38 | `SY.IMF.DEP.ADJ.EFF.DATE` | `SyImf_DepAdjEffDate` | TField |  |  |
| 39 | `SY.IMF.LOAN.PRIN.ADJUST` | `SyImf_LoanPrinAdjust` | TField |  |  |
| 40 | `SY.IMF.LOAN.NEW.INT.RATE` | `SyImf_LoanNewIntRate` | TField |  |  |
| 41 | `SY.IMF.LN.ADJ.EFF.DATE` | `SyImf_LnAdjEffDate` | TField |  |  |
| 42 | `SY.IMF.FINAL.MATURITY.DATE` | `SyImf_FinalMaturityDate` | TField |  |  |
| 43 | `SY.IMF.EARLY.MATURITY.DATE` | `SyImf_EarlyMaturityDate` | TField |  |  |
| 44 | `SY.IMF.UNWIND.CHG.CCY` | `SyImf_UnwindChgCcy` | TField |  |  |
| 45 | `SY.IMF.UNWIND.CHG.AMT` | `SyImf_UnwindChgAmt` | TField |  |  |
| 46 | `SY.IMF.UNWIND.CHG.ACC` | `SyImf_UnwindChgAcc` | TField |  |  |
| 47 | `SY.IMF.UNWIND.POST.TIME` | `SyImf_UnwindPostTime` | TField |  |  |
| 48 | `SY.IMF.DEALER.DESK` | `SyImf_DealerDesk` | TField |  |  |
| 49 | `SY.IMF.REMARKS` | `SyImf_Remarks` |  |  |  |
| 50 | `SY.IMF.CLIENT.CONT.REFER` | `SyImf_ClientContRefer` |  |  |  |
| 51 | `SY.IMF.FX.DEAL.REFERENCE` | `SyImf_FxDealReference` |  |  |  |
| 52 | `SY.IMF.EXTERNAL.REF` | `SyImf_ExternalRef` | TField |  |  |
| 53 | `SY.IMF.SY.TRANSACTION.REF` | `SyImf_SyTransactionRef` | TField |  |  |
| 54 | `SY.IMF.UNDERLYING.REF` | `SyImf_UnderlyingRef` |  |  |  |
| 55 | `SY.IMF.SY.DX.REFERENCE` | `SyImf_SyDxReference` | TField |  |  |
| 56 | `SY.IMF.NEXT.DEP.INT.AMT` | `SyImf_NextDepIntAmt` | TField |  |  |
| 57 | `SY.IMF.NEXT.DEPOSIT.AMT` | `SyImf_NextDepositAmt` | TField |  |  |
| 58 | `SY.IMF.NEXT.LOAN.INT.AMT` | `SyImf_NextLoanIntAmt` | TField |  |  |
| 59 | `SY.IMF.NEXT.LOAN.AMT` | `SyImf_NextLoanAmt` | TField |  |  |
| 60 | `SY.IMF.RESERVED.15` | `SyImf_Reserved15` | TField |  |  |
| 61 | `SY.IMF.RESERVED.14` | `SyImf_Reserved14` | TField |  |  |
| 62 | `SY.IMF.RESERVED.13` | `SyImf_Reserved13` | TField |  |  |
| 63 | `SY.IMF.RESERVED.12` | `SyImf_Reserved12` | TField |  |  |
| 64 | `SY.IMF.RESERVED.11` | `SyImf_Reserved11` | TField |  |  |
| 65 | `SY.IMF.RESERVED.10` | `SyImf_Reserved10` | TField |  |  |
| 66 | `SY.IMF.RESERVED.09` | `SyImf_Reserved09` | TField |  |  |
| 67 | `SY.IMF.RESERVED.08` | `SyImf_Reserved08` | TField |  |  |
| 68 | `SY.IMF.RESERVED.07` | `SyImf_Reserved07` | TField |  |  |
| 69 | `SY.IMF.RESERVED.06` | `SyImf_Reserved06` | TField |  |  |
| 70 | `SY.IMF.RESERVED.05` | `SyImf_Reserved05` | TField |  |  |
| 71 | `SY.IMF.RESERVED.04` | `SyImf_Reserved04` | TField |  |  |
| 72 | `SY.IMF.RESERVED.03` | `SyImf_Reserved03` | TField |  |  |
| 73 | `SY.IMF.RESERVED.02` | `SyImf_Reserved02` | TField |  |  |
| 74 | `SY.IMF.RESERVED.01` | `SyImf_Reserved01` | TField |  |  |
| 75 | `SY.IMF.LOCAL.REF` | `SyImf_LocalRef` |  |  |  |
| 76 | `SY.IMF.STMT.NOS` | `SyImf_StmtNos` |  |  |  |
| 77 | `SY.IMF.OVERRIDE` | `SyImf_Override` |  |  |  |
| 78 | `SY.IMF.RECORD.STATUS` | `SyImf_RecordStatus` | String |  |  |
| 79 | `SY.IMF.CURR.NO` | `SyImf_CurrNo` | String |  |  |
| 80 | `SY.IMF.INPUTTER` | `SyImf_Inputter` |  |  |  |
| 81 | `SY.IMF.DATE.TIME` | `SyImf_DateTime` |  |  |  |
| 82 | `SY.IMF.AUTHORISER` | `SyImf_Authoriser` | String |  |  |
| 83 | `SY.IMF.CO.CODE` | `SyImf_CoCode` | String |  |  |
| 84 | `SY.IMF.DEPT.CODE` | `SyImf_DeptCode` | String |  |  |
| 85 | `SY.IMF.AUDITOR.CODE` | `SyImf_AuditorCode` | String |  |  |
| 86 | `SY.IMF.AUDIT.DATE.TIME` | `SyImf_AuditDateTime` | String |  |  |
