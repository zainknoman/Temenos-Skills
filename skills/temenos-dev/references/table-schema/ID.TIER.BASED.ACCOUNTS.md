# ID.TIER.BASED.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.ID.TIER.BASED.ACCOUNTS` in `ID_PdsProcess.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.TBA.PDS.ACTION.REF` | `IdTierBasedAccounts_PdsActionRef` | TField |  | This field will hold valid PDS Action Reference. Validation Rules: 1. Valid record in ID.PDS.ACTION Table |
| 2 | `ID.TBA.ARRANGEMENT.REF` | `IdTierBasedAccounts_ArrangementRef` | TField |  | This field will hold valid Arrangement Account Reference. Validation Rules: 1. Valid record in AA.ARRANGEMENT Table |
| 3 | `ID.TBA.TIER.TYPE` | `IdTierBasedAccounts_TierType` | TField |  | Field holds the tier type values BAND or LEVEL based on the corresponding ID.PDS.WEIGHT record Validation Rules: 1. The value should be BAND or LEVEL |
| 4 | `ID.TBA.TIER.TYPE.ID` | `IdTierBasedAccounts_TierTypeId` |  |  |  |
| 5 | `ID.TBA.RESERVED.5` | `IdTierBasedAccounts_Reserved5` |  |  |  |
| 6 | `ID.TBA.RESERVED.4` | `IdTierBasedAccounts_Reserved4` |  |  |  |
| 7 | `ID.TBA.RESERVED.3` | `IdTierBasedAccounts_Reserved3` | TField |  | Reserved for future use |
| 8 | `ID.TBA.RESERVED.2` | `IdTierBasedAccounts_Reserved2` | TField |  | Reserved for future use |
| 9 | `ID.TBA.RESERVED.1` | `IdTierBasedAccounts_Reserved1` | TField |  | Reserved for future use |
