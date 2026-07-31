# AA.AZ.SAVINGS — Table Schema

> Source: `INSERTS/I_F.AA.AZ.SAVINGS` in `AA_ClassicProducts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AZS.ACTIVITY` | `AaArrAzSavings_Activity` |  |  |  |
| 2 | `AA.AZS.ACTION` | `AaArrAzSavings_Action` |  |  |  |
| 3 | `AA.AZS.CREDIT.AMT.MULTI` | `AaArrAzSavings_CreditAmtMulti` |  |  |  |
| 4 | `AA.AZS.BONUS.PREMIUM` | `AaArrAzSavings_BonusPremium` |  |  |  |
| 5 | `AA.AZS.LATE.PYMT.FEE` | `AaArrAzSavings_LatePymtFee` |  |  |  |
| 6 | `AA.AZS.LIAB.TO.PENALTY` | `AaArrAzSavings_LiabToPenalty` |  |  |  |
| 7 | `AA.AZS.PENALTY.COLL.AT` | `AaArrAzSavings_PenaltyCollAt` |  |  |  |
| 8 | `AA.AZS.BONUS.ON` | `AaArrAzSavings_BonusOn` |  |  |  |
| 9 | `AA.AZS.BONUS.ON.ARREARS` | `AaArrAzSavings_BonusOnArrears` |  |  |  |
| 10 | `AA.AZS.RESERVED5` | `AaArrAzSavings_Reserved5` |  |  |  |
| 11 | `AA.AZS.RESERVED4` | `AaArrAzSavings_Reserved4` |  |  |  |
| 12 | `AA.AZS.RESERVED3` | `AaArrAzSavings_Reserved3` |  |  |  |
| 13 | `AA.AZS.RESERVED2` | `AaArrAzSavings_Reserved2` |  |  |  |
| 14 | `AA.AZS.RESERVED1` | `AaArrAzSavings_Reserved1` |  |  |  |
| 15 | `AA.AZS.LOCAL.REF` | `AaArrAzSavings_LocalRef` |  |  |  |
| 16 | `AA.AZS.PR.ATTRIBUTE` | `AaArrAzSavings_PrAttribute` |  |  |  |
| 17 | `AA.AZS.PR.VALUE` | `AaArrAzSavings_PrValue` |  |  |  |
| 18 | `AA.AZS.PR.BRK.RES` | `AaArrAzSavings_PrBrkRes` |  |  |  |
| 19 | `AA.AZS.PR.BRK.MSG` | `AaArrAzSavings_PrBrkMsg` |  |  |  |
| 20 | `AA.AZS.PR.BRK.CHARGE` | `AaArrAzSavings_PrBrkCharge` |  |  |  |
| 21 | `AA.AZS.PR.RESERVED.3` | `AaArrAzSavings_PrReserved3` |  |  |  |
| 22 | `AA.AZS.PR.RESERVED.2` | `AaArrAzSavings_PrReserved2` |  |  |  |
| 23 | `AA.AZS.PR.RESERVED.1` | `AaArrAzSavings_PrReserved1` |  |  |  |
| 24 | `AA.AZS.PR.APP.METHOD` | `AaArrAzSavings_PrAppMethod` |  |  |  |
| 25 | `AA.AZS.PR.APP.PERIOD` | `AaArrAzSavings_PrAppPeriod` |  |  |  |
| 26 | `AA.AZS.SYS.RESERVE7` | `AaArrAzSavings_SysReserve7` |  |  |  |
| 27 | `AA.AZS.SYS.RESERVE6` | `AaArrAzSavings_SysReserve6` |  |  |  |
| 28 | `AA.AZS.OWNING.COMPANY` | `AaArrAzSavings_OwningCompany` |  |  |  |
| 29 | `AA.AZS.API.ATTRIBUTE` | `AaArrAzSavings_ApiAttribute` |  |  |  |
| 30 | `AA.AZS.SYS.RESERVE3` | `AaArrAzSavings_SysReserve3` |  |  |  |
| 31 | `AA.AZS.SYS.RESERVE2` | `AaArrAzSavings_SysReserve2` |  |  |  |
| 32 | `AA.AZS.SYS.RESERVE1` | `AaArrAzSavings_SysReserve1` |  |  |  |
| 33 | `AA.AZS.DEFAULT.ATTR.OPTION` | `AaArrAzSavings_DefaultAttrOption` |  |  |  |
| 34 | `AA.AZS.DEFAULT.NEGOTIABLE` | `AaArrAzSavings_DefaultNegotiable` |  |  |  |
| 35 | `AA.AZS.NR.ATTRIBUTE` | `AaArrAzSavings_NrAttribute` |  |  |  |
| 36 | `AA.AZS.NR.OPTIONS` | `AaArrAzSavings_NrOptions` |  |  |  |
| 37 | `AA.AZS.NR.RESERVED2` | `AaArrAzSavings_NrReserved2` |  |  |  |
| 38 | `AA.AZS.NR.RESERVED1` | `AaArrAzSavings_NrReserved1` |  |  |  |
| 39 | `AA.AZS.NR.STD.COMP` | `AaArrAzSavings_NrStdComp` |  |  |  |
| 40 | `AA.AZS.NR.TYPE` | `AaArrAzSavings_NrType` |  |  |  |
| 41 | `AA.AZS.NR.VALUE` | `AaArrAzSavings_NrValue` |  |  |  |
| 42 | `AA.AZS.NR.MESSAGE` | `AaArrAzSavings_NrMessage` |  |  |  |
| 43 | `AA.AZS.CHANGED.FIELDS` | `AaArrAzSavings_ChangedFields` |  |  |  |
| 44 | `AA.AZS.NEGOTIATED.FLDS` | `AaArrAzSavings_NegotiatedFlds` |  |  |  |
| 45 | `AA.AZS.ID.COMP.1` | `AaArrAzSavings_IdComp1` |  |  |  |
| 46 | `AA.AZS.ID.COMP.2` | `AaArrAzSavings_IdComp2` |  |  |  |
| 47 | `AA.AZS.ID.COMP.3` | `AaArrAzSavings_IdComp3` |  |  |  |
| 48 | `AA.AZS.ID.COMP.4` | `AaArrAzSavings_IdComp4` |  |  |  |
| 49 | `AA.AZS.ID.COMP.5` | `AaArrAzSavings_IdComp5` |  |  |  |
| 50 | `AA.AZS.ID.COMP.6` | `AaArrAzSavings_IdComp6` |  |  |  |
| 51 | `AA.AZS.RESERVED2.ID` | `AaArrAzSavings_Reserved2Id` |  |  |  |
| 52 | `AA.AZS.TARGET.PRODUCT` | `AaArrAzSavings_TargetProduct` |  |  |  |
| 53 | `AA.AZS.STMT.NOS` | `AaArrAzSavings_StmtNos` |  |  |  |
| 54 | `AA.AZS.OVERRIDE` | `AaArrAzSavings_Override` |  |  |  |
| 55 | `AA.AZS.RECORD.STATUS` | `AaArrAzSavings_RecordStatus` |  |  |  |
| 56 | `AA.AZS.CURR.NO` | `AaArrAzSavings_CurrNo` |  |  |  |
| 57 | `AA.AZS.INPUTTER` | `AaArrAzSavings_Inputter` |  |  |  |
| 58 | `AA.AZS.DATE.TIME` | `AaArrAzSavings_DateTime` |  |  |  |
| 59 | `AA.AZS.AUTHORISER` | `AaArrAzSavings_Authoriser` |  |  |  |
| 60 | `AA.AZS.CO.CODE` | `AaArrAzSavings_CoCode` |  |  |  |
| 61 | `AA.AZS.DEPT.CODE` | `AaArrAzSavings_DeptCode` |  |  |  |
| 62 | `AA.AZS.AUDITOR.CODE` | `AaArrAzSavings_AuditorCode` |  |  |  |
| 63 | `AA.AZS.AUDIT.DATE.TIME` | `AaArrAzSavings_AuditDateTime` |  |  |  |
