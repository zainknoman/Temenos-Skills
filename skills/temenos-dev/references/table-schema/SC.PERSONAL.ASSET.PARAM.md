# SC.PERSONAL.ASSET.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.PERSONAL.ASSET.PARAM` in `SC_SctOtherAssets.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PAP.BUY.TXN.CODE` | `ScPersonalAssetParam_BuyTxnCode` |  |  |  |
| 2 | `SC.PAP.SELL.TXN.CODE` | `ScPersonalAssetParam_SellTxnCode` |  |  |  |
| 3 | `SC.PAP.WR.IN.TXN.CODE` | `ScPersonalAssetParam_WrInTxnCode` |  |  |  |
| 4 | `SC.PAP.WR.OUT.TXN.CODE` | `ScPersonalAssetParam_WrOutTxnCode` |  |  |  |
| 5 | `SC.PAP.SUSP.CATEGORY` | `ScPersonalAssetParam_SuspCategory` | TField |  | Internal account category - for both buy and sell side. |
| 6 | `SC.PAP.WASH.DEPOSITORY` | `ScPersonalAssetParam_WashDepository` | TField |  | A valid CUSTOMER.SECURITY record that is defined as a DEPOSITORY. This will be a dummy depository to record non shared asset positions. |
| 7 | `SC.PAP.PRICE.SOURCE` | `ScPersonalAssetParam_PriceSource` | TField | Yes | Any valid PRICE.UPDATE record with Auto Update set as NO. Used only to default to Personal asset type transaction and its a mandatory field |
| 8 | `SC.PAP.SC.INDUSTRY` | `ScPersonalAssetParam_ScIndustry` | TField | Yes | A valid SC.INDUSTRY code. This will be used to default to the Industry field while creating a Security Master and its a mandatory field |
| 9 | `SC.PAP.COUPON.TAX.CODE` | `ScPersonalAssetParam_CouponTaxCode` | TField | Yes | Any valid coupon tax code. Ideally should be a Zero tax and its a Mandatory field |
| 10 | `SC.PAP.OFS.SOURCE` | `ScPersonalAssetParam_OfsSource` |  |  |  |
| 11 | `SC.PAP.OFS.VERSION` | `ScPersonalAssetParam_OfsVersion` |  |  |  |
| 12 | `SC.PAP.STOCK.EXCHANGE` | `ScPersonalAssetParam_StockExchange` | TField | Yes | Unique Code used to identify each separate Stock Exchange where securities may be traded. Validation Rules: 1-5 Alpha numeric characters. Mandatory input. Examples: Zurich Stock Exchange would be set up as Zurich. Basle = Basle Mandatory input |
| 13 | `SC.PAP.LIAB.IN.TXN.CODE` | `ScPersonalAssetParam_LiabInTxnCode` | TField |  | Must be a valid debit transaction code in SC.TRANS.NAME application This will be mapped to the field TRANSACTION.CODE in SC.PERSONAL.ASSET.TXN when the transaction type is BUY/WRITE.IN if LIABILITY is set to YES |
| 14 | `SC.PAP.LIAB.OUT.TXN.CODE` | `ScPersonalAssetParam_LiabOutTxnCode` | TField |  | Must be a valid credit transaction code in SC.TRANS.NAME application This will be mapped to the field TRANSACTION.CODE in SC.PERSONAL.ASSET.TXN when the transaction type is SALE/WRITE.OUT/MATURITY if LIABILITY is set to YES |
| 15 | `SC.PAP.MAT.TXN.CODE` | `ScPersonalAssetParam_MatTxnCode` |  |  |  |
| 16 | `SC.PAP.RESERVED.11` | `ScPersonalAssetParam_Reserved11` | TField |  |  |
| 17 | `SC.PAP.RESERVED.10` | `ScPersonalAssetParam_Reserved10` | TField |  |  |
| 18 | `SC.PAP.RESERVED.09` | `ScPersonalAssetParam_Reserved09` | TField |  |  |
| 19 | `SC.PAP.RESERVED.08` | `ScPersonalAssetParam_Reserved08` | TField |  |  |
| 20 | `SC.PAP.RESERVED.07` | `ScPersonalAssetParam_Reserved07` | TField |  |  |
| 21 | `SC.PAP.RESERVED.06` | `ScPersonalAssetParam_Reserved06` | TField |  |  |
| 22 | `SC.PAP.RESERVED.05` | `ScPersonalAssetParam_Reserved05` | TField |  |  |
| 23 | `SC.PAP.RESERVED.04` | `ScPersonalAssetParam_Reserved04` | TField |  |  |
| 24 | `SC.PAP.RESERVED.03` | `ScPersonalAssetParam_Reserved03` | TField |  |  |
| 25 | `SC.PAP.RESERVED.02` | `ScPersonalAssetParam_Reserved02` | TField |  |  |
| 26 | `SC.PAP.RESERVED.01` | `ScPersonalAssetParam_Reserved01` | TField |  |  |
| 27 | `SC.PAP.LOCAL.REF` | `ScPersonalAssetParam_LocalRef` |  |  |  |
| 28 | `SC.PAP.OVERRIDE` | `ScPersonalAssetParam_Override` |  |  |  |
| 29 | `SC.PAP.RECORD.STATUS` | `ScPersonalAssetParam_RecordStatus` | String |  |  |
| 30 | `SC.PAP.CURR.NO` | `ScPersonalAssetParam_CurrNo` | String |  |  |
| 31 | `SC.PAP.INPUTTER` | `ScPersonalAssetParam_Inputter` |  |  |  |
| 32 | `SC.PAP.DATE.TIME` | `ScPersonalAssetParam_DateTime` |  |  |  |
| 33 | `SC.PAP.AUTHORISER` | `ScPersonalAssetParam_Authoriser` | String |  |  |
| 34 | `SC.PAP.CO.CODE` | `ScPersonalAssetParam_CoCode` | String |  |  |
| 35 | `SC.PAP.DEPT.CODE` | `ScPersonalAssetParam_DeptCode` | String |  |  |
| 36 | `SC.PAP.AUDITOR.CODE` | `ScPersonalAssetParam_AuditorCode` | String |  |  |
| 37 | `SC.PAP.AUDIT.DATE.TIME` | `ScPersonalAssetParam_AuditDateTime` | String |  |  |
