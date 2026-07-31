# ID.WEIGHTED.BALANCE.WRK — Table Schema

> Source: `INSERTS/I_F.ID.WEIGHTED.BALANCE.WRK` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IWB.TOTAL.BALANCE` | `IdWeightedBalanceWrk_TotalBalance` | TField |  |  |
| 2 | `ID.IWB.WEIGHTED.BALANCE` | `IdWeightedBalanceWrk_WeightedBalance` | TField |  |  |
| 3 | `ID.IWB.NON.INVESTED.BALANCE` | `IdWeightedBalanceWrk_NonInvestedBalance` | TField |  |  |
| 4 | `ID.IWB.EXCLUDED.BALANCE` | `IdWeightedBalanceWrk_ExcludedBalance` | TField |  |  |
| 5 | `ID.IWB.EM.EXCLUDED.BALANCE` | `IdWeightedBalanceWrk_EmExcludedBalance` | TField |  |  |
| 6 | `ID.IWB.RESERVED.9` | `IdWeightedBalanceWrk_Reserved9` | TField |  |  |
| 7 | `ID.IWB.RESERVED.8` | `IdWeightedBalanceWrk_Reserved8` | TField |  |  |
| 8 | `ID.IWB.RESERVED.7` | `IdWeightedBalanceWrk_Reserved7` | TField |  |  |
| 9 | `ID.IWB.RESERVED.6` | `IdWeightedBalanceWrk_Reserved6` | TField |  |  |
| 10 | `ID.IWB.RESERVED.5` | `IdWeightedBalanceWrk_Reserved5` | TField |  |  |
| 11 | `ID.IWB.RESERVED.4` | `IdWeightedBalanceWrk_Reserved4` | TField |  |  |
| 12 | `ID.IWB.RESERVED.3` | `IdWeightedBalanceWrk_Reserved3` | TField |  |  |
| 13 | `ID.IWB.RESERVED.2` | `IdWeightedBalanceWrk_Reserved2` | TField |  |  |
| 14 | `ID.IWB.RESERVED.1` | `IdWeightedBalanceWrk_Reserved1` | TField |  |  |
