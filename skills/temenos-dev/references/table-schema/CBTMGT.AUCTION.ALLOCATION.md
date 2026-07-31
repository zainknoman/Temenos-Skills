# CBTMGT.AUCTION.ALLOCATION — Table Schema

> Source: `INSERTS/I_F.CBTMGT.AUCTION.ALLOCATION` in `CBTMGT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TMGT.FINAL.SECURITY.RATE` | `CbtmgtAuctionAllocation_FinalSecurityRate` | TField |  | Final rate after auction is updated in this field |
| 2 | `TMGT.FINAL.SECURITY.PRICE` | `CbtmgtAuctionAllocation_FinalSecurityPrice` | TField |  | Final price decided by bank after auction is updated in this field |
| 3 | `TMGT.CUTOFF.PRICE` | `CbtmgtAuctionAllocation_CutoffPrice` | TField |  | Bids above Cutoff price are considered as unsuccessful. Updated by bank |
| 4 | `TMGT.NON.COMPETITIVE.BID.LIMIT` | `CbtmgtAuctionAllocation_NonCompetitiveBidLimit` | TField |  | If there is a CAP on each Noncompetitive bid, then corresponding value is updated here |
| 5 | `TMGT.AUCTION.TYPE` | `CbtmgtAuctionAllocation_AuctionType` | TField |  | Possible values are Uniform and Multiprice. Defines the auction type |
| 6 | `TMGT.ALLOCATION.METHOD` | `CbtmgtAuctionAllocation_AllocationMethod` | TField |  | Possible values are Facevalue and Price. Allocation method is updated in this field |
| 7 | `TMGT.ALLOCATION.TYPE` | `CbtmgtAuctionAllocation_AllocationType` | TField |  | Possible values are Prorata and Normal. Allocation type is updated in this field |
| 8 | `TMGT.AUCTION.RATE` | `CbtmgtAuctionAllocation_AuctionRate` | TField |  | Field is to define if auction follows DISCOUNT rate or YEILD rate bids |
| 9 | `TMGT.STATUS` | `CbtmgtAuctionAllocation_Status` | TField |  | Status of the allocation. This field will be updated as Completed when service completes the allocation |
| 10 | `TMGT.LOCAL.REF` | `CbtmgtAuctionAllocation_LocalRef` |  |  |  |
| 11 | `TMGT.RESERVED.10` | `CbtmgtAuctionAllocation_Reserved10` | TField |  | Reserved field for future use |
| 12 | `TMGT.RESERVED.9` | `CbtmgtAuctionAllocation_Reserved9` | TField |  | Reserved field for future use |
| 13 | `TMGT.RESERVED.8` | `CbtmgtAuctionAllocation_Reserved8` | TField |  | Reserved field for future use |
| 14 | `TMGT.RESERVED.7` | `CbtmgtAuctionAllocation_Reserved7` | TField |  | Reserved field for future use |
| 15 | `TMGT.RESERVED.6` | `CbtmgtAuctionAllocation_Reserved6` | TField |  | Reserved field for future use |
| 16 | `TMGT.RESERVED.5` | `CbtmgtAuctionAllocation_Reserved5` | TField |  | Reserved field for future use |
| 17 | `TMGT.RESERVED.4` | `CbtmgtAuctionAllocation_Reserved4` | TField |  | Reserved field for future use |
| 18 | `TMGT.RESERVED.3` | `CbtmgtAuctionAllocation_Reserved3` | TField |  | Reserved field for future use |
| 19 | `TMGT.RESERVED.2` | `CbtmgtAuctionAllocation_Reserved2` | TField |  | Reserved field for future use |
| 20 | `TMGT.RESERVED.1` | `CbtmgtAuctionAllocation_Reserved1` | TField |  | Reserved field for future use |
| 21 | `TMGT.OVERRIDE` | `CbtmgtAuctionAllocation_Override` |  |  |  |
| 22 | `TMGT.RECORD.STATUS` | `CbtmgtAuctionAllocation_RecordStatus` | String |  |  |
| 23 | `TMGT.CURR.NO` | `CbtmgtAuctionAllocation_CurrNo` | String |  |  |
| 24 | `TMGT.INPUTTER` | `CbtmgtAuctionAllocation_Inputter` |  |  |  |
| 25 | `TMGT.DATE.TIME` | `CbtmgtAuctionAllocation_DateTime` |  |  |  |
| 26 | `TMGT.AUTHORISER` | `CbtmgtAuctionAllocation_Authoriser` | String |  |  |
| 27 | `TMGT.CO.CODE` | `CbtmgtAuctionAllocation_CoCode` | String |  |  |
| 28 | `TMGT.DEPT.CODE` | `CbtmgtAuctionAllocation_DeptCode` | String |  |  |
| 29 | `TMGT.AUDITOR.CODE` | `CbtmgtAuctionAllocation_AuditorCode` | String |  |  |
| 30 | `TMGT.AUDIT.DATE.TIME` | `CbtmgtAuctionAllocation_AuditDateTime` | String |  |  |
