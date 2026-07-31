# TRANSACTION.RULES — Table Schema

> Source: `INSERTS/I_F.TRANSACTION.RULES` in `AA_TransactionRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.TR.ACTIVITY` | `AaSimTransactionRules_Activity` |  |  |  |
| 2 | `AA.TR.ACTION` | `AaSimTransactionRules_Action` |  |  |  |
| 3 | `AA.TR.RESERVED4` | `AaSimTransactionRules_Reserved4` |  |  |  |
| 4 | `AA.TR.RESERVED5` | `AaSimTransactionRules_Reserved5` |  |  |  |
| 5 | `AA.TR.APPLICATION.TYPE` | `AaSimTransactionRules_ApplicationType` |  |  |  |
| 6 | `AA.TR.APPLICATION.ORDER` | `AaSimTransactionRules_ApplicationOrder` |  |  |  |
| 7 | `AA.TR.PROPERTY` | `AaSimTransactionRules_Property` |  |  |  |
| 8 | `AA.TR.BALANCE.TYPE` | `AaSimTransactionRules_BalanceType` |  |  |  |
| 9 | `AA.TR.PROP.APPL.TYPE` | `AaSimTransactionRules_PropApplType` |  |  |  |
| 10 | `AA.TR.RESERVED6` | `AaSimTransactionRules_Reserved6` |  |  |  |
| 11 | `AA.TR.RESERVED7` | `AaSimTransactionRules_Reserved7` |  |  |  |
| 12 | `AA.TR.RESERVED8` | `AaSimTransactionRules_Reserved8` |  |  |  |
| 13 | `AA.TR.ADVANCE.PAYMENT.METHOD` | `AaSimTransactionRules_AdvancePaymentMethod` |  |  |  |
| 14 | `AA.TR.ADVANCE.PAYMENT.RESTRICTION` | `AaSimTransactionRules_AdvancePaymentRestriction` |  |  |  |
| 15 | `AA.TR.RESERVED11` | `AaSimTransactionRules_Reserved11` |  |  |  |
| 16 | `AA.TR.RESERVED12` | `AaSimTransactionRules_Reserved12` |  |  |  |
| 17 | `AA.TR.RESERVED13` | `AaSimTransactionRules_Reserved13` |  |  |  |
| 18 | `AA.TR.RESERVED14` | `AaSimTransactionRules_Reserved14` |  |  |  |
| 19 | `AA.TR.RESERVED15` | `AaSimTransactionRules_Reserved15` |  |  |  |
| 20 | `AA.TR.LOCAL.REF` | `AaSimTransactionRules_LocalRef` |  |  |  |
| 21 | `AA.TR.PR.ATTRIBUTE` | `AaSimTransactionRules_PrAttribute` |  |  |  |
| 22 | `AA.TR.PR.VALUE` | `AaSimTransactionRules_PrValue` |  |  |  |
| 23 | `AA.TR.PR.BRK.RES` | `AaSimTransactionRules_PrBrkRes` |  |  |  |
| 24 | `AA.TR.PR.BRK.MSG` | `AaSimTransactionRules_PrBrkMsg` |  |  |  |
| 25 | `AA.TR.PR.BRK.CHARGE` | `AaSimTransactionRules_PrBrkCharge` |  |  |  |
| 26 | `AA.TR.PR.RESERVED.3` | `AaSimTransactionRules_PrReserved3` |  |  |  |
| 27 | `AA.TR.PR.RESERVED.2` | `AaSimTransactionRules_PrReserved2` |  |  |  |
| 28 | `AA.TR.PR.RESERVED.1` | `AaSimTransactionRules_PrReserved1` |  |  |  |
| 29 | `AA.TR.PR.APP.METHOD` | `AaSimTransactionRules_PrAppMethod` |  |  |  |
| 30 | `AA.TR.PR.APP.PERIOD` | `AaSimTransactionRules_PrAppPeriod` |  |  |  |
| 31 | `AA.TR.SYS.RESERVE7` | `AaSimTransactionRules_SysReserve7` |  |  |  |
| 32 | `AA.TR.SYS.RESERVE6` | `AaSimTransactionRules_SysReserve6` |  |  |  |
| 33 | `AA.TR.OWNING.COMPANY` | `AaSimTransactionRules_OwningCompany` |  |  |  |
| 34 | `AA.TR.API.ATTRIBUTE` | `AaSimTransactionRules_ApiAttribute` |  |  |  |
| 35 | `AA.TR.SYS.RESERVE3` | `AaSimTransactionRules_SysReserve3` |  |  |  |
| 36 | `AA.TR.SYS.RESERVE2` | `AaSimTransactionRules_SysReserve2` |  |  |  |
| 37 | `AA.TR.SYS.RESERVE1` | `AaSimTransactionRules_SysReserve1` |  |  |  |
| 38 | `AA.TR.DEFAULT.ATTR.OPTION` | `AaSimTransactionRules_DefaultAttrOption` |  |  |  |
| 39 | `AA.TR.DEFAULT.NEGOTIABLE` | `AaSimTransactionRules_DefaultNegotiable` |  |  |  |
| 40 | `AA.TR.NR.ATTRIBUTE` | `AaSimTransactionRules_NrAttribute` |  |  |  |
| 41 | `AA.TR.NR.OPTIONS` | `AaSimTransactionRules_NrOptions` |  |  |  |
| 42 | `AA.TR.NR.ATTRIBUTE.RULE` | `AaSimTransactionRules_NrAttributeRule` |  |  |  |
| 43 | `AA.TR.NR.VALUE.SOURCE` | `AaSimTransactionRules_NrValueSource` |  |  |  |
| 44 | `AA.TR.NR.STD.COMP` | `AaSimTransactionRules_NrStdComp` |  |  |  |
| 45 | `AA.TR.NR.TYPE` | `AaSimTransactionRules_NrType` |  |  |  |
| 46 | `AA.TR.NR.VALUE` | `AaSimTransactionRules_NrValue` |  |  |  |
| 47 | `AA.TR.NR.MESSAGE` | `AaSimTransactionRules_NrMessage` |  |  |  |
| 48 | `AA.TR.CHANGED.FIELDS` | `AaSimTransactionRules_ChangedFields` |  |  |  |
| 49 | `AA.TR.NEGOTIATED.FLDS` | `AaSimTransactionRules_NegotiatedFlds` |  |  |  |
| 50 | `AA.TR.ID.COMP.1` | `AaSimTransactionRules_IdComp1` |  |  |  |
| 51 | `AA.TR.ID.COMP.2` | `AaSimTransactionRules_IdComp2` |  |  |  |
| 52 | `AA.TR.ID.COMP.3` | `AaSimTransactionRules_IdComp3` |  |  |  |
| 53 | `AA.TR.ID.COMP.4` | `AaSimTransactionRules_IdComp4` |  |  |  |
| 54 | `AA.TR.ID.COMP.5` | `AaSimTransactionRules_IdComp5` |  |  |  |
| 55 | `AA.TR.ID.COMP.6` | `AaSimTransactionRules_IdComp6` |  |  |  |
| 56 | `AA.TR.RESERVED2.ID` | `AaSimTransactionRules_Reserved2Id` |  |  |  |
| 57 | `AA.TR.TARGET.PRODUCT` | `AaSimTransactionRules_TargetProduct` |  |  |  |
| 58 | `AA.TR.STMT.NOS` | `AaSimTransactionRules_StmtNos` |  |  |  |
| 59 | `AA.TR.OVERRIDE` | `AaSimTransactionRules_Override` |  |  |  |
| 60 | `AA.TR.RECORD.STATUS` | `AaSimTransactionRules_RecordStatus` |  |  |  |
| 61 | `AA.TR.CURR.NO` | `AaSimTransactionRules_CurrNo` |  |  |  |
| 62 | `AA.TR.INPUTTER` | `AaSimTransactionRules_Inputter` |  |  |  |
| 63 | `AA.TR.DATE.TIME` | `AaSimTransactionRules_DateTime` |  |  |  |
| 64 | `AA.TR.AUTHORISER` | `AaSimTransactionRules_Authoriser` |  |  |  |
| 65 | `AA.TR.CO.CODE` | `AaSimTransactionRules_CoCode` |  |  |  |
| 66 | `AA.TR.DEPT.CODE` | `AaSimTransactionRules_DeptCode` |  |  |  |
| 67 | `AA.TR.AUDITOR.CODE` | `AaSimTransactionRules_AuditorCode` |  |  |  |
| 68 | `AA.TR.AUDIT.DATE.TIME` | `AaSimTransactionRules_AuditDateTime` |  |  |  |
