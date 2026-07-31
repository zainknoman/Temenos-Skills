# CAPL.PLAN.TYPE — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.TYPE` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PT.DESCRIPTION` | `CaplPlanType_Description` |  |  |  |
| 2 | `CAPL.PT.PLAN.GROUP` | `CaplPlanType_PlanGroup` | TField |  |  |
| 3 | `CAPL.PT.SPOUSAL.PLAN` | `CaplPlanType_SpousalPlan` | TField |  |  |
| 4 | `CAPL.PT.COMBINE.CONTRIBUTION` | `CaplPlanType_CombineContribution` | TField |  |  |
| 5 | `CAPL.PT.MINIMUM.AGE` | `CaplPlanType_MinimumAge` | TField |  |  |
| 6 | `CAPL.PT.MAXIMUM.AGE` | `CaplPlanType_MaximumAge` | TField |  |  |
| 7 | `CAPL.PT.AUTO.CONVERT.TO` | `CaplPlanType_AutoConvertTo` |  |  |  |
| 8 | `CAPL.PT.BEF.CONV.NOTICE` | `CaplPlanType_BefConvNotice` |  |  |  |
| 9 | `CAPL.PT.BEF.CONV.NOTICE.DATE` | `CaplPlanType_BefConvNoticeDate` |  |  |  |
| 10 | `CAPL.PT.AFTER.CONV.NOTICE` | `CaplPlanType_AfterConvNotice` |  |  |  |
| 11 | `CAPL.PT.AFTER.CONV.NOTICE.DATE` | `CaplPlanType_AfterConvNoticeDate` |  |  |  |
| 12 | `CAPL.PT.QUALIFYING.IND` | `CaplPlanType_QualifyingInd` |  |  |  |
| 13 | `CAPL.PT.YEARLY.MIN.FORMULA` | `CaplPlanType_YearlyMinFormula` |  |  |  |
| 14 | `CAPL.PT.RESERVED.10` | `CaplPlanType_Reserved10` |  |  |  |
| 15 | `CAPL.PT.RESERVED.9` | `CaplPlanType_Reserved9` |  |  |  |
| 16 | `CAPL.PT.RESERVED.8` | `CaplPlanType_Reserved8` | TField |  |  |
| 17 | `CAPL.PT.LOCKED` | `CaplPlanType_Locked` | TField |  |  |
| 18 | `CAPL.PT.JURISDICTION` | `CaplPlanType_Jurisdiction` | TField |  |  |
| 19 | `CAPL.PT.INV.RETURN` | `CaplPlanType_InvReturn` | TField |  |  |
| 20 | `CAPL.PT.YEARLY.MAX.FORMULA` | `CaplPlanType_YearlyMaxFormula` | TField |  |  |
| 21 | `CAPL.PT.PRORATE.FIRST.YEAR` | `CaplPlanType_ProrateFirstYear` | TField |  |  |
| 22 | `CAPL.PT.RESERVED.7` | `CaplPlanType_Reserved7` | TField |  |  |
| 23 | `CAPL.PT.RESERVED.6` | `CaplPlanType_Reserved6` | TField |  |  |
| 24 | `CAPL.PT.PROD.CAT.ACCT` | `CaplPlanType_ProdCatAcct` | TField |  |  |
| 25 | `CAPL.PT.PROD.CAT.TERM` | `CaplPlanType_ProdCatTerm` | TField |  |  |
| 26 | `CAPL.PT.RESERVED.5` | `CaplPlanType_Reserved5` | TField |  |  |
| 27 | `CAPL.PT.RESERVED.4` | `CaplPlanType_Reserved4` | TField |  |  |
| 28 | `CAPL.PT.PLAN.ISSUER.TYPE` | `CaplPlanType_PlanIssuerType` | TField |  |  |
| 29 | `CAPL.PT.SPECIMEN.NO` | `CaplPlanType_SpecimenNo` |  |  |  |
| 30 | `CAPL.PT.SPECIMEN.NAME` | `CaplPlanType_SpecimenName` |  |  |  |
| 31 | `CAPL.PT.SECTION.ACT` | `CaplPlanType_SectionAct` |  |  |  |
| 32 | `CAPL.PT.FORWARD.BACKWARD` | `CaplPlanType_ForwardBackward` | TField |  |  |
| 33 | `CAPL.PT.SCHED.PAY.METHOD` | `CaplPlanType_SchedPayMethod` |  |  |  |
| 34 | `CAPL.PT.DAYS.AHEAD` | `CaplPlanType_DaysAhead` |  |  |  |
| 35 | `CAPL.PT.SUSP.ACCOUNT` | `CaplPlanType_SuspAccount` |  |  |  |
| 36 | `CAPL.PT.DEF.SCHED.TAX.METHOD` | `CaplPlanType_DefSchedTaxMethod` | TField |  |  |
| 37 | `CAPL.PT.DEF.SCHED.PAY.METHOD` | `CaplPlanType_DefSchedPayMethod` | TField |  |  |
| 38 | `CAPL.PT.DEF.SCHED.PAY.RULE` | `CaplPlanType_DefSchedPayRule` | TField |  |  |
| 39 | `CAPL.PT.DEF.SCHED.PAY.START` | `CaplPlanType_DefSchedPayStart` | TField |  |  |
| 40 | `CAPL.PT.SCHED.PAYM.TXN.CODE` | `CaplPlanType_SchedPaymTxnCode` | TField |  |  |
| 41 | `CAPL.PT.SALE.START.DATE` | `CaplPlanType_SaleStartDate` | TField |  |  |
| 42 | `CAPL.PT.SALE.END.DATE` | `CaplPlanType_SaleEndDate` | TField |  |  |
| 43 | `CAPL.PT.CAMB.PRODUCT.CODE` | `CaplPlanType_CambProductCode` | TField |  | Field is used to maintain the CDIC code for registered products.For example a register plan account with RRIF-REG plan will fall under RRIF plan- CDIC product code as 33eg. 33System update field. |
| 44 | `CAPL.PT.REG.PLAN.TYP.CODE` | `CaplPlanType_RegPlanTypCode` | TField |  | Field is used to maintain the product code only for CAPL.PLAN.TYPE recordsSystem udpate field. |
| 45 | `CAPL.PT.SEQ.PROD.NO` | `CaplPlanType_SeqProdNo` | TField |  | Fieldused to maintain sequence number for all categories, AZ products, AA products and Register producteg. 21System udpate field. |
| 46 | `CAPL.PT.RESERVED.1` | `CaplPlanType_Reserved1` | TField |  |  |
| 47 | `CAPL.PT.LOCAL.REF` | `CaplPlanType_LocalRef` |  |  |  |
| 48 | `CAPL.PT.OVERRIDE` | `CaplPlanType_Override` |  |  |  |
| 49 | `CAPL.PT.RECORD.STATUS` | `CaplPlanType_RecordStatus` | String |  |  |
| 50 | `CAPL.PT.CURR.NO` | `CaplPlanType_CurrNo` | String |  |  |
| 51 | `CAPL.PT.INPUTTER` | `CaplPlanType_Inputter` |  |  |  |
| 52 | `CAPL.PT.DATE.TIME` | `CaplPlanType_DateTime` |  |  |  |
| 53 | `CAPL.PT.AUTHORISER` | `CaplPlanType_Authoriser` | String |  |  |
| 54 | `CAPL.PT.CO.CODE` | `CaplPlanType_CoCode` | String |  |  |
| 55 | `CAPL.PT.DEPT.CODE` | `CaplPlanType_DeptCode` | String |  |  |
| 56 | `CAPL.PT.AUDITOR.CODE` | `CaplPlanType_AuditorCode` | String |  |  |
| 57 | `CAPL.PT.AUDIT.DATE.TIME` | `CaplPlanType_AuditDateTime` | String |  |  |
