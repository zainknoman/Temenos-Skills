# MDI.PROD.CATEG — Table Schema

> Source: `INSERTS/I_F.MDI.PROD.CATEG` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MDI.PROD.SHORT.DESCRP` | `MdiProdCateg_ShortDescrp` |  |  |  |
| 2 | `MDI.PROD.DESCRIPTION` | `MdiProdCateg_Description` |  |  |  |
| 3 | `MDI.PROD.MDI.PROD.CATEG` | `MdiProdCateg_MdiProdCateg` |  |  |  |
| 4 | `MDI.PROD.MDI.PROD.TYPE` | `MdiProdCateg_MdiProdType` |  |  |  |
| 5 | `MDI.PROD.TP.PROD.CATEG` | `MdiProdCateg_TpProdCateg` |  |  |  |
| 6 | `MDI.PROD.TP.PROD.TYPE` | `MdiProdCateg_TpProdType` |  |  |  |
| 7 | `MDI.PROD.RESERVED.8` | `MdiProdCateg_Reserved8` |  |  |  |
| 8 | `MDI.PROD.RESERVED.7` | `MdiProdCateg_Reserved7` |  |  |  |
| 9 | `MDI.PROD.RESERVED.6` | `MdiProdCateg_Reserved6` |  |  |  |
| 10 | `MDI.PROD.RESERVED.5` | `MdiProdCateg_Reserved5` |  |  |  |
| 11 | `MDI.PROD.RESERVED.4` | `MdiProdCateg_Reserved4` |  |  |  |
| 12 | `MDI.PROD.RESERVED.3` | `MdiProdCateg_Reserved3` |  |  |  |
| 13 | `MDI.PROD.RESERVED.2` | `MdiProdCateg_Reserved2` |  |  |  |
| 14 | `MDI.PROD.RESERVED.1` | `MdiProdCateg_Reserved1` |  |  |  |
| 15 | `MDI.PROD.LOCAL.REF` | `MdiProdCateg_LocalRef` |  |  |  |
| 16 | `MDI.PROD.OVERRIDE` | `MdiProdCateg_Override` |  |  |  |
| 17 | `MDI.PROD.RECORD.STATUS` | `MdiProdCateg_RecordStatus` |  |  |  |
| 18 | `MDI.PROD.CURR.NO` | `MdiProdCateg_CurrNo` |  |  |  |
| 19 | `MDI.PROD.INPUTTER` | `MdiProdCateg_Inputter` |  |  |  |
| 20 | `MDI.PROD.DATE.TIME` | `MdiProdCateg_DateTime` |  |  |  |
| 21 | `MDI.PROD.AUTHORISER` | `MdiProdCateg_Authoriser` |  |  |  |
| 22 | `MDI.PROD.CO.CODE` | `MdiProdCateg_CoCode` |  |  |  |
| 23 | `MDI.PROD.DEPT.CODE` | `MdiProdCateg_DeptCode` |  |  |  |
| 24 | `MDI.PROD.AUDITOR.CODE` | `MdiProdCateg_AuditorCode` |  |  |  |
| 25 | `MDI.PROD.AUDIT.DATE.TIME` | `MdiProdCateg_AuditDateTime` |  |  |  |
