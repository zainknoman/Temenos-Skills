# FS.GA.YEAR.END.RATIO — Table Schema

> Source: `INSERTS/I_F.FS.GA.YEAR.END.RATIO` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.YEAR.END.RATIO.FUND.ID` | `FsGaYearEndRatio_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.YEAR.END.RATIO.DATE.OF.NAV` | `FsGaYearEndRatio_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 3 | `FS.GA.YEAR.END.RATIO.SHARE.CLASS.CODE` | `FsGaYearEndRatio_ShareClassCode` | TField |  | Share class Multifonds DB Column is TPARTS. |
| 4 | `FS.GA.YEAR.END.RATIO.COUNTRY.IDENTIFIER` | `FsGaYearEndRatio_CountryIdentifier` | TField |  | Country code. Identifier of country. Multifonds DB Column is CEGA. |
| 5 | `FS.GA.YEAR.END.RATIO.INCOMES.AKG1` | `FsGaYearEndRatio_IncomesAkg1` | TField |  | This field displays the general ledger balance of ordinary income accounts of equity related instruments(AKG1) for calculating year end ratios Multifonds DB Column is MONTANT_I_AKG1. |
| 6 | `FS.GA.YEAR.END.RATIO.PROFIT.OR.LOSS.AKG1` | `FsGaYearEndRatio_ProfitOrLossAkg1` | TField |  | This field displays the general ledger balance of realized profit or loss results accounts of equity related instruments(AKG1) for calculating year end ratios Multifonds DB Column is MONTANT_P_AKG1. |
| 7 | `FS.GA.YEAR.END.RATIO.RATIO.INCOMES.AKG1` | `FsGaYearEndRatio_RatioIncomesAkg1` | TField |  | This field displays the year end ratio balance of ordinary income accounts for equity related instruments(AKG1) Multifonds DB Column is PER_I_AKG1. |
| 8 | `FS.GA.YEAR.END.RATIO.RATIO.PROFIT.OR.LOSS.AKG1` | `FsGaYearEndRatio_RatioProfitOrLossAkg1` | TField |  | This field displays the year end ratio balance of realized profit or loss results of equity related instruments(AKG1) Multifonds DB Column is PER_P_AKG1. |
| 9 | `FS.GA.YEAR.END.RATIO.INCOMES.AKG2` | `FsGaYearEndRatio_IncomesAkg2` | TField |  | This field displays the general ledger balance of ordinary income accounts of equity related instruments(AKG2) for calculating year end ratios Multifonds DB Column is MONTANT_I_AKG2. |
| 10 | `FS.GA.YEAR.END.RATIO.PROFIT.OR.LOSS.AKG2` | `FsGaYearEndRatio_ProfitOrLossAkg2` | TField |  | This field displays the general ledger balance of realized profit or loss results accounts of equity related instruments(AKG2) for calculating year end ratios Multifonds DB Column is MONTANT_P_AKG2. |
| 11 | `FS.GA.YEAR.END.RATIO.RATIO.INCOMES.AKG2` | `FsGaYearEndRatio_RatioIncomesAkg2` | TField |  | This field displays the year end ratio balance of ordinary income accounts for equity related instruments(AKG2) Multifonds DB Column is PER_I_AKG2. |
| 12 | `FS.GA.YEAR.END.RATIO.RATIO.PROFIT.OR.LOSS.AKG2` | `FsGaYearEndRatio_RatioProfitOrLossAkg2` | TField |  | This field displays the year end ratio balance of realized profit or loss results of equity related instruments(AKG2) Multifonds DB Column is PER_P_AKG2. |
| 13 | `FS.GA.YEAR.END.RATIO.INCOMES.AKG4` | `FsGaYearEndRatio_IncomesAkg4` | TField |  | This field displays the general ledger balance of ordinary income accounts of equity related instruments(AKG4) for calculating year end ratios Multifonds DB Column is MONTANT_I_AKG4. |
| 14 | `FS.GA.YEAR.END.RATIO.PROFIT.OR.LOSS.AKG4` | `FsGaYearEndRatio_ProfitOrLossAkg4` | TField |  | This field displays the general ledger balance of realized profit or loss results accounts of equity related instruments(AKG4) for calculating year end ratios Multifonds DB Column is MONTANT_P_AKG4. |
| 15 | `FS.GA.YEAR.END.RATIO.RATIO.INCOMES.AKG4` | `FsGaYearEndRatio_RatioIncomesAkg4` | TField |  | This field displays the year end ratio balance of ordinary income accounts for equity related instruments(AKG4) Multifonds DB Column is PER_I_AKG4. |
| 16 | `FS.GA.YEAR.END.RATIO.RATIO.PROFIT.OR.LOSS.AKG4` | `FsGaYearEndRatio_RatioProfitOrLossAkg4` | TField |  | This field displays the year end ratio balance of realized profit or loss results of equity related instruments(AKG4) Multifonds DB Column is PER_P_AKG4. |
| 17 | `FS.GA.YEAR.END.RATIO.MIGRATE.OR.YEAR.END` | `FsGaYearEndRatio_MigrateOrYearEnd` | TField |  | This field displays migrate or yearend flag Multifonds DB Column is YND_EXP_ALLOC. |
| 18 | `FS.GA.YEAR.END.RATIO.INCOMES.TG1` | `FsGaYearEndRatio_IncomesTg1` | TField |  | This field displays the general ledger balance of ordinary income accounts of TG1 for calculating year end ratios Multifonds DB Column is MONTANT_I_AKG2_TG1. |
| 19 | `FS.GA.YEAR.END.RATIO.PROFIT.OR.LOSS.TG1` | `FsGaYearEndRatio_ProfitOrLossTg1` | TField |  | This field displays the general ledger balance of realized profit or loss results accounts of TG1 for calculating year end ratios Multifonds DB Column is MONTANT_P_AKG2_TG1. |
| 20 | `FS.GA.YEAR.END.RATIO.RATIO.INCOMES.TG1` | `FsGaYearEndRatio_RatioIncomesTg1` | TField |  | This field displays the year end ratio balance of ordinary income accounts of TG1 Multifonds DB Column is PER_I_AKG2_TG1. |
| 21 | `FS.GA.YEAR.END.RATIO.RATIO.PROFIT.OR.LOSS.TG1` | `FsGaYearEndRatio_RatioProfitOrLossTg1` | TField |  | This field displays the year end ratio balance of realized profit or loss results of TG1 Multifonds DB Column is PER_P_AKG2_TG1. |
| 22 | `FS.GA.YEAR.END.RATIO.INCOMES.TG2` | `FsGaYearEndRatio_IncomesTg2` | TField |  | This field displays the general ledger balance of ordinary income accounts of TG2 for calculating year end ratios Multifonds DB Column is MONTANT_I_AKG2_TG2. |
| 23 | `FS.GA.YEAR.END.RATIO.PROFIT.OR.LOSS.TG2` | `FsGaYearEndRatio_ProfitOrLossTg2` | TField |  | This field displays the general ledger balance of realized profit or loss results accounts of TG2 for calculating year end ratios Multifonds DB Column is MONTANT_P_AKG2_TG2. |
| 24 | `FS.GA.YEAR.END.RATIO.RATIO.INCOMES.TG2` | `FsGaYearEndRatio_RatioIncomesTg2` | TField |  | This field displays the year end ratio balance of ordinary income accounts of TG2 Multifonds DB Column is PER_I_AKG2_TG2. |
| 25 | `FS.GA.YEAR.END.RATIO.RATIO.PROFIT.OR.LOSS.TG2` | `FsGaYearEndRatio_RatioProfitOrLossTg2` | TField |  | This field displays the year end ratio balance of realized profit or loss results of TG2 Multifonds DB Column is PER_P_AKG2_TG2. |
| 26 | `FS.GA.YEAR.END.RATIO.INCOMES.TG3` | `FsGaYearEndRatio_IncomesTg3` | TField |  | This field displays the general ledger balance of ordinary income accounts of TG3 for calculating year end ratios Multifonds DB Column is MONTANT_I_AKG2_TG3. |
| 27 | `FS.GA.YEAR.END.RATIO.PROFIT.OR.LOSS.TG3` | `FsGaYearEndRatio_ProfitOrLossTg3` | TField |  | This field displays the general ledger balance of realized profit or loss results accounts of TG3 for calculating year end ratios Multifonds DB Column is MONTANT_P_AKG2_TG3. |
| 28 | `FS.GA.YEAR.END.RATIO.RATIO.INCOMES.TG3` | `FsGaYearEndRatio_RatioIncomesTg3` | TField |  | This field displays the year end ratio balance of ordinary income accounts of TG3 Multifonds DB Column is PER_I_AKG2_TG3. |
| 29 | `FS.GA.YEAR.END.RATIO.RATIO.PROFIT.OR.LOSS.TG3` | `FsGaYearEndRatio_RatioProfitOrLossTg3` | TField |  | This field displays the year end ratio balance of realized profit or loss results of TG3 Multifonds DB Column is PER_P_AKG2_TG3. |
| 30 | `FS.GA.YEAR.END.RATIO.RESERVED10` | `FsGaYearEndRatio_Reserved10` | TField |  |  |
| 31 | `FS.GA.YEAR.END.RATIO.RESERVED9` | `FsGaYearEndRatio_Reserved9` | TField |  |  |
| 32 | `FS.GA.YEAR.END.RATIO.RESERVED8` | `FsGaYearEndRatio_Reserved8` | TField |  |  |
| 33 | `FS.GA.YEAR.END.RATIO.RESERVED7` | `FsGaYearEndRatio_Reserved7` | TField |  |  |
| 34 | `FS.GA.YEAR.END.RATIO.RESERVED6` | `FsGaYearEndRatio_Reserved6` | TField |  |  |
| 35 | `FS.GA.YEAR.END.RATIO.RESERVED5` | `FsGaYearEndRatio_Reserved5` | TField |  |  |
| 36 | `FS.GA.YEAR.END.RATIO.RESERVED4` | `FsGaYearEndRatio_Reserved4` | TField |  |  |
| 37 | `FS.GA.YEAR.END.RATIO.RESERVED3` | `FsGaYearEndRatio_Reserved3` | TField |  |  |
| 38 | `FS.GA.YEAR.END.RATIO.RESERVED2` | `FsGaYearEndRatio_Reserved2` | TField |  |  |
| 39 | `FS.GA.YEAR.END.RATIO.RESERVED1` | `FsGaYearEndRatio_Reserved1` | TField |  |  |
| 40 | `FS.GA.YEAR.END.RATIO.RECORD.STATUS` | `FsGaYearEndRatio_RecordStatus` | String |  |  |
| 41 | `FS.GA.YEAR.END.RATIO.CURR.NO` | `FsGaYearEndRatio_CurrNo` | String |  |  |
| 42 | `FS.GA.YEAR.END.RATIO.INPUTTER` | `FsGaYearEndRatio_Inputter` |  |  |  |
| 43 | `FS.GA.YEAR.END.RATIO.DATE.TIME` | `FsGaYearEndRatio_DateTime` |  |  |  |
| 44 | `FS.GA.YEAR.END.RATIO.AUTHORISER` | `FsGaYearEndRatio_Authoriser` | String |  |  |
| 45 | `FS.GA.YEAR.END.RATIO.CO.CODE` | `FsGaYearEndRatio_CoCode` | String |  |  |
| 46 | `FS.GA.YEAR.END.RATIO.DEPT.CODE` | `FsGaYearEndRatio_DeptCode` | String |  |  |
| 47 | `FS.GA.YEAR.END.RATIO.AUDITOR.CODE` | `FsGaYearEndRatio_AuditorCode` | String |  |  |
| 48 | `FS.GA.YEAR.END.RATIO.AUDIT.DATE.TIME` | `FsGaYearEndRatio_AuditDateTime` | String |  |  |
