# AA.AZ.LOAN — Table Schema

> Source: `INSERTS/I_F.AA.AZ.LOAN` in `AA_ClassicProducts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AZL.ACTIVITY` | `AaArrAzLoan_Activity` |  |  |  |
| 2 | `AA.AZL.ACTION` | `AaArrAzLoan_Action` |  |  |  |
| 3 | `AA.AZL.DRAWDOWN.TYPE` | `AaArrAzLoan_DrawdownType` |  |  |  |
| 4 | `AA.AZL.ROLL.MAT.WRK.DAY` | `AaArrAzLoan_RollMatWrkDay` |  |  |  |
| 5 | `AA.AZL.PD.LINK.TO.AZ` | `AaArrAzLoan_PdLinkToAz` |  |  |  |
| 6 | `AA.AZL.IRA.PROCESS` | `AaArrAzLoan_IraProcess` |  |  |  |
| 7 | `AA.AZL.GRACE.PERIOD` | `AaArrAzLoan_GracePeriod` |  |  |  |
| 8 | `AA.AZL.MATURITY.INSTR` | `AaArrAzLoan_MaturityInstr` |  |  |  |
| 9 | `AA.AZL.RECALC.CURR.AMT` | `AaArrAzLoan_RecalcCurrAmt` |  |  |  |
| 10 | `AA.AZL.INT.ONLY` | `AaArrAzLoan_IntOnly` |  |  |  |
| 11 | `AA.AZL.MAX.INSTL.INT.ONLY` | `AaArrAzLoan_MaxInstlIntOnly` |  |  |  |
| 12 | `AA.AZL.LOAN.INT.ADJUST` | `AaArrAzLoan_LoanIntAdjust` |  |  |  |
| 13 | `AA.AZL.REPAYMENT.TYPE` | `AaArrAzLoan_RepaymentType` |  |  |  |
| 14 | `AA.AZL.SINGLE.LIMIT` | `AaArrAzLoan_SingleLimit` |  |  |  |
| 15 | `AA.AZL.TERM.PRIORITY` | `AaArrAzLoan_TermPriority` |  |  |  |
| 16 | `AA.AZL.REDUCE.LIMIT` | `AaArrAzLoan_ReduceLimit` |  |  |  |
| 17 | `AA.AZL.PRE.CLOSURE.FEE` | `AaArrAzLoan_PreClosureFee` |  |  |  |
| 18 | `AA.AZL.RESCHED.TYPE` | `AaArrAzLoan_ReschedType` |  |  |  |
| 19 | `AA.AZL.RESCHED.NOTICE` | `AaArrAzLoan_ReschedNotice` |  |  |  |
| 20 | `AA.AZL.RESERVED1` | `AaArrAzLoan_Reserved1` |  |  |  |
| 21 | `AA.AZL.LOCAL.REF` | `AaArrAzLoan_LocalRef` |  |  |  |
| 22 | `AA.AZL.PR.ATTRIBUTE` | `AaArrAzLoan_PrAttribute` |  |  |  |
| 23 | `AA.AZL.PR.VALUE` | `AaArrAzLoan_PrValue` |  |  |  |
| 24 | `AA.AZL.PR.BRK.RES` | `AaArrAzLoan_PrBrkRes` |  |  |  |
| 25 | `AA.AZL.PR.BRK.MSG` | `AaArrAzLoan_PrBrkMsg` |  |  |  |
| 26 | `AA.AZL.PR.BRK.CHARGE` | `AaArrAzLoan_PrBrkCharge` |  |  |  |
| 27 | `AA.AZL.PR.RESERVED.3` | `AaArrAzLoan_PrReserved3` |  |  |  |
| 28 | `AA.AZL.PR.RESERVED.2` | `AaArrAzLoan_PrReserved2` |  |  |  |
| 29 | `AA.AZL.PR.RESERVED.1` | `AaArrAzLoan_PrReserved1` |  |  |  |
| 30 | `AA.AZL.PR.APP.METHOD` | `AaArrAzLoan_PrAppMethod` |  |  |  |
| 31 | `AA.AZL.PR.APP.PERIOD` | `AaArrAzLoan_PrAppPeriod` |  |  |  |
| 32 | `AA.AZL.SYS.RESERVE7` | `AaArrAzLoan_SysReserve7` |  |  |  |
| 33 | `AA.AZL.SYS.RESERVE6` | `AaArrAzLoan_SysReserve6` |  |  |  |
| 34 | `AA.AZL.OWNING.COMPANY` | `AaArrAzLoan_OwningCompany` |  |  |  |
| 35 | `AA.AZL.API.ATTRIBUTE` | `AaArrAzLoan_ApiAttribute` |  |  |  |
| 36 | `AA.AZL.SYS.RESERVE3` | `AaArrAzLoan_SysReserve3` |  |  |  |
| 37 | `AA.AZL.SYS.RESERVE2` | `AaArrAzLoan_SysReserve2` |  |  |  |
| 38 | `AA.AZL.SYS.RESERVE1` | `AaArrAzLoan_SysReserve1` |  |  |  |
| 39 | `AA.AZL.DEFAULT.ATTR.OPTION` | `AaArrAzLoan_DefaultAttrOption` |  |  |  |
| 40 | `AA.AZL.DEFAULT.NEGOTIABLE` | `AaArrAzLoan_DefaultNegotiable` |  |  |  |
| 41 | `AA.AZL.NR.ATTRIBUTE` | `AaArrAzLoan_NrAttribute` |  |  |  |
| 42 | `AA.AZL.NR.OPTIONS` | `AaArrAzLoan_NrOptions` |  |  |  |
| 43 | `AA.AZL.NR.RESERVED2` | `AaArrAzLoan_NrReserved2` |  |  |  |
| 44 | `AA.AZL.NR.RESERVED1` | `AaArrAzLoan_NrReserved1` |  |  |  |
| 45 | `AA.AZL.NR.STD.COMP` | `AaArrAzLoan_NrStdComp` |  |  |  |
| 46 | `AA.AZL.NR.TYPE` | `AaArrAzLoan_NrType` |  |  |  |
| 47 | `AA.AZL.NR.VALUE` | `AaArrAzLoan_NrValue` |  |  |  |
| 48 | `AA.AZL.NR.MESSAGE` | `AaArrAzLoan_NrMessage` |  |  |  |
| 49 | `AA.AZL.CHANGED.FIELDS` | `AaArrAzLoan_ChangedFields` |  |  |  |
| 50 | `AA.AZL.NEGOTIATED.FLDS` | `AaArrAzLoan_NegotiatedFlds` |  |  |  |
| 51 | `AA.AZL.ID.COMP.1` | `AaArrAzLoan_IdComp1` |  |  |  |
| 52 | `AA.AZL.ID.COMP.2` | `AaArrAzLoan_IdComp2` |  |  |  |
| 53 | `AA.AZL.ID.COMP.3` | `AaArrAzLoan_IdComp3` |  |  |  |
| 54 | `AA.AZL.ID.COMP.4` | `AaArrAzLoan_IdComp4` |  |  |  |
| 55 | `AA.AZL.ID.COMP.5` | `AaArrAzLoan_IdComp5` |  |  |  |
| 56 | `AA.AZL.ID.COMP.6` | `AaArrAzLoan_IdComp6` |  |  |  |
| 57 | `AA.AZL.RESERVED2.ID` | `AaArrAzLoan_Reserved2Id` |  |  |  |
| 58 | `AA.AZL.TARGET.PRODUCT` | `AaArrAzLoan_TargetProduct` |  |  |  |
| 59 | `AA.AZL.STMT.NOS` | `AaArrAzLoan_StmtNos` |  |  |  |
| 60 | `AA.AZL.OVERRIDE` | `AaArrAzLoan_Override` |  |  |  |
| 61 | `AA.AZL.RECORD.STATUS` | `AaArrAzLoan_RecordStatus` |  |  |  |
| 62 | `AA.AZL.CURR.NO` | `AaArrAzLoan_CurrNo` |  |  |  |
| 63 | `AA.AZL.INPUTTER` | `AaArrAzLoan_Inputter` |  |  |  |
| 64 | `AA.AZL.DATE.TIME` | `AaArrAzLoan_DateTime` |  |  |  |
| 65 | `AA.AZL.AUTHORISER` | `AaArrAzLoan_Authoriser` |  |  |  |
| 66 | `AA.AZL.CO.CODE` | `AaArrAzLoan_CoCode` |  |  |  |
| 67 | `AA.AZL.DEPT.CODE` | `AaArrAzLoan_DeptCode` |  |  |  |
| 68 | `AA.AZL.AUDITOR.CODE` | `AaArrAzLoan_AuditorCode` |  |  |  |
| 69 | `AA.AZL.AUDIT.DATE.TIME` | `AaArrAzLoan_AuditDateTime` |  |  |  |
