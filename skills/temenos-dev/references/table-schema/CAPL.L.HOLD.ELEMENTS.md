# CAPL.L.HOLD.ELEMENTS — Table Schema

> Source: `INSERTS/I_F.CAPL.L.HOLD.ELEMENTS` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HLD.ELEM.CR.CCY` | `CaplLHoldElements_CrCcy` |  |  |  |
| 2 | `HLD.ELEM.DR.AMOUNT` | `CaplLHoldElements_DrAmount` |  |  |  |
| 3 | `HLD.ELEM.AMOUNT.LCY` | `CaplLHoldElements_AmountLcy` |  |  |  |
| 4 | `HLD.ELEM.AMOUNT.FCY` | `CaplLHoldElements_AmountFcy` |  |  |  |
| 5 | `HLD.ELEM.HOLD.TYPE` | `CaplLHoldElements_HoldType` |  |  |  |
| 6 | `HLD.ELEM.HOLD.CODE` | `CaplLHoldElements_HoldCode` |  |  |  |
| 7 | `HLD.ELEM.HOLD.AMT` | `CaplLHoldElements_HoldAmt` |  |  |  |
| 8 | `HLD.ELEM.HOLD.EXP.DATE` | `CaplLHoldElements_HoldExpDate` |  |  |  |
| 9 | `HLD.ELEM.CUSTOMER` | `CaplLHoldElements_Customer` |  |  |  |
| 10 | `HLD.ELEM.TFS.ACCT.CR` | `CaplLHoldElements_TfsAcctCr` |  |  |  |
| 11 | `HLD.ELEM.TFS.CCY.CR` | `CaplLHoldElements_TfsCcyCr` |  |  |  |
