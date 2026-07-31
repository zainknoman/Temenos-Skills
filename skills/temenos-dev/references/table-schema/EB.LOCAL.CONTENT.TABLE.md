# EB.LOCAL.CONTENT.TABLE — Table Schema

> Source: `INSERTS/I_F.EB.LOCAL.CONTENT.TABLE` in `EB_LocalContent.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.LCT.LOCAL.CONTENT.FLD` | `EbLocalContentTable_LocalContentFld` |  |  |  |
| 2 | `EB.LCT.LOCAL.CONTENT.STATUS` | `EbLocalContentTable_LocalContentStatus` |  |  |  |
| 3 | `EB.LCT.MASTER.COMPANY.FLD` | `EbLocalContentTable_MasterCompanyFld` | TField |  |  |
| 4 | `EB.LCT.REBUILD.LCT.FLDS` | `EbLocalContentTable_RebuildLctFlds` | TField |  |  |
| 5 | `EB.LCT.FIELD.TYPE` | `EbLocalContentTable_FieldType` | TField |  |  |
| 6 | `EB.LCT.FIELD.POSITION` | `EbLocalContentTable_FieldPosition` | TField |  |  |
| 7 | `EB.LCT.RESERVED.10` | `EbLocalContentTable_Reserved10` | TField |  |  |
| 8 | `EB.LCT.RESERVED.09` | `EbLocalContentTable_Reserved09` | TField |  |  |
| 9 | `EB.LCT.RESERVED.08` | `EbLocalContentTable_Reserved08` | TField |  |  |
| 10 | `EB.LCT.RESERVED.07` | `EbLocalContentTable_Reserved07` | TField |  |  |
| 11 | `EB.LCT.RESERVED.06` | `EbLocalContentTable_Reserved06` | TField |  |  |
| 12 | `EB.LCT.RESERVED.05` | `EbLocalContentTable_Reserved05` | TField |  |  |
| 13 | `EB.LCT.RESERVED.04` | `EbLocalContentTable_Reserved04` | TField |  |  |
| 14 | `EB.LCT.RESERVED.03` | `EbLocalContentTable_Reserved03` | TField |  |  |
| 15 | `EB.LCT.RESERVED.02` | `EbLocalContentTable_Reserved02` | TField |  |  |
| 16 | `EB.LCT.RESERVED.01` | `EbLocalContentTable_Reserved01` | TField |  |  |
| 17 | `EB.LCT.RECORD.STATUS` | `EbLocalContentTable_RecordStatus` | String |  |  |
| 18 | `EB.LCT.CURR.NO` | `EbLocalContentTable_CurrNo` | String |  |  |
| 19 | `EB.LCT.INPUTTER` | `EbLocalContentTable_Inputter` |  |  |  |
| 20 | `EB.LCT.DATE.TIME` | `EbLocalContentTable_DateTime` |  |  |  |
| 21 | `EB.LCT.AUTHORISER` | `EbLocalContentTable_Authoriser` | String |  |  |
| 22 | `EB.LCT.CO.CODE` | `EbLocalContentTable_CoCode` | String |  |  |
| 23 | `EB.LCT.DEPT.CODE` | `EbLocalContentTable_DeptCode` | String |  |  |
| 24 | `EB.LCT.AUDITOR.CODE` | `EbLocalContentTable_AuditorCode` | String |  |  |
| 25 | `EB.LCT.AUDIT.DATE.TIME` | `EbLocalContentTable_AuditDateTime` | String |  |  |
