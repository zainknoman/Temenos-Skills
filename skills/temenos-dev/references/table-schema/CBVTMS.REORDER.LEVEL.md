# CBVTMS.REORDER.LEVEL — Table Schema

> Source: `INSERTS/I_F.CBVTMS.REORDER.LEVEL` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.REORDER.LEVEL` | `CbvtmsReorderLevel_ReorderLevel` |  |  |  |
| 2 | `VTMS.DENOMINATION` | `CbvtmsReorderLevel_Denomination` |  |  |  |
| 3 | `VTMS.LOCAL.REF` | `CbvtmsReorderLevel_LocalRef` |  |  |  |
| 4 | `VTMS.RESERVED.5` | `CbvtmsReorderLevel_Reserved5` | TField |  | Reserved field for future use |
| 5 | `VTMS.RESERVED.4` | `CbvtmsReorderLevel_Reserved4` | TField |  | Reserved field for future use |
| 6 | `VTMS.RESERVED.3` | `CbvtmsReorderLevel_Reserved3` | TField |  | Reserved field for future use |
| 7 | `VTMS.RESERVED.2` | `CbvtmsReorderLevel_Reserved2` | TField |  | Reserved field for future use |
| 8 | `VTMS.RESERVED.1` | `CbvtmsReorderLevel_Reserved1` | TField |  | Reserved field for future use |
| 9 | `VTMS.OVERRIDE` | `CbvtmsReorderLevel_Override` |  |  |  |
| 10 | `VTMS.RECORD.STATUS` | `CbvtmsReorderLevel_RecordStatus` | String |  |  |
| 11 | `VTMS.CURR.NO` | `CbvtmsReorderLevel_CurrNo` | String |  |  |
| 12 | `VTMS.INPUTTER` | `CbvtmsReorderLevel_Inputter` |  |  |  |
| 13 | `VTMS.DATE.TIME` | `CbvtmsReorderLevel_DateTime` |  |  |  |
| 14 | `VTMS.AUTHORISER` | `CbvtmsReorderLevel_Authoriser` | String |  |  |
| 15 | `VTMS.CO.CODE` | `CbvtmsReorderLevel_CoCode` | String |  |  |
| 16 | `VTMS.DEPT.CODE` | `CbvtmsReorderLevel_DeptCode` | String |  |  |
| 17 | `VTMS.AUDITOR.CODE` | `CbvtmsReorderLevel_AuditorCode` | String |  |  |
| 18 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsReorderLevel_AuditDateTime` | String |  |  |
