# MDI.AVAIL.PROD.WORK — Table Schema

> Source: `INSERTS/I_F.MDI.AVAIL.PROD.WORK` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AVAIL.PROD.ITEM.REQ` | `MdiAvailProdWork_ItemReq` |  |  |  |
| 2 | `AVAIL.PROD.ITEM.SENT` | `MdiAvailProdWork_ItemSent` |  |  |  |
| 3 | `AVAIL.PROD.MORE.FLAG` | `MdiAvailProdWork_MoreFlag` |  |  |  |
| 4 | `AVAIL.PROD.PAN.NO` | `MdiAvailProdWork_PanNo` |  |  |  |
| 5 | `AVAIL.PROD.MEMBER.NO` | `MdiAvailProdWork_MemberNo` |  |  |  |
| 6 | `AVAIL.PROD.REQ.PROD.CATEG` | `MdiAvailProdWork_ReqProdCateg` |  |  |  |
| 7 | `AVAIL.PROD.NO.OF.TYPES` | `MdiAvailProdWork_NoOfTypes` |  |  |  |
| 8 | `AVAIL.PROD.PRODUCT.CATEGORY` | `MdiAvailProdWork_ProductCategory` |  |  |  |
| 9 | `AVAIL.PROD.CURRENCY.CODE` | `MdiAvailProdWork_CurrencyCode` |  |  |  |
| 10 | `AVAIL.PROD.PRODUCT.TYPE` | `MdiAvailProdWork_ProductType` |  |  |  |
| 11 | `AVAIL.PROD.PRODUCT.ID` | `MdiAvailProdWork_ProductId` |  |  |  |
| 12 | `AVAIL.PROD.BENEFIT.TYPE` | `MdiAvailProdWork_BenefitType` |  |  |  |
| 13 | `AVAIL.PROD.PRODUCT.DESCRIPTION` | `MdiAvailProdWork_ProductDescription` |  |  |  |
| 14 | `AVAIL.PROD.RESERVED.10` | `MdiAvailProdWork_Reserved10` |  |  |  |
| 15 | `AVAIL.PROD.RESERVED.9` | `MdiAvailProdWork_Reserved9` |  |  |  |
| 16 | `AVAIL.PROD.RESERVED.8` | `MdiAvailProdWork_Reserved8` |  |  |  |
| 17 | `AVAIL.PROD.RESERVED.7` | `MdiAvailProdWork_Reserved7` |  |  |  |
| 18 | `AVAIL.PROD.RESERVED.6` | `MdiAvailProdWork_Reserved6` |  |  |  |
| 19 | `AVAIL.PROD.RESERVED.5` | `MdiAvailProdWork_Reserved5` |  |  |  |
| 20 | `AVAIL.PROD.RESERVED.4` | `MdiAvailProdWork_Reserved4` |  |  |  |
| 21 | `AVAIL.PROD.RESERVED.3` | `MdiAvailProdWork_Reserved3` |  |  |  |
| 22 | `AVAIL.PROD.RESERVED.2` | `MdiAvailProdWork_Reserved2` |  |  |  |
| 23 | `AVAIL.PROD.RESERVED.1` | `MdiAvailProdWork_Reserved1` |  |  |  |
| 24 | `AVAIL.PROD.LOCAL.REF` | `MdiAvailProdWork_LocalRef` |  |  |  |
