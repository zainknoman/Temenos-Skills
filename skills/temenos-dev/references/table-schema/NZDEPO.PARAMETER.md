# NZDEPO.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NZDEPO.PARAMETER` in `NZDEPO_TDBreakCost.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NZDEPO.PARAMETER.BREAK.REASON` | `NzdepoParameter_BreakReason` |  |  |  |
| 2 | `NZDEPO.PARAMETER.PAY.INTEREST` | `NzdepoParameter_PayInterest` |  |  |  |
| 3 | `NZDEPO.PARAMETER.APPLY.PENALTY.INT` | `NzdepoParameter_ApplyPenaltyInt` |  |  |  |
| 4 | `NZDEPO.PARAMETER.HOLIDAY.CHECK` | `NzdepoParameter_HolidayCheck` |  |  |  |
| 5 | `NZDEPO.PARAMETER.MIN.NOTICE.PERIOD` | `NzdepoParameter_MinNoticePeriod` |  |  |  |
| 6 | `NZDEPO.PARAMETER.REF.INT.PROPERTY` | `NzdepoParameter_RefIntProperty` | TField |  | This is the name of the Interest property from which the Reduced Rate has to be derived. |
| 7 | `NZDEPO.PARAMETER.BRKCOST.CHARGE.PROPERTY` | `NzdepoParameter_BrkcostChargeProperty` | TField |  |  |
| 8 | `NZDEPO.PARAMETER.REMAINING.TERM.PERCENT` | `NzdepoParameter_RemainingTermPercent` |  |  |  |
| 9 | `NZDEPO.PARAMETER.PERC.BREAK.INT.PAYABLE` | `NzdepoParameter_PercBreakIntPayable` |  |  |  |
| 10 | `NZDEPO.PARAMETER.PERCENT.WOP` | `NzdepoParameter_PercentWop` | TField |  | Percentage of the original CURACCOUNT balance as on base date (AA.ACCOUNT.DETAILS - BASE.DATE) for which interest will not be reduced. Cannot be greater than 100% - Error message should be generated if user inputs greater than 100% |
| 11 | `NZDEPO.PARAMETER.PROPCLASS.CHANGE.IN.COOLPERIOD` | `NzdepoParameter_PropclassChangeInCoolperiod` |  |  |  |
| 12 | `NZDEPO.PARAMETER.PROPCLASS.FIELD` | `NzdepoParameter_PropclassField` |  |  |  |
| 13 | `NZDEPO.PARAMETER.RESERVED.8` | `NzdepoParameter_Reserved8` | TField |  |  |
| 14 | `NZDEPO.PARAMETER.RESERVED.7` | `NzdepoParameter_Reserved7` | TField |  |  |
| 15 | `NZDEPO.PARAMETER.RESERVED.6` | `NzdepoParameter_Reserved6` | TField |  |  |
| 16 | `NZDEPO.PARAMETER.RESERVED.5` | `NzdepoParameter_Reserved5` | TField |  |  |
| 17 | `NZDEPO.PARAMETER.RESERVED.4` | `NzdepoParameter_Reserved4` | TField |  |  |
| 18 | `NZDEPO.PARAMETER.RESERVED.3` | `NzdepoParameter_Reserved3` | TField |  |  |
| 19 | `NZDEPO.PARAMETER.RESERVED.2` | `NzdepoParameter_Reserved2` | TField |  |  |
| 20 | `NZDEPO.PARAMETER.RESERVED.1` | `NzdepoParameter_Reserved1` | TField |  |  |
| 21 | `NZDEPO.PARAMETER.LOCAL.REF` | `NzdepoParameter_LocalRef` |  |  |  |
| 22 | `NZDEPO.PARAMETER.OVERRIDE` | `NzdepoParameter_Override` |  |  |  |
| 23 | `NZDEPO.PARAMETER.RECORD.STATUS` | `NzdepoParameter_RecordStatus` | String |  |  |
| 24 | `NZDEPO.PARAMETER.CURR.NO` | `NzdepoParameter_CurrNo` | String |  |  |
| 25 | `NZDEPO.PARAMETER.INPUTTER` | `NzdepoParameter_Inputter` |  |  |  |
| 26 | `NZDEPO.PARAMETER.DATE.TIME` | `NzdepoParameter_DateTime` |  |  |  |
| 27 | `NZDEPO.PARAMETER.AUTHORISER` | `NzdepoParameter_Authoriser` | String |  |  |
| 28 | `NZDEPO.PARAMETER.CO.CODE` | `NzdepoParameter_CoCode` | String |  |  |
| 29 | `NZDEPO.PARAMETER.DEPT.CODE` | `NzdepoParameter_DeptCode` | String |  |  |
| 30 | `NZDEPO.PARAMETER.AUDITOR.CODE` | `NzdepoParameter_AuditorCode` | String |  |  |
| 31 | `NZDEPO.PARAMETER.AUDIT.DATE.TIME` | `NzdepoParameter_AuditDateTime` | String |  |  |
