# FS.GA.CHART.CHARACTERISTICS.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.CHART.CHARACTERISTICS.DETAIL` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.CHART.CHARACTERISTICS.DETAIL.CHART.OF.ACCOUNTS.CODE` | `FsGaChartCharacteristicsDetail_ChartOfAccountsNumber` |  |  |  |
| 2 | `GA.CHART.CHARACTERISTICS.DETAIL.GL.ACCOUNT.SUFFIX` | `FsGaChartCharacteristicsDetail_SuffixNumber` |  |  |  |
| 3 | `GA.CHART.CHARACTERISTICS.DETAIL.LOCAL.CURRENCY` | `FsGaChartCharacteristicsDetail_Currency` |  |  |  |
| 4 | `GA.CHART.CHARACTERISTICS.DETAIL.LOCALE.TYPE` | `FsGaChartCharacteristicsDetail_LocaleType` | TField |  | Local Type of granular information to query in Chart Charesteric screen Multifonds DB Column is COTLOCALE. |
| 5 | `GA.CHART.CHARACTERISTICS.DETAIL.HEDGING.OR.TRADING.CATEGORY` | `FsGaChartCharacteristicsDetail_HedgingOrTradingCategory` | TField |  | Hedging or Trading Category Multifonds DB Column is CD_HEDG. |
| 6 | `GA.CHART.CHARACTERISTICS.DETAIL.GTI.CODE` | `FsGaChartCharacteristicsDetail_Gti` |  |  |  |
| 7 | `GA.CHART.CHARACTERISTICS.DETAIL.GRAND.FATHER.OR.TIS.REPORTING` | `FsGaChartCharacteristicsDetail_GrandFatherOrTisReporting` | TField |  | Grand Father or Non Grand Father i.e TIS Reporting applicable Multifonds DB Column is GDF_TISR. |
| 8 | `GA.CHART.CHARACTERISTICS.DETAIL.DESCRIPTION.CODE` | `FsGaChartCharacteristicsDetail_DescriptionCode` | TField |  | Description Code Multifonds DB Column is CODE_LIB. |
| 9 | `GA.CHART.CHARACTERISTICS.DETAIL.KEST` | `FsGaChartCharacteristicsDetail_Kest` | TField |  | If Set, Austrian KEST will be calculated for the underlying share class Multifonds DB Column is FLG_KEST. |
| 10 | `GA.CHART.CHARACTERISTICS.DETAIL.INTERIM.PROFIT.FLAG` | `FsGaChartCharacteristicsDetail_InterimProfitFlag` | TField |  | Flag for IP(Interim Profit) Multifonds DB Column is FLG_IP. |
| 11 | `GA.CHART.CHARACTERISTICS.DETAIL.TRUST.CODE` | `FsGaChartCharacteristicsDetail_TrustCode` | TField |  | Third party Trust Identification Code Multifonds DB Column is CODE_TRUST. |
| 12 | `GA.CHART.CHARACTERISTICS.DETAIL.UK.TAX` | `FsGaChartCharacteristicsDetail_UkTax` | TField |  | This field is to enable UK Bond Tax or UK Capital Gain Tax Multifonds DB Column is FLG_TAX. |
| 13 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED10` | `FsGaChartCharacteristicsDetail_Reserved10` | TField |  |  |
| 14 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED9` | `FsGaChartCharacteristicsDetail_Reserved9` | TField |  |  |
| 15 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED8` | `FsGaChartCharacteristicsDetail_Reserved8` | TField |  |  |
| 16 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED7` | `FsGaChartCharacteristicsDetail_Reserved7` | TField |  |  |
| 17 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED6` | `FsGaChartCharacteristicsDetail_Reserved6` | TField |  |  |
| 18 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED5` | `FsGaChartCharacteristicsDetail_Reserved5` | TField |  |  |
| 19 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED4` | `FsGaChartCharacteristicsDetail_Reserved4` | TField |  |  |
| 20 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED3` | `FsGaChartCharacteristicsDetail_Reserved3` | TField |  |  |
| 21 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED2` | `FsGaChartCharacteristicsDetail_Reserved2` | TField |  |  |
| 22 | `GA.CHART.CHARACTERISTICS.DETAIL.RESERVED1` | `FsGaChartCharacteristicsDetail_Reserved1` | TField |  |  |
| 23 | `GA.CHART.CHARACTERISTICS.DETAIL.RECORD.STATUS` | `FsGaChartCharacteristicsDetail_RecordStatus` | String |  |  |
| 24 | `GA.CHART.CHARACTERISTICS.DETAIL.CURR.NO` | `FsGaChartCharacteristicsDetail_CurrNo` | String |  |  |
| 25 | `GA.CHART.CHARACTERISTICS.DETAIL.INPUTTER` | `FsGaChartCharacteristicsDetail_Inputter` |  |  |  |
| 26 | `GA.CHART.CHARACTERISTICS.DETAIL.DATE.TIME` | `FsGaChartCharacteristicsDetail_DateTime` |  |  |  |
| 27 | `GA.CHART.CHARACTERISTICS.DETAIL.AUTHORISER` | `FsGaChartCharacteristicsDetail_Authoriser` | String |  |  |
| 28 | `GA.CHART.CHARACTERISTICS.DETAIL.CO.CODE` | `FsGaChartCharacteristicsDetail_CoCode` | String |  |  |
| 29 | `GA.CHART.CHARACTERISTICS.DETAIL.DEPT.CODE` | `FsGaChartCharacteristicsDetail_DeptCode` | String |  |  |
| 30 | `GA.CHART.CHARACTERISTICS.DETAIL.AUDITOR.CODE` | `FsGaChartCharacteristicsDetail_AuditorCode` | String |  |  |
| 31 | `GA.CHART.CHARACTERISTICS.DETAIL.AUDIT.DATE.TIME` | `FsGaChartCharacteristicsDetail_AuditDateTime` | String |  |  |
