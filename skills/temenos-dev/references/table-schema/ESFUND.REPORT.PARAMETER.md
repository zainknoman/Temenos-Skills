# ESFUND.REPORT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ESFUND.REPORT.PARAMETER` in `ESFUND_DailyBrokerOrderReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.ERP.OUR.BANK.ID` | `EsfundReportParameter_OurBankId` | TField |  |  |
| 2 | `ES.ERP.ASSET.TYPE` | `EsfundReportParameter_AssetType` |  |  |  |
| 3 | `ES.ERP.SUB.ASSET.TYPE` | `EsfundReportParameter_SubAssetType` |  |  |  |
| 4 | `ES.ERP.LOCAL.REF` | `EsfundReportParameter_LocalRef` |  |  |  |
| 5 | `ES.ERP.RESERVED.1` | `EsfundReportParameter_Reserved1` | TField |  |  |
| 6 | `ES.ERP.RESERVED.2` | `EsfundReportParameter_Reserved2` | TField |  |  |
| 7 | `ES.ERP.RESERVED.3` | `EsfundReportParameter_Reserved3` | TField |  |  |
| 8 | `ES.ERP.RESERVED.4` | `EsfundReportParameter_Reserved4` | TField |  |  |
| 9 | `ES.ERP.RESERVED.5` | `EsfundReportParameter_Reserved5` | TField |  |  |
| 10 | `ES.ERP.RESERVED.6` | `EsfundReportParameter_Reserved6` | TField |  |  |
| 11 | `ES.ERP.RESERVED.7` | `EsfundReportParameter_Reserved7` | TField |  |  |
| 12 | `ES.ERP.RESERVED.8` | `EsfundReportParameter_Reserved8` | TField |  |  |
| 13 | `ES.ERP.RESERVED.9` | `EsfundReportParameter_Reserved9` | TField |  |  |
| 14 | `ES.ERP.RESERVED.10` | `EsfundReportParameter_Reserved10` | TField |  |  |
| 15 | `ES.ERP.OVERRIDE` | `EsfundReportParameter_Override` |  |  |  |
| 16 | `ES.ERP.RECORD.STATUS` | `EsfundReportParameter_RecordStatus` | String |  |  |
| 17 | `ES.ERP.CURR.NO` | `EsfundReportParameter_CurrNo` | String |  |  |
| 18 | `ES.ERP.INPUTTER` | `EsfundReportParameter_Inputter` |  |  |  |
| 19 | `ES.ERP.DATE.TIME` | `EsfundReportParameter_DateTime` |  |  |  |
| 20 | `ES.ERP.AUTHORISER` | `EsfundReportParameter_Authoriser` | String |  |  |
| 21 | `ES.ERP.CO.CODE` | `EsfundReportParameter_CoCode` | String |  |  |
| 22 | `ES.ERP.DEPT.CODE` | `EsfundReportParameter_DeptCode` | String |  |  |
| 23 | `ES.ERP.AUDITOR.CODE` | `EsfundReportParameter_AuditorCode` | String |  |  |
| 24 | `ES.ERP.AUDIT.DATE.TIME` | `EsfundReportParameter_AuditDateTime` | String |  |  |
