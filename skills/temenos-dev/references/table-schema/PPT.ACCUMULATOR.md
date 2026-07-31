# PPT.ACCUMULATOR — Table Schema

> Source: `INSERTS/I_F.PPT.ACCUMULATOR` in `PP_RiskFilterService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTAR.RiskFilterConditionID` | `PptAccumulator_Riskfilterconditionid` | TField |  | Unique ID to identify the filter and also used to store the condition accumulator. This field can hold upto 65 alphanumeric characters and the value is not editable by the user. |
| 2 | `PPTAR.CompanyID` | `PptAccumulator_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 3 | `PPTAR.Day` | `PptAccumulator_Day` |  |  |  |
| 4 | `PPTAR.DailyExhaustedAmountLimit` | `PptAccumulator_Dailyexhaustedamountlimit` |  |  |  |
| 5 | `PPTAR.WeeklyExhaustedAmountLimit` | `PptAccumulator_Weeklyexhaustedamountlimit` |  |  |  |
| 6 | `PPTAR.MonthlyExhaustedAmountLimit` | `PptAccumulator_Monthlyexhaustedamountlimit` |  |  |  |
| 7 | `PPTAR.DailyExhaustedCountLimit` | `PptAccumulator_Dailyexhaustedcountlimit` |  |  |  |
| 8 | `PPTAR.WeeklyExhaustedCountLimit` | `PptAccumulator_Weeklyexhaustedcountlimit` |  |  |  |
| 9 | `PPTAR.MonthlyExhaustedCountLimit` | `PptAccumulator_Monthlyexhaustedcountlimit` |  |  |  |
