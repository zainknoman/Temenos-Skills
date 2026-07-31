# ALLFND.FUND.SECURITY — Table Schema

> Source: `INSERTS/I_F.ALLFND.FUND.SECURITY` in `ALLFND_FundsCatalogue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ALLFND.SEC.FUND.HOUSE.COUNTRY` | `AllfndFundSecurity_FundHouseCountry` | TField |  | Refers to the administration code |
| 2 | `ALLFND.SEC.GEOGRAPHIC.AREA` | `AllfndFundSecurity_GeographicArea` | TField |  | Refers to the tax model code associated with autoliquidation tax |
| 3 | `ALLFND.SEC.GEOGRAPHIC.ZONE` | `AllfndFundSecurity_GeographicZone` | TField |  | Refers to the fiscal year denoting YY |
| 4 | `ALLFND.SEC.MAXIMUM.AMOUNT` | `AllfndFundSecurity_MaximumAmount` | TField |  | It contains the maximum amount of the fund |
| 5 | `ALLFND.SEC.GAINS.COMMISSION` | `AllfndFundSecurity_GainsCommission` | TField |  | It contains the gains commission of the fund |
| 6 | `ALLFND.SEC.SUBSCRIPTION.COMMISSION` | `AllfndFundSecurity_SubscriptionCommission` | TField |  | It contains the sugscription commission of the fund |
| 7 | `ALLFND.SEC.REDEMPTION.COMMISSION` | `AllfndFundSecurity_RedemptionCommission` | TField |  | It contains the Redemption commission of the fund |
| 8 | `ALLFND.SEC.DISTRIBUTION.COMMISSION` | `AllfndFundSecurity_DistributionCommission` | TField |  | It contains the distribution commission of the fund |
| 9 | `ALLFND.SEC.TOTAL.COMMISSION` | `AllfndFundSecurity_TotalCommission` | TField |  | It contains the total commission of the fund |
| 10 | `ALLFND.SEC.DEPOSIT.COMMISSION` | `AllfndFundSecurity_DepositCommission` | TField |  | It contains the deposit commission of the fund |
| 11 | `ALLFND.SEC.INITIAL.SHARES` | `AllfndFundSecurity_InitialShares` | TField |  | It indicates the initial shares of the fund |
| 12 | `ALLFND.SEC.ADDITIONAL.SHARES` | `AllfndFundSecurity_AdditionalShares` | TField |  | It indicates the additional shares of the fund |
| 13 | `ALLFND.SEC.MINIMUM.PERMANENCE` | `AllfndFundSecurity_MinimumPermanence` | TField |  | It contains the minimum performance shares of the fund |
| 14 | `ALLFND.SEC.MAXIMUM.SHARES` | `AllfndFundSecurity_MaximumShares` | TField |  | It contains the maximum shares of the fund |
| 15 | `ALLFND.SEC.DECIMAL.SHARES` | `AllfndFundSecurity_DecimalShares` | TField |  | It indicates the Decimals for shares of the fund |
| 16 | `ALLFND.SEC.DECIMAL.AMOUNT` | `AllfndFundSecurity_DecimalAmount` | TField |  | It indicates the Decimals for amount of the fund |
| 17 | `ALLFND.SEC.PRICE.DECIMALS` | `AllfndFundSecurity_PriceDecimals` | TField |  | It indicates the Decimals for price of the fund |
| 18 | `ALLFND.SEC.TRANSFER.AGENT.NAME` | `AllfndFundSecurity_TransferAgentName` | TField |  | It indicates the Name of the Transfer Agent |
| 19 | `ALLFND.SEC.LOCAL.REF` | `AllfndFundSecurity_LocalRef` |  |  |  |
| 20 | `ALLFND.SEC.TGT.NEED.CUS` | `AllfndFundSecurity_TgtNeedCus` | TField |  | Indicates holding period |
| 21 | `ALLFND.SEC.PERF.FEE.EXANTE` | `AllfndFundSecurity_PerfFeeExante` | TField |  | Indicates Incidental costs ex ante Funds along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 22 | `ALLFND.SEC.PERF.FEE.EXPOST` | `AllfndFundSecurity_PerfFeeExpost` | TField |  | Indicates Incidental costs ex post Funds along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 23 | `ALLFND.SEC.DIST.FEE.EXANTE` | `AllfndFundSecurity_DistFeeExante` | TField |  | Indicates Instrument distribution fee Funds along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 24 | `ALLFND.SEC.DIST.FEE.EXPOST` | `AllfndFundSecurity_DistFeeExpost` | TField |  | Indicates Instrument distribution fee Funds along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 25 | `ALLFND.SEC.MGNT.FEE.ACTUAL` | `AllfndFundSecurity_MgntFeeActual` | TField |  | Indicates Management fee Funds along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 26 | `ALLFND.SEC.LEGAL.STRUCTURE` | `AllfndFundSecurity_LegalStructure` | TField |  | Indicates Legal Structure |
| 27 | `ALLFND.SEC.TRLR.FEE.EXANTE` | `AllfndFundSecurity_TrlrFeeExante` | TField |  | Indicates Trailer fee basic points applied for the distributor |
| 28 | `ALLFND.SEC.TRNS.COST.EXANTE` | `AllfndFundSecurity_TrnsCostExante` | TField |  | Indicates Transaction costs ex ante Fund along with sign. Allowed signs +(positive), -(negative), .(no information) |
| 29 | `ALLFND.SEC.TRNS.COST.EXPOST` | `AllfndFundSecurity_TrnsCostExpost` | TField |  | Indicates Transaction costs ex post Fund along with sign. Allowed signs +(positive), -(negative), .(no information) |
| 30 | `ALLFND.SEC.VALUATION.TYPE` | `AllfndFundSecurity_ValuationType` | TField |  | Indicates Type of Valuation |
| 31 | `ALLFND.SEC.ONGOING.CHARGES` | `AllfndFundSecurity_OngoingCharges` | TField |  | Indicates Ongoing charge as per the fund KIID |
| 32 | `ALLFND.SEC.UCITS.FUND` | `AllfndFundSecurity_UcitsFund` | TField |  | Indicates whether fund is under European Regulation. Allowed values Y:Yes, N:No, .(Information not available) |
| 33 | `ALLFND.SEC.CNMV.REG.CODE` | `AllfndFundSecurity_CnmvRegCode` | TField |  | Indicates name of register organism |
| 34 | `ALLFND.SEC.COMPLIANCE.LIQ` | `AllfndFundSecurity_ComplianceLiq` | TField |  | Indicates specific investment need. S:ESG, Y:Yes, N:No, I:Islamnic Banking, G:Green Investment, E:Ethical Investment |
| 35 | `ALLFND.SEC.MGNT.FEE.EXPOST` | `AllfndFundSecurity_MgntFeeExpost` | TField |  | This field indicates Financial_Instrument_Management_Fee_Ex_Post Funds |
| 36 | `ALLFND.SEC.ONGOING.COST.EXANTE` | `AllfndFundSecurity_OngoingCostExante` | TField |  | This field indicates Financial_Instrument_Gross_Ongoing_Costs Funds |
| 37 | `ALLFND.SEC.ONGOING.COST.EXPOST` | `AllfndFundSecurity_OngoingCostExpost` | TField |  | This field indicates Financial_Instrument_Ongoing_Costs_Ex_Post Funds |
| 38 | `ALLFND.SEC.MAXIMUM.ENTRY.COST` | `AllfndFundSecurity_MaximumEntryCost` | TField |  | This field indicates One-off_Cost_Financial_Instrument_Maximum_Entry_Cost_Acquired |
| 39 | `ALLFND.SEC.MAXIMUM.EXIT.COST` | `AllfndFundSecurity_MaximumExitCost` | TField |  | This field indicates One-off_Costs_Financial_Instrument_Maximum_Exit_Cost_Acquired |
| 40 | `ALLFND.SEC.OVERRIDE` | `AllfndFundSecurity_Override` |  |  |  |
| 41 | `ALLFND.SEC.RECORD.STATUS` | `AllfndFundSecurity_RecordStatus` | String |  |  |
| 42 | `ALLFND.SEC.CURR.NO` | `AllfndFundSecurity_CurrNo` | String |  |  |
| 43 | `ALLFND.SEC.INPUTTER` | `AllfndFundSecurity_Inputter` |  |  |  |
| 44 | `ALLFND.SEC.DATE.TIME` | `AllfndFundSecurity_DateTime` |  |  |  |
| 45 | `ALLFND.SEC.SIG.UNFAV.SCE1.RHP` | `AllfndFundSecurity_SigUnfavSce1Rhp` | TField |  | Indicates Sig Unfavourable scenario1 RHP along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 46 | `ALLFND.SEC.SIG.UNFAV.HALF.RHP` | `AllfndFundSecurity_SigUnfavHalfRhp` | TField |  | Indicates Sig Unfavourable half RHP along with Sign. Allowed signs +(positive), -(negative), .(no information) |
| 47 | `ALLFND.SEC.SIG.UNFAV.RHP` | `AllfndFundSecurity_SigUnfavRhp` | TField |  | Indicates Sig Unfavourable RHP. Allowed signs +(positive), -(negative), .(no information) |
| 48 | `ALLFND.SEC.UNFAV.SCENARIO1.RHP` | `AllfndFundSecurity_UnfavScenario1Rhp` | TField |  | Indicates Unfavourable scenario1 RHP. Allowed signs +(positive), -(negative), .(no information) |
| 49 | `ALLFND.SEC.UNFAV.HALF.RHP` | `AllfndFundSecurity_UnfavHalfRhp` | TField |  | Indicates Unfavourable half RHP. Allowed signs +(positive), -(negative), .(no information) |
| 50 | `ALLFND.SEC.UNFAVORABLE.RHP` | `AllfndFundSecurity_UnfavorableRhp` | TField |  | Indicates Unfavorable RHP. Allowed signs +(positive), -(negative), .(no information) |
| 51 | `ALLFND.SEC.MOD.SCENARIO1.RHP` | `AllfndFundSecurity_ModScenario1Rhp` | TField |  | Indicates Moderate scenario1 RHP. Allowed signs +(positive), -(negative), .(no information) |
| 52 | `ALLFND.SEC.MOD.HALF.RHP` | `AllfndFundSecurity_ModHalfRhp` | TField |  | Indicates Moderate half RHP. Allowed signs +(positive), -(negative), .(no information) |
| 53 | `ALLFND.SEC.MODERATE.RHP` | `AllfndFundSecurity_ModerateRhp` | TField |  | Indicates Moderate RHP. Allowed signs +(positive), -(negative), .(no information) |
| 54 | `ALLFND.SEC.FAV.SCENARIO1.RHP` | `AllfndFundSecurity_FavScenario1Rhp` | TField |  | Indicates Favourable Scenario1 RHP. Allowed signs +(positive), -(negative), .(no information) |
| 55 | `ALLFND.SEC.FAV.HALF.RHP` | `AllfndFundSecurity_FavHalfRhp` | TField |  | Indicates Favourable half RHP. Allowed signs +(positive), -(negative), .(no information) |
| 56 | `ALLFND.SEC.FAVOURABLE.RHP` | `AllfndFundSecurity_FavourableRhp` | TField |  | Indicates Favourable RHP. Allowed signs +(positive), -(negative), .(no information) |
| 57 | `ALLFND.SEC.MULTIPRICE.FUND` | `AllfndFundSecurity_MultipriceFund` | TField |  | Indicates if AFB manages several prices for the same date for the fund. Allowed values Y/N |
| 58 | `ALLFND.SEC.RDR.CLEAN` | `AllfndFundSecurity_RdrClean` | TField |  | Indicates whether the fund is RDR |
| 59 | `ALLFND.SEC.FUND.SUBSCRIPTION.COMMISSION` | `AllfndFundSecurity_FundSubscriptionCommission` | TField |  | Indicates the percentage of Fund commission for Subscriptions |
| 60 | `ALLFND.SEC.FUND.REDEMPTION.COMMISSION` | `AllfndFundSecurity_FundRedemptionCommission` | TField |  | Indicates the percentage of Fund commission for Redemption |
| 61 | `ALLFND.SEC.FUND.HOUSE.COMMISSION` | `AllfndFundSecurity_FundHouseCommission` | TField |  | Indicates Fund House Commission. Values: '' - not informed '0' - does not apply '1' - by percentage applied to amount |
| 62 | `ALLFND.SEC.FUND.HOUSE.SUB.COMM` | `AllfndFundSecurity_FundHouseSubComm` | TField |  | Indicates the percentage of Fund House commission for Subscriptions |
| 63 | `ALLFND.SEC.FUND.HOUSE.RED.COMM` | `AllfndFundSecurity_FundHouseRedComm` | TField |  | Indicates the percentage of Fund House commission for Redemption |
| 64 | `ALLFND.SEC.SWITCH.COMMISSION` | `AllfndFundSecurity_SwitchCommission` | TField |  | Indicates Switch Commission Values: '' - not informed '0' - does not apply '1' - by percentage applied to amount |
| 65 | `ALLFND.SEC.SWITCH.COMMISSION.PERCENT` | `AllfndFundSecurity_SwitchCommissionPercent` | TField |  | Indicates the Switch Commission percent |
| 66 | `ALLFND.SEC.PERFORMANCE.FEE.TYPE` | `AllfndFundSecurity_PerformanceFeeType` | TField |  | Indicates the type of calculation of performance fee. Values: '' - not informed '00' - does not apply '01' - multiseries '02' - Equalization credit '03' - Forced Redemption(with equalization) '04' - Forced Redemption(without equalization) |
| 67 | `ALLFND.SEC.PERFORMANCE.FEE.FREQUENCY` | `AllfndFundSecurity_PerformanceFeeFrequency` | TField |  | Indicates the frequency of calculation of Performance fee. Values: '' - not informed '00' - does not apply '01' - yearly '02' - half yearly '03' - quarterly |
| 68 | `ALLFND.SEC.PERFORMANCE.FEE` | `AllfndFundSecurity_PerformanceFee` | TField |  | Indicates the Performance fee. |
| 69 | `ALLFND.SEC.GUARANTEE.FLAG` | `AllfndFundSecurity_GuaranteeFlag` | TField |  | Indicates fund is secured or not. If the value in this field is Y, it is considered as a secured fund. Possible Values: "Y", "NO", "NEUTRAL" or blank Default blank |
| 70 | `ALLFND.SEC.CAPITAL.PROTECTION` | `AllfndFundSecurity_CapitalProtection` | TField |  | Specifies the percentage of the capital that is protected depending on the securing type. |
| 71 | `ALLFND.SEC.AUTHORISER` | `AllfndFundSecurity_Authoriser` | String |  |  |
| 72 | `ALLFND.SEC.CO.CODE` | `AllfndFundSecurity_CoCode` | String |  |  |
| 73 | `ALLFND.SEC.DEPT.CODE` | `AllfndFundSecurity_DeptCode` | String |  |  |
| 74 | `ALLFND.SEC.AUDITOR.CODE` | `AllfndFundSecurity_AuditorCode` | String |  |  |
| 75 | `ALLFND.SEC.AUDIT.DATE.TIME` | `AllfndFundSecurity_AuditDateTime` | String |  |  |
