# POSITION.LWORK.DAY — Table Schema

> Source: `INSERTS/I_F.POSITION.LWORK.DAY` in `AC_CurrencyPosition.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.POS.LW.AMOUNT.1` | `PositionLworkDay_Amount1` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `FX.POS.LW.AMOUNT.2` | `PositionLworkDay_Amount2` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `FX.POS.LW.LCY.EQUIV` | `PositionLworkDay_LcyEquiv` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `FX.POS.LW.APPLIC.ID` | `PositionLworkDay_ApplicId` |  |  |  |
| 5 | `FX.POS.LW.TXN.REF.NO` | `PositionLworkDay_TxnRefNo` |  |  |  |
| 6 | `FX.POS.LW.FWD.REVAL.POSTED` | `PositionLworkDay_FwdRevalPosted` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `FX.POS.LW.SYSTEM.DATE` | `PositionLworkDay_SystemDate` |  |  |  |
| 8 | `FX.POS.LW.SD.AMOUNT.1` | `PositionLworkDay_SdAmount1` |  |  |  |
| 9 | `FX.POS.LW.SD.AMOUNT.2` | `PositionLworkDay_SdAmount2` |  |  |  |
| 10 | `FX.POS.LW.SD.LCY.AMOUNT` | `PositionLworkDay_SdLcyAmount` |  |  |  |
