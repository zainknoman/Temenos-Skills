# EB.DATA.MODULE.LIST — Table Schema

> Source: `INSERTS/I_F.EB.DATA.MODULE.LIST` in `EB_Upgrade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MOD.LST.DESCRIPTION` | `EbDataModuleList_Description` | TField |  |  |
| 2 | `MOD.LST.MODULE.LIST` | `EbDataModuleList_ModuleList` |  |  |  |
| 3 | `MOD.LST.RESERVED.05` | `EbDataModuleList_Reserved05` | TField |  |  |
| 4 | `MOD.LST.RESERVED.04` | `EbDataModuleList_Reserved04` | TField |  |  |
| 5 | `MOD.LST.RESERVED.03` | `EbDataModuleList_Reserved03` | TField |  |  |
| 6 | `MOD.LST.RESERVED.02` | `EbDataModuleList_Reserved02` | TField |  |  |
| 7 | `MOD.LST.RESERVED.01` | `EbDataModuleList_Reserved01` | TField |  |  |
| 8 | `MOD.LST.RECORD.STATUS` | `EbDataModuleList_RecordStatus` | String |  |  |
| 9 | `MOD.LST.CURR.NO` | `EbDataModuleList_CurrNo` | String |  |  |
| 10 | `MOD.LST.INPUTTER` | `EbDataModuleList_Inputter` |  |  |  |
| 11 | `MOD.LST.DATE.TIME` | `EbDataModuleList_DateTime` |  |  |  |
| 12 | `MOD.LST.AUTHORISER` | `EbDataModuleList_Authoriser` | String |  |  |
| 13 | `MOD.LST.CO.CODE` | `EbDataModuleList_CoCode` | String |  |  |
| 14 | `MOD.LST.DEPT.CODE` | `EbDataModuleList_DeptCode` | String |  |  |
| 15 | `MOD.LST.AUDITOR.CODE` | `EbDataModuleList_AuditorCode` | String |  |  |
| 16 | `MOD.LST.AUDIT.DATE.TIME` | `EbDataModuleList_AuditDateTime` | String |  |  |
