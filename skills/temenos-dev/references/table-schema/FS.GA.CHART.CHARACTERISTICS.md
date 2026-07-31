# FS.GA.CHART.CHARACTERISTICS — Table Schema

> Source: `INSERTS/I_F.FS.GA.CHART.CHARACTERISTICS` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHART.CHARACTERISTICS.CHART` | `FsGaChartCharacteristics_Chart` | TField |  | Chart Multifonds DB Column is CPDC. |
| 2 | `CHART.CHARACTERISTICS.GL.ACCOUNT.SUFFIX` | `FsGaChartCharacteristics_SuffixNumber` |  |  |  |
| 3 | `CHART.CHARACTERISTICS.ISSUE.COUNTRY` | `FsGaChartCharacteristics_CountryCode` |  |  |  |
| 4 | `CHART.CHARACTERISTICS.LOCAL.TYPE` | `FsGaChartCharacteristics_LocalType` | TField |  | Local type Multifonds DB Column is COTLOCALE. |
| 5 | `CHART.CHARACTERISTICS.HEDGING.TRADING` | `FsGaChartCharacteristics_HedgingTrading` | TField |  | Hedging Trading Multifonds DB Column is CD_HEDG. |
| 6 | `CHART.CHARACTERISTICS.SECURITY.TYPE` | `FsGaChartCharacteristics_SecurityType` | TField |  | Security type Multifonds DB Column is CGTI. |
| 7 | `CHART.CHARACTERISTICS.GF.NON.GF` | `FsGaChartCharacteristics_GfNonGf` | TField |  | GF Non GF Multifonds DB Column is GDF_TISR. |
| 8 | `CHART.CHARACTERISTICS.DESCRIPTION.CODE` | `FsGaChartCharacteristics_DescriptionCode` | TField |  | Description code Multifonds DB Column is CODE_LIB. |
| 9 | `CHART.CHARACTERISTICS.AGIO.DISAGIO` | `FsGaChartCharacteristics_AgioDisagio` | TField |  | Agio Disagio Multifonds DB Column is FLG_KEST. |
| 10 | `CHART.CHARACTERISTICS.FINANCIAL.INNOVATION` | `FsGaChartCharacteristics_FinancialInnovation` | TField |  | Financial Innovation Multifonds DB Column is FLG_IP. |
| 11 | `CHART.CHARACTERISTICS.TRUST` | `FsGaChartCharacteristics_Trust` | TField |  | Trust Multifonds DB Column is CODE_TRUST. |
| 12 | `CHART.CHARACTERISTICS.UK.TAX` | `FsGaChartCharacteristics_UkTax` | TField |  | UK Tax Multifonds DB Column is FLG_TAX. |
| 13 | `CHART.CHARACTERISTICS.RECORD.STATUS` | `FsGaChartCharacteristics_RecordStatus` | String |  |  |
| 14 | `CHART.CHARACTERISTICS.CURR.NO` | `FsGaChartCharacteristics_CurrNo` | String |  |  |
| 15 | `CHART.CHARACTERISTICS.INPUTTER` | `FsGaChartCharacteristics_Inputter` |  |  |  |
| 16 | `CHART.CHARACTERISTICS.DATE.TIME` | `FsGaChartCharacteristics_DateTime` |  |  |  |
| 17 | `CHART.CHARACTERISTICS.AUTHORISER` | `FsGaChartCharacteristics_Authoriser` | String |  |  |
| 18 | `CHART.CHARACTERISTICS.CO.CODE` | `FsGaChartCharacteristics_CoCode` | String |  |  |
| 19 | `CHART.CHARACTERISTICS.DEPT.CODE` | `FsGaChartCharacteristics_DeptCode` | String |  |  |
| 20 | `CHART.CHARACTERISTICS.AUDITOR.CODE` | `FsGaChartCharacteristics_AuditorCode` | String |  |  |
| 21 | `CHART.CHARACTERISTICS.AUDIT.DATE.TIME` | `FsGaChartCharacteristics_AuditDateTime` | String |  |  |
