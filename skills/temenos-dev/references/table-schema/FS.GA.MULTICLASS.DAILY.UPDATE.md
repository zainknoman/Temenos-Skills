# FS.GA.MULTICLASS.DAILY.UPDATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.MULTICLASS.DAILY.UPDATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.MULTICLASS.DAILY.UPDATE.PARENT.REF.ID` | `FsGaMulticlassDailyUpdate_ParentRefId` |  |  |  |
| 2 | `FS.GA.MULTICLASS.DAILY.UPDATE.ORA.ROWID` | `FsGaMulticlassDailyUpdate_OraRowid` |  |  |  |
| 3 | `FS.GA.MULTICLASS.DAILY.UPDATE.FUND.ID` | `FsGaMulticlassDailyUpdate_FundId` |  |  |  |
| 4 | `FS.GA.MULTICLASS.DAILY.UPDATE.VALUATION.TYPE` | `FsGaMulticlassDailyUpdate_ValuationType` |  |  |  |
| 5 | `FS.GA.MULTICLASS.DAILY.UPDATE.DATE.OF.NAV` | `FsGaMulticlassDailyUpdate_DateOfNav` |  |  |  |
| 6 | `FS.GA.MULTICLASS.DAILY.UPDATE.SHARE.CLASS.CODE` | `FsGaMulticlassDailyUpdate_ShareClassCode` |  |  |  |
| 7 | `FS.GA.MULTICLASS.DAILY.UPDATE.SHARE.QUANTITY` | `FsGaMulticlassDailyUpdate_ShareQuantity` |  |  |  |
| 8 | `FS.GA.MULTICLASS.DAILY.UPDATE.SETTLED.SHARES` | `FsGaMulticlassDailyUpdate_SettledShares` |  |  |  |
| 9 | `FS.GA.MULTICLASS.DAILY.UPDATE.PART.AMOUNT` | `FsGaMulticlassDailyUpdate_PartAmount` |  |  |  |
| 10 | `FS.GA.MULTICLASS.DAILY.UPDATE.NAV.PER.UNIT` | `FsGaMulticlassDailyUpdate_NavPerUnit` |  |  |  |
| 11 | `FS.GA.MULTICLASS.DAILY.UPDATE.YEAR.END` | `FsGaMulticlassDailyUpdate_YearEnd` |  |  |  |
| 12 | `FS.GA.MULTICLASS.DAILY.UPDATE.UNROUNDED.NAV.PER.UNIT` | `FsGaMulticlassDailyUpdate_UnroundedNavPerUnit` |  |  |  |
| 13 | `FS.GA.MULTICLASS.DAILY.UPDATE.CAPSTOCK.SUBSCRIPTION.PRICE` | `FsGaMulticlassDailyUpdate_CapstockSubscriptionPrice` |  |  |  |
| 14 | `FS.GA.MULTICLASS.DAILY.UPDATE.CAPSTOCK.REDEMPTION.PRICE` | `FsGaMulticlassDailyUpdate_CapstockRedemptionPrice` |  |  |  |
| 15 | `FS.GA.MULTICLASS.DAILY.UPDATE.COEFFICIENT` | `FsGaMulticlassDailyUpdate_Coefficient` |  |  |  |
| 16 | `FS.GA.MULTICLASS.DAILY.UPDATE.CAPSTOCK.SUBSCRIPTION.FEE` | `FsGaMulticlassDailyUpdate_CapstockSubscriptionFee` |  |  |  |
| 17 | `FS.GA.MULTICLASS.DAILY.UPDATE.UNROUNDED.SUBSCRIPTION.PRICE` | `FsGaMulticlassDailyUpdate_UnroundedSubscriptionPrice` |  |  |  |
| 18 | `FS.GA.MULTICLASS.DAILY.UPDATE.UNROUNDED.REDEMPTION.PRICE` | `FsGaMulticlassDailyUpdate_UnroundedRedemptionPrice` |  |  |  |
| 19 | `FS.GA.MULTICLASS.DAILY.UPDATE.DIVIDEND.PER.SHARE` | `FsGaMulticlassDailyUpdate_DividendPerShare` |  |  |  |
| 20 | `FS.GA.MULTICLASS.DAILY.UPDATE.CUMULATIVE.RATE` | `FsGaMulticlassDailyUpdate_CumulativeRate` |  |  |  |
| 21 | `FS.GA.MULTICLASS.DAILY.UPDATE.CUMULATIVE.YIELD.DIFFERENCE` | `FsGaMulticlassDailyUpdate_CumulativeYieldDifference` |  |  |  |
| 22 | `FS.GA.MULTICLASS.DAILY.UPDATE.ROUNDINGDIFFERENCE` | `FsGaMulticlassDailyUpdate_Roundingdifference` |  |  |  |
| 23 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.NAV` | `FsGaMulticlassDailyUpdate_PreviousNav` |  |  |  |
| 24 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.OUTSTANDING.SHARES` | `FsGaMulticlassDailyUpdate_PreviousOutstandingShares` |  |  |  |
| 25 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.SUBSCRIBED.SHARES` | `FsGaMulticlassDailyUpdate_PreviousSubscribedShares` |  |  |  |
| 26 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.REDEMPTION.SHARES` | `FsGaMulticlassDailyUpdate_PreviousRedemptionShares` |  |  |  |
| 27 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.SUBSCRIPTION.AMOUNT` | `FsGaMulticlassDailyUpdate_PreviousSubscriptionAmount` |  |  |  |
| 28 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.REDEMPTION.AMOUNT` | `FsGaMulticlassDailyUpdate_PreviousRedemptionAmount` |  |  |  |
| 29 | `FS.GA.MULTICLASS.DAILY.UPDATE.COEFFICIENT1` | `FsGaMulticlassDailyUpdate_Coefficient1` |  |  |  |
| 30 | `FS.GA.MULTICLASS.DAILY.UPDATE.COEFFICIENT2` | `FsGaMulticlassDailyUpdate_Coefficient2` |  |  |  |
| 31 | `FS.GA.MULTICLASS.DAILY.UPDATE.NAV.PER.UNIT.BID` | `FsGaMulticlassDailyUpdate_NavPerUnitBid` |  |  |  |
| 32 | `FS.GA.MULTICLASS.DAILY.UPDATE.NAV.PER.UNIT.OFFER` | `FsGaMulticlassDailyUpdate_NavPerUnitOffer` |  |  |  |
| 33 | `FS.GA.MULTICLASS.DAILY.UPDATE.CALENDAR.DIVIDEND.DIST.RATIO` | `FsGaMulticlassDailyUpdate_CalendarDividendDistRatio` |  |  |  |
| 34 | `FS.GA.MULTICLASS.DAILY.UPDATE.YIELD.DIVIDEND.DIST.RATIO` | `FsGaMulticlassDailyUpdate_YieldDividendDistRatio` |  |  |  |
| 35 | `FS.GA.MULTICLASS.DAILY.UPDATE.ANNUAL.YIELD.DIV.DIST.RATIO` | `FsGaMulticlassDailyUpdate_AnnualYieldDivDistRatio` |  |  |  |
| 36 | `FS.GA.MULTICLASS.DAILY.UPDATE.CUMULATIVE.NET.INCOME.MONTH` | `FsGaMulticlassDailyUpdate_CumulativeNetIncomeMonth` |  |  |  |
| 37 | `FS.GA.MULTICLASS.DAILY.UPDATE.CUMULATIVE.NET.INCOME.YEAR` | `FsGaMulticlassDailyUpdate_CumulativeNetIncomeYear` |  |  |  |
| 38 | `FS.GA.MULTICLASS.DAILY.UPDATE.7DAYS.SIMPLE.YIELD` | `FsGaMulticlassDailyUpdate_7daysSimpleYield` |  |  |  |
| 39 | `FS.GA.MULTICLASS.DAILY.UPDATE.30DAYS.SIMPLE.YIELD` | `FsGaMulticlassDailyUpdate_30daysSimpleYield` |  |  |  |
| 40 | `FS.GA.MULTICLASS.DAILY.UPDATE.7DAYS.EFFECTIVE.YIELD` | `FsGaMulticlassDailyUpdate_7daysEffectiveYield` |  |  |  |
| 41 | `FS.GA.MULTICLASS.DAILY.UPDATE.30DAYS.EFFECTIVE.YIELD` | `FsGaMulticlassDailyUpdate_30daysEffectiveYield` |  |  |  |
| 42 | `FS.GA.MULTICLASS.DAILY.UPDATE.DAYS.LAST.NAV` | `FsGaMulticlassDailyUpdate_DaysLastNav` |  |  |  |
| 43 | `FS.GA.MULTICLASS.DAILY.UPDATE.CALCULATED.DIV.DIST.RATIO` | `FsGaMulticlassDailyUpdate_CalculatedDivDistRatio` |  |  |  |
| 44 | `FS.GA.MULTICLASS.DAILY.UPDATE.GROUP1.SPECIFICATION` | `FsGaMulticlassDailyUpdate_Group1Specification` |  |  |  |
| 45 | `FS.GA.MULTICLASS.DAILY.UPDATE.GROUP2.SPECIFICATION` | `FsGaMulticlassDailyUpdate_Group2Specification` |  |  |  |
| 46 | `FS.GA.MULTICLASS.DAILY.UPDATE.GROSS.NAV.PER.SHARE` | `FsGaMulticlassDailyUpdate_GrossNavPerShare` |  |  |  |
| 47 | `FS.GA.MULTICLASS.DAILY.UPDATE.GROSSNAV` | `FsGaMulticlassDailyUpdate_Grossnav` |  |  |  |
| 48 | `FS.GA.MULTICLASS.DAILY.UPDATE.GROSS.CAPITAL.INVESTMENT` | `FsGaMulticlassDailyUpdate_GrossCapitalInvestment` |  |  |  |
| 49 | `FS.GA.MULTICLASS.DAILY.UPDATE.NET.ROR.PERCENTAGE` | `FsGaMulticlassDailyUpdate_NetRorPercentage` |  |  |  |
| 50 | `FS.GA.MULTICLASS.DAILY.UPDATE.NET.ROR.IN.BPS` | `FsGaMulticlassDailyUpdate_NetRorInBps` |  |  |  |
| 51 | `FS.GA.MULTICLASS.DAILY.UPDATE.NET.UNIT.VALUE` | `FsGaMulticlassDailyUpdate_NetUnitValue` |  |  |  |
| 52 | `FS.GA.MULTICLASS.DAILY.UPDATE.PREVIOUS.NET.UNIT.VALUE` | `FsGaMulticlassDailyUpdate_PreviousNetUnitValue` |  |  |  |
| 53 | `FS.GA.MULTICLASS.DAILY.UPDATE.TNA.SHARE.CLASS.CURRENCY` | `FsGaMulticlassDailyUpdate_TnaShareClassCurrency` |  |  |  |
| 54 | `FS.GA.MULTICLASS.DAILY.UPDATE.TAXABLE.FACTOR` | `FsGaMulticlassDailyUpdate_TaxableFactor` |  |  |  |
| 55 | `FS.GA.MULTICLASS.DAILY.UPDATE.TAX.FREE.FACTOR` | `FsGaMulticlassDailyUpdate_TaxFreeFactor` |  |  |  |
| 56 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED10` | `FsGaMulticlassDailyUpdate_Reserved10` |  |  |  |
| 57 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED9` | `FsGaMulticlassDailyUpdate_Reserved9` |  |  |  |
| 58 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED8` | `FsGaMulticlassDailyUpdate_Reserved8` |  |  |  |
| 59 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED7` | `FsGaMulticlassDailyUpdate_Reserved7` |  |  |  |
| 60 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED6` | `FsGaMulticlassDailyUpdate_Reserved6` |  |  |  |
| 61 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED5` | `FsGaMulticlassDailyUpdate_Reserved5` |  |  |  |
| 62 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED4` | `FsGaMulticlassDailyUpdate_Reserved4` |  |  |  |
| 63 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED3` | `FsGaMulticlassDailyUpdate_Reserved3` |  |  |  |
| 64 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED2` | `FsGaMulticlassDailyUpdate_Reserved2` |  |  |  |
| 65 | `FS.GA.MULTICLASS.DAILY.UPDATE.RESERVED1` | `FsGaMulticlassDailyUpdate_Reserved1` |  |  |  |
| 66 | `FS.GA.MULTICLASS.DAILY.UPDATE.LOCAL.REF` | `FsGaMulticlassDailyUpdate_LocalRef` |  |  |  |
| 67 | `FS.GA.MULTICLASS.DAILY.UPDATE.OVERRIDE` | `FsGaMulticlassDailyUpdate_Override` |  |  |  |
| 68 | `FS.GA.MULTICLASS.DAILY.UPDATE.RECORD.STATUS` | `FsGaMulticlassDailyUpdate_RecordStatus` |  |  |  |
| 69 | `FS.GA.MULTICLASS.DAILY.UPDATE.CURR.NO` | `FsGaMulticlassDailyUpdate_CurrNo` |  |  |  |
| 70 | `FS.GA.MULTICLASS.DAILY.UPDATE.INPUTTER` | `FsGaMulticlassDailyUpdate_Inputter` |  |  |  |
| 71 | `FS.GA.MULTICLASS.DAILY.UPDATE.DATE.TIME` | `FsGaMulticlassDailyUpdate_DateTime` |  |  |  |
| 72 | `FS.GA.MULTICLASS.DAILY.UPDATE.AUTHORISER` | `FsGaMulticlassDailyUpdate_Authoriser` |  |  |  |
| 73 | `FS.GA.MULTICLASS.DAILY.UPDATE.CO.CODE` | `FsGaMulticlassDailyUpdate_CoCode` |  |  |  |
| 74 | `FS.GA.MULTICLASS.DAILY.UPDATE.DEPT.CODE` | `FsGaMulticlassDailyUpdate_DeptCode` |  |  |  |
| 75 | `FS.GA.MULTICLASS.DAILY.UPDATE.AUDITOR.CODE` | `FsGaMulticlassDailyUpdate_AuditorCode` |  |  |  |
| 76 | `FS.GA.MULTICLASS.DAILY.UPDATE.AUDIT.DATE.TIME` | `FsGaMulticlassDailyUpdate_AuditDateTime` |  |  |  |
