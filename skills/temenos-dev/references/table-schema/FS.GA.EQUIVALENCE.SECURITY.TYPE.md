# FS.GA.EQUIVALENCE.SECURITY.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCE.SECURITY.TYPE` in `FS_AccountingSchema.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.PARENT.REF.ID` | `FsGaEquivalenceSecurityType_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.ORA.ROWID` | `FsGaEquivalenceSecurityType_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.GTI.CODE` | `FsGaEquivalenceSecurityType_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 4 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.IML.SECURITY.TYPE` | `FsGaEquivalenceSecurityType_ImlSecurityType` | TField |  | IML Security Type used for the generation of CSSF reporting Multifonds DB Column is CGTI_IML. |
| 5 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.REPORTING.CODE` | `FsGaEquivalenceSecurityType_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 6 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.SWIFT.SECURITY.TYPE` | `FsGaEquivalenceSecurityType_SwiftSecurityType` | TField |  | SWIFT Security Type Multifonds DB Column is CGTI_SWIFT. |
| 7 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.TAX.SECURITY.TYPE` | `FsGaEquivalenceSecurityType_TaxSecurityType` | TField |  | Define the tax security type for determining the type of instruments (bonds, equities, warrants, etc.) Multifonds DB Column is TAX_SEC_TYPE. |
| 8 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.MANAGEMENT.CODE` | `FsGaEquivalenceSecurityType_ManagementCode` | TField |  | Management Code used to identify the asste type which corresponds to fund of funds Multifonds DB Column is CTYPE_GTI. |
| 9 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.COMMISSION.GROUP` | `FsGaEquivalenceSecurityType_CommissionGroup` | TField |  | Enter a free definable commission group Multifonds DB Column is COMM_GRP. |
| 10 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.OID.TAX` | `FsGaEquivalenceSecurityType_OidTax` | TField |  | OID Tax Multifonds DB Column is OID_TAX. |
| 11 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.EXCEPTION.TO.ASSET.TYPE` | `FsGaEquivalenceSecurityType_ExceptionToAssetType` | TField |  | Exception To Asset Type Multifonds DB Column is GTI_EXCEP. |
| 12 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.BOND.TAX` | `FsGaEquivalenceSecurityType_BondTax` | TField |  | This field is to define the rule related to Tax book cost for bonds Multifonds DB Column is FLG_BOND_TAX. |
| 13 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.CAPITAL.GAINS.TAX` | `FsGaEquivalenceSecurityType_CapitalGainsTax` | TField |  | If flagged, the discount and factors will be taken into account when calculating the tax liability for the lot selection Multifonds DB Column is FLG_CGT. |
| 14 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.ALLOW.SHORT.POSITION` | `FsGaEquivalenceSecurityType_AllowShortPosition` | TField |  | Allows defining the rule applicable to the fund regarding short dealings on stocks Multifonds DB Column is FLG_SHORT. |
| 15 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.COST.OF.FOREIGN.CASH` | `FsGaEquivalenceSecurityType_CostOfForeignCash` | TField |  | It allows applying cost to each foreign cash balance. There is indeed the ability to track foreign currency costs on a lot basis. Multifonds DB Column is FLG_FX_COST. |
| 16 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.ASSET.TYPE.GROUP` | `FsGaEquivalenceSecurityType_AssetTypeGroup` | TField |  | Asset Type Group Multifonds DB Column is GTI_GRP. |
| 17 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.DEFFER` | `FsGaEquivalenceSecurityType_Deffer` | TField |  | Consideration of deferred unrealized loss Multifonds DB Column is FLG_DEFFER. |
| 18 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.DEFFER.TBC` | `FsGaEquivalenceSecurityType_DefferTbc` | TField |  | Consideration of deferred TBC amortization Multifonds DB Column is FLG_DEFFER_TBC. |
| 19 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.NAV.GOV.ASSET.TYPE.GROUP` | `FsGaEquivalenceSecurityType_NavGovAssetTypeGroup` | TField |  | NAV Gov GTI Group Multifonds DB Column is GTI_NAV_GOV_GROUP. |
| 20 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.45.DAYS.HOLDING.RULE` | `FsGaEquivalenceSecurityType_45DaysHoldingRule` |  |  |  |
| 21 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.STOP.LOSS.ELIGIBLE` | `FsGaEquivalenceSecurityType_StopLossEligible` | TField |  | Allows defining security type eligible for the Stop Loss calculation Multifonds DB Column is FLG_STOP_LOSS. |
| 22 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.BENCHMARK.ANALYSIS` | `FsGaEquivalenceSecurityType_BenchmarkAnalysis` | TField |  | Allows Multifonds performing daily Rate of Return Analysis of Mutual Fund Security performance and performance of Benchmark Security. Multifonds DB Column is FLG_BM_ELIGIBLE. |
| 23 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.EX.DATE.IDENTIFIER` | `FsGaEquivalenceSecurityType_ExDateIdentifier` | TField |  | Ex Date Identifier Multifonds DB Column is FLG_EX_DATE. |
| 24 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.MANDATORY.RATING` | `FsGaEquivalenceSecurityType_MandatoryRating` | TField | Yes | Mandatory Rating Identifier Multifonds DB Column is FLG_MANDTRY_RATING. |
| 25 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.LENDING.AK.ALLOCATION` | `FsGaEquivalenceSecurityType_LendingAkAllocation` | TField |  | Lending AK Allocation Multifonds DB Column is LEND_AK_ALLOC. |
| 26 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.MIN.HLDNG.DAYS.FOR.INDIVIDUAL` | `FsGaEquivalenceSecurityType_MinHldngDaysForIndividual` | TField |  | Minimum Holding Days For Individual Multifonds DB Column is MIN_HLD_DAYS_INDV. |
| 27 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.STD.HLDNG.DAYS.FOR.INDIVIDUAL` | `FsGaEquivalenceSecurityType_StdHldngDaysForIndividual` | TField |  | Standard Holding Days For Individual Multifonds DB Column is STD_HLD_DAYS_INDV. |
| 28 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.MIN.HOLDING.DAYS.FOR.CORPORATE` | `FsGaEquivalenceSecurityType_MinHoldingDaysForCorporate` | TField |  | Minimum Holding Days For Corporate Multifonds DB Column is MIN_HLD_DAYS_CORP. |
| 29 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.STD.HOLDING.DAYS.FOR.CORPORATE` | `FsGaEquivalenceSecurityType_StdHoldingDaysForCorporate` | TField |  | Standard Holding Days For Corporate Multifonds DB Column is STD_HLD_DAYS_CORP. |
| 30 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.TAIWAN.INTEREST.SMOOTHING` | `FsGaEquivalenceSecurityType_TaiwanInterestSmoothing` | TField |  | This field enables to apply smoothing to the purchase and sold interest between the trade date and settlement date. The interest accrual will be smoothened across the period. Multifonds DB Column is FLG_TWN_SMOOTH_INT. |
| 31 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.BANKDEBT.MEMO.CHART` | `FsGaEquivalenceSecurityType_BankdebtMemoChart` | TField |  | Bankdebt Memo Chart Multifonds DB Column is BANKDEBT_CPDC. |
| 32 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.DURATION.TO.NEXT.COUPON` | `FsGaEquivalenceSecurityType_DurationToNextCoupon` | TField |  | Duration To Next Coupon Multifonds DB Column is FLG_DUR_NEXT_COUP. |
| 33 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.CUSTODY` | `FsGaEquivalenceSecurityType_Custody` | TField |  | Custody Flag Multifonds DB Column is FLG_CUSTODY. |
| 34 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED10` | `FsGaEquivalenceSecurityType_Reserved10` | TField |  |  |
| 35 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED9` | `FsGaEquivalenceSecurityType_Reserved9` | TField |  |  |
| 36 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED8` | `FsGaEquivalenceSecurityType_Reserved8` | TField |  |  |
| 37 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED7` | `FsGaEquivalenceSecurityType_Reserved7` | TField |  |  |
| 38 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED6` | `FsGaEquivalenceSecurityType_Reserved6` | TField |  |  |
| 39 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED5` | `FsGaEquivalenceSecurityType_Reserved5` | TField |  |  |
| 40 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED4` | `FsGaEquivalenceSecurityType_Reserved4` | TField |  |  |
| 41 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED3` | `FsGaEquivalenceSecurityType_Reserved3` | TField |  |  |
| 42 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED2` | `FsGaEquivalenceSecurityType_Reserved2` | TField |  |  |
| 43 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RESERVED1` | `FsGaEquivalenceSecurityType_Reserved1` | TField |  |  |
| 44 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.LOCAL.REF` | `FsGaEquivalenceSecurityType_LocalRef` |  |  |  |
| 45 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.OVERRIDE` | `FsGaEquivalenceSecurityType_Override` |  |  |  |
| 46 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.RECORD.STATUS` | `FsGaEquivalenceSecurityType_RecordStatus` | String |  |  |
| 47 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.CURR.NO` | `FsGaEquivalenceSecurityType_CurrNo` | String |  |  |
| 48 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.INPUTTER` | `FsGaEquivalenceSecurityType_Inputter` |  |  |  |
| 49 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.DATE.TIME` | `FsGaEquivalenceSecurityType_DateTime` |  |  |  |
| 50 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.AUTHORISER` | `FsGaEquivalenceSecurityType_Authoriser` | String |  |  |
| 51 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.CO.CODE` | `FsGaEquivalenceSecurityType_CoCode` | String |  |  |
| 52 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.DEPT.CODE` | `FsGaEquivalenceSecurityType_DeptCode` | String |  |  |
| 53 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.AUDITOR.CODE` | `FsGaEquivalenceSecurityType_AuditorCode` | String |  |  |
| 54 | `FS.GA.EQUIVALENCE.SECURITY.TYPE.AUDIT.DATE.TIME` | `FsGaEquivalenceSecurityType_AuditDateTime` | String |  |  |
