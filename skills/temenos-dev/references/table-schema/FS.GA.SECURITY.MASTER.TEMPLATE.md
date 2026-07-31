# FS.GA.SECURITY.MASTER.TEMPLATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.MASTER.TEMPLATE` in `FS_SecurityMasterConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.MASTER.TEMPLATE.PARENT.REF.ID` | `FsGaSecurityMasterTemplate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.MASTER.TEMPLATE.ORA.ROWID` | `FsGaSecurityMasterTemplate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.MASTER.TEMPLATE.GTI.CODE` | `FsGaSecurityMasterTemplate_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 4 | `FS.GA.SECURITY.MASTER.TEMPLATE.QUOTATION.PLACE` | `FsGaSecurityMasterTemplate_QuotationPlace` | TField |  | Quotation Place Multifonds DB Column is CPLACE. |
| 5 | `FS.GA.SECURITY.MASTER.TEMPLATE.NOMINAL.VALUE` | `FsGaSecurityMasterTemplate_NominalValue` | TField |  | Nominal of the Instrument Multifonds DB Column is NOMINAL. |
| 6 | `FS.GA.SECURITY.MASTER.TEMPLATE.PRICING.FACTOR.CODE` | `FsGaSecurityMasterTemplate_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 7 | `FS.GA.SECURITY.MASTER.TEMPLATE.CIMP.SOURCE` | `FsGaSecurityMasterTemplate_CimpSource` | TField |  | Cimp source Multifonds DB Column is CIMPSOURCE. |
| 8 | `FS.GA.SECURITY.MASTER.TEMPLATE.INCOME.TYPE` | `FsGaSecurityMasterTemplate_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 9 | `FS.GA.SECURITY.MASTER.TEMPLATE.DEPOSITORY` | `FsGaSecurityMasterTemplate_Depository` | TField |  | Third party depository/correcpondence number Multifonds DB Column is NRACINE. |
| 10 | `FS.GA.SECURITY.MASTER.TEMPLATE.SECTOR` | `FsGaSecurityMasterTemplate_Sector` | TField |  | Industry sector linked to a correspondent Multifonds DB Column is SCO. |
| 11 | `FS.GA.SECURITY.MASTER.TEMPLATE.FEES.CODE` | `FsGaSecurityMasterTemplate_FeesCode` | TField |  | This field hepls the user to take into account or remove from the fees based amount the sum of specific fees codes setup of the security master. Multifonds DB Column is FFEES. |
| 12 | `FS.GA.SECURITY.MASTER.TEMPLATE.LOCALE.TYPE` | `FsGaSecurityMasterTemplate_LocaleType` | TField |  | Local Type of granular information to query in Chart Charesteric screen Multifonds DB Column is COTLOCALE. |
| 13 | `FS.GA.SECURITY.MASTER.TEMPLATE.EVALUATION.TYPE` | `FsGaSecurityMasterTemplate_EvaluationType` | TField |  | Valuation method for specific security types such as zero bonds, polish T-bills, Mortgaged Backed Securities. Multifonds DB Column is TEVALUATION. |
| 14 | `FS.GA.SECURITY.MASTER.TEMPLATE.REPORTING.CODE` | `FsGaSecurityMasterTemplate_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 15 | `FS.GA.SECURITY.MASTER.TEMPLATE.INSTRUMENT.CODE` | `FsGaSecurityMasterTemplate_InstrumentCode` | TField |  | This is can be defined to so that transaction can be processed by charging default fees based on different countries of trading. Multifonds DB Column is CINSTRUMENT. |
| 16 | `FS.GA.SECURITY.MASTER.TEMPLATE.RISK.CODE` | `FsGaSecurityMasterTemplate_RiskCode` | TField |  | This field is used to store the risk type for the Catastrophe bonds. Multifonds DB Column is CGTI_RISK. |
| 17 | `FS.GA.SECURITY.MASTER.TEMPLATE.PRICE.SOURCE` | `FsGaSecurityMasterTemplate_PriceSource` | TField |  | Provider code like Telekers, Reuters etc Multifonds DB Column is CORC. |
| 18 | `FS.GA.SECURITY.MASTER.TEMPLATE.SECURITY.EX.COUPON.DATE` | `FsGaSecurityMasterTemplate_SecurityExCouponDate` | TField |  | allows review and update of the ex-coupon dates for the interest receivable. Multifonds DB Column is FLG_EXCOUPON. |
| 19 | `FS.GA.SECURITY.MASTER.TEMPLATE.USE.TRADE.DATE` | `FsGaSecurityMasterTemplate_UseTradeDate` | TField |  | If set, accrued interest on securities purchases and sales will be calculated as of the trade date of the respective transaction. If not set, will be calculated as of the value date. Multifonds DB Column is FLG_INT_TRADE. |
| 20 | `FS.GA.SECURITY.MASTER.TEMPLATE.ISSUE.COUNTRY` | `FsGaSecurityMasterTemplate_IssueCountry` | TField |  | Internal Identifier for a country, which is used in various places to include or exclude a specific country from a functionality Multifonds DB Column is CPAYSVAL. |
| 21 | `FS.GA.SECURITY.MASTER.TEMPLATE.COUPON.FREQUENCY.CODE` | `FsGaSecurityMasterTemplate_CouponFrequencyCode` | TField |  | Frequency of payment of coupon/ commission Multifonds DB Column is CFREQCOUP. |
| 22 | `FS.GA.SECURITY.MASTER.TEMPLATE.DAY.COUNT.CONVENTION` | `FsGaSecurityMasterTemplate_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 23 | `FS.GA.SECURITY.MASTER.TEMPLATE.FCYIELD` | `FsGaSecurityMasterTemplate_Fcyield` | TField |  | Yield Multifonds DB Column is FCYIELD. |
| 24 | `FS.GA.SECURITY.MASTER.TEMPLATE.OFFICIAL.STOCK.EXCHANGE` | `FsGaSecurityMasterTemplate_OfficialStockExchange` | TField | Yes | It has the same characteristics as the field &quot;quotation place&quot;, but it is not a mandatory field. Multifonds DB Column is OFF_STOCK_EXCHGE. |
| 25 | `FS.GA.SECURITY.MASTER.TEMPLATE.ISSUER` | `FsGaSecurityMasterTemplate_Issuer` | TField |  | To enter Issuer of the security Multifonds DB Column is NISSUING. |
| 26 | `FS.GA.SECURITY.MASTER.TEMPLATE.RISK.COUNTERPARTY` | `FsGaSecurityMasterTemplate_RiskCounterparty` | TField |  | Risk correspondent number Multifonds DB Column is NCORR_RISQUE. |
| 27 | `FS.GA.SECURITY.MASTER.TEMPLATE.SWAP` | `FsGaSecurityMasterTemplate_Swap` | TField |  | Swapped security flag Multifonds DB Column is FLAG_SWAP. |
| 28 | `FS.GA.SECURITY.MASTER.TEMPLATE.LETTER.OF.CREDIT` | `FsGaSecurityMasterTemplate_LetterOfCredit` | TField |  | Indicates the security is backed by a Letter of Credit Multifonds DB Column is FLG_LOC. |
| 29 | `FS.GA.SECURITY.MASTER.TEMPLATE.EXPIRATION.DATE` | `FsGaSecurityMasterTemplate_ExpirationDate` | TField |  | Epiration date of the letter of credit which is backing the security. Multifonds DB Column is EXPIRATION_DATE. |
| 30 | `FS.GA.SECURITY.MASTER.TEMPLATE.COUNTER.PARTY.CODE` | `FsGaSecurityMasterTemplate_CounterPartyCode` | TField |  | Guarantor,Issuer Multifonds DB Column is NISSUER_GUARANTEED. |
| 31 | `FS.GA.SECURITY.MASTER.TEMPLATE.COUPON.GENERATION` | `FsGaSecurityMasterTemplate_CouponGeneration` | TField |  | Helps in definining how manage the coupon payment on holiday Multifonds DB Column is COUP_GEN. |
| 32 | `FS.GA.SECURITY.MASTER.TEMPLATE.SOURCE` | `FsGaSecurityMasterTemplate_Source` | TField |  | Quotation source Multifonds DB Column is XSOURCE. |
| 33 | `FS.GA.SECURITY.MASTER.TEMPLATE.GUARANTEE.CODE` | `FsGaSecurityMasterTemplate_GuaranteeCode` | TField |  | This field defines if the securities are idenfied as Guaranteed or Non Guaranteed Multifonds DB Column is CGARANTIE. |
| 34 | `FS.GA.SECURITY.MASTER.TEMPLATE.ACCOUNTING.FACTOR` | `FsGaSecurityMasterTemplate_AccountingFactor` | TField |  | Used for German compliance (MIG21). The factor indicates to which extent an amount has to be imputed for the calculation of the limits. Multifonds DB Column is ACC_FACTOR. |
| 35 | `FS.GA.SECURITY.MASTER.TEMPLATE.THEORETICAL.DATE` | `FsGaSecurityMasterTemplate_TheoreticalDate` | TField |  | Theoretical date Multifonds DB Column is THEORETICAL_DATE. |
| 36 | `FS.GA.SECURITY.MASTER.TEMPLATE.YIELD.CAP` | `FsGaSecurityMasterTemplate_YieldCap` | TField |  | the computed yield to maturity using the YTM formula for fixed income securities is &gt; Yield cap then the Yield cap is used for computing SEC income. Multifonds DB Column is YIELD_CAP. |
| 37 | `FS.GA.SECURITY.MASTER.TEMPLATE.PERCENTAGE.OF.FEES` | `FsGaSecurityMasterTemplate_PercentageOfFees` | TField |  | The percentage of fee calculated at target fund level is set in the field &quot;Percentage of fees Multifonds DB Column is PCT_FPRT. |
| 38 | `FS.GA.SECURITY.MASTER.TEMPLATE.MINIMUM.AMOUNT` | `FsGaSecurityMasterTemplate_MinimumAmount` | TField |  | define a minimum amount for the transaction Multifonds DB Column is MIN_FPRT. |
| 39 | `FS.GA.SECURITY.MASTER.TEMPLATE.MAXIMUM.AMOUNT` | `FsGaSecurityMasterTemplate_MaximumAmount` | TField |  | define a maximum amount for the transaction Multifonds DB Column is MAX_FPRT. |
| 40 | `FS.GA.SECURITY.MASTER.TEMPLATE.MINIMUM.QUANTITY` | `FsGaSecurityMasterTemplate_MinimumQuantity` | TField |  | to define the minimum quantity that must be purchased or sold of the security Multifonds DB Column is MIN_QUANTITY. |
| 41 | `FS.GA.SECURITY.MASTER.TEMPLATE.MINIMUM.INCREMENT` | `FsGaSecurityMasterTemplate_MinimumIncrement` | TField |  | Define prevent users to process transactions into Multifonds with an incorrect incremental value Multifonds DB Column is MIN_INCREMENT. |
| 42 | `FS.GA.SECURITY.MASTER.TEMPLATE.SUBMITTED` | `FsGaSecurityMasterTemplate_Submitted` | TField |  | Submission of records for processing or saving record. Multifonds DB Column is CSUBMIT. |
| 43 | `FS.GA.SECURITY.MASTER.TEMPLATE.DEFAULT.STATUS` | `FsGaSecurityMasterTemplate_DefaultStatus` | TField |  | Indicate is the security is in default status Multifonds DB Column is FLG_DEFAULT_INT. |
| 44 | `FS.GA.SECURITY.MASTER.TEMPLATE.ROUNDING.CODE` | `FsGaSecurityMasterTemplate_RoundingCode` | TField |  | Decimal Rounding Code Multifonds DB Column is CDEC_ROUND. |
| 45 | `FS.GA.SECURITY.MASTER.TEMPLATE.INTEREST.DEFAULT.END.DATE` | `FsGaSecurityMasterTemplate_InterestDefaultEndDate` | TField |  | Interest Default End Date:The interest accrual will begin on the fund from this date forward Multifonds DB Column is DDEFAULT_END. |
| 46 | `FS.GA.SECURITY.MASTER.TEMPLATE.INTEREST.DEFAULT.START.DATE` | `FsGaSecurityMasterTemplate_InterestDefaultStartDate` | TField |  | Interest Default Start Date:The interest accrual will stop on the fund from this date forward Multifonds DB Column is DDEFAULT_START. |
| 47 | `FS.GA.SECURITY.MASTER.TEMPLATE.PUBLIC.CYCLE` | `FsGaSecurityMasterTemplate_PublicCycle` | TField |  | Frequency ode of the Consumer Price Index -CPI. The publication cycle of the index security is defined with its publication frequency (e.g. 5 for monthly, 6 for quarterly...).Its used for IPBs. Multifonds DB Column is COD_CYCLE. |
| 48 | `FS.GA.SECURITY.MASTER.TEMPLATE.TRUNCATION.CODE` | `FsGaSecurityMasterTemplate_TruncationCode` | TField |  | This field will be used to truncate The index factor automatically with defined decimal number Multifonds DB Column is CDEC_TRUNC. |
| 49 | `FS.GA.SECURITY.MASTER.TEMPLATE.LOOK.BACK.START.PERIOD` | `FsGaSecurityMasterTemplate_LookBackStartPeriod` | TField |  | Number of publication cycles that have to be turned backwards from the given date to select the inflation value for the start-point required for index factor calculation (e.g. 002 = 2 months). Multifonds DB Column is CMONTH_START. |
| 50 | `FS.GA.SECURITY.MASTER.TEMPLATE.LOOK.BACK.PERIOD.END` | `FsGaSecurityMasterTemplate_LookBackPeriodEnd` | TField |  | Number of publication cycles that have to be turned backwards from the given date to select the inflation value for the end-point required for index factor calculation (e.g. 003 = 3 months). Multifonds DB Column is CMONTH_END. |
| 51 | `FS.GA.SECURITY.MASTER.TEMPLATE.REFERENCE.CONSUMER.PRICE.INDEX` | `FsGaSecurityMasterTemplate_ReferenceConsumerPriceIndex` | TField |  | Define the reference Consumer Price Index as at the issue date of the Inflation Protected bond. Multifonds DB Column is REF_CPI. |
| 52 | `FS.GA.SECURITY.MASTER.TEMPLATE.RISK.ACT` | `FsGaSecurityMasterTemplate_RiskAct` | TField |  | to define if securities will appear on the French Legal report &apos;Share risk exposition&apos;. Multifonds DB Column is FLG_RISK_ACT. |
| 53 | `FS.GA.SECURITY.MASTER.TEMPLATE.FIXED.RATE.RISK` | `FsGaSecurityMasterTemplate_FixedRateRisk` | TField |  | If set, securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos;. Multifonds DB Column is FLG_FR_RISK. |
| 54 | `FS.GA.SECURITY.MASTER.TEMPLATE.VARIABLE.RATE.RISK` | `FsGaSecurityMasterTemplate_VariableRateRisk` | TField |  | to define if securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos;. Multifonds DB Column is FLG_VR_RISK. |
| 55 | `FS.GA.SECURITY.MASTER.TEMPLATE.OTHER.RATE.RISK` | `FsGaSecurityMasterTemplate_OtherRateRisk` | TField |  | to define if securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos; Multifonds DB Column is FLG_RATE_OTH. |
| 56 | `FS.GA.SECURITY.MASTER.TEMPLATE.FLOATING.RATE.RISK` | `FsGaSecurityMasterTemplate_FloatingRateRisk` | TField |  | to define if securities will appear on the French Legal reports: &apos;Rate risk report&apos; and &apos;Ventilation by interest rate type report&apos;. Multifonds DB Column is FLG_RISK_FLT. |
| 57 | `FS.GA.SECURITY.MASTER.TEMPLATE.DIVIDEND.RATE` | `FsGaSecurityMasterTemplate_DividendRate` | TField |  | Dividend rate of security Multifonds DB Column is DIV_RATE. |
| 58 | `FS.GA.SECURITY.MASTER.TEMPLATE.DIVIDEND.FREQUENCY` | `FsGaSecurityMasterTemplate_DividendFrequency` | TField |  | Dividend Frequency of a security Multifonds DB Column is DIV_FREQ. |
| 59 | `FS.GA.SECURITY.MASTER.TEMPLATE.LAST.DIVIDEND.DECLARATION.DATE` | `FsGaSecurityMasterTemplate_LastDividendDeclarationDate` | TField |  | Last Dividend Declaration Date of the security Multifonds DB Column is DLAST_DIV. |
| 60 | `FS.GA.SECURITY.MASTER.TEMPLATE.TBC.SUSPENSION.START` | `FsGaSecurityMasterTemplate_TbcSuspensionStart` | TField |  | Tax Book Cost Suspension start Date Multifonds DB Column is DDEBUT_TBC. |
| 61 | `FS.GA.SECURITY.MASTER.TEMPLATE.TBC.SUSPENSION.END` | `FsGaSecurityMasterTemplate_TbcSuspensionEnd` | TField |  | Tax Book Cost Suspension end Date Multifonds DB Column is DFIN_TBC. |
| 62 | `FS.GA.SECURITY.MASTER.TEMPLATE.DATE.OF.INDIRECT.INVESTMENT` | `FsGaSecurityMasterTemplate_DateOfIndirectInvestment` | TField |  | Indirect Investment Date Multifonds DB Column is D_IND_INV_2. |
| 63 | `FS.GA.SECURITY.MASTER.TEMPLATE.COUNTERPARTY.CORRESPONDENT` | `FsGaSecurityMasterTemplate_CounterpartyCorrespondent` | TField |  | Counterparty Correspondant Multifonds DB Column is NCORRESP_CTR. |
| 64 | `FS.GA.SECURITY.MASTER.TEMPLATE.INSTRUMENT.CODE.2` | `FsGaSecurityMasterTemplate_InstrumentCode2` | TField |  | This field is used for compliance purpose. This field is an alternative to Instrument code 1 (MIG21). It is country of incorporation whenever applicable. Multifonds DB Column is CINSTRUMENT2. |
| 65 | `FS.GA.SECURITY.MASTER.TEMPLATE.STATE.CODE` | `FsGaSecurityMasterTemplate_StateCode` | TField |  | Field is used to store the region type for Catastrophe bonds Multifonds DB Column is STATE_CODE. |
| 66 | `FS.GA.SECURITY.MASTER.TEMPLATE.USER.DEFINABLE.FIELDS.GROUP` | `FsGaSecurityMasterTemplate_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 67 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED10` | `FsGaSecurityMasterTemplate_Reserved10` | TField |  |  |
| 68 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED9` | `FsGaSecurityMasterTemplate_Reserved9` | TField |  |  |
| 69 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED8` | `FsGaSecurityMasterTemplate_Reserved8` | TField |  |  |
| 70 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED7` | `FsGaSecurityMasterTemplate_Reserved7` | TField |  |  |
| 71 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED6` | `FsGaSecurityMasterTemplate_Reserved6` | TField |  |  |
| 72 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED5` | `FsGaSecurityMasterTemplate_Reserved5` | TField |  |  |
| 73 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED4` | `FsGaSecurityMasterTemplate_Reserved4` | TField |  |  |
| 74 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED3` | `FsGaSecurityMasterTemplate_Reserved3` | TField |  |  |
| 75 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED2` | `FsGaSecurityMasterTemplate_Reserved2` | TField |  |  |
| 76 | `FS.GA.SECURITY.MASTER.TEMPLATE.RESERVED1` | `FsGaSecurityMasterTemplate_Reserved1` | TField |  |  |
| 77 | `FS.GA.SECURITY.MASTER.TEMPLATE.LOCAL.REF` | `FsGaSecurityMasterTemplate_LocalRef` |  |  |  |
| 78 | `FS.GA.SECURITY.MASTER.TEMPLATE.OVERRIDE` | `FsGaSecurityMasterTemplate_Override` |  |  |  |
| 79 | `FS.GA.SECURITY.MASTER.TEMPLATE.RECORD.STATUS` | `FsGaSecurityMasterTemplate_RecordStatus` | String |  |  |
| 80 | `FS.GA.SECURITY.MASTER.TEMPLATE.CURR.NO` | `FsGaSecurityMasterTemplate_CurrNo` | String |  |  |
| 81 | `FS.GA.SECURITY.MASTER.TEMPLATE.INPUTTER` | `FsGaSecurityMasterTemplate_Inputter` |  |  |  |
| 82 | `FS.GA.SECURITY.MASTER.TEMPLATE.DATE.TIME` | `FsGaSecurityMasterTemplate_DateTime` |  |  |  |
| 83 | `FS.GA.SECURITY.MASTER.TEMPLATE.AUTHORISER` | `FsGaSecurityMasterTemplate_Authoriser` | String |  |  |
| 84 | `FS.GA.SECURITY.MASTER.TEMPLATE.CO.CODE` | `FsGaSecurityMasterTemplate_CoCode` | String |  |  |
| 85 | `FS.GA.SECURITY.MASTER.TEMPLATE.DEPT.CODE` | `FsGaSecurityMasterTemplate_DeptCode` | String |  |  |
| 86 | `FS.GA.SECURITY.MASTER.TEMPLATE.AUDITOR.CODE` | `FsGaSecurityMasterTemplate_AuditorCode` | String |  |  |
| 87 | `FS.GA.SECURITY.MASTER.TEMPLATE.AUDIT.DATE.TIME` | `FsGaSecurityMasterTemplate_AuditDateTime` | String |  |  |
