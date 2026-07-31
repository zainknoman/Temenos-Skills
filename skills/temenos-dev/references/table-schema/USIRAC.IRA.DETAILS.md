# USIRAC.IRA.DETAILS — Table Schema

> Source: `INSERTS/I_F.USIRAC.IRA.DETAILS` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IRA.DETAILS.IRA.TYPE` | `UsiracIraDetails_IraType` | TField |  | Type of the IRA record. Updated from the Account Title of the IRA Text Field |
| 2 | `IRA.DETAILS.CONTRIBUTION` | `UsiracIraDetails_Contribution` | TField |  | Shows the IRA contribution made for the current year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the contribution transactions made to IRA for the current year |
| 3 | `IRA.DETAILS.PREV.CONTRIBUTION` | `UsiracIraDetails_PrevContribution` | TField |  | Shows the IRA contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the contribution transactions made to IRA for the previous year |
| 4 | `IRA.DETAILS.ROLLOVER` | `UsiracIraDetails_Rollover` | TField |  | Shows the rollover contribution made for the year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the rollover transactions made to IRA for the current year |
| 5 | `IRA.DETAILS.PREV.ROLLOVER` | `UsiracIraDetails_PrevRollover` | TField |  | Shows the IRA rollover contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the rollover transactions made to IRA for the previous year |
| 6 | `IRA.DETAILS.RECHARACTERIZATION` | `UsiracIraDetails_Recharacterization` | TField |  | Shows the recharacterization contribution made for the year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the recharacterization transactions made to IRA for the current year |
| 7 | `IRA.DETAILS.PREV.RECHARACTERIZATION` | `UsiracIraDetails_PrevRecharacterization` | TField |  | Shows the IRA recharacterization contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the recharacterization transactions made to IRA for the previous year |
| 8 | `IRA.DETAILS.CONVERSION` | `UsiracIraDetails_Conversion` | TField |  | Shows the conversion contribution made for the year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the conversion transactions made to IRA for the current year |
| 9 | `IRA.DETAILS.PREV.CONVERSION` | `UsiracIraDetails_PrevConversion` | TField |  | Shows the IRA conversion contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the conversion transactions made to IRA for the previous year |
| 10 | `IRA.DETAILS.PREV.DEPOSITS` | `UsiracIraDetails_PrevDeposits` | TField |  | Shows the deposits made to the IRA for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the current year Value in this field is cleared during year end cob |
| 11 | `IRA.DETAILS.EMPLOYER.DEPOSITS` | `UsiracIraDetails_EmployerDeposits` | TField |  | Shows the deposits made to the IRA by the employer for the current year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the current year when the employer flag is set to Yes |
| 12 | `IRA.DETAILS.PREV.EMP.DEPOSITS` | `UsiracIraDetails_PrevEmpDeposits` | TField |  | Shows the deposits made to the IRA by the employer for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the previous year when the employer flag is set to Yes |
| 13 | `IRA.DETAILS.PREV.EMP.CONTRIB` | `UsiracIraDetails_PrevEmpContrib` | TField |  | Shows the deposits made to the IRA by the employer for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the previous year when the employer flag is set to Yes Value in this field is cleared during year end cob |
| 14 | `IRA.DETAILS.RMD` | `UsiracIraDetails_Rmd` | TField |  | The Required Minimum Distribution of the IRA The field is updated in year end cob after the required begin date Standard T24 AMOUNT field |
| 15 | `IRA.DETAILS.RMD.DATE` | `UsiracIraDetails_RmdDate` | TField |  | shows the IRA participants required begin date Standard T24 Date format Default date should be equal to REQ.BEGIN.AGE parameterized age of IRA participant For example REQ.BEGIN.AGE = 70.5 DATE.OF.BIRTH = 27 NOV 1950 SYSTEM.DATE = 27 MAR 2013 So required begin date would be defaulted with 27 MAY 2021 That is IRA participants 70.5 years of age |
| 16 | `IRA.DETAILS.WITHHOLD.DATE` | `UsiracIraDetails_WithholdDate` | TField |  |  |
| 17 | `IRA.DETAILS.QCD.AMOUNT` | `UsiracIraDetails_QcdAmount` | TField |  |  |
| 18 | `IRA.DETAILS.TRUSTEE.TRF` | `UsiracIraDetails_TrusteeTrf` | TField |  |  |
| 19 | `IRA.DETAILS.TXN.REFERENCE` | `UsiracIraDetails_TxnReference` |  |  |  |
| 20 | `IRA.DETAILS.CONTRIBUTION.TYPE` | `UsiracIraDetails_ContributionType` |  |  |  |
| 21 | `IRA.DETAILS.PRIOR.YEAR` | `UsiracIraDetails_PriorYear` |  |  |  |
| 22 | `IRA.DETAILS.EMPLOYER.IND` | `UsiracIraDetails_EmployerInd` |  |  |  |
| 23 | `IRA.DETAILS.LOCATION` | `UsiracIraDetails_Location` |  |  |  |
| 24 | `IRA.DETAILS.SELF.CERTIFIED` | `UsiracIraDetails_SelfCertified` |  |  |  |
| 25 | `IRA.DETAILS.DISASTER.CODE` | `UsiracIraDetails_DisasterCode` |  |  |  |
| 26 | `IRA.DETAILS.RESERVED.1` | `UsiracIraDetails_Reserved1` |  |  |  |
| 27 | `IRA.DETAILS.POSTPONED.ROLLOVER` | `UsiracIraDetails_PostponedRollover` |  |  |  |
