# LIMIT.CHANGE — Table Schema

> Source: `INSERTS/I_F.LIMIT.CHANGE` in `LI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.CH.CUSTOMER.NO` | `LimitChange_CustomerNo` |  |  |  |
| 2 | `LI.CH.LIABILITY.NO` | `LimitChange_LiabilityNo` |  |  |  |
| 3 | `LI.CH.CREDIT.LINE.NO` | `LimitChange_CreditLineNo` |  |  |  |
| 4 | `LI.CH.NEW.CURRENCY` | `LimitChange_NewCurrency` |  |  |  |
| 5 | `LI.CH.NEW.CHECK.LIMIT` | `LimitChange_NewCheckLimit` |  |  |  |
| 6 | `LI.CH.LIMIT.REFERENCE` | `LimitChange_LimitReference` |  |  |  |
| 7 | `LI.CH.NEW.PERCENTAGE` | `LimitChange_NewPercentage` |  |  |  |
| 8 | `LI.CH.LIM.BAND.LEVEL` | `LimitChange_LimBandLevel` |  |  |  |
| 9 | `LI.CH.MATUR.PERIOD` | `LimitChange_MaturPeriod` |  |  |  |
| 10 | `LI.CH.NEW.PERC` | `LimitChange_NewPerc` |  |  |  |
| 11 | `LI.CH.LIMIT.SUBR` | `LimitChange_LimitSubr` |  |  |  |
| 12 | `LI.CH.PERCENTAGE.CAP` | `LimitChange_PercentageCap` |  |  |  |
| 13 | `LI.CH.PERCENTAGE.FLR` | `LimitChange_PercentageFlr` |  |  |  |
| 14 | `LI.CH.PERC.CALC.BASIS` | `LimitChange_PercCalcBasis` |  |  |  |
| 15 | `LI.CH.NET.OUTSTANDING` | `LimitChange_NetOutstanding` | TField | No | Used to change the status of the NET.OUTSTANDING flag on the SYSTEM record of LIMIT.PARAMETER. The actual change will take place at the beginning of the next limits batch processing. This field will be reset to null during the Limits end of day processing. Validation Rules: Optional input. Values can be "Y", "N" or blank. The value entered depends on the contents of the field NET.OUTSTANDING on the LIMIT.PARAMETER record called SYSTEM. A value of "Y" is acceptable if the LIMIT.PARAMETER is set to "N". A value of "N" is acceptable if the LIMIT.PARAMETER is set to "Y". |
| 16 | `LI.CH.ORDER.PRIORITY` | `LimitChange_OrderPriority` | TField |  | "MANUAL" or "NONE". Allows or disallows manually setting allocation priorities in Collateral Right records. The corresponding field will be set to this value in each of the COLLATERAL.PARAMETER records. Validation Rules: "MANUAL" or "NONE". |
| 17 | `LI.CH.SHARING.GROUP.KEY` | `LimitChange_SharingGroupKey` |  |  |  |
| 18 | `LI.CH.REMOVE.CUSTOMER` | `LimitChange_RemoveCustomer` |  |  |  |
| 19 | `LI.CH.REMOVE.PRODUCT` | `LimitChange_RemoveProduct` |  |  |  |
| 20 | `LI.CH.GROUP.CUSTOMER` | `LimitChange_GroupCustomer` |  |  |  |
| 21 | `LI.CH.NEW.CUS.PRIORITY` | `LimitChange_NewCusPriority` |  |  |  |
| 22 | `LI.CH.NEW.GROUP.ORDER` | `LimitChange_NewGroupOrder` |  |  |  |
| 23 | `LI.CH.ALLOCATION.KEY` | `LimitChange_AllocationKey` |  |  |  |
| 24 | `LI.CH.NEW.COVER.LIABILITY` | `LimitChange_NewCoverLiability` |  |  |  |
| 25 | `LI.CH.NEW.USE.COLLATERAL` | `LimitChange_NewUseCollateral` |  |  |  |
| 26 | `LI.CH.NEW.PRIORITY.RECEIVE` | `LimitChange_NewPriorityReceive` |  |  |  |
| 27 | `LI.CH.NEW.ASSET.ORDER` | `LimitChange_NewAssetOrder` |  |  |  |
| 28 | `LI.CH.ALLOC.RESERVED10` | `LimitChange_AllocReserved10` |  |  |  |
| 29 | `LI.CH.ALLOC.RESERVED9` | `LimitChange_AllocReserved9` |  |  |  |
| 30 | `LI.CH.ALLOC.RESERVED8` | `LimitChange_AllocReserved8` |  |  |  |
| 31 | `LI.CH.ALLOC.RESERVED7` | `LimitChange_AllocReserved7` |  |  |  |
| 32 | `LI.CH.ALLOC.RESERVED6` | `LimitChange_AllocReserved6` |  |  |  |
| 33 | `LI.CH.ALLOC.RESERVED5` | `LimitChange_AllocReserved5` |  |  |  |
| 34 | `LI.CH.ALLOC.RESERVED4` | `LimitChange_AllocReserved4` |  |  |  |
| 35 | `LI.CH.ALLOC.RESERVED3` | `LimitChange_AllocReserved3` |  |  |  |
| 36 | `LI.CH.ALLOC.RESERVED2` | `LimitChange_AllocReserved2` |  |  |  |
| 37 | `LI.CH.ALLOC.RESERVED1` | `LimitChange_AllocReserved1` |  |  |  |
| 38 | `LI.CH.RESERVED5` | `LimitChange_Reserved5` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 39 | `LI.CH.RESERVED4` | `LimitChange_Reserved4` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 40 | `LI.CH.RESERVED3` | `LimitChange_Reserved3` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 41 | `LI.CH.LOCAL.REF` | `LimitChange_LocalRef` |  |  |  |
| 42 | `LI.CH.RESERVED1` | `LimitChange_Reserved1` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 43 | `LI.CH.RECORD.STATUS` | `LimitChange_RecordStatus` | String |  |  |
| 44 | `LI.CH.CURR.NO` | `LimitChange_CurrNo` | String |  |  |
| 45 | `LI.CH.INPUTTER` | `LimitChange_Inputter` |  |  |  |
| 46 | `LI.CH.DATE.TIME` | `LimitChange_DateTime` |  |  |  |
| 47 | `LI.CH.AUTHORISER` | `LimitChange_Authoriser` | String |  |  |
| 48 | `LI.CH.CO.CODE` | `LimitChange_CoCode` | String |  |  |
| 49 | `LI.CH.DEPT.CODE` | `LimitChange_DeptCode` | String |  |  |
| 50 | `LI.CH.AUDITOR.CODE` | `LimitChange_AuditorCode` | String |  |  |
| 51 | `LI.CH.AUDIT.DATE.TIME` | `LimitChange_AuditDateTime` | String |  |  |
