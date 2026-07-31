# AA.AZ.DEPOSIT — Table Schema

> Source: `INSERTS/I_F.AA.AZ.DEPOSIT` in `AA_ClassicProducts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AZD.ACTIVITY` | `AaArrAzDeposit_Activity` |  |  |  |
| 2 | `AA.AZD.ACTION` | `AaArrAzDeposit_Action` |  |  |  |
| 3 | `AA.AZD.MULTI` | `AaArrAzDeposit_Multi` |  |  |  |
| 4 | `AA.AZD.OD.CATEGORY` | `AaArrAzDeposit_OdCategory` |  |  |  |
| 5 | `AA.AZD.PART.REDEMPTION` | `AaArrAzDeposit_PartRedemption` |  |  |  |
| 6 | `AA.AZD.ROLL.MAT.WRK.DAY` | `AaArrAzDeposit_RollMatWrkDay` |  |  |  |
| 7 | `AA.AZD.PI.TABLE.TO.USE` | `AaArrAzDeposit_PiTableToUse` |  |  |  |
| 8 | `AA.AZD.EARLY.RED.MARGIN` | `AaArrAzDeposit_EarlyRedMargin` |  |  |  |
| 9 | `AA.AZD.PASSBOOK.ID` | `AaArrAzDeposit_PassbookId` |  |  |  |
| 10 | `AA.AZD.CREATE.TD.FOR.INT` | `AaArrAzDeposit_CreateTdForInt` |  |  |  |
| 11 | `AA.AZD.PAY.INT.AT.MAT` | `AaArrAzDeposit_PayIntAtMat` |  |  |  |
| 12 | `AA.AZD.MATURITY.INSTR` | `AaArrAzDeposit_MaturityInstr` |  |  |  |
| 13 | `AA.AZD.ROLLOVER.ACCTNG` | `AaArrAzDeposit_RolloverAcctng` |  |  |  |
| 14 | `AA.AZD.PRE.CLOSE.RTN` | `AaArrAzDeposit_PreCloseRtn` |  |  |  |
| 15 | `AA.AZD.MIN.CREDIT.BAL` | `AaArrAzDeposit_MinCreditBal` |  |  |  |
| 16 | `AA.AZD.REPAYMENT.TYPE` | `AaArrAzDeposit_RepaymentType` |  |  |  |
| 17 | `AA.AZD.SINGLE.LIMIT` | `AaArrAzDeposit_SingleLimit` |  |  |  |
| 18 | `AA.AZD.PRE.CLOSURE.FEE` | `AaArrAzDeposit_PreClosureFee` |  |  |  |
| 19 | `AA.AZD.CR.INT.FQU` | `AaArrAzDeposit_CrIntFqu` |  |  |  |
| 20 | `AA.AZD.CR.INT.TYPE` | `AaArrAzDeposit_CrIntType` |  |  |  |
| 21 | `AA.AZD.CR.DEP.FQU` | `AaArrAzDeposit_CrDepFqu` |  |  |  |
| 22 | `AA.AZD.RESCHED.TYPE` | `AaArrAzDeposit_ReschedType` |  |  |  |
| 23 | `AA.AZD.RESCHED.NOTICE` | `AaArrAzDeposit_ReschedNotice` |  |  |  |
| 24 | `AA.AZD.RESERVED1` | `AaArrAzDeposit_Reserved1` |  |  |  |
| 25 | `AA.AZD.LOCAL.REF` | `AaArrAzDeposit_LocalRef` |  |  |  |
| 26 | `AA.AZD.PR.ATTRIBUTE` | `AaArrAzDeposit_PrAttribute` |  |  |  |
| 27 | `AA.AZD.PR.VALUE` | `AaArrAzDeposit_PrValue` |  |  |  |
| 28 | `AA.AZD.PR.BRK.RES` | `AaArrAzDeposit_PrBrkRes` |  |  |  |
| 29 | `AA.AZD.PR.BRK.MSG` | `AaArrAzDeposit_PrBrkMsg` |  |  |  |
| 30 | `AA.AZD.PR.BRK.CHARGE` | `AaArrAzDeposit_PrBrkCharge` |  |  |  |
| 31 | `AA.AZD.PR.RESERVED.3` | `AaArrAzDeposit_PrReserved3` |  |  |  |
| 32 | `AA.AZD.PR.RESERVED.2` | `AaArrAzDeposit_PrReserved2` |  |  |  |
| 33 | `AA.AZD.PR.RESERVED.1` | `AaArrAzDeposit_PrReserved1` |  |  |  |
| 34 | `AA.AZD.PR.APP.METHOD` | `AaArrAzDeposit_PrAppMethod` |  |  |  |
| 35 | `AA.AZD.PR.APP.PERIOD` | `AaArrAzDeposit_PrAppPeriod` |  |  |  |
| 36 | `AA.AZD.SYS.RESERVE7` | `AaArrAzDeposit_SysReserve7` |  |  |  |
| 37 | `AA.AZD.SYS.RESERVE6` | `AaArrAzDeposit_SysReserve6` |  |  |  |
| 38 | `AA.AZD.OWNING.COMPANY` | `AaArrAzDeposit_OwningCompany` |  |  |  |
| 39 | `AA.AZD.API.ATTRIBUTE` | `AaArrAzDeposit_ApiAttribute` |  |  |  |
| 40 | `AA.AZD.SYS.RESERVE3` | `AaArrAzDeposit_SysReserve3` |  |  |  |
| 41 | `AA.AZD.SYS.RESERVE2` | `AaArrAzDeposit_SysReserve2` |  |  |  |
| 42 | `AA.AZD.SYS.RESERVE1` | `AaArrAzDeposit_SysReserve1` |  |  |  |
| 43 | `AA.AZD.DEFAULT.ATTR.OPTION` | `AaArrAzDeposit_DefaultAttrOption` |  |  |  |
| 44 | `AA.AZD.DEFAULT.NEGOTIABLE` | `AaArrAzDeposit_DefaultNegotiable` |  |  |  |
| 45 | `AA.AZD.NR.ATTRIBUTE` | `AaArrAzDeposit_NrAttribute` |  |  |  |
| 46 | `AA.AZD.NR.OPTIONS` | `AaArrAzDeposit_NrOptions` |  |  |  |
| 47 | `AA.AZD.NR.RESERVED2` | `AaArrAzDeposit_NrReserved2` |  |  |  |
| 48 | `AA.AZD.NR.RESERVED1` | `AaArrAzDeposit_NrReserved1` |  |  |  |
| 49 | `AA.AZD.NR.STD.COMP` | `AaArrAzDeposit_NrStdComp` |  |  |  |
| 50 | `AA.AZD.NR.TYPE` | `AaArrAzDeposit_NrType` |  |  |  |
| 51 | `AA.AZD.NR.VALUE` | `AaArrAzDeposit_NrValue` |  |  |  |
| 52 | `AA.AZD.NR.MESSAGE` | `AaArrAzDeposit_NrMessage` |  |  |  |
| 53 | `AA.AZD.CHANGED.FIELDS` | `AaArrAzDeposit_ChangedFields` |  |  |  |
| 54 | `AA.AZD.NEGOTIATED.FLDS` | `AaArrAzDeposit_NegotiatedFlds` |  |  |  |
| 55 | `AA.AZD.ID.COMP.1` | `AaArrAzDeposit_IdComp1` |  |  |  |
| 56 | `AA.AZD.ID.COMP.2` | `AaArrAzDeposit_IdComp2` |  |  |  |
| 57 | `AA.AZD.ID.COMP.3` | `AaArrAzDeposit_IdComp3` |  |  |  |
| 58 | `AA.AZD.ID.COMP.4` | `AaArrAzDeposit_IdComp4` |  |  |  |
| 59 | `AA.AZD.ID.COMP.5` | `AaArrAzDeposit_IdComp5` |  |  |  |
| 60 | `AA.AZD.ID.COMP.6` | `AaArrAzDeposit_IdComp6` |  |  |  |
| 61 | `AA.AZD.RESERVED2.ID` | `AaArrAzDeposit_Reserved2Id` |  |  |  |
| 62 | `AA.AZD.TARGET.PRODUCT` | `AaArrAzDeposit_TargetProduct` |  |  |  |
| 63 | `AA.AZD.STMT.NOS` | `AaArrAzDeposit_StmtNos` |  |  |  |
| 64 | `AA.AZD.OVERRIDE` | `AaArrAzDeposit_Override` |  |  |  |
| 65 | `AA.AZD.RECORD.STATUS` | `AaArrAzDeposit_RecordStatus` |  |  |  |
| 66 | `AA.AZD.CURR.NO` | `AaArrAzDeposit_CurrNo` |  |  |  |
| 67 | `AA.AZD.INPUTTER` | `AaArrAzDeposit_Inputter` |  |  |  |
| 68 | `AA.AZD.DATE.TIME` | `AaArrAzDeposit_DateTime` |  |  |  |
| 69 | `AA.AZD.AUTHORISER` | `AaArrAzDeposit_Authoriser` |  |  |  |
| 70 | `AA.AZD.CO.CODE` | `AaArrAzDeposit_CoCode` |  |  |  |
| 71 | `AA.AZD.DEPT.CODE` | `AaArrAzDeposit_DeptCode` |  |  |  |
| 72 | `AA.AZD.AUDITOR.CODE` | `AaArrAzDeposit_AuditorCode` |  |  |  |
| 73 | `AA.AZD.AUDIT.DATE.TIME` | `AaArrAzDeposit_AuditDateTime` |  |  |  |
