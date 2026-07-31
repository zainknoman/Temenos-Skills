# EB.SUB.PRODUCT — Table Schema

> Source: `INSERTS/I_F.EB.SUB.PRODUCT` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SUB.PRD.DESCRIPTION` | `EbSubProduct_Description` |  |  |  |
| 2 | `EB.SUB.PRD.PRODUCT` | `EbSubProduct_Product` | TField |  | The main Product. |
| 3 | `EB.SUB.PRD.RESERVED.10` | `EbSubProduct_Reserved10` | TField |  |  |
| 4 | `EB.SUB.PRD.RESERVED.9` | `EbSubProduct_Reserved9` | TField |  |  |
| 5 | `EB.SUB.PRD.RESERVED.8` | `EbSubProduct_Reserved8` | TField |  |  |
| 6 | `EB.SUB.PRD.RESERVED.7` | `EbSubProduct_Reserved7` | TField |  |  |
| 7 | `EB.SUB.PRD.RESERVED.6` | `EbSubProduct_Reserved6` | TField |  |  |
| 8 | `EB.SUB.PRD.RESERVED.5` | `EbSubProduct_Reserved5` | TField |  |  |
| 9 | `EB.SUB.PRD.RESERVED.4` | `EbSubProduct_Reserved4` | TField |  |  |
| 10 | `EB.SUB.PRD.RESERVED.3` | `EbSubProduct_Reserved3` | TField |  |  |
| 11 | `EB.SUB.PRD.RESERVED.2` | `EbSubProduct_Reserved2` | TField |  |  |
| 12 | `EB.SUB.PRD.RESERVED.1` | `EbSubProduct_Reserved1` | TField |  |  |
| 13 | `EB.SUB.PRD.LOCAL.REF` | `EbSubProduct_LocalRef` |  |  |  |
| 14 | `EB.SUB.PRD.OVERRIDE` | `EbSubProduct_Override` |  |  |  |
| 15 | `EB.SUB.PRD.RECORD.STATUS` | `EbSubProduct_RecordStatus` | String |  |  |
| 16 | `EB.SUB.PRD.CURR.NO` | `EbSubProduct_CurrNo` | String |  |  |
| 17 | `EB.SUB.PRD.INPUTTER` | `EbSubProduct_Inputter` |  |  |  |
| 18 | `EB.SUB.PRD.DATE.TIME` | `EbSubProduct_DateTime` |  |  |  |
| 19 | `EB.SUB.PRD.AUTHORISER` | `EbSubProduct_Authoriser` | String |  |  |
| 20 | `EB.SUB.PRD.CO.CODE` | `EbSubProduct_CoCode` | String |  |  |
| 21 | `EB.SUB.PRD.DEPT.CODE` | `EbSubProduct_DeptCode` | String |  |  |
| 22 | `EB.SUB.PRD.AUDITOR.CODE` | `EbSubProduct_AuditorCode` | String |  |  |
| 23 | `EB.SUB.PRD.AUDIT.DATE.TIME` | `EbSubProduct_AuditDateTime` | String |  |  |
