# AA.ACTIVITY.HISTORY — Table Schema

> Source: `INSERTS/I_F.AA.ACTIVITY.HISTORY` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AH.EFFECTIVE.DATE` | `AaActivityHistory_EffectiveDate` |  |  |  |
| 2 | `AA.AH.ACTIVITY.REF` | `AaActivityHistory_ActivityRef` |  |  |  |
| 3 | `AA.AH.ACTIVITY` | `AaActivityHistory_Activity` |  |  |  |
| 4 | `AA.AH.SYSTEM.DATE` | `AaActivityHistory_SystemDate` |  |  |  |
| 5 | `AA.AH.CONTRACT.ID` | `AaActivityHistory_ContractId` |  |  |  |
| 6 | `AA.AH.ACTIVITY.AMT` | `AaActivityHistory_ActivityAmt` |  |  |  |
| 7 | `AA.AH.ACT.STATUS` | `AaActivityHistory_ActStatus` |  |  |  |
| 8 | `AA.AH.AGENT.EVENT.REF` | `AaActivityHistory_AgentEventRef` |  |  |  |
| 9 | `AA.AH.AGENT.EVENT.STATUS` | `AaActivityHistory_AgentEventStatus` |  |  |  |
| 10 | `AA.AH.TRANSACTION.INITIATION` | `AaActivityHistory_TransactionInitiation` |  |  |  |
| 11 | `AA.AH.INITIATION` | `AaActivityHistory_Initiation` |  |  |  |
| 12 | `AA.AH.ACTIVITY.CON.REF` | `AaActivityHistory_ActivityConRef` |  |  |  |
| 13 | `AA.AH.ACT.DATE` | `AaActivityHistory_ActDate` |  |  |  |
| 14 | `AA.AH.DAILY.CUMULATIVE` | `AaActivityHistory_DailyCumulative` |  |  |  |
| 15 | `AA.AH.TOT.CUMULATIVE` | `AaActivityHistory_TotCumulative` |  |  |  |
| 16 | `AA.AH.USED.CONTEXT.TYPE` | `AaActivityHistory_UsedContextType` |  |  |  |
| 17 | `AA.AH.RESERVED.4` | `AaActivityHistory_Reserved4` | TField |  |  |
| 18 | `AA.AH.LAST.HIST.COUNT` | `AaActivityHistory_LastHistCount` |  |  |  |
| 19 | `AA.AH.LAST.EFF.DATE` | `AaActivityHistory_LastEffDate` |  |  |  |
| 20 | `AA.AH.ARC.ID` | `AaActivityHistory_ArcId` |  |  |  |
| 21 | `AA.AH.ARC.DATE.TILL` | `AaActivityHistory_ArcDateTill` |  |  |  |
| 22 | `AA.AH.REF.ACTIVITY.REF` | `AaActivityHistory_RefActivityRef` |  |  |  |
| 23 | `AA.AH.BILL.ID` | `AaActivityHistory_BillId` |  |  |  |
| 24 | `AA.AH.PAY.ORDER.REF` | `AaActivityHistory_PayOrderRef` |  |  |  |
| 25 | `AA.AH.DD.REF.ID` | `AaActivityHistory_DdRefId` |  |  |  |
| 26 | `AA.AH.TRANS.REF` | `AaActivityHistory_TransRef` |  |  |  |
| 27 | `AA.AH.AAA.ID` | `AaActivityHistory_AaaId` |  |  |  |
| 28 | `AA.AH.TRANS.INFO` | `AaActivityHistory_TransInfo` |  |  |  |
| 29 | `AA.AH.SETTLEMENT.ARR.INFO` | `AaActivityHistory_SettlementArrInfo` |  |  |  |
| 30 | `AA.AH.ASSESSMENT.ACTIVITY` | `AaActivityHistory_AssessmentActivity` |  |  |  |
| 31 | `AA.AH.LINKED.ACTIVITY` | `AaActivityHistory_LinkedActivity` |  |  |  |
| 32 | `AA.AH.SECONDARY.TYPE` | `AaActivityHistory_SecondaryType` |  |  |  |
| 33 | `AA.AH.EVALUATED.ACTIVITY` | `AaActivityHistory_EvaluatedActivity` |  |  |  |
| 34 | `AA.AH.EVALUATED.REFERENCE` | `AaActivityHistory_EvaluatedReference` |  |  |  |
| 35 | `AA.AH.PARENT.ID` | `AaActivityHistory_ParentId` |  |  |  |
| 36 | `AA.AH.GRID.LINK.DATE` | `AaActivityHistory_GridLinkDate` |  |  |  |
| 37 | `AA.AH.GRID.ACTIVITY.REF` | `AaActivityHistory_GridActivityRef` |  |  |  |
| 38 | `AA.AH.GRID.PROP` | `AaActivityHistory_GridProp` |  |  |  |
| 39 | `AA.AH.GRID.TARGET` | `AaActivityHistory_GridTarget` |  |  |  |
| 40 | `AA.AH.ACT.TIME.STAMP` | `AaActivityHistory_ActTimeStamp` |  |  |  |
| 41 | `AA.AH.CONTRACT.ENQ` | `AaActivityHistory_ContractEnq` | TField |  |  |
| 42 | `AA.AH.PRICING.ACTIVITY` | `AaActivityHistory_PricingActivity` |  |  |  |
| 43 | `AA.AH.PRICING.REFERENCE` | `AaActivityHistory_PricingReference` |  |  |  |
| 44 | `AA.AH.PRICING.LINK.ACTIVITY` | `AaActivityHistory_PricingLinkActivity` |  |  |  |
| 45 | `AA.AH.IFRS.CHARGEOFF.OPR` | `AaActivityHistory_IfrsChargeoffOpr` |  |  |  |
| 46 | `AA.AH.IFRS.CHARGEOFF.AMT` | `AaActivityHistory_IfrsChargeoffAmt` |  |  |  |
| 47 | `AA.AH.ACTUAL.ARC.TILL.DATE` | `AaActivityHistory_ActualArcTillDate` | TField |  | Field to store the Archival Till Date so that if any backdated activity comes for that period may go into the same .HIST. record. |
