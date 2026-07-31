# TEST.ACCRUAL — Table Schema

> Source: `INSERTS/I_F.TEST.ACCRUAL` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TA.DESCRIPTION` | `TestAccrual_Description` |  |  |  |
| 2 | `TA.EB.ACCRUAL.PARAM` | `TestAccrual_EbAccrualParam` |  |  |  |
| 3 | `TA.CURRENCY` | `TestAccrual_Currency` |  |  |  |
| 4 | `TA.PRINCIPAL` | `TestAccrual_Principal` |  |  |  |
| 5 | `TA.CONTRACT.START` | `TestAccrual_ContractStart` |  |  |  |
| 6 | `TA.CONTRACT.END` | `TestAccrual_ContractEnd` |  |  |  |
| 7 | `TA.INTEREST.DAY.BASIS` | `TestAccrual_InterestDayBasis` |  |  |  |
| 8 | `TA.ACCRUE.TO.DATE` | `TestAccrual_AccrueToDate` |  |  |  |
| 9 | `TA.LAST.INT.DATE` | `TestAccrual_LastIntDate` |  |  |  |
| 10 | `TA.NEXT.INT.DATE` | `TestAccrual_NextIntDate` |  |  |  |
| 11 | `TA.CLEAR.ACCR.DATA` | `TestAccrual_ClearAccrData` |  |  |  |
| 12 | `TA.EB.ROUNDING.RULE` | `TestAccrual_EbRoundingRule` |  |  |  |
| 13 | `TA.CUSTOMER` | `TestAccrual_Customer` |  |  |  |
| 14 | `TA.ADJUST.DATE` | `TestAccrual_AdjustDate` |  |  |  |
| 15 | `TA.INT.PERIODS` | `TestAccrual_IntPeriods` |  |  |  |
| 16 | `TA.EFF.INT.RATE` | `TestAccrual_EffIntRate` |  |  |  |
| 17 | `TA.COMPOUND.FREQ` | `TestAccrual_CompoundFreq` |  |  |  |
| 18 | `TA.RESERVED1` | `TestAccrual_Reserved1` |  |  |  |
| 19 | `TA.INTEREST.DATE` | `TestAccrual_InterestDate` |  |  |  |
| 20 | `TA.RATE.TIER.TYPE` | `TestAccrual_RateTierType` |  |  |  |
| 21 | `TA.INTEREST.RATE` | `TestAccrual_InterestRate` |  |  |  |
| 22 | `TA.TIER.AMOUNT` | `TestAccrual_TierAmount` |  |  |  |
| 23 | `TA.TIER.PERCENT` | `TestAccrual_TierPercent` |  |  |  |
| 24 | `TA.MOVEMENT.DATE` | `TestAccrual_MovementDate` |  |  |  |
| 25 | `TA.MOVEMENT.TYPE` | `TestAccrual_MovementType` |  |  |  |
| 26 | `TA.MOVEMENT.AMT` | `TestAccrual_MovementAmt` |  |  |  |
| 27 | `TA.PRIN.IN.DATE` | `TestAccrual_PrinInDate` |  |  |  |
| 28 | `TA.PRIN.IN.AMT` | `TestAccrual_PrinInAmt` |  |  |  |
| 29 | `TA.PRIN.OUT.DATE` | `TestAccrual_PrinOutDate` |  |  |  |
| 30 | `TA.PRIN.OUT.AMT` | `TestAccrual_PrinOutAmt` |  |  |  |
| 31 | `TA.ACCR.FROM.DATE` | `TestAccrual_AccrFromDate` |  |  |  |
| 32 | `TA.ACCR.TO.DATE` | `TestAccrual_AccrToDate` |  |  |  |
| 33 | `TA.ACCR.DAYS` | `TestAccrual_AccrDays` |  |  |  |
| 34 | `TA.ACCR.PRIN` | `TestAccrual_AccrPrin` |  |  |  |
| 35 | `TA.ACCR.RATE` | `TestAccrual_AccrRate` |  |  |  |
| 36 | `TA.ACCR.AMT` | `TestAccrual_AccrAmt` |  |  |  |
| 37 | `TA.ACCR.ACT.AMT` | `TestAccrual_AccrActAmt` |  |  |  |
| 38 | `TA.THIS.MONTH.ACCR` | `TestAccrual_ThisMonthAccr` |  |  |  |
| 39 | `TA.PREV.MONTH.ACCR` | `TestAccrual_PrevMonthAccr` |  |  |  |
| 40 | `TA.PREV.YEAR.ACCR` | `TestAccrual_PrevYearAccr` |  |  |  |
| 41 | `TA.OTS.AMOUNT` | `TestAccrual_OtsAmount` |  |  |  |
| 42 | `TA.RESERVED.4` | `TestAccrual_Reserved4` |  |  |  |
| 43 | `TA.RESERVED.3` | `TestAccrual_Reserved3` |  |  |  |
| 44 | `TA.RESERVED.2` | `TestAccrual_Reserved2` |  |  |  |
| 45 | `TA.RESERVED.1` | `TestAccrual_Reserved1` |  |  |  |
| 46 | `TA.RECORD.STATUS` | `TestAccrual_RecordStatus` |  |  |  |
| 47 | `TA.CURR.NO` | `TestAccrual_CurrNo` |  |  |  |
| 48 | `TA.INPUTTER` | `TestAccrual_Inputter` |  |  |  |
| 49 | `TA.DATE.TIME` | `TestAccrual_DateTime` |  |  |  |
| 50 | `TA.AUTHORISER` | `TestAccrual_Authoriser` |  |  |  |
| 51 | `TA.CO.CODE` | `TestAccrual_CoCode` |  |  |  |
| 52 | `TA.DEPT.CODE` | `TestAccrual_DeptCode` |  |  |  |
| 53 | `TA.AUDITOR.CODE` | `TestAccrual_AuditorCode` |  |  |  |
| 54 | `TA.AUDIT.DATE.TIME` | `TestAccrual_AuditDateTime` |  |  |  |
