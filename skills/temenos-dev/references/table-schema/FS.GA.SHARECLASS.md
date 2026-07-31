# FS.GA.SHARECLASS — Table Schema

> Source: `INSERTS/I_F.FS.GA.SHARECLASS` in `FS_FundMasterAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SHARECLASS.PARENT.REF.ID` | `FsGaShareclass_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SHARECLASS.ORA.ROWID` | `FsGaShareclass_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SHARECLASS.FUND.ID` | `FsGaShareclass_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SHARECLASS.SHARE.CLASS.CODE` | `FsGaShareclass_ShareClassCode` | TField |  | Share Class Code Multifonds DB Column is TPARTS. |
| 5 | `FS.GA.SHARECLASS.COUPON` | `FsGaShareclass_Coupon` | TField |  | This field allows to define how the coupon income should be treatred. User can enter &apos;D&apos; for dividend distributed income or &apos;R&apos; for reinvestment. Multifonds DB Column is TREV. |
| 6 | `FS.GA.SHARECLASS.SHARE.QUANTITY` | `FsGaShareclass_ShareQuantity` | TField |  | This field automatically updates number of shares outstanding on NAV accounting. Multifonds DB Column is QT_PART. |
| 7 | `FS.GA.SHARECLASS.PART.AMOUNT` | `FsGaShareclass_PartAmount` | TField |  | Part Amount Multifonds DB Column is MNT_PART. |
| 8 | `FS.GA.SHARECLASS.REV.EQUALISATION` | `FsGaShareclass_RevEqualisation` | TField |  | Rev Equalization Multifonds DB Column is REV_EGAL. |
| 9 | `FS.GA.SHARECLASS.INTERNAL.SECURITY.ID` | `FsGaShareclass_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 10 | `FS.GA.SHARECLASS.SUBSCRIPTION.ACCOUNT.NUMBER` | `FsGaShareclass_SubscriptionAccountNumber` | TField |  | This field allows to define the account number on which subscription is accounted. Multifonds DB Column is NRUBR_SUBS. |
| 11 | `FS.GA.SHARECLASS.REDEMPTION.ACCOUNT.NUMBER` | `FsGaShareclass_RedemptionAccountNumber` | TField |  | This field allows to define the account number on which redemption is accounted. Multifonds DB Column is NRUBR_REMB. |
| 12 | `FS.GA.SHARECLASS.TARGET.YIELD` | `FsGaShareclass_TargetYield` | TField |  | This field refers to the minimum target yield for dividend distribution in a daily dividend distribution fund. Multifonds DB Column is TARGET_YIELD. |
| 13 | `FS.GA.SHARECLASS.INCOME.ACCOUNT.NUMBER` | `FsGaShareclass_IncomeAccountNumber` | TField |  | This field allows to define the account number on which income distribution of the fund is accounted. Multifonds DB Column is NRUBR_INCOME. |
| 14 | `FS.GA.SHARECLASS.EQUALISATION.ON.INTEREST` | `FsGaShareclass_EqualisationOnInterest` | TField |  | Equalization On Interest Multifonds DB Column is EGAL_INT_REPRISE. |
| 15 | `FS.GA.SHARECLASS.EQUALISATION.ON.FEES` | `FsGaShareclass_EqualisationOnFees` | TField |  | Equalization On Fees Multifonds DB Column is EGAL_FRAIS_REPRISE. |
| 16 | `FS.GA.SHARECLASS.EQUALISATION.ON.DIVIDEND` | `FsGaShareclass_EqualisationOnDividend` | TField |  | Equalization On Dividend Multifonds DB Column is EGAL_DIV_REPRISE. |
| 17 | `FS.GA.SHARECLASS.DISTRIBUTION.INCOME.TYPE` | `FsGaShareclass_DistributionIncomeType` | TField |  | This field allows defining the distribution and the allocation methodology of the P/L accounts between the different share class IDs. Multifonds DB Column is TYP_DISTR_INC. |
| 18 | `FS.GA.SHARECLASS.DIVIDEND.GROUP` | `FsGaShareclass_DividendGroup` | TField |  | This field indicates a dividend group number (any number between 1 and 99) for all units where the daily dividend amount must be identical (identical dividends = identical dividend group codes). Multifonds DB Column is COD_DIV_GRP. |
| 19 | `FS.GA.SHARECLASS.MAXIMUM.TARGET.YIELD` | `FsGaShareclass_MaximumTargetYield` | TField |  | This field refers to the maximum target yield for dividend distribution in a daily dividend distribution fund. Multifonds DB Column is TARGET_YIELD_MAX. |
| 20 | `FS.GA.SHARECLASS.EQUALISATION.ON.FX.RESULTS` | `FsGaShareclass_EqualisationOnFxResults` | TField |  | Equalization On FX Results Multifonds DB Column is EGAL_CHANGE_REPRISE. |
| 21 | `FS.GA.SHARECLASS.EQUALISATION.ON.REALISED.GAINS` | `FsGaShareclass_EqualisationOnRealisedGains` | TField |  | Equalization On Realized Gains Multifonds DB Column is EGAL_VTE_PT_REPRISE. |
| 22 | `FS.GA.SHARECLASS.EQUALISATION.UNREALISED.GAINS` | `FsGaShareclass_EqualisationUnrealisedGains` | TField |  | Equalization Unrealized Gains Multifonds DB Column is EGAL_NON_PT_REPRISE. |
| 23 | `FS.GA.SHARECLASS.FUND.SHARE.TYPE` | `FsGaShareclass_FundShareType` | TField |  | Fund Share Type Multifonds DB Column is NPTF_SUB. |
| 24 | `FS.GA.SHARECLASS.SUBSCRIPTION.SHARE.CLASS.CODE` | `FsGaShareclass_SubscriptionShareClassCode` | TField |  | Subscription Share class code Multifonds DB Column is TPARTS_SUB. |
| 25 | `FS.GA.SHARECLASS.BENCH.MARK.INDEX.1` | `FsGaShareclass_BenchMarkIndex1` | TField |  | Bench Mark Index security 1 - The functionality is Not in use Multifonds DB Column is NOVAL_BENCHMARK_1. |
| 26 | `FS.GA.SHARECLASS.BENCH.MARK.INDEX.2` | `FsGaShareclass_BenchMarkIndex2` | TField |  | Bench Mark Index security 2 - The functionality is Not in use Multifonds DB Column is NOVAL_BENCHMARK_2. |
| 27 | `FS.GA.SHARECLASS.BENCH.MARK.INDEX.3` | `FsGaShareclass_BenchMarkIndex3` | TField |  | Bench Mark Index security 3 - The functionality is Not in use Multifonds DB Column is NOVAL_BENCHMARK_3. |
| 28 | `FS.GA.SHARECLASS.BENCH.MARK.INDEX.4` | `FsGaShareclass_BenchMarkIndex4` | TField |  | Bench Mark Index security 4 - The functionality is Not in use Multifonds DB Column is NOVAL_BENCHMARK_4. |
| 29 | `FS.GA.SHARECLASS.BENCH.MARK.INDEX.5` | `FsGaShareclass_BenchMarkIndex5` | TField |  | Bench Mark Index security 5 - The functionality is Not in use Multifonds DB Column is NOVAL_BENCHMARK_5. |
| 30 | `FS.GA.SHARECLASS.EQUALISATION.ON.SPECIAL.LOSS` | `FsGaShareclass_EqualisationOnSpecialLoss` | TField |  | Equalization On Special Loss Multifonds DB Column is EGAL_REAL_SP_REPRISE. |
| 31 | `FS.GA.SHARECLASS.EQUALISATION.ON.SPECIAL.FEES` | `FsGaShareclass_EqualisationOnSpecialFees` | TField |  | Equalization On Special Fees Multifonds DB Column is EGAL_FRAIS_SP_REPRISE. |
| 32 | `FS.GA.SHARECLASS.BVI.BDB.CODE` | `FsGaShareclass_BviBdbCode` | TField |  | BVI BDB code for german reporting. Value N - Units not included for reporting, Y - Units included &amp; P - Units included in NAV details Multifonds DB Column is BVI_BDB_CODE. |
| 33 | `FS.GA.SHARECLASS.SHARE.TYPE` | `FsGaShareclass_ShareType` | TField |  | Related to Performance fees. It allows users distinguishing Bearer, Registered shares and Gross price, Net price (mainly used for the fees calculation). Multifonds DB Column is TYPE_SHARE. |
| 34 | `FS.GA.SHARECLASS.HYPOTHETICAL.INCOME.CORRECTION` | `FsGaShareclass_HypotheticalIncomeCorrection` | TField |  | Hypothetical Income Correction Multifonds DB Column is HI_PART_PREV. |
| 35 | `FS.GA.SHARECLASS.ADJUST.AMOUNT` | `FsGaShareclass_AdjustAmount` | TField |  | Adjustment Amount Multifonds DB Column is MSOLDE_AJUST_REPRISE. |
| 36 | `FS.GA.SHARECLASS.INITIAL.NAV.PRICE` | `FsGaShareclass_InitialNavPrice` | TField |  | Define the initial NAV price of a Share type held by a fund. This has to be entered to get the fields related to unit capital, unit premium and equalization reflected in the capstock transaction. Multifonds DB Column is INIT_PRICE_PART. |
| 37 | `FS.GA.SHARECLASS.PREVIOUS.UNUSED.INCOME.RELIEF` | `FsGaShareclass_PreviousUnusedIncomeRelief` | TField |  | Previous Unused Income Relief Multifonds DB Column is PREV_UN_INC_RELIEF_BF. |
| 38 | `FS.GA.SHARECLASS.PREVIOUS.UNUSED.CAPITAL.RELIEF` | `FsGaShareclass_PreviousUnusedCapitalRelief` | TField |  | Previous Unused Capital Relief Multifonds DB Column is PREV_UN_CAP_RELIEF_BF. |
| 39 | `FS.GA.SHARECLASS.UNUSED.INC.RELIEF.BF` | `FsGaShareclass_UnusedIncReliefBf` | TField |  | UK Corporate Tax- If the user defines the value U in the field &apos;Relief Calc.&apos; the unused income (b/f), retrieved at share class level, is automatically reset to 0 during the year end closing process. Multifonds DB Column is UN_INC_RELIEF_BF. |
| 40 | `FS.GA.SHARECLASS.UNUSED.CAP.RELIEF.BF` | `FsGaShareclass_UnusedCapReliefBf` | TField |  | UK Corporate Tax If the user defines the value U in the field &apos;Relief Calc.&apos; the unused capital (b/f), retrieved at share class level, is automatically reset to 0 during the year end closing process. Multifonds DB Column is UN_CAP_RELIEF_BF. |
| 41 | `FS.GA.SHARECLASS.TAX.REGIME` | `FsGaShareclass_TaxRegime` | TField |  | A group of Tax rules can be defined in the Tax tables against a Tax regime and all the funds defined with the respective Tax regime would follow the tax rules defined under this Tax regime. Multifonds DB Column is TAX_REG. |
| 42 | `FS.GA.SHARECLASS.FOOTNOTES` | `FsGaShareclass_Footnotes` | TField |  | Used in the context of US variable NAV mutual funds. Any recurring foot note can be input in the share values screen and will not need to be re-input on the NASDAQ submission screen on a daily basis. Multifonds DB Column is FOOTNOTES. |
| 43 | `FS.GA.SHARECLASS.KEST` | `FsGaShareclass_Kest` | TField |  | If Set, Austrian KEST will be calculated for the underlying share class Multifonds DB Column is FLG_KEST. |
| 44 | `FS.GA.SHARECLASS.STATPRO` | `FsGaShareclass_Statpro` | TField |  | If flagged, there will be Statpro export for the share class for AC transactions (subscriptions/redemptions). Also, a unique security ID has to be setup for each share class. Multifonds DB Column is FLG_STATPRO. |
| 45 | `FS.GA.SHARECLASS.ADJUSTED.IG.BALANCE` | `FsGaShareclass_AdjustedIgBalance` | TField |  | Adjusted IG Balance Multifonds DB Column is MSOLDE_AJUST_REPRISE_IG. |
| 46 | `FS.GA.SHARECLASS.BENCHMARK.SECURITY.ID` | `FsGaShareclass_BenchmarkSecurityId` | TField |  | This field is used in the context of the performance fee calculation. The index fund is linked to the gross NAV fund via this field. Multifonds DB Column is BMK_NOVAL. |
| 47 | `FS.GA.SHARECLASS.ROUNDING.SUB.PRICE` | `FsGaShareclass_RoundingSubPrice` | TField |  | Indicates how the subscription price should be rounded/truncated (at share class level). Multifonds DB Column is CDEC_ARR_SOUSC. |
| 48 | `FS.GA.SHARECLASS.ROUNDING.RED.PRICE` | `FsGaShareclass_RoundingRedPrice` | TField |  | Indicates how the redemption price should be rounded/truncated (at share class level). Multifonds DB Column is CDEC_ARR_RACHAT. |
| 49 | `FS.GA.SHARECLASS.NAV.ROUNDING.METHOD` | `FsGaShareclass_NavRoundingMethod` | TField |  | Displays the method code used for rounding the NAV Price (at share class level). Multifonds DB Column is CDEC_ARR_NAV. |
| 50 | `FS.GA.SHARECLASS.REFERENCE.SHARE.CLASS` | `FsGaShareclass_ReferenceShareClass` | TField |  | Share class is in scope for the exception report SDEXR11 (NAV control report) where one share class should be defined as a reference to justify the NAV/share variation Multifonds DB Column is FLG_REF_SHARE. |
| 51 | `FS.GA.SHARECLASS.BEGIN.DATE` | `FsGaShareclass_BeginDate` | TField |  | This field is used for the calculation of management expense ratio (MER) at the share class level. It refers to the launch date of a share class ID for MER reporting. Multifonds DB Column is BEGIN_DATE. |
| 52 | `FS.GA.SHARECLASS.END.DATE` | `FsGaShareclass_EndDate` | TField |  | This field is used for the calculation of management expense ratio (MER) at the share class level. It refers to the date upto which a share class is in existence for MER reporting. Multifonds DB Column is END_DATE. |
| 53 | `FS.GA.SHARECLASS.HURDLE.SECURITY.ID` | `FsGaShareclass_HurdleSecurityId` | TField |  | This field is used for the performance fee calculation. Enter here the security which represents the hurdle Multifonds DB Column is HURDLE_SEC_ID. |
| 54 | `FS.GA.SHARECLASS.SHARE.CLASS.ID.REFERENCE` | `FsGaShareclass_ShareClassIdReference` | TField |  | This field adjusts the multiclass rounding difference to the share class ID which is parameterized as reference class (Y&quot;) in case all the share classes have equal asset value.&quot; Multifonds DB Column is TPARTS_REF. |
| 55 | `FS.GA.SHARECLASS.DIVIDEND.CALCULATION` | `FsGaShareclass_DividendCalculation` | TField |  | This field enables the calculation of daily dividend rate on the cumulative (coupon &apos;R&apos;) share classes. Multifonds DB Column is FLG_CALC_DIV. |
| 56 | `FS.GA.SHARECLASS.PUBLISH.TIS` | `FsGaShareclass_PublishTis` | TField |  | The publication of TIS can be defined at global level or at fund&apos;s share class level which could be helpful for the funds in which different share classes are distributed in different countries. Multifonds DB Column is PUB_TIS. |
| 57 | `FS.GA.SHARECLASS.PUBLISH.IP` | `FsGaShareclass_PublishIp` | TField |  | If the flags Publish IP&quot; (button Addl. data) are ticked, then the tax IP figures will be published.&quot; Multifonds DB Column is FLG_PUB_IP. |
| 58 | `FS.GA.SHARECLASS.PUBLISH.AG` | `FsGaShareclass_PublishAg` | TField |  | If the flags Publish AG&quot; (button Addl. data) are ticked, then the tax AG figures will be published.&quot; Multifonds DB Column is FLG_PUB_AG. |
| 59 | `FS.GA.SHARECLASS.PUBLISH.IG` | `FsGaShareclass_PublishIg` | TField |  | This field enables the calculation of IG Multifonds DB Column is CALC_IG. |
| 60 | `FS.GA.SHARECLASS.QUOTATION.UNITS` | `FsGaShareclass_QuotationUnits` | TField |  | Enter units (NAV of the fund in such no. of units). In the context of taxable and non taxable NAV (Korea), the field &apos;Quotation units&apos; allows reporting the NAV of the fund in such number of units. Multifonds DB Column is QUOT_UNITS. |
| 61 | `FS.GA.SHARECLASS.DISTRIBUTION.TYPE` | `FsGaShareclass_DistributionType` | TField |  | This field refers to the year end distribution method. It is related to the Korean taxable NAV. Multifonds DB Column is DIST_TYPE. |
| 62 | `FS.GA.SHARECLASS.CORRESPONDENT` | `FsGaShareclass_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 63 | `FS.GA.SHARECLASS.ASSET.ALLOCATION` | `FsGaShareclass_AssetAllocation` | TField |  | Asset Allocation Multifonds DB Column is FLG_ASSET_CLASS. |
| 64 | `FS.GA.SHARECLASS.INITIAL.NAV.PRICE.FOR.ROR` | `FsGaShareclass_InitialNavPriceForRor` | TField |  | Initial NAV Price for ROR Multifonds DB Column is GROSS_ROR_NAV_PRICE. |
| 65 | `FS.GA.SHARECLASS.CLOSED` | `FsGaShareclass_Closed` | TField |  | Closed Multifonds DB Column is FLG_CLOSED. |
| 66 | `FS.GA.SHARECLASS.USER.DEFINABLE.FIELDS.GROUP` | `FsGaShareclass_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 67 | `FS.GA.SHARECLASS.SHARE.CLASS.ID.CURRENCY` | `FsGaShareclass_ShareClassIdCurrency` | TField |  | This field enables the user to manage share class currency other than the fund currency. Multifonds DB Column is FLG_TPARTS_CCY. |
| 68 | `FS.GA.SHARECLASS.DESCRIPTIONS` | `FsGaShareclass_Descriptions` | TField |  | The fund description is a 40 character alphanumeric field. The fund description appears on all Multifonds reports. Multifonds DB Column is DESCRIPTION. |
| 69 | `FS.GA.SHARECLASS.FREEZE.NAV` | `FsGaShareclass_FreezeNav` | TField |  | It is the benchmark if exceeded by the Current NAV will be used for Dividend. The difference between the Current NAV/unit and predefined Freezed NAV/unit will be calculated as Dividend declared/unit Multifonds DB Column is FREEZE_NAV. |
| 70 | `FS.GA.SHARECLASS.DDT.INDIVIDUAL.AND.HUF` | `FsGaShareclass_DdtIndividualAndHuf` | TField |  | The DDT percentage for Individual Investor units Multifonds DB Column is DDT_IND_HUF. |
| 71 | `FS.GA.SHARECLASS.DDT.OTHERS` | `FsGaShareclass_DdtOthers` | TField |  | The DDT percentage Rate for Other Investor units Multifonds DB Column is DDT_OTH. |
| 72 | `FS.GA.SHARECLASS.PUBLISHED.TG` | `FsGaShareclass_PublishedTg` | TField |  | Published TG Multifonds DB Column is PUB_TG. |
| 73 | `FS.GA.SHARECLASS.EXPENSE.RATIO` | `FsGaShareclass_ExpenseRatio` | TField |  | Expense Ratio Multifonds DB Column is EXPENSE_RATIO. |
| 74 | `FS.GA.SHARECLASS.TOTAL.EXPENSE.RATIO` | `FsGaShareclass_TotalExpenseRatio` | TField |  | Total Expense Ratio Multifonds DB Column is TER. |
| 75 | `FS.GA.SHARECLASS.RESERVED10` | `FsGaShareclass_Reserved10` | TField |  |  |
| 76 | `FS.GA.SHARECLASS.RESERVED9` | `FsGaShareclass_Reserved9` | TField |  |  |
| 77 | `FS.GA.SHARECLASS.RESERVED8` | `FsGaShareclass_Reserved8` | TField |  |  |
| 78 | `FS.GA.SHARECLASS.RESERVED7` | `FsGaShareclass_Reserved7` | TField |  |  |
| 79 | `FS.GA.SHARECLASS.RESERVED6` | `FsGaShareclass_Reserved6` | TField |  |  |
| 80 | `FS.GA.SHARECLASS.RESERVED5` | `FsGaShareclass_Reserved5` | TField |  |  |
| 81 | `FS.GA.SHARECLASS.RESERVED4` | `FsGaShareclass_Reserved4` | TField |  |  |
| 82 | `FS.GA.SHARECLASS.RESERVED3` | `FsGaShareclass_Reserved3` | TField |  |  |
| 83 | `FS.GA.SHARECLASS.RESERVED2` | `FsGaShareclass_Reserved2` | TField |  |  |
| 84 | `FS.GA.SHARECLASS.RESERVED1` | `FsGaShareclass_Reserved1` | TField |  |  |
| 85 | `FS.GA.SHARECLASS.LOCAL.REF` | `FsGaShareclass_LocalRef` |  |  |  |
| 86 | `FS.GA.SHARECLASS.OVERRIDE` | `FsGaShareclass_Override` |  |  |  |
| 87 | `FS.GA.SHARECLASS.RECORD.STATUS` | `FsGaShareclass_RecordStatus` | String |  |  |
| 88 | `FS.GA.SHARECLASS.CURR.NO` | `FsGaShareclass_CurrNo` | String |  |  |
| 89 | `FS.GA.SHARECLASS.INPUTTER` | `FsGaShareclass_Inputter` |  |  |  |
| 90 | `FS.GA.SHARECLASS.DATE.TIME` | `FsGaShareclass_DateTime` |  |  |  |
| 91 | `FS.GA.SHARECLASS.AUTHORISER` | `FsGaShareclass_Authoriser` | String |  |  |
| 92 | `FS.GA.SHARECLASS.CO.CODE` | `FsGaShareclass_CoCode` | String |  |  |
| 93 | `FS.GA.SHARECLASS.DEPT.CODE` | `FsGaShareclass_DeptCode` | String |  |  |
| 94 | `FS.GA.SHARECLASS.AUDITOR.CODE` | `FsGaShareclass_AuditorCode` | String |  |  |
| 95 | `FS.GA.SHARECLASS.AUDIT.DATE.TIME` | `FsGaShareclass_AuditDateTime` | String |  |  |
