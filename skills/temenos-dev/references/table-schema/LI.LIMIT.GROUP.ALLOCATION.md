# LI.LIMIT.GROUP.ALLOCATION — Table Schema

> Source: `INSERTS/I_F.LI.LIMIT.GROUP.ALLOCATION` in `LI_GroupLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.GR.AL.DEAL.REFERENCE` | `LiLimitGroupAllocation_DealReference` |  |  |  |
| 2 | `LI.GR.AL.DEAL.CURRENCY` | `LiLimitGroupAllocation_DealCurrency` |  |  |  |
| 3 | `LI.GR.AL.DEAL.AMOUNT` | `LiLimitGroupAllocation_DealAmount` |  |  |  |
| 4 | `LI.GR.AL.OVERDRAW.AMT` | `LiLimitGroupAllocation_OverdrawAmt` |  |  |  |
| 5 | `LI.GR.AL.COMMT.OVERDRAW.AMT` | `LiLimitGroupAllocation_CommtOverdrawAmt` |  |  |  |
| 6 | `LI.GR.AL.OVERDRAW.LIMIT` | `LiLimitGroupAllocation_OverdrawLimit` |  |  |  |
| 7 | `LI.GR.AL.RESERVED.19` | `LiLimitGroupAllocation_Reserved19` |  |  |  |
| 8 | `LI.GR.AL.RESERVED.18` | `LiLimitGroupAllocation_Reserved18` |  |  |  |
| 9 | `LI.GR.AL.LIMIT.KEY` | `LiLimitGroupAllocation_LimitKey` |  |  |  |
| 10 | `LI.GR.AL.LIMIT.AMT.ALLOC` | `LiLimitGroupAllocation_LimitAmtAlloc` |  |  |  |
| 11 | `LI.GR.AL.COMMT.AMT.ALLOC` | `LiLimitGroupAllocation_CommtAmtAlloc` |  |  |  |
| 12 | `LI.GR.AL.RESERVED.17` | `LiLimitGroupAllocation_Reserved17` | TField |  |  |
| 13 | `LI.GR.AL.RESERVED.16` | `LiLimitGroupAllocation_Reserved16` | TField |  |  |
| 14 | `LI.GR.AL.RESERVED.15` | `LiLimitGroupAllocation_Reserved15` | TField |  |  |
| 15 | `LI.GR.AL.GROUP.KEY` | `LiLimitGroupAllocation_GroupKey` |  |  |  |
| 16 | `LI.GR.AL.GROUP.CURRENCY` | `LiLimitGroupAllocation_GroupCurrency` |  |  |  |
| 17 | `LI.GR.AL.TOTAL.ALLOCATION` | `LiLimitGroupAllocation_TotalAllocation` |  |  |  |
| 18 | `LI.GR.AL.RESERVED.14` | `LiLimitGroupAllocation_Reserved14` | TField |  |  |
| 19 | `LI.GR.AL.RESERVED.13` | `LiLimitGroupAllocation_Reserved13` | TField |  |  |
| 20 | `LI.GR.AL.RESERVED.12` | `LiLimitGroupAllocation_Reserved12` | TField |  |  |
| 21 | `LI.GR.AL.RESERVED.11` | `LiLimitGroupAllocation_Reserved11` | TField |  |  |
| 22 | `LI.GR.AL.RESERVED.10` | `LiLimitGroupAllocation_Reserved10` | TField |  |  |
| 23 | `LI.GR.AL.RESERVED.9` | `LiLimitGroupAllocation_Reserved9` | TField |  |  |
| 24 | `LI.GR.AL.RESERVED.8` | `LiLimitGroupAllocation_Reserved8` | TField |  |  |
| 25 | `LI.GR.AL.RESERVED.7` | `LiLimitGroupAllocation_Reserved7` | TField |  |  |
| 26 | `LI.GR.AL.RESERVED.6` | `LiLimitGroupAllocation_Reserved6` | TField |  |  |
| 27 | `LI.GR.AL.RESERVED.5` | `LiLimitGroupAllocation_Reserved5` | TField |  |  |
| 28 | `LI.GR.AL.RESERVED.4` | `LiLimitGroupAllocation_Reserved4` | TField |  |  |
| 29 | `LI.GR.AL.RESERVED.3` | `LiLimitGroupAllocation_Reserved3` | TField |  |  |
| 30 | `LI.GR.AL.RESERVED.2` | `LiLimitGroupAllocation_Reserved2` | TField |  |  |
| 31 | `LI.GR.AL.RESERVED.1` | `LiLimitGroupAllocation_Reserved1` | TField |  |  |
