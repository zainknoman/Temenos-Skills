# EB.DATA.RELEASE.API.TABLE — Table Schema

> Source: `INSERTS/I_F.EB.DATA.RELEASE.API.TABLE` in `EB_Upgrade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DAR.API.DESC` | `EbDataReleaseApiTable_ApiDesc` |  |  |  |
| 2 | `EB.DAR.RELEASE.API` | `EbDataReleaseApiTable_ReleaseApi` | TField |  |  |
| 7 | `EB.DAR.RESERVED.10` | `EbDataReleaseApiTable_Reserved10` | TField |  |  |
| 8 | `EB.DAR.RESERVED.09` | `EbDataReleaseApiTable_Reserved09` | TField |  |  |
| 9 | `EB.DAR.RESERVED.08` | `EbDataReleaseApiTable_Reserved08` | TField |  |  |
| 10 | `EB.DAR.RESERVED.07` | `EbDataReleaseApiTable_Reserved07` | TField |  |  |
| 11 | `EB.DAR.RESERVED.06` | `EbDataReleaseApiTable_Reserved06` | TField |  |  |
| 12 | `EB.DAR.RESERVED.05` | `EbDataReleaseApiTable_Reserved05` | TField |  |  |
| 13 | `EB.DAR.RESERVED.04` | `EbDataReleaseApiTable_Reserved04` | TField |  |  |
| 14 | `EB.DAR.RESERVED.03` | `EbDataReleaseApiTable_Reserved03` | TField |  |  |
| 15 | `EB.DAR.RESERVED.02` | `EbDataReleaseApiTable_Reserved02` | TField |  |  |
| 16 | `EB.DAR.RESERVED.01` | `EbDataReleaseApiTable_Reserved01` | TField |  |  |
| 17 | `EB.DAR.RECORD.STATUS` | `EbDataReleaseApiTable_RecordStatus` | String |  |  |
| 18 | `EB.DAR.CURR.NO` | `EbDataReleaseApiTable_CurrNo` | String |  |  |
| 19 | `EB.DAR.INPUTTER` | `EbDataReleaseApiTable_Inputter` |  |  |  |
| 20 | `EB.DAR.DATE.TIME` | `EbDataReleaseApiTable_DateTime` |  |  |  |
| 21 | `EB.DAR.AUTHORISER` | `EbDataReleaseApiTable_Authoriser` | String |  |  |
| 22 | `EB.DAR.CO.CODE` | `EbDataReleaseApiTable_CoCode` | String |  |  |
| 23 | `EB.DAR.DEPT.CODE` | `EbDataReleaseApiTable_DeptCode` | String |  |  |
| 24 | `EB.DAR.AUDITOR.CODE` | `EbDataReleaseApiTable_AuditorCode` | String |  |  |
| 25 | `EB.DAR.AUDIT.DATE.TIME` | `EbDataReleaseApiTable_AuditDateTime` | String |  |  |
