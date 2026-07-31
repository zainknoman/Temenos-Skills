# ID.PDS.DISTRIB.DETAILS — Table Schema

> Source: `INSERTS/I_F.ID.PDS.DISTRIB.DETAILS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.PDD.DISTRIB.ID` | `IdPdsDistribDetails_DistribId` |  |  |  |
| 2 | `ID.PDD.DISTRIB.DATE` | `IdPdsDistribDetails_DistribDate` |  |  |  |
| 3 | `ID.PDD.RESERVED.10` | `IdPdsDistribDetails_Reserved10` |  |  |  |
| 4 | `ID.PDD.RESERVED.9` | `IdPdsDistribDetails_Reserved9` |  |  |  |
| 5 | `ID.PDD.RESERVED.8` | `IdPdsDistribDetails_Reserved8` |  |  |  |
| 6 | `ID.PDD.RESERVED.7` | `IdPdsDistribDetails_Reserved7` |  |  |  |
| 7 | `ID.PDD.RESERVED.6` | `IdPdsDistribDetails_Reserved6` |  |  |  |
| 8 | `ID.PDD.DEPOSIT.BAND` | `IdPdsDistribDetails_DepositBand` |  |  |  |
| 9 | `ID.PDD.RESERVED.4` | `IdPdsDistribDetails_Reserved4` | TField |  |  |
| 10 | `ID.PDD.RESERVED.3` | `IdPdsDistribDetails_Reserved3` | TField |  |  |
| 11 | `ID.PDD.RESERVED.2` | `IdPdsDistribDetails_Reserved2` | TField |  |  |
| 12 | `ID.PDD.RESERVED.1` | `IdPdsDistribDetails_Reserved1` | TField |  |  |
