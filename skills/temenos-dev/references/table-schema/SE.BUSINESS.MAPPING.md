# SE.BUSINESS.MAPPING — Table Schema

> Source: `INSERTS/I_F.SE.BUSINESS.MAPPING` in `SE_SeatHeatMap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SE.BM.DESCRIPTION` | `SeBusinessMapping_Description` |  |  |  |
| 2 | `SE.BM.PRODUCT.GROUP` | `SeBusinessMapping_ProductGroup` | TField |  |  |
| 3 | `SE.BM.BUSINESS.LEVEL` | `SeBusinessMapping_BusinessLevel` |  |  |  |
| 4 | `SE.BM.LEVEL.VALUES` | `SeBusinessMapping_LevelValues` |  |  |  |
| 5 | `SE.BM.RESERVED.15` | `SeBusinessMapping_Reserved15` |  |  |  |
| 6 | `SE.BM.RESERVED.14` | `SeBusinessMapping_Reserved14` |  |  |  |
| 7 | `SE.BM.RESERVED.13` | `SeBusinessMapping_Reserved13` |  |  |  |
| 8 | `SE.BM.RESERVED.12` | `SeBusinessMapping_Reserved12` |  |  |  |
| 9 | `SE.BM.RESERVED.11` | `SeBusinessMapping_Reserved11` |  |  |  |
| 10 | `SE.BM.WORKFLOW` | `SeBusinessMapping_Workflow` |  |  |  |
| 11 | `SE.BM.RESERVED.10` | `SeBusinessMapping_Reserved10` | TField |  |  |
| 12 | `SE.BM.RESERVED.9` | `SeBusinessMapping_Reserved9` | TField |  |  |
| 13 | `SE.BM.RESERVED.8` | `SeBusinessMapping_Reserved8` | TField |  |  |
| 14 | `SE.BM.RESERVED.7` | `SeBusinessMapping_Reserved7` | TField |  |  |
| 15 | `SE.BM.RESERVED.6` | `SeBusinessMapping_Reserved6` | TField |  |  |
| 16 | `SE.BM.RESERVED.5` | `SeBusinessMapping_Reserved5` | TField |  |  |
| 17 | `SE.BM.RESERVED.4` | `SeBusinessMapping_Reserved4` | TField |  |  |
| 18 | `SE.BM.RESERVED.3` | `SeBusinessMapping_Reserved3` | TField |  |  |
| 19 | `SE.BM.RESERVED.2` | `SeBusinessMapping_Reserved2` | TField |  |  |
| 20 | `SE.BM.RESERVED.1` | `SeBusinessMapping_Reserved1` | TField |  |  |
| 21 | `SE.BM.RECORD.STATUS` | `SeBusinessMapping_RecordStatus` | String |  |  |
| 22 | `SE.BM.CURR.NO` | `SeBusinessMapping_CurrNo` | String |  |  |
| 23 | `SE.BM.INPUTTER` | `SeBusinessMapping_Inputter` |  |  |  |
| 24 | `SE.BM.DATE.TIME` | `SeBusinessMapping_DateTime` |  |  |  |
| 25 | `SE.BM.AUTHORISER` | `SeBusinessMapping_Authoriser` | String |  |  |
| 26 | `SE.BM.CO.CODE` | `SeBusinessMapping_CoCode` | String |  |  |
| 27 | `SE.BM.DEPT.CODE` | `SeBusinessMapping_DeptCode` | String |  |  |
| 28 | `SE.BM.AUDITOR.CODE` | `SeBusinessMapping_AuditorCode` | String |  |  |
| 29 | `SE.BM.AUDIT.DATE.TIME` | `SeBusinessMapping_AuditDateTime` | String |  |  |
