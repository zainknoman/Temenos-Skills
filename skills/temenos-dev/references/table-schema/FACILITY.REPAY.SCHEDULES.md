# FACILITY.REPAY.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.FACILITY.REPAY.SCHEDULES` in `SL_Facility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FAC.RS.FACILITY.CCY` | `FacilityRepaySchedules_FacilityCcy` | TField |  | This field will be defaulted with the FACILITY currency. NOINPUT and CCY type field. |
| 2 | `FAC.RS.TOTAL.REPAY.AMT` | `FacilityRepaySchedules_TotalRepayAmt` | TField |  | This field will be defaulted with the First tranche redemption amount. For unscheduled repayment the amount can be user input Validation Rules: Field value cannot be null Amount cannot be negative. Amount cannot be greater the sum of the loan amounts to be repaid. |
| 3 | `FAC.RS.TR.RPY.DATE` | `FacilityRepaySchedules_TrRpyDate` | TField |  | This field will be defaulted with the Tranche redemption date for scheduled type of transaction . For unscheduled type of transaction field will always be defaulted with TODAY. |
| 4 | `FAC.RS.PRO.RATA` | `FacilityRepaySchedules_ProRata` | TField |  | The value in the field will determine on the settlement of the total repayment amount across the Loan amount. should either be settled in PRO.RATA or in a adhoc settlement. Validation Rules: Allowed values are YES/NO Default value is NO |
| 5 | `FAC.RS.LOAN.CCY` | `FacilityRepaySchedules_LoanCcy` |  |  |  |
| 6 | `FAC.RS.LOAN.ID` | `FacilityRepaySchedules_LoanId` |  |  |  |
| 7 | `FAC.RS.LOAN.AMT` | `FacilityRepaySchedules_LoanAmt` |  |  |  |
| 8 | `FAC.RS.LOAN.BCCY.AMT` | `FacilityRepaySchedules_LoanBccyAmt` |  |  |  |
| 9 | `FAC.RS.LOAN.REPAY.AMT` | `FacilityRepaySchedules_LoanRepayAmt` |  |  |  |
| 10 | `FAC.RS.LN.REP.BCY.AMT` | `FacilityRepaySchedules_LnRepBcyAmt` |  |  |  |
| 11 | `FAC.RS.LN.END.PRD.DT` | `FacilityRepaySchedules_LnEndPrdDt` |  |  |  |
| 12 | `FAC.RS.REP.SCH.TYPE` | `FacilityRepaySchedules_RepSchType` | TField |  | This field is used to define repayment schedule order for the cancellation of the schedules in SL.REPAY.SCHEDS. PRO.RATA � Entire schedule pro-rata basis according to loan size FIRST - Will repay schedules from first repay schedule date LAST - Will repay schedules from last repay schedule date . |
| 13 | `FAC.RS.TR.REDEM.TYPE` | `FacilityRepaySchedules_TrRedemType` | TField |  | This field will decide on scheduled or Achoc settlement of Loans under the tranche. validation rules Allowed values are SCHEDULED_UNSCHEDULED. Default is value SCHEDULED for tranche redemption Atleast one loan should fall on the Tranche redemption date for scheduled type repayment. |
| 14 | `FAC.RS.RESERVED4` | `FacilityRepaySchedules_Reserved4` | TField |  |  |
| 15 | `FAC.RS.RESERVED3` | `FacilityRepaySchedules_Reserved3` | TField |  |  |
| 16 | `FAC.RS.RESERVED2` | `FacilityRepaySchedules_Reserved2` | TField |  |  |
| 17 | `FAC.RS.RESERVED1` | `FacilityRepaySchedules_Reserved1` | TField |  |  |
| 18 | `FAC.RS.LOCAL.REF` | `FacilityRepaySchedules_LocalRef` |  |  |  |
| 19 | `FAC.RS.OVERRIDE` | `FacilityRepaySchedules_Override` |  |  |  |
| 20 | `FAC.RS.RECORD.STATUS` | `FacilityRepaySchedules_RecordStatus` | String |  |  |
| 21 | `FAC.RS.CURR.NO` | `FacilityRepaySchedules_CurrNo` | String |  |  |
| 22 | `FAC.RS.INPUTTER` | `FacilityRepaySchedules_Inputter` |  |  |  |
| 23 | `FAC.RS.DATE.TIME` | `FacilityRepaySchedules_DateTime` |  |  |  |
| 24 | `FAC.RS.AUTHORISER` | `FacilityRepaySchedules_Authoriser` | String |  |  |
| 25 | `FAC.RS.CO.CODE` | `FacilityRepaySchedules_CoCode` | String |  |  |
| 26 | `FAC.RS.DEPT.CODE` | `FacilityRepaySchedules_DeptCode` | String |  |  |
| 27 | `FAC.RS.AUDITOR.CODE` | `FacilityRepaySchedules_AuditorCode` | String |  |  |
| 28 | `FAC.RS.AUDIT.DATE.TIME` | `FacilityRepaySchedules_AuditDateTime` | String |  |  |
