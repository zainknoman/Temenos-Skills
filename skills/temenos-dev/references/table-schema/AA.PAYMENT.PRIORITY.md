# AA.PAYMENT.PRIORITY — Table Schema

> Source: `INSERTS/I_F.AA.PAYMENT.PRIORITY` in `AA_PaymentPriority.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PAYPRTY.ACTIVITY` | `AaPaymentPriority_Activity` |  |  |  |
| 2 | `AA.PAYPRTY.ACTION` | `AaPaymentPriority_Action` |  |  |  |
| 3 | `AA.PAYPRTY.APPLICATION.TYPE` | `AaPaymentPriority_ApplicationType` |  |  |  |
| 4 | `AA.PAYPRTY.RESERVED.3` | `AaPaymentPriority_Reserved3` |  |  |  |
| 5 | `AA.PAYPRTY.RESERVED.2` | `AaPaymentPriority_Reserved2` |  |  |  |
| 6 | `AA.PAYPRTY.RESERVED.1` | `AaPaymentPriority_Reserved1` |  |  |  |
| 7 | `AA.PAYPRTY.PRIORITY.RULE` | `AaPaymentPriority_PriorityRule` |  |  |  |
| 8 | `AA.PAYPRTY.PRIORITY.RULE.LIST` | `AaPaymentPriority_PriorityRuleList` |  |  |  |
| 9 | `AA.PAYPRTY.RESERVED.6` | `AaPaymentPriority_Reserved6` |  |  |  |
| 10 | `AA.PAYPRTY.RESERVED.5` | `AaPaymentPriority_Reserved5` |  |  |  |
| 11 | `AA.PAYPRTY.RESERVED.4` | `AaPaymentPriority_Reserved4` |  |  |  |
| 12 | `AA.PAYPRTY.REMAINDER.PAY.ACTIVITY` | `AaPaymentPriority_RemainderPayActivity` |  |  |  |
| 13 | `AA.PAYPRTY.ADVANCE.PAYMENT.METHOD` | `AaPaymentPriority_AdvancePaymentMethod` |  |  |  |
| 14 | `AA.PAYPRTY.ADVANCE.PAYMENT.RESTRICTION` | `AAPaymentPriority_AdvancePaymentRestriction` |  |  |  |
| 15 | `AA.PAYPRTY.RESERVED.9` | `AAPaymentPriority_Reserved9` |  |  |  |
| 16 | `AA.PAYPRTY.RESERVED.8` | `AAPaymentPriority_Reserved8` |  |  |  |
| 17 | `AA.PAYPRTY.RESERVED.7` | `AAPaymentPriority_Reserved7` |  |  |  |
| 18 | `AA.PAYPRTY.LOCAL.REF` | `AAPaymentPriority_LocalRef` |  |  |  |
| 19 | `AA.PAYPRTY.PR.ATTRIBUTE` | `AAPaymentPriority_PrAttribute` |  |  |  |
| 20 | `AA.PAYPRTY.PR.VALUE` | `AAPaymentPriority_PrValue` |  |  |  |
| 21 | `AA.PAYPRTY.PR.BRK.RES` | `AAPaymentPriority_PrBrkRes` |  |  |  |
| 22 | `AA.PAYPRTY.PR.BRK.MSG` | `AAPaymentPriority_PrBrkMsg` |  |  |  |
| 23 | `AA.PAYPRTY.PR.BRK.CHARGE` | `AAPaymentPriority_PrBrkCharge` |  |  |  |
| 24 | `AA.PAYPRTY.PR.RESERVED.3` | `AAPaymentPriority_PrReserved3` |  |  |  |
| 25 | `AA.PAYPRTY.PR.RESERVED.2` | `AAPaymentPriority_PrReserved2` |  |  |  |
| 26 | `AA.PAYPRTY.PR.RESERVED.1` | `AAPaymentPriority_PrReserved1` |  |  |  |
| 27 | `AA.PAYPRTY.PR.APP.METHOD` | `AAPaymentPriority_PrAppMethod` |  |  |  |
| 28 | `AA.PAYPRTY.PR.APP.PERIOD` | `AAPaymentPriority_PrAppPeriod` |  |  |  |
| 29 | `AA.PAYPRTY.SYS.RESERVE7` | `AAPaymentPriority_SysReserve7` |  |  |  |
| 30 | `AA.PAYPRTY.SYS.RESERVE6` | `AAPaymentPriority_SysReserve6` |  |  |  |
| 31 | `AA.PAYPRTY.OWNING.COMPANY` | `AAPaymentPriority_OwningCompany` |  |  |  |
| 32 | `AA.PAYPRTY.API.ATTRIBUTE` | `AAPaymentPriority_ApiAttribute` |  |  |  |
| 33 | `AA.PAYPRTY.SYS.RESERVE3` | `AAPaymentPriority_SysReserve3` |  |  |  |
| 34 | `AA.PAYPRTY.SYS.RESERVE2` | `AAPaymentPriority_SysReserve2` |  |  |  |
| 35 | `AA.PAYPRTY.SYS.RESERVE1` | `AAPaymentPriority_SysReserve1` |  |  |  |
| 36 | `AA.PAYPRTY.DEFAULT.ATTR.OPTION` | `AAPaymentPriority_DefaultAttrOption` |  |  |  |
| 37 | `AA.PAYPRTY.DEFAULT.NEGOTIABLE` | `AAPaymentPriority_DefaultNegotiable` |  |  |  |
| 38 | `AA.PAYPRTY.NR.ATTRIBUTE` | `AAPaymentPriority_NrAttribute` |  |  |  |
| 39 | `AA.PAYPRTY.NR.OPTIONS` | `AAPaymentPriority_NrOptions` |  |  |  |
| 40 | `AA.PAYPRTY.NR.ATTRIBUTE.RULE` | `AAPaymentPriority_NrAttributeRule` |  |  |  |
| 41 | `AA.PAYPRTY.NR.VALUE.SOURCE` | `AAPaymentPriority_NrValueSource` |  |  |  |
| 42 | `AA.PAYPRTY.NR.STD.COMP` | `AAPaymentPriority_NrStdComp` |  |  |  |
| 43 | `AA.PAYPRTY.NR.TYPE` | `AAPaymentPriority_NrType` |  |  |  |
| 44 | `AA.PAYPRTY.NR.VALUE` | `AAPaymentPriority_NrValue` |  |  |  |
| 45 | `AA.PAYPRTY.NR.MESSAGE` | `AAPaymentPriority_NrMessage` |  |  |  |
| 46 | `AA.PAYPRTY.CHANGED.FIELDS` | `AAPaymentPriority_ChangedFields` |  |  |  |
| 47 | `AA.PAYPRTY.NEGOTIATED.FLDS` | `AAPaymentPriority_NegotiatedFlds` |  |  |  |
| 48 | `AA.PAYPRTY.ID.COMP.1` | `AAPaymentPriority_IdComp1` |  |  |  |
| 49 | `AA.PAYPRTY.ID.COMP.2` | `AAPaymentPriority_IdComp2` |  |  |  |
| 50 | `AA.PAYPRTY.ID.COMP.3` | `AAPaymentPriority_IdComp3` |  |  |  |
| 51 | `AA.PAYPRTY.ID.COMP.4` | `AAPaymentPriority_IdComp4` |  |  |  |
| 52 | `AA.PAYPRTY.ID.COMP.5` | `AAPaymentPriority_IdComp5` |  |  |  |
| 53 | `AA.PAYPRTY.ID.COMP.6` | `AAPaymentPriority_IdComp6` |  |  |  |
| 54 | `AA.PAYPRTY.RESERVED2.ID` | `AAPaymentPriority_Reserved2Id` |  |  |  |
| 55 | `AA.PAYPRTY.TARGET.PRODUCT` | `AAPaymentPriority_TargetProduct` |  |  |  |
| 56 | `AA.PAYPRTY.STMT.NOS` | `AAPaymentPriority_StmtNos` |  |  |  |
| 57 | `AA.PAYPRTY.OVERRIDE` | `AAPaymentPriority_Override` |  |  |  |
| 58 | `AA.PAYPRTY.RECORD.STATUS` | `AAPaymentPriority_RecordStatus` |  |  |  |
| 59 | `AA.PAYPRTY.CURR.NO` | `AAPaymentPriority_CurrNo` |  |  |  |
| 60 | `AA.PAYPRTY.INPUTTER` | `AAPaymentPriority_Inputter` |  |  |  |
| 61 | `AA.PAYPRTY.DATE.TIME` | `AAPaymentPriority_DateTime` |  |  |  |
| 62 | `AA.PAYPRTY.AUTHORISER` | `AAPaymentPriority_Authoriser` |  |  |  |
| 63 | `AA.PAYPRTY.CO.CODE` | `AAPaymentPriority_CoCode` |  |  |  |
| 64 | `AA.PAYPRTY.DEPT.CODE` | `AAPaymentPriority_DeptCode` |  |  |  |
| 65 | `AA.PAYPRTY.AUDITOR.CODE` | `AAPaymentPriority_AuditorCode` |  |  |  |
| 66 | `AA.PAYPRTY.AUDIT.DATE.TIME` | `AAPaymentPriority_AuditDateTime` |  |  |  |
