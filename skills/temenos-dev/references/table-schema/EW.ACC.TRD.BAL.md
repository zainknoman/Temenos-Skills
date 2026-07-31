# EW.ACC.TRD.BAL — Table Schema

> Source: `INSERTS/I_F.EW.ACC.TRD.BAL` in `EW_InitialLoad.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EW.TD.CUSTOMER` | `EwAccTrdBal_Customer` | TField |  |  |
| 2 | `EW.TD.CATEGORY` | `EwAccTrdBal_Category` | TField |  |  |
| 3 | `EW.TD.SHORT.TITLE` | `EwAccTrdBal_ShortTitle` |  |  |  |
| 4 | `EW.TD.MNEMONIC` | `EwAccTrdBal_Mnemonic` | TField |  |  |
| 5 | `EW.TD.POSITION.TYPE` | `EwAccTrdBal_PositionType` | TField |  |  |
| 6 | `EW.TD.CURRENCY` | `EwAccTrdBal_Currency` | TField |  |  |
| 7 | `EW.TD.CURRENCY.MARKET` | `EwAccTrdBal_CurrencyMarket` | TField |  |  |
| 8 | `EW.TD.LIMIT.REF` | `EwAccTrdBal_LimitRef` | TField |  |  |
| 9 | `EW.TD.ACCOUNT.OFFICER` | `EwAccTrdBal_AccountOfficer` | TField |  |  |
| 10 | `EW.TD.OTHER.OFFICER` | `EwAccTrdBal_OtherOfficer` |  |  |  |
| 11 | `EW.TD.COMP.TD.BALANCE` | `EwAccTrdBal_CompTdBalance` | TField |  |  |
