# LUFDRT.FDR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LUFDRT.FDR.PARAMETER` in `LUFDRT_FdrTaxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LUFDRT.COUPON.REV.DIARY.TYPE` | `LufdrtFdrParameter_CouponRevDiaryType` |  |  |  |
| 2 | `LUFDRT.COUPON.REV.SUB.ASSET.TYPE` | `LufdrtFdrParameter_CouponRevSubAssetType` |  |  |  |
| 3 | `LUFDRT.DISC.PRICE.REV.DIARY.TYPE` | `LufdrtFdrParameter_DiscPriceRevDiaryType` |  |  |  |
| 4 | `LUFDRT.DISC.PRICE.REV.SUB.ASSET.TYPE` | `LufdrtFdrParameter_DiscPriceRevSubAssetType` |  |  |  |
| 5 | `LUFDRT.DISC.PRICE.REV.TRANS.TYPE` | `LufdrtFdrParameter_DiscPriceRevTransType` |  |  |  |
| 6 | `LUFDRT.DISC.PRICE.REV.TR.SUB.ASSET` | `LufdrtFdrParameter_DiscPriceRevTrSubAsset` |  |  |  |
| 7 | `LUFDRT.TOTAL.DISC` | `LufdrtFdrParameter_TotalDisc` | TField |  | Define total spread limit between issue and redemption price. For eg., total spread must not be higher than 3% between issue price and redemption price |
| 8 | `LUFDRT.PERIOD.DISC` | `LufdrtFdrParameter_PeriodDisc` | TField |  | Define issue discount % per year For eg.,issue discount must not be > 0.5% per year |
| 9 | `LUFDRT.TRADE.TRANSFER.CR.TRANS.TYPE` | `LufdrtFdrParameter_TradeTransferCrTransType` |  |  |  |
| 10 | `LUFDRT.ACCRUED.INT.REV.TRANS.TYPE` | `LufdrtFdrParameter_AccruedIntRevTransType` |  |  |  |
| 11 | `LUFDRT.ACCRUED.INT.REV.SUB.ASSET.TYPE` | `LufdrtFdrParameter_AccruedIntRevSubAssetType` |  |  |  |
| 12 | `LUFDRT.INTEREST.PROPERTY` | `LufdrtFdrParameter_InterestProperty` |  |  |  |
| 13 | `LUFDRT.INTEREST.RATE.CURRENT.ACCT` | `LufdrtFdrParameter_InterestRateCurrentAcct` | TField |  | Define threshold interest rate for current account based on which interest on current account is subject or not to FDR tax |
| 14 | `LUFDRT.ACCOUNT.CLASS` | `LufdrtFdrParameter_AccountClass` | TField |  | Define ACCOUNT.CLASS @ID of current account; for accounts with category defined in account class, FDR tax will be calculated subject to the conditions. |
| 15 | `LUFDRT.OVERRIDE` | `LufdrtFdrParameter_Override` |  |  |  |
| 16 | `LUFDRT.RECORD.STATUS` | `LufdrtFdrParameter_RecordStatus` | String |  |  |
| 17 | `LUFDRT.CURR.NO` | `LufdrtFdrParameter_CurrNo` | String |  |  |
| 18 | `LUFDRT.INPUTTER` | `LufdrtFdrParameter_Inputter` |  |  |  |
| 19 | `LUFDRT.DATE.TIME` | `LufdrtFdrParameter_DateTime` |  |  |  |
| 20 | `LUFDRT.AUTHORISER` | `LufdrtFdrParameter_Authoriser` | String |  |  |
| 21 | `LUFDRT.CO.CODE` | `LufdrtFdrParameter_CoCode` | String |  |  |
| 22 | `LUFDRT.DEPT.CODE` | `LufdrtFdrParameter_DeptCode` | String |  |  |
| 23 | `LUFDRT.AUDITOR.CODE` | `LufdrtFdrParameter_AuditorCode` | String |  |  |
| 24 | `LUFDRT.AUDIT.DATE.TIME` | `LufdrtFdrParameter_AuditDateTime` | String |  |  |
| 25 | `LUFDRT.DISC.PRICE.CR.TRANS.TYPE` | `LufdrtFdrParameter_DiscPriceCrTransType` |  |  |  |
| 26 | `LUFDRT.TAX.TYPE` | `LufdrtFdrParameter_TaxType` | TField |  | Define the Tax Type/Tax name which has to be applied on Luxembourg taxation |
| 27 | `LUFDRT.DISC.TAX.TYPE` | `LufdrtFdrParameter_DiscTaxType` | TField |  | Define the Tax Type/Tax name for Discount counter method which has to be applied on Luxembourg taxation |
