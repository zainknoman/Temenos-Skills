# AA.ELIGIBILITY — Table Schema

> Source: `INSERTS/I_F.AA.ELIGIBILITY` in `AA_Eligibility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.EL.ACTIVITY` | `AaSimEligibility_Activity` |  |  |  |
| 2 | `AA.EL.ACTION` | `AaSimEligibility_Action` |  |  |  |
| 3 | `AA.EL.RULE` | `AaSimEligibility_Rule` |  |  |  |
| 4 | `AA.EL.FAILURE.TYPE` | `AaSimEligibility_FailureType` |  |  |  |
| 5 | `AA.EL.FAILURE.ACTION` | `AaSimEligibility_FailureAction` |  |  |  |
| 6 | `AA.EL.CUSTOMER.ROLE` | `AaSimEligibility_CustomerRole` |  |  |  |
| 7 | `AA.EL.ROLE.RULE` | `AaSimEligibility_RoleRule` |  |  |  |
| 8 | `AA.EL.ROLE.FAILURE.TYPE` | `AaSimEligibility_RoleFailureType` |  |  |  |
| 9 | `AA.EL.ROLE.FAILURE.ACTION` | `AaSimEligibility_RoleFailureAction` |  |  |  |
| 10 | `AA.EL.CHANGE.ACTIVITY` | `AaSimEligibility_ChangeActivity` |  |  |  |
| 11 | `AA.EL.PERIODIC.REVIEW` | `AaSimEligibility_PeriodicReview` |  |  |  |
| 12 | `AA.EL.REVIEW.FREQUENCY` | `AaSimEligibility_ReviewFrequency` |  |  |  |
| 13 | `AA.EL.CUST.STATIC.REVIEW` | `AaSimEligibility_CustStaticReview` |  |  |  |
| 14 | `AA.EL.ELIGIBILE.DEFAULT.PRD` | `AaSimEligibility_EligibileDefaultPrd` |  |  |  |
| 15 | `AA.EL.LAST.RUN.DATE` | `AaSimEligibility_LastRunDate` |  |  |  |
| 16 | `AA.EL.FAILURE.RULE` | `AaSimEligibility_FailureRule` |  |  |  |
| 17 | `AA.EL.RULE.RESULT` | `AaSimEligibility_RuleResult` |  |  |  |
| 18 | `AA.EL.PRD.CHANGE.REQUIRED` | `AaSimEligibility_PrdChangeRequired` |  |  |  |
| 19 | `AA.EL.SATISFY.RULE` | `AaSimEligibility_SatisfyRule` |  |  |  |
| 20 | `AA.EL.RESERVED9` | `AaSimEligibility_Reserved9` |  |  |  |
| 21 | `AA.EL.RESERVED8` | `AaSimEligibility_Reserved8` |  |  |  |
| 22 | `AA.EL.RESERVED7` | `AaSimEligibility_Reserved7` |  |  |  |
| 23 | `AA.EL.RESERVED6` | `AaSimEligibility_Reserved6` |  |  |  |
| 24 | `AA.EL.RESERVED5` | `AaSimEligibility_Reserved5` |  |  |  |
| 25 | `AA.EL.RESERVED4` | `AaSimEligibility_Reserved4` |  |  |  |
| 26 | `AA.EL.RESERVED3` | `AaSimEligibility_Reserved3` |  |  |  |
| 27 | `AA.EL.RESERVED2` | `AaSimEligibility_Reserved2` |  |  |  |
| 28 | `AA.EL.RESERVED1` | `AaSimEligibility_Reserved1` |  |  |  |
| 29 | `AA.EL.LOCAL.REF` | `AaSimEligibility_LocalRef` |  |  |  |
| 30 | `AA.EL.PR.ATTRIBUTE` | `AaSimEligibility_PrAttribute` |  |  |  |
| 31 | `AA.EL.PR.VALUE` | `AaSimEligibility_PrValue` |  |  |  |
| 32 | `AA.EL.PR.BRK.RES` | `AaSimEligibility_PrBrkRes` |  |  |  |
| 33 | `AA.EL.PR.BRK.MSG` | `AaSimEligibility_PrBrkMsg` |  |  |  |
| 34 | `AA.EL.PR.BRK.CHARGE` | `AaSimEligibility_PrBrkCharge` |  |  |  |
| 35 | `AA.EL.PR.RESERVED.3` | `AaSimEligibility_PrReserved3` |  |  |  |
| 36 | `AA.EL.PR.RESERVED.2` | `AaSimEligibility_PrReserved2` |  |  |  |
| 37 | `AA.EL.PR.RESERVED.1` | `AaSimEligibility_PrReserved1` |  |  |  |
| 38 | `AA.EL.PR.APP.METHOD` | `AaSimEligibility_PrAppMethod` |  |  |  |
| 39 | `AA.EL.PR.APP.PERIOD` | `AaSimEligibility_PrAppPeriod` |  |  |  |
| 40 | `AA.EL.SYS.RESERVE7` | `AaSimEligibility_SysReserve7` |  |  |  |
| 41 | `AA.EL.SYS.RESERVE6` | `AaSimEligibility_SysReserve6` |  |  |  |
| 42 | `AA.EL.OWNING.COMPANY` | `AaSimEligibility_OwningCompany` |  |  |  |
| 43 | `AA.EL.API.ATTRIBUTE` | `AaSimEligibility_ApiAttribute` |  |  |  |
| 44 | `AA.EL.SYS.RESERVE3` | `AaSimEligibility_SysReserve3` |  |  |  |
| 45 | `AA.EL.SYS.RESERVE2` | `AaSimEligibility_SysReserve2` |  |  |  |
| 46 | `AA.EL.SYS.RESERVE1` | `AaSimEligibility_SysReserve1` |  |  |  |
| 47 | `AA.EL.DEFAULT.ATTR.OPTION` | `AaSimEligibility_DefaultAttrOption` |  |  |  |
| 48 | `AA.EL.DEFAULT.NEGOTIABLE` | `AaSimEligibility_DefaultNegotiable` |  |  |  |
| 49 | `AA.EL.NR.ATTRIBUTE` | `AaSimEligibility_NrAttribute` |  |  |  |
| 50 | `AA.EL.NR.OPTIONS` | `AaSimEligibility_NrOptions` |  |  |  |
| 51 | `AA.EL.NR.ATTRIBUTE.RULE` | `AaSimEligibility_NrAttributeRule` |  |  |  |
| 52 | `AA.EL.NR.VALUE.SOURCE` | `AaSimEligibility_NrValueSource` |  |  |  |
| 53 | `AA.EL.NR.STD.COMP` | `AaSimEligibility_NrStdComp` |  |  |  |
| 54 | `AA.EL.NR.TYPE` | `AaSimEligibility_NrType` |  |  |  |
| 55 | `AA.EL.NR.VALUE` | `AaSimEligibility_NrValue` |  |  |  |
| 56 | `AA.EL.NR.MESSAGE` | `AaSimEligibility_NrMessage` |  |  |  |
| 57 | `AA.EL.CHANGED.FIELDS` | `AaSimEligibility_ChangedFields` |  |  |  |
| 58 | `AA.EL.NEGOTIATED.FLDS` | `AaSimEligibility_NegotiatedFlds` |  |  |  |
| 59 | `AA.EL.ID.COMP.1` | `AaSimEligibility_IdComp1` |  |  |  |
| 60 | `AA.EL.ID.COMP.2` | `AaSimEligibility_IdComp2` |  |  |  |
| 61 | `AA.EL.ID.COMP.3` | `AaSimEligibility_IdComp3` |  |  |  |
| 62 | `AA.EL.ID.COMP.4` | `AaSimEligibility_IdComp4` |  |  |  |
| 63 | `AA.EL.ID.COMP.5` | `AaSimEligibility_IdComp5` |  |  |  |
| 64 | `AA.EL.ID.COMP.6` | `AaSimEligibility_IdComp6` |  |  |  |
| 65 | `AA.EL.RESERVED2.ID` | `AaSimEligibility_Reserved2Id` |  |  |  |
| 66 | `AA.EL.TARGET.PRODUCT` | `AaSimEligibility_TargetProduct` |  |  |  |
| 67 | `AA.EL.STMT.NOS` | `AaSimEligibility_StmtNos` |  |  |  |
| 68 | `AA.EL.OVERRIDE` | `AaSimEligibility_Override` |  |  |  |
| 69 | `AA.EL.RECORD.STATUS` | `AaSimEligibility_RecordStatus` |  |  |  |
| 70 | `AA.EL.CURR.NO` | `AaSimEligibility_CurrNo` |  |  |  |
| 71 | `AA.EL.INPUTTER` | `AaSimEligibility_Inputter` |  |  |  |
| 72 | `AA.EL.DATE.TIME` | `AaSimEligibility_DateTime` |  |  |  |
| 73 | `AA.EL.AUTHORISER` | `AaSimEligibility_Authoriser` |  |  |  |
| 74 | `AA.EL.CO.CODE` | `AaSimEligibility_CoCode` |  |  |  |
| 75 | `AA.EL.DEPT.CODE` | `AaSimEligibility_DeptCode` |  |  |  |
| 76 | `AA.EL.AUDITOR.CODE` | `AaSimEligibility_AuditorCode` |  |  |  |
| 77 | `AA.EL.AUDIT.DATE.TIME` | `AaSimEligibility_AuditDateTime` |  |  |  |
| 78 | `AA.EL.RULE.EXPRESSION` | `AaSimEligibility_RuleExpression` |  |  |  |
| 79 | `AA.EL.ROLE.RULE.EXPRESSION` | `AaSimEligibility_RoleRuleExpression` |  |  |  |
