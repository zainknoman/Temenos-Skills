# IC.CHARGE — Table Schema

> Source: `INSERTS/I_F.IC.CHARGE` in `IC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CHG.IC.CHG.PRODUCT` | `IcCharge_IcChgProduct` |  |  |  |
| 2 | `IC.CHG.CAL.STEP.PERIOD` | `IcCharge_CalStepPeriod` |  |  |  |
| 3 | `IC.CHG.CHRG.FREQUENCY` | `IcCharge_ChrgFrequency` |  |  |  |
| 4 | `IC.CHG.WAIVE.CHARGE` | `IcCharge_WaiveCharge` |  |  |  |
| 5 | `IC.CHG.CHRG.EFF.DATE` | `IcCharge_ChrgEffDate` |  |  |  |
| 6 | `IC.CHG.ACCRUE.AMORT` | `IcCharge_AccrueAmort` |  |  |  |
| 7 | `IC.CHG.AMORT.TYPE` | `IcCharge_AmortType` |  |  |  |
| 8 | `IC.CHG.AMORT.DIFF.PL` | `IcCharge_AmortDiffPl` |  |  |  |
| 9 | `IC.CHG.AMORT.DIF.ACCT` | `IcCharge_AmortDifAcct` |  |  |  |
| 10 | `IC.CHG.AMORT.RMN.ACCT` | `IcCharge_AmortRmnAcct` |  |  |  |
| 11 | `IC.CHG.AMORT.ADJUST` | `IcCharge_AmortAdjust` |  |  |  |
| 12 | `IC.CHG.END.DATE` | `IcCharge_EndDate` |  |  |  |
| 13 | `IC.CHG.RESERVED.13` | `IcCharge_Reserved13` |  |  |  |
| 14 | `IC.CHG.RESERVED.12` | `IcCharge_Reserved12` |  |  |  |
| 15 | `IC.CHG.RESERVED.11` | `IcCharge_Reserved11` |  |  |  |
| 16 | `IC.CHG.RESERVED.10` | `IcCharge_Reserved10` |  |  |  |
| 17 | `IC.CHG.RESERVED.9` | `IcCharge_Reserved9` |  |  |  |
| 18 | `IC.CHG.WAIVE.ALL` | `IcCharge_WaiveAll` | TField | No | Optional input allowed values "YES" or "NO". This field defines whether the generic charges need to be waived. Input allowed only for IC.CHARGE defined for an account. Input into other fields is not allowed when WAIVE.ALL has value "YES". Validation Rules: If WAIVE.ALL and WAIVE.CHARGE both set as "YES", WAIVE.ALL will take the predence. |
| 19 | `IC.CHG.EB.ACCRUAL.PARAM` | `IcCharge_EbAccrualParam` | TField |  | Oprional Input. Indicates whether non standard accrual / amortisation processing is required. Normal accrual/amortisation processing will begin on the period start date and finish 1 day before the period end date, i.e. no accrual takes place on the last day. |
| 20 | `IC.CHG.RESERVED.8` | `IcCharge_Reserved8` | TField |  |  |
| 21 | `IC.CHG.RESERVED.7` | `IcCharge_Reserved7` | TField |  |  |
| 22 | `IC.CHG.RESERVED.6` | `IcCharge_Reserved6` | TField |  |  |
| 23 | `IC.CHG.RESERVED.5` | `IcCharge_Reserved5` | TField |  |  |
| 24 | `IC.CHG.RESERVED.4` | `IcCharge_Reserved4` | TField |  |  |
| 25 | `IC.CHG.RESERVED.3` | `IcCharge_Reserved3` | TField |  |  |
| 26 | `IC.CHG.RESERVED.2` | `IcCharge_Reserved2` | TField |  |  |
| 27 | `IC.CHG.RESERVED.1` | `IcCharge_Reserved1` | TField |  |  |
| 28 | `IC.CHG.LOCAL.REF` | `IcCharge_LocalRef` |  |  |  |
| 29 | `IC.CHG.OVERRIDE` | `IcCharge_Override` |  |  |  |
| 30 | `IC.CHG.RECORD.STATUS` | `IcCharge_RecordStatus` | String |  |  |
| 31 | `IC.CHG.CURR.NO` | `IcCharge_CurrNo` | String |  |  |
| 32 | `IC.CHG.INPUTTER` | `IcCharge_Inputter` |  |  |  |
| 33 | `IC.CHG.DATE.TIME` | `IcCharge_DateTime` |  |  |  |
| 34 | `IC.CHG.AUTHORISER` | `IcCharge_Authoriser` | String |  |  |
| 35 | `IC.CHG.CO.CODE` | `IcCharge_CoCode` | String |  |  |
| 36 | `IC.CHG.DEPT.CODE` | `IcCharge_DeptCode` | String |  |  |
| 37 | `IC.CHG.AUDITOR.CODE` | `IcCharge_AuditorCode` | String |  |  |
| 38 | `IC.CHG.AUDIT.DATE.TIME` | `IcCharge_AuditDateTime` | String |  |  |
