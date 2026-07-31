# DX.VARIATION.MARGIN.DETS — Table Schema

> Source: `INSERTS/I_F.DX.VARIATION.MARGIN.DETS` in `DX_Trade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.VMDET.DATE` | `DxVariationMarginDets_Date` |  |  |  |
| 2 | `DX.VMDET.ACCOUNT` | `DxVariationMarginDets_Account` |  |  |  |
| 3 | `DX.VMDET.CURRENCY` | `DxVariationMarginDets_Currency` |  |  |  |
| 4 | `DX.VMDET.MARGIN.REF.CCY` | `DxVariationMarginDets_MarginRefCcy` |  |  |  |
| 5 | `DX.VMDET.AMOUNT` | `DxVariationMarginDets_Amount` |  |  |  |
| 6 | `DX.VMDET.EXC.RATE.VM` | `DxVariationMarginDets_ExcRateVm` |  |  |  |
| 7 | `DX.VMDET.EXC.RATE.REF` | `DxVariationMarginDets_ExcRateRef` |  |  |  |
| 8 | `DX.VMDET.EXC.RATE.ACC` | `DxVariationMarginDets_ExcRateAcc` |  |  |  |
| 9 | `DX.VMDET.RESERVED1` | `DxVariationMarginDets_Reserved1` |  |  |  |
| 10 | `DX.VMDET.RESERVED2` | `DxVariationMarginDets_Reserved2` |  |  |  |
| 11 | `DX.VMDET.TRADE.STATUS` | `DxVariationMarginDets_TradeStatus` | TField |  | Updated with value 'RNA' when the reversal trade is authorised. This status is used by COB job DX.POST.VM.INDIV.ENTRIES to post reversal variation margin entries during COB or by online service DX.RV.SERVICE. |
| 12 | `DX.VMDET.RESERVED3` | `DxVariationMarginDets_Reserved3` | TField |  |  |
| 13 | `DX.VMDET.RESERVED4` | `DxVariationMarginDets_Reserved4` | TField |  |  |
