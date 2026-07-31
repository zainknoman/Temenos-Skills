# EB.USAGE.STATISTICS — Table Schema

> Source: `INSERTS/I_F.EB.USAGE.STATISTICS` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.USG.IN.API.ID` | `EbUsageStatistics_InApiId` |  |  |  |
| 2 | `EB.USG.IN.OPER` | `EbUsageStatistics_InOper` |  |  |  |
| 3 | `EB.USG.IN.URL.INFO` | `EbUsageStatistics_InUrlInfo` |  |  |  |
| 4 | `EB.USG.IN.OPER.COUNT` | `EbUsageStatistics_InOperCount` |  |  |  |
| 5 | `EB.USG.RESERVED.10` | `EbUsageStatistics_Reserved10` |  |  |  |
| 6 | `EB.USG.RESERVED.9` | `EbUsageStatistics_Reserved9` |  |  |  |
| 7 | `EB.USG.RESERVED.8` | `EbUsageStatistics_Reserved8` |  |  |  |
| 8 | `EB.USG.RESERVED.7` | `EbUsageStatistics_Reserved7` |  |  |  |
| 9 | `EB.USG.RESERVED.6` | `EbUsageStatistics_Reserved6` |  |  |  |
| 10 | `EB.USG.RESERVED.5` | `EbUsageStatistics_Reserved5` |  |  |  |
| 11 | `EB.USG.RESERVED.4` | `EbUsageStatistics_Reserved4` |  |  |  |
| 12 | `EB.USG.RESERVED.3` | `EbUsageStatistics_Reserved3` |  |  |  |
| 13 | `EB.USG.RESERVED.2` | `EbUsageStatistics_Reserved2` |  |  |  |
| 14 | `EB.USG.RESERVED.1` | `EbUsageStatistics_Reserved1` |  |  |  |
| 15 | `EB.USG.IN.API.COUNT` | `EbUsageStatistics_InApiCount` |  |  |  |
| 16 | `EB.USG.API.ID` | `EbUsageStatistics_ApiId` |  |  |  |
| 17 | `EB.USG.OPERATION` | `EbUsageStatistics_Operation` |  |  |  |
| 18 | `EB.USG.URL.INFO` | `EbUsageStatistics_UrlInfo` |  |  |  |
| 19 | `EB.USG.OPER.COUNT` | `EbUsageStatistics_OperCount` |  |  |  |
| 20 | `EB.USG.RESERVED.20` | `EbUsageStatistics_Reserved20` |  |  |  |
| 21 | `EB.USG.RESERVED.19` | `EbUsageStatistics_Reserved19` |  |  |  |
| 22 | `EB.USG.RESERVED.18` | `EbUsageStatistics_Reserved18` |  |  |  |
| 23 | `EB.USG.RESERVED.17` | `EbUsageStatistics_Reserved17` |  |  |  |
| 24 | `EB.USG.RESERVED.16` | `EbUsageStatistics_Reserved16` |  |  |  |
| 25 | `EB.USG.RESERVED.15` | `EbUsageStatistics_Reserved15` |  |  |  |
| 26 | `EB.USG.RESERVED.14` | `EbUsageStatistics_Reserved14` |  |  |  |
| 27 | `EB.USG.RESERVED.13` | `EbUsageStatistics_Reserved13` |  |  |  |
| 28 | `EB.USG.RESERVED.12` | `EbUsageStatistics_Reserved12` |  |  |  |
| 29 | `EB.USG.RESERVED.11` | `EbUsageStatistics_Reserved11` |  |  |  |
| 30 | `EB.USG.API.COUNT` | `EbUsageStatistics_ApiCount` |  |  |  |
| 31 | `EB.USG.MODULE` | `EbUsageStatistics_Module` |  |  |  |
| 32 | `EB.USG.TARGET` | `EbUsageStatistics_Target` |  |  |  |
| 33 | `EB.USG.TARGET.COUNT` | `EbUsageStatistics_TargetCount` |  |  |  |
| 34 | `EB.USG.RESERVED.30` | `EbUsageStatistics_Reserved30` |  |  |  |
| 35 | `EB.USG.RESERVED.29` | `EbUsageStatistics_Reserved29` |  |  |  |
| 36 | `EB.USG.RESERVED.28` | `EbUsageStatistics_Reserved28` |  |  |  |
| 37 | `EB.USG.RESERVED.27` | `EbUsageStatistics_Reserved27` |  |  |  |
| 38 | `EB.USG.RESERVED.26` | `EbUsageStatistics_Reserved26` |  |  |  |
| 39 | `EB.USG.RESERVED.25` | `EbUsageStatistics_Reserved25` |  |  |  |
| 40 | `EB.USG.RESERVED.24` | `EbUsageStatistics_Reserved24` |  |  |  |
| 41 | `EB.USG.RESERVED.23` | `EbUsageStatistics_Reserved23` |  |  |  |
| 42 | `EB.USG.RESERVED.22` | `EbUsageStatistics_Reserved22` |  |  |  |
| 43 | `EB.USG.RESERVED.21` | `EbUsageStatistics_Reserved21` |  |  |  |
| 44 | `EB.USG.MODULE.COUNT` | `EbUsageStatistics_ModuleCount` |  |  |  |
| 45 | `EB.USG.METRIC.TYPE` | `EbUsageStatistics_MetricType` |  |  |  |
| 46 | `EB.USG.METRIC.UNIT` | `EbUsageStatistics_MetricUnit` |  |  |  |
| 47 | `EB.USG.IF.EVENT.TYPE` | `EbUsageStatistics_IfEventType` |  |  |  |
| 48 | `EB.USG.IF.EVENT.COUNT` | `EbUsageStatistics_IfEventCount` |  |  |  |
| 49 | `EB.USG.RESERVED.36` | `EbUsageStatistics_Reserved36` |  |  |  |
| 50 | `EB.USG.RESERVED.35` | `EbUsageStatistics_Reserved35` | TField |  |  |
| 51 | `EB.USG.RESERVED.34` | `EbUsageStatistics_Reserved34` | TField |  |  |
| 52 | `EB.USG.RESERVED.33` | `EbUsageStatistics_Reserved33` | TField |  |  |
| 53 | `EB.USG.RESERVED.32` | `EbUsageStatistics_Reserved32` | TField |  |  |
| 54 | `EB.USG.RESERVED.31` | `EbUsageStatistics_Reserved31` | TField |  |  |
| 55 | `EB.USG.RECORD.STATUS` | `EbUsageStatistics_RecordStatus` | String |  |  |
| 56 | `EB.USG.CURR.NO` | `EbUsageStatistics_CurrNo` | String |  |  |
| 57 | `EB.USG.INPUTTER` | `EbUsageStatistics_Inputter` |  |  |  |
| 58 | `EB.USG.DATE.TIME` | `EbUsageStatistics_DateTime` |  |  |  |
| 59 | `EB.USG.AUTHORISER` | `EbUsageStatistics_Authoriser` | String |  |  |
| 60 | `EB.USG.CO.CODE` | `EbUsageStatistics_CoCode` | String |  |  |
| 61 | `EB.USG.DEPT.CODE` | `EbUsageStatistics_DeptCode` | String |  |  |
| 62 | `EB.USG.AUDITOR.CODE` | `EbUsageStatistics_AuditorCode` | String |  |  |
| 63 | `EB.USG.AUDIT.DATE.TIME` | `EbUsageStatistics_AuditDateTime` | String |  |  |
