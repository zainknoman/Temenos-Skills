# ID.CONTRACT.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.CONTRACT.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.ICD.PROFIT.LOSS.CAT` | `IdContractDetails_ProfitLossCat` | TField |  | Field contains the profit and loss category for which entry is generated Validation Rules: 1. Must be a valid record from the table CATEGORY. 2. Valid Internal category ranging from 50000 to 69999. 3. This is a NOINPUT field. |
| 2 | `ID.ICD.BOOKING.YR.MONTH` | `IdContractDetails_BookingYrMonth` | TField |  | Field contains the year and month details on which entry is generated. This field value is normally first 6 digits of the BOOKING.DATE field value. Validation Rules: 1. This is a NOINPUT field |
| 3 | `ID.ICD.CONTRACT.CAT` | `IdContractDetails_ContractCat` | TField |  | Field contains the contract/arrangement category code. Validation Rules: 1. Must be a valid record from the table CATEGORY. 2. Valid category ranging from 1000 to 49999. 3. This is a NOINPUT field. |
| 4 | `ID.ICD.ENTRY.REF` | `IdContractDetails_EntryRef` |  |  |  |
