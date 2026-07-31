# PGM.DATA.CONTROL — Table Schema

> Source: `INSERTS/I_F.PGM.DATA.CONTROL` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PDC.PRODUCT` | `PgmDataControl_Product` | TField |  | Contains the actual product code. I.e., AC-Account, DE- Delivery, OB-Obsolete, etc Validation Rules: Standard T24 alphanumeric of maximum 4 characters. |
| 2 | `PDC.SUB.PRODUCT` | `PgmDataControl_SubProduct` | TField |  | Identifies the product of a product. For ex: Product EB, has a sub product like ARCHIVE, GUI, RELEASE, PRINTER, UTILITIES, BATCH, etc Validation Rules: Standard T24 alphanumeric of maximum 20 characters. |
| 3 | `PDC.OBSOLETE` | `PgmDataControl_Obsolete` | TField |  | Identifies release in which the program become obsolete. Validation Rules: Standard T24 alphanumeric of maximum 15 characters. |
| 4 | `PDC.SOURCE.REQ` | `PgmDataControl_SourceReq` | TField |  | Contains 'Y', 'N', 'S', 'T' or ' '(null) Validation Rules: Standard T24 alphanumeric of maximum 2 characters. |
| 5 | `PDC.COMPONENT` | `PgmDataControl_Component` | TField |  | Identifies the component of the program I.e LM_Schedules,TV_Foundation etc Validation rules 1)1-35 characters 2) Valid entry in EB.COMPONENT |
| 6 | `PDC.ADDITIONAL.MODULE` | `PgmDataControl_PdcAdditionalModule` |  |  |  |
| 7 | `PDC.INHERIT.INST.DET` | `PgmDataControl_PdcInheritInstDet` |  |  |  |
| 8 | `PDC.ALTERNATE.ID.REF` | `PgmDataControl_PdcAlternateIdRef` |  |  |  |
