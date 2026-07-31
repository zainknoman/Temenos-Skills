# CG.INVENTORY.METHOD — Table Schema

> Source: `INSERTS/I_F.CG.INVENTORY.METHOD` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.INV.CUSTOMER` | `CgInventoryMethod_Customer` | TField |  | This field will hold the name of the Customer where the first part of the ID is a Customer This is a NOINPUT, system generated field. This is to enable ease of creating enquiries based on this table |
| 2 | `CG.INV.PORTFOLIO.GROUP` | `CgInventoryMethod_PortfolioGroup` | TField |  | This field will hold the name of the Portfolio Group where the second part of the ID is a Portfolio group name This is a NOINPUT, system generated field. |
| 3 | `CG.INV.CG.METHOD` | `CgInventoryMethod_CgMethod` |  |  |  |
| 4 | `CG.INV.DATE.TO` | `CgInventoryMethod_DateTo` |  |  |  |
| 5 | `CG.INV.LONG.TERM.PERIOD` | `CgInventoryMethod_LongTermPeriod` |  |  |  |
| 6 | `CG.INV.SHORT.TERM.RATE` | `CgInventoryMethod_ShortTermRate` |  |  |  |
| 7 | `CG.INV.LONG.TERM.RATE` | `CgInventoryMethod_LongTermRate` |  |  |  |
| 8 | `CG.INV.DISCOUNT.FACTOR` | `CgInventoryMethod_DiscountFactor` |  |  |  |
| 9 | `CG.INV.ADJUSTMENT.FACTOR` | `CgInventoryMethod_AdjustmentFactor` |  |  |  |
| 10 | `CG.INV.PERIOD.INC.TD` | `CgInventoryMethod_PeriodIncTd` | TField |  | Field determines calculation of long term period of holding.Defaulted from CG.PARAMETER Allowed options : YES,NO or blank NO : Long term period calculation will not include trade date of BUY transaction to identify holding period. YES,Blank : Long term period calculation will include trade date of BUY transaction to identify holding period. |
| 11 | `CG.INV.REVENUE.ASSET` | `CgInventoryMethod_RevenueAsset` | TField | Yes | If this field is flagged as YES, then the asset will be treated as a Revenue asset.This means that the capital gain calculated on this asset is to be treated as a Revenue income instead of a capital gain This field will be used to denote that Capital gain calculated and held in the CG.PL field will be reported as a Revenue income. Validation Rules: Allowed Values: YES or Blank This field is a non-mandatory field. |
| 12 | `CG.INV.EXEMPT.FCY.ACC` | `CgInventoryMethod_ExemptFcyAcc` |  |  |  |
| 13 | `CG.INV.EXEMPT.REASON` | `CgInventoryMethod_ExemptReason` |  |  |  |
| 14 | `CG.INV.RESERVED.21` | `CgInventoryMethod_Reserved21` | TField |  |  |
| 15 | `CG.INV.RESERVED.20` | `CgInventoryMethod_Reserved20` | TField |  |  |
| 16 | `CG.INV.RESERVED.19` | `CgInventoryMethod_Reserved19` | TField |  |  |
| 17 | `CG.INV.RESERVED.18` | `CgInventoryMethod_Reserved18` | TField |  |  |
| 18 | `CG.INV.RESERVED.17` | `CgInventoryMethod_Reserved17` | TField |  |  |
| 19 | `CG.INV.RESERVED.16` | `CgInventoryMethod_Reserved16` | TField |  |  |
| 20 | `CG.INV.RESERVED.15` | `CgInventoryMethod_Reserved15` | TField |  |  |
| 21 | `CG.INV.RESERVED.14` | `CgInventoryMethod_Reserved14` | TField |  |  |
| 22 | `CG.INV.RESERVED.13` | `CgInventoryMethod_Reserved13` | TField |  |  |
| 23 | `CG.INV.RESERVED.12` | `CgInventoryMethod_Reserved12` | TField |  |  |
| 24 | `CG.INV.RESERVED.11` | `CgInventoryMethod_Reserved11` | TField |  |  |
| 25 | `CG.INV.RESERVED.10` | `CgInventoryMethod_Reserved10` | TField |  |  |
| 26 | `CG.INV.RESERVED.9` | `CgInventoryMethod_Reserved9` | TField |  |  |
| 27 | `CG.INV.RESERVED.8` | `CgInventoryMethod_Reserved8` | TField |  |  |
| 28 | `CG.INV.RESERVED.7` | `CgInventoryMethod_Reserved7` | TField |  |  |
| 29 | `CG.INV.RESERVED.6` | `CgInventoryMethod_Reserved6` | TField |  |  |
| 30 | `CG.INV.RESERVED.5` | `CgInventoryMethod_Reserved5` | TField |  |  |
| 31 | `CG.INV.RESERVED.4` | `CgInventoryMethod_Reserved4` | TField |  |  |
| 32 | `CG.INV.RESERVED.3` | `CgInventoryMethod_Reserved3` | TField |  |  |
| 33 | `CG.INV.RESERVED.2` | `CgInventoryMethod_Reserved2` | TField |  |  |
| 34 | `CG.INV.RESERVED.1` | `CgInventoryMethod_Reserved1` | TField |  |  |
| 35 | `CG.INV.LOCAL.REF` | `CgInventoryMethod_LocalRef` |  |  |  |
| 36 | `CG.INV.OVERRIDE` | `CgInventoryMethod_Override` |  |  |  |
| 37 | `CG.INV.RECORD.STATUS` | `CgInventoryMethod_RecordStatus` | String |  |  |
| 38 | `CG.INV.CURR.NO` | `CgInventoryMethod_CurrNo` | String |  |  |
| 39 | `CG.INV.INPUTTER` | `CgInventoryMethod_Inputter` |  |  |  |
| 40 | `CG.INV.DATE.TIME` | `CgInventoryMethod_DateTime` |  |  |  |
| 41 | `CG.INV.AUTHORISER` | `CgInventoryMethod_Authoriser` | String |  |  |
| 42 | `CG.INV.CO.CODE` | `CgInventoryMethod_CoCode` | String |  |  |
| 43 | `CG.INV.DEPT.CODE` | `CgInventoryMethod_DeptCode` | String |  |  |
| 44 | `CG.INV.AUDITOR.CODE` | `CgInventoryMethod_AuditorCode` | String |  |  |
| 45 | `CG.INV.AUDIT.DATE.TIME` | `CgInventoryMethod_AuditDateTime` | String |  |  |
