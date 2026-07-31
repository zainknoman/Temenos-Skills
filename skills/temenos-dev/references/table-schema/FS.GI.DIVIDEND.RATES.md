# FS.GI.DIVIDEND.RATES — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.RATES` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIV.RATES.GROUP.ID` | `FsGiDividendRates_GroupId` |  |  |  |
| 2 | `GI.DIV.RATES.LEGAL.ENTITY.ID` | `FsGiDividendRates_LegalEntityId` |  |  |  |
| 3 | `GI.DIV.RATES.FUND.ID` | `FsGiDividendRates_FundId` |  |  |  |
| 4 | `GI.DIV.RATES.SHARE.CLASS.CODE` | `FsGiDividendRates_ShareClassCode` |  |  |  |
| 5 | `GI.DIV.RATES.EXECUTION.DATE` | `FsGiDividendRates_ExecutionDate` |  |  |  |
| 6 | `GI.DIV.RATES.DIVIDEND.RATE.PER.SHARE` | `FsGiDividendRates_DividendRatePerShare` |  |  |  |
| 7 | `GI.DIV.RATES.TISD` | `FsGiDividendRates_Tisd` |  |  |  |
| 8 | `GI.DIV.RATES.AVERAGE.EQUALIZATION.RATE` | `FsGiDividendRates_AverageEqualizationRate` |  |  |  |
| 9 | `GI.DIV.RATES.GROUP.UPDATE.ONLY` | `FsGiDividendRates_GroupUpdateOnly` |  |  |  |
| 10 | `GI.DIV.RATES.INCOME.TYPE` | `FsGiDividendRates_IncomeType` |  |  |  |
| 11 | `GI.DIV.RATES.DISTRIBUTION.TYPE` | `FsGiDividendRates_DistributionType` |  |  |  |
| 12 | `GI.DIV.RATES.FRANKED.INCOME.PERCENTAGE` | `FsGiDividendRates_FrankedIncomePercentage` |  |  |  |
| 13 | `GI.DIV.RATES.UNFRANKED.NON.FOREIGN.INCOME` | `FsGiDividendRates_UnfrankedNonForeignIncome` |  |  |  |
| 14 | `GI.DIV.RATES.UNFRANKED.FOREIGN.INCOME` | `FsGiDividendRates_UnfrankedForeignIncome` |  |  |  |
| 15 | `GI.DIV.RATES.CORPORATION.TAX.AMOUNT` | `FsGiDividendRates_CorporationTaxAmount` |  |  |  |
| 16 | `GI.DIV.RATES.CORPORATION.TAX.RATE` | `FsGiDividendRates_CorporationTaxRate` |  |  |  |
| 17 | `GI.DIV.RATES.RESERVED10` | `FsGiDividendRates_Reserved10` |  |  |  |
| 18 | `GI.DIV.RATES.RESERVED9` | `FsGiDividendRates_Reserved9` |  |  |  |
| 19 | `GI.DIV.RATES.RESERVED8` | `FsGiDividendRates_Reserved8` |  |  |  |
| 20 | `GI.DIV.RATES.RESERVED7` | `FsGiDividendRates_Reserved7` |  |  |  |
| 21 | `GI.DIV.RATES.RESERVED6` | `FsGiDividendRates_Reserved6` |  |  |  |
| 22 | `GI.DIV.RATES.RESERVED5` | `FsGiDividendRates_Reserved5` |  |  |  |
| 23 | `GI.DIV.RATES.RESERVED4` | `FsGiDividendRates_Reserved4` |  |  |  |
| 24 | `GI.DIV.RATES.RESERVED3` | `FsGiDividendRates_Reserved3` |  |  |  |
| 25 | `GI.DIV.RATES.RESERVED2` | `FsGiDividendRates_Reserved2` |  |  |  |
| 26 | `GI.DIV.RATES.RESERVED1` | `FsGiDividendRates_Reserved1` |  |  |  |
| 27 | `GI.DIV.RATES.LOCAL.REF` | `FsGiDividendRates_LocalRef` |  |  |  |
| 28 | `GI.DIV.RATES.OVERRIDE` | `FsGiDividendRates_Override` |  |  |  |
| 29 | `GI.DIV.RATES.RECORD.STATUS` | `FsGiDividendRates_RecordStatus` |  |  |  |
| 30 | `GI.DIV.RATES.CURR.NO` | `FsGiDividendRates_CurrNo` |  |  |  |
| 31 | `GI.DIV.RATES.INPUTTER` | `FsGiDividendRates_Inputter` |  |  |  |
| 32 | `GI.DIV.RATES.DATE.TIME` | `FsGiDividendRates_DateTime` |  |  |  |
| 33 | `GI.DIV.RATES.AUTHORISER` | `FsGiDividendRates_Authoriser` |  |  |  |
| 34 | `GI.DIV.RATES.CO.CODE` | `FsGiDividendRates_CoCode` |  |  |  |
| 35 | `GI.DIV.RATES.DEPT.CODE` | `FsGiDividendRates_DeptCode` |  |  |  |
| 36 | `GI.DIV.RATES.AUDITOR.CODE` | `FsGiDividendRates_AuditorCode` |  |  |  |
| 37 | `GI.DIV.RATES.AUDIT.DATE.TIME` | `FsGiDividendRates_AuditDateTime` |  |  |  |
