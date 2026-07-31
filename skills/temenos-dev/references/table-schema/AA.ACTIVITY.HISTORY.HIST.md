# AA.ACTIVITY.HISTORY.HIST — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.HISTORY.HIST` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AH.EFFECTIVE.DATE` | `AaActivityHistoryHist_EffectiveDate` |  |  |  |
| 2 | `AA.AH.ACTIVITY.REF` | `AaActivityHistoryHist_ActivityRef` |  |  |  |
| 3 | `AA.AH.ACTIVITY` | `AaActivityHistoryHist_Activity` |  |  |  |
| 4 | `AA.AH.SYSTEM.DATE` | `AaActivityHistoryHist_SystemDate` |  |  |  |
| 5 | `AA.AH.CONTRACT.ID` | `AaActivityHistoryHist_ContractId` |  |  |  |
| 6 | `AA.AH.ACTIVITY.AMT` | `AaActivityHistoryHist_ActivityAmt` |  |  |  |
| 7 | `AA.AH.ACT.STATUS` | `AaActivityHistoryHist_ActStatus` |  |  |  |
| 8 | `AA.AH.AGENT.EVENT.REF` | `AaActivityHistoryHist_AgentEventRef` |  |  |  |
| 9 | `AA.AH.AGENT.EVENT.STATUS` | `AaActivityHistoryHist_AgentEventStatus` |  |  |  |
| 10 | `AA.AH.TRANSACTION.INITIATION` | `AaActivityHistoryHist_TransactionInitiation` |  |  |  |
| 11 | `AA.AH.INITIATION` | `AaActivityHistoryHist_Initiation` |  |  |  |
| 12 | `AA.AH.ACTIVITY.CON.REF` | `AaActivityHistoryHist_ActivityConRef` |  |  |  |
| 13 | `AA.AH.ACT.DATE` | `AaActivityHistoryHist_ActDate` |  |  |  |
| 14 | `AA.AH.DAILY.CUMULATIVE` | `AaActivityHistoryHist_DailyCumulative` |  |  |  |
| 15 | `AA.AH.TOT.CUMULATIVE` | `AaActivityHistoryHist_TotCumulative` |  |  |  |
| 16 | `AA.AH.USED.CONTEXT.TYPE` | `AaActivityHistoryHist_UsedContextType` |  |  |  |
| 17 | `AA.AH.RESERVED.4` | `AaActivityHistoryHist_Reserved4` | TField |  |  |
| 18 | `AA.AH.LAST.HIST.COUNT` | `AaActivityHistoryHist_LastHistCount` |  |  |  |
| 19 | `AA.AH.LAST.EFF.DATE` | `AaActivityHistoryHist_LastEffDate` |  |  |  |
| 20 | `AA.AH.ARC.ID` | `AaActivityHistoryHist_ArcId` |  |  |  |
| 21 | `AA.AH.ARC.DATE.TILL` | `AaActivityHistoryHist_ArcDateTill` |  |  |  |
| 22 | `AA.AH.REF.ACTIVITY.REF` | `AaActivityHistoryHist_RefActivityRef` |  |  |  |
| 23 | `AA.AH.BILL.ID` | `AaActivityHistoryHist_BillId` |  |  |  |
| 24 | `AA.AH.PAY.ORDER.REF` | `AaActivityHistoryHist_PayOrderRef` |  |  |  |
| 25 | `AA.AH.DD.REF.ID` | `AaActivityHistoryHist_DdRefId` |  |  |  |
| 26 | `AA.AH.TRANS.REF` | `AaActivityHistoryHist_TransRef` |  |  |  |
| 27 | `AA.AH.AAA.ID` | `AaActivityHistoryHist_AaaId` |  |  |  |
| 28 | `AA.AH.TRANS.INFO` | `AaActivityHistoryHist_TransInfo` |  |  |  |
| 29 | `AA.AH.SETTLEMENT.ARR.INFO` | `AaActivityHistoryHist_SettlementArrInfo` |  |  |  |
| 30 | `AA.AH.ASSESSMENT.ACTIVITY` | `AaActivityHistoryHist_AssessmentActivity` |  |  |  |
| 31 | `AA.AH.LINKED.ACTIVITY` | `AaActivityHistoryHist_LinkedActivity` |  |  |  |
| 32 | `AA.AH.SECONDARY.TYPE` | `AaActivityHistoryHist_SecondaryType` |  |  |  |
| 33 | `AA.AH.EVALUATED.ACTIVITY` | `AaActivityHistoryHist_EvaluatedActivity` |  |  |  |
| 34 | `AA.AH.EVALUATED.REFERENCE` | `AaActivityHistoryHist_EvaluatedReference` |  |  |  |
| 35 | `AA.AH.PARENT.ID` | `AaActivityHistoryHist_ParentId` |  |  |  |
| 36 | `AA.AH.GRID.LINK.DATE` | `AaActivityHistory_GridLinkDate` |  |  |  |
| 37 | `AA.AH.GRID.ACTIVITY.REF` | `AaActivityHistory_GridActivityRef` |  |  |  |
| 38 | `AA.AH.GRID.PROP` | `AaActivityHistory_GridProp` |  |  |  |
| 39 | `AA.AH.GRID.TARGET` | `AaActivityHistory_GridTarget` |  |  |  |
| 40 | `AA.AH.ACT.TIME.STAMP` | `AaActivityHistory_ActTimeStamp` |  |  |  |
| 41 | `AA.AH.CONTRACT.ENQ` | `AaActivityHistoryHist_ContractEnq` | TField |  |  |
| 42 | `AA.AH.PRICING.ACTIVITY` | `AaActivityHistoryHist_PricingActivity` |  |  |  |
| 43 | `AA.AH.PRICING.REFERENCE` | `AaActivityHistoryHist_PricingReference` |  |  |  |
| 44 | `AA.AH.PRICING.LINK.ACTIVITY` | `AaActivityHistoryHist_PricingLinkActivity` |  |  |  |
| 45 | `AA.AH.IFRS.CHARGEOFF.OPR` | `AaActivityHistoryHist_IfrsChargeoffOpr` |  |  |  |
| 46 | `AA.AH.IFRS.CHARGEOFF.AMT` | `AaActivityHistoryHist_IfrsChargeoffAmt` |  |  |  |
