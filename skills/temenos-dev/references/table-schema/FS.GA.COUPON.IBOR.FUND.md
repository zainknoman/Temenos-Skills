# FS.GA.COUPON.IBOR.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.COUPON.IBOR.FUND` in `FS_IncomeCorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.COUPON.IBOR.FUND.INTERNAL.SECURITY.ID` | `FsGaCouponIborFund_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 2 | `FS.GA.COUPON.IBOR.FUND.NUMBER.SEQUENCE` | `FsGaCouponIborFund_NumberSequence` | TField |  | Sequence Number Multifonds DB Column is NO_SEQ. |
| 3 | `FS.GA.COUPON.IBOR.FUND.ENTITLEMENT.DATE` | `FsGaCouponIborFund_EntitlementDate` | TField |  | The ex-date, or ex-dividend date, is the date on or after which a security is traded without a previously declared dividend or distribution. Multifonds DB Column is DEXEC. |
| 4 | `FS.GA.COUPON.IBOR.FUND.DIVIDEND.EXECUTION.DATE` | `FsGaCouponIborFund_DividendExecutionDate` | TField |  | Dividend Execution Date Multifonds DB Column is DEXEC_DIV. |
| 5 | `FS.GA.COUPON.IBOR.FUND.EXTERNAL.REFERENCE.NUMBER` | `FsGaCouponIborFund_ExternalReferenceNumber` | TField |  | External reference corresponds a trade,security or fund Multifonds DB Column is EXT_REF. |
| 6 | `FS.GA.COUPON.IBOR.FUND.SERVICE.CODE.POT` | `FsGaCouponIborFund_ServiceCodePot` | TField |  | Service Code Pot Multifonds DB Column is CSERV_POT. |
| 7 | `FS.GA.COUPON.IBOR.FUND.FUND.ID` | `FsGaCouponIborFund_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 8 | `FS.GA.COUPON.IBOR.FUND.SERVICE.CODE` | `FsGaCouponIborFund_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 9 | `FS.GA.COUPON.IBOR.FUND.CUSTODIAN` | `FsGaCouponIborFund_Custodian` | TField |  | Custodian where the units of the transaction would be lodged Multifonds DB Column is NDEPOSI. |
| 10 | `FS.GA.COUPON.IBOR.FUND.LOT.NUMBER` | `FsGaCouponIborFund_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 11 | `FS.GA.COUPON.IBOR.FUND.MANAGER.CODE` | `FsGaCouponIborFund_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 12 | `FS.GA.COUPON.IBOR.FUND.OPERATION.CODE` | `FsGaCouponIborFund_OperationCode` | TField |  | Transaction type identifier Multifonds DB Column is COPER. |
| 13 | `FS.GA.COUPON.IBOR.FUND.CONFIRMED.ORIGINAL.QUANTITY` | `FsGaCouponIborFund_ConfirmedOriginalQuantity` | TField |  | Confirmed original quantity Multifonds DB Column is QTE_CONF_ORIG. |
| 14 | `FS.GA.COUPON.IBOR.FUND.CONFIRMED.REVISED.QUANTITY` | `FsGaCouponIborFund_ConfirmedRevisedQuantity` | TField |  | Confirmed revised quantity Multifonds DB Column is QTE_CONF. |
| 15 | `FS.GA.COUPON.IBOR.FUND.UNCONFIRMED.ORIGINAL.QUANTITY` | `FsGaCouponIborFund_UnconfirmedOriginalQuantity` | TField |  | Unconfirmed original quantity Multifonds DB Column is QTE_UNCONF_ORIG. |
| 16 | `FS.GA.COUPON.IBOR.FUND.UNCONFIRMED.REVISED.QUANTITY` | `FsGaCouponIborFund_UnconfirmedRevisedQuantity` | TField |  | Unconfirmed revised quantity Multifonds DB Column is QTE_UNCONF. |
| 17 | `FS.GA.COUPON.IBOR.FUND.TOTAL.ORIGINAL.QUANTITY` | `FsGaCouponIborFund_TotalOriginalQuantity` | TField |  | Total original quantity Multifonds DB Column is QTE_TOTAL_ORIG. |
| 18 | `FS.GA.COUPON.IBOR.FUND.TOTAL.REVISED.QUANTITY` | `FsGaCouponIborFund_TotalRevisedQuantity` | TField |  | Total revised quantity Multifonds DB Column is QTE_TOTAL. |
| 19 | `FS.GA.COUPON.IBOR.FUND.RATIO` | `FsGaCouponIborFund_Ratio` | TField |  | Exercise Ratio between Option and underlying security. Also in futures it's used for French Year End Reporting Multifonds DB Column is RATIO. |
| 20 | `FS.GA.COUPON.IBOR.FUND.PURCHASE.UNITS` | `FsGaCouponIborFund_PurchaseUnits` | TField |  | Quantity purchased Multifonds DB Column is QACHAT. |
| 21 | `FS.GA.COUPON.IBOR.FUND.SALE.OR.DISPOSED.UNITS` | `FsGaCouponIborFund_SaleOrDisposedUnits` | TField |  | Quantity sold or disposed Multifonds DB Column is QVENTE. |
| 22 | `FS.GA.COUPON.IBOR.FUND.PURCHASE.AMT.IN.SECURITY.CCY` | `FsGaCouponIborFund_PurchaseAmtInSecurityCcy` |  |  |  |
| 23 | `FS.GA.COUPON.IBOR.FUND.SALE.AMOUNT.IN.SECURITY.CCY` | `FsGaCouponIborFund_SaleAmountInSecurityCcy` | TField |  | Sale amount in Security Ccy Multifonds DB Column is MTVENTE. |
| 24 | `FS.GA.COUPON.IBOR.FUND.PURCHASE.AMOUNT.IN.FUND.CCY` | `FsGaCouponIborFund_PurchaseAmountInFundCcy` | TField |  | Purchase Amount in Fund Ccy Multifonds DB Column is MTACHAT_PTF. |
| 25 | `FS.GA.COUPON.IBOR.FUND.SALE.AMOUNT.IN.FUND.CCY` | `FsGaCouponIborFund_SaleAmountInFundCcy` | TField |  | Sale amount in Fund Ccy Multifonds DB Column is MTVENTE_PTF. |
| 26 | `FS.GA.COUPON.IBOR.FUND.FLAG.UNCONFIRMED.SELECT` | `FsGaCouponIborFund_FlagUnconfirmedSelect` | TField |  | Flag Unconfirmed Select Multifonds DB Column is FLG_UNCONF_SELECT. |
| 27 | `FS.GA.COUPON.IBOR.FUND.ACTUAL.CONFIRMED.QUANTITY` | `FsGaCouponIborFund_ActualConfirmedQuantity` | TField |  | Actual Confirmed Quantity Multifonds DB Column is QTE_ACTUAL_CONF. |
| 28 | `FS.GA.COUPON.IBOR.FUND.TAX.REGIME` | `FsGaCouponIborFund_TaxRegime` | TField |  | A group of Tax rules can be defined in the Tax tables against a Tax regime and all the funds defined with the respective Tax regime would follow the tax rules defined under this Tax regime. Multifonds DB Column is TAX_REG. |
| 29 | `FS.GA.COUPON.IBOR.FUND.LOCAL.CURRENCY` | `FsGaCouponIborFund_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 30 | `FS.GA.COUPON.IBOR.FUND.EX.DATE.FLAG` | `FsGaCouponIborFund_ExDateFlag` | TField |  | Trade Date in case of income transaction like coupon or dividend, Execution date for Dividend announcement and Corporate Action Multifonds DB Column is DPAYMNT. |
| 31 | `FS.GA.COUPON.IBOR.FUND.RESERVED10` | `FsGaCouponIborFund_Reserved10` | TField |  |  |
| 32 | `FS.GA.COUPON.IBOR.FUND.RESERVED9` | `FsGaCouponIborFund_Reserved9` | TField |  |  |
| 33 | `FS.GA.COUPON.IBOR.FUND.RESERVED8` | `FsGaCouponIborFund_Reserved8` | TField |  |  |
| 34 | `FS.GA.COUPON.IBOR.FUND.RESERVED7` | `FsGaCouponIborFund_Reserved7` | TField |  |  |
| 35 | `FS.GA.COUPON.IBOR.FUND.RESERVED6` | `FsGaCouponIborFund_Reserved6` | TField |  |  |
| 36 | `FS.GA.COUPON.IBOR.FUND.RESERVED5` | `FsGaCouponIborFund_Reserved5` | TField |  |  |
| 37 | `FS.GA.COUPON.IBOR.FUND.RESERVED4` | `FsGaCouponIborFund_Reserved4` | TField |  |  |
| 38 | `FS.GA.COUPON.IBOR.FUND.RESERVED3` | `FsGaCouponIborFund_Reserved3` | TField |  |  |
| 39 | `FS.GA.COUPON.IBOR.FUND.RESERVED2` | `FsGaCouponIborFund_Reserved2` | TField |  |  |
| 40 | `FS.GA.COUPON.IBOR.FUND.RESERVED1` | `FsGaCouponIborFund_Reserved1` | TField |  |  |
| 41 | `FS.GA.COUPON.IBOR.FUND.RECORD.STATUS` | `FsGaCouponIborFund_RecordStatus` | String |  |  |
| 42 | `FS.GA.COUPON.IBOR.FUND.CURR.NO` | `FsGaCouponIborFund_CurrNo` | String |  |  |
| 43 | `FS.GA.COUPON.IBOR.FUND.INPUTTER` | `FsGaCouponIborFund_Inputter` |  |  |  |
| 44 | `FS.GA.COUPON.IBOR.FUND.DATE.TIME` | `FsGaCouponIborFund_DateTime` |  |  |  |
| 45 | `FS.GA.COUPON.IBOR.FUND.AUTHORISER` | `FsGaCouponIborFund_Authoriser` | String |  |  |
| 46 | `FS.GA.COUPON.IBOR.FUND.CO.CODE` | `FsGaCouponIborFund_CoCode` | String |  |  |
| 47 | `FS.GA.COUPON.IBOR.FUND.DEPT.CODE` | `FsGaCouponIborFund_DeptCode` | String |  |  |
| 48 | `FS.GA.COUPON.IBOR.FUND.AUDITOR.CODE` | `FsGaCouponIborFund_AuditorCode` | String |  |  |
| 49 | `FS.GA.COUPON.IBOR.FUND.AUDIT.DATE.TIME` | `FsGaCouponIborFund_AuditDateTime` | String |  |  |
