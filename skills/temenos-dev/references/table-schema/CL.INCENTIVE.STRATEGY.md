# CL.INCENTIVE.STRATEGY — Table Schema

> Source: `INSERTS/I_F.CL.INCENTIVE.STRATEGY` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.INCST.TRGT.MAIN.ACT` | `ClIncentiveStrategy_TrgtMainAct` | TField |  | Number of main actions required as target for the collector. |
| 2 | `CL.INCST.TRGT.PTS.MACT` | `ClIncentiveStrategy_TrgtPtsMact` | TField |  | Number of incentive points allocated to collector if the target main actions is reached. |
| 3 | `CL.INCST.FACTOR.MAIN.ACT` | `ClIncentiveStrategy_FactorMainAct` | TField |  | Number of main actions over the target to be considered as an extra unit. |
| 4 | `CL.INCST.POINTS.MACTION` | `ClIncentiveStrategy_PointsMaction` | TField |  | Number of points to allocate to collector per extra unit of main actions. |
| 5 | `CL.INCST.TRGT.PROD.MACTION` | `ClIncentiveStrategy_TrgtProdMaction` | TField |  | Number of productive outcomes related to main actions required as target for the collector. |
| 6 | `CL.INCST.TRGT.PTS.PRO.MACT` | `ClIncentiveStrategy_TrgtPtsProMact` | TField |  | Number of incentive points allocated to collector if the target productive outcomes related to main actions is reached. |
| 7 | `CL.INCST.PROD.MACTION` | `ClIncentiveStrategy_ProdMaction` | TField |  | Number of productive outcomes related to main actions over the target to be considered as an extra unit. |
| 8 | `CL.INCST.PROD.MACT.POINTS` | `ClIncentiveStrategy_ProdMactPoints` | TField |  | Number of points to allocate to collector per extra unit of productive outcomes related to main actions. |
| 9 | `CL.INCST.TRGT.OTHERS.ACT` | `ClIncentiveStrategy_TrgtOthersAct` | TField |  | Number of other actions (other than main action) required as target for the collector. |
| 10 | `CL.INCST.TRGT.PTS.OACTION` | `ClIncentiveStrategy_TrgtPtsOaction` | TField |  | Number of incentive points allocated to collector if the target other actions is reached. |
| 11 | `CL.INCST.FACTOR.OTHER.ACT` | `ClIncentiveStrategy_FactorOtherAct` | TField |  | Number of other actions over the target to be considered as an extra unit. |
| 12 | `CL.INCST.PTS.OTHER.ACTION` | `ClIncentiveStrategy_PtsOtherAction` | TField |  | Number of points to allocate to collector per extra unit of other actions. |
| 13 | `CL.INCST.TRGT.PROD.OACT` | `ClIncentiveStrategy_TrgtProdOact` | TField |  | Number of productive outcomes related to other actions (other than main action) required as target for the collector. |
| 14 | `CL.INCST.TRGT.PTS.PRO.OACT` | `ClIncentiveStrategy_TrgtPtsProOact` | TField |  |  |
| 15 | `CL.INCST.FACTOR.PRO.OACT` | `ClIncentiveStrategy_FactorProOact` | TField |  | Number of productive outcomes related to other actions over the target to be considered as an extra unit. |
| 16 | `CL.INCST.PTS.PROD.OACTION` | `ClIncentiveStrategy_PtsProdOaction` | TField |  | Number of points to allocate to collector per extra unit of productive outcomes related to other actions. |
| 17 | `CL.INCST.TRGT.NO.PTP` | `ClIncentiveStrategy_TrgtNoPtp` | TField |  | Number of PTP (promise to pay) to be obtained by collector as target. |
| 18 | `CL.INCST.TRGT.PTS.PTP` | `ClIncentiveStrategy_TrgtPtsPtp` | TField |  | Number of incentive points allocated to collector if the target number PTP is reached. |
| 19 | `CL.INCST.FACTOR.PTP` | `ClIncentiveStrategy_FactorPtp` | TField |  | Number of PTP over the target to be considered as an extra unit. |
| 20 | `CL.INCST.PTS.UNIT.PTP` | `ClIncentiveStrategy_PtsUnitPtp` | TField |  | Number of points to allocate to collector per extra unit of PTP. |
| 21 | `CL.INCST.TRGT.PTP.AMT` | `ClIncentiveStrategy_TrgtPtpAmt` | TField |  | Total PTP amount (promise to pay amount) to be obtained by collector as target (Not Used) |
| 22 | `CL.INCST.TRGT.PTP.AMT.PTS` | `ClIncentiveStrategy_TrgtPtpAmtPts` | TField |  | Number of incentive points allocated to collector if the target PTP amount is reached. (Not Used). |
| 23 | `CL.INCST.FACTOR.PTP.AMT` | `ClIncentiveStrategy_FactorPtpAmt` | TField |  | PTP amount over the target to be considered as an extra unit. (Not Used). |
| 24 | `CL.INCST.PTS.UNIT.PTP.AMT` | `ClIncentiveStrategy_PtsUnitPtpAmt` | TField |  | Number of points to allocate to collector per extra unit of PTP amount (Not Used). |
| 25 | `CL.INCST.TRGT.NO.KPTP` | `ClIncentiveStrategy_TrgtNoKptp` | TField |  | Number of KPTP (kept promise to pay) to be achieved by collector as target. |
| 26 | `CL.INCST.TRGT.PTS.KPTP` | `ClIncentiveStrategy_TrgtPtsKptp` | TField |  | Number of incentive points allocated to collector if the target number KPTP is reached. |
| 27 | `CL.INCST.FACTOR.KPTP` | `ClIncentiveStrategy_FactorKptp` | TField |  | Number of KPTP over the target to be considered as an extra unit. |
| 28 | `CL.INCST.PTS.UNIT.KPTP` | `ClIncentiveStrategy_PtsUnitKptp` | TField |  | Number of points to allocate to collector per extra unit of KPTP. |
| 29 | `CL.INCST.TRGT.KPTP.AMT` | `ClIncentiveStrategy_TrgtKptpAmt` | TField |  | Total KPTP amount (kept promise to pay amount) to be achieved by collector as target. |
| 30 | `CL.INCST.TRGT.KPTP.AMT.PTS` | `ClIncentiveStrategy_TrgtKptpAmtPts` | TField |  | Number of incentive points allocated to collector if the target KPTP amount is reached. |
| 31 | `CL.INCST.FACTOR.KPTP.AMT` | `ClIncentiveStrategy_FactorKptpAmt` | TField |  | KPTP amount over the target to be considered as an extra unit. |
| 32 | `CL.INCST.PTS.UNIT.KPTP.AMT` | `ClIncentiveStrategy_PtsUnitKptpAmt` | TField |  | Number of points to allocate to collector per extra unit of KPTP amount. |
| 33 | `CL.INCST.LOCAL.REF` | `ClIncentiveStrategy_LocalRef` |  |  |  |
| 34 | `CL.INCST.RESERVED.5` | `ClIncentiveStrategy_Reserved5` | TField |  |  |
| 35 | `CL.INCST.RESERVED.4` | `ClIncentiveStrategy_Reserved4` | TField |  |  |
| 36 | `CL.INCST.RESERVED.3` | `ClIncentiveStrategy_Reserved3` | TField |  |  |
| 37 | `CL.INCST.RESERVED.2` | `ClIncentiveStrategy_Reserved2` | TField |  |  |
| 38 | `CL.INCST.RESERVED.1` | `ClIncentiveStrategy_Reserved1` | TField |  |  |
| 39 | `CL.INCST.RECORD.STATUS` | `ClIncentiveStrategy_RecordStatus` | String |  |  |
| 40 | `CL.INCST.CURR.NO` | `ClIncentiveStrategy_CurrNo` | String |  |  |
| 41 | `CL.INCST.INPUTTER` | `ClIncentiveStrategy_Inputter` |  |  |  |
| 42 | `CL.INCST.DATE.TIME` | `ClIncentiveStrategy_DateTime` |  |  |  |
| 43 | `CL.INCST.AUTHORISER` | `ClIncentiveStrategy_Authoriser` | String |  |  |
| 44 | `CL.INCST.CO.CODE` | `ClIncentiveStrategy_CoCode` | String |  |  |
| 45 | `CL.INCST.DEPT.CODE` | `ClIncentiveStrategy_DeptCode` | String |  |  |
| 46 | `CL.INCST.AUDITOR.CODE` | `ClIncentiveStrategy_AuditorCode` | String |  |  |
| 47 | `CL.INCST.AUDIT.DATE.TIME` | `ClIncentiveStrategy_AuditDateTime` | String |  |  |
