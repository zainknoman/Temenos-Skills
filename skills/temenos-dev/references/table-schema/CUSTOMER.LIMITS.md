# CUSTOMER.LIMITS — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.LIMITS` in `LI_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.CUL.RISK.GROUP.ID` | `CustomerLimits_RiskGroupId` | TField |  |  |
| 2 | `LI.CUL.LIABILITY.NO` | `CustomerLimits_LiabilityNo` | TField |  |  |
| 3 | `LI.CUL.LIMIT.ID` | `CustomerLimits_LimitId` | TField |  |  |
| 4 | `LI.CUL.CREDIT.LINE.NO` | `CustomerLimits_CreditLineNo` | TField |  |  |
| 5 | `LI.CUL.RECORD.PARENT` | `CustomerLimits_RecordParent` | TField |  |  |
| 6 | `LI.CUL.LIMIT.PRODUCT` | `CustomerLimits_LimitProduct` | TField |  |  |
| 7 | `LI.CUL.SERIAL.NUMBER` | `CustomerLimits_SerialNumber` | TField |  |  |
| 8 | `LI.CUL.LIMIT.CURRENCY` | `CustomerLimits_LimitCurrency` | TField |  |  |
| 9 | `LI.CUL.BUSINESS.UNIT` | `CustomerLimits_BusinessUnit` | TField |  |  |
| 10 | `LI.CUL.EXPIRY.DATE` | `CustomerLimits_ExpiryDate` | TField |  |  |
| 11 | `LI.CUL.TIME.BAND` | `CustomerLimits_TimeBand` | TField |  |  |
| 12 | `LI.CUL.INTERNAL.AMT` | `CustomerLimits_InternalAmt` | TField |  |  |
| 13 | `LI.CUL.ADVISED.AMT` | `CustomerLimits_AdvisedAmt` | TField |  |  |
| 14 | `LI.CUL.TOTAL.OS` | `CustomerLimits_TotalOs` | TField |  |  |
| 15 | `LI.CUL.AVAIL.AMT` | `CustomerLimits_AvailAmt` | TField |  |  |
| 16 | `LI.CUL.EXCESS.AMT` | `CustomerLimits_ExcessAmt` | TField |  |  |
| 17 | `LI.CUL.TOTAL.COMMIT` | `CustomerLimits_TotalCommit` | TField |  |  |
| 18 | `LI.CUL.TOTAL.CR` | `CustomerLimits_TotalCr` | TField |  |  |
| 19 | `LI.CUL.TOTAL.DR` | `CustomerLimits_TotalDr` | TField |  |  |
| 20 | `LI.CUL.REPORT.CURRENCY` | `CustomerLimits_ReportCurrency` | TField |  |  |
| 21 | `LI.CUL.EXCH.RATE` | `CustomerLimits_ExchRate` | TField |  |  |
| 22 | `LI.CUL.IDL.TYPE` | `CustomerLimits_IdlType` |  |  |  |
| 23 | `LI.CUL.IDL.APPROVED.AMT` | `CustomerLimits_IdlApprovedAmt` |  |  |  |
| 24 | `LI.CUL.IDL.ADVISED.AMT` | `CustomerLimits_IdlAdvisedAmt` |  |  |  |
| 25 | `LI.CUL.LIMIT.TYPE` | `CustomerLimits_LimitType` | TField |  |  |
| 26 | `LI.CUL.REL.CUSTOMER` | `CustomerLimits_RelCustomer` |  |  |  |
| 27 | `LI.CUL.AGG.CUSTOMER.ID` | `CustomerLimits_AggCustomerId` |  |  |  |
| 28 | `LI.CUL.AGG.CUSTOMER.REL` | `CustomerLimits_AggCustomerRel` |  |  |  |
| 29 | `LI.CUL.JOINT.LIMIT` | `CustomerLimits_JointLimit` | TField |  |  |
| 30 | `LI.CUL.SHARED.LIMIT` | `CustomerLimits_SharedLimit` | TField |  |  |
| 31 | `LI.CUL.LIMIT.NOTES` | `CustomerLimits_LimitNotes` |  |  |  |
| 32 | `LI.CUL.SESSION.ID` | `CustomerLimits_SessionId` | TField |  |  |
| 33 | `LI.CUL.SUB.GROUP` | `CustomerLimits_SubGroup` |  |  |  |
| 34 | `LI.CUL.ORIG.INTERNAL.AMT` | `CustomerLimits_OrigInternalAmt` | TField |  |  |
| 35 | `LI.CUL.ORIG.ADVISED.AMT` | `CustomerLimits_OrigAdvisedAmt` | TField |  |  |
| 36 | `LI.CUL.REPAID.AMOUNT` | `CustomerLimits_RepaidAmount` | TField |  |  |
| 37 | `LI.CUL.TOTAL.REPAID.AMT` | `CustomerLimits_TotalRepaidAmt` | TField |  |  |
| 38 | `LI.CUL.EXCESS.FLAG` | `CustomerLimits_ExcessFlag` | TField |  |  |
| 39 | `LI.CUL.FIXED.VARIABLE` | `CustomerLimits_FixedVariable` | TField |  |  |
| 40 | `LI.CUL.TOTAL.SECURED.AMOUNT` | `CustomerLimits_TotalSecuredAmount` | TField |  |  |
| 41 | `LI.CUL.MULTI.CUSTOMER.LIMIT` | `CustomerLimits_MultiCustomerLimit` | TField |  |  |
| 42 | `LI.CUL.GROUP.CLASS` | `CustomerLimits_GroupClass` | TField |  |  |
| 43 | `LI.CUL.AGGREGATION.EXISTS` | `CustomerLimits_AggregationExists` | TField |  |  |
| 44 | `LI.CUL.MAIN.GROUP.ID` | `CustomerLimits_MainGroupId` | TField |  |  |
| 45 | `LI.CUL.CREDIT.LINE.PRODUCT` | `CustomerLimits_CreditLineProduct` | TField |  |  |
| 46 | `LI.CUL.ONLINE.AMT` | `CustomerLimits_OnlineAmt` | TField |  |  |
| 47 | `LI.CUL.AMT.IN.UNITS` | `CustomerLimits_AmtInUnits` | TField |  |  |
| 48 | `LI.CUL.GV.INDICATOR` | `CustomerLimits_GvIndicator` | TField |  |  |
| 49 | `LI.CUL.SUB.ALLOCATION.AMT` | `CustomerLimits_SubAllocationAmt` | TField |  |  |
| 50 | `LI.CUL.BUFFER.TOTAL` | `CustomerLimits_BufferTotal` | TField |  |  |
| 51 | `LI.CUL.BUFFER.ALLOCATED` | `CustomerLimits_BufferAllocated` | TField |  |  |
