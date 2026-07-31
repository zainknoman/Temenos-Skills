# FS.GA.COLLATERAL.COVERAGE.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.COLLATERAL.COVERAGE.DETAIL` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.PARENT.REF.ID` | `FsGaCollateralCoverageDetail_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.ORA.ROWID` | `FsGaCollateralCoverageDetail_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.FUND.ID` | `FsGaCollateralCoverageDetail_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.TRANSACTION.SERVICE.CODE` | `FsGaCollateralCoverageDetail_TransactionServiceCode` | TField |  | This is the transaction type. Multifonds DB Column is CSERV. |
| 5 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.INTERNAL.SECURITY.ID` | `FsGaCollateralCoverageDetail_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 6 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.COUNTERPARTY.CORRESPONDENT` | `FsGaCollateralCoverageDetail_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 7 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.QUANTITY` | `FsGaCollateralCoverageDetail_Quantity` | TField |  | Transaction Quantity Multifonds DB Column is QUANTITE. |
| 8 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.MARKET.PRICE` | `FsGaCollateralCoverageDetail_MarketPrice` | TField |  | Market price for NAV Multifonds DB Column is COURSVAL. |
| 9 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.DATE.OF.PRICE` | `FsGaCollateralCoverageDetail_DateOfPrice` | TField |  | Value date of the securities prices Multifonds DB Column is DATECOURS. |
| 10 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.MARKET.VALUE.IN.BOOK.CURRENCY` | `FsGaCollateralCoverageDetail_MarketValueInBookCurrency` | TField |  | Market Value in Book Currency Multifonds DB Column is MNT_ACT. |
| 11 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.ACCRUED.INTEREST.COLLATERAL` | `FsGaCollateralCoverageDetail_AccruedInterestCollateral` | TField |  | Displayed by the system in case of bonds. It is computed from the last coupon date of the collateral security to the accounting date on which the collateral is attached to the counterparty. Multifonds DB Column is MNT_INT_ACR. |
| 12 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.TOTAL.VALUE.COLLATERAL` | `FsGaCollateralCoverageDetail_TotalValueCollateral` | TField |  | Total value of the collateral attached to security lending or deposit contract,i.e. sm of Market Value and the interest accruals. Multifonds DB Column is MNT_TOTAL. |
| 13 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.SECURITIES.COVERAGE.MINIMUM` | `FsGaCollateralCoverageDetail_SecuritiesCoverageMinimum` | TField |  | Input the minimum value of securities coverage for Securities Lending Multifonds DB Column is PCT_SEC_MIN. |
| 14 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.SECURITIES.COVERAGE.MAXIMUM` | `FsGaCollateralCoverageDetail_SecuritiesCoverageMaximum` | TField |  | Input the maximum value of securities coverage for Securities Lending Multifonds DB Column is PCT_SEC_MAX. |
| 15 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.CASH.COVERAGE.PERCENTAGE` | `FsGaCollateralCoverageDetail_CashCoveragePercentage` | TField |  | Input the cash coverage percent to be applicable to the security lending engagement Multifonds DB Column is PCT_CASH. |
| 16 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.OPERATION.CODE` | `FsGaCollateralCoverageDetail_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 17 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED10` | `FsGaCollateralCoverageDetail_Reserved10` | TField |  |  |
| 18 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED9` | `FsGaCollateralCoverageDetail_Reserved9` | TField |  |  |
| 19 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED8` | `FsGaCollateralCoverageDetail_Reserved8` | TField |  |  |
| 20 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED7` | `FsGaCollateralCoverageDetail_Reserved7` | TField |  |  |
| 21 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED6` | `FsGaCollateralCoverageDetail_Reserved6` | TField |  |  |
| 22 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED5` | `FsGaCollateralCoverageDetail_Reserved5` | TField |  |  |
| 23 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED4` | `FsGaCollateralCoverageDetail_Reserved4` | TField |  |  |
| 24 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED3` | `FsGaCollateralCoverageDetail_Reserved3` | TField |  |  |
| 25 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED2` | `FsGaCollateralCoverageDetail_Reserved2` | TField |  |  |
| 26 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RESERVED1` | `FsGaCollateralCoverageDetail_Reserved1` | TField |  |  |
| 27 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.LOCAL.REF` | `FsGaCollateralCoverageDetail_LocalRef` |  |  |  |
| 28 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.OVERRIDE` | `FsGaCollateralCoverageDetail_Override` |  |  |  |
| 29 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.RECORD.STATUS` | `FsGaCollateralCoverageDetail_RecordStatus` | String |  |  |
| 30 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.CURR.NO` | `FsGaCollateralCoverageDetail_CurrNo` | String |  |  |
| 31 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.INPUTTER` | `FsGaCollateralCoverageDetail_Inputter` |  |  |  |
| 32 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.DATE.TIME` | `FsGaCollateralCoverageDetail_DateTime` |  |  |  |
| 33 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.AUTHORISER` | `FsGaCollateralCoverageDetail_Authoriser` | String |  |  |
| 34 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.CO.CODE` | `FsGaCollateralCoverageDetail_CoCode` | String |  |  |
| 35 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.DEPT.CODE` | `FsGaCollateralCoverageDetail_DeptCode` | String |  |  |
| 36 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.AUDITOR.CODE` | `FsGaCollateralCoverageDetail_AuditorCode` | String |  |  |
| 37 | `FS.GA.COLLATERAL.COVERAGE.DETAIL.AUDIT.DATE.TIME` | `FsGaCollateralCoverageDetail_AuditDateTime` | String |  |  |
