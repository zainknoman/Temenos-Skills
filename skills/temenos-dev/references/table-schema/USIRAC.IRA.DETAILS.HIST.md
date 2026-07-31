# USIRAC.IRA.DETAILS.HIST — Table Schema

> Source: `INSERTS/I_F.USIRAC.IRA.DETAILS.HIST` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IRA.DETAILS.HIST.IRA.TYPE` | `UsiracIraDetailsHist_IraType` | TField |  | Type of the IRA record. Updated from the Account Title of the IRA Text Field |
| 2 | `IRA.DETAILS.HIST.CONTRIBUTION` | `UsiracIraDetailsHist_Contribution` | TField |  | Shows the IRA contribution made for the current year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the contribution transactions made to IRA for the current year |
| 3 | `IRA.DETAILS.HIST.PREV.CONTRIBUTION` | `UsiracIraDetailsHist_PrevContribution` | TField |  | Shows the IRA contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the contribution transactions made to IRA for the previous year |
| 4 | `IRA.DETAILS.HIST.ROLLOVER` | `UsiracIraDetailsHist_Rollover` | TField |  | Shows the rollover contribution made for the year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the rollover transactions made to IRA for the current year |
| 5 | `IRA.DETAILS.HIST.PREV.ROLLOVER` | `UsiracIraDetailsHist_PrevRollover` | TField |  | Shows the IRA rollover contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the rollover transactions made to IRA for the previous year |
| 6 | `IRA.DETAILS.HIST.RECHARACTERIZATION` | `UsiracIraDetailsHist_Recharacterization` | TField |  | Shows the recharacterization contribution made for the year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the recharacterization transactions made to IRA for the current year |
| 7 | `IRA.DETAILS.HIST.PREV.RECHARACTERIZATION` | `UsiracIraDetailsHist_PrevRecharacterization` | TField |  | Shows the IRA recharacterization contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the recharacterization transactions made to IRA for the previous year |
| 8 | `IRA.DETAILS.HIST.CONVERSION` | `UsiracIraDetailsHist_Conversion` | TField |  | Shows the conversion contribution made for the year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the conversion transactions made to IRA for the current year |
| 9 | `IRA.DETAILS.HIST.PREV.CONVERSION` | `UsiracIraDetailsHist_PrevConversion` | TField |  | Shows the IRA conversion contribution made for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the conversion transactions made to IRA for the previous year |
| 10 | `IRA.DETAILS.HIST.PREV.DEPOSITS` | `UsiracIraDetailsHist_PrevDeposits` | TField |  | Shows the deposits made to the IRA for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the current year Value in this field is cleared during year end cob |
| 11 | `IRA.DETAILS.HIST.EMPLOYER.DEPOSITS` | `UsiracIraDetailsHist_EmployerDeposits` | TField |  | Shows the deposits made to the IRA by the employer for the current year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the current year when the employer flag is set to Yes |
| 12 | `IRA.DETAILS.HIST.PREV.EMP.DEPOSITS` | `UsiracIraDetailsHist_PrevEmpDeposits` | TField |  | Shows the deposits made to the IRA by the employer for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the previous year when the employer flag is set to Yes |
| 13 | `IRA.DETAILS.HIST.PREV.EMP.CONTRIB` | `UsiracIraDetailsHist_PrevEmpContrib` | TField |  | Shows the deposits made to the IRA by the employer for the previous year Standard T24 AMOUNT field Defaulted or value added with CREDIT.AMOUNT from the all the deposit transactions made to IRA for the previous year when the employer flag is set to Yes Value in this field is cleared during year end cob |
| 14 | `IRA.DETAILS.HIST.RMD` | `UsiracIraDetailsHist_Rmd` | TField |  | The Required Minimum Distribution of the IRA The field is updated in year end cob after the required begin date Standard T24 AMOUNT field |
| 15 | `IRA.DETAILS.HIST.RMD.DATE` | `UsiracIraDetailsHist_RmdDate` | TField |  | shows the IRA participants required begin date Standard T24 Date format Default date should be equal to REQ.BEGIN.AGE parameterized age of IRA participant For example REQ.BEGIN.AGE = 70.5 DATE.OF.BIRTH = 27 NOV 1950 SYSTEM.DATE = 27 MAR 2013 So required begin date would be defaulted with 27 MAY 2021 That is IRA participants 70.5 years of age |
| 16 | `IRA.DETAILS.HIST.WITHHOLD.DATE` | `UsiracIraDetailsHist_WithholdDate` | TField |  |  |
| 17 | `IRA.DETAILS.HIST.QCD.AMOUNT` | `UsiracIraDetailsHist_QcdAmount` | TField |  |  |
| 18 | `IRA.DETAILS.HIST.TRUSTEE.TRF` | `UsiracIraDetailsHist_TrusteeTrf` | TField |  |  |
| 19 | `IRA.DETAILS.HIST.TXN.REFERENCE` | `UsiracIraDetailsHist_TxnReference` |  |  |  |
| 20 | `IRA.DETAILS.HIST.CONTRIBUTION.TYPE` | `UsiracIraDetailsHist_ContributionType` |  |  |  |
| 21 | `IRA.DETAILS.HIST.PRIOR.YEAR` | `UsiracIraDetailsHist_PriorYear` |  |  |  |
| 22 | `IRA.DETAILS.HIST.EMPLOYER.IND` | `UsiracIraDetailsHist_EmployerInd` |  |  |  |
| 23 | `IRA.DETAILS.HIST.LOCATION` | `UsiracIraDetailsHist_Location` |  |  |  |
| 24 | `IRA.DETAILS.HIST.SELF.CERTIFIED` | `UsiracIraDetailsHist_SelfCertified` |  |  |  |
| 25 | `IRA.DETAILS.HIST.DISASTER.CODE` | `UsiracIraDetailsHist_DisasterCode` |  |  |  |
| 26 | `IRA.DETAILS.HIST.RESERVED.2` | `UsiracIraDetailsHist_Reserved2` |  |  |  |
| 27 | `IRA.DETAILS.HIST.RESERVED.1` | `UsiracIraDetailsHist_Reserved1` |  |  |  |
| 28 | `IRA.DETAILS.HIST.POSTPONED.ROLLOVER` | `UsiracIraDetailsHist_PostponedRollover` |  |  |  |
