# EB.PRODUCT — Table Schema

> Source: `INSERTS/I_F.EB.PRODUCT` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.PRD.DESCRIPTION` | `EbProduct_Description` |  |  |  |
| 2 | `EB.PRD.COMPONENT` | `EbProduct_Component` |  |  |  |
| 3 | `EB.PRD.PRODUCT.GROUP` | `EbProduct_ProductGroup` | TField |  |  |
| 4 | `EB.PRD.MODULE.UPGRADE` | `EbProduct_ModuleUpgrade` | TField |  |  |
| 5 | `EB.PRD.CURRENT.RELEASE` | `EbProduct_CurrentRelease` | TField |  |  |
| 6 | `EB.PRD.PREVIOUS.RELEASE` | `EbProduct_PreviousRelease` | TField |  |  |
| 7 | `EB.PRD.PRODUCT.COUNTRY` | `EbProduct_ProductCountry` |  |  |  |
| 8 | `EB.PRD.MDAL.ENTITY` | `EbProduct_PrdMdalEntity` |  |  |  |
| 9 | `EB.PRD.RESERVED3` | `EbProduct_Reserved3` | TField |  |  |
| 10 | `EB.PRD.RESERVED2` | `EbProduct_Reserved2` | TField |  |  |
| 11 | `EB.PRD.RESERVED1` | `EbProduct_Reserved1` | TField |  |  |
| 12 | `EB.PRD.LOCAL.REF` | `EbProduct_LocalRef` |  |  |  |
| 13 | `EB.PRD.RECORD.STATUS` | `EbProduct_RecordStatus` | String |  |  |
| 14 | `EB.PRD.CURR.NO` | `EbProduct_CurrNo` | String |  |  |
| 15 | `EB.PRD.INPUTTER` | `EbProduct_Inputter` |  |  |  |
| 16 | `EB.PRD.DATE.TIME` | `EbProduct_DateTime` |  |  |  |
| 17 | `EB.PRD.AUTHORISER` | `EbProduct_Authoriser` | String |  |  |
| 18 | `EB.PRD.CO.CODE` | `EbProduct_CoCode` | String |  |  |
| 19 | `EB.PRD.DEPT.CODE` | `EbProduct_DeptCode` | String |  |  |
| 20 | `EB.PRD.AUDITOR.CODE` | `EbProduct_AuditorCode` | String |  |  |
| 21 | `EB.PRD.AUDIT.DATE.TIME` | `EbProduct_AuditDateTime` | String |  |  |
