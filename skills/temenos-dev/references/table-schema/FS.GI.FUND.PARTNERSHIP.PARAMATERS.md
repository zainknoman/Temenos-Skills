# FS.GI.FUND.PARTNERSHIP.PARAMATERS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.PARTNERSHIP.PARAMATERS` in `FS_LimitedPartnershipStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.PARENT.REF.ID` | `FsGiFundPartnershipParamaters_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.ORA.ROWID` | `FsGiFundPartnershipParamaters_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.TA.FUND.ID` | `FsGiFundPartnershipParamaters_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.MAXIMUM.PARTNERS` | `FsGiFundPartnershipParamaters_MaximumPartners` | TField |  | Maximum number of active partners in the partnership. Multifonds DB Column is MAX_PARTNERS. |
| 5 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.THRESHOLD.WARNING` | `FsGiFundPartnershipParamaters_ThresholdWarning` | TField |  | A value lower than the maximum number of partners at which a warning should be issued at order entry level if the number of partners drops. Multifonds DB Column is THRESHOLD_WARNING. |
| 6 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCEPTION.DATE` | `FsGiFundPartnershipParamaters_InceptionDate` | TField |  | Launch date of the fund. Multifonds DB Column is INCEP_DATE. |
| 7 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.CONVERSION.DATE` | `FsGiFundPartnershipParamaters_ConversionDate` | TField |  | Date on which the fund was migrated to the client. Multifonds DB Column is CONV_DATE. |
| 8 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.CALC.AT.TRANCHE.LEVEL.FLAG` | `FsGiFundPartnershipParamaters_CalcAtTrancheLevelFlag` | TField |  | Flag to open new &quot;tranche&quot; for every credit cash flow for the investor. Otherwise the calculation will be done at partner level. Multifonds DB Column is FLG_TRANCHE_LEVEL. |
| 9 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.AUTO.COLLAPSE.TRANCHE.FLAG` | `FsGiFundPartnershipParamaters_AutoCollapseTrancheFlag` | TField |  | Flag allows to automatically roll up multiple tranches for an investor assuming they all have the same fee structure, and have all paid their fees on the same date. Multifonds DB Column is FLG_COLLAPSE_TRANCHE. |
| 10 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.UNITIZED.FLAG` | `FsGiFundPartnershipParamaters_UnitizedFlag` | TField |  | Flag allows to display reporting built by the client on Infocenter. Multifonds DB Column is FLG_UNITIZED. |
| 11 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.BREAK.PERIOD.START.DATE` | `FsGiFundPartnershipParamaters_BreakPeriodStartDate` | TField |  | Start date of the current processed break period. Multifonds DB Column is BP_START_DATE. |
| 12 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.BREAK.PERIOD.END.DATE` | `FsGiFundPartnershipParamaters_BreakPeriodEndDate` | TField |  | End date of the current processed break period. Multifonds DB Column is BP_END_DATE. |
| 13 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.EXCLUDE.FLAG` | `FsGiFundPartnershipParamaters_ExcludeFlag` | TField |  | Flag to include/exclude incentive fee accruals from capital basis for income allocation (the default basis is on beginning adjusted gross capital). Multifonds DB Column is FLG_EXCLUDE. |
| 14 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.ASSET.FEE.OPTION` | `FsGiFundPartnershipParamaters_AssetFeeOption` | TField |  | Fee type of asset-based fees defines if the system should net only crystallized fees, or accruals and crystallized fees before income distribution. Multifonds DB Column is COPTION_ASSET_FEE. |
| 15 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.CHANGED.FLAG` | `FsGiFundPartnershipParamaters_ChangedFlag` | TField |  | Internal flag to indicate change in the record. Multifonds DB Column is FLG_CHANGED. |
| 16 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCOME.DIST.ROUNDING.TYPE` | `FsGiFundPartnershipParamaters_IncomeDistRoundingType` | TField |  | Rounding type defintion for auto generated Income distribution orders, order amount is generated with commercial rounding to whole amount, round down to whole amount or commercial rounding to 2 decimals based on rounding type setup Multifonds DB Column is TYPE_ARRONDI. |
| 17 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCOME.DIST.FREQUENCY` | `FsGiFundPartnershipParamaters_IncomeDistFrequency` | TField |  | Frequency definition for auto generated income distribution orders, Frequency end date and break period end date are matching system auto generates the income distribution orders for the break period Multifonds DB Column is CFEQ. |
| 18 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCOME.DIST.ORDER.TD` | `FsGiFundPartnershipParamaters_IncomeDistOrderTd` | TField |  | Order trade date definition for auto generated income distribution orders, whether order to be generated with current break period end date or next break period start date Multifonds DB Column is CODE_ORD_TD. |
| 19 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCOME.DIST.START.DATE` | `FsGiFundPartnershipParamaters_IncomeDistStartDate` | TField |  | Income distribution frequency start date, for new funds defaults the break period start date, if the break period status is 10 user allowed to modify the date. Multifonds DB Column is INC_DIST_DSTART. |
| 20 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCOME.DIST.END.DATE` | `FsGiFundPartnershipParamaters_IncomeDistEndDate` | TField |  | Income distribution frequency end date, based on selected frequency and start date auto populates the end date, if the break period status is 10 user allowed to modify the date. Multifonds DB Column is INC_DIST_DEND. |
| 21 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCOME.DIST.NEXT.THEORET.DATE` | `FsGiFundPartnershipParamaters_IncomeDistNextTheoretDate` | TField |  | Income distribution frequency next theoretical date, based on selected frequency auto populates the next theoretical date, if the break period status is 10 user allowed to modify the date Multifonds DB Column is INC_DIST_NXT_THD. |
| 22 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.NAV.METHOD` | `FsGiFundPartnershipParamaters_NavMethod` | TField |  | Field to define the approach taken to calculate the Gross/Net Nav per share, units, and transaction prices. Multifonds DB Column is CNAV_OPTION. |
| 23 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.ASSET.BASED.FEE.UNIT.FLAG` | `FsGiFundPartnershipParamaters_AssetBasedFeeUnitFlag` | TField |  | Flag to define whether Units move for crystallized Asset Based Fees. Multifonds DB Column is FLG_ABF_UNIT. |
| 24 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INCENTIVE.FEE.UNIT.FLAG` | `FsGiFundPartnershipParamaters_IncentiveFeeUnitFlag` | TField |  | Flag to define whether Units move for crystallized Incentive Fees. Multifonds DB Column is FLG_INCF_UNIT. |
| 25 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.NEW.ISSUE.UNIT.FLAG` | `FsGiFundPartnershipParamaters_NewIssueUnitFlag` | TField |  | Flag to to define whether Units move for new issue (IPO) income. Multifonds DB Column is FLG_NEWISSUE_INC_UNIT. |
| 26 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.SPECIAL.ALLOC.CLASS.UNIT.FLAG` | `FsGiFundPartnershipParamaters_SpecialAllocClassUnitFlag` | TField |  | Flag to define whether Units move for profit and loss items categorized as part of a special allocation classes. Multifonds DB Column is FLG_SPECIAL_INC_UNIT. |
| 27 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.PROPORTIONAL.WITHDRAW.METHOD` | `FsGiFundPartnershipParamaters_ProportionalWithdrawMethod` | TField |  | Proportional withdrawal method is enabled when the accounting method for the MF fund is defined as a 0006-Proportionate withdrawal by TDa , this value will be used for calculation of Tranche % at Lots screen Multifonds DB Column is PROP_WIDRAW. |
| 28 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.FUND.ID` | `FsGiFundPartnershipParamaters_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 29 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.CLASS.CURRENCY` | `FsGiFundPartnershipParamaters_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 30 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.AUTO.CREATE.NEW.GL.ACC` | `FsGiFundPartnershipParamaters_AutoCreateNewGlAcc` | TField |  | Flag to enable Automatic creation of New GL Accounts Multifonds DB Column is AUTO_CREATE_NEW_GL_ACC. |
| 31 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.APPND.SOURCE.ID.GL.ACC` | `FsGiFundPartnershipParamaters_AppndSourceIdGlAcc` | TField |  | Flag to enable appending the source ID to the GL Accounts Multifonds DB Column is APP_SOURCE_ID_GL_ACC. |
| 32 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED10` | `FsGiFundPartnershipParamaters_Reserved10` | TField |  |  |
| 33 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED9` | `FsGiFundPartnershipParamaters_Reserved9` | TField |  |  |
| 34 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED8` | `FsGiFundPartnershipParamaters_Reserved8` | TField |  |  |
| 35 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED7` | `FsGiFundPartnershipParamaters_Reserved7` | TField |  |  |
| 36 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED6` | `FsGiFundPartnershipParamaters_Reserved6` | TField |  |  |
| 37 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED5` | `FsGiFundPartnershipParamaters_Reserved5` | TField |  |  |
| 38 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED4` | `FsGiFundPartnershipParamaters_Reserved4` | TField |  |  |
| 39 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED3` | `FsGiFundPartnershipParamaters_Reserved3` | TField |  |  |
| 40 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED2` | `FsGiFundPartnershipParamaters_Reserved2` | TField |  |  |
| 41 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RESERVED1` | `FsGiFundPartnershipParamaters_Reserved1` | TField |  |  |
| 42 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.LOCAL.REF` | `FsGiFundPartnershipParamaters_LocalRef` |  |  |  |
| 43 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.OVERRIDE` | `FsGiFundPartnershipParamaters_Override` |  |  |  |
| 44 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.RECORD.STATUS` | `FsGiFundPartnershipParamaters_RecordStatus` | String |  |  |
| 45 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.CURR.NO` | `FsGiFundPartnershipParamaters_CurrNo` | String |  |  |
| 46 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.INPUTTER` | `FsGiFundPartnershipParamaters_Inputter` |  |  |  |
| 47 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.DATE.TIME` | `FsGiFundPartnershipParamaters_DateTime` |  |  |  |
| 48 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.AUTHORISER` | `FsGiFundPartnershipParamaters_Authoriser` | String |  |  |
| 49 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.CO.CODE` | `FsGiFundPartnershipParamaters_CoCode` | String |  |  |
| 50 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.DEPT.CODE` | `FsGiFundPartnershipParamaters_DeptCode` | String |  |  |
| 51 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.AUDITOR.CODE` | `FsGiFundPartnershipParamaters_AuditorCode` | String |  |  |
| 52 | `FS.GI.FUND.PARTNERSHIP.PARAMATERS.AUDIT.DATE.TIME` | `FsGiFundPartnershipParamaters_AuditDateTime` | String |  |  |
