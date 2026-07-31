# LIMIT.CHANGE.HIST — Table Schema

> Source: `INSERTS/I_F.LIMIT.CHANGE.HIST` in `LI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.CH.HIST.CUSTOMER.NO` | `LimitChangeHist_CustomerNo` |  |  |  |
| 2 | `LI.CH.HIST.LIABILITY.NO` | `LimitChangeHist_LiabilityNo` |  |  |  |
| 3 | `LI.CH.HIST.CREDIT.LINE.NO` | `LimitChangeHist_CreditLineNo` |  |  |  |
| 4 | `LI.CH.HIST.NEW.CURRENCY` | `LimitChangeHist_NewCurrency` |  |  |  |
| 5 | `LI.CH.HIST.NEW.CHECK.LIMIT` | `LimitChangeHist_NewCheckLimit` |  |  |  |
| 6 | `LI.CH.HIST.LIMIT.REFERENCE` | `LimitChangeHist_LimitReference` |  |  |  |
| 7 | `LI.CH.HIST.NEW.PERCENTAGE` | `LimitChangeHist_NewPercentage` |  |  |  |
| 8 | `LI.CH.HIST.LIM.BAND.LEVEL` | `LimitChangeHist_LimBandLevel` |  |  |  |
| 9 | `LI.CH.HIST.MATUR.PERIOD` | `LimitChangeHist_MaturPeriod` |  |  |  |
| 10 | `LI.CH.HIST.NEW.PERC` | `LimitChangeHist_NewPerc` |  |  |  |
| 11 | `LI.CH.HIST.LIMIT.SUBR` | `LimitChangeHist_LimitSubr` |  |  |  |
| 12 | `LI.CH.HIST.PERCENTAGE.CAP` | `LimitChangeHist_PercentageCap` |  |  |  |
| 13 | `LI.CH.HIST.PERCENTAGE.FLR` | `LimitChangeHist_PercentageFlr` |  |  |  |
| 14 | `LI.CH.HIST.PERC.CALC.BASIS` | `LimitChangeHist_PercCalcBasis` |  |  |  |
| 15 | `LI.CH.HIST.NET.OUTSTANDING` | `LimitChangeHist_NetOutstanding` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 16 | `LI.CH.HIST.ORDER.PRIORITY` | `LimitChangeHist_OrderPriority` | TField |  |  |
| 17 | `LI.CH.HIST.SHARING.GROUP.KEY` | `LimitChangeHist_SharingGroupKey` |  |  |  |
| 18 | `LI.CH.HIST.REMOVE.CUSTOMER` | `LimitChangeHist_RemoveCustomer` |  |  |  |
| 19 | `LI.CH.HIST.REMOVE.PRODUCT` | `LimitChangeHist_RemoveProduct` |  |  |  |
| 20 | `LI.CH.HIST.GROUP.CUSTOMER` | `LimitChangeHist_GroupCustomer` |  |  |  |
| 21 | `LI.CH.HIST.NEW.CUS.PRIORITY` | `LimitChangeHist_NewCusPriority` |  |  |  |
| 22 | `LI.CH.HIST.NEW.GROUP.ORDER` | `LimitChangeHist_NewGroupOrder` |  |  |  |
| 23 | `LI.CH.HIST.ALLOCATION.KEY` | `LimitChangeHist_AllocationKey` |  |  |  |
| 24 | `LI.CH.HIST.NEW.COVER.LIABILITY` | `LimitChangeHist_NewCoverLiability` |  |  |  |
| 25 | `LI.CH.HIST.NEW.USE.COLLATERAL` | `LimitChangeHist_NewUseCollateral` |  |  |  |
| 26 | `LI.CH.HIST.NEW.PRIORITY.RECEIVE` | `LimitChangeHist_NewPriorityReceive` |  |  |  |
| 27 | `LI.CH.HIST.NEW.ASSET.ORDER` | `LimitChangeHist_NewAssetOrder` |  |  |  |
| 28 | `LI.CH.HIST.ALLOC.RESERVED10` | `LimitChangeHist_AllocReserved10` |  |  |  |
| 29 | `LI.CH.HIST.ALLOC.RESERVED9` | `LimitChangeHist_AllocReserved9` |  |  |  |
| 30 | `LI.CH.HIST.ALLOC.RESERVED8` | `LimitChangeHist_AllocReserved8` |  |  |  |
| 31 | `LI.CH.HIST.ALLOC.RESERVED7` | `LimitChangeHist_AllocReserved7` |  |  |  |
| 32 | `LI.CH.HIST.ALLOC.RESERVED6` | `LimitChangeHist_AllocReserved6` |  |  |  |
| 33 | `LI.CH.HIST.ALLOC.RESERVED5` | `LimitChangeHist_AllocReserved5` |  |  |  |
| 34 | `LI.CH.HIST.ALLOC.RESERVED4` | `LimitChangeHist_AllocReserved4` |  |  |  |
| 35 | `LI.CH.HIST.ALLOC.RESERVED3` | `LimitChangeHist_AllocReserved3` |  |  |  |
| 36 | `LI.CH.HIST.ALLOC.RESERVED2` | `LimitChangeHist_AllocReserved2` |  |  |  |
| 37 | `LI.CH.HIST.ALLOC.RESERVED1` | `LimitChangeHist_AllocReserved1` |  |  |  |
| 38 | `LI.CH.HIST.RESERVED5` | `LimitChangeHist_Reserved5` | TField |  |  |
| 39 | `LI.CH.HIST.RESERVED4` | `LimitChangeHist_Reserved4` | TField |  |  |
| 40 | `LI.CH.HIST.RESERVED3` | `LimitChangeHist_Reserved3` | TField |  |  |
| 41 | `LI.CH.HIST.RESERVED2` | `LimitChangeHist_Reserved2` | TField |  |  |
| 42 | `LI.CH.HIST.RESERVED1` | `LimitChangeHist_Reserved1` | TField |  |  |
| 43 | `LI.CH.HIST.RECORD.STATUS` | `LimitChangeHist_RecordStatus` | String |  |  |
| 44 | `LI.CH.HIST.CURR.NO` | `LimitChangeHist_CurrNo` | String |  |  |
| 45 | `LI.CH.HIST.INPUTTER` | `LimitChangeHist_Inputter` |  |  |  |
| 46 | `LI.CH.HIST.DATE.TIME` | `LimitChangeHist_DateTime` |  |  |  |
| 47 | `LI.CH.HIST.AUTHORISER` | `LimitChangeHist_Authoriser` | String |  |  |
| 48 | `LI.CH.HIST.CO.CODE` | `LimitChangeHist_CoCode` | String |  |  |
| 49 | `LI.CH.HIST.DEPT.CODE` | `LimitChangeHist_DeptCode` | String |  |  |
| 50 | `LI.CH.HIST.AUDITOR.CODE` | `LimitChangeHist_AuditorCode` | String |  |  |
| 51 | `LI.CH.HIST.AUDIT.DATE.TIME` | `LimitChangeHist_AuditDateTime` | String |  |  |
