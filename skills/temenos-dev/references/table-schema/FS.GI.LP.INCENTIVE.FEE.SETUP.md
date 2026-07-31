# FS.GI.LP.INCENTIVE.FEE.SETUP — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.INCENTIVE.FEE.SETUP` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.INCENTIVE.FEE.SETUP.PARENT.REF.ID` | `FsGiLpIncentiveFeeSetup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ORA.ROWID` | `FsGiLpIncentiveFeeSetup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.SEQ.NO` | `FsGiLpIncentiveFeeSetup_IncentiveFeeSeqNo` | TField |  | Incentive fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 4 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.STATUS` | `FsGiLpIncentiveFeeSetup_IncentiveFeeStatus` | TField |  | Incentive fee setup status automatically assigned by the system. Multifonds DB Column is STATUS. |
| 5 | `FS.GI.LP.INCENTIVE.FEE.SETUP.TA.FUND.ID` | `FsGiLpIncentiveFeeSetup_TaFundId` | TField |  | Fund Internal ID for which the incentive Fee is being defined. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.LP.INCENTIVE.FEE.SETUP.SHARE.CLASS.CODE` | `FsGiLpIncentiveFeeSetup_ShareClassCode` | TField |  | Fund share class code for which the Incentive fee is being defined. defined. Multifonds DB Column is TPART. |
| 7 | `FS.GI.LP.INCENTIVE.FEE.SETUP.LP.GROUP.ID` | `FsGiLpIncentiveFeeSetup_LpGroupId` | TField |  | Internal Id of the group of partners for which the Incentive fees is to be applied. Multifonds DB Column is GROUP_ID. |
| 8 | `FS.GI.LP.INCENTIVE.FEE.SETUP.DEFAULT.FEE.GROUP.FLAG` | `FsGiLpIncentiveFeeSetup_DefaultFeeGroupFlag` | TField |  | This flag is used to indicate that new partners into the fund and class should be added by default to the fee group. Multifonds DB Column is DEFAULT_FEE_GRP. |
| 9 | `FS.GI.LP.INCENTIVE.FEE.SETUP.LP.GROUP.DESCRIPTION` | `FsGiLpIncentiveFeeSetup_LpGroupDescription` | TField |  | Description for the Group ID. Multifonds DB Column is GROUP_DESCRIPTION. |
| 10 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.ANNIVERSARY.DURATION` | `FsGiLpIncentiveFeeSetup_IcfAnniversaryDuration` | TField |  | Specifies the period in months during which No incentive fees will pay until the period is over.The accrual will occur as per the normal calculation although there will be no crystallizations until after the anniversary date is passed. Multifonds DB Column is NB_ANNIVERSARY. |
| 11 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.VALID.START.DATE` | `FsGiLpIncentiveFeeSetup_IncentiveFeeValidStartDate` | TField |  | Incentive fee validity period start date. Multifonds DB Column is DVALID_START. |
| 12 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.VALID.END.DATE` | `FsGiLpIncentiveFeeSetup_IncentiveFeeValidEndDate` | TField |  | Incentive fee validity period end date. Multifonds DB Column is DVALID_END. |
| 13 | `FS.GI.LP.INCENTIVE.FEE.SETUP.REGISTER.ID` | `FsGiLpIncentiveFeeSetup_RegisterId` | TField |  | Internal register Id of the specific Partner for whom the Incentive fees is to be applied. Multifonds DB Column is NREGISTER. |
| 14 | `FS.GI.LP.INCENTIVE.FEE.SETUP.CONTRACT.ID` | `FsGiLpIncentiveFeeSetup_ContractId` | TField |  | Specific tranch for which the Incentive fees is to be applied. Multifonds DB Column is NCONTRACT. |
| 15 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.CALC.METHOD` | `FsGiLpIncentiveFeeSetup_IncentiveFeeCalcMethod` | TField |  | Specifies the methodof incentive fee. Example Simple - No Hurdle - Total Profit, Hurdle - Excess Income Note that if no hurdlea is chosen, then the selections in the a hurdle calculationa section will not be available Multifonds DB Column is CFEE_CALC. |
| 16 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.RATE.TYPE` | `FsGiLpIncentiveFeeSetup_IncentiveFeeRateType` | TField |  | Allows defining the type of incentive fee rate.Example: Percentage, Scale. Multifonds DB Column is CTYPE_RATE. |
| 17 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.SCALE.CODE` | `FsGiLpIncentiveFeeSetup_IncentiveFeeScaleCode` | TField |  | Internal Scale ID to be applied to cacluate incentive fess when rate type is chosen as &quot;Scale&quot;. Multifonds DB Column is SCALE_CODE. |
| 18 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.RATE.PERCENTAGE` | `FsGiLpIncentiveFeeSetup_IncentiveFeeRatePercentage` | TField |  | Fixed % rate to be applied to cacluate incentive fess when rate type is chosen as &quot;Percentage&quot;. Multifonds DB Column is PCT_FEE. |
| 19 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INCENTIVE.FEE.APPLICABLE.FLAG` | `FsGiLpIncentiveFeeSetup_IncentiveFeeApplicableFlag` | TField |  | If flagged, the fee will be calculated. If no fee calculation is required this flag SHOULD NOT be ticked. This setup has to be completed at the fund/share class level even if there is no incentive fee on the fund. Otherwise an error message would be returned when executing the break period processing. Multifonds DB Column is FLG_FEE_APPLICABLE. |
| 20 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.PAYMENT.FREQUENCY` | `FsGiLpIncentiveFeeSetup_IcfPaymentFrequency` | TField |  | Define how often the Incentive fee should be crystallized and paid. For example: Monthly, Quarterly, Half year. Multifonds DB Column is CFREQ_PAY. |
| 21 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.PAYMENT.PERIOD.START.DATE` | `FsGiLpIncentiveFeeSetup_IcfPaymentPeriodStartDate` | TField |  | Start date for the incentive fee payment frequency. Multifonds DB Column is DPAY_START. |
| 22 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.PAYMENT.PERIOD.END.DATE` | `FsGiLpIncentiveFeeSetup_IcfPaymentPeriodEndDate` | TField |  | Auto populated End date for the incentive fee payment frequency. Multifonds DB Column is DPAY_END. |
| 23 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.PAY.PER.NEXT.THEORET.DATE` | `FsGiLpIncentiveFeeSetup_IcfPayPerNextTheoretDate` | TField |  | Auto populated Next expected end date for the incentive fee payment frequency. Multifonds DB Column is DPAY_NTCD. |
| 24 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.ORDER.CRYST.OPTION` | `FsGiLpIncentiveFeeSetup_IcfOrderCrystOption` | TField |  | To specify fee crystallization options for debit orders. For example: At time of order, Deferred crystallization. Multifonds DB Column is CFEE_CRYST. |
| 25 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.CRYST.FEE.WITHDRAW.METHOD` | `FsGiLpIncentiveFeeSetup_IcfCrystFeeWithdrawMethod` | TField |  | Defines on which basis the portion of accrued incentive fee has to be calculated (and profit/loss and hurdle are to be adjusted), either on the capital gross or net of Asset-Based fees accruals. Multifonds DB Column is CFEE_CRYST_METHOD. |
| 26 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.REALLOCATION.PARTNERS` | `FsGiLpIncentiveFeeSetup_IcfReallocationPartners` | TField |  | If ticked, fees reallocation can be done to some partners. Multifonds DB Column is FLG_RE_ALLOC. |
| 27 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.SIDE.POC.CHARGE.MAIN.CLASS` | `FsGiLpIncentiveFeeSetup_IcfSidePocChargeMainClass` | TField |  | Fund share class code on which the Incentive fees have to be charged. Multifonds DB Column is TPART_MAIN. |
| 28 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.SP.CHARGE.MAIN.CLASS.FLAG` | `FsGiLpIncentiveFeeSetup_IcfSpChargeMainClassFlag` | TField |  | If ticked, it Indicates that another share class need to get charged the incentive fees calculated on the current share class. Multifonds DB Column is FLG_TPART_MAIN. |
| 29 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.SP.CHG.MAIN.CLASS.FEE.TYPE` | `FsGiLpIncentiveFeeSetup_IcfSpChgMainClassFeeType` | TField |  | It helps define if the charge should be levied on the lowest tranche number of the class being charged, or to spread the charge across tranches. Multifonds DB Column is CTYPE_SP. |
| 30 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.TYPE` | `FsGiLpIncentiveFeeSetup_IcfHurdleType` | TField |  | Specfify the type of hurdle used for calculation of the hurdle amount. Example Simple hurdle - fixed percentage, Variable hurdle - benchmark. Multifonds DB Column is CTYPE_HURDLE. |
| 31 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.BENCHMARK.SECURITY.ID` | `FsGiLpIncentiveFeeSetup_IcfBenchmarkSecurityId` | TField |  | Internal Security ID with reporting code as &apos;IDX&apos; used for the benchmark (market index). Only in case of variable hurdle hurdle type. Multifonds DB Column is NOVAL_BENCHMARK. |
| 32 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.RATE.PERCENTAGE` | `FsGiLpIncentiveFeeSetup_IcfHurdleRatePercentage` | TField |  | The fixed annual hurdle rate in percentage. Available only in case 0001 - Simple hurdle - fixed percentage is selected. Multifonds DB Column is HURDLE_RATE. |
| 33 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.RATE.COMPOUND` | `FsGiLpIncentiveFeeSetup_IcfHurdleRateCompound` | TField |  | Specifies whether or not the hurdle rate will be compounded within the payment frequency. Ticked - Compounded , Unticked - Not compound. Multifonds DB Column is FLG_COMPOUND. |
| 34 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.RATE.COMMULATIVE` | `FsGiLpIncentiveFeeSetup_IcfHurdleRateCommulative` | TField |  | If ticked,will allow cumulative hurdle calculation within break periods. Multifonds DB Column is FLG_CUMULATIVE. |
| 35 | `FS.GI.LP.INCENTIVE.FEE.SETUP.HURDLE.BASIS` | `FsGiLpIncentiveFeeSetup_HurdleBasis` | TField |  | Hurdle basis field allows cumulative hurdle calculation within break periods. Multifonds DB Column is HURDLE_BASIS. |
| 36 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.CARRY.FORWORD.FLAG` | `FsGiLpIncentiveFeeSetup_IcfHurdleCarryForwordFlag` | TField |  | If ticked,will allow hurdle carries forward at payment period end. Multifonds DB Column is FLG_HURDLE_CF. |
| 37 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.CATCH.UP.PROV.FLAG` | `FsGiLpIncentiveFeeSetup_IcfHurdleCatchUpProvFlag` | TField |  | If ticked, enables the a catch-up functionalitya , so that a payment on a fully qualified incomea doesna t put net total profit back below the hurdle. Multifonds DB Column is FLG_CATCH_UP. |
| 38 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.CATCH.UP.PERCENTAGE` | `FsGiLpIncentiveFeeSetup_IcfHurdleCatchUpPercentage` | TField |  | Percentage of fee calculated under catch-up provision that GP will be paid. Defaults to 100% unless overridden when Catch-Up Provision = ticked. Multifonds DB Column is PCT_CATCH_UP. |
| 39 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.HURDLE.CALENDAR.BASIS` | `FsGiLpIncentiveFeeSetup_IcfHurdleCalendarBasis` | TField |  | Specifies how the annual rate is applied across break periods. Example ACT/ACT, ACT/Month. Multifonds DB Column is HURDLE_CALENDAR_BASIS. |
| 40 | `FS.GI.LP.INCENTIVE.FEE.SETUP.CHANGED.FLAG` | `FsGiLpIncentiveFeeSetup_ChangedFlag` | TField |  | Flag indicates the change in the incentive fees setup. Multifonds DB Column is FLG_CHANGED. |
| 41 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.LOSS.CARRY.FORWARD.FLAG` | `FsGiLpIncentiveFeeSetup_IcfLossCarryForwardFlag` | TField |  | Specfify if the loss have to be carried-forward from one payment period to the next payment period. Multifonds DB Column is FLG_LOSS_CF. |
| 42 | `FS.GI.LP.INCENTIVE.FEE.SETUP.ICF.LOSS.CF.RECOVERY.RATE.PERC` | `FsGiLpIncentiveFeeSetup_IcfLossCfRecoveryRatePerc` | TField |  | Specify in % how much additional gain the fund manager has to recover before the incentive fee is paid. Multifonds DB Column is PCT_LOSS_CF. |
| 43 | `FS.GI.LP.INCENTIVE.FEE.SETUP.FUND.ID` | `FsGiLpIncentiveFeeSetup_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 44 | `FS.GI.LP.INCENTIVE.FEE.SETUP.CLASS.CURRENCY` | `FsGiLpIncentiveFeeSetup_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 45 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED10` | `FsGiLpIncentiveFeeSetup_Reserved10` | TField |  |  |
| 46 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED9` | `FsGiLpIncentiveFeeSetup_Reserved9` | TField |  |  |
| 47 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED8` | `FsGiLpIncentiveFeeSetup_Reserved8` | TField |  |  |
| 48 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED7` | `FsGiLpIncentiveFeeSetup_Reserved7` | TField |  |  |
| 49 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED6` | `FsGiLpIncentiveFeeSetup_Reserved6` | TField |  |  |
| 50 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED5` | `FsGiLpIncentiveFeeSetup_Reserved5` | TField |  |  |
| 51 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED4` | `FsGiLpIncentiveFeeSetup_Reserved4` | TField |  |  |
| 52 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED3` | `FsGiLpIncentiveFeeSetup_Reserved3` | TField |  |  |
| 53 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED2` | `FsGiLpIncentiveFeeSetup_Reserved2` | TField |  |  |
| 54 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RESERVED1` | `FsGiLpIncentiveFeeSetup_Reserved1` | TField |  |  |
| 55 | `FS.GI.LP.INCENTIVE.FEE.SETUP.LOCAL.REF` | `FsGiLpIncentiveFeeSetup_LocalRef` |  |  |  |
| 56 | `FS.GI.LP.INCENTIVE.FEE.SETUP.OVERRIDE` | `FsGiLpIncentiveFeeSetup_Override` |  |  |  |
| 57 | `FS.GI.LP.INCENTIVE.FEE.SETUP.RECORD.STATUS` | `FsGiLpIncentiveFeeSetup_RecordStatus` | String |  |  |
| 58 | `FS.GI.LP.INCENTIVE.FEE.SETUP.CURR.NO` | `FsGiLpIncentiveFeeSetup_CurrNo` | String |  |  |
| 59 | `FS.GI.LP.INCENTIVE.FEE.SETUP.INPUTTER` | `FsGiLpIncentiveFeeSetup_Inputter` |  |  |  |
| 60 | `FS.GI.LP.INCENTIVE.FEE.SETUP.DATE.TIME` | `FsGiLpIncentiveFeeSetup_DateTime` |  |  |  |
| 61 | `FS.GI.LP.INCENTIVE.FEE.SETUP.AUTHORISER` | `FsGiLpIncentiveFeeSetup_Authoriser` | String |  |  |
| 62 | `FS.GI.LP.INCENTIVE.FEE.SETUP.CO.CODE` | `FsGiLpIncentiveFeeSetup_CoCode` | String |  |  |
| 63 | `FS.GI.LP.INCENTIVE.FEE.SETUP.DEPT.CODE` | `FsGiLpIncentiveFeeSetup_DeptCode` | String |  |  |
| 64 | `FS.GI.LP.INCENTIVE.FEE.SETUP.AUDITOR.CODE` | `FsGiLpIncentiveFeeSetup_AuditorCode` | String |  |  |
| 65 | `FS.GI.LP.INCENTIVE.FEE.SETUP.AUDIT.DATE.TIME` | `FsGiLpIncentiveFeeSetup_AuditDateTime` | String |  |  |
