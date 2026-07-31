# USIRAC.DISTRIBUTION.PLAN — Table Schema

> Source: `INSERTS/I_F.USIRAC.DISTRIBUTION.PLAN` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IRA.DIST.PLAN` | `UsiracDistributionPlan_Plan` |  |  |  |
| 2 | `IRA.DIST.RMD.WAIVE` | `UsiracDistributionPlan_RmdWaive` |  |  |  |
| 3 | `IRA.DIST.WAIVE.REASON` | `UsiracDistributionPlan_WaiveReason` |  |  |  |
| 4 | `IRA.DIST.RMD.INDICATOR` | `UsiracDistributionPlan_RmdIndicator` |  |  |  |
| 5 | `IRA.DIST.DISTRIBUTION.TYPE` | `UsiracDistributionPlan_DistributionType` |  |  |  |
| 6 | `IRA.DIST.EARLY.DISTRIBUTION.REASON` | `UsiracDistributionPlan_EarlyDistributionReason` |  |  |  |
| 7 | `IRA.DIST.RMD.CALCULATION` | `UsiracDistributionPlan_RmdCalculation` |  |  |  |
| 8 | `IRA.DIST.RMD.CALC.FREQ` | `UsiracDistributionPlan_RmdCalcFreq` |  |  |  |
| 9 | `IRA.DIST.DISTRIBUTION.AMT` | `UsiracDistributionPlan_DistributionAmt` |  |  |  |
| 10 | `IRA.DIST.DISTRIBUTION.START.DATE` | `UsiracDistributionPlan_DistributionStartDate` |  |  |  |
| 11 | `IRA.DIST.WAIVE.BANK.PENALTY` | `UsiracDistributionPlan_WaiveBankPenalty` |  |  |  |
| 12 | `IRA.DIST.DISTRIBUTION.FREQUENCY` | `UsiracDistributionPlan_DistributionFrequency` |  |  |  |
| 13 | `IRA.DIST.PAY.METHOD` | `UsiracDistributionPlan_PayMethod` |  |  |  |
| 14 | `IRA.DIST.DISTRIBUTION.ACCOUNT` | `UsiracDistributionPlan_DistributionAccount` |  |  |  |
| 15 | `IRA.DIST.RECIPIENT` | `UsiracDistributionPlan_Recipient` |  |  |  |
| 16 | `IRA.DIST.DISTRIBUTION.SEQ` | `UsiracDistributionPlan_DistributionSeq` |  |  |  |
| 17 | `IRA.DIST.ACCOUNT` | `UsiracDistributionPlan_Account` |  |  |  |
| 18 | `IRA.DIST.WV.BANK.PENALTY.REASON` | `UsiracDistributionPlan_WvBankPenaltyReason` |  |  |  |
| 19 | `IRA.DIST.RESERVED.19` | `UsiracDistributionPlan_Reserved19` |  |  |  |
| 20 | `IRA.DIST.RESERVED.18` | `UsiracDistributionPlan_Reserved18` |  |  |  |
| 21 | `IRA.DIST.RESERVED.17` | `UsiracDistributionPlan_Reserved17` |  |  |  |
| 22 | `IRA.DIST.RESERVED.16` | `UsiracDistributionPlan_Reserved16` |  |  |  |
| 23 | `IRA.DIST.RESERVED.15` | `UsiracDistributionPlan_Reserved15` |  |  |  |
| 24 | `IRA.DIST.RESERVED.14` | `UsiracDistributionPlan_Reserved14` |  |  |  |
| 25 | `IRA.DIST.RESERVED.13` | `UsiracDistributionPlan_Reserved13` |  |  |  |
| 26 | `IRA.DIST.RESERVED.12` | `UsiracDistributionPlan_Reserved12` |  |  |  |
| 27 | `IRA.DIST.RESERVED.11` | `UsiracDistributionPlan_Reserved11` |  |  |  |
| 28 | `IRA.DIST.RESERVED.10` | `UsiracDistributionPlan_Reserved10` | TField |  |  |
| 29 | `IRA.DIST.RESERVED.9` | `UsiracDistributionPlan_Reserved9` | TField |  |  |
| 30 | `IRA.DIST.RESERVED.8` | `UsiracDistributionPlan_Reserved8` | TField |  |  |
| 31 | `IRA.DIST.RESERVED.7` | `UsiracDistributionPlan_Reserved7` | TField |  |  |
| 32 | `IRA.DIST.RESERVED.6` | `UsiracDistributionPlan_Reserved6` | TField |  |  |
| 33 | `IRA.DIST.RESERVED.5` | `UsiracDistributionPlan_Reserved5` | TField |  |  |
| 34 | `IRA.DIST.RESERVED.4` | `UsiracDistributionPlan_Reserved4` | TField |  |  |
| 35 | `IRA.DIST.RESERVED.3` | `UsiracDistributionPlan_Reserved3` | TField |  |  |
| 36 | `IRA.DIST.RESERVED.2` | `UsiracDistributionPlan_Reserved2` | TField |  |  |
| 37 | `IRA.DIST.RESERVED.1` | `UsiracDistributionPlan_Reserved1` | TField |  |  |
| 38 | `IRA.DIST.LOCAL.REF` | `UsiracDistributionPlan_LocalRef` |  |  |  |
| 39 | `IRA.DIST.OVERRIDE` | `UsiracDistributionPlan_Override` |  |  |  |
| 40 | `IRA.DIST.RECORD.STATUS` | `UsiracDistributionPlan_RecordStatus` | String |  |  |
| 41 | `IRA.DIST.CURR.NO` | `UsiracDistributionPlan_CurrNo` | String |  |  |
| 42 | `IRA.DIST.INPUTTER` | `UsiracDistributionPlan_Inputter` |  |  |  |
| 43 | `IRA.DIST.DATE.TIME` | `UsiracDistributionPlan_DateTime` |  |  |  |
| 44 | `IRA.DIST.AUTHORISER` | `UsiracDistributionPlan_Authoriser` | String |  |  |
| 45 | `IRA.DIST.CO.CODE` | `UsiracDistributionPlan_CoCode` | String |  |  |
| 46 | `IRA.DIST.DEPT.CODE` | `UsiracDistributionPlan_DeptCode` | String |  |  |
| 47 | `IRA.DIST.AUDITOR.CODE` | `UsiracDistributionPlan_AuditorCode` | String |  |  |
| 48 | `IRA.DIST.AUDIT.DATE.TIME` | `UsiracDistributionPlan_AuditDateTime` | String |  |  |
