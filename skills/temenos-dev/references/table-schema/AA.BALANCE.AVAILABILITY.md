# AA.BALANCE.AVAILABILITY — Table Schema

> Source: `INSERTS/I_F.AA.BALANCE.AVAILABILITY` in `AA_BalanceAvailability.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.BA.ACTIVITY` | `AaSimBalanceAvailability_Activity` |  |  |  |
| 2 | `AA.BA.ACTION` | `AaSimBalanceAvailability_Action` |  |  |  |
| 3 | `AA.BA.NOTICE.AMOUNT` | `AaSimBalanceAvailability_NoticeAmount` |  |  |  |
| 4 | `AA.BA.NOTICE.PERIOD` | `AaSimBalanceAvailability_NoticePeriod` |  |  |  |
| 5 | `AA.BA.NOTICE.AVAILABILITY` | `AaSimBalanceAvailability_NoticeAvailability` |  |  |  |
| 6 | `AA.BA.CREDIT.CHECK` | `AaSimBalanceAvailability_CreditCheck` |  |  |  |
| 7 | `AA.BA.AVAIL.BAL.UPD` | `AaSimBalanceAvailability_AvailBalUpd` |  |  |  |
| 8 | `AA.BA.TOLERANCE.AMOUNT` | `AaSimBalanceAvailability_ToleranceAmount` |  |  |  |
| 9 | `AA.BA.TOLERANCE.CCY` | `AaSimBalanceAvailability_ToleranceCcy` |  |  |  |
| 10 | `AA.BA.ACTIVITY.CLASS` | `AaSimBalanceAvailability_ActivityClass` |  |  |  |
| 11 | `AA.BA.ON.ACTIVITY` | `AaSimBalanceAvailability_OnActivity` |  |  |  |
| 12 | `AA.BA.ACT.CREDIT.CHECK` | `AaSimBalanceAvailability_ActCreditCheck` |  |  |  |
| 13 | `AA.BA.LIMIT.CHECK` | `AaSimBalanceAvailability_LimitCheck` |  |  |  |
| 14 | `AA.BA.OVERDRAWN.ACTION` | `AaSimBalanceAvailability_OverdrawnAction` |  |  |  |
| 15 | `AA.BA.OD.CHARGE.ACTION` | `AaSimBalanceAvailability_OdChargeAction` |  |  |  |
| 16 | `AA.BA.OD.CHARGE.REV.ACTION` | `AaSimBalanceAvailability_OdChargeRevAction` |  |  |  |
| 17 | `AA.BA.OVERDRAFT.PROCESSING` | `AaSimBalanceAvailability_OverdraftProcessing` |  |  |  |
| 18 | `AA.BA.LOCAL.REF` | `AaSimBalanceAvailability_LocalRef` |  |  |  |
| 19 | `AA.BA.PR.ATTRIBUTE` | `AaSimBalanceAvailability_PrAttribute` |  |  |  |
| 20 | `AA.BA.PR.VALUE` | `AaSimBalanceAvailability_PrValue` |  |  |  |
| 21 | `AA.BA.PR.BRK.RES` | `AaSimBalanceAvailability_PrBrkRes` |  |  |  |
| 22 | `AA.BA.PR.BRK.MSG` | `AaSimBalanceAvailability_PrBrkMsg` |  |  |  |
| 23 | `AA.BA.PR.BRK.CHARGE` | `AaSimBalanceAvailability_PrBrkCharge` |  |  |  |
| 24 | `AA.BA.PR.RESERVED.3` | `AaSimBalanceAvailability_PrReserved3` |  |  |  |
| 25 | `AA.BA.PR.RESERVED.2` | `AaSimBalanceAvailability_PrReserved2` |  |  |  |
| 26 | `AA.BA.PR.RESERVED.1` | `AaSimBalanceAvailability_PrReserved1` |  |  |  |
| 27 | `AA.BA.PR.APP.METHOD` | `AaSimBalanceAvailability_PrAppMethod` |  |  |  |
| 28 | `AA.BA.PR.APP.PERIOD` | `AaSimBalanceAvailability_PrAppPeriod` |  |  |  |
| 29 | `AA.BA.SYS.RESERVE7` | `AaSimBalanceAvailability_SysReserve7` |  |  |  |
| 30 | `AA.BA.SYS.RESERVE6` | `AaSimBalanceAvailability_SysReserve6` |  |  |  |
| 31 | `AA.BA.OWNING.COMPANY` | `AaSimBalanceAvailability_OwningCompany` |  |  |  |
| 32 | `AA.BA.API.ATTRIBUTE` | `AaSimBalanceAvailability_ApiAttribute` |  |  |  |
| 33 | `AA.BA.SYS.RESERVE3` | `AaSimBalanceAvailability_SysReserve3` |  |  |  |
| 34 | `AA.BA.SYS.RESERVE2` | `AaSimBalanceAvailability_SysReserve2` |  |  |  |
| 35 | `AA.BA.SYS.RESERVE1` | `AaSimBalanceAvailability_SysReserve1` |  |  |  |
| 36 | `AA.BA.DEFAULT.ATTR.OPTION` | `AaSimBalanceAvailability_DefaultAttrOption` |  |  |  |
| 37 | `AA.BA.DEFAULT.NEGOTIABLE` | `AaSimBalanceAvailability_DefaultNegotiable` |  |  |  |
| 38 | `AA.BA.NR.ATTRIBUTE` | `AaSimBalanceAvailability_NrAttribute` |  |  |  |
| 39 | `AA.BA.NR.OPTIONS` | `AaSimBalanceAvailability_NrOptions` |  |  |  |
| 40 | `AA.BA.NR.ATTRIBUTE.RULE` | `AaSimBalanceAvailability_NrAttributeRule` |  |  |  |
| 41 | `AA.BA.NR.VALUE.SOURCE` | `AaSimBalanceAvailability_NrValueSource` |  |  |  |
| 42 | `AA.BA.NR.STD.COMP` | `AaSimBalanceAvailability_NrStdComp` |  |  |  |
| 43 | `AA.BA.NR.TYPE` | `AaSimBalanceAvailability_NrType` |  |  |  |
| 44 | `AA.BA.NR.VALUE` | `AaSimBalanceAvailability_NrValue` |  |  |  |
| 45 | `AA.BA.NR.MESSAGE` | `AaSimBalanceAvailability_NrMessage` |  |  |  |
| 46 | `AA.BA.CHANGED.FIELDS` | `AaSimBalanceAvailability_ChangedFields` |  |  |  |
| 47 | `AA.BA.NEGOTIATED.FLDS` | `AaSimBalanceAvailability_NegotiatedFlds` |  |  |  |
| 48 | `AA.BA.ID.COMP.1` | `AaSimBalanceAvailability_IdComp1` |  |  |  |
| 49 | `AA.BA.ID.COMP.2` | `AaSimBalanceAvailability_IdComp2` |  |  |  |
| 50 | `AA.BA.ID.COMP.3` | `AaSimBalanceAvailability_IdComp3` |  |  |  |
| 51 | `AA.BA.ID.COMP.4` | `AaSimBalanceAvailability_IdComp4` |  |  |  |
| 52 | `AA.BA.ID.COMP.5` | `AaSimBalanceAvailability_IdComp5` |  |  |  |
| 53 | `AA.BA.ID.COMP.6` | `AaSimBalanceAvailability_IdComp6` |  |  |  |
| 54 | `AA.BA.RESERVED2.ID` | `AaSimBalanceAvailability_Reserved2Id` |  |  |  |
| 55 | `AA.BA.TARGET.PRODUCT` | `AaSimBalanceAvailability_TargetProduct` |  |  |  |
| 56 | `AA.BA.STMT.NOS` | `AaSimBalanceAvailability_StmtNos` |  |  |  |
| 57 | `AA.BA.OVERRIDE` | `AaSimBalanceAvailability_Override` |  |  |  |
| 58 | `AA.BA.RECORD.STATUS` | `AaSimBalanceAvailability_RecordStatus` |  |  |  |
| 59 | `AA.BA.CURR.NO` | `AaSimBalanceAvailability_CurrNo` |  |  |  |
| 60 | `AA.BA.INPUTTER` | `AaSimBalanceAvailability_Inputter` |  |  |  |
| 61 | `AA.BA.DATE.TIME` | `AaSimBalanceAvailability_DateTime` |  |  |  |
| 62 | `AA.BA.AUTHORISER` | `AaSimBalanceAvailability_Authoriser` |  |  |  |
| 63 | `AA.BA.CO.CODE` | `AaSimBalanceAvailability_CoCode` |  |  |  |
| 64 | `AA.BA.DEPT.CODE` | `AaSimBalanceAvailability_DeptCode` |  |  |  |
| 65 | `AA.BA.AUDITOR.CODE` | `AaSimBalanceAvailability_AuditorCode` |  |  |  |
| 66 | `AA.BA.AUDIT.DATE.TIME` | `AaSimBalanceAvailability_AuditDateTime` |  |  |  |
| 67 | `AA.BA.USE.LIMIT` | `AaSimBalanceAvailability_UseLimit` |  |  |  |
| 68 | `AA.BA.NOTICE.ACCOUNT` | `AaSimBalanceAvailability_NoticeAccount` |  |  |  |
| 69 | `AA.BA.CC.COM.CURRENCY` | `AaSimBalanceAvailability_CcComCurrency` |  |  |  |
| 70 | `AA.BA.CC.COM.MAXIMUM` | `AaSimBalanceAvailability_CcComMaximum` |  |  |  |
| 71 | `AA.BA.CC.COM.MINIMUM` | `AaSimBalanceAvailability_CcComMinimum` |  |  |  |
| 72 | `AA.BA.POSITION.ADJUSTMENT` | `AaSimBalanceAvailability_PositionAdjustment` |  |  |  |
| 73 | `AA.BA.ADJUSTMENT.ORDER` | `AaSimBalanceAvailability_AdjustmentOrder` |  |  |  |
| 74 | `AA.BA.NOTICE.CONVENTION` | `AaSimBalanceAvailability_NoticeConvention` |  |  |  |
| 75 | `AA.BA.INCLUDE.LIMIT` | `AaSimBalanceAvailability_IncludeLimit` |  |  |  |
| 76 | `AA.BA.PERIOD.TYPE` | `AaSimBalanceAvailability_PeriodType` |  |  |  |
