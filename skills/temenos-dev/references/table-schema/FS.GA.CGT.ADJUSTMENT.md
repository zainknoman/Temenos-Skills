# FS.GA.CGT.ADJUSTMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.CGT.ADJUSTMENT` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CGT.ADJUSTMENT.FUND.ID` | `FsGaCgtAdjustment_FundId` |  |  |  |
| 2 | `FS.GA.CGT.ADJUSTMENT.CAPITAL.GAIN.TAX.CODE` | `FsGaCgtAdjustment_CapitalGainTaxCode` |  |  |  |
| 3 | `FS.GA.CGT.ADJUSTMENT.TAX.DOMICILE` | `FsGaCgtAdjustment_TaxDomicile` |  |  |  |
| 4 | `FS.GA.CGT.ADJUSTMENT.CURRENCY.CODE` | `FsGaCgtAdjustment_CurrencyCode` |  |  |  |
| 5 | `FS.GA.CGT.ADJUSTMENT.CGT.CATEGORIES` | `FsGaCgtAdjustment_CgtCategories` |  |  |  |
| 6 | `FS.GA.CGT.ADJUSTMENT.TRADE.DATE` | `FsGaCgtAdjustment_TradeDate` |  |  |  |
| 7 | `FS.GA.CGT.ADJUSTMENT.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaCgtAdjustment_AmountInLocalCurrency` |  |  |  |
| 8 | `FS.GA.CGT.ADJUSTMENT.RESERVED10` | `FsGaCgtAdjustment_Reserved10` |  |  |  |
| 9 | `FS.GA.CGT.ADJUSTMENT.RESERVED9` | `FsGaCgtAdjustment_Reserved9` |  |  |  |
| 10 | `FS.GA.CGT.ADJUSTMENT.RESERVED8` | `FsGaCgtAdjustment_Reserved8` |  |  |  |
| 11 | `FS.GA.CGT.ADJUSTMENT.RESERVED7` | `FsGaCgtAdjustment_Reserved7` |  |  |  |
| 12 | `FS.GA.CGT.ADJUSTMENT.RESERVED6` | `FsGaCgtAdjustment_Reserved6` |  |  |  |
| 13 | `FS.GA.CGT.ADJUSTMENT.RESERVED5` | `FsGaCgtAdjustment_Reserved5` |  |  |  |
| 14 | `FS.GA.CGT.ADJUSTMENT.RESERVED4` | `FsGaCgtAdjustment_Reserved4` |  |  |  |
| 15 | `FS.GA.CGT.ADJUSTMENT.RESERVED3` | `FsGaCgtAdjustment_Reserved3` |  |  |  |
| 16 | `FS.GA.CGT.ADJUSTMENT.RESERVED2` | `FsGaCgtAdjustment_Reserved2` |  |  |  |
| 17 | `FS.GA.CGT.ADJUSTMENT.RESERVED1` | `FsGaCgtAdjustment_Reserved1` |  |  |  |
| 18 | `FS.GA.CGT.ADJUSTMENT.RECORD.STATUS` | `FsGaCgtAdjustment_RecordStatus` |  |  |  |
| 19 | `FS.GA.CGT.ADJUSTMENT.CURR.NO` | `FsGaCgtAdjustment_CurrNo` |  |  |  |
| 20 | `FS.GA.CGT.ADJUSTMENT.INPUTTER` | `FsGaCgtAdjustment_Inputter` |  |  |  |
| 21 | `FS.GA.CGT.ADJUSTMENT.DATE.TIME` | `FsGaCgtAdjustment_DateTime` |  |  |  |
| 22 | `FS.GA.CGT.ADJUSTMENT.AUTHORISER` | `FsGaCgtAdjustment_Authoriser` |  |  |  |
| 23 | `FS.GA.CGT.ADJUSTMENT.CO.CODE` | `FsGaCgtAdjustment_CoCode` |  |  |  |
| 24 | `FS.GA.CGT.ADJUSTMENT.DEPT.CODE` | `FsGaCgtAdjustment_DeptCode` |  |  |  |
| 25 | `FS.GA.CGT.ADJUSTMENT.AUDITOR.CODE` | `FsGaCgtAdjustment_AuditorCode` |  |  |  |
| 26 | `FS.GA.CGT.ADJUSTMENT.AUDIT.DATE.TIME` | `FsGaCgtAdjustment_AuditDateTime` |  |  |  |
