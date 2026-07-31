# TY.PRODUCT.TXNS — Table Schema

> Source: `INSERTS/I_F.TY.PRODUCT.TXNS` in `TY_Limits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.PRODUCT.TXNS.DEAL.CCY` | `TyProductTxns_DealCcy` |  |  |  |
| 2 | `TY.PRODUCT.TXNS.DEAL.AMOUNT` | `TyProductTxns_DealAmount` |  |  |  |
| 3 | `TY.PRODUCT.TXNS.DEAL.LCY.AMT` | `TyProductTxns_DealLcyAmt` |  |  |  |
| 4 | `TY.PRODUCT.TXNS.MAT.DATE` | `TyProductTxns_MatDate` | TField |  | This field contains the maturity date of the transaction that updated the limits in TY.DEALER.TXN.LIMITS |
| 5 | `TY.PRODUCT.TXNS.START.OF.DAY.MAT` | `TyProductTxns_StartOfDayMat` | TField |  | This field contains the value to indicate if the transaction matures during start of day or end of day. A value of &quot;Y&quot; indicates that the deal matures during start of day. A value of &quot;N&quot; indicates that the deal matures during end of day. |
| 6 | `TY.PRODUCT.TXNS.DAYS.LEFT` | `TyProductTxns_DaysLeft` | TField |  | This field contains the number of days left to maturity for the transaction. This is recalibrated everyday during cob using today&apos;s date and the MAT.DATE field. When the value is less than zero, it means that the deal has matured and the amount that was consumed by this deal already in TY.DEALER.TXN.LIMITS is to be reversed. |
| 7 | `TY.PRODUCT.TXNS.RESERVED.10` | `TyProductTxns_Reserved10` | TField |  |  |
| 8 | `TY.PRODUCT.TXNS.RESERVED.9` | `TyProductTxns_Reserved9` | TField |  |  |
| 9 | `TY.PRODUCT.TXNS.RESERVED.8` | `TyProductTxns_Reserved8` | TField |  |  |
| 10 | `TY.PRODUCT.TXNS.RESERVED.7` | `TyProductTxns_Reserved7` | TField |  |  |
| 11 | `TY.PRODUCT.TXNS.RESERVED.6` | `TyProductTxns_Reserved6` | TField |  |  |
| 12 | `TY.PRODUCT.TXNS.RESERVED.5` | `TyProductTxns_Reserved5` | TField |  |  |
| 13 | `TY.PRODUCT.TXNS.RESERVED.4` | `TyProductTxns_Reserved4` | TField |  |  |
| 14 | `TY.PRODUCT.TXNS.RESERVED.3` | `TyProductTxns_Reserved3` | TField |  |  |
| 15 | `TY.PRODUCT.TXNS.RESERVED.2` | `TyProductTxns_Reserved2` | TField |  |  |
| 16 | `TY.PRODUCT.TXNS.RESERVED.1` | `TyProductTxns_Reserved1` | TField |  |  |
| 17 | `TY.PRODUCT.TXNS.LOCAL.REF` | `TyProductTxns_LocalRef` |  |  |  |
