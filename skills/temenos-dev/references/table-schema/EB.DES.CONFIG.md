# EB.DES.CONFIG — Table Schema

> Source: `INSERTS/I_F.EB.DES.CONFIG` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DES.PROPERTY.KEY` | `EbDesConfig_PropertyKey` |  |  |  |
| 2 | `EB.DES.PROPERTY.VALUE` | `EbDesConfig_PropertyValue` |  |  |  |
| 3 | `EB.DES.RESERVED.10` | `EbDesConfig_Reserved10` | TField |  |  |
| 4 | `EB.DES.RESERVED.9` | `EbDesConfig_Reserved9` | TField |  |  |
| 5 | `EB.DES.RESERVED.8` | `EbDesConfig_Reserved8` | TField |  |  |
| 6 | `EB.DES.RESERVED.7` | `EbDesConfig_Reserved7` | TField |  |  |
| 7 | `EB.DES.RESERVED.6` | `EbDesConfig_Reserved6` | TField |  |  |
| 8 | `EB.DES.RESERVED.5` | `EbDesConfig_Reserved5` | TField |  |  |
| 9 | `EB.DES.RESERVED.4` | `EbDesConfig_Reserved4` | TField |  |  |
| 10 | `EB.DES.RESERVED.3` | `EbDesConfig_Reserved3` | TField |  |  |
| 11 | `EB.DES.RESERVED.2` | `EbDesConfig_Reserved2` | TField |  |  |
| 12 | `EB.DES.RESERVED.1` | `EbDesConfig_Reserved1` | TField |  |  |
| 13 | `EB.DES.RECORD.STATUS` | `EbDesConfig_RecordStatus` | String |  |  |
| 14 | `EB.DES.CURR.NO` | `EbDesConfig_CurrNo` | String |  |  |
| 15 | `EB.DES.INPUTTER` | `EbDesConfig_Inputter` |  |  |  |
| 16 | `EB.DES.DATE.TIME` | `EbDesConfig_DateTime` |  |  |  |
| 17 | `EB.DES.AUTHORISER` | `EbDesConfig_Authoriser` | String |  |  |
| 18 | `EB.DES.CO.CODE` | `EbDesConfig_CoCode` | String |  |  |
| 19 | `EB.DES.DEPT.CODE` | `EbDesConfig_DeptCode` | String |  |  |
| 20 | `EB.DES.AUDITOR.CODE` | `EbDesConfig_AuditorCode` | String |  |  |
| 21 | `EB.DES.AUDIT.DATE.TIME` | `EbDesConfig_AuditDateTime` | String |  |  |
