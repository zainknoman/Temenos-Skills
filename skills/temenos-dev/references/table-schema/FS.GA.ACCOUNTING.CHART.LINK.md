# FS.GA.ACCOUNTING.CHART.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNTING.CHART.LINK` in `FS_ChartOfAccount.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.ACCOUNTING.CHART.LINK.PARENT.REF.ID` | `FsGaAccountingChartLink_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.ACCOUNTING.CHART.LINK.ORA.ROWID` | `FsGaAccountingChartLink_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.ACCOUNTING.CHART.LINK.LEDGER.NUMBER` | `FsGaAccountingChartLink_LedgerNumber` | TField |  | This is the account number for the ledger. Multifonds DB Column is NCOMPTE. |
| 4 | `FS.GA.ACCOUNTING.CHART.LINK.CHART.OF.ACCOUNTS.CODE` | `FsGaAccountingChartLink_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 5 | `FS.GA.ACCOUNTING.CHART.LINK.BALANCE.SHEET.CHART.CR.GROUP` | `FsGaAccountingChartLink_BalanceSheetChartCrGroup` | TField |  | This is the credit Balance Sheet chart group linked to an account Multifonds DB Column is NRUBCR. |
| 6 | `FS.GA.ACCOUNTING.CHART.LINK.BALANCE.SHEET.CHART.DB.GROUP` | `FsGaAccountingChartLink_BalanceSheetChartDbGroup` | TField |  | This is the debit Balance Sheet chart group linked to an account Multifonds DB Column is NRUBDB. |
| 7 | `FS.GA.ACCOUNTING.CHART.LINK.NAV.CHART.CREDIT.GROUP` | `FsGaAccountingChartLink_NavChartCreditGroup` | TField |  | This is the credit NAV chart group linked to an account Multifonds DB Column is NRUBCR_NAV. |
| 8 | `FS.GA.ACCOUNTING.CHART.LINK.NAV.CHART.DEBIT.GROUP` | `FsGaAccountingChartLink_NavChartDebitGroup` | TField |  | This is the debit NAV chart group linked to an account Multifonds DB Column is NRUBDB_NAV. |
| 9 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.CHART.GROUP` | `FsGaAccountingChartLink_EqualisationChartGroup` | TField |  | This code is to assign an account to the relevant income bucket for equalisation calculation. Multifonds DB Column is NRUBDB_EQL. |
| 10 | `FS.GA.ACCOUNTING.CHART.LINK.USE.FOR.DIVIDEND.DISTRIBUTION` | `FsGaAccountingChartLink_UseForDividendDistribution` | TField |  | This flag indicates the system, if a PandL account should be taken into account for the dividend distribution of a Non Multi class fund for equalization purposes only. Multifonds DB Column is DIV_EQL. |
| 11 | `FS.GA.ACCOUNTING.CHART.LINK.USE.FOR.DIVIDEND.REINVESTMENT` | `FsGaAccountingChartLink_UseForDividendReinvestment` | TField |  | This flag indicates the system, if a PandL account should be taken into account for the reinvesting of units for a Non Multi class fund for equalization purposes only. Multifonds DB Column is REI_EQL. |
| 12 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.1` | `FsGaAccountingChartLink_EqualisationCountry1` | TField |  | Eq. Country 1, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_1_EGA. |
| 13 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.2` | `FsGaAccountingChartLink_EqualisationCountry2` | TField |  | Eq. Country 2, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_2_EGA. |
| 14 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.3` | `FsGaAccountingChartLink_EqualisationCountry3` | TField |  | Eq. Country 3, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_3_EGA. |
| 15 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.4` | `FsGaAccountingChartLink_EqualisationCountry4` | TField |  | Eq. Country 4, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_4_EGA. |
| 16 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.5` | `FsGaAccountingChartLink_EqualisationCountry5` | TField |  | Eq. Country 5, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_5_EGA. |
| 17 | `FS.GA.ACCOUNTING.CHART.LINK.CASH.FLOW.CODE` | `FsGaAccountingChartLink_CashFlowCode` | TField |  | This is the cash flow code to include an account in cash flow reporting Multifonds DB Column is CASH_FLOW. |
| 18 | `FS.GA.ACCOUNTING.CHART.LINK.REPORTING.CODE` | `FsGaAccountingChartLink_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 19 | `FS.GA.ACCOUNTING.CHART.LINK.CAPITAL.PL.CHART.GROUP` | `FsGaAccountingChartLink_CapitalPlChartGroup` | TField |  | This is to group the capital and P&amp;L account for reporting. Multifonds DB Column is NRUBDB_STO. |
| 20 | `FS.GA.ACCOUNTING.CHART.LINK.LUX.LEGAL.ACCOUNT` | `FsGaAccountingChartLink_LuxLegalAccount` | TField |  | This is the equivalent account for Lux legal reporting. Multifonds DB Column is NRUBDB_IML. |
| 21 | `FS.GA.ACCOUNTING.CHART.LINK.CCLUX.REPORTING.CODE` | `FsGaAccountingChartLink_CcluxReportingCode` | TField |  | This is the CCLUX reporting code linked to an account to facilitate CCLUX reporting. Multifonds DB Column is NCODEIML. |
| 22 | `FS.GA.ACCOUNTING.CHART.LINK.UNREAL.FOREX.ADJ.CODE` | `FsGaAccountingChartLink_UnrealForexAdjCode` | TField |  | This code is used to post the unrealised forex gain/loss on a balance sheet account in the NAV Multifonds DB Column is COPER_NAV. |
| 23 | `FS.GA.ACCOUNTING.CHART.LINK.FEES` | `FsGaAccountingChartLink_Fees` | TField |  | Activates a control of fees calculated for a fund. This control will be performed with a NAV control parameter and will be reported on the report SDNAC08. Multifonds DB Column is FLG_FEES. |
| 24 | `FS.GA.ACCOUNTING.CHART.LINK.REPORT.A.NOUVEAU` | `FsGaAccountingChartLink_ReportANouveau` | TField |  | This is used for French reporting to indicate if an account is included in Report a Nouveau. Multifonds DB Column is FLG_RANEX1. |
| 25 | `FS.GA.ACCOUNTING.CHART.LINK.AVOIR.FISCAL.CREDIT.IMPOT` | `FsGaAccountingChartLink_AvoirFiscalCreditImpot` | TField |  | This is used for French reporting to indicate if an account is included in AFCI. Multifonds DB Column is FLG_AFCI. |
| 26 | `FS.GA.ACCOUNTING.CHART.LINK.UNREAL.FOREX.CLOSING.ADJ.CODE` | `FsGaAccountingChartLink_UnrealForexClosingAdjCode` | TField |  | This code is used to post the forex gain/loss on a balance sheet account in the NAV when its balance goes to zero in deal currency Multifonds DB Column is COPER_NAV2. |
| 27 | `FS.GA.ACCOUNTING.CHART.LINK.IFRS.TAG` | `FsGaAccountingChartLink_IfrsTag` | TField |  | IFRS Tag Multifonds DB Column is CGTI_IFRS. |
| 28 | `FS.GA.ACCOUNTING.CHART.LINK.EXCLUDE.IFRS.CLASS` | `FsGaAccountingChartLink_ExcludeIfrsClass` | TField |  | This flag is to denote if an account is to included in IFRS reporting. Multifonds DB Column is FLG_EXCLUDE_IFRS. |
| 29 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.6` | `FsGaAccountingChartLink_EqualisationCountry6` | TField |  | Eq. Country 6, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_6_EGA. |
| 30 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.7` | `FsGaAccountingChartLink_EqualisationCountry7` | TField |  | Eq. Country 7, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_7_EGA. |
| 31 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.8` | `FsGaAccountingChartLink_EqualisationCountry8` | TField |  | Eq. Country 8, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_8_EGA. |
| 32 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.9` | `FsGaAccountingChartLink_EqualisationCountry9` | TField |  | Eq. Country 9, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_9_EGA. |
| 33 | `FS.GA.ACCOUNTING.CHART.LINK.EQUALISATION.COUNTRY.10` | `FsGaAccountingChartLink_EqualisationCountry10` | TField |  | Eq. Country 10, GA supports 10 different eq. tables by country. It is required if specific income and / or expense accounts to be included or excluded from the equalization calculation by country. Multifonds DB Column is CPAYS_10_EGA. |
| 34 | `FS.GA.ACCOUNTING.CHART.LINK.REALISED.FOREX.CLOSING.CODE` | `FsGaAccountingChartLink_RealisedForexClosingCode` | TField |  | This code is used to post the realised forex gain/loss on a balance sheet account. Multifonds DB Column is COPER_FX_REALISE. |
| 35 | `FS.GA.ACCOUNTING.CHART.LINK.EQL.CREDIT.ACCOUNT` | `FsGaAccountingChartLink_EqlCreditAccount` | TField |  | EQL Credit Account Multifonds DB Column is NRUBCR_EQL. |
| 36 | `FS.GA.ACCOUNTING.CHART.LINK.CHA.DEBIT.ACCOUNT` | `FsGaAccountingChartLink_ChaDebitAccount` | TField |  | CHA DebitAccount Multifonds DB Column is NRUBDB_CHA. |
| 37 | `FS.GA.ACCOUNTING.CHART.LINK.CAMBIO.EXCEPTION` | `FsGaAccountingChartLink_CambioException` | TField |  | Cambio Exception Multifonds DB Column is FLG_CAMBIO_EXCEP. |
| 38 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED10` | `FsGaAccountingChartLink_Reserved10` | TField |  |  |
| 39 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED9` | `FsGaAccountingChartLink_Reserved9` | TField |  |  |
| 40 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED8` | `FsGaAccountingChartLink_Reserved8` | TField |  |  |
| 41 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED7` | `FsGaAccountingChartLink_Reserved7` | TField |  |  |
| 42 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED6` | `FsGaAccountingChartLink_Reserved6` | TField |  |  |
| 43 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED5` | `FsGaAccountingChartLink_Reserved5` | TField |  |  |
| 44 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED4` | `FsGaAccountingChartLink_Reserved4` | TField |  |  |
| 45 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED3` | `FsGaAccountingChartLink_Reserved3` | TField |  |  |
| 46 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED2` | `FsGaAccountingChartLink_Reserved2` | TField |  |  |
| 47 | `FS.GA.ACCOUNTING.CHART.LINK.RESERVED1` | `FsGaAccountingChartLink_Reserved1` | TField |  |  |
| 48 | `FS.GA.ACCOUNTING.CHART.LINK.LOCAL.REF` | `FsGaAccountingChartLink_LocalRef` |  |  |  |
| 49 | `FS.GA.ACCOUNTING.CHART.LINK.OVERRIDE` | `FsGaAccountingChartLink_Override` |  |  |  |
| 50 | `FS.GA.ACCOUNTING.CHART.LINK.RECORD.STATUS` | `FsGaAccountingChartLink_RecordStatus` | String |  |  |
| 51 | `FS.GA.ACCOUNTING.CHART.LINK.CURR.NO` | `FsGaAccountingChartLink_CurrNo` | String |  |  |
| 52 | `FS.GA.ACCOUNTING.CHART.LINK.INPUTTER` | `FsGaAccountingChartLink_Inputter` |  |  |  |
| 53 | `FS.GA.ACCOUNTING.CHART.LINK.DATE.TIME` | `FsGaAccountingChartLink_DateTime` |  |  |  |
| 54 | `FS.GA.ACCOUNTING.CHART.LINK.AUTHORISER` | `FsGaAccountingChartLink_Authoriser` | String |  |  |
| 55 | `FS.GA.ACCOUNTING.CHART.LINK.CO.CODE` | `FsGaAccountingChartLink_CoCode` | String |  |  |
| 56 | `FS.GA.ACCOUNTING.CHART.LINK.DEPT.CODE` | `FsGaAccountingChartLink_DeptCode` | String |  |  |
| 57 | `FS.GA.ACCOUNTING.CHART.LINK.AUDITOR.CODE` | `FsGaAccountingChartLink_AuditorCode` | String |  |  |
| 58 | `FS.GA.ACCOUNTING.CHART.LINK.AUDIT.DATE.TIME` | `FsGaAccountingChartLink_AuditDateTime` | String |  |  |
