# CO.ALLOCATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.CO.ALLOCATION.DETAILS` in `CO_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COALD.LIABILITY.ID` | `CoAllocationDetails_LiabilityId` |  |  |  |
| 2 | `COALD.LIABILITY.CCY` | `CoAllocationDetails_LiabilityCcy` |  |  |  |
| 3 | `COALD.LIABILITY.AMOUNT` | `CoAllocationDetails_LiabilityAmount` |  |  |  |
| 4 | `COALD.LIABILITY.CATEG` | `CoAllocationDetails_LiabilityCateg` |  |  |  |
| 5 | `COALD.RESERVED.11` | `CoAllocationDetails_Reserved11` |  |  |  |
| 6 | `COALD.RESERVED.10` | `CoAllocationDetails_Reserved10` |  |  |  |
| 7 | `COALD.RESERVED.9` | `CoAllocationDetails_Reserved9` |  |  |  |
| 8 | `COALD.RESERVED.8` | `CoAllocationDetails_Reserved8` |  |  |  |
| 9 | `COALD.RESERVED.7` | `CoAllocationDetails_Reserved7` |  |  |  |
| 10 | `COALD.RESERVED.6` | `CoAllocationDetails_Reserved6` |  |  |  |
| 11 | `COALD.COLLATERAL.ID` | `CoAllocationDetails_CollateralId` |  |  |  |
| 12 | `COALD.COLLATERAL.CCY` | `CoAllocationDetails_CollateralCcy` |  |  |  |
| 13 | `COALD.AVAIL.AMT` | `CoAllocationDetails_AvailAmt` |  |  |  |
| 14 | `COALD.ALLOCATED.AMT` | `CoAllocationDetails_AllocatedAmt` |  |  |  |
| 15 | `COALD.UNALLOCATED.AMT` | `CoAllocationDetails_UnallocatedAmt` |  |  |  |
| 16 | `COALD.RESERVED.5` | `CoAllocationDetails_Reserved5` |  |  |  |
| 17 | `COALD.RESERVED.4` | `CoAllocationDetails_Reserved4` |  |  |  |
| 18 | `COALD.RESERVED.3` | `CoAllocationDetails_Reserved3` |  |  |  |
| 19 | `COALD.RESERVED.2` | `CoAllocationDetails_Reserved2` |  |  |  |
| 20 | `COALD.RESERVED.1` | `CoAllocationDetails_Reserved1` |  |  |  |
| 21 | `COALD.TOTAL.ALLOC` | `CoAllocationDetails_TotalAlloc` |  |  |  |
| 22 | `COALD.TOTAL.UNALLOC` | `CoAllocationDetails_TotalUnalloc` |  |  |  |
