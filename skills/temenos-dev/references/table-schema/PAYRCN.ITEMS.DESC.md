# PAYRCN.ITEMS.DESC — Table Schema

> Source: `INSERTS/I_F.PAYRCN.ITEMS.DESC` in `FINEXT_ATMRECON.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAYRCN.DESC.DESCRIPTION` | `PayrcnItemsDesc_Description` |  |  |  |
| 2 | `PAYRCN.DESC.FIELD.NAME` | `PayrcnItemsDesc_FieldName` |  |  |  |
| 3 | `PAYRCN.DESC.RESERVED.13` | `PayrcnItemsDesc_Reserved13` |  |  |  |
| 4 | `PAYRCN.DESC.RESERVED.12` | `PayrcnItemsDesc_Reserved12` |  |  |  |
| 5 | `PAYRCN.DESC.RESERVED.11` | `PayrcnItemsDesc_Reserved11` |  |  |  |
| 6 | `PAYRCN.DESC.FIELD.DESC` | `PayrcnItemsDesc_FieldDesc` |  |  |  |
| 7 | `PAYRCN.DESC.RESERVED.10` | `PayrcnItemsDesc_Reserved10` | TField |  |  |
| 8 | `PAYRCN.DESC.RESERVED.9` | `PayrcnItemsDesc_Reserved9` | TField |  |  |
| 9 | `PAYRCN.DESC.RESERVED.8` | `PayrcnItemsDesc_Reserved8` | TField |  |  |
| 10 | `PAYRCN.DESC.RESERVED.7` | `PayrcnItemsDesc_Reserved7` | TField |  |  |
| 11 | `PAYRCN.DESC.RESERVED.6` | `PayrcnItemsDesc_Reserved6` | TField |  |  |
| 12 | `PAYRCN.DESC.RESERVED.5` | `PayrcnItemsDesc_Reserved5` | TField |  |  |
| 13 | `PAYRCN.DESC.RESERVED.4` | `PayrcnItemsDesc_Reserved4` | TField |  |  |
| 14 | `PAYRCN.DESC.RESERVED.3` | `PayrcnItemsDesc_Reserved3` | TField |  |  |
| 15 | `PAYRCN.DESC.RESERVED.2` | `PayrcnItemsDesc_Reserved2` | TField |  |  |
| 16 | `PAYRCN.DESC.RESERVED.1` | `PayrcnItemsDesc_Reserved1` | TField |  |  |
| 17 | `PAYRCN.DESC.RECORD.STATUS` | `PayrcnItemsDesc_RecordStatus` | String |  |  |
| 18 | `PAYRCN.DESC.CURR.NO` | `PayrcnItemsDesc_CurrNo` | String |  |  |
| 19 | `PAYRCN.DESC.INPUTTER` | `PayrcnItemsDesc_Inputter` |  |  |  |
| 20 | `PAYRCN.DESC.DATE.TIME` | `PayrcnItemsDesc_DateTime` |  |  |  |
| 21 | `PAYRCN.DESC.AUTHORISER` | `PayrcnItemsDesc_Authoriser` | String |  |  |
| 22 | `PAYRCN.DESC.CO.CODE` | `PayrcnItemsDesc_CoCode` | String |  |  |
| 23 | `PAYRCN.DESC.DEPT.CODE` | `PayrcnItemsDesc_DeptCode` | String |  |  |
| 24 | `PAYRCN.DESC.AUDITOR.CODE` | `PayrcnItemsDesc_AuditorCode` | String |  |  |
| 25 | `PAYRCN.DESC.AUDIT.DATE.TIME` | `PayrcnItemsDesc_AuditDateTime` | String |  |  |
