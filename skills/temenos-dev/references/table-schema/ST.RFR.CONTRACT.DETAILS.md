# ST.RFR.CONTRACT.DETAILS — Table Schema

> Source: `INSERTS/I_F.ST.RFR.CONTRACT.DETAILS` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RCD.CONTRACT.ID` | `StRfrContractDetails_ContractId` | TField |  | Refers the ID of the contract who is using the RFR. |
| 2 | `RCD.SYSTEM.ID` | `StRfrContractDetails_SystemId` | TField |  | Refers the System Id of the contract Validation rules: Valid EB.SYSTEM.ID record |
| 3 | `RCD.INTEREST.TYPE` | `StRfrContractDetails_InterestType` | TField |  | Hold the interets Type of the contracct. For AA this should be the interest property. For all other applications it can be defined as required (for example Swaps may wish to use ASSET or LIABILITY or an abbreviation of the same) |
| 4 | `RCD.RFR.NAME` | `StRfrContractDetails_RfrName` | TField |  | Name of the RFR value. |
| 5 | `RCD.PERIOD.START.DATE` | `StRfrContractDetails_PeriodStartDate` | TField |  | Start date for the interest period |
| 6 | `RCD.PERIOD.END.DATE` | `StRfrContractDetails_PeriodEndDate` | TField |  | End date for the interest period. Can be future interest date where referencing the current period. |
| 7 | `RCD.MARGIN.METHOD` | `StRfrContractDetails_MarginMethod` | TField |  | Indicates the Margin method applied for Rate calculation. |
| 8 | `RCD.RFR.YEAR.MONTH` | `StRfrContractDetails_RfrYearMonth` |  |  |  |
