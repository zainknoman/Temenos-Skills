# FS.GI.FUND.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.MASTER` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.MASTER.PARENT.REF.ID` | `FsGiFundMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.MASTER.ORA.ROWID` | `FsGiFundMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.MASTER.FUND.ID` | `FsGiFundMaster_FundId` | TField |  | Fund internal ID Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.MASTER.NAME` | `FsGiFundMaster_Name` | TField |  | Name of the Fund. Multifonds DB Column is XLIBELLE. |
| 5 | `FS.GI.FUND.MASTER.USE.TYPE` | `FsGiFundMaster_UseType` | TField |  | Fund status code. Multifonds DB Column is TYPE_USE. |
| 6 | `FS.GI.FUND.MASTER.LINKED.MASTER.FUND.ID` | `FsGiFundMaster_LinkedMasterFundId` | TField |  | Linked Master fund ID. Multifonds DB Column is MASTER_PTF. |
| 7 | `FS.GI.FUND.MASTER.CURRENCY` | `FsGiFundMaster_Currency` | TField |  | Fund reference currency (in 3 letter ISO format eg &apos;USD&apos;). Currency in which all accounting records are kept and in which valuations are reported. Multifonds DB Column is CMONREF. |
| 8 | `FS.GI.FUND.MASTER.EXCHANGE.GROUP` | `FsGiFundMaster_ExchangeGroup` | TField |  | The exchange rate group code used for the cash flow forecast report at the simulation level, fund exchange forex and for the swift EOD level. Multifonds DB Column is CGROUPE_COURS. |
| 9 | `FS.GI.FUND.MASTER.DOMICILE` | `FsGiFundMaster_Domicile` | TField |  | Fund domicile country code (2 letter country code: Eg. US). Multifonds DB Column is CDOMICI. |
| 10 | `FS.GI.FUND.MASTER.FISCAL.YEAR.START.DATE` | `FsGiFundMaster_FiscalYearStartDate` | TField |  | Start date of the Fiscal year Multifonds DB Column is DDEBUT_EXERCICE. |
| 11 | `FS.GI.FUND.MASTER.FISCAL.YEAR.END.DATE` | `FsGiFundMaster_FiscalYearEndDate` | TField |  | End date of the Fiscal year Multifonds DB Column is DFIN_EXERCICE. |
| 12 | `FS.GI.FUND.MASTER.MANAGEMENT.TYPE` | `FsGiFundMaster_ManagementType` | TField |  | Management type code which defines the nature of the fund. Multifonds DB Column is CGENGEST. |
| 13 | `FS.GI.FUND.MASTER.VALUATION.METHOD` | `FsGiFundMaster_ValuationMethod` | TField |  | Valuation Method code of the fund-allows the Dual Pricing functionality to be activated. Multifonds DB Column is FCYELD. |
| 14 | `FS.GI.FUND.MASTER.TIME.ZONE.CUT.OFF` | `FsGiFundMaster_TimeZoneCutOff` | TField |  | Time Zone Cut off (hh:mm) of the fund. Multifonds DB Column is TZCTOFF. |
| 15 | `FS.GI.FUND.MASTER.TIME.ZONE` | `FsGiFundMaster_TimeZone` | TField |  | Time Zone country information. Multifonds DB Column is TZONE. |
| 16 | `FS.GI.FUND.MASTER.INITIAL.DATE` | `FsGiFundMaster_InitialDate` | TField |  | The first date when the fund calculates the NAV. Multifonds DB Column is DT_BASE_CALC. |
| 17 | `FS.GI.FUND.MASTER.FREQUENCY` | `FsGiFundMaster_Frequency` | TField |  | The frequency code for the NAV calculation. Multifonds DB Column is CFREQ. |
| 18 | `FS.GI.FUND.MASTER.USE.FIXED.FUND.CALENDAR.FLAG` | `FsGiFundMaster_UseFixedFundCalendarFlag` | TField |  | Flag allows to use fixed Fund Calendar. Multifonds DB Column is FLG_FUND_CAL. |
| 19 | `FS.GI.FUND.MASTER.NUMBER.OF.DAYS.TO.CALCULAE` | `FsGiFundMaster_NumberOfDaysToCalculae` | TField | Yes | The number of days to add to the initial date for NAV date calculation. The field is mandatory if the frequency code is &apos;0009&apos;(+ number fixed days) Multifonds DB Column is NB_FIX_JOUR. |
| 20 | `FS.GI.FUND.MASTER.DAY.NUMBER.IN.WEEK` | `FsGiFundMaster_DayNumberInWeek` | TField |  | The day number in a week. Multifonds DB Column is NUM_JOUR. |
| 21 | `FS.GI.FUND.MASTER.WEEK.NUMBER` | `FsGiFundMaster_WeekNumber` | TField |  | The week number Multifonds DB Column is NUM_SEM. |
| 22 | `FS.GI.FUND.MASTER.HOLIDAY.COUNTRY.CODE` | `FsGiFundMaster_HolidayCountryCode` | TField |  | The country code(in 2 letter for,at eg. &apos;LU&apos;) for legal holiday application . Multifonds DB Column is CD_PAYS_NPTF. |
| 23 | `FS.GI.FUND.MASTER.APPLICATION.COUNTRY.CODE` | `FsGiFundMaster_ApplicationCountryCode` | TField |  | The country code (in 2 letter format eg. &apos;LU&apos;) of the application country linked to MF fund. Multifonds DB Column is CD_PAYS_APPL. |
| 24 | `FS.GI.FUND.MASTER.TYPE.OF.DATE` | `FsGiFundMaster_TypeOfDate` | TField |  | Type of date code for NAV calculation. Multifonds DB Column is CTR_DATE. |
| 25 | `FS.GI.FUND.MASTER.DELAY.DAYS` | `FsGiFundMaster_DelayDays` | TField |  | Delay days to be taken into account when calculating the revised trade date Multifonds DB Column is DELAY_DAYS. |
| 26 | `FS.GI.FUND.MASTER.CUT.OFF.WORKING.DAYS.FLAG` | `FsGiFundMaster_CutOffWorkingDaysFlag` | TField |  | Flag allows to consider 5 days a week while applying cut-off time. Multifonds DB Column is FLG_CUT_OFF_WRK. |
| 27 | `FS.GI.FUND.MASTER.TYPE.OF.DAYS` | `FsGiFundMaster_TypeOfDays` | TField |  | Type of day code that will impact the delay days and settlement days while calculating the Trade date and Value date for an order. Multifonds DB Column is TYPE_DAYS. |
| 28 | `FS.GI.FUND.MASTER.HOLIDAY.INCL.FOR.TD.FLAG` | `FsGiFundMaster_HolidayInclForTdFlag` | TField |  | Flag allows to consider the hoilday for trade date calculation. Multifonds DB Column is FLG_HOL_RD. |
| 29 | `FS.GI.FUND.MASTER.PROSPECTUS.CUTOFF` | `FsGiFundMaster_ProspectusCutoff` | TField |  | The prospectus cut-off (hh:mm) time Multifonds DB Column is PROSPECTUS_CUT_OFF. |
| 30 | `FS.GI.FUND.MASTER.PRICE.DATE` | `FsGiFundMaster_PriceDate` | TField |  | The number of days to be added to Trade date to arrive at the price reception date to calculate the trade date and the value date of the switch transaction. Multifonds DB Column is PRICE_DATE. |
| 31 | `FS.GI.FUND.MASTER.PRICE.RECEPTION.TIME` | `FsGiFundMaster_PriceReceptionTime` | TField |  | The Price reception time (hh:mm). If the Price date (T+...) is filled in and the Price reception time (hh:mm) field is left blank, the system will consider that the price reception time is 23:59 Multifonds DB Column is PRICE_RECEIPTION_TIME. |
| 32 | `FS.GI.FUND.MASTER.CUT.OFF.DELAY.DAYS.COUN.FLAG` | `FsGiFundMaster_CutOffDelayDaysCounFlag` | TField |  | Flag allows to include country holidays for cut-off and delay days calculation. Multifonds DB Column is FLG_DELCUT_COUNTRY. |
| 33 | `FS.GI.FUND.MASTER.AUTO.FIFO` | `FsGiFundMaster_AutoFifo` | TField |  | Auto FIFO of the fund. Multifonds DB Column is AUTO_HIFO. |
| 34 | `FS.GI.FUND.MASTER.ACCOUNTING.METHOD` | `FsGiFundMaster_AccountingMethod` | TField |  | The accounting method used for the fund. Average method should be used for a fund under the EUSD regulations. Multifonds DB Column is CPT_METHOD. |
| 35 | `FS.GI.FUND.MASTER.CUT.OFF.TIME` | `FsGiFundMaster_CutOffTime` | TField |  | The fund cut-off time(hh:mm) which will apply on all sub-funds linked to the selected MF fund except if exceptions are defined. Multifonds DB Column is CUT_OFF. |
| 36 | `FS.GI.FUND.MASTER.ACCOUNTING.DATE.TA` | `FsGiFundMaster_AccountingDateTa` | TField |  | The accounting date of TA used for calculation of fund accounting date Multifonds DB Column is DCTA_TA. |
| 37 | `FS.GI.FUND.MASTER.FORECAST.TA.CODE` | `FsGiFundMaster_ForecastTaCode` | TField |  | The cash flow forecast report specifications at the simulation level. Multifonds DB Column is FORECAST. |
| 38 | `FS.GI.FUND.MASTER.CTV.CREDIT.AMOUNT` | `FsGiFundMaster_CtvCreditAmount` | TField |  | The amount of credit limit defined as to Control on Transaction Volume Multifonds DB Column is AMT_IN. |
| 39 | `FS.GI.FUND.MASTER.CTV.DEBIT.AMOUNT` | `FsGiFundMaster_CtvDebitAmount` | TField |  | The amount of debit limit defined as to Control on Transaction Volume Multifonds DB Column is AMT_OUT. |
| 40 | `FS.GI.FUND.MASTER.CTV.NETTING.AMOUNT` | `FsGiFundMaster_CtvNettingAmount` | TField |  | The netting amount limit defined as to Control on Transaction Volume Multifonds DB Column is AMT_NET. |
| 41 | `FS.GI.FUND.MASTER.USE.SIMULATION.CALENDAR.FLAG` | `FsGiFundMaster_UseSimulationCalendarFlag` | TField |  | Flag allows to consider &apos;Simulation calendar&apos; definition for trade date and simulation date calcuation. Multifonds DB Column is FLG_SIM_CAL. |
| 42 | `FS.GI.FUND.MASTER.BUSINESS.EVENT.CTL.SIM.FLAG` | `FsGiFundMaster_BusinessEventCtlSimFlag` | TField |  | Business Event Control Simulation Flag Multifonds DB Column is FLG_BUSINESS_CTL. |
| 43 | `FS.GI.FUND.MASTER.SIMULATION.CUT.OFF.TIME` | `FsGiFundMaster_SimulationCutOffTime` | TField |  | It specifies the Time before which the simulation has to be done on a valid simulation date. Multifonds DB Column is SIM_CUT_OFF. |
| 44 | `FS.GI.FUND.MASTER.THRESHOLD.AMOUNT` | `FsGiFundMaster_ThresholdAmount` | TField |  | Threshold amount for ADL and SSP calculation. Multifonds DB Column is THRESHOLD_AMT. |
| 45 | `FS.GI.FUND.MASTER.THRESHOLD.CURRENCY` | `FsGiFundMaster_ThresholdCurrency` | TField |  | Threshold currency (in 3 letter ISO format eg: &apos;USD&apos;). Multifonds DB Column is THRESHOLD_CCY. |
| 46 | `FS.GI.FUND.MASTER.CTV.REPORT.CURRENCY` | `FsGiFundMaster_CtvReportCurrency` | TField |  | The currency code (in 3 letter ISO format eg. USD) in which the variation will be displayed apart from the MF fund ccy (default functionality). Multifonds DB Column is CTV_REPORT_CCY. |
| 47 | `FS.GI.FUND.MASTER.MANUAL.GRACE.PERIOD` | `FsGiFundMaster_ManualGracePeriod` | TField |  | The delay (positive or negative) time for orders entered manually in the system. Multifonds DB Column is MANUAL_GRACE. |
| 48 | `FS.GI.FUND.MASTER.DFLT.TO.CBO.FOR.TRAN.FLAG` | `FsGiFundMaster_DfltToCboForTranFlag` | TField |  | Master Fund Crystallization on transfer flag Multifonds DB Column is FLG_TRANSFER_NET. |
| 49 | `FS.GI.FUND.MASTER.LOCKUP.METHOD` | `FsGiFundMaster_LockupMethod` | TField |  | It specifies if the lockup applies to Redemptions, Switches, or both. Multifonds DB Column is LOCKUP_MTHD. |
| 50 | `FS.GI.FUND.MASTER.LOCKUP.DURATION` | `FsGiFundMaster_LockupDuration` | TField |  | The number of days in the lockup period. Multifonds DB Column is LOCKUP_DURATION. |
| 51 | `FS.GI.FUND.MASTER.LOCKUP.SOFT.WARNING.FLAG` | `FsGiFundMaster_LockupSoftWarningFlag` | TField |  | Flag enables &apos;soft&apos; warning if a debit transaction covered by the lockup method is attempted in the lockup period. Multifonds DB Column is FLG_SOFT_WARNING. |
| 52 | `FS.GI.FUND.MASTER.LOCKUP.REG.INCEPTION.FLAG` | `FsGiFundMaster_LockupRegInceptionFlag` | TField |  | Flag allows checking lock up period based on the trade date of the order or based on each credit contract&apos;s trade date for partnership funds. Multifonds DB Column is FLG_REG_INCEPTION. |
| 53 | `FS.GI.FUND.MASTER.FUND.TRADING.DESK` | `FsGiFundMaster_FundTradingDesk` | TField |  | The Fund trading desk code. Multifonds DB Column is FUND_TDSK. |
| 54 | `FS.GI.FUND.MASTER.FUND.TRADING.DESK.MODEL` | `FsGiFundMaster_FundTradingDeskModel` | TField |  | The Fund trading desk model. Multifonds DB Column is FUND_TDSK_MODEL. |
| 55 | `FS.GI.FUND.MASTER.DIV.FUND.TRADING.DESK` | `FsGiFundMaster_DivFundTradingDesk` | TField |  | The dividend fund trading desk code. Multifonds DB Column is DIV_FUND_TDSK. |
| 56 | `FS.GI.FUND.MASTER.FUND.FX.VALUE.DATE` | `FsGiFundMaster_FundFxValueDate` | TField |  | Fund FX Value Date Code Multifonds DB Column is FUND_FX_VAL_DT. |
| 57 | `FS.GI.FUND.MASTER.SOFT.THRESHOLD.FLAG` | `FsGiFundMaster_SoftThresholdFlag` | TField |  | Flag allows to enable ADL fees calculation on the total amount of Net In/Outflow. Multifonds DB Column is FLG_SFT_THRHLD. |
| 58 | `FS.GI.FUND.MASTER.TNA.THRESHOLD.PERCENTAGE` | `FsGiFundMaster_TnaThresholdPercentage` | TField |  | TNA threshold percentage Multifonds DB Column is PCT_TNA_THRESHOLD. |
| 59 | `FS.GI.FUND.MASTER.NAV.DECIMALS` | `FsGiFundMaster_NavDecimals` | TField |  | The number of decimals used in the Share Price definition - up to 6 decimals. Multifonds DB Column is CODE_ARRONDI. |
| 60 | `FS.GI.FUND.MASTER.QUANTITY.DECIMALS` | `FsGiFundMaster_QuantityDecimals` | TField |  | Number of decimal places in the client share quantity calculation. Multifonds DB Column is CODE_ARRONDI_QT. |
| 61 | `FS.GI.FUND.MASTER.DEPOSITARY.BANK.ID` | `FsGiFundMaster_DepositaryBankId` | TField |  | The default Depository Bank ID linked to the fund Multifonds DB Column is NRACINE. |
| 62 | `FS.GI.FUND.MASTER.CASH.FLOW.ID` | `FsGiFundMaster_CashFlowId` | TField |  | Cash Flow ID code linked to Master Fund. Multifonds DB Column is CASH_FLOW_ID. |
| 63 | `FS.GI.FUND.MASTER.COLLECTION.ACCOUNT.GROUP` | `FsGiFundMaster_CollectionAccountGroup` | TField |  | Collection Account Group code used to group deals and receipts that can be matched together. Multifonds DB Column is COLL_ACC_GRP. |
| 64 | `FS.GI.FUND.MASTER.PAYMENT.PROCESS` | `FsGiFundMaster_PaymentProcess` | TField |  | The payment process to be followed for the deals. Multifonds DB Column is PY_PROCESS. |
| 65 | `FS.GI.FUND.MASTER.GL.FLOW.ID` | `FsGiFundMaster_GlFlowId` | TField |  | General Ledger Flow ID code linked to Master Fund. Multifonds DB Column is GL_FLOW_ID. |
| 66 | `FS.GI.FUND.MASTER.GL.ACCOUNT.GROUP.ID` | `FsGiFundMaster_GlAccountGroupId` | TField |  | General Ledger account group ID Multifonds DB Column is GL_ACCT_GROUP_ID. |
| 67 | `FS.GI.FUND.MASTER.EXEMPT.STATUS.REVIEW.DATE` | `FsGiFundMaster_ExemptStatusReviewDate` | TField |  | It specifies the date when the US Tax exemption was provided if the &apos;US Tax&apos; is set as &apos;N&apos;. Multifonds DB Column is EXMT_STATUS_DATE. |
| 68 | `FS.GI.FUND.MASTER.FATCA.STATUS` | `FsGiFundMaster_FatcaStatus` | TField |  | FATCA status code. Multifonds DB Column is FAT_STATUS. |
| 69 | `FS.GI.FUND.MASTER.GIIN.NUMBER` | `FsGiFundMaster_GiinNumber` | TField |  | GIIN identification number. Each registering FI will be given a FATCA ID that will be used for purposes of establishing and accessing the FI&apos;s online FATCA account. Multifonds DB Column is FAT_GIIN. |
| 70 | `FS.GI.FUND.MASTER.FATCA.EFFECTIVE.DATE` | `FsGiFundMaster_FatcaEffectiveDate` | TField |  | FATCA effective date Multifonds DB Column is FAT_DEFFECTIVE. |
| 71 | `FS.GI.FUND.MASTER.FATCA.EXPIRY.DATE` | `FsGiFundMaster_FatcaExpiryDate` | TField |  | FATCA expiry date Multifonds DB Column is FAT_DEXPIRY. |
| 72 | `FS.GI.FUND.MASTER.FATCA.REVOKE.DATE` | `FsGiFundMaster_FatcaRevokeDate` | TField |  | FATCA revoke date Multifonds DB Column is FAT_DREVOKE. |
| 73 | `FS.GI.FUND.MASTER.FATCA.EXEMPTION.REASON` | `FsGiFundMaster_FatcaExemptionReason` | TField |  | FATCA exempt reason code. Multifonds DB Column is FAT_EXEM_REASON. |
| 74 | `FS.GI.FUND.MASTER.SWUNG.FA.FLAG` | `FsGiFundMaster_SwungFaFlag` | TField |  | Redemption gating Multifonds DB Column is FLG_SWUNG_FA. |
| 75 | `FS.GI.FUND.MASTER.FATCA.MODEL` | `FsGiFundMaster_FatcaModel` | TField |  | It specifies the IGA model code. Multifonds DB Column is FAT_MODEL. |
| 76 | `FS.GI.FUND.MASTER.OPAQUE.SSP.FLAG` | `FsGiFundMaster_OpaqueSspFlag` | TField |  | flag allows defining the Opaque SSP for the selected fund. Multifonds DB Column is FLG_OPAQUE_SSP. |
| 77 | `FS.GI.FUND.MASTER.SPONSORING.ENTITY.ID` | `FsGiFundMaster_SponsoringEntityId` | TField |  | Central Register ID having &apos;Type&apos; as &apos;SE&apos;, can be specified as Sponsoring Entity External ID. Multifonds DB Column is FAT_SPONSOR. |
| 78 | `FS.GI.FUND.MASTER.AIFMD.REPORTING` | `FsGiFundMaster_AifmdReporting` | TField |  | Flag allows to enable AIFMD reporting for the fund. Multifonds DB Column is FLG_AIFMD_REPORTING. |
| 79 | `FS.GI.FUND.MASTER.AIFMD.REPORTING.FREQUENCY` | `FsGiFundMaster_AifmdReportingFrequency` | TField |  | The frequency of the AIFMD reporting. Multifonds DB Column is AIFMD_REPORTING_FREQ. |
| 80 | `FS.GI.FUND.MASTER.AIFMD.AUTHORIZATION.DATE` | `FsGiFundMaster_AifmdAuthorizationDate` | TField |  | Date of authorization of central register type called a AI a Alternative Investment Fund Managera Multifonds DB Column is AIFMD_AUTHORIZATION_DATE. |
| 81 | `FS.GI.FUND.MASTER.AUTHORIZED.AIFM` | `FsGiFundMaster_AuthorizedAifm` | TField |  | The authorized AIFMD ID (Central Register with &quot;Type&quot; - a AI a Alternative Investment Fund Managera ) Multifonds DB Column is AUTHORIZED_AIFM. |
| 82 | `FS.GI.FUND.MASTER.AIFMD.TEXT` | `FsGiFundMaster_AifmdText` | TField |  | Free text field that allows upto 1000 alpha numerical characters for AIFMD related information Multifonds DB Column is AIFMD_TEXT. |
| 83 | `FS.GI.FUND.MASTER.CRS.STATUS` | `FsGiFundMaster_CrsStatus` | TField |  | CRS status code. Multifonds DB Column is CRS_STATUS. |
| 84 | `FS.GI.FUND.MASTER.AML.JURISDICTION` | `FsGiFundMaster_AmlJurisdiction` | TField |  | Jurisdiction code (in 2 letter format eg: &apos;US&apos;). Multifonds DB Column is JURISDICTION. |
| 85 | `FS.GI.FUND.MASTER.TAX.ID.NUMBER` | `FsGiFundMaster_TaxIdNumber` | TField |  | Tax ID for FATCA process. Multifonds DB Column is TIN_NUMBER. |
| 86 | `FS.GI.FUND.MASTER.MONEY.MARKET.FUND.FLAG` | `FsGiFundMaster_MoneyMarketFundFlag` | TField |  | Manual gating Multifonds DB Column is FLG_MONEY_MRKT_FUND. |
| 87 | `FS.GI.FUND.MASTER.DAYS.FROM.VALUATION.DATE` | `FsGiFundMaster_DaysFromValuationDate` | TField |  | The number of days between the valuation date and the NAV date for NAV reception through interface Multifonds DB Column is NVALUATION. |
| 88 | `FS.GI.FUND.MASTER.MANUAL.GATING.FLAG` | `FsGiFundMaster_ManualGatingFlag` | TField |  | Box decision Multifonds DB Column is FLG_MANUAL_GATING. |
| 89 | `FS.GI.FUND.MASTER.BOX.DECISION.FLAG` | `FsGiFundMaster_BoxDecisionFlag` | TField |  | Auto Series of Sharers ID Multifonds DB Column is FLG_BOX_DECISION. |
| 90 | `FS.GI.FUND.MASTER.IMPORT.NAV.BY` | `FsGiFundMaster_ImportNavBy` | TField |  | NAV currency used for interface NAV price. Multifonds DB Column is CNAV_IMP. |
| 91 | `FS.GI.FUND.MASTER.ADL.TYPE` | `FsGiFundMaster_AdlType` | TField |  | ADL Type code. ADL type is defined per MF fund and will be applicable to all TA funds linked to this MF fund Multifonds DB Column is FLG_ADL_DEALING. |
| 92 | `FS.GI.FUND.MASTER.THRESHOLD.TYPE` | `FsGiFundMaster_ThresholdType` | TField |  | It specifies the method for the purpose of ADL threshold calculation. Multifonds DB Column is ADL_TYPE. |
| 93 | `FS.GI.FUND.MASTER.THRESHOLD.NAV.PERCENTAGE` | `FsGiFundMaster_ThresholdNavPercentage` | TField |  | The Threshold NAV percentage based on which the threshold amount will be calculated. Multifonds DB Column is ADL_PCT. |
| 94 | `FS.GI.FUND.MASTER.PERFORMANCE.FEE.CODE` | `FsGiFundMaster_PerformanceFeeCode` | TField |  | The fund performance fee code. Multifonds DB Column is CPERFOR_FEE. |
| 95 | `FS.GI.FUND.MASTER.PERF.PERIOD.START.DATE` | `FsGiFundMaster_PerfPeriodStartDate` | TField |  | Master Fund Performance Fees crystallization period end date Multifonds DB Column is DPERFOR_START. |
| 96 | `FS.GI.FUND.MASTER.PERFORMANCE.PERIOD.END.DATE` | `FsGiFundMaster_PerformancePeriodEndDate` | TField |  | Master Fund Performance Fees crystallization period start date Multifonds DB Column is DPERFOR_END. |
| 97 | `FS.GI.FUND.MASTER.IRISH.TAX.FLAG` | `FsGiFundMaster_IrishTaxFlag` | TField |  | Flag to enable Irish Tax functionality. Multifonds DB Column is CGT_DEDUCTION. |
| 98 | `FS.GI.FUND.MASTER.CRYST.FREQUENCY` | `FsGiFundMaster_CrystFrequency` | TField |  | Crystallization Multifonds DB Column is CRYST_CFREQ. |
| 99 | `FS.GI.FUND.MASTER.CRYTS.DATE.ADJ.TYPE` | `FsGiFundMaster_CrytsDateAdjType` | TField |  | Crystallization frequency Multifonds DB Column is CRYST_DATE_ADJ_TYPE. |
| 100 | `FS.GI.FUND.MASTER.DEBIT.ADJ.PER.LOT.FLAG` | `FsGiFundMaster_DebitAdjPerLotFlag` | TField |  | Flag allows to issue one debit adjustment per linked credit contract, instead of providing only one bulk debit adjustment. Multifonds DB Column is FLG_DR_ADJ_LOT. |
| 101 | `FS.GI.FUND.MASTER.US.TAX.FLAG` | `FsGiFundMaster_UsTaxFlag` | TField |  | Flag allows to enable US Tax functionality. Multifonds DB Column is FLG_USTAX. |
| 102 | `FS.GI.FUND.MASTER.US.TAX.EFFECTIVE.DATE` | `FsGiFundMaster_UsTaxEffectiveDate` | TField |  | The date in which the US tax comes into force Multifonds DB Column is USTAX_DATE. |
| 103 | `FS.GI.FUND.MASTER.AUTO.SS.ID.FLAG` | `FsGiFundMaster_AutoSsIdFlag` | TField |  | Crystallization adjustment date Multifonds DB Column is FLG_AUTO_SS_ID. |
| 104 | `FS.GI.FUND.MASTER.SWEDISH.TAX.FLAG` | `FsGiFundMaster_SwedishTaxFlag` | TField |  | It specifies if Swedish tax calculation is applicable for the register. Multifonds DB Column is FLG_SWEDISH_TAX. |
| 105 | `FS.GI.FUND.MASTER.EXCEPTIONAL.PF.PARAMETER` | `FsGiFundMaster_ExceptionalPfParameter` | TField |  | The number of decimal to be considered for the performance fee calculation and hurdle management. Multifonds DB Column is PF_EXCEPT. |
| 106 | `FS.GI.FUND.MASTER.INCOME.ALLOCATION.METHOD` | `FsGiFundMaster_IncomeAllocationMethod` | TField |  | The general accounting method for partnerships. The field is applicable for partnership funds (Management type = &quot;PART&quot;). Multifonds DB Column is INC_ALLOC_METHOD. |
| 107 | `FS.GI.FUND.MASTER.BREAK.PERIOD.DATE.TYPE` | `FsGiFundMaster_BreakPeriodDateType` | TField |  | Break Period date type code Multifonds DB Column is BP_TYPE. |
| 108 | `FS.GI.FUND.MASTER.MONTH.END.DATE.TYPE` | `FsGiFundMaster_MonthEndDateType` | TField |  | The month end type code to apply for NAV date calculation if the month end falls on a week end or holiday. Multifonds DB Column is CTR_DATE_MONTHEND. |
| 109 | `FS.GI.FUND.MASTER.SERIES.PRICE.LEAD.SHARES.FLAG` | `FsGiFundMaster_SeriesPriceLeadSharesFlag` | TField |  | Flag allows to calculate the series prices from the lead series. If the flag is &apos;N&apos;, the series share prices needs to be manually recorded. Multifonds DB Column is FLG_TPART_LEAD. |
| 110 | `FS.GI.FUND.MASTER.FIFO.BY.TRADE.DATE.FLAG` | `FsGiFundMaster_FifoByTradeDateFlag` | TField |  | FIFO Trade Date Flag Multifonds DB Column is FLG_FIFO_TRADE_DATE. |
| 111 | `FS.GI.FUND.MASTER.TAX.LOTS.FLAG` | `FsGiFundMaster_TaxLotsFlag` | TField |  | It specifies if the tax lot calculated or not. Multifonds DB Column is FLG_TAX_LOTS. |
| 112 | `FS.GI.FUND.MASTER.DEPRECIATION.DEPOSIT.FLAG` | `FsGiFundMaster_DepreciationDepositFlag` | TField |  | Flag allows to calculate performance fees based on the a Depreciation deposita method. Multifonds DB Column is FLG_PF_DD. |
| 113 | `FS.GI.FUND.MASTER.RED.GATING.FLAG` | `FsGiFundMaster_RedGatingFlag` | TField |  | Opaque SSP Multifonds DB Column is FLG_RED_GATE. |
| 114 | `FS.GI.FUND.MASTER.SPLIT.INCOME.CAP.MF` | `FsGiFundMaster_SplitIncomeCapMf` | TField |  | Split Income Cap Mf Internal Fixed Value Multifonds DB Column is CINCOME_FLG. |
| 115 | `FS.GI.FUND.MASTER.ACCOUNTING.CHART` | `FsGiFundMaster_AccountingChart` | TField |  | The reference number of the master fund accounting chart of accounts . Multifonds DB Column is CPDC. |
| 116 | `FS.GI.FUND.MASTER.SAVINGS.DIRECTIVE.CODE` | `FsGiFundMaster_SavingsDirectiveCode` | TField |  | To define if the fund is out of scope, in scope for redemption, dividend or for both for the EUSD. Multifonds DB Column is CSAV_DIRECTIVE. |
| 117 | `FS.GI.FUND.MASTER.TYPE.COMM.MF` | `FsGiFundMaster_TypeCommMf` | TField |  | Type Comm Mf Internal Fixed Value Multifonds DB Column is CTYPE_COMM. |
| 118 | `FS.GI.FUND.MASTER.FX.ADJUSTMENT` | `FsGiFundMaster_FxAdjustment` | TField |  | It specifies how the cambio positions should be managed. Multifonds DB Column is EXCH_ADJ. |
| 119 | `FS.GI.FUND.MASTER.SETTLEMENT.METHOD` | `FsGiFundMaster_SettlementMethod` | TField |  | The master fund settlement method. Multifonds DB Column is FCPT_VAL. |
| 120 | `FS.GI.FUND.MASTER.TYPE.OF.STATISTICS` | `FsGiFundMaster_TypeOfStatistics` | TField |  | The report code for Specific country reports. Multifonds DB Column is IML. |
| 121 | `FS.GI.FUND.MASTER.NECRITUR.MF` | `FsGiFundMaster_NecriturMf` | TField |  | NECRITUR Mf Internal Fixed Value Multifonds DB Column is NECRITUR_PTF. |
| 122 | `FS.GI.FUND.MASTER.VALUATION.MODEL` | `FsGiFundMaster_ValuationModel` | TField |  | The default valuation model cdoe. Multifonds DB Column is NESTI. |
| 123 | `FS.GI.FUND.MASTER.VALUATION.CCLUX.MF` | `FsGiFundMaster_ValuationCcluxMf` | TField |  | Valuation Model CC Lux MF Internal Fixed Value Multifonds DB Column is NESTI_CCLUX. |
| 124 | `FS.GI.FUND.MASTER.TYPE.AARR.AMOUNT` | `FsGiFundMaster_TypeAarrAmount` | TField |  | Type AR Amount MF Internal Fixed Value Multifonds DB Column is TYP_AARR_MNT. |
| 125 | `FS.GI.FUND.MASTER.LONG.NAME` | `FsGiFundMaster_LongName` | TField |  | Fund long name Multifonds DB Column is LONG_NAME. |
| 126 | `FS.GI.FUND.MASTER.EXTERNAL.ID` | `FsGiFundMaster_ExternalId` | TField |  | External Id of the fund. Multifonds DB Column is NPTF_EXTERN. |
| 127 | `FS.GI.FUND.MASTER.INACTIVATION.DATE` | `FsGiFundMaster_InactivationDate` | TField |  | Inactivation date Multifonds DB Column is DATE_INACTIVE. |
| 128 | `FS.GI.FUND.MASTER.TFC.ID` | `FsGiFundMaster_TfcId` | TField |  | TFC external ID linked to the TA fund Multifonds DB Column is NTFC. |
| 129 | `FS.GI.FUND.MASTER.LEGAL.ENTITY.EXTERNAL.ID` | `FsGiFundMaster_LegalEntityExternalId` | TField |  | TFC external ID linked to the fund Multifonds DB Column is NTFC_EXTERN. |
| 130 | `FS.GI.FUND.MASTER.FUND.TYPE` | `FsGiFundMaster_FundType` | TField |  | The type of fund code. Multifonds DB Column is NPTF_TYPE. |
| 131 | `FS.GI.FUND.MASTER.OPENING.DATE` | `FsGiFundMaster_OpeningDate` | TField |  | TA fund first authorized business date Multifonds DB Column is OPEN_DATE. |
| 132 | `FS.GI.FUND.MASTER.CLOSING.DATE` | `FsGiFundMaster_ClosingDate` | TField |  | The TA fund last business date before set to inactive Multifonds DB Column is CLOSING_DATE. |
| 133 | `FS.GI.FUND.MASTER.FUND.CATEGORY` | `FsGiFundMaster_FundCategory` | TField |  | The fund category code. Multifonds DB Column is CATEGORY_ID. |
| 134 | `FS.GI.FUND.MASTER.AGENT.ID` | `FsGiFundMaster_AgentId` | TField |  | Agent External ID linked to the TA Fund Multifonds DB Column is NOUTLET. |
| 135 | `FS.GI.FUND.MASTER.SECURITY.CATEGORY` | `FsGiFundMaster_SecurityCategory` | TField |  | Security category code. Multifonds DB Column is SEC_TYPE. |
| 136 | `FS.GI.FUND.MASTER.FUND.RISK.CODE` | `FsGiFundMaster_FundRiskCode` | TField |  | Fund risk code Multifonds DB Column is NPTF_RISK_CODE. |
| 137 | `FS.GI.FUND.MASTER.AUDITOR` | `FsGiFundMaster_Auditor` | TField |  | Fund Auditor name Multifonds DB Column is AUDITOR. |
| 138 | `FS.GI.FUND.MASTER.MANAGER` | `FsGiFundMaster_Manager` | TField |  | The TA Fund Manager Name. Multifonds DB Column is MANAGER. |
| 139 | `FS.GI.FUND.MASTER.CO.MANAGER` | `FsGiFundMaster_CoManager` | TField |  | TA Fund Co-Manager name Multifonds DB Column is CO_MANAGER. |
| 140 | `FS.GI.FUND.MASTER.CONTACT.PERSON` | `FsGiFundMaster_ContactPerson` | TField |  | TA Fund contact person Multifonds DB Column is CONTACT_PERSON. |
| 141 | `FS.GI.FUND.MASTER.AUDITOR.ID` | `FsGiFundMaster_AuditorId` | TField |  | Fund auditor external ID Multifonds DB Column is AUDITOR_ID. |
| 142 | `FS.GI.FUND.MASTER.ACCOUNTING.PROVIDER` | `FsGiFundMaster_AccountingProvider` | TField |  | The Account Manager of the TA fund. Multifonds DB Column is ACC_PROVIDER. |
| 143 | `FS.GI.FUND.MASTER.REGULATOR` | `FsGiFundMaster_Regulator` | TField |  | Regulator name. This field is for Information purpose. Multifonds DB Column is REGULATOR. |
| 144 | `FS.GI.FUND.MASTER.CORRESPONDANT.ID` | `FsGiFundMaster_CorrespondantId` | TField |  | External ID of Central Register created with &apos;Type&apos; as &apos;CT&apos;. Multifonds DB Column is NCORRESP. |
| 145 | `FS.GI.FUND.MASTER.MANAGEMENT.COMPANY.FLAG` | `FsGiFundMaster_ManagementCompanyFlag` | TField |  | Flag allows to report the commission amount as the management fee and is not included in the cash flow forecast. Multifonds DB Column is FLG_MGMT. |
| 146 | `FS.GI.FUND.MASTER.SINGLE.INVESTOR.ID` | `FsGiFundMaster_SingleInvestorId` | TField |  | Single Investor Id linked to the fund. Multifonds DB Column is SID. |
| 147 | `FS.GI.FUND.MASTER.DELAY.TYPE` | `FsGiFundMaster_DelayType` | TField |  | Delay type code Multifonds DB Column is DELAY_TYPE. |
| 148 | `FS.GI.FUND.MASTER.CURRENCY.CALENDAR.CODE` | `FsGiFundMaster_CurrencyCalendarCode` | TField |  | Quotation Currency Calendar linked to the TA Fund. Multifonds DB Column is CCY_INDICATOR. |
| 149 | `FS.GI.FUND.MASTER.FIRST.SUBSCRIPTION.DATE` | `FsGiFundMaster_FirstSubscriptionDate` | TField |  | The first subscription date of initial subscription period. Multifonds DB Column is STARTING_DATE. |
| 150 | `FS.GI.FUND.MASTER.LAST.SUBSCRIPTION.DATE` | `FsGiFundMaster_LastSubscriptionDate` | TField |  | The fund last subscription date of the initial subscription period. Multifonds DB Column is ENDING_DATE. |
| 151 | `FS.GI.FUND.MASTER.SUBSCRIPTION.PRICE` | `FsGiFundMaster_SubscriptionPrice` | TField |  | The Initial subscription price in fund quotation currency. This price will be applicable during the initial subscription period only. Multifonds DB Column is SUBSCRIPTION_PRICE. |
| 152 | `FS.GI.FUND.MASTER.MIN.SUBSCRIPTION.AMOUNT` | `FsGiFundMaster_MinSubscriptionAmount` | TField |  | The minimum subscription amount in quotation currency. Multifonds DB Column is MNT_MIN. |
| 153 | `FS.GI.FUND.MASTER.QUANTITY.ROUNDING.TYPE` | `FsGiFundMaster_QuantityRoundingType` | TField |  | Quantity Rounding type code. This will override the parameters defined at fund level. Multifonds DB Column is TYPE_ARRONDI. |
| 154 | `FS.GI.FUND.MASTER.VALUE.DATE.TYPE` | `FsGiFundMaster_ValueDateType` | TField |  | Value date type code which allows the user to define a fixed or minimum number of days to be taken into account . Multifonds DB Column is VALUE_DATE_TYPE. |
| 155 | `FS.GI.FUND.MASTER.REGISTER.TYPE` | `FsGiFundMaster_RegisterType` | TField |  | Register Type code. Multifonds DB Column is TYPE_REG. |
| 156 | `FS.GI.FUND.MASTER.PRICE.BASIS` | `FsGiFundMaster_PriceBasis` | TField |  | It specifies if Forward or Historic Prices is used as calculation basis. This field is for information purposes only. Multifonds DB Column is CP_BASIS. |
| 157 | `FS.GI.FUND.MASTER.ONLY.REDEMPTION.FLAG` | `FsGiFundMaster_OnlyRedemptionFlag` | TField |  | Flag enables to allow only a defined set of transactions to be placed for the fund. The flag shall be used when no new subscriptions are allowed. Multifonds DB Column is FLG_ONLY_REDEM. |
| 158 | `FS.GI.FUND.MASTER.SIGNIFICANT.FIGURES` | `FsGiFundMaster_SignificantFigures` | TField |  | The number of digits of the share price instead of a number of decimals. &apos;0&apos; on the left of the first digit greater or equal to 1 are not considered as significant figures. Multifonds DB Column is CODE_ARRONDI_SIGNIFICANT. |
| 159 | `FS.GI.FUND.MASTER.NO.AMOUNT.FLAG` | `FsGiFundMaster_NoAmountFlag` | TField |  | Flag allows to block placing any transaction in amount for the related operation code. Multifonds DB Column is FLG_NO_AMT. |
| 160 | `FS.GI.FUND.MASTER.ROUNDING.FROM.SWITCH` | `FsGiFundMaster_RoundingFromSwitch` | TField |  | The rounding rules code defined for the switch-out fund. Multifonds DB Column is CROUND_SWITCH. |
| 161 | `FS.GI.FUND.MASTER.CUT.OFF.GROUP` | `FsGiFundMaster_CutOffGroup` | TField |  | Cutoff group code linked to the fund for the cut off definition by group of agent and by group of fund. Multifonds DB Column is CUT_OFF_GRP. |
| 162 | `FS.GI.FUND.MASTER.FIRST.SUBSCRIPTION.FLAG` | `FsGiFundMaster_FirstSubscriptionFlag` | TField |  | Flag allows to enables first subscription functionality for the fund. Multifonds DB Column is FLG_FIRST_SUB. |
| 163 | `FS.GI.FUND.MASTER.LATEST.NAV.DATE` | `FsGiFundMaster_LatestNavDate` | TField |  | Latest NAV date (in DD/MM/YYYY format) Multifonds DB Column is LATEST_NAV_DATE. |
| 164 | `FS.GI.FUND.MASTER.NEXT.NAV.DATE` | `FsGiFundMaster_NextNavDate` | TField |  | Next NAV date (in DD/MM/YYYY format) Multifonds DB Column is NEXT_NAV_DATE. |
| 165 | `FS.GI.FUND.MASTER.DEAL.TYPE` | `FsGiFundMaster_DealType` | TField |  | Deal type code for Cash handling at TA Fund level. Multifonds DB Column is TYPE_DEAL. |
| 166 | `FS.GI.FUND.MASTER.MATURITY.DATE` | `FsGiFundMaster_MaturityDate` | TField |  | The maturity date of the TA fund. Multifonds DB Column is MATURITY_DATE. |
| 167 | `FS.GI.FUND.MASTER.WARNING.DATE` | `FsGiFundMaster_WarningDate` | TField |  | The cut-off date to display a warning message if a credit order is placed on and after the &apos;Warning date&apos; but before the &apos;Maturity date&apos; of the fund . Multifonds DB Column is WARNING_DATE. |
| 168 | `FS.GI.FUND.MASTER.GLOBAL.ORDERING.FLAG` | `FsGiFundMaster_GlobalOrderingFlag` | TField |  | Flag allows to enable the global ordering functionality. Multifonds DB Column is FLG_GLOBAL_ORD. |
| 169 | `FS.GI.FUND.MASTER.TRANSACTION.BULKING.NETTING` | `FsGiFundMaster_TransactionBulkingNetting` | TField |  | The grouping or Netting method code of cash movements. Multifonds DB Column is TRNS_BULK_NET. |
| 170 | `FS.GI.FUND.MASTER.CASH.DIVIDEND.REGISTER.ID` | `FsGiFundMaster_CashDividendRegisterId` | TField |  | Technical register External ID having &apos;Person type&apos; as &apos;0900-Fund&apos;, can be specified as Cash dividend register External ID. Multifonds DB Column is NREGISTER_CASH_DIV. |
| 171 | `FS.GI.FUND.MASTER.REINVESTMENT.REGISTER.ID` | `FsGiFundMaster_ReinvestmentRegisterId` | TField |  | Technical Register External ID having &apos;Person type&apos; as &apos;0900-Fund&apos;, can be specified as Reinvestment register External ID. Multifonds DB Column is NREGISTER_REINVEST. |
| 172 | `FS.GI.FUND.MASTER.DISPLAY.DB.BANK.DETAILS.FLAG` | `FsGiFundMaster_DisplayDbBankDetailsFlag` | TField |  | Flag allows to enable the bank details (for debit orders) in order level. This setup is part of &quot;Control on debit order bank details&quot; functionality. Multifonds DB Column is FLG_DB_BANK. |
| 173 | `FS.GI.FUND.MASTER.VALUE.DATE.NUMBER.OF.DAYS` | `FsGiFundMaster_ValueDateNumberOfDays` | TField |  | It specifies the number of days between trade date and value date for the fund. Multifonds DB Column is NUMBER_DAYS. |
| 174 | `FS.GI.FUND.MASTER.VALUE.DATE.METHOD` | `FsGiFundMaster_ValueDateMethod` | TField |  | Value date method code to manage the settlement date based on the holidays to consider. Multifonds DB Column is WORKING_DAY. |
| 175 | `FS.GI.FUND.MASTER.CASH.ACC.MANAGEMENT.FLAG` | `FsGiFundMaster_CashAccManagementFlag` | TField |  | Flag allows to authorise the register for the cash account functionality. . Multifonds DB Column is FLG_CASH_ACCOUNT. |
| 176 | `FS.GI.FUND.MASTER.VD.RECALC.ON.PAYMENT.FLAG` | `FsGiFundMaster_VdRecalcOnPaymentFlag` | TField |  | Flag enables to recalculate the value date based on the forced trade date entered at payment level. Multifonds DB Column is FLG_DVALEUR_RECALC. |
| 177 | `FS.GI.FUND.MASTER.PARTIAL.SETTLEMENT.PCT` | `FsGiFundMaster_PartialSettlementPct` | TField |  | The percentage of the transaction that will be paid immediately if the fund is in scope of partial settlement. Multifonds DB Column is PART_SETT_PCT. |
| 178 | `FS.GI.FUND.MASTER.RECEIPT.DUE.TIME` | `FsGiFundMaster_ReceiptDueTime` | TField |  | The receipts due time Multifonds DB Column is RECPT_DUE_TIME. |
| 179 | `FS.GI.FUND.MASTER.RECEIPT.DELAY.DAYS` | `FsGiFundMaster_ReceiptDelayDays` | TField |  | The receipts delay days Multifonds DB Column is RECPT_DELAY_DAYS. |
| 180 | `FS.GI.FUND.MASTER.CORRECTIVE.PAYMENT.FLAG` | `FsGiFundMaster_CorrectivePaymentFlag` | TField |  | Flag allows to automatically create the corrective payment for the cancellation of the orders and reversal of the contracts. Multifonds DB Column is FLG_CORR_PAY. |
| 181 | `FS.GI.FUND.MASTER.PARTIAL.PAYMENT.FLAG` | `FsGiFundMaster_PartialPaymentFlag` | TField |  | Flag allows to enable partial payment functionality for the fund. Multifonds DB Column is FLG_PART_PAY. |
| 182 | `FS.GI.FUND.MASTER.COMMISSION.CODE` | `FsGiFundMaster_CommissionCode` | TField |  | Commission Code used for commission calculation. Multifonds DB Column is CODE_COMMISSION. |
| 183 | `FS.GI.FUND.MASTER.COMMISSION.GROUP` | `FsGiFundMaster_CommissionGroup` | TField |  | Fund commission group code linked to the TA Fund . Multifonds DB Column is CGROUP. |
| 184 | `FS.GI.FUND.MASTER.COMMISSION.DISCLOSURE.CODE` | `FsGiFundMaster_CommissionDisclosureCode` | TField |  | It specifies if the split of commissions between the Management company and agents may or may not have to be disclosed on contract notes. Multifonds DB Column is COMM_DISCLOSURE. |
| 185 | `FS.GI.FUND.MASTER.TOTAL.COMMISSION.FLAG` | `FsGiFundMaster_TotalCommissionFlag` | TField |  | Flag allows defining the method applied on Total commission for the selected fund. Multifonds DB Column is FLG_TOT_COMM. |
| 186 | `FS.GI.FUND.MASTER.MAXIMUM.COMMISSION.FLAG` | `FsGiFundMaster_MaximumCommissionFlag` | TField |  | Flag allows defining the method applied on maximum commission charges for the selected fund. Multifonds DB Column is FLG_MAX_COMM. |
| 187 | `FS.GI.FUND.MASTER.ACCRUAL.MANAGEMENT` | `FsGiFundMaster_AccrualManagement` | TField |  | Accrual Management Code Multifonds DB Column is ACCRL_MGMT. |
| 188 | `FS.GI.FUND.MASTER.MIFID.STRUCTURE` | `FsGiFundMaster_MifidStructure` | TField |  | It specifies if the fund is hedged product or a standard product . Multifonds DB Column is MIFID_STR. |
| 189 | `FS.GI.FUND.MASTER.BOX.MANAGEMENT.CODE` | `FsGiFundMaster_BoxManagementCode` | TField |  | It specifies whether the fund supports the Box Management. Multifonds DB Column is CMANAGE. |
| 190 | `FS.GI.FUND.MASTER.UK.REPORTING.CODE` | `FsGiFundMaster_UkReportingCode` | TField |  | It specifies if the fund is in scope of UK reporting regime or not. Multifonds DB Column is UK_DIV_REPORT. |
| 191 | `FS.GI.FUND.MASTER.BOX.VALUE.DATE.METHOD` | `FsGiFundMaster_BoxValueDateMethod` | TField |  | The box Value date method code to manage the settlement date based on the holidays to consider. Multifonds DB Column is BOX_WORKING_DAY. |
| 192 | `FS.GI.FUND.MASTER.BOX.NUMBER.OF.DAYS` | `FsGiFundMaster_BoxNumberOfDays` | TField |  | The number of days to be added to Trade date to arrive at the settlement date. Multifonds DB Column is BOX_NUM_DAYS. |
| 193 | `FS.GI.FUND.MASTER.EQUALIZATION.CODE` | `FsGiFundMaster_EqualizationCode` | TField |  | Equalization code linked to the Fund. Multifonds DB Column is CODE_EGA. |
| 194 | `FS.GI.FUND.MASTER.STABLE.NAV` | `FsGiFundMaster_StableNav` | TField |  | The Stable NAV price. The field is used only if the fund type is 0006 - Money Market - Stable NAV Fund. Multifonds DB Column is PRICE_STABLE_NAV. |
| 195 | `FS.GI.FUND.MASTER.DAILY.DIV.CALC.TYPE` | `FsGiFundMaster_DailyDivCalcType` | TField |  | It specifies if Daily Dividend will be calculated as of Trade Date, as of Previous Trade Date or as of Value Date. Multifonds DB Column is REG_POS_CLC_METHOD. |
| 196 | `FS.GI.FUND.MASTER.DAILY.DIV.PAYMENT.TYPE` | `FsGiFundMaster_DailyDivPaymentType` | TField |  | Daily Dividend accruals payment frequency code. Multifonds DB Column is DLYDIV_PAYMTHD. |
| 197 | `FS.GI.FUND.MASTER.NO.REINVESTMENT.FLAG` | `FsGiFundMaster_NoReinvestmentFlag` | TField |  | Flag allows to block automatic reinvestment order created by the system. Multifonds DB Column is FLG_NO_REINVEST. |
| 198 | `FS.GI.FUND.MASTER.DIV.INCOME.EQUALISATION` | `FsGiFundMaster_DivIncomeEqualisation` | TField |  | The dividend income equalisation methods. Multifonds DB Column is DIV_INCOME_EQUI. |
| 199 | `FS.GI.FUND.MASTER.FOF.REGISTER.ID` | `FsGiFundMaster_FofRegisterId` | TField |  | Fund Of Fund Register External ID who will be placing the transactions for the fund of funds (If the fund type is 0020 - Fund of funds). Multifonds DB Column is FOF_NREGISTER. |
| 200 | `FS.GI.FUND.MASTER.DIV.DISTRIBUTION.OPTION` | `FsGiFundMaster_DivDistributionOption` | TField |  | It specifies if the dividend distribution will be grouped or not. Multifonds DB Column is DIVIDEND_DIST_OPTION. |
| 201 | `FS.GI.FUND.MASTER.REDEMPTION.FOR.DIV.FLAG` | `FsGiFundMaster_RedemptionForDivFlag` | TField |  | Flag allows to automatically redeem the holdings for dividend payout operation. Multifonds DB Column is FLG_AUTO_DIV. |
| 202 | `FS.GI.FUND.MASTER.CROSS.PRICING` | `FsGiFundMaster_CrossPricing` | TField |  | Flag allows to activate the cross pricing. Multifonds DB Column is FLG_CROSS_PRICE. |
| 203 | `FS.GI.FUND.MASTER.BYPASS.TOLERANCE` | `FsGiFundMaster_BypassTolerance` | TField |  | Bypass tolerance code for Cross Pricing. Multifonds DB Column is BYPASS_TOLERAN. |
| 204 | `FS.GI.FUND.MASTER.AUTO.MANUAL` | `FsGiFundMaster_AutoManual` | TField |  | Model code for cross price calculation method. Multifonds DB Column is AUTO_MANUAL. |
| 205 | `FS.GI.FUND.MASTER.INDIVIDUAL.EQ.RATE.RECEIPT` | `FsGiFundMaster_IndividualEqRateReceipt` | TField | Conditional | Individual Equilization Rate Receipt code used to specify if the Rate recipts is optional/mandatory for pricing transaction. Multifonds DB Column is IND_EQUI_RATE_REC. |
| 206 | `FS.GI.FUND.MASTER.INDIVIDUAL.EQ.METHOD` | `FsGiFundMaster_IndividualEqMethod` | TField |  | It specifies the individual equilization method code. Multifonds DB Column is IND_EQUI_METHOD. |
| 207 | `FS.GI.FUND.MASTER.CONTRACT.NOTES.MODEL` | `FsGiFundMaster_ContractNotesModel` | TField |  | The model code of contract note sent by the TA. Multifonds DB Column is CMODEL_CN. |
| 208 | `FS.GI.FUND.MASTER.TA.FUND.ID` | `FsGiFundMaster_TaFundId` | TField |  | TA Fund is an Internal ID with combination of Fund ID and Base Currency. Multifonds DB Column is NPTF. |
| 209 | `FS.GI.FUND.MASTER.TA.THRESHOLD.AMOUNT` | `FsGiFundMaster_TaThresholdAmount` | TField |  | Threshold amount for Partial settlement. Multifonds DB Column is TA_FUND_THRESHOLD_AMT. |
| 210 | `FS.GI.FUND.MASTER.TA.THRESHOLD.CURRENCY` | `FsGiFundMaster_TaThresholdCurrency` | TField |  | Threshold currency (in 3 letter ISO format eg: &apos;USD&apos;). Multifonds DB Column is TA_FUND_THRESHOLD_CCY. |
| 211 | `FS.GI.FUND.MASTER.CALENDAR.START.DATE` | `FsGiFundMaster_CalendarStartDate` | TField |  | Generate calendar start date input. Nondatabase field doesn&apos;t store in the core table. Multifonds DB Column is CALENDAR_START_DATE. |
| 212 | `FS.GI.FUND.MASTER.CALENDAR.END.DATE` | `FsGiFundMaster_CalendarEndDate` | TField |  | Generate calendar end Date input. Nondatabase field doesn&apos;t store in the core table. Multifonds DB Column is CALENDAR_END_DATE. |
| 213 | `FS.GI.FUND.MASTER.RESERVED10` | `FsGiFundMaster_Reserved10` | TField |  |  |
| 214 | `FS.GI.FUND.MASTER.RESERVED9` | `FsGiFundMaster_Reserved9` | TField |  |  |
| 215 | `FS.GI.FUND.MASTER.RESERVED8` | `FsGiFundMaster_Reserved8` | TField |  |  |
| 216 | `FS.GI.FUND.MASTER.RESERVED7` | `FsGiFundMaster_Reserved7` | TField |  |  |
| 217 | `FS.GI.FUND.MASTER.RESERVED6` | `FsGiFundMaster_Reserved6` | TField |  |  |
| 218 | `FS.GI.FUND.MASTER.RESERVED5` | `FsGiFundMaster_Reserved5` | TField |  |  |
| 219 | `FS.GI.FUND.MASTER.RESERVED4` | `FsGiFundMaster_Reserved4` | TField |  |  |
| 220 | `FS.GI.FUND.MASTER.RESERVED3` | `FsGiFundMaster_Reserved3` | TField |  |  |
| 221 | `FS.GI.FUND.MASTER.RESERVED2` | `FsGiFundMaster_Reserved2` | TField |  |  |
| 222 | `FS.GI.FUND.MASTER.RESERVED1` | `FsGiFundMaster_Reserved1` | TField |  |  |
| 223 | `FS.GI.FUND.MASTER.LOCAL.REF` | `FsGiFundMaster_LocalRef` |  |  |  |
| 224 | `FS.GI.FUND.MASTER.OVERRIDE` | `FsGiFundMaster_Override` |  |  |  |
| 225 | `FS.GI.FUND.MASTER.RECORD.STATUS` | `FsGiFundMaster_RecordStatus` | String |  |  |
| 226 | `FS.GI.FUND.MASTER.CURR.NO` | `FsGiFundMaster_CurrNo` | String |  |  |
| 227 | `FS.GI.FUND.MASTER.INPUTTER` | `FsGiFundMaster_Inputter` |  |  |  |
| 228 | `FS.GI.FUND.MASTER.DATE.TIME` | `FsGiFundMaster_DateTime` |  |  |  |
| 229 | `FS.GI.FUND.MASTER.AUTHORISER` | `FsGiFundMaster_Authoriser` | String |  |  |
| 230 | `FS.GI.FUND.MASTER.CO.CODE` | `FsGiFundMaster_CoCode` | String |  |  |
| 231 | `FS.GI.FUND.MASTER.DEPT.CODE` | `FsGiFundMaster_DeptCode` | String |  |  |
| 232 | `FS.GI.FUND.MASTER.AUDITOR.CODE` | `FsGiFundMaster_AuditorCode` | String |  |  |
| 233 | `FS.GI.FUND.MASTER.AUDIT.DATE.TIME` | `FsGiFundMaster_AuditDateTime` | String |  |  |
