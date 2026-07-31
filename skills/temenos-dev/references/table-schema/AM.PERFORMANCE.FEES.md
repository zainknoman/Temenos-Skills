# AM.PERFORMANCE.FEES — Table Schema

> Source: `INSERTS/I_F.AM.PERFORMANCE.FEES` in `AM_PerformanceFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PF.PORTFOLIO` | `AmPerformanceFees_Portfolio` | TField |  | Valid SEC.ACC.MASTER. Non editable. |
| 2 | `AM.PF.CALCULATION.DATE` | `AmPerformanceFees_CalculationDate` | TField |  | Calculation date of performance fees. Non editable. |
| 3 | `AM.PF.PERIOD.START` | `AmPerformanceFees_PeriodStart` | TField |  | Start date of this fees period. Non editable. |
| 4 | `AM.PF.PF.FEES` | `AmPerformanceFees_PfFees` | TField |  | Total performance fees calculated for this period. |
| 5 | `AM.PF.ADJUSTMENT.AMT` | `AmPerformanceFees_AdjustmentAmt` | TField |  | It can accept a positive or negative value. |
| 6 | `AM.PF.TOTAL.FEES` | `AmPerformanceFees_TotalFees` | TField |  | Sum of PF.FEES and ADJUSTMENT.AMT |
| 7 | `AM.PF.ACCRUED.FEES` | `AmPerformanceFees_AccruedFees` | TField |  | Total fees accrued for this period in reference currency. Non Editable |
| 8 | `AM.PF.ACCR.FEES.LCY` | `AmPerformanceFees_AccrFeesLcy` | TField |  | Total fees accrued for this period in local currency. Non editable. |
| 9 | `AM.PF.ADJUST.ACCRUAL` | `AmPerformanceFees_AdjustAccrual` | TField |  | Value accepted is Yes or No. If Yes, the difference between ACCRUED.FEES and TOTAL.FEES would be posted as PL entries to bring the PL amount in sync with the amount debited from the customer. If the value is null then it gets defaulted from AM.PF.FEES.CONFIG. |
| 10 | `AM.PF.ACCOUNT.NO` | `AmPerformanceFees_AccountNo` | TField |  | Account number to debit total fees. |
| 11 | `AM.PF.EXCH.RATE.ACC` | `AmPerformanceFees_ExchRateAcc` | TField |  | It contains the exchange rate between the account currency and portfolio reference currency Editable and default to current buy rate. The rate is used to convert performance fees into account currency |
| 12 | `AM.PF.EXCH.RATE.REF` | `AmPerformanceFees_ExchRateRef` | TField |  | It contains the exchange rate between portfolio reference currency and local currency. Editable and defaulted to current mid rate. This is used to fees amount in local currency from portfolio's reference currency to update PL. |
| 13 | `AM.PF.STATUS` | `AmPerformanceFees_Status` | TField |  | This field is initially set to Calculated and set to Posted if COB.POSTING is set after the posting window. User can hold the fees posting within or even after posting window by setting the status to Hold and can be posted anytime after posting window by setting the status to Reviewed. Once the status is set to Posted, the record cannot be edited. |
| 14 | `AM.PF.NOTES` | `AmPerformanceFees_Notes` | TField |  | Its a free text. |
| 15 | `AM.PF.RESERVED.10` | `AmPerformanceFees_Reserved10` | TField |  |  |
| 16 | `AM.PF.RESERVED.9` | `AmPerformanceFees_Reserved9` | TField |  |  |
| 17 | `AM.PF.RESERVED.8` | `AmPerformanceFees_Reserved8` | TField |  |  |
| 18 | `AM.PF.RESERVED.7` | `AmPerformanceFees_Reserved7` | TField |  |  |
| 19 | `AM.PF.RESERVED.6` | `AmPerformanceFees_Reserved6` | TField |  |  |
| 20 | `AM.PF.RESERVED.5` | `AmPerformanceFees_Reserved5` | TField |  |  |
| 21 | `AM.PF.RESERVED.4` | `AmPerformanceFees_Reserved4` | TField |  |  |
| 22 | `AM.PF.RESERVED.3` | `AmPerformanceFees_Reserved3` | TField |  |  |
| 23 | `AM.PF.RESERVED.2` | `AmPerformanceFees_Reserved2` | TField |  |  |
| 24 | `AM.PF.RESERVED.1` | `AmPerformanceFees_Reserved1` | TField |  |  |
| 25 | `AM.PF.LOCAL.REF` | `AmPerformanceFees_LocalRef` |  |  |  |
| 26 | `AM.PF.STATEMENT.NOS` | `AmPerformanceFees_StatementNos` |  |  |  |
| 27 | `AM.PF.OVERRIDE` | `AmPerformanceFees_Override` |  |  |  |
| 28 | `AM.PF.RECORD.STATUS` | `AmPerformanceFees_RecordStatus` | String |  |  |
| 29 | `AM.PF.CURR.NO` | `AmPerformanceFees_CurrNo` | String |  |  |
| 30 | `AM.PF.INPUTTER` | `AmPerformanceFees_Inputter` |  |  |  |
| 31 | `AM.PF.DATE.TIME` | `AmPerformanceFees_DateTime` |  |  |  |
| 32 | `AM.PF.AUTHORISER` | `AmPerformanceFees_Authoriser` | String |  |  |
| 33 | `AM.PF.CO.CODE` | `AmPerformanceFees_CoCode` | String |  |  |
| 34 | `AM.PF.DEPT.CODE` | `AmPerformanceFees_DeptCode` | String |  |  |
| 35 | `AM.PF.AUDITOR.CODE` | `AmPerformanceFees_AuditorCode` | String |  |  |
| 36 | `AM.PF.AUDIT.DATE.TIME` | `AmPerformanceFees_AuditDateTime` | String |  |  |
