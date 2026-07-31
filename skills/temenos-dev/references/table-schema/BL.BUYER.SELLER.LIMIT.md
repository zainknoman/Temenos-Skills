# BL.BUYER.SELLER.LIMIT — Table Schema

> Source: `INSERTS/I_F.BL.BUYER.SELLER.LIMIT` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.BSL.CURRENCY` | `BlBuyerSellerLimit_Currency` | TField |  | This Field defines the currency in which the BUYER-SELLER limit is defined Validation Rules: Id of the Currency |
| 2 | `BL.BSL.LIMIT.AMOUNT` | `BlBuyerSellerLimit_LimitAmount` | TField | Yes | Field to define the overall exposure of the buyer,Amount expressed in the currency defined in the CURRENCY field Validation Rules: Field is Mandatory |
| 3 | `BL.BSL.OUTSTANDING.AMT` | `BlBuyerSellerLimit_OutstandingAmt` | TField |  |  |
| 4 | `BL.BSL.AVAILABLE.AMT` | `BlBuyerSellerLimit_AvailableAmt` | TField |  |  |
| 5 | `BL.BSL.RESERVED.12` | `BlBuyerSellerLimit_Reserved12` | TField |  |  |
| 6 | `BL.BSL.RESERVED.11` | `BlBuyerSellerLimit_Reserved11` | TField |  |  |
| 7 | `BL.BSL.SELLER.ID` | `BlBuyerSellerLimit_SellerId` |  |  |  |
| 8 | `BL.BSL.LIMIT.AMT` | `BlBuyerSellerLimit_LimitAmt` |  |  |  |
| 9 | `BL.BSL.TOT.OS.AMT` | `BlBuyerSellerLimit_TotOsAmt` |  |  |  |
| 10 | `BL.BSL.AVAIL.AMT` | `BlBuyerSellerLimit_AvailAmt` |  |  |  |
| 11 | `BL.BSL.OS.CCY` | `BlBuyerSellerLimit_OsCcy` |  |  |  |
| 12 | `BL.BSL.OS.AMT` | `BlBuyerSellerLimit_OsAmt` |  |  |  |
| 13 | `BL.BSL.RETENTION.MARGIN` | `BlBuyerSellerLimit_RetentionMargin` | TField | No | Field to define percentage of margin to be applied when a financial transaction is input involving the buyer and the seller. Validation Rules: Value defined will get defaulted in BL.REGISTER when BL.TYPE is assigned and retention margin is set to 'Allowed'. Acceptable values to be any numeric between 1 and 99. Decimals not to be allowed. Optional field. |
| 14 | `BL.BSL.RESERVED.10` | `BlBuyerSellerLimit_Reserved10` | TField |  |  |
| 15 | `BL.BSL.RESERVED.9` | `BlBuyerSellerLimit_Reserved9` | TField |  |  |
| 16 | `BL.BSL.RESERVED.8` | `BlBuyerSellerLimit_Reserved8` | TField |  |  |
| 17 | `BL.BSL.RESERVED.7` | `BlBuyerSellerLimit_Reserved7` | TField |  |  |
| 18 | `BL.BSL.RESERVED.6` | `BlBuyerSellerLimit_Reserved6` | TField |  |  |
| 19 | `BL.BSL.RESERVED.5` | `BlBuyerSellerLimit_Reserved5` | TField |  |  |
| 20 | `BL.BSL.RESERVED.4` | `BlBuyerSellerLimit_Reserved4` | TField |  |  |
| 21 | `BL.BSL.RESERVED.3` | `BlBuyerSellerLimit_Reserved3` | TField |  |  |
| 22 | `BL.BSL.RESERVED.2` | `BlBuyerSellerLimit_Reserved2` | TField |  |  |
| 23 | `BL.BSL.RESERVED.1` | `BlBuyerSellerLimit_Reserved1` | TField |  |  |
| 24 | `BL.BSL.LOCAL.REF` | `BlBuyerSellerLimit_LocalRef` |  |  |  |
| 25 | `BL.BSL.OVERRIDE` | `BlBuyerSellerLimit_Override` |  |  |  |
| 26 | `BL.BSL.RECORD.STATUS` | `BlBuyerSellerLimit_RecordStatus` | String |  |  |
| 27 | `BL.BSL.CURR.NO` | `BlBuyerSellerLimit_CurrNo` | String |  |  |
| 28 | `BL.BSL.INPUTTER` | `BlBuyerSellerLimit_Inputter` |  |  |  |
| 29 | `BL.BSL.DATE.TIME` | `BlBuyerSellerLimit_DateTime` |  |  |  |
| 30 | `BL.BSL.AUTHORISER` | `BlBuyerSellerLimit_Authoriser` | String |  |  |
| 31 | `BL.BSL.CO.CODE` | `BlBuyerSellerLimit_CoCode` | String |  |  |
| 32 | `BL.BSL.DEPT.CODE` | `BlBuyerSellerLimit_DeptCode` | String |  |  |
| 33 | `BL.BSL.AUDITOR.CODE` | `BlBuyerSellerLimit_AuditorCode` | String |  |  |
| 34 | `BL.BSL.AUDIT.DATE.TIME` | `BlBuyerSellerLimit_AuditDateTime` | String |  |  |
