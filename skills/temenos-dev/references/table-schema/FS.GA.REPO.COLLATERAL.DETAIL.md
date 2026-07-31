# FS.GA.REPO.COLLATERAL.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.REPO.COLLATERAL.DETAIL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.REPO.COLLATERAL.DETAIL.PARENT.REF.ID` | `FsGaRepoCollateralDetail_ParentRefId` |  |  |  |
| 2 | `FS.GA.REPO.COLLATERAL.DETAIL.ORA.ROWID` | `FsGaRepoCollateralDetail_OraRowid` |  |  |  |
| 3 | `FS.GA.REPO.COLLATERAL.DETAIL.FUND.ID` | `FsGaRepoCollateralDetail_FundId` |  |  |  |
| 4 | `FS.GA.REPO.COLLATERAL.DETAIL.TRANSACTION.SERVICE.CODE` | `FsGaRepoCollateralDetail_TransactionServiceCode` |  |  |  |
| 5 | `FS.GA.REPO.COLLATERAL.DETAIL.TRANSACTION.NUMBER` | `FsGaRepoCollateralDetail_TransactionNumber` |  |  |  |
| 6 | `FS.GA.REPO.COLLATERAL.DETAIL.INTERNAL.SECURITY.ID` | `FsGaRepoCollateralDetail_InternalSecurityId` |  |  |  |
| 7 | `FS.GA.REPO.COLLATERAL.DETAIL.QUANTITY` | `FsGaRepoCollateralDetail_Quantity` |  |  |  |
| 8 | `FS.GA.REPO.COLLATERAL.DETAIL.MARKET.PRICE` | `FsGaRepoCollateralDetail_MarketPrice` |  |  |  |
| 9 | `FS.GA.REPO.COLLATERAL.DETAIL.DATE.OF.PRICE` | `FsGaRepoCollateralDetail_DateOfPrice` |  |  |  |
| 10 | `FS.GA.REPO.COLLATERAL.DETAIL.MARKET.VALUE.IN.BOOK.CURRENCY` | `FsGaRepoCollateralDetail_MarketValueInBookCurrency` |  |  |  |
| 11 | `FS.GA.REPO.COLLATERAL.DETAIL.ACCRUED.INTEREST.COLLATERAL` | `FsGaRepoCollateralDetail_AccruedInterestCollateral` |  |  |  |
| 12 | `FS.GA.REPO.COLLATERAL.DETAIL.TOTAL.VALUE.COLLATERAL` | `FsGaRepoCollateralDetail_TotalValueCollateral` |  |  |  |
| 13 | `FS.GA.REPO.COLLATERAL.DETAIL.PERCENT.COVERED` | `FsGaRepoCollateralDetail_PercentCovered` |  |  |  |
| 14 | `FS.GA.REPO.COLLATERAL.DETAIL.INCOME.TYPE.COUNTERPARTY.LEG` | `FsGaRepoCollateralDetail_IncomeTypeCounterpartyLeg` |  |  |  |
| 15 | `FS.GA.REPO.COLLATERAL.DETAIL.INVESTMENT.CURRENCY` | `FsGaRepoCollateralDetail_InvestmentCurrency` |  |  |  |
| 16 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED10` | `FsGaRepoCollateralDetail_Reserved10` |  |  |  |
| 17 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED9` | `FsGaRepoCollateralDetail_Reserved9` |  |  |  |
| 18 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED8` | `FsGaRepoCollateralDetail_Reserved8` |  |  |  |
| 19 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED7` | `FsGaRepoCollateralDetail_Reserved7` |  |  |  |
| 20 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED6` | `FsGaRepoCollateralDetail_Reserved6` |  |  |  |
| 21 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED5` | `FsGaRepoCollateralDetail_Reserved5` |  |  |  |
| 22 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED4` | `FsGaRepoCollateralDetail_Reserved4` |  |  |  |
| 23 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED3` | `FsGaRepoCollateralDetail_Reserved3` |  |  |  |
| 24 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED2` | `FsGaRepoCollateralDetail_Reserved2` |  |  |  |
| 25 | `FS.GA.REPO.COLLATERAL.DETAIL.RESERVED1` | `FsGaRepoCollateralDetail_Reserved1` |  |  |  |
| 26 | `FS.GA.REPO.COLLATERAL.DETAIL.LOCAL.REF` | `FsGaRepoCollateralDetail_LocalRef` |  |  |  |
| 27 | `FS.GA.REPO.COLLATERAL.DETAIL.OVERRIDE` | `FsGaRepoCollateralDetail_Override` |  |  |  |
| 28 | `FS.GA.REPO.COLLATERAL.DETAIL.RECORD.STATUS` | `FsGaRepoCollateralDetail_RecordStatus` |  |  |  |
| 29 | `FS.GA.REPO.COLLATERAL.DETAIL.CURR.NO` | `FsGaRepoCollateralDetail_CurrNo` |  |  |  |
| 30 | `FS.GA.REPO.COLLATERAL.DETAIL.INPUTTER` | `FsGaRepoCollateralDetail_Inputter` |  |  |  |
| 31 | `FS.GA.REPO.COLLATERAL.DETAIL.DATE.TIME` | `FsGaRepoCollateralDetail_DateTime` |  |  |  |
| 32 | `FS.GA.REPO.COLLATERAL.DETAIL.AUTHORISER` | `FsGaRepoCollateralDetail_Authoriser` |  |  |  |
| 33 | `FS.GA.REPO.COLLATERAL.DETAIL.CO.CODE` | `FsGaRepoCollateralDetail_CoCode` |  |  |  |
| 34 | `FS.GA.REPO.COLLATERAL.DETAIL.DEPT.CODE` | `FsGaRepoCollateralDetail_DeptCode` |  |  |  |
| 35 | `FS.GA.REPO.COLLATERAL.DETAIL.AUDITOR.CODE` | `FsGaRepoCollateralDetail_AuditorCode` |  |  |  |
| 36 | `FS.GA.REPO.COLLATERAL.DETAIL.AUDIT.DATE.TIME` | `FsGaRepoCollateralDetail_AuditDateTime` |  |  |  |
