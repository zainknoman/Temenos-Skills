# ID.CATEG.ENT.DETAILS.WRK — Table Schema

> Source: `INSERTS/I_F.ID.CATEG.ENT.DETAILS.WRK` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.CEW.PROFIT.LOSS.CAT` | `IdCategEntDetailsWrk_ProfitLossCat` |  |  |  |
| 2 | `ID.CEW.BOOKING.YR.MONTH` | `IdCategEntDetailsWrk_BookingYrMonth` |  |  |  |
| 3 | `ID.CEW.CONTRACT.CAT` | `IdCategEntDetailsWrk_ContractCat` |  |  |  |
| 4 | `ID.CEW.BOOKING.DATE` | `IdCategEntDetailsWrk_BookingDate` |  |  |  |
| 5 | `ID.CEW.OUR.REFERENCE` | `IdCategEntDetailsWrk_OurReference` |  |  |  |
| 6 | `ID.CEW.VALUE.DATE` | `IdCategEntDetailsWrk_ValueDate` |  |  |  |
| 7 | `ID.CEW.AMOUNT.LCY` | `IdCategEntDetailsWrk_AmountLcy` |  |  |  |
| 8 | `ID.CEW.CURRENCY` | `IdCategEntDetailsWrk_Currency` |  |  |  |
| 9 | `ID.CEW.AMOUNT.FCY` | `IdCategEntDetailsWrk_AmountFcy` |  |  |  |
| 10 | `ID.CEW.CONTRACT.TYPE` | `IdCategEntDetailsWrk_ContractType` |  |  |  |
| 11 | `ID.CEW.CATEG.ENTRY.REF` | `IdCategEntDetailsWrk_CategEntryRef` |  |  |  |
