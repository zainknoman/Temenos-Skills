# ILIPOA.ALLOCATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.ILIPOA.ALLOCATION.DETAILS` in `ILIPOA_Allocation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILIPOA.ALLOC.AUCTION.METHOD` | `IlipoaAllocationDetails_AuctionMethod` | TField |  | Type of auction method. Possible values are UNIFORM � FIFO, UNIFORM � PRO-RATA, UNIFORM - FIFO + PRO-RATA, DISCRIMINATORY, FIXED. |
| 2 | `ILIPOA.ALLOC.CLOSING.PRICE` | `IlipoaAllocationDetails_ClosingPrice` | TField |  | Closing price, yield, interest, ratio, and margin will be updated in this field. |
| 3 | `ILIPOA.ALLOC.AVERAGE.PRICE` | `IlipoaAllocationDetails_AveragePrice` | TField |  | Average price of the security. |
| 4 | `ILIPOA.ALLOC.CLOSING.PRICE.ALLOC.RATE` | `IlipoaAllocationDetails_ClosingPriceAllocRate` | TField |  | Allocation rate for the bid with closing price. |
| 5 | `ILIPOA.ALLOC.AVG.PRICE.ACCEPTANCE.RATE` | `IlipoaAllocationDetails_AvgPriceAcceptanceRate` | TField |  | Allocation rate for the bid with average price. |
| 6 | `ILIPOA.ALLOC.ALLOTMENT.RATE` | `IlipoaAllocationDetails_AllotmentRate` | TField |  | Pro-rata rate received by IPO coordinator. |
| 7 | `ILIPOA.ALLOC.TOTAL.ALLOCATED.QUANTITY` | `IlipoaAllocationDetails_TotalAllocatedQuantity` | TField |  | Total allocation quantity assigned for the bank. |
| 8 | `ILIPOA.ALLOC.IPO.STATUS` | `IlipoaAllocationDetails_IpoStatus` | TField |  | No Input field. Completed / In Progress are the possible values. |
| 9 | `ILIPOA.ALLOC.ROUNDING.METHOD` | `IlipoaAllocationDetails_RoundingMethod` | TField |  | Possible values are Up, Down, Standard, Lot and None. It is the rounding method to round of the allocated nominal. |
| 10 | `ILIPOA.ALLOC.ALLOCATION.STATUS` | `IlipoaAllocationDetails_AllocationStatus` | TField |  |  |
| 11 | `ILIPOA.ALLOC.SYSTEM.ALLOC.QUANTITY` | `IlipoaAllocationDetails_SystemAllocQuantity` | TField |  | Final Quantity allocated. No Input field. |
| 12 | `ILIPOA.ALLOC.RESERVED1` | `IlipoaAllocationDetails_Reserved1` | TField |  | Reserved for future use. |
| 13 | `ILIPOA.ALLOC.RESERVED2` | `IlipoaAllocationDetails_Reserved2` | TField |  | Reserved for future use. |
| 14 | `ILIPOA.ALLOC.RESERVED3` | `IlipoaAllocationDetails_Reserved3` | TField |  | Reserved for future use. |
| 15 | `ILIPOA.ALLOC.RESERVED4` | `IlipoaAllocationDetails_Reserved4` | TField |  | Reserved for future use. |
| 16 | `ILIPOA.ALLOC.RESERVED5` | `IlipoaAllocationDetails_Reserved5` | TField |  | Reserved for future use. |
| 17 | `ILIPOA.ALLOC.RESERVED6` | `IlipoaAllocationDetails_Reserved6` | TField |  | Reserved for future use. |
| 18 | `ILIPOA.ALLOC.RESERVED7` | `IlipoaAllocationDetails_Reserved7` | TField |  | Reserved for future use. |
| 19 | `ILIPOA.ALLOC.RESERVED8` | `IlipoaAllocationDetails_Reserved8` | TField |  | Reserved for future use. |
| 20 | `ILIPOA.ALLOC.RESERVED9` | `IlipoaAllocationDetails_Reserved9` | TField |  | Reserved for future use. |
| 21 | `ILIPOA.ALLOC.RESERVED10` | `IlipoaAllocationDetails_Reserved10` | TField |  | Reserved for future use. |
| 22 | `ILIPOA.ALLOC.LOCAL.REF` | `IlipoaAllocationDetails_LocalRef` |  |  |  |
| 23 | `ILIPOA.ALLOC.OVERRIDE` | `IlipoaAllocationDetails_Override` |  |  |  |
| 24 | `ILIPOA.ALLOC.RECORD.STATUS` | `IlipoaAllocationDetails_RecordStatus` | String |  |  |
| 25 | `ILIPOA.ALLOC.CURR.NO` | `IlipoaAllocationDetails_CurrNo` | String |  |  |
| 26 | `ILIPOA.ALLOC.INPUTTER` | `IlipoaAllocationDetails_Inputter` |  |  |  |
| 27 | `ILIPOA.ALLOC.DATE.TIME` | `IlipoaAllocationDetails_DateTime` |  |  |  |
| 28 | `ILIPOA.ALLOC.AUTHORISER` | `IlipoaAllocationDetails_Authoriser` | String |  |  |
| 29 | `ILIPOA.ALLOC.CO.CODE` | `IlipoaAllocationDetails_CoCode` | String |  |  |
| 30 | `ILIPOA.ALLOC.DEPT.CODE` | `IlipoaAllocationDetails_DeptCode` | String |  |  |
| 31 | `ILIPOA.ALLOC.AUDITOR.CODE` | `IlipoaAllocationDetails_AuditorCode` | String |  |  |
| 32 | `ILIPOA.ALLOC.AUDIT.DATE.TIME` | `IlipoaAllocationDetails_AuditDateTime` | String |  |  |
