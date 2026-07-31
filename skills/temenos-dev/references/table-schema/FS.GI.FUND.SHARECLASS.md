# FS.GI.FUND.SHARECLASS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.SHARECLASS` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.SHARECLASS.PARENT.REF.ID` | `FsGiFundShareclass_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.SHARECLASS.ORA.ROWID` | `FsGiFundShareclass_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.SHARECLASS.LEGAL.ENTITY.ID` | `FsGiFundShareclass_LegalEntityId` | TField |  | Legal Entity internal Id. Multifonds DB Column is NTFC. |
| 4 | `FS.GI.FUND.SHARECLASS.FUND.ID` | `FsGiFundShareclass_FundId` | TField |  | Fund Internal Identification. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.FUND.SHARECLASS.SHARE.CLASS.CODE` | `FsGiFundShareclass_ShareClassCode` | TField |  | Shareclass code linked to the security. Multifonds DB Column is TPARTS. |
| 6 | `FS.GI.FUND.SHARECLASS.SECURITY.ID` | `FsGiFundShareclass_SecurityId` | TField |  | Security internal Id. Multifonds DB Column is NOVAL. |
| 7 | `FS.GI.FUND.SHARECLASS.NAME` | `FsGiFundShareclass_Name` | TField |  | Name of the security. Multifonds DB Column is NOMVAL. |
| 8 | `FS.GI.FUND.SHARECLASS.SHORT.NAME` | `FsGiFundShareclass_ShortName` | TField |  | Short Name of the Security. Multifonds DB Column is ABREGE. |
| 9 | `FS.GI.FUND.SHARECLASS.ENTITY.STATUS` | `FsGiFundShareclass_EntityStatus` | TField |  | Entity status. Multifonds DB Column is ACTIF. |
| 10 | `FS.GI.FUND.SHARECLASS.QUANTITY.DECIMALS` | `FsGiFundShareclass_QuantityDecimals` | TField |  | Number of decimal places in the client share quantity calculation. Multifonds DB Column is CODE_ARRONDI_QT. |
| 11 | `FS.GI.FUND.SHARECLASS.FUND.MESSAGE` | `FsGiFundShareclass_FundMessage` | TField |  | The fund warning message which will be displayed in the order entry screen. Multifonds DB Column is CODEID. |
| 12 | `FS.GI.FUND.SHARECLASS.LOCKUP.SCOPE.FLAG` | `FsGiFundShareclass_LockupScopeFlag` | TField |  | Flag allows to enable the lock-up period functionality for share class. Multifonds DB Column is LOCKUP_SCOPE. |
| 13 | `FS.GI.FUND.SHARECLASS.LOCKUP.METHOD` | `FsGiFundShareclass_LockupMethod` | TField |  | Lockup period method to be followed for the fund. Multifonds DB Column is LOCKUP_MTHD. |
| 14 | `FS.GI.FUND.SHARECLASS.LOCKUP.DURATION` | `FsGiFundShareclass_LockupDuration` | TField |  | The duration during which the lock up period functionality will apply to the fund. Multifonds DB Column is LOCKUP_DURATION. |
| 15 | `FS.GI.FUND.SHARECLASS.LOCKUP.SOFT.WARNING.FLAG` | `FsGiFundShareclass_LockupSoftWarningFlag` | TField |  | Flag allows to enable the soft warning messages by the system as a result of the lock up period set up. Multifonds DB Column is FLG_SOFT_WARNING. |
| 16 | `FS.GI.FUND.SHARECLASS.MULTIPLE.NAV.FLAG` | `FsGiFundShareclass_MultipleNavFlag` | TField |  | Flag allows to in scope the Multiple NAV functionality for fund shareclass. Multifonds DB Column is FLG_MNAV. |
| 17 | `FS.GI.FUND.SHARECLASS.ORDER.BLOCKED.FLAG` | `FsGiFundShareclass_OrderBlockedFlag` | TField |  | Flag allows to block the Fund Share class for transactions. Multifonds DB Column is FLG_BLOCKED. |
| 18 | `FS.GI.FUND.SHARECLASS.BATCH.BLOCKED.FLAG` | `FsGiFundShareclass_BatchBlockedFlag` | TField |  | Flag allows to block the simulation and batch process of orders in the shareclasses as the NAV price required for these processes is blocked. Multifonds DB Column is FLG_BLOCKED_NAV. |
| 19 | `FS.GI.FUND.SHARECLASS.DEAL.TYPE` | `FsGiFundShareclass_DealType` | TField |  | Deal type code for Cash handling at Shareclass level. Multifonds DB Column is TYPE_DEAL. |
| 20 | `FS.GI.FUND.SHARECLASS.NO.PRICE.REQUIRED.FLAG` | `FsGiFundShareclass_NoPriceRequiredFlag` | TField |  | Flag allows to specify that price is not required for the series. Multifonds DB Column is FLG_NO_PRICE. |
| 21 | `FS.GI.FUND.SHARECLASS.INTERFACE.BLOCKED` | `FsGiFundShareclass_InterfaceBlocked` | TField |  | Flag allows to block the Fund Share class for interface transactions. Multifonds DB Column is FLG_INT_BLOCKED_SHARE. |
| 22 | `FS.GI.FUND.SHARECLASS.FUND.TRADING.DESK.PROCESS` | `FsGiFundShareclass_FundTradingDeskProcess` | TField |  | It specifies if the fund share class is in scope of Fund trading desk or Hedge FX or not in scope of both. Multifonds DB Column is FUND_TDSK_PROC. |
| 23 | `FS.GI.FUND.SHARECLASS.RESTRICTED.FLAG` | `FsGiFundShareclass_RestrictedFlag` | TField |  | Flag allows to differentiate the share classes from being normal share class vs restricted share class and this flag will also help for reporting certain transactions. Multifonds DB Column is FLG_RESTRICTED. |
| 24 | `FS.GI.FUND.SHARECLASS.BLANKET.MIN.LIMIT.WAIVER.FLAG` | `FsGiFundShareclass_BlanketMinLimitWaiverFlag` | TField |  | Flag to enable blanket waiver for transactions that do not meet the minimum investment limits. Multifonds DB Column is FLG_BLANKET_WAIVER. |
| 25 | `FS.GI.FUND.SHARECLASS.MIN.LIMITS.MONITORING.FLAG` | `FsGiFundShareclass_MinLimitsMonitoringFlag` | TField |  | Flag allows to enable the minimum limit tracking for the confirmed orders. Multifonds DB Column is FLG_MIN_MON. |
| 26 | `FS.GI.FUND.SHARECLASS.LAST.NAV.FLAG` | `FsGiFundShareclass_LastNavFlag` | TField |  | Flag allows to block the NAV to be inserted for the shareclass. Multifonds DB Column is FLG_LAST_NAV. |
| 27 | `FS.GI.FUND.SHARECLASS.VALUE.DATE.NUMBER.OF.DAYS` | `FsGiFundShareclass_ValueDateNumberOfDays` | TField |  | It specifies the number of days between trade date and value date for the fund. Multifonds DB Column is NUMBER_DAYS. |
| 28 | `FS.GI.FUND.SHARECLASS.REGISTER.VALUE.DATE.CODE` | `FsGiFundShareclass_RegisterValueDateCode` | TField |  | The exception value date for all operation codes of the share class and TA fund. Multifonds DB Column is REG_VALDT_CODE. |
| 29 | `FS.GI.FUND.SHARECLASS.GL.FLOW.ID` | `FsGiFundShareclass_GlFlowId` | TField |  | General ledger flow ID. Multifonds DB Column is GL_FLOW_ID. |
| 30 | `FS.GI.FUND.SHARECLASS.GL.ACCOUNT.GROUP.ID` | `FsGiFundShareclass_GlAccountGroupId` | TField |  | General ledger account group ID. Multifonds DB Column is GL_ACCT_GROUP_ID. |
| 31 | `FS.GI.FUND.SHARECLASS.CUSIP` | `FsGiFundShareclass_Cusip` | TField |  | CUSIP is a nine-digit numeric or nine-character alphanumeric code for the purposes of facilitating clearing and settlement of trades. Multifonds DB Column is CUSIP. |
| 32 | `FS.GI.FUND.SHARECLASS.NSCC.FLAG` | `FsGiFundShareclass_NsccFlag` | TField |  | Flag allows to enable to link the security to a CUSIP. Multifonds DB Column is FLG_NSCC. |
| 33 | `FS.GI.FUND.SHARECLASS.CDSC.FLAG` | `FsGiFundShareclass_CdscFlag` | TField |  | Flag enables the CDSC functionality for the fund share class. Multifonds DB Column is USE_CDSC. |
| 34 | `FS.GI.FUND.SHARECLASS.HISTORICAL.TRANSFER.FLAG` | `FsGiFundShareclass_HistoricalTransferFlag` | TField |  | Flag allows to activate the functionality of placing transfer with history. Multifonds DB Column is USE_HISTO_TRANSFER. |
| 35 | `FS.GI.FUND.SHARECLASS.CDSC.BUCKET.FLAG` | `FsGiFundShareclass_CdscBucketFlag` | TField |  | Flag allows to enable the bucketing principle to switches and transfers placed in the share class. The flag can be enabled only for share class having the flag &quot;Use CDSC&quot; set. Multifonds DB Column is CDSC_BUCKET. |
| 36 | `FS.GI.FUND.SHARECLASS.CDSC.CALC.PRICE.BASIS` | `FsGiFundShareclass_CdscCalcPriceBasis` | TField |  | To define the method of calculation of CDSC amount for the share class. Multifonds DB Column is CDSC_CALC_PRICE_BASE. |
| 37 | `FS.GI.FUND.SHARECLASS.ROLLOVER.FUND.ID` | `FsGiFundShareclass_RolloverFundId` | TField |  | The rollover TA Fund ID for the CDSC share class. Multifonds DB Column is NPTF_ROLLOVER. |
| 38 | `FS.GI.FUND.SHARECLASS.ROLLOVER.SHARE.CLASS.CODE` | `FsGiFundShareclass_RolloverShareClassCode` | TField |  | The rollover share class for the CDSC share class. Multifonds DB Column is TPART_ROLLOVER. |
| 39 | `FS.GI.FUND.SHARECLASS.AGEING.PERIOD.IN.MONTHS` | `FsGiFundShareclass_AgeingPeriodInMonths` | TField |  | Ageing period (in months) for the CDSC share class. Multifonds DB Column is AGE_PERIOD. |
| 40 | `FS.GI.FUND.SHARECLASS.KIID.COMPLIANCE.FLAG` | `FsGiFundShareclass_KiidComplianceFlag` | TField |  | It specifies the type of KIID TA control at order entry for the shareclass. Multifonds DB Column is KIID_COMP. |
| 41 | `FS.GI.FUND.SHARECLASS.ERISA.CHECK` | `FsGiFundShareclass_ErisaCheck` | TField |  | ERISA check that needs to be performed in the order level for the share class. Multifonds DB Column is ERISA_CHECK. |
| 42 | `FS.GI.FUND.SHARECLASS.US.PERSON.CONTROL` | `FsGiFundShareclass_UsPersonControl` | TField |  | It specifies the restrictions of transactions for US persons. Multifonds DB Column is US_PERS_CTRL. |
| 43 | `FS.GI.FUND.SHARECLASS.ERISA.CLASS.FLAG` | `FsGiFundShareclass_ErisaClassFlag` | TField |  | Flag allows to enable the custody settlement a ERISAa for the transactions created in the share class and for all underlying transaction created from this transaction. Multifonds DB Column is FLG_ERISA_CLS. |
| 44 | `FS.GI.FUND.SHARECLASS.IMA.RECEIVED.FLAG` | `FsGiFundShareclass_ImaReceivedFlag` | TField |  | Flag allows checking if an IMA has been signed by the investor for the fund and share class in which the deal is placed. Multifonds DB Column is FLG_IMA. |
| 45 | `FS.GI.FUND.SHARECLASS.MIFID.CONTROL` | `FsGiFundShareclass_MifidControl` | TField |  | It specifies the MIFID contorl for share class. Multifonds DB Column is MIFID_CTL. |
| 46 | `FS.GI.FUND.SHARECLASS.UK.EQ.RATES.FLAG` | `FsGiFundShareclass_UkEqRatesFlag` | TField |  | Flag allows to in scope of Equalization calculation for the shareclass. Multifonds DB Column is FLG_IA_EQ_RATE. |
| 47 | `FS.GI.FUND.SHARECLASS.INITIAL.BOX.DATE` | `FsGiFundShareclass_InitialBoxDate` | TField |  | Initial Box date on which Box is created with status &apos;Open&apos; and an initial box number. Multifonds DB Column is BOX_INIT_DATE. |
| 48 | `FS.GI.FUND.SHARECLASS.NO.WRAP.PRODUCT.FLAG` | `FsGiFundShareclass_NoWrapProductFlag` | TField |  | Flag allows to block the Share Class for selection at Product and will be considered as excluded where a @@@@a is selected. Multifonds DB Column is FLG_NPROD. |
| 49 | `FS.GI.FUND.SHARECLASS.NEW.ISSUE.STATUS.FLAG` | `FsGiFundShareclass_NewIssueStatusFlag` | TField |  | New issue status. Multifonds DB Column is FLG_NEW_ISSUE. |
| 50 | `FS.GI.FUND.SHARECLASS.PF.CALCULATION.STATUS` | `FsGiFundShareclass_PfCalculationStatus` | TField |  | It specifies the setup for automation of performance fees calculation at NAV reception. Multifonds DB Column is PF_CALC_STATUS. |
| 51 | `FS.GI.FUND.SHARECLASS.DIVIDEND.TYPE` | `FsGiFundShareclass_DividendType` | TField |  | Code of the Coupon Type of share class. Multifonds DB Column is TREV. |
| 52 | `FS.GI.FUND.SHARECLASS.CALCULATE.PF` | `FsGiFundShareclass_CalculatePf` | TField |  | It specifies if the share class is in scope for performance fees calculation or not. Multifonds DB Column is CALC_PF. |
| 53 | `FS.GI.FUND.SHARECLASS.BEGIN.DATE` | `FsGiFundShareclass_BeginDate` | TField |  | First Date of each share class linked Series Of Shares fund. Multifonds DB Column is BEGIN_DATE. |
| 54 | `FS.GI.FUND.SHARECLASS.REFERENCE.NAV.CONTROL` | `FsGiFundShareclass_ReferenceNavControl` | TField |  | It specifies the control on reception/input of the &apos;reference NAV&apos; (HWM or Benchmark Index) for each NAV date at fund level performance fee calculation. Multifonds DB Column is REF_NAV_CONTROL. |
| 55 | `FS.GI.FUND.SHARECLASS.PF.RESET.DATE` | `FsGiFundShareclass_PfResetDate` | TField |  | It specifies the date from which the share class, which has been suspended for performance fees calculation, bought in scope again for PF calculation. Multifonds DB Column is PF_RESET_DATE. |
| 56 | `FS.GI.FUND.SHARECLASS.PF.PERCENTAGE` | `FsGiFundShareclass_PfPercentage` | TField |  | It specifies the Performance Fee value in percentage form from 0 to 100%. Multifonds DB Column is PCT_PERFOR. |
| 57 | `FS.GI.FUND.SHARECLASS.REFERENCE.NAV.SECURITY.ID` | `FsGiFundShareclass_ReferenceNavSecurityId` | TField |  | External ID of the Reference NAV security linked to the shareclass. Multifonds DB Column is NOVAL_BSI. |
| 58 | `FS.GI.FUND.SHARECLASS.EQ.DEBIT.DEDUCTION` | `FsGiFundShareclass_EqDebitDeduction` | TField |  | The code of the calculation method for the Equalization debit to be deducted from the investor proceeds on Redemption. Multifonds DB Column is CEQUAL_DB_DEDUCT. |
| 59 | `FS.GI.FUND.SHARECLASS.EQ.CREDIT.REFUND.FLAG` | `FsGiFundShareclass_EqCreditRefundFlag` | TField |  | Flag allows to disable the refund of refundable equalization credit of the share class. Multifonds DB Column is FLG_EQUAL_CR_REFUND. |
| 60 | `FS.GI.FUND.SHARECLASS.MANUAL.COLLAPSE.FLAG` | `FsGiFundShareclass_ManualCollapseFlag` | TField |  | Flag allows the series linked to shareclass to be manually collapsed even though the fund does not permit it. Multifonds DB Column is FLG_COLLAPSE. |
| 61 | `FS.GI.FUND.SHARECLASS.EQ.DIVIDEND.FLAG` | `FsGiFundShareclass_EqDividendFlag` | TField |  | It specifies the Equalization fund distributes dividend to its investors and therefore taken into account for performance fees calculation. The option is available for Dividend for Hedge fund. Multifonds DB Column is FLG_DIVIDEND_EQ. |
| 62 | `FS.GI.FUND.SHARECLASS.REPORTING.CODE` | `FsGiFundShareclass_ReportingCode` | TField |  | The Reporting Code of the security which are used for the performance fees and Series of shares modules. Multifonds DB Column is CODE_RAPPORT. |
| 63 | `FS.GI.FUND.SHARECLASS.HURDLE.RATE` | `FsGiFundShareclass_HurdleRate` | TField |  | Hurdle rate. Multifonds DB Column is HURDLE_RATE. |
| 64 | `FS.GI.FUND.SHARECLASS.HURDLE.FOR.SERIES.FLAG` | `FsGiFundShareclass_HurdleForSeriesFlag` | TField |  | Hurdle for series flag. Multifonds DB Column is FLG_HURDLE. |
| 65 | `FS.GI.FUND.SHARECLASS.DISTRIBUTION.TYPE` | `FsGiFundShareclass_DistributionType` | TField |  | Dividend distribution type code for the fund and share class. Multifonds DB Column is CDIV_DISTRIB_TYPE. |
| 66 | `FS.GI.FUND.SHARECLASS.COLLAPSE.RECIPIENT.FLAG` | `FsGiFundShareclass_CollapseRecipientFlag` | TField |  | Flag allows specify the series as the lead series for the end of period merge. Multifonds DB Column is FLG_RECIPIENT. |
| 67 | `FS.GI.FUND.SHARECLASS.DAILY.DIVIDEND.FLAG` | `FsGiFundShareclass_DailyDividendFlag` | TField |  | Flag allows to specify the TA fund (with fund type as &apos;0006 - Money Market - Stable NAV Fund&apos;) is daily dividend fund. Multifonds DB Column is FLG_DAILY_DIV. |
| 68 | `FS.GI.FUND.SHARECLASS.NEGATIVE.DAILY.DIV.FLAG` | `FsGiFundShareclass_NegativeDailyDivFlag` | TField |  | Flag allows accepting the negative daily dividend rates for the fund share class. Multifonds DB Column is FLG_NEG_DAILY_DIV. |
| 69 | `FS.GI.FUND.SHARECLASS.PRIVATE.EQUITY.PRICING.METHOD` | `FsGiFundShareclass_PrivateEquityPricingMethod` | TField |  | It specifies the pricing method of Private Equity or Real Estate fund. Multifonds DB Column is PE_RE_PRICE_METHOD. |
| 70 | `FS.GI.FUND.SHARECLASS.CAPITAL.TRANCHE.FLAG` | `FsGiFundShareclass_CapitalTrancheFlag` | TField |  | Flag allows to specify that the share class works by tranche of committed capital. Multifonds DB Column is FLG_CAP_TRANCHE. |
| 71 | `FS.GI.FUND.SHARECLASS.MONTH.END.YIELD.RATE` | `FsGiFundShareclass_MonthEndYieldRate` | TField |  | Flag enables the shareclass to receive Month End yield rates. Multifonds DB Column is FLG_ME_YLD_RATE. |
| 72 | `FS.GI.FUND.SHARECLASS.CALCULATION.TYPE` | `FsGiFundShareclass_CalculationType` | TField |  | Security Calculation type. Multifonds DB Column is CCALCUL. |
| 73 | `FS.GI.FUND.SHARECLASS.TYPE` | `FsGiFundShareclass_Type` | TField |  | Security Type ID code. Multifonds DB Column is CGTI. |
| 74 | `FS.GI.FUND.SHARECLASS.LOCAL.TYPE` | `FsGiFundShareclass_LocalType` | TField |  | Local Type Code which are used to generate statutory reports as required by the authorities. Multifonds DB Column is COTLOCALE. |
| 75 | `FS.GI.FUND.SHARECLASS.QUOTATION.PLACE.CODE` | `FsGiFundShareclass_QuotationPlaceCode` | TField |  | The stock exchange from which a market price of the security is required. Multifonds DB Column is CPLACE. |
| 76 | `FS.GI.FUND.SHARECLASS.FEE.CODE` | `FsGiFundShareclass_FeeCode` | TField |  | Fee code which allows the user to exclude / Include certain securities for accrued expenses calculation. Multifonds DB Column is FFEES. |
| 77 | `FS.GI.FUND.SHARECLASS.ISSUER.EXTERNAL.ID` | `FsGiFundShareclass_IssuerExternalId` | TField |  | The External ID of the Issuer. The issuer is mainly used for compliance purposes. Issuers needs to be defined in the central register list. Multifonds DB Column is NISSUING. |
| 78 | `FS.GI.FUND.SHARECLASS.BRANCH.CODE` | `FsGiFundShareclass_BranchCode` | TField |  | Branch Ccode applicable to the security. Multifonds DB Column is SCO. |
| 79 | `FS.GI.FUND.SHARECLASS.INCOME.TYPE` | `FsGiFundShareclass_IncomeType` | TField |  | Income type for the security. Multifonds DB Column is TREVENU. |
| 80 | `FS.GI.FUND.SHARECLASS.CURRENCY` | `FsGiFundShareclass_Currency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CMONREF. |
| 81 | `FS.GI.FUND.SHARECLASS.TA.FUND.ID` | `FsGiFundShareclass_TaFundId` | TField |  | TA Fund is an Internal ID with combination of Fund ID and Class Currency. Multifonds DB Column is NPTF. |
| 82 | `FS.GI.FUND.SHARECLASS.ISIN.COUNTRY.CODE` | `FsGiFundShareclass_IsinCountryCode` | TField |  | Two letter word country code allocated to the secruity where fund is domiciled by the International Organization for Standardization (ISO). Multifonds DB Column is CODISIN. |
| 83 | `FS.GI.FUND.SHARECLASS.ISIN.IDENTIFIER` | `FsGiFundShareclass_IsinIdentifier` | TField |  | Identifier of the security. With combination of ISIN Country code, it will derive the ISIN code. Multifonds DB Column is SEQISIN. |
| 84 | `FS.GI.FUND.SHARECLASS.BENCHMARK.INDEX.1` | `FsGiFundShareclass_BenchmarkIndex1` | TField |  | Benchmark index 1. Multifonds DB Column is NOVAL_BENCHMARK_1. |
| 85 | `FS.GI.FUND.SHARECLASS.BENCHMARK.INDEX.2` | `FsGiFundShareclass_BenchmarkIndex2` | TField |  | Benchmark index 2. Multifonds DB Column is NOVAL_BENCHMARK_2. |
| 86 | `FS.GI.FUND.SHARECLASS.BENCHMARK.INDEX.3` | `FsGiFundShareclass_BenchmarkIndex3` | TField |  | Benchmark index 3. Multifonds DB Column is NOVAL_BENCHMARK_3. |
| 87 | `FS.GI.FUND.SHARECLASS.BENCHMARK.INDEX.4` | `FsGiFundShareclass_BenchmarkIndex4` | TField |  | Benchmark index 4. Multifonds DB Column is NOVAL_BENCHMARK_4. |
| 88 | `FS.GI.FUND.SHARECLASS.BENCHMARK.INDEX.5` | `FsGiFundShareclass_BenchmarkIndex5` | TField |  | Benchmark index 5. Multifonds DB Column is NOVAL_BENCHMARK_5. |
| 89 | `FS.GI.FUND.SHARECLASS.RESERVED10` | `FsGiFundShareclass_Reserved10` | TField |  |  |
| 90 | `FS.GI.FUND.SHARECLASS.RESERVED9` | `FsGiFundShareclass_Reserved9` | TField |  |  |
| 91 | `FS.GI.FUND.SHARECLASS.RESERVED8` | `FsGiFundShareclass_Reserved8` | TField |  |  |
| 92 | `FS.GI.FUND.SHARECLASS.RESERVED7` | `FsGiFundShareclass_Reserved7` | TField |  |  |
| 93 | `FS.GI.FUND.SHARECLASS.RESERVED6` | `FsGiFundShareclass_Reserved6` | TField |  |  |
| 94 | `FS.GI.FUND.SHARECLASS.RESERVED5` | `FsGiFundShareclass_Reserved5` | TField |  |  |
| 95 | `FS.GI.FUND.SHARECLASS.RESERVED4` | `FsGiFundShareclass_Reserved4` | TField |  |  |
| 96 | `FS.GI.FUND.SHARECLASS.RESERVED3` | `FsGiFundShareclass_Reserved3` | TField |  |  |
| 97 | `FS.GI.FUND.SHARECLASS.RESERVED2` | `FsGiFundShareclass_Reserved2` | TField |  |  |
| 98 | `FS.GI.FUND.SHARECLASS.RESERVED1` | `FsGiFundShareclass_Reserved1` | TField |  |  |
| 99 | `FS.GI.FUND.SHARECLASS.LOCAL.REF` | `FsGiFundShareclass_LocalRef` |  |  |  |
| 100 | `FS.GI.FUND.SHARECLASS.OVERRIDE` | `FsGiFundShareclass_Override` |  |  |  |
| 101 | `FS.GI.FUND.SHARECLASS.RECORD.STATUS` | `FsGiFundShareclass_RecordStatus` | String |  |  |
| 102 | `FS.GI.FUND.SHARECLASS.CURR.NO` | `FsGiFundShareclass_CurrNo` | String |  |  |
| 103 | `FS.GI.FUND.SHARECLASS.INPUTTER` | `FsGiFundShareclass_Inputter` |  |  |  |
| 104 | `FS.GI.FUND.SHARECLASS.DATE.TIME` | `FsGiFundShareclass_DateTime` |  |  |  |
| 105 | `FS.GI.FUND.SHARECLASS.AUTHORISER` | `FsGiFundShareclass_Authoriser` | String |  |  |
| 106 | `FS.GI.FUND.SHARECLASS.CO.CODE` | `FsGiFundShareclass_CoCode` | String |  |  |
| 107 | `FS.GI.FUND.SHARECLASS.DEPT.CODE` | `FsGiFundShareclass_DeptCode` | String |  |  |
| 108 | `FS.GI.FUND.SHARECLASS.AUDITOR.CODE` | `FsGiFundShareclass_AuditorCode` | String |  |  |
| 109 | `FS.GI.FUND.SHARECLASS.AUDIT.DATE.TIME` | `FsGiFundShareclass_AuditDateTime` | String |  |  |
