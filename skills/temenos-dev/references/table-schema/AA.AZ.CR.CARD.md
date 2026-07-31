# AA.AZ.CR.CARD — Table Schema

> Source: `INSERTS/I_F.AA.AZ.CR.CARD` in `AA_ClassicProducts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AZC.ACTIVITY` | `AaArrAzCrCard_Activity` |  |  |  |
| 2 | `AA.AZC.ACTION` | `AaArrAzCrCard_Action` |  |  |  |
| 3 | `AA.AZC.MULTI` | `AaArrAzCrCard_Multi` |  |  |  |
| 4 | `AA.AZC.CARD.TYPE` | `AaArrAzCrCard_CardType` |  |  |  |
| 5 | `AA.AZC.APPROPRIATE.TYPE` | `AaArrAzCrCard_AppropriateType` |  |  |  |
| 6 | `AA.AZC.REVOLVING.RATIO` | `AaArrAzCrCard_RevolvingRatio` |  |  |  |
| 7 | `AA.AZC.HIGHEST.RANGE` | `AaArrAzCrCard_HighestRange` |  |  |  |
| 8 | `AA.AZC.AMT.PERCENT` | `AaArrAzCrCard_AmtPercent` |  |  |  |
| 9 | `AA.AZC.CC.PR.GRACE.PERIOD` | `AaArrAzCrCard_CcPrGracePeriod` |  |  |  |
| 10 | `AA.AZC.CREATE.PD.EOD` | `AaArrAzCrCard_CreatePdEod` |  |  |  |
| 11 | `AA.AZC.PD.LINK.MAIN.AZ` | `AaArrAzCrCard_PdLinkMainAz` |  |  |  |
| 12 | `AA.AZC.CC.AMT.RTN` | `AaArrAzCrCard_CcAmtRtn` |  |  |  |
| 13 | `AA.AZC.RESERVED2` | `AaArrAzCrCard_Reserved2` |  |  |  |
| 14 | `AA.AZC.RESERVED1` | `AaArrAzCrCard_Reserved1` |  |  |  |
| 15 | `AA.AZC.LOCAL.REF` | `AaArrAzCrCard_LocalRef` |  |  |  |
| 16 | `AA.AZC.PR.ATTRIBUTE` | `AaArrAzCrCard_PrAttribute` |  |  |  |
| 17 | `AA.AZC.PR.VALUE` | `AaArrAzCrCard_PrValue` |  |  |  |
| 18 | `AA.AZC.PR.BRK.RES` | `AaArrAzCrCard_PrBrkRes` |  |  |  |
| 19 | `AA.AZC.PR.BRK.MSG` | `AaArrAzCrCard_PrBrkMsg` |  |  |  |
| 20 | `AA.AZC.PR.BRK.CHARGE` | `AaArrAzCrCard_PrBrkCharge` |  |  |  |
| 21 | `AA.AZC.PR.RESERVED.3` | `AaArrAzCrCard_PrReserved3` |  |  |  |
| 22 | `AA.AZC.PR.RESERVED.2` | `AaArrAzCrCard_PrReserved2` |  |  |  |
| 23 | `AA.AZC.PR.RESERVED.1` | `AaArrAzCrCard_PrReserved1` |  |  |  |
| 24 | `AA.AZC.PR.APP.METHOD` | `AaArrAzCrCard_PrAppMethod` |  |  |  |
| 25 | `AA.AZC.PR.APP.PERIOD` | `AaArrAzCrCard_PrAppPeriod` |  |  |  |
| 26 | `AA.AZC.SYS.RESERVE7` | `AaArrAzCrCard_SysReserve7` |  |  |  |
| 27 | `AA.AZC.SYS.RESERVE6` | `AaArrAzCrCard_SysReserve6` |  |  |  |
| 28 | `AA.AZC.OWNING.COMPANY` | `AaArrAzCrCard_OwningCompany` |  |  |  |
| 29 | `AA.AZC.API.ATTRIBUTE` | `AaArrAzCrCard_ApiAttribute` |  |  |  |
| 30 | `AA.AZC.SYS.RESERVE3` | `AaArrAzCrCard_SysReserve3` |  |  |  |
| 31 | `AA.AZC.SYS.RESERVE2` | `AaArrAzCrCard_SysReserve2` |  |  |  |
| 32 | `AA.AZC.SYS.RESERVE1` | `AaArrAzCrCard_SysReserve1` |  |  |  |
| 33 | `AA.AZC.DEFAULT.ATTR.OPTION` | `AaArrAzCrCard_DefaultAttrOption` |  |  |  |
| 34 | `AA.AZC.DEFAULT.NEGOTIABLE` | `AaArrAzCrCard_DefaultNegotiable` |  |  |  |
| 35 | `AA.AZC.NR.ATTRIBUTE` | `AaArrAzCrCard_NrAttribute` |  |  |  |
| 36 | `AA.AZC.NR.OPTIONS` | `AaArrAzCrCard_NrOptions` |  |  |  |
| 37 | `AA.AZC.NR.RESERVED2` | `AaArrAzCrCard_NrReserved2` |  |  |  |
| 38 | `AA.AZC.NR.RESERVED1` | `AaArrAzCrCard_NrReserved1` |  |  |  |
| 39 | `AA.AZC.NR.STD.COMP` | `AaArrAzCrCard_NrStdComp` |  |  |  |
| 40 | `AA.AZC.NR.TYPE` | `AaArrAzCrCard_NrType` |  |  |  |
| 41 | `AA.AZC.NR.VALUE` | `AaArrAzCrCard_NrValue` |  |  |  |
| 42 | `AA.AZC.NR.MESSAGE` | `AaArrAzCrCard_NrMessage` |  |  |  |
| 43 | `AA.AZC.CHANGED.FIELDS` | `AaArrAzCrCard_ChangedFields` |  |  |  |
| 44 | `AA.AZC.NEGOTIATED.FLDS` | `AaArrAzCrCard_NegotiatedFlds` |  |  |  |
| 45 | `AA.AZC.ID.COMP.1` | `AaArrAzCrCard_IdComp1` |  |  |  |
| 46 | `AA.AZC.ID.COMP.2` | `AaArrAzCrCard_IdComp2` |  |  |  |
| 47 | `AA.AZC.ID.COMP.3` | `AaArrAzCrCard_IdComp3` |  |  |  |
| 48 | `AA.AZC.ID.COMP.4` | `AaArrAzCrCard_IdComp4` |  |  |  |
| 49 | `AA.AZC.ID.COMP.5` | `AaArrAzCrCard_IdComp5` |  |  |  |
| 50 | `AA.AZC.ID.COMP.6` | `AaArrAzCrCard_IdComp6` |  |  |  |
| 51 | `AA.AZC.RESERVED2.ID` | `AaArrAzCrCard_Reserved2Id` |  |  |  |
| 52 | `AA.AZC.TARGET.PRODUCT` | `AaArrAzCrCard_TargetProduct` |  |  |  |
| 53 | `AA.AZC.STMT.NOS` | `AaArrAzCrCard_StmtNos` |  |  |  |
| 54 | `AA.AZC.OVERRIDE` | `AaArrAzCrCard_Override` |  |  |  |
| 55 | `AA.AZC.RECORD.STATUS` | `AaArrAzCrCard_RecordStatus` |  |  |  |
| 56 | `AA.AZC.CURR.NO` | `AaArrAzCrCard_CurrNo` |  |  |  |
| 57 | `AA.AZC.INPUTTER` | `AaArrAzCrCard_Inputter` |  |  |  |
| 58 | `AA.AZC.DATE.TIME` | `AaArrAzCrCard_DateTime` |  |  |  |
| 59 | `AA.AZC.AUTHORISER` | `AaArrAzCrCard_Authoriser` |  |  |  |
| 60 | `AA.AZC.CO.CODE` | `AaArrAzCrCard_CoCode` |  |  |  |
| 61 | `AA.AZC.DEPT.CODE` | `AaArrAzCrCard_DeptCode` |  |  |  |
| 62 | `AA.AZC.AUDITOR.CODE` | `AaArrAzCrCard_AuditorCode` |  |  |  |
| 63 | `AA.AZC.AUDIT.DATE.TIME` | `AaArrAzCrCard_AuditDateTime` |  |  |  |
