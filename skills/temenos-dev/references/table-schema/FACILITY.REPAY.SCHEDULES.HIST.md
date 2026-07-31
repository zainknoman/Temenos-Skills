# FACILITY.REPAY.SCHEDULES.HIST — Table Schema

> Source: `INSERTS/I_F.FACILITY.REPAY.SCHEDULES.HIST` in `SL_Facility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FAC.RSH.FACILITY.CCY` | `FacilityRepaySchedulesHist_FacilityCcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `FAC.RSH.TOTAL.REPAY.AMT` | `FacilityRepaySchedulesHist_TotalRepayAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `FAC.RSH.TR.RPY.DATE` | `FacilityRepaySchedulesHist_TrRpyDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `FAC.RSH.PRO.RATA` | `FacilityRepaySchedulesHist_ProRata` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `FAC.RSH.LOAN.CCY` | `FacilityRepaySchedulesHist_LoanCcy` |  |  |  |
| 6 | `FAC.RSH.LOAN.ID` | `FacilityRepaySchedulesHist_LoanId` |  |  |  |
| 7 | `FAC.RSH.LOAN.AMT` | `FacilityRepaySchedulesHist_LoanAmt` |  |  |  |
| 8 | `FAC.RSH.LOAN.BCCY.AMT` | `FacilityRepaySchedulesHist_LoanBccyAmt` |  |  |  |
| 9 | `FAC.RSH.LOAN.REPAY.AMT` | `FacilityRepaySchedulesHist_LoanRepayAmt` |  |  |  |
| 10 | `FAC.RSH.LN.REP.BCY.AMT` | `FacilityRepaySchedulesHist_LnRepBcyAmt` |  |  |  |
| 11 | `FAC.RSH.LN.END.PRD.DT` | `FacilityRepaySchedulesHist_LnEndPrdDt` |  |  |  |
| 12 | `FAC.RSH.REP.SCH.TYPE` | `FacilityRepaySchedulesHist_RepSchType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `FAC.RSH.TR.REDEM.TYPE` | `FacilityRepaySchedulesHist_TrRedemType` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
