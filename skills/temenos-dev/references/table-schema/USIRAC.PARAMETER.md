# USIRAC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USIRAC.PARAMETER` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IRAC.DESCRIPTION` | `UsiracParameter_Description` | TField | Yes | Description of the record Mandatory Field Text Field |
| 2 | `IRAC.MAX.CONTRIB` | `UsiracParameter_MaxContrib` | TField | Yes | This field specifies the maximum contribution amount for participant who are equal to or less than 49 years old Mandatory Field Standard T24 AMOUNT field Text Field For example 5500.00 |
| 3 | `IRAC.MAX.CONTRIB.50` | `UsiracParameter_MaxContrib50` | TField | Yes | This field specifies the maximum contribution amount for participant who are equal to or greater than 50 years old Mandatory Field Standard T24 AMOUNT field Text Field For example 6500.00 |
| 4 | `IRAC.EMP.MAX.CONT` | `UsiracParameter_EmpMaxCont` | TField | No | This field specifies the maximum contribution amount for employee participant who are equal to or less than 49 years old. This field is applicable only for SIMPLE IRA Optional Field Standard T24 AMOUNT field Text Field For example 12000.00 |
| 5 | `IRAC.EMP.MAX.CONT.50` | `UsiracParameter_EmpMaxCont50` | TField | No | This field specifies the maximum contribution amount for employee participant who are equal to or greater than 50 years old. This field is applicable only for SIMPLE IRA Optional Field Standard T24 AMOUNT field Text Field For example 14500.00 |
| 6 | `IRAC.CONTRB.END.DATE` | `UsiracParameter_ContrbEndDate` | TField | Yes | This field shows the contribution deadline for the previous year IRA subscription Mandatory Field Standard T24 DATE field Text Field in format MMDD For example 09/15 |
| 7 | `IRAC.CONTRIB.CONCES` | `UsiracParameter_ContribConces` | TField | Yes | This field shows the previous year contribution deadline Mandatory Field Standard T24 DATE field Text Field in format MMDD For example 09/18 |
| 8 | `IRAC.REQ.BEGIN.AGE` | `UsiracParameter_ReqBeginAge` | TField | No | This field will indicate the minimum required age to withdraw from IRA accounts Optional Field Text Field Including 2 decimal points For example 70.5. or 55.10 |
| 9 | `IRAC.WITHDRAWAL.AGE` | `UsiracParameter_WithdrawalAge` | TField | Yes | This field shows the withdrawal age limit for normal withdrawals Mandatory Field Standard T24 DATE field Text Field For example 15th APR 2013 |
| 10 | `IRAC.PY.MAX.CONTR` | `UsiracParameter_PyMaxContr` | TField | No | This amount, dictated by the IRS, determine the maximum a person who is equal to or less than 49 years old can contribute in a given tax year. Optional Field Standard T24 Amount field Text Field For example 6500.00 |
| 11 | `IRAC.PY.MAX.CONTR.50` | `UsiracParameter_PyMaxContr50` | TField | No | This amount, dictated by the IRS, determine the maximum a person who is equal to or greater than 50 years old can contribute in a given tax year. Optional Field Standard T24 Amount field Text Field For example 6500.00 |
| 12 | `IRAC.PY.EMP.MAX.CONTR` | `UsiracParameter_PyEmpMaxContr` | TField | No | This amount, dictated by the IRS, determine the maximum an employee who is equal to or less than 49 years old can contribute in a given tax year. Optional Field Standard T24 Amount field Text Field For example 6500.00 |
| 13 | `IRAC.PY.EMP.MAX.CONTR.50` | `UsiracParameter_PyEmpMaxContr50` | TField | No | This amount, dictated by the IRS, determine the maximum an employee who is equal to or greater than 50 years old can contribute in a given tax year. Optional Field Standard T24 Amount field Text Field For example 6500.00 |
| 14 | `IRAC.RMD.NOTICE.PREF` | `UsiracParameter_RmdNoticePref` | TField |  | This new field allows the bank to determine per plan what notice will be provided per plan with valid values of: Account Plan |
| 15 | `IRAC.RMD.CALC.FREQ` | `UsiracParameter_RmdCalcFreq` | TField |  | Determines the frequency the RMD calculation occurs. |
| 16 | `IRAC.INH.RMD.EXP.NOTICE` | `UsiracParameter_InhRmdExpNotice` | TField |  | Indicates the number of days prior to the anniversary date in which a notice should be delivered to the customer that their 5 year or 10 year distribution should be taken. Numeric Value; up to 2 digits. |
| 17 | `IRAC.RESERVED.2` | `UsiracParameter_Reserved2` | TField |  |  |
| 18 | `IRAC.RESERVED.1` | `UsiracParameter_Reserved1` | TField |  |  |
| 19 | `IRAC.OVERRIDE` | `UsiracParameter_Override` |  |  |  |
| 20 | `IRAC.RECORD.STATUS` | `UsiracParameter_RecordStatus` | String |  |  |
| 21 | `IRAC.CURR.NO` | `UsiracParameter_CurrNo` | String |  |  |
| 22 | `IRAC.INPUTTER` | `UsiracParameter_Inputter` |  |  |  |
| 23 | `IRAC.DATE.TIME` | `UsiracParameter_DateTime` |  |  |  |
| 24 | `IRAC.AUTHORISER` | `UsiracParameter_Authoriser` | String |  |  |
| 25 | `IRAC.CO.CODE` | `UsiracParameter_CoCode` | String |  |  |
| 26 | `IRAC.DEPT.CODE` | `UsiracParameter_DeptCode` | String |  |  |
| 27 | `IRAC.AUDITOR.CODE` | `UsiracParameter_AuditorCode` | String |  |  |
| 28 | `IRAC.AUDIT.DATE.TIME` | `UsiracParameter_AuditDateTime` | String |  |  |
