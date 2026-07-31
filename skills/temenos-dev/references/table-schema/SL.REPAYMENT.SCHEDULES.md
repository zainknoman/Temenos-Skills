# SL.REPAYMENT.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.SL.REPAYMENT.SCHEDULES` in `SL_Repayment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.REP.RPT.START.DATE` | `SlRepaymentSchedules_RptStartDate` |  |  |  |
| 2 | `SL.REP.RPT.END.DATE` | `SlRepaymentSchedules_RptEndDate` |  |  |  |
| 3 | `SL.REP.RPT.FQY` | `SlRepaymentSchedules_RptFqy` |  |  |  |
| 4 | `SL.REP.RPT.AMOUNT` | `SlRepaymentSchedules_RptAmount` |  |  |  |
| 5 | `SL.REP.RPT.PERC` | `SlRepaymentSchedules_RptPerc` |  |  |  |
| 6 | `SL.REP.NXT.RPT.DATE` | `SlRepaymentSchedules_NxtRptDate` |  |  |  |
| 7 | `SL.REP.NXT.RPT.AMT` | `SlRepaymentSchedules_NxtRptAmt` |  |  |  |
| 8 | `SL.REP.ANNUITY.TYPE` | `SlRepaymentSchedules_AnnuityType` | TField |  | Field to indicate whether the repayment schedule is ANNUITY type or not. Annuity type schedules are permitted only for loan level schedules. YES would mean that repayment amount comprises principal and interest (annuity type). NO would mean repayment amount is only towards principal. If this field contains a value YES, INT.EFF.DATE may not be greater than RPT.START.DATE. Value YES is allowed only if repayment schedules are defined at SL.LOAN level and not Facility level. Effective the RPT.START.DATE the contract would have Annuity schedules and interest and principal would be scheduled on the same date as cycled for principal. Validation Rules: Only allowed values are YES and NO If this field contains a value YES, INT.EFF.DATE may not be greater than RPT.START.DATE. |
| 9 | `SL.REP.INT.EFF.DATE` | `SlRepaymentSchedules_IntEffDate` |  |  |  |
| 10 | `SL.REP.INT.DUE.FQY` | `SlRepaymentSchedules_IntDueFqy` |  |  |  |
| 11 | `SL.REP.INT.AMOUNT` | `SlRepaymentSchedules_IntAmount` |  |  |  |
| 12 | `SL.REP.BASE.DATE` | `SlRepaymentSchedules_BaseDate` | TField |  | This field provides the user options to specify the basis under which subsequent event dates will be derived. The options are; BASE System would use the first scheduled date entered to compute the subsequent event date. PREV System will use the last computed scheduled date to compute subsequent event date Validation Rules: Only allowed values are BASE and PREV . |
| 13 | `SL.REP.FWD.BWD.KEY` | `SlRepaymentSchedules_FwdBwdKey` | TField |  | This field indicates the method that will be followed for the generation of schedules and the action that will be taken if the derived date is a non-working day. FWD The system will go forward to the next working day BWD System will go backward to the last working day FSM System will go forward to the next working day if within the same month. Else it will go backward to the last working day CAL The system will use the derived date without change, irrespective of the fact whether it is a working day or not Validation Rules: Allowed values are FWD, BWD, FSM and CAL |
| 14 | `SL.REP.R.SCH.FQY` | `SlRepaymentSchedules_RSchFqy` | TField |  | Frequency at which the rate revision, if any, needs to be applied. Validation Rules: Input allowed to this field only with interest type as periodic automatic (3)" |
| 15 | `SL.REP.REPAY.TYPE` | `SlRepaymentSchedules_RepayType` |  |  |  |
| 16 | `SL.REP.REPAY.DATE` | `SlRepaymentSchedules_RepayDate` |  |  |  |
| 17 | `SL.REP.REPAY.AMOUNT` | `SlRepaymentSchedules_RepayAmount` |  |  |  |
| 18 | `SL.REP.REPAY.PERC` | `SlRepaymentSchedules_RepayPerc` |  |  |  |
| 19 | `SL.REP.DELIVERY.CUST` | `SlRepaymentSchedules_DeliveryCust` |  |  |  |
| 20 | `SL.REP.ACTIVITY.CODE` | `SlRepaymentSchedules_ActivityCode` |  |  |  |
| 21 | `SL.REP.ACTIVITY.DATE` | `SlRepaymentSchedules_ActivityDate` |  |  |  |
| 22 | `SL.REP.PRIOR.DAYS` | `SlRepaymentSchedules_PriorDays` |  |  |  |
| 23 | `SL.REP.MSG.TYPE` | `SlRepaymentSchedules_MsgType` |  |  |  |
| 24 | `SL.REP.MSG.CLASS` | `SlRepaymentSchedules_MsgClass` |  |  |  |
| 25 | `SL.REP.OVR.CARRIER` | `SlRepaymentSchedules_OvrCarrier` |  |  |  |
| 26 | `SL.REP.SEND.MSG` | `SlRepaymentSchedules_SendMsg` |  |  |  |
| 27 | `SL.REP.MSG.DATE` | `SlRepaymentSchedules_MsgDate` |  |  |  |
| 28 | `SL.REP.DELIVERY.REF` | `SlRepaymentSchedules_DeliveryRef` |  |  |  |
| 29 | `SL.REP.AMORT.TERM` | `SlRepaymentSchedules_AmortTerm` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 30 | `SL.REP.ANNUITY.REPAY.AMT` | `SlRepaymentSchedules_AnnuityRepayAmt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 31 | `SL.REP.INT.RST.BUS.DAYS` | `SlRepaymentSchedules_IntRstBusDays` |  |  |  |
| 32 | `SL.REP.RESERVED7` | `SlRepaymentSchedules_Reserved7` | TField |  |  |
| 33 | `SL.REP.RESERVED6` | `SlRepaymentSchedules_Reserved6` | TField |  |  |
| 34 | `SL.REP.RESERVED5` | `SlRepaymentSchedules_Reserved5` | TField |  |  |
| 35 | `SL.REP.RESERVED4` | `SlRepaymentSchedules_Reserved4` | TField |  |  |
| 36 | `SL.REP.RESERVED3` | `SlRepaymentSchedules_Reserved3` | TField |  |  |
| 37 | `SL.REP.RESERVED2` | `SlRepaymentSchedules_Reserved2` | TField |  |  |
| 38 | `SL.REP.LOCAL.REF` | `SlRepaymentSchedules_LocalRef` |  |  |  |
| 39 | `SL.REP.OVERRIDE` | `SlRepaymentSchedules_Override` |  |  |  |
| 40 | `SL.REP.RECORD.STATUS` | `SlRepaymentSchedules_RecordStatus` | String |  |  |
| 41 | `SL.REP.CURR.NO` | `SlRepaymentSchedules_CurrNo` | String |  |  |
| 42 | `SL.REP.INPUTTER` | `SlRepaymentSchedules_Inputter` |  |  |  |
| 43 | `SL.REP.DATE.TIME` | `SlRepaymentSchedules_DateTime` |  |  |  |
| 44 | `SL.REP.AUTHORISER` | `SlRepaymentSchedules_Authoriser` | String |  |  |
| 45 | `SL.REP.CO.CODE` | `SlRepaymentSchedules_CoCode` | String |  |  |
| 46 | `SL.REP.DEPT.CODE` | `SlRepaymentSchedules_DeptCode` | String |  |  |
| 47 | `SL.REP.AUDITOR.CODE` | `SlRepaymentSchedules_AuditorCode` | String |  |  |
| 48 | `SL.REP.AUDIT.DATE.TIME` | `SlRepaymentSchedules_AuditDateTime` | String |  |  |
