# PERIODIC.COMMISSION — Table Schema

> Source: `INSERTS/I_F.PERIODIC.COMMISSION` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PC.DESCRIPTION` | `PeriodicCommission_Description` |  |  |  |
| 2 | `PC.SHORT.DESCR` | `PeriodicCommission_ShortDescr` |  |  |  |
| 3 | `PC.CALCULATION.TYPE` | `PeriodicCommission_CalculationType` | TField | Yes | Specifies the calculation type to be used Level or Band. Mandatory field |
| 4 | `PC.UPTO.PERIOD` | `PeriodicCommission_UptoPeriod` |  |  |  |
| 5 | `PC.COMMISSION.CODE` | `PeriodicCommission_CommissionCode` |  |  |  |
| 6 | `PC.MIN.COMM.PERIOD` | `PeriodicCommission_MinCommPeriod` | TField |  | Minimum Number of days for which the commission is calculated. E.g if tenure of contract is 20 days and minimum period is defined as 30 days then commission should be calculated for 30 days. |
| 7 | `PC.GRACE.PERIOD` | `PeriodicCommission_GracePeriod` | TField |  | Number of grace days for which commission will not be applied defined as rest period. E,g if tenure of contract is 92 days and if there are 2 bands defined UPTO � 90 Days UPTO � REST If grace period is 2 days then commission will be calculated for 90 days. |
| 8 | `PC.COMM.CALC.BASE` | `PeriodicCommission_CommCalcBase` | TField | Yes | Calculation base using which commission will be calculated. Original - Original principal amount Outstanding � Current outstanding principal amount Mandatory field |
| 9 | `PC.RESERVED.5` | `PeriodicCommission_Reserved5` | TField |  |  |
| 10 | `PC.RESERVED.4` | `PeriodicCommission_Reserved4` | TField |  |  |
| 11 | `PC.RESERVED.3` | `PeriodicCommission_Reserved3` | TField |  |  |
| 12 | `PC.RESERVED.2` | `PeriodicCommission_Reserved2` | TField |  |  |
| 13 | `PC.RESERVED.1` | `PeriodicCommission_Reserved1` | TField |  |  |
| 14 | `PC.RECORD.STATUS` | `PeriodicCommission_RecordStatus` | String |  |  |
| 15 | `PC.CURR.NO` | `PeriodicCommission_CurrNo` | String |  |  |
| 16 | `PC.INPUTTER` | `PeriodicCommission_Inputter` |  |  |  |
| 17 | `PC.DATE.TIME` | `PeriodicCommission_DateTime` |  |  |  |
| 18 | `PC.AUTHORISER` | `PeriodicCommission_Authoriser` | String |  |  |
| 19 | `PC.CO.CODE` | `PeriodicCommission_CoCode` | String |  |  |
| 20 | `PC.DEPT.CODE` | `PeriodicCommission_DeptCode` | String |  |  |
| 21 | `PC.AUDITOR.CODE` | `PeriodicCommission_AuditorCode` | String |  |  |
| 22 | `PC.AUDIT.DATE.TIME` | `PeriodicCommission_AuditDateTime` | String |  |  |
