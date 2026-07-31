# AA.PAYMENT.RULES — Table Schema

> Source: `INSERTS/I_F.AA.PAYMENT.RULES` in `AA_PaymentRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PAYRULE.ACTIVITY` | `AaSimPaymentRules_Activity` |  |  |  |
| 2 | `AA.PAYRULE.ACTION` | `AaSimPaymentRules_Action` |  |  |  |
| 3 | `AA.PAYRULE.FINANCIAL.STATUS` | `AaSimPaymentRules_FinancialStatus` |  |  |  |
| 4 | `AA.PAYRULE.APPLICATION.TYPE` | `AaSimPaymentRules_ApplicationType` |  |  |  |
| 5 | `AA.PAYRULE.APPLICATION.ORDER` | `AaSimPaymentRules_ApplicationOrder` |  |  |  |
| 6 | `AA.PAYRULE.TAX.SETTLEMENT` | `AaSimPaymentRules_TaxSettlement` |  |  |  |
| 7 | `AA.PAYRULE.REPAYMENT.ORDER` | `AaSimPaymentRules_RepaymentOrder` |  |  |  |
| 8 | `AA.PAYRULE.SEQUENCE` | `AaSimPaymentRules_Sequence` |  |  |  |
| 9 | `AA.PAYRULE.PROPERTY` | `AaSimPaymentRules_Property` |  |  |  |
| 10 | `AA.PAYRULE.BALANCE.TYPE` | `AaSimPaymentRules_BalanceType` |  |  |  |
| 11 | `AA.PAYRULE.PROP.APPL.TYPE` | `AaSimPaymentRules_PropApplType` |  |  |  |
| 12 | `AA.PAYRULE.PRE.BILL.ACTIVITY` | `AaSimPaymentRules_PreBillActivity` |  |  |  |
| 13 | `AA.PAYRULE.REMAINDER.ACTIVITY` | `AaSimPaymentRules_RemainderActivity` |  |  |  |
| 14 | `AA.PAYRULE.MAKE.BILL.DUE` | `AaSimPaymentRules_MakeBillDue` |  |  |  |
| 15 | `AA.PAYRULE.ADVANCE.PAYMENT.METHOD` | `AaSimPaymentRules_AdvancePaymentMethod` |  |  |  |
| 16 | `AA.PAYRULE.ADVANCE.PAYMENT.RESTRICTION` | `AaSimPaymentRules_AdvancePaymentRestriction` |  |  |  |
| 17 | `AA.PAYRULE.SETTLE.UNEARNED.INTEREST` | `AaSimPaymentRules_SettleUnearnedInterest` |  |  |  |
| 18 | `AA.PAYRULE.RESERVED7` | `AaSimPaymentRules_Reserved7` |  |  |  |
| 19 | `AA.PAYRULE.RESERVED6` | `AaSimPaymentRules_Reserved6` |  |  |  |
| 20 | `AA.PAYRULE.RESERVED5` | `AaSimPaymentRules_Reserved5` |  |  |  |
| 21 | `AA.PAYRULE.RESERVED4` | `AaSimPaymentRules_Reserved4` |  |  |  |
| 22 | `AA.PAYRULE.RESERVED3` | `AaSimPaymentRules_Reserved3` |  |  |  |
| 23 | `AA.PAYRULE.RESERVED2` | `AaSimPaymentRules_Reserved2` |  |  |  |
| 24 | `AA.PAYRULE.RESERVED1` | `AaSimPaymentRules_Reserved1` |  |  |  |
| 25 | `AA.PAYRULE.LOCAL.REF` | `AaSimPaymentRules_LocalRef` |  |  |  |
| 26 | `AA.PAYRULE.PR.ATTRIBUTE` | `AaSimPaymentRules_PrAttribute` |  |  |  |
| 27 | `AA.PAYRULE.PR.VALUE` | `AaSimPaymentRules_PrValue` |  |  |  |
| 28 | `AA.PAYRULE.PR.BRK.RES` | `AaSimPaymentRules_PrBrkRes` |  |  |  |
| 29 | `AA.PAYRULE.PR.BRK.MSG` | `AaSimPaymentRules_PrBrkMsg` |  |  |  |
| 30 | `AA.PAYRULE.PR.BRK.CHARGE` | `AaSimPaymentRules_PrBrkCharge` |  |  |  |
| 31 | `AA.PAYRULE.PR.RESERVED.3` | `AaSimPaymentRules_PrReserved3` |  |  |  |
| 32 | `AA.PAYRULE.PR.RESERVED.2` | `AaSimPaymentRules_PrReserved2` |  |  |  |
| 33 | `AA.PAYRULE.PR.RESERVED.1` | `AaSimPaymentRules_PrReserved1` |  |  |  |
| 34 | `AA.PAYRULE.PR.APP.METHOD` | `AaSimPaymentRules_PrAppMethod` |  |  |  |
| 35 | `AA.PAYRULE.PR.APP.PERIOD` | `AaSimPaymentRules_PrAppPeriod` |  |  |  |
| 36 | `AA.PAYRULE.SYS.RESERVE7` | `AaSimPaymentRules_SysReserve7` |  |  |  |
| 37 | `AA.PAYRULE.SYS.RESERVE6` | `AaSimPaymentRules_SysReserve6` |  |  |  |
| 38 | `AA.PAYRULE.OWNING.COMPANY` | `AaSimPaymentRules_OwningCompany` |  |  |  |
| 39 | `AA.PAYRULE.API.ATTRIBUTE` | `AaSimPaymentRules_ApiAttribute` |  |  |  |
| 40 | `AA.PAYRULE.SYS.RESERVE3` | `AaSimPaymentRules_SysReserve3` |  |  |  |
| 41 | `AA.PAYRULE.SYS.RESERVE2` | `AaSimPaymentRules_SysReserve2` |  |  |  |
| 42 | `AA.PAYRULE.SYS.RESERVE1` | `AaSimPaymentRules_SysReserve1` |  |  |  |
| 43 | `AA.PAYRULE.DEFAULT.ATTR.OPTION` | `AaSimPaymentRules_DefaultAttrOption` |  |  |  |
| 44 | `AA.PAYRULE.DEFAULT.NEGOTIABLE` | `AaSimPaymentRules_DefaultNegotiable` |  |  |  |
| 45 | `AA.PAYRULE.NR.ATTRIBUTE` | `AaSimPaymentRules_NrAttribute` |  |  |  |
| 46 | `AA.PAYRULE.NR.OPTIONS` | `AaSimPaymentRules_NrOptions` |  |  |  |
| 47 | `AA.PAYRULE.NR.ATTRIBUTE.RULE` | `AaSimPaymentRules_NrAttributeRule` |  |  |  |
| 48 | `AA.PAYRULE.NR.VALUE.SOURCE` | `AaSimPaymentRules_NrValueSource` |  |  |  |
| 49 | `AA.PAYRULE.NR.STD.COMP` | `AaSimPaymentRules_NrStdComp` |  |  |  |
| 50 | `AA.PAYRULE.NR.TYPE` | `AaSimPaymentRules_NrType` |  |  |  |
| 51 | `AA.PAYRULE.NR.VALUE` | `AaSimPaymentRules_NrValue` |  |  |  |
| 52 | `AA.PAYRULE.NR.MESSAGE` | `AaSimPaymentRules_NrMessage` |  |  |  |
| 53 | `AA.PAYRULE.CHANGED.FIELDS` | `AaSimPaymentRules_ChangedFields` |  |  |  |
| 54 | `AA.PAYRULE.NEGOTIATED.FLDS` | `AaSimPaymentRules_NegotiatedFlds` |  |  |  |
| 55 | `AA.PAYRULE.ID.COMP.1` | `AaSimPaymentRules_IdComp1` |  |  |  |
| 56 | `AA.PAYRULE.ID.COMP.2` | `AaSimPaymentRules_IdComp2` |  |  |  |
| 57 | `AA.PAYRULE.ID.COMP.3` | `AaSimPaymentRules_IdComp3` |  |  |  |
| 58 | `AA.PAYRULE.ID.COMP.4` | `AaSimPaymentRules_IdComp4` |  |  |  |
| 59 | `AA.PAYRULE.ID.COMP.5` | `AaSimPaymentRules_IdComp5` |  |  |  |
| 60 | `AA.PAYRULE.ID.COMP.6` | `AaSimPaymentRules_IdComp6` |  |  |  |
| 61 | `AA.PAYRULE.RESERVED2.ID` | `AaSimPaymentRules_Reserved2Id` |  |  |  |
| 62 | `AA.PAYRULE.TARGET.PRODUCT` | `AaSimPaymentRules_TargetProduct` |  |  |  |
| 63 | `AA.PAYRULE.STMT.NOS` | `AaSimPaymentRules_StmtNos` |  |  |  |
| 64 | `AA.PAYRULE.OVERRIDE` | `AaSimPaymentRules_Override` |  |  |  |
| 65 | `AA.PAYRULE.RECORD.STATUS` | `AaSimPaymentRules_RecordStatus` |  |  |  |
| 66 | `AA.PAYRULE.CURR.NO` | `AaSimPaymentRules_CurrNo` |  |  |  |
| 67 | `AA.PAYRULE.INPUTTER` | `AaSimPaymentRules_Inputter` |  |  |  |
| 68 | `AA.PAYRULE.DATE.TIME` | `AaSimPaymentRules_DateTime` |  |  |  |
| 69 | `AA.PAYRULE.AUTHORISER` | `AaSimPaymentRules_Authoriser` |  |  |  |
| 70 | `AA.PAYRULE.CO.CODE` | `AaSimPaymentRules_CoCode` |  |  |  |
| 71 | `AA.PAYRULE.DEPT.CODE` | `AaSimPaymentRules_DeptCode` |  |  |  |
| 72 | `AA.PAYRULE.AUDITOR.CODE` | `AaSimPaymentRules_AuditorCode` |  |  |  |
| 73 | `AA.PAYRULE.AUDIT.DATE.TIME` | `AaSimPaymentRules_AuditDateTime` |  |  |  |
