# CZ.CDP.PDD.BUILD.REQUEST — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.PDD.BUILD.REQUEST` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CPBR.DESCRIPTION` | `CzCdpPddBuildRequest_Description` |  |  |  |
| 2 | `CZ.CPBR.REBUILD.ALL.PRDTS` | `CzCdpPddBuildRequest_RebuildAllPrdts` | TField |  |  |
| 3 | `CZ.CPBR.REBUILD.PRODUCT` | `CzCdpPddBuildRequest_RebuildProduct` |  |  |  |
| 4 | `CZ.CPBR.REBUILD.APPLICATION` | `CzCdpPddBuildRequest_RebuildApplication` |  |  |  |
| 5 | `CZ.CPBR.CLEAR.EXISTING.PDD` | `CzCdpPddBuildRequest_ClearExistingPdd` | TField |  |  |
| 6 | `CZ.CPBR.DATE.PROCESSED` | `CzCdpPddBuildRequest_DateProcessed` | TField |  |  |
| 7 | `CZ.CPBR.RESERVED.05` | `CzCdpPddBuildRequest_Reserved05` | TField |  |  |
| 8 | `CZ.CPBR.RESERVED.04` | `CzCdpPddBuildRequest_Reserved04` | TField |  |  |
| 9 | `CZ.CPBR.RESERVED.03` | `CzCdpPddBuildRequest_Reserved03` | TField |  |  |
| 10 | `CZ.CPBR.RESERVED.02` | `CzCdpPddBuildRequest_Reserved02` | TField |  |  |
| 11 | `CZ.CPBR.RESERVED.01` | `CzCdpPddBuildRequest_Reserved01` | TField |  |  |
| 12 | `CZ.CPBR.RECORD.STATUS` | `CzCdpPddBuildRequest_RecordStatus` | String |  |  |
| 13 | `CZ.CPBR.CURR.NO` | `CzCdpPddBuildRequest_CurrNo` | String |  |  |
| 14 | `CZ.CPBR.INPUTTER` | `CzCdpPddBuildRequest_Inputter` |  |  |  |
| 15 | `CZ.CPBR.DATE.TIME` | `CzCdpPddBuildRequest_DateTime` |  |  |  |
| 16 | `CZ.CPBR.AUTHORISER` | `CzCdpPddBuildRequest_Authoriser` | String |  |  |
| 17 | `CZ.CPBR.CO.CODE` | `CzCdpPddBuildRequest_CoCode` | String |  |  |
| 18 | `CZ.CPBR.DEPT.CODE` | `CzCdpPddBuildRequest_DeptCode` | String |  |  |
| 19 | `CZ.CPBR.AUDITOR.CODE` | `CzCdpPddBuildRequest_AuditorCode` | String |  |  |
| 20 | `CZ.CPBR.AUDIT.DATE.TIME` | `CzCdpPddBuildRequest_AuditDateTime` | String |  |  |
