# ID.BANDWISE.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.ID.BANDWISE.ACCOUNTS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.IBC.ACTION.ID` | `IdBandwiseAccounts_ActionId` | TField |  |  |
| 2 | `ID.IBC.POOL.REF` | `IdBandwiseAccounts_PoolRef` | TField |  |  |
| 3 | `ID.IBC.CATEGORY` | `IdBandwiseAccounts_Category` | TField |  |  |
| 4 | `ID.IBC.CURRENCY` | `IdBandwiseAccounts_Currency` | TField |  |  |
| 5 | `ID.IBC.DIST.FREQUENCY` | `IdBandwiseAccounts_DistFrequency` | TField |  |  |
| 6 | `ID.IBC.AMOUNT.FROM` | `IdBandwiseAccounts_AmountFrom` | TField |  |  |
| 7 | `ID.IBC.AMOUNT.TO` | `IdBandwiseAccounts_AmountTo` | TField |  |  |
| 8 | `ID.IBC.CONTRACT.REF` | `IdBandwiseAccounts_ContractRef` | TField |  |  |
| 9 | `ID.IBC.RESERVED10` | `IdBandwiseAccounts_Reserved10` | TField |  |  |
| 10 | `ID.IBC.RESERVED.9` | `IdBandwiseAccounts_Reserved9` | TField |  |  |
| 11 | `ID.IBC.RESERVED.8` | `IdBandwiseAccounts_Reserved8` | TField |  |  |
| 12 | `ID.IBC.RESERVED.7` | `IdBandwiseAccounts_Reserved7` | TField |  |  |
| 13 | `ID.IBC.RESERVED.6` | `IdBandwiseAccounts_Reserved6` | TField |  |  |
| 14 | `ID.IBC.RESERVED.5` | `IdBandwiseAccounts_Reserved5` | TField |  |  |
| 15 | `ID.IBC.RESERVED.4` | `IdBandwiseAccounts_Reserved4` | TField |  |  |
| 16 | `ID.IBC.RESERVED.3` | `IdBandwiseAccounts_Reserved3` | TField |  |  |
| 17 | `ID.IBC.RESERVED.2` | `IdBandwiseAccounts_Reserved2` | TField |  |  |
| 18 | `ID.IBC.RESERVED.1` | `IdBandwiseAccounts_Reserved1` | TField |  |  |
