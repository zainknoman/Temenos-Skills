# CBTMGT.AUCTION.UNALLOCATED.DATA — Table Schema

> Source: `INSERTS/I_F.CBTMGT.AUCTION.UNALLOCATED.DATA` in `CBTMGT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TMGT.ELIGIBLE.NOMINAL` | `CbtmgtAuctionUnallocatedData_EligibleNominal` | TField |  | Updated with nominal that is eligible for this bid. It includes the odd lot nominal also. |
| 2 | `TMGT.ALLOCATED.NOMINAL` | `CbtmgtAuctionUnallocatedData_AllocatedNominal` | TField |  | Updated with nominal that is allocated for this bid. It is the nominal for which order is executed. |
| 3 | `TMGT.UNALLOCATED.NOMINAL` | `CbtmgtAuctionUnallocatedData_UnallocatedNominal` | TField |  | Updated with nominal that is not allocated for this bid as result of odd lot. |
| 4 | `TMGT.SECURITY.NO` | `CbtmgtAuctionUnallocatedData_SecurityNo` | TField |  | Security Id involved in the Auction |
| 5 | `TMGT.RESERVED.1` | `CbtmgtAuctionUnallocatedData_Reserved1` | TField |  | Reserved field for future use |
| 6 | `TMGT.RESERVED.2` | `CbtmgtAuctionUnallocatedData_Reserved2` | TField |  | Reserved field for future use |
| 7 | `TMGT.RESERVED.3` | `CbtmgtAuctionUnallocatedData_Reserved3` | TField |  | Reserved field for future use |
| 8 | `TMGT.RESERVED.4` | `CbtmgtAuctionUnallocatedData_Reserved4` | TField |  | Reserved field for future use |
| 10 | `TMGT.RESERVED.6` | `CbtmgtAuctionUnallocatedData_Reserved6` | TField |  | Reserved field for future use |
| 11 | `TMGT.RESERVED.7` | `CbtmgtAuctionUnallocatedData_Reserved7` | TField |  | Reserved field for future use |
| 12 | `TMGT.RESERVED.8` | `CbtmgtAuctionUnallocatedData_Reserved8` | TField |  | Reserved field for future use |
| 13 | `TMGT.RESERVED.9` | `CbtmgtAuctionUnallocatedData_Reserved9` | TField |  | Reserved field for future use |
| 14 | `TMGT.RESERVED.10` | `CbtmgtAuctionUnallocatedData_Reserved10` | TField |  | Reserved field for future use |
