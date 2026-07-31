# AA.PROMO.CODE — Table Schema

> Source: `INSERTS/I_F.AA.PROMO.CODE` in `AA_PromotionRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PROC.CUSTOMER.ID` | `AaPromoCode_CustomerId` | TField |  | Key to the table and is a valid CUSTOMER reference. |
| 2 | `AA.PROC.PROMOTION.PRODUCT` | `AaPromoCode_PromotionProduct` |  |  |  |
| 3 | `AA.PROC.ALLOWED.PRODUCT.LINE` | `AaPromoCode_AllowedProductLine` |  |  |  |
| 4 | `AA.PROC.ALLOWED.PRODUCT.GROUP` | `AaPromoCode_AllowedProductGroup` |  |  |  |
| 5 | `AA.PROC.ALLOWED.PRODUCT` | `AaPromoCode_AllowedProduct` |  |  |  |
| 6 | `AA.PROC.PROMO.COUNT` | `AaPromoCode_PromoCount` |  |  |  |
| 7 | `AA.PROC.SYSTEM.CREATED` | `AaPromoCode_SystemCreated` |  |  |  |
| 8 | `AA.PROC.EXPIRY.DATE` | `AaPromoCode_ExpiryDate` |  |  |  |
| 9 | `AA.PROC.RESERVED.9` | `AaPromoCode_Reserved9` |  |  |  |
| 10 | `AA.PROC.RESERVED.8` | `AaPromoCode_Reserved8` |  |  |  |
| 11 | `AA.PROC.RESERVED.7` | `AaPromoCode_Reserved7` |  |  |  |
| 12 | `AA.PROC.RESERVED.6` | `AaPromoCode_Reserved6` | TField |  |  |
| 13 | `AA.PROC.RESERVED.5` | `AaPromoCode_Reserved5` | TField |  |  |
| 14 | `AA.PROC.RESERVED.4` | `AaPromoCode_Reserved4` | TField |  |  |
| 15 | `AA.PROC.RESERVED.3` | `AaPromoCode_Reserved3` | TField |  |  |
| 16 | `AA.PROC.RESERVED.2` | `AaPromoCode_Reserved2` | TField |  |  |
| 17 | `AA.PROC.RESERVED.1` | `AaPromoCode_Reserved1` | TField |  |  |
| 18 | `AA.PROC.LOCAL.REF` | `AaPromoCode_LocalRef` |  |  |  |
| 19 | `AA.PROC.OVERRIDE` | `AaPromoCode_Override` |  |  |  |
| 20 | `AA.PROC.RECORD.STATUS` | `AaPromoCode_RecordStatus` | String |  |  |
| 21 | `AA.PROC.CURR.NO` | `AaPromoCode_CurrNo` | String |  |  |
| 22 | `AA.PROC.INPUTTER` | `AaPromoCode_Inputter` |  |  |  |
| 23 | `AA.PROC.DATE.TIME` | `AaPromoCode_DateTime` |  |  |  |
| 24 | `AA.PROC.AUTHORISER` | `AaPromoCode_Authoriser` | String |  |  |
| 25 | `AA.PROC.CO.CODE` | `AaPromoCode_CoCode` | String |  |  |
| 26 | `AA.PROC.DEPT.CODE` | `AaPromoCode_DeptCode` | String |  |  |
| 27 | `AA.PROC.AUDITOR.CODE` | `AaPromoCode_AuditorCode` | String |  |  |
| 28 | `AA.PROC.AUDIT.DATE.TIME` | `AaPromoCode_AuditDateTime` | String |  |  |
