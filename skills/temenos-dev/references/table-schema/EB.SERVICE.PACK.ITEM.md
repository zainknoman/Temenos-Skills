# EB.SERVICE.PACK.ITEM — Table Schema

> Source: `INSERTS/I_F.EB.SERVICE.PACK.ITEM` in `EB_Upgrade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SRPI.RELATED.SP` | `EbServicePackItem_RelatedSp` | TField |  |  |
| 2 | `EB.SRPI.PRODUCT` | `EbServicePackItem_Product` | TField |  |  |
| 3 | `EB.SRPI.REFERENCE` | `EbServicePackItem_Reference` | TField |  |  |
| 4 | `EB.SRPI.PROBLEM` | `EbServicePackItem_Problem` | TField |  |  |
| 5 | `EB.SRPI.SYMPTOM` | `EbServicePackItem_Symptom` | TField |  |  |
| 6 | `EB.SRPI.NATURE.OF.FIX` | `EbServicePackItem_NatureOfFix` | TField |  |  |
| 7 | `EB.SRPI.RESERVED.10` | `EbServicePackItem_Reserved10` | TField |  |  |
| 8 | `EB.SRPI.RESERVED.9` | `EbServicePackItem_Reserved9` | TField |  |  |
| 9 | `EB.SRPI.RESERVED.8` | `EbServicePackItem_Reserved8` | TField |  |  |
| 10 | `EB.SRPI.RESERVED.7` | `EbServicePackItem_Reserved7` | TField |  |  |
| 11 | `EB.SRPI.RESERVED.6` | `EbServicePackItem_Reserved6` | TField |  |  |
| 12 | `EB.SRPI.RESERVED.5` | `EbServicePackItem_Reserved5` | TField |  |  |
| 13 | `EB.SRPI.RESERVED.4` | `EbServicePackItem_Reserved4` | TField |  |  |
| 14 | `EB.SRPI.RESERVED.3` | `EbServicePackItem_Reserved3` | TField |  |  |
| 15 | `EB.SRPI.RESERVED.2` | `EbServicePackItem_Reserved2` | TField |  |  |
| 16 | `EB.SRPI.RESERVED.1` | `EbServicePackItem_Reserved1` | TField |  |  |
| 17 | `EB.SRPI.LOCAL.REF` | `EbServicePackItem_LocalRef` |  |  |  |
| 18 | `EB.SRPI.OVERRIDE` | `EbServicePackItem_Override` |  |  |  |
| 19 | `EB.SRPI.RECORD.STATUS` | `EbServicePackItem_RecordStatus` | String |  |  |
| 20 | `EB.SRPI.CURR.NO` | `EbServicePackItem_CurrNo` | String |  |  |
| 21 | `EB.SRPI.INPUTTER` | `EbServicePackItem_Inputter` |  |  |  |
| 22 | `EB.SRPI.DATE.TIME` | `EbServicePackItem_DateTime` |  |  |  |
| 23 | `EB.SRPI.AUTHORISER` | `EbServicePackItem_Authoriser` | String |  |  |
| 24 | `EB.SRPI.CO.CODE` | `EbServicePackItem_CoCode` | String |  |  |
| 25 | `EB.SRPI.DEPT.CODE` | `EbServicePackItem_DeptCode` | String |  |  |
| 26 | `EB.SRPI.AUDITOR.CODE` | `EbServicePackItem_AuditorCode` | String |  |  |
| 27 | `EB.SRPI.AUDIT.DATE.TIME` | `EbServicePackItem_AuditDateTime` | String |  |  |
