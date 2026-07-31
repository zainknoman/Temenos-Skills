# AA.PAYMENT.HOLIDAY — Table Schema

> Source: `INSERTS/I_F.AA.PAYMENT.HOLIDAY` in `AA_PaymentHoliday.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PH.ACTIVITY` | `AaSimPaymentHoliday_Activity` |  |  |  |
| 2 | `AA.PH.ACTION` | `AaSimPaymentHoliday_Action` |  |  |  |
| 3 | `AA.PH.PAYMENT.DATE` | `AaSimPaymentHoliday_PaymentDate` |  |  |  |
| 4 | `AA.PH.BILL.TYPE` | `AaSimPaymentHoliday_BillType` |  |  |  |
| 5 | `AA.PH.PAYMENT.TYPE` | `AaSimPaymentHoliday_PaymentType` |  |  |  |
| 6 | `AA.PH.NEW.PAYMENT.AMOUNT` | `AaSimPaymentHoliday_NewPaymentAmount` |  |  |  |
| 7 | `AA.PH.NUMBER` | `AaSimPaymentHoliday_Number` |  |  |  |
| 8 | `AA.PH.RECALCULATION` | `AaSimPaymentHoliday_Recalculation` |  |  |  |
| 9 | `AA.PH.LOCAL.REF` | `AaSimPaymentHoliday_LocalRef` |  |  |  |
| 10 | `AA.PH.PR.ATTRIBUTE` | `AaSimPaymentHoliday_PrAttribute` |  |  |  |
| 11 | `AA.PH.PR.VALUE` | `AaSimPaymentHoliday_PrValue` |  |  |  |
| 12 | `AA.PH.PR.BRK.RES` | `AaSimPaymentHoliday_PrBrkRes` |  |  |  |
| 13 | `AA.PH.PR.BRK.MSG` | `AaSimPaymentHoliday_PrBrkMsg` |  |  |  |
| 14 | `AA.PH.PR.BRK.CHARGE` | `AaSimPaymentHoliday_PrBrkCharge` |  |  |  |
| 15 | `AA.PH.PR.RESERVED.3` | `AaSimPaymentHoliday_PrReserved3` |  |  |  |
| 16 | `AA.PH.PR.RESERVED.2` | `AaSimPaymentHoliday_PrReserved2` |  |  |  |
| 17 | `AA.PH.PR.RESERVED.1` | `AaSimPaymentHoliday_PrReserved1` |  |  |  |
| 18 | `AA.PH.PR.APP.METHOD` | `AaSimPaymentHoliday_PrAppMethod` |  |  |  |
| 19 | `AA.PH.PR.APP.PERIOD` | `AaSimPaymentHoliday_PrAppPeriod` |  |  |  |
| 20 | `AA.PH.SYS.RESERVE7` | `AaSimPaymentHoliday_SysReserve7` |  |  |  |
| 21 | `AA.PH.SYS.RESERVE6` | `AaSimPaymentHoliday_SysReserve6` |  |  |  |
| 22 | `AA.PH.OWNING.COMPANY` | `AaSimPaymentHoliday_OwningCompany` |  |  |  |
| 23 | `AA.PH.API.ATTRIBUTE` | `AaSimPaymentHoliday_ApiAttribute` |  |  |  |
| 24 | `AA.PH.SYS.RESERVE3` | `AaSimPaymentHoliday_SysReserve3` |  |  |  |
| 25 | `AA.PH.SYS.RESERVE2` | `AaSimPaymentHoliday_SysReserve2` |  |  |  |
| 26 | `AA.PH.SYS.RESERVE1` | `AaSimPaymentHoliday_SysReserve1` |  |  |  |
| 27 | `AA.PH.DEFAULT.ATTR.OPTION` | `AaSimPaymentHoliday_DefaultAttrOption` |  |  |  |
| 28 | `AA.PH.DEFAULT.NEGOTIABLE` | `AaSimPaymentHoliday_DefaultNegotiable` |  |  |  |
| 29 | `AA.PH.NR.ATTRIBUTE` | `AaSimPaymentHoliday_NrAttribute` |  |  |  |
| 30 | `AA.PH.NR.OPTIONS` | `AaSimPaymentHoliday_NrOptions` |  |  |  |
| 31 | `AA.PH.NR.ATTRIBUTE.RULE` | `AaSimPaymentHoliday_NrAttributeRule` |  |  |  |
| 32 | `AA.PH.NR.VALUE.SOURCE` | `AaSimPaymentHoliday_NrValueSource` |  |  |  |
| 33 | `AA.PH.NR.STD.COMP` | `AaSimPaymentHoliday_NrStdComp` |  |  |  |
| 34 | `AA.PH.NR.TYPE` | `AaSimPaymentHoliday_NrType` |  |  |  |
| 35 | `AA.PH.NR.VALUE` | `AaSimPaymentHoliday_NrValue` |  |  |  |
| 36 | `AA.PH.NR.MESSAGE` | `AaSimPaymentHoliday_NrMessage` |  |  |  |
| 37 | `AA.PH.CHANGED.FIELDS` | `AaSimPaymentHoliday_ChangedFields` |  |  |  |
| 38 | `AA.PH.NEGOTIATED.FLDS` | `AaSimPaymentHoliday_NegotiatedFlds` |  |  |  |
| 39 | `AA.PH.ID.COMP.1` | `AaSimPaymentHoliday_IdComp1` |  |  |  |
| 40 | `AA.PH.ID.COMP.2` | `AaSimPaymentHoliday_IdComp2` |  |  |  |
| 41 | `AA.PH.ID.COMP.3` | `AaSimPaymentHoliday_IdComp3` |  |  |  |
| 42 | `AA.PH.ID.COMP.4` | `AaSimPaymentHoliday_IdComp4` |  |  |  |
| 43 | `AA.PH.ID.COMP.5` | `AaSimPaymentHoliday_IdComp5` |  |  |  |
| 44 | `AA.PH.ID.COMP.6` | `AaSimPaymentHoliday_IdComp6` |  |  |  |
| 45 | `AA.PH.RESERVED2.ID` | `AaSimPaymentHoliday_Reserved2Id` |  |  |  |
| 46 | `AA.PH.TARGET.PRODUCT` | `AaSimPaymentHoliday_TargetProduct` |  |  |  |
| 47 | `AA.PH.STMT.NOS` | `AaSimPaymentHoliday_StmtNos` |  |  |  |
| 48 | `AA.PH.OVERRIDE` | `AaSimPaymentHoliday_Override` |  |  |  |
| 49 | `AA.PH.RECORD.STATUS` | `AaSimPaymentHoliday_RecordStatus` |  |  |  |
| 50 | `AA.PH.CURR.NO` | `AaSimPaymentHoliday_CurrNo` |  |  |  |
| 51 | `AA.PH.INPUTTER` | `AaSimPaymentHoliday_Inputter` |  |  |  |
| 52 | `AA.PH.DATE.TIME` | `AaSimPaymentHoliday_DateTime` |  |  |  |
| 53 | `AA.PH.AUTHORISER` | `AaSimPaymentHoliday_Authoriser` |  |  |  |
| 54 | `AA.PH.CO.CODE` | `AaSimPaymentHoliday_CoCode` |  |  |  |
| 55 | `AA.PH.DEPT.CODE` | `AaSimPaymentHoliday_DeptCode` |  |  |  |
| 56 | `AA.PH.AUDITOR.CODE` | `AaSimPaymentHoliday_AuditorCode` |  |  |  |
| 57 | `AA.PH.AUDIT.DATE.TIME` | `AaSimPaymentHoliday_AuditDateTime` |  |  |  |
| 58 | `AA.PH.HOLIDAY.DATE` | `AaSimPaymentHoliday_HolidayDate` |  |  |  |
| 59 | `AA.PH.ORIG.PAY.AMOUNT` | `AaSimPaymentHoliday_OrigPayAmount` |  |  |  |
| 60 | `AA.PH.HOLIDAY.PAY.AMOUNT` | `AaSimPaymentHoliday_HolidayPayAmount` |  |  |  |
| 61 | `AA.PH.CANCEL` | `AaSimPaymentHoliday_Cancel` |  |  |  |
| 62 | `AA.PH.REPAY.OPTION` | `AaSimPaymentHoliday_RepayOption` |  |  |  |
| 63 | `AA.PH.REPAY.PERIOD` | `AaSimPaymentHoliday_RepayPeriod` |  |  |  |
| 64 | `AA.PH.REFER.SETTLEMENT.TYPE` | `AaSimPaymentHoliday_ReferSettlementType` |  |  |  |
