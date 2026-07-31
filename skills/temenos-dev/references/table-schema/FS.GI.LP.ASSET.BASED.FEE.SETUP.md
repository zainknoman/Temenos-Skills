# FS.GI.LP.ASSET.BASED.FEE.SETUP — Table Schema

> Source: `INSERTS/I_F.FS.GI.LP.ASSET.BASED.FEE.SETUP` in `FS_LimitedPartnershipConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.PARENT.REF.ID` | `FsGiLpAssetBasedFeeSetup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ORA.ROWID` | `FsGiLpAssetBasedFeeSetup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ASSET.BASED.FEE.SEQ.NO` | `FsGiLpAssetBasedFeeSetup_AssetBasedFeeSeqNo` | TField |  | Asset based fee unique sequence number automatically assigned by the system. Multifonds DB Column is FEE_SEQ_NO. |
| 4 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.STATUS` | `FsGiLpAssetBasedFeeSetup_AbfStatus` | TField |  | Asset based fee setup status automatically assigned by the system. Multifonds DB Column is STATUS. |
| 5 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.TA.FUND.ID` | `FsGiLpAssetBasedFeeSetup_TaFundId` | TField |  | Fund identification ID for which the Asset based fees are to be defined. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.SHARE.CLASS.CODE` | `FsGiLpAssetBasedFeeSetup_ShareClassCode` | TField |  | Fund share class code for which the Asset based fees are to be defined. Multifonds DB Column is TPART. |
| 7 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ASSET.BASED.FEE.TYPE` | `FsGiLpAssetBasedFeeSetup_AssetBasedFeeType` | TField |  | Type of asset-based fee to be applied. Multifonds DB Column is CFEE_TYPE. |
| 8 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.LP.GROUP.ID` | `FsGiLpAssetBasedFeeSetup_LpGroupId` | TField |  | Internal Id of the group of partners for which the Asset based fees is to be applied. Multifonds DB Column is GROUP_ID. |
| 9 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.DEFAULT.FEE.GROUP.FLAG` | `FsGiLpAssetBasedFeeSetup_DefaultFeeGroupFlag` | TField |  | This flag is used to indicate that new partners into the fund and class should be added by default to the fee group. Multifonds DB Column is DEFAULT_FEE_GRP. |
| 10 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.LP.GROUP.DESCRIPTION` | `FsGiLpAssetBasedFeeSetup_LpGroupDescription` | TField |  | Description for the Group ID. Multifonds DB Column is GROUP_DESCRIPTION. |
| 11 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.VALID.START.DATE` | `FsGiLpAssetBasedFeeSetup_AbfValidStartDate` | TField |  | Asset based fee validity period start date. Multifonds DB Column is DVALID_START. |
| 12 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.VALID.END.DATE` | `FsGiLpAssetBasedFeeSetup_AbfValidEndDate` | TField |  | Asset based fee validity period end date. Multifonds DB Column is DVALID_END. |
| 13 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.REGISTER.ID` | `FsGiLpAssetBasedFeeSetup_RegisterId` | TField |  | Internal register Id of the specific Partner for whom the Asset based fees is to be applied. Multifonds DB Column is NREGISTER. |
| 14 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.CONTRACT.ID` | `FsGiLpAssetBasedFeeSetup_ContractId` | TField |  | Specific tranch for which the Asset based fees is to be applied. Multifonds DB Column is NCONTRACT. |
| 15 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.FEE.APPLICABLE` | `FsGiLpAssetBasedFeeSetup_AbfFeeApplicable` | TField |  | If ticked then Asste based fee will be calculated. Setup for all fees as specified at the Partnership (TA Fund) level has to be completed. Multifonds DB Column is FLG_FEE_APPLICABLE. |
| 16 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.RATE.TYPE` | `FsGiLpAssetBasedFeeSetup_AbfRateType` | TField |  | Type of rate to be applied on Asset base fees Example: Rate in %, Scale. Multifonds DB Column is CRATE_TYPE. |
| 17 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.RATE.PERCENTAGE` | `FsGiLpAssetBasedFeeSetup_AbfRatePercentage` | TField |  | Fixed % rate to be applied to cacluate asset based fess when rate type is chosen as &quot;Rate&quot;. Multifonds DB Column is PCT_RATE. |
| 18 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.SCALE.CODE` | `FsGiLpAssetBasedFeeSetup_AbfScaleCode` | TField |  | Internal Scale ID to be applied to cacluate asset based fess when rate type is chosen as &quot;Scale&quot;. Multifonds DB Column is SCALE_CODE. |
| 19 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.DAY.COUNT.METHOD` | `FsGiLpAssetBasedFeeSetup_AbfDayCountMethod` | TField |  | The day count method used to calculate the asset-based fee rate. For example: ACT/ACT, ACT/Payment Period. Multifonds DB Column is DC_METHOD. |
| 20 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.SCALE.GROUP.ID.CODE` | `FsGiLpAssetBasedFeeSetup_AbfScaleGroupIdCode` | TField |  | Internal Id of group of partners for whom asset based fee needs to be applied at discounted fee rate . Multifonds DB Column is SCALE_GRP. |
| 21 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CUSTOM.ASSET.GROUP` | `FsGiLpAssetBasedFeeSetup_AbfCustomAssetGroup` | TField |  | Group ID that is used to aggregate assets in case the Aggregation method chosen is a 0010 - Custom assets groupa . Multifonds DB Column is SCALE_GROUP_DESCRIPTION. |
| 22 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.SCALE.CAP.BASIS.ALIGNMENT` | `FsGiLpAssetBasedFeeSetup_AbfScaleCapBasisAlignment` | TField |  | Calculate the a Scale capital basisa when the assets are aggregated by the most recent registers balances from each fund. Multifonds DB Column is SCA_CAP_BASIS. |
| 23 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.NEW.INV.CUS.ASSET` | `FsGiLpAssetBasedFeeSetup_AbfNewInvCusAsset` | TField |  | Flag to facilitate the management of memberships into custom assets groups. Multifonds DB Column is FLG_INV_CUSTOM_FEE_GRP. |
| 24 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.REPORTING.ONLY.FLAG` | `FsGiLpAssetBasedFeeSetup_ReportingOnlyFlag` | TField |  | Flag that allows to keep &quot;crystallization&quot; from impacting the capital balance. If ticked, the calculation will be for informational purposes only. Multifonds DB Column is FLG_REPORT. |
| 25 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CRYSTALLIZATION.METHOD` | `FsGiLpAssetBasedFeeSetup_AbfCrystallizationMethod` | TField |  | Method of asset-based fees crystallization (at what point in the payment frequency). Multifonds DB Column is CRYST_METHOD. |
| 26 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CRYST.BEFORE.ALLOC.FLAG` | `FsGiLpAssetBasedFeeSetup_AbfCrystBeforeAllocFlag` | TField |  | Flag if ticked will crystallize asset based fee before income allocation , if not ticked will crystallized after income allocation. Multifonds DB Column is FLG_BFR_ALLOC. |
| 27 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.PAYMENT.FREQUENCY` | `FsGiLpAssetBasedFeeSetup_AbfPaymentFrequency` | TField |  | Define how often the asset-based fee should be crystallized and paid. For example: Monthly, Quarterly, Half year. Multifonds DB Column is CFREQ_PAY. |
| 28 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.PAYMENT.PERIOD.START.DATE` | `FsGiLpAssetBasedFeeSetup_AbfPaymentPeriodStartDate` | TField |  | Start date for the payment frequency provided for the first period. Multifonds DB Column is DPAY_START. |
| 29 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.PAYMENT.PERIOD.END.DATE` | `FsGiLpAssetBasedFeeSetup_AbfPaymentPeriodEndDate` | TField |  | Auto populated End date for the payment frequency. Multifonds DB Column is DPAY_END. |
| 30 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.PAY.PER.NEXT.THEORET.DATE` | `FsGiLpAssetBasedFeeSetup_AbfPayPerNextTheoretDate` | TField |  | Auto populated Next expected end date for the payment frequency. Multifonds DB Column is DPAY_NTCD. |
| 31 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.ORDER.CRYST.OPTION` | `FsGiLpAssetBasedFeeSetup_AbfOrderCrystOption` | TField |  | To specify fee crystallization options when an order occurs from an order. For example: At time of order, Deferred crystallization. Multifonds DB Column is ORD_CRYST_OP. |
| 32 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.REALLOCATION.PARTNERS.FLAG` | `FsGiLpAssetBasedFeeSetup_AbfReallocationPartnersFlag` | TField |  | If ticked, fees reallocation can be done to some partners. Multifonds DB Column is FLG_RE_ALLOC. |
| 33 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.SP.CHARGE.MAIN.CLASS.FLAG` | `FsGiLpAssetBasedFeeSetup_AbfSpChargeMainClassFlag` | TField |  | If ticked, it Indicates that another share class need to get charged the Asset Based fees calculated on the current share class. Multifonds DB Column is FLG_TPART_MAIN. |
| 34 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.SIDE.POC.CHARGE.MAIN.CLASS` | `FsGiLpAssetBasedFeeSetup_AbfSidePocChargeMainClass` | TField |  | Fund share class code on which the Asset Based fees have to be charged. Multifonds DB Column is TPART_MAIN. |
| 35 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.SP.CHG.MAIN.CLASS.FEE.TYPE` | `FsGiLpAssetBasedFeeSetup_AbfSpChgMainClassFeeType` | TField |  | It helps define if the charge should be levied on the lowest tranche number of the class being charged, or to spread the charge across tranches. Multifonds DB Column is TPART_MAIN_TYPE. |
| 36 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.FIRST.BP.OFFSET.ACCRUAL` | `FsGiLpAssetBasedFeeSetup_AbfFirstBpOffsetAccrual` | TField |  | First BP Offsetting accrual flag. Multifonds DB Column is FLG_FBP_OFF_ACC. |
| 37 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CAPITAL.BASIS` | `FsGiLpAssetBasedFeeSetup_AbfCapitalBasis` | TField |  | It specifies which capital balance to use as a basis for fee calculation. Example Ending Capital, Average capital. Multifonds DB Column is CAP_BASIS. |
| 38 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CAPITAL.BASIS.CALC.PERIOD` | `FsGiLpAssetBasedFeeSetup_AbfCapitalBasisCalcPeriod` | TField |  | It specifies the period length over which the capital basis should be used for calculation. Multifonds DB Column is CFREQ_CAP. |
| 39 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CAPITAL.BASIS.START.DATE` | `FsGiLpAssetBasedFeeSetup_AbfCapitalBasisStartDate` | TField |  | Start date for the fee capital basis frequency. Multifonds DB Column is DCAP_START. |
| 40 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CAPITAL.BASIS.END.DATE` | `FsGiLpAssetBasedFeeSetup_AbfCapitalBasisEndDate` | TField |  | Auto populated End date for the fee capital basis frequency. Multifonds DB Column is DCAP_END. |
| 41 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.CAPITAL.BASIS.NEXT.TC.DATE` | `FsGiLpAssetBasedFeeSetup_AbfCapitalBasisNextTcDate` | TField |  | Auto populated Next expected end date for the fee capital basis frequency. Multifonds DB Column is DCAP_NTCD. |
| 42 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.PRORATE.PARITIAL.WITHDRAW` | `FsGiLpAssetBasedFeeSetup_AbfProrateParitialWithdraw` | TField |  | If flagged it takes the mid-period debits into account in the capital basis (amount and number of days) and does a pro-rated accrual calculation. If not, the capital basis would ignore that there were capital movements. This flag is used in conjunction with the &quot;Crystallization method&quot;, &quot;Order crystallization option&quot;, and &quot;Capital basis type&quot;, to determine the timing and pro-ration of all fee accruals and payments. Multifonds DB Column is ADJ_PART_WIDRAW. |
| 43 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.PRORATE.ON.CONTRIBUTION` | `FsGiLpAssetBasedFeeSetup_AbfProrateOnContribution` | TField |  | If flagged it takes the mid-period credits into account in the capital basis (amount and number of days) and does a pro-rated accrual calculation. If not, the capital basis would ignore that there were capital movements. This flag is used in conjunction with the &quot;Crystallization method&quot;, &quot;Order crystallization option&quot;, and &quot;Capital basis type&quot;, to determine the timing and pro-ration of all fee accruals and payments. Multifonds DB Column is FLG_ADJ_CONTRIB. |
| 44 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.ABF.NET.OF.INCENTIVE.FEE` | `FsGiLpAssetBasedFeeSetup_AbfNetOfIncentiveFee` | TField |  | If flagged, for beginning capital balances, capital basis will be Net of incentive fee accruals. If not flagged, capital basis will be gross. Multifonds DB Column is FLG_NET_INC_FEE. |
| 45 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.CHANGED.FLAG` | `FsGiLpAssetBasedFeeSetup_ChangedFlag` | TField |  | If flagged, indicates the change in the asset based fee setup. Multifonds DB Column is FLG_CHANGED. |
| 46 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.FUND.ID` | `FsGiLpAssetBasedFeeSetup_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 47 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.CLASS.CURRENCY` | `FsGiLpAssetBasedFeeSetup_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 48 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED10` | `FsGiLpAssetBasedFeeSetup_Reserved10` | TField |  |  |
| 49 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED9` | `FsGiLpAssetBasedFeeSetup_Reserved9` | TField |  |  |
| 50 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED8` | `FsGiLpAssetBasedFeeSetup_Reserved8` | TField |  |  |
| 51 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED7` | `FsGiLpAssetBasedFeeSetup_Reserved7` | TField |  |  |
| 52 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED6` | `FsGiLpAssetBasedFeeSetup_Reserved6` | TField |  |  |
| 53 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED5` | `FsGiLpAssetBasedFeeSetup_Reserved5` | TField |  |  |
| 54 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED4` | `FsGiLpAssetBasedFeeSetup_Reserved4` | TField |  |  |
| 55 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED3` | `FsGiLpAssetBasedFeeSetup_Reserved3` | TField |  |  |
| 56 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED2` | `FsGiLpAssetBasedFeeSetup_Reserved2` | TField |  |  |
| 57 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RESERVED1` | `FsGiLpAssetBasedFeeSetup_Reserved1` | TField |  |  |
| 58 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.LOCAL.REF` | `FsGiLpAssetBasedFeeSetup_LocalRef` |  |  |  |
| 59 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.OVERRIDE` | `FsGiLpAssetBasedFeeSetup_Override` |  |  |  |
| 60 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.RECORD.STATUS` | `FsGiLpAssetBasedFeeSetup_RecordStatus` | String |  |  |
| 61 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.CURR.NO` | `FsGiLpAssetBasedFeeSetup_CurrNo` | String |  |  |
| 62 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.INPUTTER` | `FsGiLpAssetBasedFeeSetup_Inputter` |  |  |  |
| 63 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.DATE.TIME` | `FsGiLpAssetBasedFeeSetup_DateTime` |  |  |  |
| 64 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.AUTHORISER` | `FsGiLpAssetBasedFeeSetup_Authoriser` | String |  |  |
| 65 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.CO.CODE` | `FsGiLpAssetBasedFeeSetup_CoCode` | String |  |  |
| 66 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.DEPT.CODE` | `FsGiLpAssetBasedFeeSetup_DeptCode` | String |  |  |
| 67 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.AUDITOR.CODE` | `FsGiLpAssetBasedFeeSetup_AuditorCode` | String |  |  |
| 68 | `FS.GI.LP.ASSET.BASED.FEE.SETUP.AUDIT.DATE.TIME` | `FsGiLpAssetBasedFeeSetup_AuditDateTime` | String |  |  |
