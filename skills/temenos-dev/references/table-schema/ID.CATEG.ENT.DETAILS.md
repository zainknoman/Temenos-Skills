# ID.CATEG.ENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.CATEG.ENT.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.CED.PROFIT.LOSS.CAT` | `IdCategEntDetails_ProfitLossCat` |  |  |  |
| 2 | `ID.CED.BOOKING.YR.MONTH` | `IdCategEntDetails_BookingYrMonth` |  |  |  |
| 3 | `ID.CED.CONTRACT.CAT` | `IdCategEntDetails_ContractCat` |  |  |  |
| 4 | `ID.CED.BOOKING.DATE` | `IdCategEntDetails_BookingDate` |  |  |  |
| 5 | `ID.CED.OUR.REFERENCE` | `IdCategEntDetails_OurReference` |  |  |  |
| 6 | `ID.CED.VALUE.DATE` | `IdCategEntDetails_ValueDate` |  |  |  |
| 7 | `ID.CED.AMOUNT.LCY` | `IdCategEntDetails_AmountLcy` |  |  |  |
| 8 | `ID.CED.CURRENCY` | `IdCategEntDetails_Currency` |  |  |  |
| 9 | `ID.CED.AMOUNT.FCY` | `IdCategEntDetails_AmountFcy` |  |  |  |
| 10 | `ID.CED.CONTRACT.TYPE` | `IdCategEntDetails_ContractType` |  |  |  |
| 11 | `ID.CED.CATEG.ENTRY.REF` | `IdCategEntDetails_CategEntryRef` |  |  |  |
