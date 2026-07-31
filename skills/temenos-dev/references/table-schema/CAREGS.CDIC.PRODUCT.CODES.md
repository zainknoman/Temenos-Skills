# CAREGS.CDIC.PRODUCT.CODES — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.PRODUCT.CODES` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.PRD.CODES.DESCRIPTION` | `CaregsCdicProductCodes_Description` | TField |  | Selection Criteria for Product, product group and Account type for CDIC reporting. |
| 2 | `CDIC.PRD.CODES.PRODUCT.SELECTION` | `CaregsCdicProductCodes_ProductSelection` |  |  |  |
| 3 | `CDIC.PRD.CODES.SELECTION.CRITERIA` | `CaregsCdicProductCodes_SelectionCriteria` |  |  |  |
| 4 | `CDIC.PRD.CODES.PROD.DESCRIPTION` | `CaregsCdicProductCodes_ProdDescription` |  |  |  |
| 5 | `CDIC.PRD.CODES.PRD.TYPE.START.SEQ` | `CaregsCdicProductCodes_PrdTypeStartSeq` | TField |  |  |
| 6 | `CDIC.PRD.CODES.DEFAULT.PROD.CODE` | `CaregsCdicProductCodes_DefaultProductCode` |  |  |  |
| 7 | `CDIC.PRD.CODES.DEFAULT.PRODUCT` | `CaregsCdicProductCodes_DefaultProduct` |  |  |  |
| 8 | `CDIC.PRD.CODES.DEFAULT.PROD.GRP` | `CaregsCdicProductCodes_DefaultProdGrp` |  |  |  |
| 9 | `CDIC.PRD.CODES.DEFAULT.PROD.DES` | `CaregsCdicProductCodes_DefaultProdDes` |  |  |  |
| 10 | `CDIC.PRD.CODES.RESERVED.1` | `CaregsCdicProductCodes_Reserved1` | TField |  |  |
| 11 | `CDIC.PRD.CODES.RESERVED.2` | `CaregsCdicProductCodes_Reserved2` | TField |  |  |
| 12 | `CDIC.PRD.CODES.RESERVED.3` | `CaregsCdicProductCodes_Reserved3` | TField |  |  |
| 13 | `CDIC.PRD.CODES.RESERVED.4` | `CaregsCdicProductCodes_Reserved4` | TField |  |  |
| 14 | `CDIC.PRD.CODES.RESERVED.5` | `CaregsCdicProductCodes_Reserved5` | TField |  |  |
| 15 | `CDIC.PRD.CODES.LOCAL.REF` | `CaregsCdicProductCodes_LocalRef` |  |  |  |
| 16 | `CDIC.PRD.CODES.RECORD.STATUS` | `CaregsCdicProductCodes_RecordStatus` | String |  |  |
| 17 | `CDIC.PRD.CODES.CURR.NO` | `CaregsCdicProductCodes_CurrNo` | String |  |  |
| 18 | `CDIC.PRD.CODES.INPUTTER` | `CaregsCdicProductCodes_Inputter` |  |  |  |
| 19 | `CDIC.PRD.CODES.DATE.TIME` | `CaregsCdicProductCodes_DateTime` |  |  |  |
| 20 | `CDIC.PRD.CODES.AUTHORISER` | `CaregsCdicProductCodes_Authoriser` | String |  |  |
| 21 | `CDIC.PRD.CODES.CO.CODE` | `CaregsCdicProductCodes_CoCode` | String |  |  |
| 22 | `CDIC.PRD.CODES.DEPT.CODE` | `CaregsCdicProductCodes_DeptCode` | String |  |  |
| 23 | `CDIC.PRD.CODES.AUDITOR.CODE` | `CaregsCdicProductCodes_AuditorCode` | String |  |  |
| 24 | `CDIC.PRD.CODES.AUDIT.DATE.TIME` | `CaregsCdicProductCodes_AuditDateTime` | String |  |  |
