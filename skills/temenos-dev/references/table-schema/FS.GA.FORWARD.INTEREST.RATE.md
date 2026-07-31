# FS.GA.FORWARD.INTEREST.RATE — Table Schema

> Source: `INSERTS/I_F.FS.GA.FORWARD.INTEREST.RATE` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FORWARD.INTEREST.RATE.PARENT.REF.ID` | `FsGaForwardInterestRate_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FORWARD.INTEREST.RATE.ORA.ROWID` | `FsGaForwardInterestRate_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FORWARD.INTEREST.RATE.INTEREST.RATE.TYPE` | `FsGaForwardInterestRate_InterestRateType` | TField |  | Interest/ forward exchange rate maintenance based on source ( LIBOR/MIBOR) Multifonds DB Column is TYP_TAUX. |
| 4 | `FS.GA.FORWARD.INTEREST.RATE.LOCAL.CURRENCY` | `FsGaForwardInterestRate_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 5 | `FS.GA.FORWARD.INTEREST.RATE.MATURITY.CODE` | `FsGaForwardInterestRate_MaturityCode` | TField |  | Maturity code of the floating interest rate that needs to be applied for commission accrual on a lending/borrowing transaction Multifonds DB Column is CODE_MOIS. |
| 6 | `FS.GA.FORWARD.INTEREST.RATE.VALUE.DATE` | `FsGaForwardInterestRate_ValueDate` | TField |  | Value date of the Forward Interest/exchange rate Multifonds DB Column is DFIXING. |
| 7 | `FS.GA.FORWARD.INTEREST.RATE.ASSETS.INTEREST.RATE` | `FsGaForwardInterestRate_AssetsInterestRate` | TField |  | Interest rate to be used for the delivery side of the forward exchange contract. Multifonds DB Column is TAUX_DB. |
| 8 | `FS.GA.FORWARD.INTEREST.RATE.LIABILITIES.INTEREST.RATE` | `FsGaForwardInterestRate_LiabilitiesInterestRate` | TField |  | Interest rate to be used for the payment side of the forward exchange contract. Multifonds DB Column is TAUX_CR. |
| 9 | `FS.GA.FORWARD.INTEREST.RATE.CREATED.USER` | `FsGaForwardInterestRate_CreatedUser` | TField |  | Created User Multifonds DB Column is XUSER_CRE. |
| 10 | `FS.GA.FORWARD.INTEREST.RATE.UPDATED.USER2` | `FsGaForwardInterestRate_UpdatedUser2` | TField |  | Updated User2 Multifonds DB Column is XUSER_UPD. |
| 11 | `FS.GA.FORWARD.INTEREST.RATE.RATE.DATE` | `FsGaForwardInterestRate_RateDate` | TField |  | Exchange, Interest Rate date Multifonds DB Column is DCTA_TCHG. |
| 12 | `FS.GA.FORWARD.INTEREST.RATE.INTEREST.ACTION.BID` | `FsGaForwardInterestRate_InterestActionBid` | TField |  | Interest Action BID Multifonds DB Column is TAUX_ACT_BID. |
| 13 | `FS.GA.FORWARD.INTEREST.RATE.INTEREST.ACTION.OFFER` | `FsGaForwardInterestRate_InterestActionOffer` | TField |  | Interest Action Offer Multifonds DB Column is TAUX_ACT_OFFER. |
| 14 | `FS.GA.FORWARD.INTEREST.RATE.INTEREST.ACTION.ANNUAL.BID` | `FsGaForwardInterestRate_InterestActionAnnualBid` | TField |  | Interest Action Annual Bid Multifonds DB Column is TAUX_ACT_ANNUEL_BID. |
| 15 | `FS.GA.FORWARD.INTEREST.RATE.INTEREST.ACTION.ANNUAL.OFFER` | `FsGaForwardInterestRate_InterestActionAnnualOffer` | TField |  | Interest Action Annual Offer Multifonds DB Column is TAUX_ACT_ANNUEL_OFFER. |
| 16 | `FS.GA.FORWARD.INTEREST.RATE.ZERO.COUPON.INTEREST.BID` | `FsGaForwardInterestRate_ZeroCouponInterestBid` | TField |  | Zero Coupon Interest Bid Multifonds DB Column is TAUX_ZERO_COUPON_BID. |
| 17 | `FS.GA.FORWARD.INTEREST.RATE.ZERO.COUPON.INTEREST.OFFER` | `FsGaForwardInterestRate_ZeroCouponInterestOffer` | TField |  | Zero Coupon Interest Offer Multifonds DB Column is TAUX_ZERO_COUPON_OFFER. |
| 18 | `FS.GA.FORWARD.INTEREST.RATE.PROCESS.ID` | `FsGaForwardInterestRate_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 19 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED10` | `FsGaForwardInterestRate_Reserved10` | TField |  |  |
| 20 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED9` | `FsGaForwardInterestRate_Reserved9` | TField |  |  |
| 21 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED8` | `FsGaForwardInterestRate_Reserved8` | TField |  |  |
| 22 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED7` | `FsGaForwardInterestRate_Reserved7` | TField |  |  |
| 23 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED6` | `FsGaForwardInterestRate_Reserved6` | TField |  |  |
| 24 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED5` | `FsGaForwardInterestRate_Reserved5` | TField |  |  |
| 25 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED4` | `FsGaForwardInterestRate_Reserved4` | TField |  |  |
| 26 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED3` | `FsGaForwardInterestRate_Reserved3` | TField |  |  |
| 27 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED2` | `FsGaForwardInterestRate_Reserved2` | TField |  |  |
| 28 | `FS.GA.FORWARD.INTEREST.RATE.RESERVED1` | `FsGaForwardInterestRate_Reserved1` | TField |  |  |
| 29 | `FS.GA.FORWARD.INTEREST.RATE.LOCAL.REF` | `FsGaForwardInterestRate_LocalRef` |  |  |  |
| 30 | `FS.GA.FORWARD.INTEREST.RATE.OVERRIDE` | `FsGaForwardInterestRate_Override` |  |  |  |
| 31 | `FS.GA.FORWARD.INTEREST.RATE.RECORD.STATUS` | `FsGaForwardInterestRate_RecordStatus` | String |  |  |
| 32 | `FS.GA.FORWARD.INTEREST.RATE.CURR.NO` | `FsGaForwardInterestRate_CurrNo` | String |  |  |
| 33 | `FS.GA.FORWARD.INTEREST.RATE.INPUTTER` | `FsGaForwardInterestRate_Inputter` |  |  |  |
| 34 | `FS.GA.FORWARD.INTEREST.RATE.DATE.TIME` | `FsGaForwardInterestRate_DateTime` |  |  |  |
| 35 | `FS.GA.FORWARD.INTEREST.RATE.AUTHORISER` | `FsGaForwardInterestRate_Authoriser` | String |  |  |
| 36 | `FS.GA.FORWARD.INTEREST.RATE.CO.CODE` | `FsGaForwardInterestRate_CoCode` | String |  |  |
| 37 | `FS.GA.FORWARD.INTEREST.RATE.DEPT.CODE` | `FsGaForwardInterestRate_DeptCode` | String |  |  |
| 38 | `FS.GA.FORWARD.INTEREST.RATE.AUDITOR.CODE` | `FsGaForwardInterestRate_AuditorCode` | String |  |  |
| 39 | `FS.GA.FORWARD.INTEREST.RATE.AUDIT.DATE.TIME` | `FsGaForwardInterestRate_AuditDateTime` | String |  |  |
