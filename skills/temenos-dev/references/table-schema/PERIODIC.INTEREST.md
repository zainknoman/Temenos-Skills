# PERIODIC.INTEREST — Table Schema

> Source: `INSERTS/I_F.PERIODIC.INTEREST` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PI.DESCRIPTION` | `PeriodicInterest_Description` |  |  |  |
| 2 | `PI.DEFAULT.MIS.TABLE` | `PeriodicInterest_DefaultMisTable` | TField |  | Identifies the default M.I.S. rate to be taken when the ID has been defined in a transaction. 2 numeric characters in range 01-99. Default to the sequence number of the ID. The sequence number of this currency must already exist on the PERIODIC.INTEREST table. |
| 3 | `PI.REST.PERIOD` | `PeriodicInterest_RestPeriod` |  |  |  |
| 4 | `PI.REST.DATE` | `PeriodicInterest_RestDate` |  |  |  |
| 5 | `PI.DAYS.SINCE.SPOT` | `PeriodicInterest_DaysSinceSpot` |  |  |  |
| 6 | `PI.AMT` | `PeriodicInterest_Amt` |  |  |  |
| 7 | `PI.BID.RATE` | `PeriodicInterest_BidRate` |  |  |  |
| 8 | `PI.OFFER.RATE` | `PeriodicInterest_OfferRate` |  |  |  |
| 9 | `PI.BUILD.FWD.RATE` | `PeriodicInterest_BuildFwdRate` | TField | No | Flag to indicate if Forward rate for this currency should be calculated automatically using the bid and offer rate from the Periodic Interest table. Format; Y (Optional input) Only allowed for current record and for ID&apos;s having 01 as sequence number. |
| 10 | `PI.INT.TOLERANCE` | `PeriodicInterest_IntTolerance` | TField | No | Interest percentage tolerance allowed on money market contracts. A tolerance entered here will be used to check if an over-ride is required for any interest rate difference found on any money market contracts entered. The existence of a default INT.TOLERANCE in LMM.INSTALL.CONDS indicates that a check for an interest rate difference over-ride should be made on money market contracts. If the difference between the rate entered and that calculated exceeds the percentage tolerance entered here then an over-ride is required. 4 Numeric character input up to 100% (Optional input) This field may only be entered for records in this file with a leading sequence number of &apos;01&apos;. |
| 11 | `PI.MAX.INT.RATE` | `PeriodicInterest_MaxIntRate` | TField | No | Definition of the largest possible interest rate for the currency. No input indicates that there is no maximum rate. Standard Rate Format. Optional input. Should only be allowed if the key begins 01. |
| 12 | `PI.LOCAL.ROUTINE` | `PeriodicInterest_LocalRoutine` |  |  |  |
| 13 | `PI.USE.LAST.WRKNG.DAY` | `PeriodicInterest_UseLastWrkngDay` | TField |  | If this field is set to &apos;Y&apos; and rest period is defined in &apos;M&apos;onths then the Rest date will be derived as Working day if the actual date falls on an holiday. This is a NOCHANGE field. Validation Rules:It can contain Y or N |
| 14 | `PI.APPLICATION` | `PeriodicInterest_Application` |  |  |  |
| 15 | `PI.HIST.CO.CODE` | `PeriodicInterest_HistCoCode` |  |  |  |
| 16 | `PI.HIST.DATE` | `PeriodicInterest_HistDate` |  |  |  |
| 17 | `PI.HIST.NO` | `PeriodicInterest_HistNo` |  |  |  |
| 18 | `PI.LOCAL.REF` | `PeriodicInterest_LocalRef` |  |  |  |
| 19 | `PI.OVERRIDE` | `PeriodicInterest_Override` |  |  |  |
| 20 | `PI.RECORD.STATUS` | `PeriodicInterest_RecordStatus` | String |  |  |
| 21 | `PI.CURR.NO` | `PeriodicInterest_CurrNo` | String |  |  |
| 22 | `PI.INPUTTER` | `PeriodicInterest_Inputter` |  |  |  |
| 23 | `PI.DATE.TIME` | `PeriodicInterest_DateTime` |  |  |  |
| 24 | `PI.AUTHORISER` | `PeriodicInterest_Authoriser` | String |  |  |
| 25 | `PI.CO.CODE` | `PeriodicInterest_CoCode` | String |  |  |
| 26 | `PI.DEPT.CODE` | `PeriodicInterest_DeptCode` | String |  |  |
| 27 | `PI.AUDITOR.CODE` | `PeriodicInterest_AuditorCode` | String |  |  |
| 28 | `PI.AUDIT.DATE.TIME` | `PeriodicInterest_AuditDateTime` | String |  |  |
| 29 | `PI.RFR.RATE` | `PeriodicInterest_RfrRate` | TField |  | Risk free rate can be specified here. Validation rule: Inputtable field.Should be a valid T24 rate. |
| 30 | `PI.RFR.DATE.RECD` | `PeriodicInterest_RfrDateRecd` | TField |  | This field holds the date on which RFR rate is received. If date is not specified , will be defaulted to Today. Validation rule: Should be a valid T24 date. Date should not be greater than Today. |
