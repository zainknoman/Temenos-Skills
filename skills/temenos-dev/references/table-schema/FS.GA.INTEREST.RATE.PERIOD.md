# FS.GA.INTEREST.RATE.PERIOD — Table Schema

> Source: `INSERTS/I_F.FS.GA.INTEREST.RATE.PERIOD` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INTEREST.RATE.PERIOD.PARENT.REF.ID` | `FsGaInterestRatePeriod_ParentRefId` |  |  |  |
| 2 | `FS.GA.INTEREST.RATE.PERIOD.ORA.ROWID` | `FsGaInterestRatePeriod_OraRowid` |  |  |  |
| 3 | `FS.GA.INTEREST.RATE.PERIOD.SEQ.NUMBER` | `FsGaInterestRatePeriod_SeqNumber` |  |  |  |
| 4 | `FS.GA.INTEREST.RATE.PERIOD.INTERNAL.SECURITY.ID` | `FsGaInterestRatePeriod_InternalSecurityId` |  |  |  |
| 5 | `FS.GA.INTEREST.RATE.PERIOD.FROM.DT` | `FsGaInterestRatePeriod_FromDt` |  |  |  |
| 6 | `FS.GA.INTEREST.RATE.PERIOD.TO.DATE` | `FsGaInterestRatePeriod_ToDate` |  |  |  |
| 7 | `FS.GA.INTEREST.RATE.PERIOD.REFERENCE.RATE.FRN` | `FsGaInterestRatePeriod_ReferenceRateFrn` |  |  |  |
| 8 | `FS.GA.INTEREST.RATE.PERIOD.PIK.FACTOR` | `FsGaInterestRatePeriod_PikFactor` |  |  |  |
| 9 | `FS.GA.INTEREST.RATE.PERIOD.PIK.INTEREST.RATE` | `FsGaInterestRatePeriod_PikInterestRate` |  |  |  |
| 10 | `FS.GA.INTEREST.RATE.PERIOD.REFIX.PRICE.FRN` | `FsGaInterestRatePeriod_RefixPriceFrn` |  |  |  |
| 11 | `FS.GA.INTEREST.RATE.PERIOD.REFERENCE.RATE.AARR` | `FsGaInterestRatePeriod_ReferenceRateAarr` |  |  |  |
| 12 | `FS.GA.INTEREST.RATE.PERIOD.BALANCE.PRINCIPLE` | `FsGaInterestRatePeriod_BalancePrinciple` |  |  |  |
| 13 | `FS.GA.INTEREST.RATE.PERIOD.INTEREST.RATE.SEC.MASTER` | `FsGaInterestRatePeriod_InterestRateSecMaster` |  |  |  |
| 14 | `FS.GA.INTEREST.RATE.PERIOD.REFERENCE.RATE.TOT` | `FsGaInterestRatePeriod_ReferenceRateTot` |  |  |  |
| 15 | `FS.GA.INTEREST.RATE.PERIOD.FIXING.DATE.FRN` | `FsGaInterestRatePeriod_FixingDateFrn` |  |  |  |
| 16 | `FS.GA.INTEREST.RATE.PERIOD.REFERENCE.RATE.ORIGINAL` | `FsGaInterestRatePeriod_ReferenceRateOriginal` |  |  |  |
| 17 | `FS.GA.INTEREST.RATE.PERIOD.COMPOSITE.RATE` | `FsGaInterestRatePeriod_CompositeRate` |  |  |  |
| 18 | `FS.GA.INTEREST.RATE.PERIOD.COMPOSITE.SPREAD.RATE` | `FsGaInterestRatePeriod_CompositeSpreadRate` |  |  |  |
| 19 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED10` | `FsGaInterestRatePeriod_Reserved10` |  |  |  |
| 20 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED9` | `FsGaInterestRatePeriod_Reserved9` |  |  |  |
| 21 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED8` | `FsGaInterestRatePeriod_Reserved8` |  |  |  |
| 22 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED7` | `FsGaInterestRatePeriod_Reserved7` |  |  |  |
| 23 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED6` | `FsGaInterestRatePeriod_Reserved6` |  |  |  |
| 24 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED5` | `FsGaInterestRatePeriod_Reserved5` |  |  |  |
| 25 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED4` | `FsGaInterestRatePeriod_Reserved4` |  |  |  |
| 26 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED3` | `FsGaInterestRatePeriod_Reserved3` |  |  |  |
| 27 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED2` | `FsGaInterestRatePeriod_Reserved2` |  |  |  |
| 28 | `FS.GA.INTEREST.RATE.PERIOD.RESERVED1` | `FsGaInterestRatePeriod_Reserved1` |  |  |  |
| 29 | `FS.GA.INTEREST.RATE.PERIOD.LOCAL.REF` | `FsGaInterestRatePeriod_LocalRef` |  |  |  |
| 30 | `FS.GA.INTEREST.RATE.PERIOD.OVERRIDE` | `FsGaInterestRatePeriod_Override` |  |  |  |
| 31 | `FS.GA.INTEREST.RATE.PERIOD.RECORD.STATUS` | `FsGaInterestRatePeriod_RecordStatus` |  |  |  |
| 32 | `FS.GA.INTEREST.RATE.PERIOD.CURR.NO` | `FsGaInterestRatePeriod_CurrNo` |  |  |  |
| 33 | `FS.GA.INTEREST.RATE.PERIOD.INPUTTER` | `FsGaInterestRatePeriod_Inputter` |  |  |  |
| 34 | `FS.GA.INTEREST.RATE.PERIOD.DATE.TIME` | `FsGaInterestRatePeriod_DateTime` |  |  |  |
| 35 | `FS.GA.INTEREST.RATE.PERIOD.AUTHORISER` | `FsGaInterestRatePeriod_Authoriser` |  |  |  |
| 36 | `FS.GA.INTEREST.RATE.PERIOD.CO.CODE` | `FsGaInterestRatePeriod_CoCode` |  |  |  |
| 37 | `FS.GA.INTEREST.RATE.PERIOD.DEPT.CODE` | `FsGaInterestRatePeriod_DeptCode` |  |  |  |
| 38 | `FS.GA.INTEREST.RATE.PERIOD.AUDITOR.CODE` | `FsGaInterestRatePeriod_AuditorCode` |  |  |  |
| 39 | `FS.GA.INTEREST.RATE.PERIOD.AUDIT.DATE.TIME` | `FsGaInterestRatePeriod_AuditDateTime` |  |  |  |
